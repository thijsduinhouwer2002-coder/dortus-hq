// Bedragen van TikTok zijn tekst ("12.34", "-30"). Reken ze om naar een geheel
// getal in de kleinste munteenheid, zonder kommagetallen en zonder afronden.

/** Het bedrag heeft meer decimalen dan de munt toestaat: een verkeerde aanname, geen rare waarde. */
export class TeVeelDecimalen extends Error {}

const NUL_DECIMALEN = new Set(["JPY", "KRW", "VND"]);

export function decimalen(valuta: string): number {
  return NUL_DECIMALEN.has(valuta.toUpperCase()) ? 0 : 2;
}

export function naarKleinsteEenheid(bedrag: string, valuta: string): number {
  const m = /^(-?)(\d+)(?:\.(\d+))?$/.exec(bedrag.trim());
  if (!m) throw new Error(`geen geldig bedrag: "${bedrag}"`);
  const [, teken, heel, frac = ""] = m;
  const d = decimalen(valuta);
  if (frac.length > d) throw new TeVeelDecimalen(`"${bedrag}" heeft meer dan ${d} decimalen voor ${valuta}`);
  const waarde = Number(heel + frac.padEnd(d, "0"));
  if (!Number.isSafeInteger(waarde)) throw new Error(`bedrag te groot: "${bedrag}"`);
  return teken === "-" && waarde !== 0 ? -waarde : waarde;
}
