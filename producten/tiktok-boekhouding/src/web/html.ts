// HTML maken met verplicht escapen, het omhulsel van elke pagina en de kopregels (ontwerp-schermen.md, "Waar en hoe").
// Alles wat in `html\`...\`` wordt ingevoegd wordt ge-escaped, behalve een waarde die zelf al `Html` is.

import { STIJL_PAD } from "./stijl.ts";

export class Html {
  readonly tekst: string;
  constructor(tekst: string) {
    this.tekst = tekst;
  }
  toString(): string {
    return this.tekst;
  }
}

export function esc(s: unknown): string {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function invoeg(w: unknown): string {
  if (w instanceof Html) return w.tekst;
  if (Array.isArray(w)) return w.map(invoeg).join("");
  if (w === null || w === undefined || w === false) return "";
  return esc(w);
}

export function html(delen: TemplateStringsArray, ...waarden: unknown[]): Html {
  let uit = delen[0];
  for (let i = 0; i < waarden.length; i++) uit += invoeg(waarden[i]) + delen[i + 1];
  return new Html(uit);
}

export const CSP = [
  "default-src 'self'",
  "style-src 'self'",
  "font-src 'self'",
  "img-src 'self' data:",
  "form-action 'self' https://moneybird.com",
  "base-uri 'none'",
  "object-src 'none'",
  "frame-ancestors 'self'",
].join("; ");

/** Kopregels voor elke pagina (niet voor `stijl.css`, die mag lang in de cache). */
export function kopregels(extra: Record<string, string> = {}): Headers {
  const h = new Headers({
    "content-type": "text/html; charset=utf-8",
    "content-security-policy": CSP,
    "x-content-type-options": "nosniff",
    "referrer-policy": "same-origin",
    "cache-control": "no-store",
    "strict-transport-security": "max-age=31536000",
  });
  for (const [k, v] of Object.entries(extra)) h.set(k, v);
  return h;
}

export interface PaginaOpties {
  titel: string;
  inhoud: Html;
  /** "Stap 1 van 3" bovenaan, zoals de schets. */
  stap?: { nu: number; van: number };
  status?: number;
  cookies?: string[];
}

export function pagina(o: PaginaOpties): Response {
  const stap = o.stap ? html`<p class="stap">Stap ${o.stap.nu} van ${o.stap.van}</p>` : "";
  const body = html`<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${o.titel} · Klopt</title>
<link rel="stylesheet" href="${new Html(STIJL_PAD)}">
</head>
<body>
<header class="kop"><span class="merk">Klopt</span></header>
<main class="vlak">
${stap}${o.inhoud}
</main>
</body>
</html>`;
  const h = kopregels();
  for (const c of o.cookies ?? []) h.append("set-cookie", c);
  return new Response(body.tekst, { status: o.status ?? 200, headers: h });
}

/** Buiten de app alleen naar inloggen bij TikTok en Moneybird (geen open doorverwijzing). */
const BUITEN = ["https://services.tiktokshop.com/", "https://moneybird.com/oauth/"];

/** Doorsturen, met cookies. Alleen naar `/app...` of een adres uit BUITEN. */
export function naar(adres: string, cookies: string[] = []): Response {
  const binnen = adres === "/app" || adres.startsWith("/app/") || adres.startsWith("/app?");
  if (!binnen && !BUITEN.some((b) => adres.startsWith(b))) throw new Error(`doorsturen naar ${adres} niet toegestaan`);
  const h = kopregels({ location: adres });
  h.delete("content-type");
  for (const c of cookies) h.append("set-cookie", c);
  return new Response(null, { status: 302, headers: h });
}
