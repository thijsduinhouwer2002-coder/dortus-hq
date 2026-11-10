// Gedeelde stukken voor de routes van de schermen (ontwerp-schermen.md versie 3): omgeving, context per verzoek,
// sessie opzoeken, POST-controle (csrf en herkomst), formulier lezen en een scherm tonen.
import { TikTokClient } from "../../../tiktok-shop-basis/src/client.ts";
import { Budget } from "../budget.ts";
import type { Omgeving } from "../worker.ts";
import { pagina } from "./html.ts";
import type { Scherm } from "./schermen.ts";
import { csrfKlopt, herkomstKlopt, leesCookies, leesSessie, SESSIE_COOKIE, type SessieSleutels } from "./sessie.ts";

/** Budget per verzoek (gratis plan: 50 subrequests, D1 telt mee). */
export const WEB_BUDGET = 50;
/** Kort winkelslot voor een route met opgeslagen tokens (ontwerp: 60 s). */
export const WEB_SLOT_DUUR = 60;
/** Volgende_run van een nieuwe winkel: de cron pakt hem pas na "Zet aan" (deel 3). */
export const NOOIT = 253402300799;

export interface WebOmgeving extends Omgeving {
  sessie: SessieSleutels;
  tiktokServiceId: string;
  /** Eigen origin van de app, bijv. `https://klopt.dortus.com`. */
  appAdres: string;
}

export interface Ctx {
  request: Request;
  url: URL;
  o: WebOmgeving;
  nu: number;
  budget: Budget;
  teller: { neem(): void; neemAfmaken(): void };
  /** fetch binnen het budget. */
  fetch: typeof fetch;
  cookies: Record<string, string>;
}

export function maakCtx(request: Request, o: WebOmgeving, nu: number): Ctx {
  const budget = new Budget(WEB_BUDGET);
  return { request, url: new URL(request.url), o, nu, budget, teller: budget.opslagTeller(), fetch: budget.omhul(o.fetchFn), cookies: leesCookies(request) };
}

/** TikTok-client met één poging en geen wachten: de verkoper wacht, en mislukt is niet erg (opnieuw koppelen). */
export function snelleTikTok(c: Ctx): TikTokClient {
  return new TikTokClient({ appKey: c.o.tiktokApp.appKey, appSecret: c.o.tiktokApp.appSecret, fetchFn: c.fetch, nu: () => c.nu, slaap: async () => {}, pogingen: 1 });
}

export function toon(s: Scherm, cookies: string[] = []): Response {
  return pagina({ titel: s.titel, inhoud: s.inhoud, stap: s.stap, status: s.status, kopregels: s.kopregels, cookies });
}

export interface WinkelRij {
  id: string;
  shop_cipher: string | null;
  instellingen: string | null;
  tt_tokens: string | null;
  tt_versie: number;
  mb_tokens: string | null;
  mb_versie: number;
  administratie: string | null;
}

export interface Sessie {
  winkel: WinkelRij;
  /** De ruwe cookiewaarde, voor csrf. */
  cookie: string;
}

/** Geldige sessie: HMAC klopt, niet verlopen, en de winkel bestaat en is gekoppeld. Anders null. */
export async function sessieVan(c: Ctx): Promise<Sessie | null> {
  const cookie = c.cookies[SESSIE_COOKIE];
  const id = await leesSessie(c.o.sessie, cookie, c.nu);
  if (!id || !cookie) return null;
  c.teller.neem();
  const rij = await c.o.db
    .prepare(`SELECT id, shop_cipher, instellingen, tt_tokens, tt_versie, mb_tokens, mb_versie, administratie FROM winkels WHERE id = ? AND ontkoppeld_op IS NULL`)
    .bind(id)
    .first<WinkelRij>();
  return rij ? { winkel: rij, cookie } : null;
}

export function instellingenVan(rij: { instellingen: string | null }): Record<string, any> {
  try {
    const x = rij.instellingen ? JSON.parse(rij.instellingen) : {};
    return x && typeof x === "object" ? x : {};
  } catch {
    return {};
  }
}

/** Formulier (application/x-www-form-urlencoded), hoogstens 8 kB. */
export async function formulier(c: Ctx): Promise<URLSearchParams> {
  const tekst = await c.request.text();
  if (tekst.length > 8192) return new URLSearchParams();
  return new URLSearchParams(tekst);
}

/** POST-controle: herkomst eigen adres en csrf bij deze cookiewaarde. Geeft false als het verzoek geweigerd moet worden (403). */
export async function postKlopt(c: Ctx, cookiewaarde: string | undefined, form: URLSearchParams): Promise<boolean> {
  if (!herkomstKlopt(c.request, c.o.appAdres)) return false;
  return csrfKlopt(c.o.sessie, cookiewaarde, form.get("csrf"));
}

export const foutTekst = (e: unknown) => String((e as Error)?.message ?? e);
