// Opruimen na ontkoppelen, per cron-aanroep (ontwerp-d1-worker.md, punt 7). Vorm van `taken`: zie ontkoppel.ts.
// Kost: één leesbatch, hoogstens 5 fetches, één schrijfbatch, en hoogstens 3 keer ontkoppelen (3 per keer). Alles in het
// meegegeven budget; is het op, dan stopt het netjes en gaat de volgende cron verder.
import { isBudgetOp, type Budget } from "../budget.ts";
import { DAG, INTREKKEN_MAX_DUUR, WINKEL_TABELLEN, intrekkenKlaar, intrekStatement, ontkoppel, trekMoneybirdIn, type IntrekDeps } from "./ontkoppel.ts";
import type { D1, D1Statement } from "./opslag.ts";
import { PolarClient, type OpzegUitkomst, type PolarInstellingen } from "../polar/client.ts";

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
/** (e) Hoogstens zoveel winkels per aanroep opzeggen bij Polar (elk 1 tot ±3 verzoeken), en per winkel hoogstens één poging per uur. */
export const OPZEGGEN_PER_AANROEP = 3;
export const OPZEGGEN_WACHT = 3600;

/**
 * (e) Wat een opzegpoging in D1 betekent (vorm van `taken` in ontkoppel.ts): gelukt haalt `$.opzeggen` weg en zet
 * `polar_klant` op NULL; later telt `pogingen` op met `laatste_poging` en `laatste_fout`; uitgesteld schrijft niets.
 */
export function opzegStatement(db: D1, winkel: string, u: OpzegUitkomst, nu: number): D1Statement | undefined {
  if (u.uitkomst === "uitgesteld") return undefined;
  if (u.uitkomst === "gelukt") {
    return db.prepare(`UPDATE winkels SET polar_klant = NULL, taken = json_remove(taken, '$.opzeggen') WHERE id = ? AND ontkoppeld_op IS NOT NULL`).bind(winkel);
  }
  return db
    .prepare(
      `UPDATE winkels SET taken = json_set(taken, '$.opzeggen.pogingen', coalesce(json_extract(taken, '$.opzeggen.pogingen'), 0) + 1,
         '$.opzeggen.laatste_poging', ?, '$.opzeggen.laatste_fout', ?)
       WHERE id = ? AND ontkoppeld_op IS NOT NULL AND json_extract(taken, '$.opzeggen') IS NOT NULL`,
    )
    .bind(nu, u.fout.slice(0, 200), winkel);
}

export interface OpruimUitkomst {
  ingetrokken: number;
  alarmen: number;
  ontkoppeld: number;
  /** (e) Opzeggingen bij Polar die lukten. */
  opgezegd: number;
  /** true: het budget raakte op; de volgende cron gaat verder. */
  budgetOp: boolean;
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
       abonnement = NULL, polar_gestart = NULL,
       mb_tokens = CASE WHEN ${INTREKKEN_OPEN} THEN mb_tokens END,
       polar_klant = CASE WHEN ${OPZEGGEN_OPEN} THEN polar_klant END
       WHERE id IN (SELECT id FROM winkels WHERE ontkoppeld_op IS NOT NULL AND (shop_id IS NOT NULL OR shop_cipher IS NOT NULL
         OR tt_tokens IS NOT NULL OR administratie IS NOT NULL OR instellingen IS NOT NULL OR markering IS NOT NULL
         OR winkelfout IS NOT NULL OR winkelfout_sinds IS NOT NULL OR abonnement IS NOT NULL OR polar_gestart IS NOT NULL OR tt_versie <> 0 OR mb_versie <> 0 OR volgende_run <> 0 OR snel_teller <> 0
         OR (mb_tokens IS NOT NULL AND NOT ${INTREKKEN_OPEN}) OR (polar_klant IS NOT NULL AND NOT ${OPZEGGEN_OPEN})) LIMIT ${n})`,
    ),
  ];
}

/**
 * (c) Kale rij weg als beide taken klaar zijn, of na dag 23 als alleen `intrekken` nog openstaat. Staat `opzeggen` nog
 * open, dan blijft de rij altijd (een opzegging die niet gelukt is verdwijnt nooit stil). Alleen als er geen rijen meer
 * in de vijf tabellen staan, zodat het vangnet ze nog kan vinden.
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

/** `polar`: zonder (geen POLAR_TOKEN) wordt niet opgezegd; dan volgt na dag 23 het dagelijkse ALARM. */
export async function ruimOntkoppeldOp(db: D1, nu: number, budget: Budget, deps: IntrekDeps & { polar?: PolarInstellingen }): Promise<OpruimUitkomst> {
  const teller = budget.opslagTeller();
  const uit: OpruimUitkomst = { ingetrokken: 0, alarmen: 0, ontkoppeld: 0, opgezegd: 0, budgetOp: false };
  try {
    teller.neem();
  } catch (e) {
    if (!isBudgetOp(e)) throw e;
    return { ...uit, budgetOp: true };
  }
  const [verlopenIntr, opnieuw, opzeg, verlopen, teOpzeggen] = await db.batch([
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
    // (e) opzeggen bij Polar, langst niet geprobeerd eerst, hoogstens één poging per uur per winkel
    db
      .prepare(
        `SELECT id FROM winkels WHERE ontkoppeld_op IS NOT NULL AND ${OPZEGGEN_OPEN}
         AND coalesce(json_extract(taken, '$.opzeggen.laatste_poging'), 0) <= ?
         ORDER BY coalesce(json_extract(taken, '$.opzeggen.laatste_poging'), 0), id LIMIT ?`,
      )
      .bind(nu - OPZEGGEN_WACHT, OPZEGGEN_PER_AANROEP),
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
    if (u === "uitgesteld") { uit.budgetOp = true; break; } // budget op: de rest de volgende keer
    if (u === "gelukt") uit.ingetrokken++;
    if (u === "alarm") uit.alarmen++;
    schrijf.push(intrekStatement(db, id, u, nu)!);
  }
  // (e) Eerst opzeggen; wat nu lukt krijgt geen ALARM meer.
  const gelukt = new Set<string>();
  if (deps.polar?.token) {
    const polar = new PolarClient({ instellingen: deps.polar, budget, fetchFn: deps.fetchFn, nu: () => nu });
    for (const { id } of rijen<{ id: string }>(teOpzeggen)) {
      const u = await polar.zegOp(id);
      if (u.uitkomst === "uitgesteld") { uit.budgetOp = true; break; }
      if (u.uitkomst === "gelukt") { uit.opgezegd++; gelukt.add(id); }
      else deps.log(`winkel ${id}: opzeggen bij Polar mislukt, later opnieuw (${u.fout})`);
      schrijf.push(opzegStatement(db, id, u, nu)!);
    }
  }
  for (const { id, pogingen } of rijen<{ id: string; pogingen: number }>(opzeg)) {
    if (gelukt.has(id)) continue;
    const wat = Number(pogingen) > 0 ? `${pogingen} keer mislukt` : "na 23 dagen nog niet gedaan";
    deps.log(`ALARM winkel ${id}: abonnement bij Polar opzeggen ${wat}; zeg handmatig op in Polar (external_customer_id ${id})`);
    uit.alarmen++;
    schrijf.push(db.prepare(`UPDATE winkels SET taken = json_set(taken, '$.opzeggen.alarm_op', ?) WHERE id = ? AND ontkoppeld_op IS NOT NULL`).bind(nu, id));
  }
  // Volgorde: eerst de taken bijwerken, dan het vangnet, dan pas de kale rijen weg.
  schrijf.push(...wisVangnet(db), verwijderKaleRijen(db, nu));
  try {
    teller.neemAfmaken();
  } catch (e) {
    // Pot echt leeg: niets geschreven. Intrekken dat net lukte wordt de volgende keer herhaald (geeft dan weer 200).
    if (!isBudgetOp(e)) throw e;
    return { ...uit, budgetOp: true };
  }
  await db.batch(schrijf);

  for (const { id } of rijen<{ id: string }>(verlopen)) {
    try {
      if ((await ontkoppel(db, id, "koppeling_verlopen_21_dagen", nu, budget, deps)).ontkoppeld) uit.ontkoppeld++;
    } catch (e) {
      if (isBudgetOp(e)) { uit.budgetOp = true; break; }
      throw e;
    }
  }
  return uit;
}
