// Gratis grens (ontwerp-betalen.md, punt 1 en 2): maand en aantal bestellingen van een afrekening.
import type { Transactie } from "../../tiktok-shop-basis/src/endpoints.ts";
import { bestellingenVan } from "./samenstel.ts";

/** Zoveel bestellingen per kalendermaand gratis (werkwaarde tot Chris beslist). */
export const GRATIS_PER_MAAND = 30;

const MAAND = new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Amsterdam", year: "numeric", month: "2-digit" });

/** `JJJJ-MM` van `statement_time` (unix-seconden) in Europe/Amsterdam: 31 dec 23:30 UTC is al januari. */
export function maandVan(statementTime: number): string {
  // en-CA geeft "JJJJ-MM"; via de delen, zodat een andere scheiding in een runtime niets uitmaakt.
  const delen = MAAND.formatToParts(statementTime * 1000);
  const jaar = delen.find((d) => d.type === "year")?.value;
  const maand = delen.find((d) => d.type === "month")?.value;
  return `${jaar}-${maand}`;
}

/** `n`: aantal unieke `order_id` van transacties met type ORDER. Een afrekening zonder bestellingen telt 0. */
export function telBestellingen(transacties: Transactie[]): number {
  return bestellingenVan(transacties).length;
}

/** `JJJJ-MM` één maand terug. */
export function maandTerug(maand: string): string {
  const [j, m] = maand.split("-").map(Number);
  return m === 1 ? `${j - 1}-12` : `${j}-${String(m - 1).padStart(2, "0")}`;
}

/** De vorige kalendermaand (Europe/Amsterdam) gezien vanaf `nu`. Ouder dan deze maand en geen abonnement: `wacht_ouder`. */
export function vorigeMaand(nu: number): string {
  return maandTerug(maandVan(nu));
}

/** Unix-seconden van 1 `maand` 00:00 in Europe/Amsterdam (UTC+1 of UTC+2). */
export function beginVanMaand(maand: string): number {
  const [j, m] = maand.split("-").map(Number);
  const middernachtUtc = Date.UTC(j, m - 1, 1) / 1000;
  for (const verschuiving of [3600, 7200]) {
    const t = middernachtUtc - verschuiving;
    if (maandVan(t) === maand && maandVan(t - 1) !== maand) return t;
  }
  throw new Error(`begin van maand ${maand} niet te bepalen`);
}

/** Som van de bestellingen van `maand` zonder afrekening `behalve` (elke telling sluit de eigen afrekening uit). */
export function somVanMaand(telling: Map<string, { maand: string; bestellingen: number }>, maand: string, behalve: string): number {
  let som = 0;
  for (const [id, r] of telling) if (id !== behalve && r.maand === maand) som += r.bestellingen;
  return som;
}
