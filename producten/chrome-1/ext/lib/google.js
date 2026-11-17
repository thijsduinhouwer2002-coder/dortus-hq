// Inloggen bij Google en praten met de Calendar-API, zonder eigen server.
// Ontwerp: producten/chrome-1/ontwerp.md, deel "Hoe het aansluit".
// Alles van buiten (fetch, token halen, wachten) wordt meegegeven: één plek om na te bootsen in tests.

export const API = "https://www.googleapis.com/calendar/v3";
export const AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth";
export const SCOPES = [
  "https://www.googleapis.com/auth/calendar.events",
  "https://www.googleapis.com/auth/calendar.calendarlist.readonly",
];
export const WACHTTIJDEN_MS = [1000, 2000, 4000, 8000]; // opnieuw proberen, ontwerp: 1, 2, 4, 8 s
export const TIJDSLIMIET_MS = 30000;
export const MAX_PAGINAS = 200; // 200 x 2.500 afspraken; beschermt tegen een API die steeds een nextPageToken geeft

export const MELDINGEN = {
  quota: "Google laat je even niet meer wijzigen. Wat gedaan is, blijft gedaan. Probeer het later opnieuw.",
  quota_lezen: "Google laat je even niets meer ophalen. Probeer het over een paar minuten opnieuw.",
  onzeker: "Google antwoordde niet. Deze afspraak is misschien toch al veranderd. Ververs de lijst om te zien hoe hij nu staat.",
  inloggen: "Je bent niet meer verbonden met Google. Klik op 'Opnieuw verbinden'.",
  geen_toegang: "Je mag deze agenda of afspraak niet wijzigen.",
  niet_gevonden: "Deze afspraak bestaat niet meer. Misschien is hij net ergens anders veranderd.",
  netwerk: "Google antwoordt even niet. Je afspraken zijn niet veranderd. Probeer het over een minuut opnieuw.",
  onbekend: "Er ging iets mis bij Google. Probeer het opnieuw.",
};

export class GoogleFout extends Error {
  constructor(soort, status, reden) {
    super(MELDINGEN[soort] || MELDINGEN.onbekend);
    this.soort = soort;
    this.status = status;
    this.reden = reden || null;
  }
}

// ---------- Inloggen (chrome.identity.launchWebAuthFlow, impliciete flow) ----------

export function maakAuthUrl({ clientId, redirectUri, state, stil = false, loginHint }) {
  if (!clientId || !redirectUri || !state) throw new Error("clientId, redirectUri en state zijn nodig");
  const p = new URLSearchParams({
    client_id: clientId,
    redirect_uri: redirectUri,
    response_type: "token",
    scope: SCOPES.join(" "),
    state,
    include_granted_scopes: "true",
  });
  if (stil) p.set("prompt", "none");
  if (loginHint) p.set("login_hint", loginHint);
  return `${AUTH_URL}?${p.toString()}`;
}

// Leest het token uit de redirect-URL. Geeft { token, verlooptOp } of gooit een GoogleFout("inloggen").
export function leesToken(redirectUrl, verwachteState, nu) {
  let u;
  try { u = new URL(redirectUrl); } catch { throw new GoogleFout("inloggen", 0, "geen_url"); }
  const p = new URLSearchParams((u.hash || "").replace(/^#/, ""));
  const fout = p.get("error") || u.searchParams.get("error");
  if (fout) throw new GoogleFout("inloggen", 0, fout);
  if (p.get("state") !== verwachteState) throw new GoogleFout("inloggen", 0, "state");
  const token = p.get("access_token");
  if (!token) throw new GoogleFout("inloggen", 0, "geen_token");
  // Niet elke scope is aangevinkt: zonder calendar.events kunnen we niets wijzigen.
  const scope = p.get("scope");
  if (scope && !scope.split(/\s+/).includes(SCOPES[0])) throw new GoogleFout("inloggen", 0, "scope");
  const sec = Number(p.get("expires_in"));
  const geldig = Number.isFinite(sec) && sec > 0 ? sec : 3600;
  return { token, verlooptOp: nu + Math.max(0, geldig - 60) * 1000 }; // een minuut eerder vernieuwen
}

// ---------- API ----------

function redenUit(json) {
  const e = json && json.error;
  if (!e) return null;
  if (Array.isArray(e.errors) && e.errors[0] && e.errors[0].reason) return e.errors[0].reason;
  return typeof e.status === "string" ? e.status : null;
}

const OPNIEUW_403 = new Set(["rateLimitExceeded", "userRateLimitExceeded"]);

// deps: { fetch, haalToken({ stil }) -> Promise<string>, slaap(ms) -> Promise, tijdslimietMs }
export function maakGoogle(deps) {
  const { fetch, haalToken, slaap = (ms) => new Promise((r) => setTimeout(r, ms)), tijdslimietMs = TIJDSLIMIET_MS } = deps;
  let token = null;

  async function eenKeer(method, url, body) {
    const ctrl = typeof AbortController !== "undefined" ? new AbortController() : null;
    const timer = ctrl ? setTimeout(() => ctrl.abort(), tijdslimietMs) : null;
    try {
      const headers = { Authorization: `Bearer ${token}` };
      if (body !== undefined) headers["Content-Type"] = "application/json";
      const res = await fetch(url, { method, headers, body: body === undefined ? undefined : JSON.stringify(body), signal: ctrl ? ctrl.signal : undefined });
      let json = null;
      if (res.status !== 204) { try { json = await res.json(); } catch { json = null; } }
      return { status: res.status, json };
    } catch {
      return { status: 0, json: null }; // geen netwerk, time-out
    } finally {
      if (timer) clearTimeout(timer);
    }
  }

  // Eén verzoek met opnieuw proberen. opts.bijHerhaling(status, poging) mag een antwoord omzetten
  // (bijvoorbeeld 410 na een herhaalde delete telt als gelukt).
  async function verzoek(method, pad, { query, body, bijHerhaling } = {}) {
    const qs = query ? "?" + new URLSearchParams(Object.entries(query).filter(([, v]) => v !== undefined && v !== null && v !== "").map(([k, v]) => [k, String(v)])).toString() : "";
    const url = API + pad + (qs === "?" ? "" : qs);
    if (!token) {
      try { token = await haalToken({ stil: true }); } catch (e) { throw new GoogleFout("inloggen", 0, e && e.message ? String(e.message) : null); }
      if (!token) throw new GoogleFout("inloggen", 0, "geen_token");
    }
    let nieuwToken = false;
    let poging = 0;
    let herhaald = false; // is er al een poging geweest die misschien aankwam?
    for (;;) {
      const r = await eenKeer(method, url, body);
      if (r.status >= 200 && r.status < 300) return r.json;
      // Een DELETE die 410 "deleted" geeft: de afspraak is al weg, dat was het doel (Google: "no further action is necessary").
      if (method === "DELETE" && r.status === 410) return null;
      if (herhaald && bijHerhaling) {
        const om = await bijHerhaling(r.status);
        if (om !== undefined) return om;
      }
      const reden = redenUit(r.json);
      if (r.status === 401) {
        if (nieuwToken) throw new GoogleFout("inloggen", 401, reden);
        nieuwToken = true;
        try { token = await haalToken({ stil: true }); } catch { throw new GoogleFout("inloggen", 401, reden); }
        continue; // 401 kwam niet aan: geen herhaling
      }
      const tijdelijk = r.status === 0 || r.status === 429 || r.status >= 500 || (r.status === 403 && OPNIEUW_403.has(reden));
      if (tijdelijk && poging < WACHTTIJDEN_MS.length) {
        await slaap(WACHTTIJDEN_MS[poging]);
        poging++;
        // Bij een time-out of 5xx kan de wijziging toch zijn uitgevoerd; bij 429/403 niet.
        if (r.status === 0 || r.status >= 500) herhaald = true;
        continue;
      }
      const lezen = method === "GET";
      if (r.status === 403 && (reden === "quotaExceeded" || reden === "dailyLimitExceeded")) throw new GoogleFout(lezen ? "quota_lezen" : "quota", 403, reden);
      // Een wijziging die misschien aankwam (time-out of 5xx eerder): niet zeggen dat er niets veranderde.
      if (herhaald && !lezen) throw new GoogleFout("onzeker", r.status, reden);
      if (tijdelijk) throw new GoogleFout(r.status === 403 || r.status === 429 ? (lezen ? "quota_lezen" : "quota") : "netwerk", r.status, reden);
      if (r.status === 403) throw new GoogleFout("geen_toegang", 403, reden);
      if (r.status === 404 || r.status === 410) throw new GoogleFout("niet_gevonden", r.status, reden);
      throw new GoogleFout("onbekend", r.status, reden);
    }
  }

  async function allePaginas(pad, query, veld = "items") {
    const uit = [];
    let pageToken;
    let extra = null;
    for (let i = 0; i < MAX_PAGINAS; i++) {
      const json = await verzoek("GET", pad, { query: { ...query, pageToken } });
      if (json && Array.isArray(json[veld])) uit.push(...json[veld]);
      if (json && !extra) extra = { timeZone: json.timeZone, accessRole: json.accessRole };
      pageToken = json && json.nextPageToken; // ook een lege pagina kan een nextPageToken hebben
      if (!pageToken) return { items: uit, ...extra };
    }
    throw new GoogleFout("onbekend", 0, "te_veel_paginas");
  }

  const cal = (id) => `/calendars/${encodeURIComponent(id)}`;
  const ev = (calId, evId) => `${cal(calId)}/events/${encodeURIComponent(evId)}`;

  return {
    verzoek,
    // Alle agenda's in de lijst van de gebruiker, met accessRole.
    async agendas() {
      const { items } = await allePaginas("/users/me/calendarList", { maxResults: 250, minAccessRole: "freeBusyReader" });
      return items;
    },
    // Losse keren (singleEvents) in een periode. Afgezegde afspraken laat Google zelf weg (showDeleted=false).
    async afspraken(calId, { timeMin, timeMax, q } = {}) {
      return allePaginas(`${cal(calId)}/events`, { singleEvents: "true", maxResults: 2500, timeMin, timeMax, q, showDeleted: "false" });
    },
    async haal(calId, evId) {
      return verzoek("GET", ev(calId, evId));
    },
    // Een herhaalde delete die 410 geeft, kwam de eerste keer aan: telt als gelukt.
    async verwijder(calId, evId, { mailGasten = false } = {}) {
      await verzoek("DELETE", ev(calId, evId), { query: { sendUpdates: mailGasten ? "all" : "none" } });
      return true;
    },
    async wijzig(calId, evId, velden, { mailGasten = false } = {}) {
      return verzoek("PATCH", ev(calId, evId), { query: { sendUpdates: mailGasten ? "all" : "none" }, body: velden });
    },
    // Terugzetten van een verwijderde afspraak: Google bewaart hem als cancelled met dezelfde id.
    async zetTerug(calId, evId) {
      return verzoek("PATCH", ev(calId, evId), { query: { sendUpdates: "none" }, body: { status: "confirmed" } });
    },
    // Naar een andere agenda. Een herhaalde move die 404 geeft: kijk of hij al in de doelagenda staat.
    async verplaats(calId, evId, doelId, { mailGasten = false } = {}) {
      return verzoek("POST", `${ev(calId, evId)}/move`, {
        query: { destination: doelId, sendUpdates: mailGasten ? "all" : "none" },
        bijHerhaling: async (status) => {
          if (status < 400 || status >= 500 || status === 401) return undefined; // echte Google: welke 4xx is onbekend (GOK), dus kijk bij elke 4xx
          try {
            const al = await verzoek("GET", ev(doelId, evId));
            return al && al.status !== "cancelled" ? al : undefined;
          } catch { return undefined; }
        },
      });
    },
  };
}
