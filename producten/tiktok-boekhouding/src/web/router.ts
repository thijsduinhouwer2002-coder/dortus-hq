// Alles onder /app (ontwerp-schermen.md versie 3, "Waar en hoe"): kiest de route, geeft elk verzoek een eigen budget
// van 50 en vangt onverwachte fouten af zonder iets geheims te tonen. Schrijven alleen met POST (csrf en herkomst in de route).
import { isBudgetOp } from "../budget.ts";
import { tiktokSoort, TokenBron } from "../d1/tokens.ts";
import { formulier, foutTekst, instellingenVan, maakCtx, postKlopt, sessieVan, toon, type Ctx, type WebOmgeving } from "./basis.ts";
import { meldWebhooksAan, tiktokKies, tiktokStart, tiktokTerug } from "./koppelen.ts";
import { kiesAdministratieScherm, moneybirdAdministratie, moneybirdStart, moneybirdTerug, onderSlot, winkelnaam } from "./moneybird.ts";
import { evenGeduld, gekoppeld, koppelScherm, nietVoorJou, uitgelogd } from "./schermen.ts";
import { csrfVan, herkomstKlopt, SESSIE_COOKIE, wisCookie } from "./sessie.ts";
import { stijlAntwoord } from "./stijl.ts";
import { html } from "./html.ts";

export type { WebOmgeving } from "./basis.ts";

export function isAppPad(pad: string): boolean {
  return pad === "/app" || pad.startsWith("/app/");
}

type Route = (c: Ctx) => Response | Promise<Response>;

const ROUTES: Record<string, Route> = {
  "GET /app": appScherm,
  "GET /app/stijl.css": () => stijlAntwoord(),
  "GET /app/tiktok/start": tiktokStart,
  "GET /app/tiktok/terug": tiktokTerug,
  "POST /app/tiktok/kies": tiktokKies,
  "POST /app/moneybird/start": moneybirdStart,
  "GET /app/moneybird/terug": moneybirdTerug,
  "POST /app/moneybird/administratie": moneybirdAdministratie,
  "GET /app/niet-voor-jou": nietVoorJouRoute,
  "POST /app/uit": uitloggen,
};

export async function router(request: Request, o: WebOmgeving, nu: number): Promise<Response> {
  const c = maakCtx(request, o, nu);
  const pad = c.url.pathname.replace(/\/+$/, "") || "/";
  const route = ROUTES[`${request.method} ${pad}`];
  if (!route) {
    const bestaat = Object.keys(ROUTES).some((k) => k.endsWith(` ${pad}`));
    return toon({ titel: "Niet gevonden", status: bestaat ? 405 : 404, inhoud: html`<h1>Deze pagina bestaat niet</h1><p><a href="/app">Naar Klopt</a></p>` });
  }
  try {
    return await route(c);
  } catch (e) {
    if (isBudgetOp(e)) return toon(evenGeduld());
    o.log(`web: ${request.method} ${pad} mislukt: ${foutTekst(e)}`);
    return toon({ titel: "Er ging iets mis", status: 500, inhoud: html`<h1>Er ging iets mis</h1><p class="zacht">Probeer het zo nog eens.</p><p><a href="/app">Naar Klopt</a></p>` });
  }
}

/** GET /app: het scherm uit de stand van de winkel. */
async function appScherm(c: Ctx): Promise<Response> {
  const s = await sessieVan(c);
  if (!s) return toon(uitgelogd(), c.cookies[SESSIE_COOKIE] ? [wisCookie(SESSIE_COOKIE)] : []);
  const inst = instellingenVan(s.winkel);
  if (inst.webhooks === 0 && s.winkel.shop_cipher) {
    // Eén nieuwe poging, alleen onder het slot met de opgeslagen tokens; slot bezet: deze keer overslaan.
    const cipher = s.winkel.shop_cipher;
    try {
      await onderSlot(c, s.winkel.id, async () => {
        const bron = new TokenBron({ db: c.o.db, winkel: s.winkel.id, soort: tiktokSoort(c.o.tiktokApp), sleutels: c.o.sleutels, budget: c.budget, fetchFn: c.o.fetchFn, nu: () => c.nu, log: c.o.log });
        await bron.vanRij(s.winkel.tt_tokens, s.winkel.tt_versie);
        const { tokens } = await bron.geef();
        await meldWebhooksAan(c, s.winkel.id, tokens.accessToken, cipher);
      });
    } catch (e) {
      c.o.log(`web: webhooks opnieuw aanmelden voor winkel ${s.winkel.id} mislukt: ${foutTekst(e)}`);
    }
  }
  if (!s.winkel.mb_tokens) return toon(koppelScherm({ winkelnaam: winkelnaam(s.winkel), csrf: await csrfVan(c.o.sessie, s.cookie) }));
  if (!s.winkel.administratie) return kiesAdministratieScherm(c, s);
  return toon(gekoppeld(winkelnaam(s.winkel)));
}

function nietVoorJouRoute(c: Ctx): Response {
  if (c.url.searchParams.get("voor") !== "exact") return toon({ titel: "Niet gevonden", status: 404, inhoud: html`<h1>Deze pagina bestaat niet</h1>` });
  return toon(nietVoorJou({ soort: "exact" }));
}

/** POST /app/uit: alleen van ons eigen adres; wist het cookie (gedeelde computers). */
async function uitloggen(c: Ctx): Promise<Response> {
  const form = await formulier(c);
  const cookie = c.cookies[SESSIE_COOKIE];
  const goed = cookie ? await postKlopt(c, cookie, form) : herkomstKlopt(c.request, c.o.appAdres);
  if (!goed) return new Response("Geweigerd", { status: 403 });
  return toon(uitgelogd(), [wisCookie(SESSIE_COOKIE)]);
}
