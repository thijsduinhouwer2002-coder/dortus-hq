// OAuth bij Moneybird. Bron: developer.moneybird.com/authentication.md. Tokens bewaart de app zelf.

export const MONEYBIRD_OAUTH = "https://moneybird.com/oauth";
/** `documents` om te boeken en rekeningen en btw-tarieven te lezen; `settings` om rekeningen aan te maken (ontwerp-schermen.md, stap 3). */
export const SCOPES = ["documents", "settings"];

export interface OAuthApp {
  clientId: string;
  clientSecret: string;
  redirectUri: string;
}

export interface MoneybirdTokens {
  accessToken: string;
  refreshToken: string;
  scope: string;
  /** Unix-seconden; ontbreekt zolang Moneybird tokens niet laat verlopen. */
  verlooptOp?: number;
}

export function inlogLink(app: OAuthApp, state: string): string {
  const q = new URLSearchParams({ client_id: app.clientId, redirect_uri: app.redirectUri, response_type: "code", scope: SCOPES.join(" "), state });
  return `${MONEYBIRD_OAUTH}/authorize?${q.toString()}`;
}

async function tokenVerzoek(app: OAuthApp, velden: Record<string, string>, fetchFn: typeof fetch): Promise<MoneybirdTokens> {
  const body = new URLSearchParams({ client_id: app.clientId, client_secret: app.clientSecret, ...velden });
  const res = await fetchFn(`${MONEYBIRD_OAUTH}/token`, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded", accept: "application/json" },
    body: body.toString(),
  });
  const json: any = await res.json().catch(() => null);
  if (!res.ok || !json?.access_token) {
    throw new Error(`Moneybird token mislukt (${res.status}): ${json?.error_description ?? json?.error ?? "geen uitleg"}`);
  }
  const t: MoneybirdTokens = { accessToken: json.access_token, refreshToken: json.refresh_token, scope: String(json.scope ?? "") };
  if (typeof json.expires_in === "number" && typeof json.created_at === "number") t.verlooptOp = json.created_at + json.expires_in;
  return t;
}

export function wisselCode(app: OAuthApp, code: string, fetchFn: typeof fetch = fetch): Promise<MoneybirdTokens> {
  return tokenVerzoek(app, { code, redirect_uri: app.redirectUri, grant_type: "authorization_code" }, fetchFn);
}

export function ververs(app: OAuthApp, refreshToken: string, fetchFn: typeof fetch = fetch): Promise<MoneybirdTokens> {
  return tokenVerzoek(app, { grant_type: "refresh_token", refresh_token: refreshToken }, fetchFn);
}

export async function trekIn(app: OAuthApp, token: string, fetchFn: typeof fetch = fetch): Promise<void> {
  const body = new URLSearchParams({ client_id: app.clientId, client_secret: app.clientSecret, token });
  const res = await fetchFn(`${MONEYBIRD_OAUTH}/revoke`, { method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" }, body: body.toString() });
  // httpStatus erbij, zodat ontkoppelen een 403 (verkeerde app, niet herhalen) van 5xx en 429 (later opnieuw) kan scheiden.
  if (!res.ok) throw Object.assign(new Error(`Moneybird intrekken mislukt (${res.status})`), { httpStatus: res.status });
}
