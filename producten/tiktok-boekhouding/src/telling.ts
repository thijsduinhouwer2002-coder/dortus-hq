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
