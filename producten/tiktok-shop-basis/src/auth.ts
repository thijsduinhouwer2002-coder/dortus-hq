// Inloggen namens een winkel: inloglink, auth_code inwisselen, token verversen.
// Bron: https://partner.tiktokshop.com/docv2/page/authorization-overview-202407
// Let op: deze aanroepen gaan NIET via de tekenende client. Ze sturen app_secret
// in de query, dus de url wordt nooit gelogd of in een fout gezet.

import { TikTokApiError } from "./fouten.ts";

export const TOKEN_BASIS = "https://auth.tiktok-shops.com";
const AUTORISEER_ROW = "https://services.tiktokshop.com/open/authorize";
const AUTORISEER_US = "https://services.us.tiktokshop.com/open/authorize";

export interface AppGegevens {
  appKey: string;
  appSecret: string;
}

export interface Tokens {
  accessToken: string;
  /** Unix-tijdstip in seconden (geen duur, ondanks de naam bij TikTok). */
  accessTokenVerlooptOp: number;
  refreshToken: string;
  refreshTokenVerlooptOp: number;
  openId: string;
  sellerName: string;
  sellerBaseRegion: string;
  userType: number;
  grantedScopes: string[];
}

export function inlogLink(serviceId: string, state: string, markt: "ROW" | "US" = "ROW"): string {
  const basis = markt === "US" ? AUTORISEER_US : AUTORISEER_ROW;
  const q = new URLSearchParams({ service_id: serviceId, state });
  return `${basis}?${q.toString()}`;
}

/** Een onvoorspelbare state van 32 tekens (hex) tegen CSRF. */
export function maakState(): string {
  const b = new Uint8Array(16);
  crypto.getRandomValues(b);
  return Array.from(b, (x) => x.toString(16).padStart(2, "0")).join("");
}

/** Vergelijkt in vaste tijd, zodat de lengte van de overeenkomst niet uitlekt. */
export function stateKlopt(verwacht: string, ontvangen: string | null | undefined): boolean {
  if (!ontvangen || verwacht.length !== ontvangen.length) return false;
  let verschil = 0;
  for (let i = 0; i < verwacht.length; i++) verschil |= verwacht.charCodeAt(i) ^ ontvangen.charCodeAt(i);
  return verschil === 0;
}

export function verlooptBinnen(verlooptOp: number, margeSeconden: number, nu = Math.floor(Date.now() / 1000)): boolean {
  return verlooptOp - nu <= margeSeconden;
}

type FetchFn = typeof fetch;

async function tokenAanroep(pad: string, params: Record<string, string>, fetchFn: FetchFn): Promise<Tokens> {
  const url = `${TOKEN_BASIS}${pad}?${new URLSearchParams(params).toString()}`;
  const antw = await fetchFn(url, { method: "GET" });
  let json: any;
  try {
    json = await antw.json();
  } catch {
    throw new TikTokApiError(-1, `geen JSON van ${pad} (HTTP ${antw.status})`, "", antw.status);
  }
  if (json?.code !== 0 || !json.data) {
    throw new TikTokApiError(Number(json?.code ?? -1), String(json?.message ?? "onbekend"), String(json?.request_id ?? ""), antw.status);
  }
  const d = json.data;
  return {
    accessToken: d.access_token,
    accessTokenVerlooptOp: Number(d.access_token_expire_in),
    refreshToken: d.refresh_token,
    refreshTokenVerlooptOp: Number(d.refresh_token_expire_in),
    openId: String(d.open_id ?? ""),
    sellerName: String(d.seller_name ?? ""),
    sellerBaseRegion: String(d.seller_base_region ?? ""),
    userType: Number(d.user_type ?? 0),
    grantedScopes: Array.isArray(d.granted_scopes) ? d.granted_scopes : [],
  };
}

export function haalTokens(app: AppGegevens, authCode: string, fetchFn: FetchFn = fetch): Promise<Tokens> {
  return tokenAanroep(
    "/api/v2/token/get",
    // "authorized_code" is zoals TikTok het wil, niet het gewone OAuth "authorization_code".
    { app_key: app.appKey, app_secret: app.appSecret, auth_code: authCode, grant_type: "authorized_code" },
    fetchFn,
  );
}

export function ververs(app: AppGegevens, refreshToken: string, fetchFn: FetchFn = fetch): Promise<Tokens> {
  return tokenAanroep(
    "/api/v2/token/refresh",
    { app_key: app.appKey, app_secret: app.appSecret, refresh_token: refreshToken, grant_type: "refresh_token" },
    fetchFn,
  );
}
