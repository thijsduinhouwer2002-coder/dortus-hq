// Fouten van de TikTok Shop API, ingedeeld in soorten waar de app op kan handelen.
// Bron: https://partner.tiktokshop.com/docv2/page/common-errors

export type FoutSoort =
  | "te_veel_verzoeken" // HTTP 429 of 36009002: later opnieuw
  | "token_verlopen" // 105002: token verversen
  | "geen_toegang" // 105005: scope ontbreekt
  | "handtekening_fout" // 106001
  | "auth_code_ongeldig" // 36004004: gebruikt, verlopen of fout
  | "server" // HTTP 5xx
  | "overig";

export class TikTokApiError extends Error {
  readonly code: number;
  readonly requestId: string;
  readonly httpStatus: number;
  readonly soort: FoutSoort;

  constructor(code: number, message: string, requestId: string, httpStatus: number) {
    super(`TikTok Shop fout ${code}: ${message} (request_id ${requestId || "onbekend"})`);
    this.name = "TikTokApiError";
    this.code = code;
    this.requestId = requestId;
    this.httpStatus = httpStatus;
    this.soort = bepaalSoort(code, httpStatus);
  }
}

export function bepaalSoort(code: number, httpStatus: number): FoutSoort {
  if (httpStatus === 429 || code === 36009002) return "te_veel_verzoeken";
  if (code === 105002) return "token_verlopen";
  if (code === 105005) return "geen_toegang";
  if (code === 106001) return "handtekening_fout";
  if (code === 36004004) return "auth_code_ongeldig";
  if (httpStatus >= 500) return "server";
  return "overig";
}

/** Mag de client deze fout zelf opnieuw proberen? */
export function opnieuwProberen(fout: TikTokApiError): boolean {
  return fout.soort === "te_veel_verzoeken" || fout.soort === "server";
}
