// Sessie, CSRF, state en het keuze-cookie voor de schermen (ontwerp-schermen.md versie 3, kop "Sessie, CSRF en state").
// Inloggen gaat alleen via TikTok; deze module maakt en controleert alleen de cookies. Alles met Web Crypto, geen afhankelijkheden.

/** Sleutels per versie (ruwe bytes uit het Worker-secret `SESSIE_SLEUTELS`), `huidig` om mee te tekenen. */
export interface SessieSleutels {
  huidig: string;
  sleutels: Record<string, Uint8Array>;
}

export const SESSIE_COOKIE = "__Host-klopt";
export const TT_STATE_COOKIE = "__Host-klopt_tt";
export const MB_STATE_COOKIE = "__Host-klopt_mb";
export const KEUZE_COOKIE = "__Host-klopt_keuze";
export const SESSIE_DUUR = 30 * 24 * 3600;
export const KORT = 10 * 60;

const enc = new TextEncoder();
const DEEL = /^[A-Za-z0-9_-]+$/;

function b64url(b: Uint8Array): string {
  return btoa(Array.from(b, (x) => String.fromCharCode(x)).join("")).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function vanB64url(s: string): Uint8Array {
  const t = s.replace(/-/g, "+").replace(/_/g, "/");
  return Uint8Array.from(atob(t + "=".repeat((4 - (t.length % 4)) % 4)), (c) => c.charCodeAt(0));
}

function ruweSleutel(bos: SessieSleutels, versie: string): Uint8Array | null {
  if (!DEEL.test(versie) || !Object.hasOwn(bos.sleutels, versie)) return null;
  const k = bos.sleutels[versie];
  return k.length >= 32 ? k : null;
}

async function mac(sleutel: Uint8Array, data: string): Promise<string> {
  const k = await crypto.subtle.importKey("raw", sleutel, { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return b64url(new Uint8Array(await crypto.subtle.sign("HMAC", k, enc.encode(data))));
}

/** Vergelijken in vaste tijd (bij gelijke lengte). */
export function zelfde(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let v = 0;
  for (let i = 0; i < a.length; i++) v |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return v === 0;
}

// ---- sessie ----

/** `versie.winkel.verloopt.mac`; de winkel-id mag geen punt bevatten (wij maken uuid's). */
export async function maakSessie(bos: SessieSleutels, winkel: string, nu: number): Promise<string> {
  const k = ruweSleutel(bos, bos.huidig);
  if (!k) throw new Error("sessiesleutel ontbreekt of is te kort");
  if (!DEEL.test(winkel)) throw new Error("ongeldige winkel-id voor een sessie");
  const kern = `${bos.huidig}.${winkel}.${nu + SESSIE_DUUR}`;
  return `${kern}.${await mac(k, "sessie." + kern)}`;
}

/** Geeft de winkel-id als het cookie echt van ons is en niet verlopen; anders null. Of de winkel nog gekoppeld is, kijkt de router na. */
export async function leesSessie(bos: SessieSleutels, waarde: string | undefined, nu: number): Promise<string | null> {
  const d = waarde?.split(".");
  if (!d || d.length !== 4 || !DEEL.test(d[1]) || !/^\d{1,12}$/.test(d[2])) return null;
  const k = ruweSleutel(bos, d[0]);
  if (!k) return null;
  if (!zelfde(await mac(k, "sessie." + d.slice(0, 3).join(".")), d[3])) return null;
  return Number(d[2]) > nu ? d[1] : null;
}

// ---- csrf ----

/** HMAC over de cookiewaarde (sessie of keuze), met de sleutel van de versie vooraan in die waarde. */
export async function csrfVan(bos: SessieSleutels, cookiewaarde: string): Promise<string> {
  const k = ruweSleutel(bos, cookiewaarde.split(".")[0]);
  if (!k) throw new Error("onbekende sleutelversie in cookie");
  return mac(k, "csrf." + cookiewaarde);
}

export async function csrfKlopt(bos: SessieSleutels, cookiewaarde: string | undefined, veld: string | null | undefined): Promise<boolean> {
  if (!cookiewaarde || !veld || !ruweSleutel(bos, cookiewaarde.split(".")[0])) return false;
  return zelfde(await csrfVan(bos, cookiewaarde), veld);
}

/** Origin, of anders Referer, moet ons eigen adres zijn; geen van beide is ook nee. */
export function herkomstKlopt(request: Request, appAdres: string): boolean {
  const eigen = new URL(appAdres).origin;
  const origin = request.headers.get("origin");
  if (origin) return origin === eigen;
  const referer = request.headers.get("referer");
  if (!referer) return false;
  try {
    return new URL(referer).origin === eigen;
  } catch {
    return false;
  }
}

// ---- state voor Moneybird, gebonden aan de winkel ----

export async function maakMbState(bos: SessieSleutels, state: string, winkel: string): Promise<string> {
  const k = ruweSleutel(bos, bos.huidig);
  if (!k || !DEEL.test(state) || !DEEL.test(winkel)) throw new Error("ongeldige state of winkel");
  const kern = `${bos.huidig}.${state}.${winkel}`;
  return `${kern}.${await mac(k, "mb." + kern)}`;
}

/** Geeft de state alleen terug als het cookie van ons is en bij deze winkel hoort. */
export async function leesMbState(bos: SessieSleutels, waarde: string | undefined, winkel: string): Promise<string | null> {
  const d = waarde?.split(".");
  if (!d || d.length !== 4) return null;
  const k = ruweSleutel(bos, d[0]);
  if (!k || !zelfde(await mac(k, "mb." + d.slice(0, 3).join(".")), d[3])) return null;
  return d[2] === winkel ? d[1] : null;
}

// ---- keuze-cookie (meer dan één NL-winkel): versleuteld, eigen sleutel via HKDF ----

export interface Keuze {
  tokens: unknown;
  shops: Array<{ id: string; cipher: string; naam: string }>;
  openId: string;
  stateKlopte: boolean;
  verloopt: number;
}

async function keuzeSleutel(ruw: Uint8Array): Promise<CryptoKey> {
  const basis = await crypto.subtle.importKey("raw", ruw, "HKDF", false, ["deriveKey"]);
  return crypto.subtle.deriveKey(
    { name: "HKDF", hash: "SHA-256", salt: new Uint8Array(0), info: enc.encode("keuze") },
    basis,
    { name: "AES-GCM", length: 256 },
    false,
    ["encrypt", "decrypt"],
  );
}

export async function maakKeuze(bos: SessieSleutels, k: Omit<Keuze, "verloopt">, nu: number): Promise<string> {
  const ruw = ruweSleutel(bos, bos.huidig);
  if (!ruw) throw new Error("sessiesleutel ontbreekt of is te kort");
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const data = await crypto.subtle.encrypt(
    { name: "AES-GCM", iv, additionalData: enc.encode("keuze." + bos.huidig) },
    await keuzeSleutel(ruw),
    enc.encode(JSON.stringify({ ...k, verloopt: nu + KORT })),
  );
  return `${bos.huidig}.${b64url(iv)}.${b64url(new Uint8Array(data))}`;
}

export async function leesKeuze(bos: SessieSleutels, waarde: string | undefined, nu: number): Promise<Keuze | null> {
  const d = waarde?.split(".");
  if (!d || d.length !== 3) return null;
  const ruw = ruweSleutel(bos, d[0]);
  if (!ruw) return null;
  try {
    const tekst = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv: vanB64url(d[1]), additionalData: enc.encode("keuze." + d[0]) },
      await keuzeSleutel(ruw),
      vanB64url(d[2]),
    );
    const k = JSON.parse(new TextDecoder().decode(tekst)) as Keuze;
    return typeof k.verloopt === "number" && k.verloopt > nu ? k : null;
  } catch {
    return null;
  }
}

// ---- cookies ----

/** Alle cookies van de app: `__Host-`, dus Secure, Path=/ en geen Domain. */
export function zetCookie(naam: string, waarde: string, maxAge: number): string {
  return `${naam}=${waarde}; Max-Age=${maxAge}; Path=/; HttpOnly; Secure; SameSite=Lax`;
}

export function wisCookie(naam: string): string {
  return zetCookie(naam, "", 0);
}

export function leesCookies(request: Request): Record<string, string> {
  const uit: Record<string, string> = {};
  for (const deel of (request.headers.get("cookie") ?? "").split(";")) {
    const i = deel.indexOf("=");
    if (i <= 0) continue;
    const naam = deel.slice(0, i).trim();
    if (!Object.hasOwn(uit, naam)) uit[naam] = deel.slice(i + 1).trim();
  }
  return uit;
}
