// Kleine query's op de tabel winkels voor de Worker (ontwerp-d1-worker.md, punt 6 en 7). De Worker zelf is nog niet gebouwd.
import type { D1, D1Statement, Teller } from "./opslag.ts";

/** Hoogstens zoveel winkels per cron-aanroep (punt 6). */
export const CRON_LIMIET = 100;

/**
 * Cron: winkels die aan de beurt zijn. Alleen gekoppelde winkels (`ontkoppeld_op IS NULL`), via de gedeeltelijke index
 * `winkels_volgende_run`. Eén query, nieuw werk.
 */
export async function winkelsAanDeBeurt(db: D1, nu: number, teller: Pick<Teller, "neem">, limiet = CRON_LIMIET): Promise<string[]> {
  teller.neem();
  const r = await db
    .prepare(`SELECT id FROM winkels WHERE volgende_run <= ? AND ontkoppeld_op IS NULL ORDER BY volgende_run LIMIT ?`)
    .bind(nu, limiet)
    .all<{ id: string }>();
  return r.results.map((x) => x.id);
}

/**
 * Winkelfout zoals hij in `winkels.winkelfout` staat (JSON). `kant` zegt waar de fout vandaan komt: de regel van 21 dagen
 * (punt 7) geldt alleen voor `koppeling_verlopen` aan de kant van TikTok. De Worker weet welke kant (TokenBron van TikTok
 * of van Moneybird, of een MoneybirdFout) en vult hem in.
 */
export interface OpgeslagenWinkelfout {
  soort: string;
  bericht: string;
  kant: "tiktok" | "moneybird" | "app";
}

/**
 * Statement dat de winkelfout zet (of met `null` wist). `winkelfout_sinds` blijft staan zolang dezelfde soort en kant
 * blijft; een andere fout of wissen begint opnieuw. Geeft een statement, zodat de Worker het meestuurt in de slotbatch
 * (`D1Opslag.klaar(extra)`, punt 6). Alleen aanroepen als de run echt een uitkomst had (niet bij een bezet winkelslot).
 */
export function winkelfoutStatement(db: D1, winkel: string, fout: OpgeslagenWinkelfout | null, nu: number): D1Statement {
  if (!fout) return db.prepare(`UPDATE winkels SET winkelfout = NULL, winkelfout_sinds = NULL WHERE id = ? AND ontkoppeld_op IS NULL`).bind(winkel);
  return db
    .prepare(
      `UPDATE winkels SET winkelfout = ?,
       winkelfout_sinds = CASE WHEN winkelfout IS NOT NULL AND winkelfout_sinds IS NOT NULL
         AND json_extract(winkelfout, '$.soort') = ? AND json_extract(winkelfout, '$.kant') = ? THEN winkelfout_sinds ELSE ? END
       WHERE id = ? AND ontkoppeld_op IS NULL`,
    )
    .bind(JSON.stringify(fout), fout.soort, fout.kant, nu, winkel);
}
