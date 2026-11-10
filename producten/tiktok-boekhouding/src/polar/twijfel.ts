// Stap 5 van ontwerp-betalen.md, punt 2: twijfel aan de stand van het abonnement. Eén keer Customer State opvragen
// (1 verzoek uit de pot van 50, vóór het ophalen bij TikTok) en de stand voorwaardelijk schrijven.
import type { Budget } from "../budget.ts";
import { isBudgetOp } from "../budget.ts";
import type { D1 } from "../d1/opslag.ts";
import { PolarClient, PolarFout, type PolarInstellingen } from "./client.ts";
import { abonnementActief, schrijfStand, type Abonnement } from "./abonnement.ts";

/** Stand ouder dan dit: twijfel (punt 2.5). */
export const TWIJFEL_NA = 3 * 24 * 3600;

export interface TwijfelDeps {
  db: D1;
  winkel: string;
  /** Kolom `winkels.abonnement` zoals gelezen aan het begin van de aanroep. */
  kolom: string | null;
  /** Er wacht een afrekening van de lopende of vorige maand op een abonnement (`wacht_op_abonnement`). */
  wachtRecent: boolean;
  nu: number;
  polar?: PolarInstellingen;
  budget: Budget;
  fetchFn: typeof fetch;
  slaap?: (ms: number) => Promise<void>;
  /** D1-query uit dezelfde pot. */
  neem: () => void;
  log: (regel: string) => void;
}

function lees(kolom: string | null): Abonnement {
  if (!kolom) return {};
  try {
    return (JSON.parse(kolom) as Abonnement) ?? {};
  } catch {
    return {};
  }
}

/** Is er twijfel (punt 2.5)? Zonder stand telt de stand als oud. */
export function heeftTwijfel(kolom: string | null, wachtRecent: boolean, nu: number): boolean {
  const a = lees(kolom);
  const standSec = typeof a.stand === "number" ? a.stand / 1_000_000 : -Infinity;
  const oud = nu - standSec > TWIJFEL_NA;
  if (a.actief === true && !(typeof a.tot === "number" && a.tot > nu)) return true; // verlenging gemist
  if (a.actief === true && oud) return true; // gemiste intrekking (bijv. endpoint door Polar uitgezet)
  return wachtRecent && oud;
}

/**
 * Mag deze aanroep boeken wat een abonnement nodig heeft? Zonder twijfel: de kolom. Met twijfel: Customer State vragen en
 * voorwaardelijk schrijven. Polar onbereikbaar, 429, 5xx, budget op of geen instellingen: niet (gratis boeken gaat door),
 * geen winkelfout, wel een logregel.
 */
export async function abonnementVoorRun(d: TwijfelDeps): Promise<boolean> {
  const actief = abonnementActief(d.kolom, d.nu);
  if (!heeftTwijfel(d.kolom, d.wachtRecent, d.nu)) return actief;
  if (!d.polar?.token) {
    d.log(`ALARM winkel ${d.winkel}: twijfel aan het abonnement, maar Polar is niet ingesteld; alleen gratis boeken`);
    return false;
  }
  try {
    const c = new PolarClient({ instellingen: d.polar, budget: d.budget, fetchFn: d.fetchFn, nu: () => d.nu, ...(d.slaap ? { slaap: d.slaap } : {}) });
    const { abonnement, klant } = await c.standVan(d.winkel);
    d.neem();
    await d.db.batch([schrijfStand(d.db, d.winkel, abonnement, klant)]);
    return abonnement.actief && typeof abonnement.tot === "number" && abonnement.tot > d.nu;
  } catch (e) {
    const wat = isBudgetOp(e) ? "budget op" : e instanceof PolarFout ? `${e.httpStatus}${e.code ? ` ${e.code}` : ""}` : String((e as Error)?.message ?? e);
    const alarm = e instanceof PolarFout && (e.httpStatus === 401 || e.httpStatus === 403) ? "ALARM " : "";
    d.log(`${alarm}winkel ${d.winkel}: abonnement niet opgevraagd bij Polar (${wat}); alleen gratis boeken`);
    return false;
  }
}
