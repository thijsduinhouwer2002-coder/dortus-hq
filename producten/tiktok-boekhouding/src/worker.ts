// De Worker (ontwerp-d1-worker.md, punt 6): cron elke 15 minuten en een queue-consumer die één winkel verwerkt.
// `cron` en `consumer` krijgen alles mee (db, wachtrij, fetch, log, sleutels), zodat ze los te toetsen zijn.
// De `export default` onderaan is dun: hij bouwt de Omgeving uit de echte env van Cloudflare en roept ze aan.
import { TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { TikTokApiError } from "../../tiktok-shop-basis/src/fouten.ts";
import type { AppGegevens } from "../../tiktok-shop-basis/src/auth.ts";
import { Budget, isBudgetOp } from "./budget.ts";
import { MoneybirdClient } from "./moneybird/client.ts";
import { MoneybirdFout } from "./moneybird/fouten.ts";
import type { OAuthApp } from "./moneybird/oauth.ts";
import { isOntkoppeld } from "./opslag.ts";
import { WinkelStop } from "./ophalen.ts";
import { verwerkWinkel, type Instellingen, type RunUitkomst } from "./verwerk.ts";
import { D1Opslag, type D1 } from "./d1/opslag.ts";
import { ruimOntkoppeldOp } from "./d1/opruimen.ts";
import { TokenBron, moneybirdSoort, tiktokSoort, type Sleutelbos } from "./d1/tokens.ts";
import { winkelfoutStatement, winkelsAanDeBeurt, type OpgeslagenWinkelfout } from "./d1/winkels.ts";

/** Budget per aanroep (gratis plan: 50 subrequests, D1 en de wachtrij tellen mee). */
export const WORKER_BUDGET = 50;
/** Deel dat nieuw werk niet mag gebruiken: voor afmaken (status, volgende_run, slot terug). */
export const AFMAAK_RESERVE = 6;
export const LEASE = 30 * 60;
export const WINKELSLOT = "__winkel";
export const WINKELSLOT_DUUR = 15 * 60;
export const GEWOON = 6 * 3600;
export const SNEL = 15 * 60;
export const MAX_SNEL = 8;

/** Het deel van een Cloudflare Queue dat de cron gebruikt. */
export interface Wachtrij {
  sendBatch(berichten: Array<{ body: WinkelBericht }>): Promise<unknown>;
}
export interface WinkelBericht {
  winkel: string;
}

/** Alles wat cron en consumer nodig hebben. In productie gebouwd door `omgevingVan(env)`. */
export interface Omgeving {
  db: D1;
  wachtrij: Wachtrij;
  fetchFn: typeof fetch;
  log: (regel: string) => void;
  sleutels: Sleutelbos;
  tiktokApp: AppGegevens;
  moneybirdApp: OAuthApp;
  /** Wachten bij 429 (clients); in toetsen niets. */
  slaap?: (ms: number) => Promise<void>;
  /** Uniek per aanroep: eigenaar van de sloten. Standaard willekeurig. */
  eigenaar?: () => string;
}

const foutTekst = (e: unknown) => String((e as Error)?.message ?? e);

// ---------------------------------------------------------------------------------------------------------------
// Cron

export interface CronUitkomst {
  verstuurd: number;
}

/** Winkels aan de beurt in de wachtrij, dan een lease van 30 minuten, dan opruimen. Gooit nooit. */
export async function cron(o: Omgeving, nu: number): Promise<CronUitkomst> {
  const budget = new Budget(WORKER_BUDGET);
  const teller = budget.opslagTeller();
  let verstuurd = 0;
  try {
    const ids = await winkelsAanDeBeurt(o.db, nu, teller);
    if (ids.length) {
      // Eerst versturen, dan de lease: mislukt de lease, dan komt er hoogstens een dubbel bericht (winkelslot vangt het op).
      // Andersom zou een winkel 30 minuten overslaan als het versturen mislukt.
      budget.neem();
      await o.wachtrij.sendBatch(ids.map((winkel) => ({ body: { winkel } })));
      verstuurd = ids.length;
      teller.neemAfmaken();
      await o.db.batch(ids.map((id) => o.db.prepare(`UPDATE winkels SET volgende_run = ? WHERE id = ? AND ontkoppeld_op IS NULL`).bind(nu + LEASE, id)));
    }
  } catch (e) {
    o.log(`cron: winkels in de wachtrij zetten mislukt: ${foutTekst(e)}`);
  }
  try {
    await ruimOntkoppeldOp(o.db, nu, budget, { app: o.moneybirdApp, sleutels: o.sleutels, fetchFn: o.fetchFn, log: o.log });
  } catch (e) {
    o.log(`cron: opruimen mislukt: ${foutTekst(e)}`);
  }
  return { verstuurd };
}

// ---------------------------------------------------------------------------------------------------------------
// Consumer

export type ConsumerUitkomst = "slot_bezet" | "ontkoppeld" | "verwerkt" | "fout";

interface WinkelRij {
  shop_cipher: string | null;
  instellingen: string | null;
  snel_teller: number;
  tt_tokens: string | null;
  tt_versie: number;
  mb_tokens: string | null;
  mb_versie: number;
}

/** Soorten die alleen bij één kant voorkomen. `te_veel_verzoeken` en `server` komen bij beide voor. */
const ALLEEN_TIKTOK = ["token_verlopen", "geen_toegang", "handtekening_fout", "auth_code_ongeldig"];
const ALLEEN_MONEYBIRD = ["koppeling_verlopen", "geen_abonnement", "geblokkeerd", "niet_gevonden"];
const VAN_ONS = ["instelling", "btw_nog_niet_getest"];

/**
 * Waar kwam de winkelfout vandaan? `verwerkWinkel` geeft alleen soort en bericht. Eerst de soort; bij een soort die bij
 * beide voorkomt de kant van het laatste uitgaande verzoek (dat is het verzoek dat de stop gaf, want na een stop gaat er
 * niets meer uit).
 */
export function kantVan(soort: string, laatste: "tiktok" | "moneybird" | undefined): OpgeslagenWinkelfout["kant"] {
  if (ALLEEN_TIKTOK.includes(soort)) return "tiktok";
  if (ALLEEN_MONEYBIRD.includes(soort)) return "moneybird";
  if (VAN_ONS.includes(soort)) return "app";
  return laatste ?? "app";
}

/** Kant van een fout die buiten verwerkWinkel gegooid werd (tokens). */
function kantVanFout(e: WinkelStop, bron: "tiktok" | "moneybird"): OpgeslagenWinkelfout["kant"] {
  if (e.oorzaak instanceof TikTokApiError) return "tiktok";
  if (e.oorzaak instanceof MoneybirdFout) return "moneybird";
  return bron;
}

/**
 * Eén winkel. Gooit nooit; de aanroeper bevestigt het bericht altijd (max_retries 0: de cron pakt de winkel vanzelf
 * weer op na de lease van 30 minuten).
 */
export async function consumer(bericht: WinkelBericht, o: Omgeving, nu: number): Promise<ConsumerUitkomst> {
  const winkel = String(bericht?.winkel ?? "");
  if (!winkel) {
    o.log("consumer: bericht zonder winkel");
    return "fout";
  }
  const budget = new Budget(WORKER_BUDGET);
  budget.reserve = AFMAAK_RESERVE;
  const teller = budget.opslagTeller();
  const opslag = new D1Opslag(o.db, winkel, teller);
  const eigenaar = o.eigenaar?.() ?? `run-${crypto.randomUUID()}`;

  try {
    if (!(await opslag.neemSlot(WINKELSLOT, eigenaar, nu + WINKELSLOT_DUUR, nu))) return "slot_bezet";
  } catch (e) {
    o.log(`consumer ${winkel}: winkelslot nemen mislukt: ${foutTekst(e)}`);
    return "fout";
  }

  // Vanaf hier is het winkelslot van ons; aan het eind altijd terug (ook bij een fout).
  let slotTerugInKlaar = false;
  try {
    const uit = await verwerkOnderSlot(o, winkel, nu, budget, teller, opslag, eigenaar);
    slotTerugInKlaar = uit !== "fout";
    return uit;
  } catch (e) {
    if (isOntkoppeld(e)) return "ontkoppeld";
    o.log(`consumer ${winkel}: onverwachte fout: ${foutTekst(e)}`);
    return "fout";
  } finally {
    if (!slotTerugInKlaar) {
      try {
        await opslag.geefSlotTerug(WINKELSLOT, eigenaar);
      } catch (e) {
        // Ontkoppeld: geen slotrij meer. Anders verloopt het slot na 15 minuten vanzelf.
        if (!isOntkoppeld(e)) o.log(`consumer ${winkel}: winkelslot teruggeven mislukt: ${foutTekst(e)}`);
      }
    }
  }
}

async function verwerkOnderSlot(
  o: Omgeving, winkel: string, nu: number, budget: Budget, teller: ReturnType<Budget["opslagTeller"]>, opslag: D1Opslag, eigenaar: string,
): Promise<ConsumerUitkomst> {
  teller.neem();
  const rij = await o.db
    // Winkelrij en beide tokens in één query (scheelt 2 per aanroep); TokenBron.vanRij gebruikt de tokenkolommen.
    .prepare(`SELECT shop_cipher, instellingen, snel_teller, tt_tokens, tt_versie, mb_tokens, mb_versie FROM winkels WHERE id = ? AND ontkoppeld_op IS NULL`)
    .bind(winkel)
    .first<WinkelRij>();
  if (!rij) return "ontkoppeld";

  // Laatste uitgaande verzoek: TikTok of Moneybird (voor de kant van de winkelfout).
  let laatste: "tiktok" | "moneybird" | undefined;
  const volg = (async (input: any, init?: any) => {
    laatste = String(input instanceof Request ? input.url : input).includes("moneybird") ? "moneybird" : "tiktok";
    return o.fetchFn(input, init);
  }) as typeof fetch;
  const klok = () => nu;
  const tokenDeps = { db: o.db, winkel, sleutels: o.sleutels, budget, fetchFn: volg, nu: klok, log: o.log };

  let fout: OpgeslagenWinkelfout | null = null;
  let nogWerk = false;
  try {
    const inst = rij.instellingen ? (JSON.parse(rij.instellingen) as Instellingen) : undefined;
    if (!inst?.koppeling || !inst.administratie || !rij.shop_cipher) {
      fout = { soort: "instelling", bericht: "instellingen of shop_cipher ontbreken", kant: "app" };
    } else {
      // Tokens: alleen hier, onder het winkelslot (tokens.ts, versie 3b).
      let bron: "tiktok" | "moneybird" = "tiktok";
      try {
        const ttBron = new TokenBron({ ...tokenDeps, soort: tiktokSoort(o.tiktokApp) });
        const mbBron = new TokenBron({ ...tokenDeps, soort: moneybirdSoort(o.moneybirdApp) });
        await ttBron.vanRij(rij.tt_tokens, rij.tt_versie);
        const tt = await ttBron.geef();
        bron = "moneybird";
        await mbBron.vanRij(rij.mb_tokens, rij.mb_versie);
        await mbBron.geef();
        if (tt.waarschuwing) o.log(`winkel ${winkel}: refresh token van TikTok verloopt binnen 14 dagen; verkoper moet opnieuw koppelen`);
        const f = budget.omhul(volg);
        const slaap = o.slaap ?? ((ms: number) => new Promise<void>((r) => setTimeout(r, ms)));
        const run = (ttTok: string, mbTok: string) =>
          verwerkWinkel(
            {
              tiktok: new TikTokClient({ appKey: o.tiktokApp.appKey, appSecret: o.tiktokApp.appSecret, fetchFn: f, nu: klok, slaap }),
              moneybird: new MoneybirdClient({ accessToken: mbTok, fetchFn: f, nu: klok, slaap }),
              accessToken: ttTok,
              shopCipher: rij.shop_cipher!,
              opslag, budget, nu: klok, eigenaar,
            },
            inst,
          );
        // Punt 5: na een 401 één keer verversen en opnieuw, in dezelfde aanroep en hetzelfde budget, via TokenBron.met.
        const uit = await metVerversen(ttBron, mbBron, run, (k) => { bron = k; });
        if (uit.winkel?.soort === "ontkoppeld") return "ontkoppeld";
        if (uit.winkel) fout = { soort: uit.winkel.soort, bericht: uit.winkel.bericht, kant: kantVan(uit.winkel.soort, laatste) };
        nogWerk = uit.budgetOp || uit.verwerkt.some((v) => v.status === "bezig_met_ophalen");
      } catch (e) {
        if (isOntkoppeld(e)) return "ontkoppeld";
        if (e instanceof WinkelStop) fout = { soort: e.soort, bericht: e.message, kant: kantVanFout(e, bron) };
        else if (isBudgetOp(e)) nogWerk = true;
        else throw e;
      }
    }
  } catch (e) {
    if (isOntkoppeld(e)) return "ontkoppeld";
    // Onverwacht (D1, kapotte JSON, ontsleutelen): niets aan de winkel veranderen; de lease brengt hem over 30 minuten terug.
    o.log(`consumer ${winkel}: run mislukt: ${foutTekst(e)}`);
    return "fout";
  }

  // De echte volgende_run: snel als er nog werk is, hoogstens 8 keer achter elkaar.
  const snel = nogWerk && Number(rij.snel_teller) < MAX_SNEL;
  const extra = [
    winkelfoutStatement(o.db, winkel, fout, nu),
    o.db
      .prepare(`UPDATE winkels SET volgende_run = ?, snel_teller = ? WHERE id = ? AND ontkoppeld_op IS NULL`)
      .bind(nu + (snel ? SNEL : GEWOON), snel ? Number(rij.snel_teller) + 1 : 0, winkel),
    // Winkelslot terug in dezelfde batch (scheelt een query).
    o.db.prepare(`DELETE FROM sloten WHERE winkel = ? AND statement_id = ? AND eigenaar = ?`).bind(winkel, WINKELSLOT, eigenaar),
  ];
  await opslag.klaar(extra);
  return "verwerkt";
}

/** Herkent een 401 van de ene kant zonder dat `is401` in de andere TokenBron hem ziet (geen httpStatus of soort). */
class Kant401 extends Error {
  readonly uit: RunUitkomst;
  constructor(uit: RunUitkomst) { super("401 midden in de run"); this.uit = uit; }
}
class MbStop extends Error {
  readonly stop: WinkelStop;
  constructor(stop: WinkelStop) { super(stop.message); this.stop = stop; }
}

/**
 * `verwerkWinkel` vangt fouten van de clients zelf af en geeft ze terug als `uit.winkel`: `token_verlopen` is de 401
 * van TikTok, `koppeling_verlopen` die van Moneybird. Die zetten we hier om in een fout, zodat `TokenBron.met` één keer
 * ververst en de run opnieuw doet (statussen zijn teruggezet, markering staat vast, dus opnieuw is veilig). Tweede keer
 * weer 401: WinkelStop `koppeling_verlopen` van die kant. Ook een geldig paar dat al door een andere aanroep ververst
 * werd, komt zo terug (TokenBron leest D1 opnieuw).
 */
async function metVerversen(
  tt: TokenBron<{ accessToken: string }>, mb: TokenBron<{ accessToken: string }>,
  run: (ttTok: string, mbTok: string) => Promise<RunUitkomst>, kant: (k: "tiktok" | "moneybird") => void,
): Promise<RunUitkomst> {
  try {
    return await tt.met(async (ttTok) => {
      try {
        return await mb.met(async (mbTok) => {
          const uit = await run(ttTok.accessToken, mbTok.accessToken);
          if (uit.winkel?.soort === "token_verlopen") throw new Kant401(uit); // niet voor mb.met
          if (uit.winkel?.soort === "koppeling_verlopen") throw Object.assign(new Error(uit.winkel.bericht), { httpStatus: 401 });
          return uit;
        });
      } catch (e) {
        if (e instanceof Kant401) throw Object.assign(new Error(e.message), { httpStatus: 401 }); // nu wel voor tt.met
        if (e instanceof WinkelStop) throw new MbStop(e); // tweede 401 van Moneybird: niet tt.met laten verversen
        throw e;
      }
    });
  } catch (e) {
    if (e instanceof MbStop) { kant("moneybird"); throw e.stop; }
    if (e instanceof WinkelStop) kant("tiktok");
    throw e;
  }
}

// ---------------------------------------------------------------------------------------------------------------
// Echte env (Cloudflare). Geen uitrol hier; zie wrangler.voorbeeld.toml.

export interface WorkerEnv {
  DB: D1;
  WACHTRIJ: Wachtrij;
  /** Secret: JSON `{"v1": "<32 bytes base64>", ...}`. */
  TOKEN_SLEUTELS: string;
  /** Versie om mee te versleutelen, bijv. "v1". */
  TOKEN_SLEUTEL_HUIDIG: string;
  /** TikTok Partner Center: app key en app secret (secret), nodig voor tekenen en verversen. */
  TIKTOK_APP_KEY: string;
  TIKTOK_APP_SECRET: string;
  /** Moneybird OAuth-app: nodig voor verversen en intrekken. */
  MONEYBIRD_CLIENT_ID: string;
  MONEYBIRD_CLIENT_SECRET: string;
  MONEYBIRD_REDIRECT_URI: string;
}

export function omgevingVan(env: WorkerEnv): Omgeving {
  const ruw = JSON.parse(env.TOKEN_SLEUTELS) as Record<string, string>;
  const sleutels: Sleutelbos = {
    huidig: env.TOKEN_SLEUTEL_HUIDIG,
    sleutels: Object.fromEntries(Object.entries(ruw).map(([v, b]) => [v, Uint8Array.from(atob(b), (c) => c.charCodeAt(0))])),
  };
  return {
    db: env.DB,
    wachtrij: env.WACHTRIJ,
    fetchFn: (...a) => fetch(...a),
    log: (r) => console.log(r),
    sleutels,
    tiktokApp: { appKey: env.TIKTOK_APP_KEY, appSecret: env.TIKTOK_APP_SECRET },
    moneybirdApp: { clientId: env.MONEYBIRD_CLIENT_ID, clientSecret: env.MONEYBIRD_CLIENT_SECRET, redirectUri: env.MONEYBIRD_REDIRECT_URI },
  };
}

const seconden = (ms: number) => Math.floor(ms / 1000);

export default {
  async scheduled(controller: { scheduledTime: number }, env: WorkerEnv, ctx: { waitUntil(p: Promise<unknown>): void }) {
    ctx.waitUntil(cron(omgevingVan(env), seconden(controller.scheduledTime)).catch((e) => console.log(`cron: ${foutTekst(e)}`)));
  },
  async queue(batch: { messages: Array<{ body: WinkelBericht; ack(): void }> }, env: WorkerEnv) {
    let o: Omgeving | undefined;
    try {
      o = omgevingVan(env);
    } catch (e) {
      console.log(`queue: env onbruikbaar: ${foutTekst(e)}`);
    }
    for (const m of batch.messages) {
      try {
        if (o) await consumer(m.body, o, seconden(Date.now()));
      } catch (e) {
        console.log(`queue: ${foutTekst(e)}`);
      }
      m.ack(); // altijd bevestigen (max_retries 0)
    }
  },
};
