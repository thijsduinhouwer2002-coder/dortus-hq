// Opruimen na ontkoppelen, per cron-aanroep (ontwerp-d1-worker.md, punt 7). Vorm van `taken`: zie ontkoppel.ts.
// Kost: één leesbatch, hoogstens 5 fetches, één schrijfbatch, en hoogstens 3 keer ontkoppelen (3 per keer). Alles in het
// meegegeven budget; is het op, dan stopt het netjes en gaat de volgende cron verder.
import { isBudgetOp, type Budget } from "../budget.ts";
import { DAG, INTREKKEN_MAX_DUUR, WINKEL_TABELLEN, intrekkenKlaar, intrekStatement, ontkoppel, trekMoneybirdIn, type IntrekDeps } from "./ontkoppel.ts";
import type { D1, D1Statement } from "./opslag.ts";

/** (a) Hoogstens zoveel winkels per aanroep opnieuw intrekken (elk één fetch). */
export const INTREKKEN_PER_AANROEP = 5;
/** (b) Wissen herhalen voor hoogstens zoveel kale rijen per aanroep (per tabel), in één batch. */
export const WISSEN_PER_AANROEP = 20;
/** (c) De kale rij gaat uiterlijk na zoveel dagen weg (D1 bewaart herstelpunten 7 dagen op het gratis plan: 23 + 7 = 30). */
export const KALE_RIJ_MAX = 23 * DAG;
/** (d) Zo lang onafgebroken `koppeling_verlopen` aan de kant van TikTok: ontkoppelen. */
export const VERLOPEN_MAX = 21 * DAG;
/** (d) Hoogstens zoveel winkels per aanroep ontkoppelen. */
export const ONTKOPPELEN_PER_AANROEP = 3;

export interface OpruimUitkomst {
  ingetrokken: number;
  alarmen: number;
  ontkoppeld: number;
}

const OPZEGGEN_OPEN = `json_extract(taken, '$.opzeggen') IS NOT NULL`;
const INTREKKEN_OPEN = `json_extract(taken, '$.intrekken') IS NOT NULL`;
const EERSTE_POGING = `coalesce(json_extract(taken, '$.intrekken.eerste_poging'), ontkoppeld_op)`;

/** (b) Vangnet: wat er van kale rijen nog over is weg, hoogstens 20 winkels per statement. Raakt nooit een gekoppelde winkel. */
export function wisVangnet(db: D1): D1Statement[] {
  const n = WISSEN_PER_AANROEP;
  return [
    ...WINKEL_TABELLEN.map((t) =>
      db.prepare(
        `DELETE FROM ${t} WHERE winkel IN (SELECT w.id FROM winkels w WHERE w.ontkoppeld_op IS NOT NULL
         AND EXISTS (SELECT 1 FROM ${t} x WHERE x.winkel = w.id) LIMIT ${n})`,
      ),
    ),
    db.prepare(
      `UPDATE winkels SET shop_id = NULL, shop_cipher = NULL, tt_tokens = NULL, tt_versie = 0, mb_versie = 0, administratie = NULL,
       instellingen = NULL, markering = NULL, winkelfout = NULL, winkelfout_sinds = NULL, volgende_run = 0, snel_teller = 0,
       mb_tokens = CASE WHEN ${INTREKKEN_OPEN} THEN mb_tokens END,
       polar_klant = CASE WHEN ${OPZEGGEN_OPEN} THEN polar_klant END
       WHERE id IN (SELECT id FROM winkels WHERE ontkoppeld_op IS NOT NULL AND (shop_id IS NOT NULL OR shop_cipher IS NOT NULL
         OR tt_tokens IS NOT NULL OR administratie IS NOT NULL OR instellingen IS NOT NULL OR markering IS NOT NULL
         OR winkelfout IS NOT NULL OR winkelfout_sinds IS NOT NULL OR tt_versie <> 0 OR mb_versie <> 0 OR volgende_run <> 0 OR snel_teller <> 0
         OR (mb_tokens IS NOT NULL AND NOT ${INTREKKEN_OPEN}) OR (polar_klant IS NOT NULL AND NOT ${OPZEGGEN_OPEN})) LIMIT ${n})`,
    ),
  ];
}

/**
 * (c) Kale rij weg als beide taken klaar zijn, of na dag 23 als alleen `intrekken` nog openstaat. Staat `opzeggen` nog
 * open, dan blijft de rij altijd (een opzegging die niet gelukt is verdwijnt nooit stil). Alleen als er geen rijen meer
 * in de vier tabellen staan, zodat het vangnet ze nog kan vinden.
 */
export function verwijderKaleRijen(db: D1, nu: number): D1Statement {
  return db
    .prepare(
      `DELETE FROM winkels WHERE ontkoppeld_op IS NOT NULL AND NOT ${OPZEGGEN_OPEN}
       AND (NOT ${INTREKKEN_OPEN} OR ontkoppeld_op <= ?)
       ${WINKEL_TABELLEN.map((t) => `AND NOT EXISTS (SELECT 1 FROM ${t} x WHERE x.winkel = winkels.id)`).join(" ")}`,
    )
    .bind(nu - KALE_RIJ_MAX);
}

export async function ruimOntkoppeldOp(db: D1, nu: number, budget: Budget, deps: IntrekDeps): Promise<OpruimUitkomst> {
  const teller = budget.opslagTeller();
  const uit: OpruimUitkomst = { ingetrokken: 0, alarmen: 0, ontkoppeld: 0 };
  teller.neem();
  const [verlopenIntr, opnieuw, opzeg, verlopen] = await db.batch([
    // (a) intrekken langer dan 7 dagen geprobeerd: token toch weg, ALARM
    db.prepare(`SELECT id FROM winkels WHERE ontkoppeld_op IS NOT NULL AND ${INTREKKEN_OPEN} AND ${EERSTE_POGING} <= ? LIMIT 50`).bind(nu - INTREKKEN_MAX_DUUR),
    // (a) opnieuw proberen, langst niet geprobeerd eerst
    db
      .prepare(
        `SELECT id, mb_tokens FROM winkels WHERE ontkoppeld_op IS NOT NULL AND ${INTREKKEN_OPEN} AND ${EERSTE_POGING} > ?
         ORDER BY coalesce(json_extract(taken, '$.intrekken.laatste_poging'), 0), id LIMIT ?`,
      )
      .bind(nu - INTREKKEN_MAX_DUUR, INTREKKEN_PER_AANROEP),
    // (c) opzeggen mislukt, of na dag 23 nog open: ALARM, hoogstens één keer per dag
    db
      .prepare(
        `SELECT id, coalesce(json_extract(taken, '$.opzeggen.pogingen'), 0) AS pogingen FROM winkels
         WHERE ontkoppeld_op IS NOT NULL AND ${OPZEGGEN_OPEN}
         AND (coalesce(json_extract(taken, '$.opzeggen.pogingen'), 0) > 0 OR ontkoppeld_op <= ?)
         AND coalesce(json_extract(taken, '$.opzeggen.alarm_op'), 0) <= ? LIMIT 50`,
      )
      .bind(nu - KALE_RIJ_MAX, nu - DAG),
    // (d) 21 dagen onafgebroken koppeling_verlopen aan de kant van TikTok
    db
      .prepare(
        `SELECT id FROM winkels WHERE ontkoppeld_op IS NULL AND winkelfout_sinds <= ?
         AND json_extract(winkelfout, '$.soort') = 'koppeling_verlopen' AND json_extract(winkelfout, '$.kant') = 'tiktok'
         ORDER BY winkelfout_sinds LIMIT ?`,
      )
      .bind(nu - VERLOPEN_MAX, ONTKOPPELEN_PER_AANROEP),
  ]);
  const rijen = <T>(r: { results?: unknown[] }) => (r.results ?? []) as T[];

  const schrijf: D1Statement[] = [];
  for (const { id } of rijen<{ id: string }>(verlopenIntr)) {
    deps.log(`ALARM winkel ${id}: Moneybird-toegang na 7 dagen nog niet ingetrokken; token gewist, trek de koppeling handmatig in`);
    uit.alarmen++;
    schrijf.push(intrekkenKlaar(db, id));
  }
  for (const { id, mb_tokens } of rijen<{ id: string; mb_tokens: string | null }>(opnieuw)) {
    if (!mb_tokens) { schrijf.push(intrekkenKlaar(db, id)); continue; }
    const u = await trekMoneybirdIn(id, mb_tokens, budget, deps);
    if (u === "uitgesteld") break; // budget op: de rest de volgende keer
    if (u === "gelukt") uit.ingetrokken++;
    if (u === "alarm") uit.alarmen++;
    schrijf.push(intrekStatement(db, id, u, nu)!);
  }
  for (const { id, pogingen } of rijen<{ id: string; pogingen: number }>(opzeg)) {
    const wat = Number(pogingen) > 0 ? `${pogingen} keer mislukt` : "na 23 dagen nog niet gedaan";
    deps.log(`ALARM winkel ${id}: abonnement bij Polar opzeggen ${wat}; zeg handmatig op in Polar (external_customer_id ${id})`);
    uit.alarmen++;
    schrijf.push(db.prepare(`UPDATE winkels SET taken = json_set(taken, '$.opzeggen.alarm_op', ?) WHERE id = ? AND ontkoppeld_op IS NOT NULL`).bind(nu, id));
  }
  // Volgorde: eerst de taken bijwerken, dan het vangnet, dan pas de kale rijen weg.
  schrijf.push(...wisVangnet(db), verwijderKaleRijen(db, nu));
  teller.neemAfmaken();
  await db.batch(schrijf);

  for (const { id } of rijen<{ id: string }>(verlopen)) {
    try {
      if ((await ontkoppel(db, id, "koppeling_verlopen_21_dagen", nu, budget, deps)).ontkoppeld) uit.ontkoppeld++;
    } catch (e) {
      if (isBudgetOp(e)) break;
      throw e;
    }
  }
  return uit;
}
