// HTML van scherm 1 (koppelen) en de staten eromheen (ontwerp-schermen.md versie 3; schetsen kunst/1-koppelen.png en
// kunst/4-staten.png). Alleen opbouw en tekst: de routes in koppelen.ts en moneybird.ts kiezen welk scherm en geven het aan `pagina`.
// Alle teksten van een scherm staan hier bij elkaar, zodat Engels er later naast kan.

import { html, type Html } from "./html.ts";

export interface Scherm {
  titel: string;
  inhoud: Html;
  stap?: { nu: number; van: number };
  status?: number;
}

const STAP1 = { nu: 1, van: 3 };
export const START_TIKTOK = "/app/tiktok/start";
export const SUPPORT = "thijs@dortus.com";

/** Landen waar TikTok Shop in de EU (en het VK) zit, in gewone woorden; onbekend blijft de code. */
const LANDEN: Record<string, string> = {
  DE: "Duitsland", FR: "Frankrijk", IT: "Italië", ES: "Spanje", IE: "Ierland", GB: "het Verenigd Koninkrijk", UK: "het Verenigd Koninkrijk",
  BE: "België", AT: "Oostenrijk", PL: "Polen", PT: "Portugal", NL: "Nederland",
};
export function landNaam(code: string): string {
  return LANDEN[code.toUpperCase()] ?? code.toUpperCase();
}

const knopLink = (adres: string, tekst: string) => html`<a class="knop knop-hoofd" href="${adres}">${tekst}</a>`;
const verborgenCsrf = (csrf: string) => html`<input type="hidden" name="csrf" value="${csrf}">`;

/** Rustige staat: teken, één vette zin, één zin uitleg, hoogstens één knop (Daan, punt 4). */
function staat(teken: string, kop: string, uitleg: string, knop?: Html): Html {
  return html`<section class="staat"><div class="teken" aria-hidden="true">${teken}</div><h1>${kop}</h1><p class="zacht">${uitleg}</p>${knop ?? ""}</section>`;
}

export interface KoppelGegevens {
  winkelnaam: string;
  csrf: string;
  /** Zachte zin bovenaan, bijvoorbeeld na een weigering bij Moneybird. */
  melding?: string;
}

/** Scherm 1: TikTok Shop al gekoppeld, Moneybird nog niet. */
export function koppelScherm(g: KoppelGegevens): Scherm {
  return {
    titel: "Koppel je boekhouding",
    stap: STAP1,
    inhoud: html`<h1>Koppel je boekhouding</h1>
<p class="zacht">Daarna zie je meteen hoe je laatste uitbetalingen geboekt worden. Er gaat nog niets naar Moneybird.</p>
${g.melding ? html`<p class="pil pil-apart">${g.melding}</p>` : ""}
<div class="blokken">
<section class="kaart"><h2>TikTok Shop</h2><p><span class="stip stip-goed"></span>${g.winkelnaam} · gekoppeld</p><p class="pil pil-goed">Klaar</p></section>
<section class="kaart"><h2>Moneybird</h2><p><span class="stip stip-uit"></span>Je boekhouding</p>
<form method="post" action="/app/moneybird/start">${verborgenCsrf(g.csrf)}<button class="knop knop-hoofd" type="submit">Koppel Moneybird</button></form>
<p class="zacht">We vragen Moneybird om boekingen te maken en je grootboekrekeningen te lezen en aan te maken.</p></section>
</div>
<p class="zacht">Geen Moneybird? <a href="/app/niet-voor-jou?voor=exact">Zet je op de wachtlijst voor Exact</a></p>`,
  };
}

export type NietVoorJou = { soort: "land"; land: string } | { soort: "exact" } | { soort: "geen_administratie" } | { soort: "geen_nl_administratie" };

/** "Nog niet voor jou": wachtlijst via mail, wij bewaren geen e-mailadressen. */
export function nietVoorJou(n: NietVoorJou): Scherm {
  let kop: string, uitleg: string, onderwerp: string, teken = "NL";
  if (n.soort === "land") {
    kop = "Nu alleen voor Nederlandse winkels";
    uitleg = `Je winkel staat in ${landNaam(n.land)}. We breiden uit per land.`;
    onderwerp = `Wachtlijst Klopt: ${landNaam(n.land)}`;
  } else if (n.soort === "exact") {
    kop = "Klopt werkt nu alleen met Moneybird";
    uitleg = "Exact komt misschien later. Hoe meer mensen erom vragen, hoe eerder.";
    onderwerp = "Wachtlijst Klopt: Exact";
    teken = "M";
  } else if (n.soort === "geen_administratie") {
    kop = "We vonden geen Moneybird-administratie";
    uitleg = "Maak eerst een administratie aan in Moneybird en koppel daarna opnieuw.";
    onderwerp = "Klopt: geen administratie";
    teken = "M";
  } else {
    kop = "Geen Nederlandse administratie in euro";
    uitleg = "Klopt boekt nu alleen in een Nederlandse Moneybird-administratie in euro.";
    onderwerp = "Wachtlijst Klopt: andere administratie";
  }
  const mail = `mailto:${SUPPORT}?subject=${encodeURIComponent(onderwerp)}`;
  return {
    titel: kop,
    inhoud: staat(teken, kop, `${uitleg} Mail ons, dan hoor je het als Klopt voor jou werkt.`, knopLink(mail, "Mail ons")),
  };
}

/** Foutstaat zonder belofte dat we het vanzelf opnieuw proberen (dat doen we bij koppelen niet). */
export function foutBijKoppelen(kant: "TikTok" | "Moneybird"): Scherm {
  return {
    titel: `${kant} gaf geen antwoord`,
    status: 502,
    inhoud: staat("!", `${kant} gaf geen antwoord`, "Dat ligt niet aan jou. Probeer het zo nog eens.", knopLink(START_TIKTOK, "Opnieuw koppelen")),
  };
}

/** Na een weigering bij TikTok (Moneybird gaat terug naar scherm 1 met een melding). */
export function weigeringTikTok(): Scherm {
  return {
    titel: "Geen toestemming",
    inhoud: staat("!", "Je gaf TikTok Shop geen toestemming", "Zonder toestemming kan Klopt je uitbetalingen niet lezen.", knopLink(START_TIKTOK, "Opnieuw koppelen")),
  };
}

/** Geen (geldige) sessie: nooit gegevens van een winkel tonen. */
export function uitgelogd(): Scherm {
  return {
    titel: "Open Klopt vanuit TikTok Shop",
    status: 401,
    inhoud: staat("✓", "Open Klopt vanuit TikTok Shop", "Je logt in via TikTok Shop. Wachtwoorden hebben we niet.", knopLink(START_TIKTOK, "Inloggen met TikTok Shop")),
  };
}

/** Na installeren zonder onze state: tokens staan, maar eerst zelf inloggen (tegen login-CSRF). */
export function openAls(winkelnaam: string): Scherm {
  return {
    titel: "Open Klopt",
    inhoud: staat("✓", `Open Klopt als ${winkelnaam}`, "Bevestig even via TikTok Shop dat jij het bent.", knopLink(START_TIKTOK, "Doorgaan met TikTok Shop")),
  };
}

export function evenGeduld(): Scherm {
  return {
    titel: "Even geduld",
    status: 503,
    inhoud: staat("…", "Even geduld", "Klopt is net bezig met je winkel. Probeer het over een minuut opnieuw.", knopLink("/app", "Vernieuwen")),
  };
}

export function kiesWinkel(shops: Array<{ id: string; naam: string }>, csrf: string): Scherm {
  return {
    titel: "Kies je winkel",
    stap: STAP1,
    inhoud: html`<h1>Kies je winkel</h1><p class="zacht">Eén abonnement is voor één winkel. Welke koppel je met Klopt?</p>
<form method="post" action="/app/tiktok/kies" class="kaart">${verborgenCsrf(csrf)}<ul class="lijst">${shops.map(
      (s, i) => html`<li><label><input type="radio" name="shop" value="${s.id}"${i === 0 ? html` checked` : ""}> ${s.naam}</label></li>`,
    )}</ul><button class="knop knop-hoofd" type="submit">Koppel deze winkel</button></form>`,
  };
}

export function kiesAdministratie(adms: Array<{ id: string; naam: string }>, csrf: string): Scherm {
  return {
    titel: "Kies je administratie",
    stap: STAP1,
    inhoud: html`<h1>Kies je administratie</h1><p class="zacht">In welke Moneybird-administratie boekt Klopt je TikTok-uitbetalingen?</p>
<form method="post" action="/app/moneybird/administratie" class="kaart">${verborgenCsrf(csrf)}<ul class="lijst">${adms.map(
      (a, i) => html`<li><label><input type="radio" name="administratie" value="${a.id}"${i === 0 ? html` checked` : ""}> ${a.naam}</label></li>`,
    )}</ul><button class="knop knop-hoofd" type="submit">Kies deze administratie</button></form>`,
  };
}

/** Tot deel 2 (proef) er is. */
export function gekoppeld(winkelnaam: string): Scherm {
  return { titel: "Gekoppeld", stap: STAP1, inhoud: staat("✓", "Gekoppeld", `${winkelnaam} en Moneybird zijn gekoppeld. De proef volgt in de volgende stap.`) };
}
