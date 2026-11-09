// Aanroepen naar de Moneybird API v2.
// Ontwerp: ontwerp-moneybird.md deel 2. Bron: developer.moneybird.com/introduction.md en de OpenAPI.

import { MoneybirdFout, soortVanStatus } from "./fouten.ts";

export const MONEYBIRD_API = "https://moneybird.com/api/v2";
export const MAX_POGINGEN = 3;

export interface MoneybirdClientOpties {
  accessToken: string;
  basisUrl?: string;
  fetchFn?: typeof fetch;
  /** Huidige tijd in seconden; te vervangen in tests. */
  nu?: () => number;
  slaap?: (ms: number) => Promise<void>;
}

export type Methode = "GET" | "POST" | "PATCH" | "DELETE";

/**
 * Wachttijd bij 429. Retry-After is volgens de OpenAPI een tijdstip in Unix-seconden;
 * een kleine waarde lezen we als aantal seconden. Altijd tussen 1 en 60 s.
 */
export function wachttijdMs(retryAfter: string | null, nuSeconden: number): number {
  let s = 5;
  const n = retryAfter === null ? NaN : Number(retryAfter);
  if (Number.isFinite(n)) s = n > 1_000_000_000 ? n - nuSeconden : n;
  return Math.min(60, Math.max(1, s)) * 1000;
}

/** De tekst van Moneybird: `full_message`, of `error` als tekst, of het object als JSON. */
export function foutTekst(json: unknown): string {
  if (typeof json === "string") return json;
  const j = json as any;
  if (typeof j?.full_message === "string") return j.full_message;
  if (typeof j?.error === "string") return j.error;
  return JSON.stringify(j?.error ?? j ?? "");
}

export class MoneybirdClient {
  private readonly o: Required<MoneybirdClientOpties>;

  constructor(opties: MoneybirdClientOpties) {
    this.o = {
      basisUrl: MONEYBIRD_API,
      fetchFn: (...a) => fetch(...a),
      nu: () => Math.floor(Date.now() / 1000),
      slaap: (ms) => new Promise((r) => setTimeout(r, ms)),
      ...opties,
    };
  }

  /**
   * Eén aanroep. `pad` zonder .json, bijvoorbeeld `/123/ledger_accounts`.
   * Herhaalt bij 429 altijd, bij 5xx of netwerkfout alleen bij GET (een herhaalde POST of PATCH kan dubbel boeken).
   */
  async roep<T>(methode: Methode, pad: string, opties: { query?: Record<string, string>; body?: unknown } = {}): Promise<T> {
    const qs = opties.query && Object.keys(opties.query).length ? `?${new URLSearchParams(opties.query).toString()}` : "";
    const url = `${this.o.basisUrl}${pad}.json${qs}`;
    const headers: Record<string, string> = { authorization: `Bearer ${this.o.accessToken}`, accept: "application/json" };
    let body: string | undefined;
    if (opties.body !== undefined) {
      headers["content-type"] = "application/json";
      body = JSON.stringify(opties.body);
    }
    for (let poging = 1; ; poging++) {
      let res: Response | undefined;
      let netwerkFout: Error | undefined;
      try {
        res = await this.o.fetchFn(url, { method: methode, headers, body });
      } catch (e) {
        netwerkFout = e as Error;
      }
      if (res && res.ok) {
        if (res.status === 204) return undefined as T;
        try {
          const tekst = await res.text();
          return (tekst ? JSON.parse(tekst) : undefined) as T;
        } catch (e) {
          // Gelukt bij Moneybird, maar het antwoord is niet te lezen: voor POST en PATCH is de uitkomst dan onzeker.
          netwerkFout = new Error(`antwoord ${res.status} niet te lezen: ${(e as Error).message}`);
          res = undefined;
        }
      }
      let fout: MoneybirdFout;
      if (netwerkFout) {
        fout = new MoneybirdFout("server", `netwerkfout bij Moneybird: ${netwerkFout.message}`, 0);
      } else {
        let json: unknown = undefined;
        const tekst = await res!.text();
        try {
          json = tekst ? JSON.parse(tekst) : undefined;
        } catch {
          json = tekst;
        }
        const uitleg = foutTekst(json);
        fout = new MoneybirdFout(soortVanStatus(res!.status, json), `Moneybird ${res!.status}: ${uitleg}`, res!.status, json);
      }
      const magHerhalen = fout.soort === "te_veel_verzoeken" || (fout.soort === "server" && methode === "GET");
      if (!magHerhalen || poging >= MAX_POGINGEN) throw fout;
      const wacht = fout.soort === "te_veel_verzoeken" ? wachttijdMs(res!.headers.get("retry-after"), this.o.nu()) : 1000 * 2 ** (poging - 1);
      await this.o.slaap(wacht);
    }
  }
}
