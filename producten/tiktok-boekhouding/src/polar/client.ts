// Kleine client voor de Polar API (ontwerp-betalen.md, punt 4). Elk verzoek gaat via `budget.omhul` en telt dus in de pot
// van 50 van de aanroep, ook een herhaling na 429. Geen SDK: alleen fetch.
//
// Vormen uit de OpenAPI (https://polar.sh/docs/openapi/2026-10.openapi.json, gelezen met curl op 10 nov 2026):
//   GET  /v1/customers/external/{external_id}/state  200 CustomerState, 404 ResourceNotFound ("Customer not found.")
//   POST /v1/checkouts/        body CheckoutProductsCreate (`products` verplicht, `external_customer_id`, `metadata`,
//                              `success_url`, `customer_ip_address`), 201 Checkout (`url`)
//   POST /v1/customer-sessions/  body CustomerSessionCustomerExternalIDCreate (`external_customer_id`, `return_url`),
//                              201 CustomerSession (`customer_portal_url`), 409 AmbiguousExternalCustomerID
//   PATCH /v1/subscriptions/{id}  body SubscriptionCancel (`cancel_at_period_end`), 200 Subscription;
//                              403 AlreadyCanceledSubscription | InactiveSubscription | PaymentNotReady (veld `error`);
//                              404 ResourceNotFound; 409 SubscriptionLocked | SubscriptionNotScheduledToCancel
import { isBudgetOp, type Budget } from "../budget.ts";
import type { D1 } from "../d1/opslag.ts";
import { secondenVan, standUitState, type PolarKlantStand, type StandUitPolar } from "./abonnement.ts";

export const POLAR_VERSIE = "2026-10";
/** Langer wachten dan dit na een 429 doen we niet in de aanroep zelf: dan later opnieuw. */
export const MAX_WACHT_429 = 2;

export interface PolarInstellingen {
  /** `https://api.polar.sh` of `https://sandbox-api.polar.sh` (env POLAR_API). */
  api: string;
  /** Organization Access Token (env POLAR_TOKEN). */
  token: string;
  /** Env POLAR_PRODUCT_ID: het product van €15 per maand. */
  productId: string;
  /** Env POLAR_WEBHOOK_SECRET (`whsec_...`), alleen voor de webhook. */
  webhookSecret: string;
  /** Env POLAR_TERUG_URL: waar de verkoper na de checkout of het portaal terugkomt. Leeg: niet meesturen. */
  terugUrl?: string;
}

export interface PolarDeps {
  instellingen: PolarInstellingen;
  budget: Budget;
  fetchFn?: typeof fetch;
  slaap?: (ms: number) => Promise<void>;
  /** Unix-seconden; voor de `stand` van een opvraging. */
  nu: () => number;
  /** Alleen voor `maakCheckout` (zet `polar_gestart`). D1 telt via `budget.opslagTeller()` in dezelfde pot. */
  db?: D1;
}

/** Fout van Polar of het netwerk. `httpStatus` 0: netwerk of geen antwoord. `code`: het veld `error` uit de body. */
export class PolarFout extends Error {
  readonly httpStatus: number;
  readonly code: string | undefined;
  constructor(bericht: string, httpStatus = 0, code?: string) {
    super(bericht);
    this.name = "PolarFout";
    this.httpStatus = httpStatus;
    this.code = code;
  }
}

/** gelukt: niets meer op te zeggen. later: opnieuw bij de volgende cron. uitgesteld: budget op, niets (meer) verstuurd. */
export type OpzegUitkomst = { uitkomst: "gelukt" } | { uitkomst: "later"; fout: string } | { uitkomst: "uitgesteld" };

export class PolarClient {
  private readonly d: PolarDeps;
  private readonly f: typeof fetch;
  constructor(deps: PolarDeps) {
    this.d = deps;
    this.f = deps.budget.omhul(deps.fetchFn ?? fetch);
  }

  /** Eén verzoek, met één herhaling bij 429 als `Retry-After` hoogstens 2 seconden is. Geeft status en body (JSON of null). */
  private async verzoek(methode: string, pad: string, body?: unknown): Promise<{ status: number; json: any }> {
    const url = this.d.instellingen.api.replace(/\/+$/, "") + pad;
    const init: RequestInit = {
      method: methode,
      headers: {
        authorization: `Bearer ${this.d.instellingen.token}`,
        "polar-version": POLAR_VERSIE,
        accept: "application/json",
        ...(body === undefined ? {} : { "content-type": "application/json" }),
      },
      ...(body === undefined ? {} : { body: JSON.stringify(body) }),
    };
    for (let poging = 0; ; poging++) {
      let r: Response;
      try {
        r = await this.f(url, init);
      } catch (e) {
        if (isBudgetOp(e)) throw e;
        throw new PolarFout(`Polar onbereikbaar: ${String((e as Error)?.message ?? e)}`);
      }
      if (r.status === 429 && poging === 0) {
        // Alleen seconden als getal; ontbreekt de kop (Number(null) is 0!) of is het een datum: opgeven.
        const kop = (r.headers.get("retry-after") ?? "").trim();
        const wacht = /^\d+(\.\d+)?$/.test(kop) ? Number(kop) : NaN;
        if (wacht <= MAX_WACHT_429) {
          await (this.d.slaap ?? ((ms: number) => new Promise<void>((k) => setTimeout(k, ms))))(wacht * 1000);
          continue;
        }
      }
      let json: any = null;
      try {
        json = await r.json();
      } catch {
        json = null;
      }
      return { status: r.status, json };
    }
  }

  private fout(wat: string, a: { status: number; json: any }): PolarFout {
    const code = typeof a.json?.error === "string" ? a.json.error : undefined;
    return new PolarFout(`Polar ${wat}: ${a.status}${code ? ` ${code}` : ""}`, a.status, code);
  }

  private pad(winkel: string) {
    return `/v1/customers/external/${encodeURIComponent(winkel)}/state`;
  }

  /** Customer State ruw; null bij 404 (nooit klant geworden). Gooit PolarFout of BudgetOp. */
  private async state(winkel: string): Promise<PolarKlantStand | null> {
    const a = await this.verzoek("GET", this.pad(winkel));
    if (a.status === 404) return null;
    if (a.status !== 200 || !a.json || typeof a.json !== "object") throw this.fout("customer state", a);
    return a.json as PolarKlantStand;
  }

  /**
   * Stand van het abonnement van deze winkel (punt 2.5 en 4). 404: niet actief. `stand` is het tijdstip van de opvraging
   * in microseconden. Schrijven doet de aanroeper met `schrijfStand` (voorwaardelijk op `stand`). Gooit PolarFout of BudgetOp.
   */
  async standVan(winkel: string): Promise<{ abonnement: StandUitPolar; klant: string | null }> {
    const state = await this.state(winkel);
    return { abonnement: standUitState(state, winkel, this.d.nu() * 1_000_000), klant: typeof state?.id === "string" ? state.id : null };
  }

  /**
   * Checkout voor deze winkel; geeft de `url`. Zet eerst `polar_gestart` (alleen de eerste keer), zodat ontkoppelen ook
   * een betaalde checkout opzegt waarvan de webhook nog niet binnen is. Onbekende of ontkoppelde winkel: fout, geen checkout.
   * `ip`: `CF-Connecting-IP` van de verkoper (btw-bepaling van Polar).
   */
  async maakCheckout(winkel: string, ip?: string): Promise<string> {
    const db = this.d.db;
    if (!db) throw new Error("maakCheckout zonder db");
    this.d.budget.opslagTeller().neem();
    const z = await db
      .prepare(`UPDATE winkels SET polar_gestart = coalesce(polar_gestart, ?) WHERE id = ? AND ontkoppeld_op IS NULL`)
      .bind(this.d.nu(), winkel)
      .run();
    if (z.meta.changes !== 1) throw new Error(`winkel ${winkel} onbekend of ontkoppeld: geen checkout`);
    const i = this.d.instellingen;
    const a = await this.verzoek("POST", "/v1/checkouts/", {
      products: [i.productId],
      external_customer_id: winkel,
      metadata: { winkel },
      ...(i.terugUrl ? { success_url: i.terugUrl } : {}),
      ...(ip ? { customer_ip_address: ip } : {}),
    });
    if (a.status !== 201 && a.status !== 200) throw this.fout("checkout", a);
    if (typeof a.json?.url !== "string") throw new PolarFout("Polar checkout: antwoord zonder url", a.status);
    return a.json.url;
  }

  /** Link naar het klantportaal van Polar (abonnement beheren). Gooit PolarFout of BudgetOp. */
  async portaalLink(winkel: string): Promise<string> {
    const i = this.d.instellingen;
    const a = await this.verzoek("POST", "/v1/customer-sessions/", {
      external_customer_id: winkel,
      ...(i.terugUrl ? { return_url: i.terugUrl } : {}),
    });
    if (a.status !== 201 && a.status !== 200) throw this.fout("customer session", a);
    if (typeof a.json?.customer_portal_url !== "string") throw new PolarFout("Polar customer session: antwoord zonder customer_portal_url", a.status);
    return a.json.customer_portal_url;
  }

  /**
   * Taak `opzeggen` (punt 4): Customer State lezen, dan elk actief abonnement van deze winkel dat nog niet opgezegd is
   * `cancel_at_period_end`. 200, 403 AlreadyCanceledSubscription en 404 zijn gelukt; de rest later. `voor` (unix-seconden,
   * `taken.opzeggen.voor`): abonnementen die daarna begonnen niet opzeggen. Gooit nooit (BudgetOp wordt `uitgesteld`).
   *
   * "Van deze winkel": met `metadata.winkel` gelijk aan de sleutel, of zonder `metadata.winkel` (de klant is per winkel,
   * via `external_customer_id`). Eén met de sleutel van een andere winkel blijft staan.
   */
  async zegOp(winkel: string, voor?: number): Promise<OpzegUitkomst> {
    try {
      const state = await this.state(winkel);
      if (!state) return { uitkomst: "gelukt" };
      const lijst = (Array.isArray(state.active_subscriptions) ? state.active_subscriptions : []).filter((a) => {
        if (!a || typeof a.id !== "string" || a.cancel_at_period_end === true) return false;
        const w = a.metadata?.winkel;
        if (w !== undefined && w !== null && String(w) !== winkel) return false;
        const begin = secondenVan(a.started_at ?? a.created_at);
        return voor === undefined || begin === null || begin <= voor;
      });
      for (const a of lijst) {
        const r = await this.verzoek("PATCH", `/v1/subscriptions/${encodeURIComponent(a.id)}`, { cancel_at_period_end: true });
        if (r.status === 200 || r.status === 404) continue;
        if (r.status === 403 && r.json?.error === "AlreadyCanceledSubscription") continue;
        return { uitkomst: "later", fout: this.fout("opzeggen", r).message };
      }
      return { uitkomst: "gelukt" };
    } catch (e) {
      if (isBudgetOp(e)) return { uitkomst: "uitgesteld" };
      return { uitkomst: "later", fout: String((e as Error)?.message ?? e) };
    }
  }
}
