// Ontkoppelen en wissen (ontwerp-d1-worker.md, punt 7). Boeken stopt meteen, alles van de winkel gaat in één batch weg,
// daarna wordt de Moneybird-toegang ingetrokken. Opruimen per cron staat in opruimen.ts.
//
// Vorm van `winkels.taken` (JSON) na ontkoppelen. Een taak die klaar is staat er niet meer in.
//   {
//     "reden": "knop" | "webhook" | "koppeling_verlopen_21_dagen" | ...,
//     "intrekken": { "pogingen": 0, "eerste_poging"?: s, "laatste_poging"?: s },   // alleen als er mb_tokens waren
//     "opzeggen":  { "voor": s, "pogingen": 0, "laatste_poging"?: s, "laatste_fout"?: "...", "alarm_op"?: s }   // alleen als polar_klant gezet was
//   }
// Tijden in Unix-seconden. `opzeggen.voor` is `ontkoppeld_op`: het betaalstuk zegt alleen abonnementen op die daarvoor
// begonnen. Het betaalstuk (eigen bouwstuk) verhoogt bij een mislukte poging `pogingen` en zet `laatste_poging` en
// `laatste_fout`; lukt het, dan haalt het `$.opzeggen` weg en zet `polar_klant` op NULL. `alarm_op` is van de cron
// (ALARM hoogstens één keer per dag). Opnieuw koppelen mag een kale rij alleen hergebruiken als `taken` leeg is.
import { trekIn, type MoneybirdTokens, type OAuthApp } from "../moneybird/oauth.ts";
import { isBudgetOp, type Budget } from "../budget.ts";
import { ontsleutel, type Sleutelbos } from "./tokens.ts";
import type { D1, D1Statement } from "./opslag.ts";

export const DAG = 24 * 3600;
/** Intrekken hoogstens zo lang opnieuw proberen (vanaf de eerste poging), daarna token toch weg en ALARM. */
export const INTREKKEN_MAX_DUUR = 7 * DAG;
/** Tabellen met rijen per winkel; DELETE wordt niet door de triggers geweigerd. */
export const WINKEL_TABELLEN = ["statussen", "transacties", "bestellingen", "sloten"] as const;

export interface IntrekDeps {
  app: OAuthApp;
  /** Dezelfde sleutels als TokenBron: het refresh token wordt met `ontsleutel` uit tokens.ts gelezen. */
  sleutels: Sleutelbos;
  fetchFn?: typeof fetch;
  /** Eén regel in het log van de Worker. Regels die met `ALARM` beginnen moeten opvallen. */
  log: (regel: string) => void;
}

/** gelukt: 200. later: netwerk, 5xx, 429 of iets onbekends. alarm: 403 (fout bij ons). uitgesteld: budget op, niets verstuurd. */
export type IntrekUitkomst = "gelukt" | "later" | "alarm" | "uitgesteld";

export interface OntkoppelUitkomst {
  /** false: onbekende of al ontkoppelde winkel, er is niets gedaan. */
  ontkoppeld: boolean;
  /** "geen": er waren geen Moneybird-tokens. */
  intrekken?: IntrekUitkomst | "geen";
}

/** Eén poging om de Moneybird-toegang in te trekken met het refresh token (één token trekt het hele paar in). */
export async function trekMoneybirdIn(winkel: string, versleuteld: string, budget: Budget, deps: IntrekDeps): Promise<IntrekUitkomst> {
  let refresh: string;
  try {
    refresh = (JSON.parse(await ontsleutel(deps.sleutels, winkel, versleuteld)) as MoneybirdTokens).refreshToken;
    if (!refresh) throw new Error("geen refresh token");
  } catch (e) {
    // Bijvoorbeeld een sleutel die (nog) niet in de Worker staat: later opnieuw; na 7 dagen geeft de cron ALARM.
    deps.log(`winkel ${winkel}: Moneybird-token niet te lezen, intrekken later opnieuw (${(e as Error).message})`);
    return "later";
  }
  try {
    await trekIn(deps.app, refresh, budget.omhul(deps.fetchFn ?? fetch));
    return "gelukt";
  } catch (e) {
    if (isBudgetOp(e)) return "uitgesteld";
    if ((e as { httpStatus?: unknown })?.httpStatus === 403) {
      deps.log(`ALARM winkel ${winkel}: Moneybird weigert intrekken met 403 (verkeerde app-gegevens?); niet herhaald, token gewist`);
      return "alarm";
    }
    return "later";
  }
}

/** Taak `intrekken` klaar (gelukt, 403 of na 7 dagen): token weg, taak weg. */
export function intrekkenKlaar(db: D1, winkel: string): D1Statement {
  return db.prepare(`UPDATE winkels SET mb_tokens = NULL, taken = json_remove(taken, '$.intrekken') WHERE id = ? AND ontkoppeld_op IS NOT NULL`).bind(winkel);
}

/** Wat een uitkomst in D1 betekent; `uitgesteld` schrijft niets (er is niets geprobeerd). */
export function intrekStatement(db: D1, winkel: string, u: IntrekUitkomst, nu: number): D1Statement | undefined {
  if (u === "gelukt" || u === "alarm") return intrekkenKlaar(db, winkel);
  if (u === "uitgesteld") return undefined;
  return db
    .prepare(
      `UPDATE winkels SET taken = json_set(taken,
         '$.intrekken.eerste_poging', coalesce(json_extract(taken, '$.intrekken.eerste_poging'), ?),
         '$.intrekken.laatste_poging', ?,
         '$.intrekken.pogingen', coalesce(json_extract(taken, '$.intrekken.pogingen'), 0) + 1)
       WHERE id = ? AND ontkoppeld_op IS NOT NULL AND json_extract(taken, '$.intrekken') IS NOT NULL`,
    )
    .bind(nu, nu, winkel);
}

/**
 * Ontkoppelen: in één batch (één query, één transactie) `ontkoppeld_op`, alles van de winkel leeg behalve de kale rij,
 * en alle rijen weg uit de vier tabellen. Daarna Moneybird intrekken (één fetch) en de uitkomst opslaan (één query).
 * Onbekend of al ontkoppeld: niets veranderd, geen fout. Kost hoogstens 3 uit het budget.
 */
export async function ontkoppel(db: D1, winkel: string, reden: string, nu: number, budget: Budget, deps: IntrekDeps): Promise<OntkoppelUitkomst> {
  const teller = budget.opslagTeller();
  teller.neem();
  // Volgorde: eerst de oude mb_tokens lezen, dan winkels bijwerken (zet ontkoppeld_op; vanaf dan weigeren de triggers elke
  // INSERT en UPDATE op de vier tabellen, ook van een aanroep die nog loopt), dan de DELETEs (die weigeren de triggers niet).
  // In SET verwijst `mb_tokens` naar de oude waarde: intrekken alleen als er Moneybird-tokens waren; opzeggen alleen als er
  // een Polar-klant is (geen klant: niets op te zeggen).
  const uit = await db.batch([
    db.prepare(`SELECT mb_tokens FROM winkels WHERE id = ? AND ontkoppeld_op IS NULL`).bind(winkel),
    db
      .prepare(
        `UPDATE winkels SET ontkoppeld_op = ?, shop_id = NULL, shop_cipher = NULL, tt_tokens = NULL, tt_versie = 0, mb_versie = 0,
         administratie = NULL, instellingen = NULL, markering = NULL, winkelfout = NULL, winkelfout_sinds = NULL,
         volgende_run = 0, snel_teller = 0,
         taken = json_patch(json_object('reden', ?), json_patch(
           CASE WHEN mb_tokens IS NOT NULL THEN json_object('intrekken', json_object('pogingen', 0)) ELSE '{}' END,
           CASE WHEN polar_klant IS NOT NULL THEN json_object('opzeggen', json_object('voor', ?, 'pogingen', 0)) ELSE '{}' END))
         WHERE id = ? AND ontkoppeld_op IS NULL`,
      )
      .bind(nu, reden, nu, winkel),
    ...WINKEL_TABELLEN.map((t) => db.prepare(`DELETE FROM ${t} WHERE winkel = ?`).bind(winkel)),
  ]);
  if (uit[1].meta.changes !== 1) return { ontkoppeld: false };
  const mb = ((uit[0].results ?? [])[0] as { mb_tokens: string | null } | undefined)?.mb_tokens;
  if (!mb) return { ontkoppeld: true, intrekken: "geen" };

  const u = await trekMoneybirdIn(winkel, mb, budget, deps);
  const st = intrekStatement(db, winkel, u, nu);
  if (st) {
    try {
      teller.neemAfmaken();
      await st.run();
    } catch (e) {
      // Pot echt leeg: de taak blijft staan en de cron probeert opnieuw (intrekken geeft dan gewoon weer 200).
      if (!isBudgetOp(e)) throw e;
    }
  }
  return { ontkoppeld: true, intrekken: u };
}

/** Voor de webhook type 6 (nog niet gebouwd): winkel zoeken op shop_id. Onbekend of al ontkoppeld: niets doen. */
export async function ontkoppelOpShopId(db: D1, shopId: string, reden: string, nu: number, budget: Budget, deps: IntrekDeps): Promise<OntkoppelUitkomst> {
  budget.opslagTeller().neem();
  const rij = await db.prepare(`SELECT id FROM winkels WHERE shop_id = ? AND ontkoppeld_op IS NULL`).bind(shopId).first<{ id: string }>();
  if (!rij) return { ontkoppeld: false };
  return ontkoppel(db, rij.id, reden, nu, budget, deps);
}
