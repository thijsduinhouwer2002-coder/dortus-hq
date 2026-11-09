// Fouten van de Moneybird API en van onze eigen controles, met een soort waar de app op kan handelen.
// Ontwerp: ontwerp-moneybird.md. Bron status-codes: developer.moneybird.com/introduction.md

export type MoneybirdFoutSoort =
  | "koppeling_verlopen" // 401: product-laag ververst één keer
  | "geen_abonnement" // 402
  | "geblokkeerd" // 403: IP geblokkeerd
  | "geweigerd" // 400 of 422
  | "niet_gevonden" // 404
  | "te_veel_verzoeken" // 429
  | "server" // 5xx of netwerkfout
  | "periode_afgesloten" // datum op of vóór period_locked_until, of 422 in_locked_period
  | "invoer" // eigen controle vóór de aanroep (gegevens van de afrekening)
  | "instelling" // eigen controle: de koppeling met rekeningen klopt niet (winkel stil tot de gebruiker het regelt)
  | "btw_nog_niet_getest"
  | "dubbel"
  | "antwoord" // onverwacht antwoord (bijv. id als getal)
  | "overig";

export class MoneybirdFout extends Error {
  readonly soort: MoneybirdFoutSoort;
  readonly httpStatus: number;
  readonly body: unknown;

  constructor(soort: MoneybirdFoutSoort, bericht: string, httpStatus = 0, body: unknown = undefined) {
    super(bericht);
    this.name = "MoneybirdFout";
    this.soort = soort;
    this.httpStatus = httpStatus;
    this.body = body;
  }
}

export function soortVanStatus(status: number, body: unknown): MoneybirdFoutSoort {
  if (status === 401) return "koppeling_verlopen";
  if (status === 402) return "geen_abonnement";
  if (status === 403) return "geblokkeerd";
  if (status === 404) return "niet_gevonden";
  if (status === 429) return "te_veel_verzoeken";
  if (status === 400 || status === 422) {
    if (JSON.stringify(body ?? "").includes("in_locked_period")) return "periode_afgesloten";
    return "geweigerd";
  }
  if (status >= 500 || status === 0) return "server";
  return "overig";
}

/** Een id die we gebruiken moet tekst uit cijfers zijn; een getal kan al afgerond zijn. */
export function idTekst(waarde: unknown, naam: string): string {
  if (typeof waarde === "string" && /^\d+$/.test(waarde)) return waarde;
  throw new MoneybirdFout("antwoord", `${naam} is geen tekst met cijfers maar ${JSON.stringify(waarde)}; een groot id als getal kan afgerond zijn`);
}

/** Administratie-id mag een klein getal zijn (zo staat het in de voorbeelden), anders tekst. */
export function administratieId(waarde: unknown): string {
  if (typeof waarde === "number" && Number.isSafeInteger(waarde) && waarde > 0) return String(waarde);
  return idTekst(waarde, "administration_id");
}
