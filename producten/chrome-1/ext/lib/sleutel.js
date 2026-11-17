// Licentiesleutel van Gumroad controleren, zonder eigen server.
// Ontwerp: producten/chrome-1/ontwerp.md, deel "Sleutel en betalen".
// Alles wat van buiten komt (fetch, tijd, opslag) wordt meegegeven, zodat het los te testen is.

export const GUMROAD_URL = "https://api.gumroad.com/v2/licenses/verify";
export const DAG = 24 * 60 * 60 * 1000;
export const UITSTEL_BIJ_STORING = 30 * DAG; // les Lars, verhaal 29
export const TIJDSLIMIET_MS = 10000;

export const MELDINGEN = {
  goed: "Pro staat aan. Dank je wel!",
  onbekend: "Deze sleutel kennen we niet. Kijk of je hem helemaal goed hebt geplakt, of kopieer hem opnieuw uit de mail van Gumroad.",
  terugbetaald: "Deze aankoop is terugbetaald, dus Pro staat uit. Klopt dat niet? Mail thijs@dortus.com.",
  gestopt: "Je abonnement is gestopt, dus Pro staat uit. Je kunt het opnieuw starten via Gumroad.",
  betaling_mislukt: "De laatste betaling van je abonnement is niet gelukt, dus Pro staat uit. Pas je betaling aan bij Gumroad.",
  storing: "We konden je sleutel even niet controleren (Gumroad antwoordt niet). Pro blijft gewoon aan; we proberen het later opnieuw.",
  storing_nieuw: "We konden je sleutel even niet controleren (Gumroad antwoordt niet). Probeer het over een minuut opnieuw.",
  storing_te_lang: "We konden je sleutel al 30 dagen niet controleren. Pro staat uit tot dat weer lukt. Ga online en klik op 'Opnieuw controleren'.",
  leeg: "Plak eerst je sleutel.",
};

const NEE_REDENEN = ["onbekend", "terugbetaald", "gestopt", "betaling_mislukt", "leeg"];

// Gumroad zegt nee met { success: false, message: "..." } (GEZIEN 17 nov bij een 404).
function isNeeVanGumroad(json) {
  return !!json && json.success === false && typeof json.message === "string" && json.message.length > 0;
}

// Sleutels van Gumroad bevatten geen spaties; geplakt over meer regels haalt alle witruimte weg.
export function normaliseer(sleutel) {
  if (sleutel === null || sleutel === undefined) return "";
  return String(sleutel).replace(/[\s\u200B-\u200D\u2060\uFEFF]+/g, "");
}

function inVerleden(waarde, nu) {
  if (!waarde) return false;
  const t = Date.parse(waarde);
  return Number.isFinite(t) ? t <= nu : true; // onleesbare datum telt als gezet
}

// Beoordeelt het antwoord van Gumroad. Geeft { uitslag: "goed" | "nee", reden }.
export function beoordeel(json, nu) {
  // Alleen een echt antwoord van Gumroad telt; een onverwacht antwoord is een storing, geen nee.
  if (isNeeVanGumroad(json)) return { uitslag: "nee", reden: "onbekend" };
  if (!json || json.success !== true || !json.purchase || typeof json.purchase !== "object") return { uitslag: "storing", reden: "storing" };
  const p = json.purchase;
  if (p.refunded === true || p.disputed === true || p.chargebacked === true) return { uitslag: "nee", reden: "terugbetaald" };
  // Volgens Gumroad (artikel 76, GEZIEN 17 nov) zijn alle drie de EINDDATUM van het lidmaatschap,
  // niet het moment van opzeggen. Tot die datum is er betaald, dus pas daarna telt het.
  if (inVerleden(p.subscription_failed_at, nu)) return { uitslag: "nee", reden: "betaling_mislukt" };
  if (inVerleden(p.subscription_cancelled_at, nu) || inVerleden(p.subscription_ended_at, nu)) return { uitslag: "nee", reden: "gestopt" };
  return { uitslag: "goed", reden: "goed" };
}

// Eén controle bij Gumroad voor één product. Geeft { uitslag: "goed" | "nee" | "storing", reden }.
async function vraagGumroad(productId, sleutel, { fetch, nu, tijdslimietMs = TIJDSLIMIET_MS }) {
  const ctrl = typeof AbortController !== "undefined" ? new AbortController() : null;
  const timer = ctrl ? setTimeout(() => ctrl.abort(), tijdslimietMs) : null;
  try {
    const body = new URLSearchParams({ product_id: productId, license_key: sleutel, increment_uses_count: "false" });
    const res = await fetch(GUMROAD_URL, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: body.toString(),
      signal: ctrl ? ctrl.signal : undefined,
    });
    if (res.status === 429 || res.status >= 500) return { uitslag: "storing", reden: "storing" };
    let json = null;
    try { json = await res.json(); } catch { return { uitslag: "storing", reden: "storing" }; }
    // Een 404 of andere 4xx telt alleen als nee met het echte foutantwoord van Gumroad erin,
    // niet als het een pagina van een proxy of wifi-inlog is.
    if (!res.ok) return isNeeVanGumroad(json) ? { uitslag: "nee", reden: "onbekend" } : { uitslag: "storing", reden: "storing" };
    return beoordeel(json, nu);
  } catch {
    return { uitslag: "storing", reden: "storing" }; // geen netwerk, time-out, CORS
  } finally {
    if (timer) clearTimeout(timer);
  }
}

// Probeert elk product (bijvoorbeeld abonnement en levenslang). Goed bij één product is genoeg.
export async function controleer(sleutel, productIds, deps) {
  const s = normaliseer(sleutel);
  if (!s) return { uitslag: "nee", reden: "leeg" };
  if (!Array.isArray(productIds) || productIds.length === 0) return { uitslag: "storing", reden: "storing" }; // instelling ontbreekt: nooit Pro afpakken
  let storing = false;
  let nee = null;
  for (const id of productIds) {
    const r = await vraagGumroad(id, s, deps);
    if (r.uitslag === "goed") return { ...r, productId: id };
    if (r.uitslag === "storing") storing = true;
    else if (!nee || nee.reden === "onbekend") nee = r;
  }
  // Een echte uitspraak (terugbetaald, gestopt) gaat voor; bij alleen "onbekend" plus storing weten we het niet.
  if (nee && nee.reden !== "onbekend") return nee;
  if (storing) return { uitslag: "storing", reden: "storing" };
  return nee || { uitslag: "nee", reden: "onbekend" };
}

// Wat de extensie bewaart: { sleutel, productId, laatsteGoed, laatsteControle, reden }.
// Pro staat aan als de laatste goede controle niet ouder is dan het uitstel, en er sindsdien geen "nee" kwam.
export function isPro(rec, nu) {
  if (!rec || !rec.sleutel || !rec.laatsteGoed) return false;
  if (rec.reden && rec.reden !== "goed" && rec.reden !== "storing") return false;
  return nu - rec.laatsteGoed <= UITSTEL_BIJ_STORING; // een datum in de toekomst: zie moetControleren en verwerk
}

export function melding(rec, nu) {
  if (!rec || !rec.sleutel) return null;
  if (isPro(rec, nu)) return rec.reden === "storing" ? MELDINGEN.storing : MELDINGEN.goed;
  if (rec.laatsteGoed && (rec.reden === "goed" || rec.reden === "storing")) return MELDINGEN.storing_te_lang;
  if (!rec.laatsteGoed && rec.reden === "storing") return MELDINGEN.storing_nieuw;
  return MELDINGEN[rec.reden] || MELDINGEN.onbekend;
}

// Werkt het bewaarde record bij met een nieuwe uitslag. Zuiver: geeft een nieuw record terug.
export function verwerk(rec, sleutelRuw, uitslag, nu) {
  const sleutel = normaliseer(sleutelRuw);
  const zelfde = rec && rec.sleutel === sleutel;
  const basis = zelfde ? { ...rec } : { sleutel, productId: null, laatsteGoed: null };
  basis.laatsteControle = nu;
  if (uitslag.uitslag === "goed") {
    basis.laatsteGoed = nu;
    basis.productId = uitslag.productId || basis.productId;
    basis.reden = "goed";
  } else if (uitslag.uitslag === "storing") {
    // laatsteGoed blijft staan, maar nooit later dan nu (klok die vooruit stond geeft geen extra tijd).
    if (basis.laatsteGoed && basis.laatsteGoed > nu) basis.laatsteGoed = nu;
    // Na een duidelijk nee blijft die reden staan, zodat de gebruiker de echte uitleg ziet.
    if (!(zelfde && NEE_REDENEN.includes(basis.reden))) basis.reden = "storing";
  } else {
    basis.reden = uitslag.reden;
    basis.laatsteGoed = null; // een duidelijk nee haalt Pro weg
  }
  return basis;
}

// Achtergrondcontrole: hooguit één keer per dag, en vaker alleen als de vorige een storing was (na een uur).
export function moetControleren(rec, nu) {
  if (!rec || !rec.sleutel) return false;
  if (!rec.laatsteControle) return true;
  if (rec.laatsteControle > nu || (rec.laatsteGoed && rec.laatsteGoed > nu)) return true; // klok verzet
  const wacht = rec.reden === "storing" ? 60 * 60 * 1000 : DAG;
  return nu - rec.laatsteControle >= wacht;
}
