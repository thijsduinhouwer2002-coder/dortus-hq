// Nagebootste Google Calendar-API in het geheugen, in de vorm van de documentatie.
// Voor unit-tests (als fetch) en later voor de e2e in Playwright (via page.route).
// Storingen: nep.storingen.push({ methode, pad (regex), status, reden, toch }) — "toch" voert het verzoek
// eerst uit en geeft dan de storing (de wijziging kwam aan, het antwoord niet). status 0 = geen netwerk.

export function maakNepGoogle({ paginaGrootte = 2500, legePagina = false } = {}) {
  const nep = {
    agendas: [], // { id, summary, accessRole, primary, timeZone }
    afspraken: {}, // calId -> Map(evId -> event)
    storingen: [],
    log: [], // { methode, pad, query }
    geldigeTokens: new Set(["tok1"]),
  };

  nep.agenda = (id, accessRole = "owner", extra = {}) => {
    nep.agendas.push({ id, summary: id, accessRole, timeZone: "Europe/Amsterdam", ...extra });
    nep.afspraken[id] = new Map();
  };
  nep.afspraak = (calId, ev) => {
    const e = { status: "confirmed", iCalUID: `${ev.id}@google.com`, ...ev };
    nep.afspraken[calId].set(e.id, e);
    return e;
  };

  function antwoord(status, json) {
    return { status, ok: status >= 200 && status < 300, json: async () => { if (json === undefined) throw new Error("geen json"); return json; } };
  }
  const fout = (status, reden, msg = "fout") => antwoord(status, { error: { code: status, message: msg, errors: [{ reason: reden, message: msg }] } });

  function pagina(items, pageToken, grootte) {
    let start = Number(pageToken || 0);
    // Eén lege pagina met nextPageToken ertussen, zoals Google soms doet.
    if (legePagina && pageToken === undefined && items.length > 0) return { items: [], nextPageToken: "0" };
    const stuk = items.slice(start, start + grootte);
    const verder = start + grootte < items.length ? String(start + grootte) : undefined;
    return { items: stuk, ...(verder ? { nextPageToken: verder } : {}) };
  }

  function voerUit(methode, pad, q, body) {
    let m;
    if (methode === "GET" && pad === "/users/me/calendarList") {
      return antwoord(200, { kind: "calendar#calendarList", ...pagina(nep.agendas, q.get("pageToken") ?? undefined, Math.min(paginaGrootte, Number(q.get("maxResults") || 100))) });
    }
    if ((m = pad.match(/^\/calendars\/([^/]+)\/events$/)) && methode === "GET") {
      const calId = decodeURIComponent(m[1]);
      const map = nep.afspraken[calId];
      if (!map) return fout(404, "notFound");
      let items = [...map.values()].filter((e) => e.status !== "cancelled");
      const tmin = q.get("timeMin"), tmax = q.get("timeMax");
      const begin = (e) => e.start.dateTime || e.start.date;
      if (tmin) items = items.filter((e) => (e.end.dateTime || e.end.date) > tmin);
      if (tmax) items = items.filter((e) => begin(e) < tmax);
      items.sort((a, b) => begin(a).localeCompare(begin(b)));
      const cal = nep.agendas.find((a) => a.id === calId);
      return antwoord(200, { kind: "calendar#events", timeZone: cal.timeZone, accessRole: cal.accessRole, ...pagina(items, q.get("pageToken") ?? undefined, Math.min(paginaGrootte, Number(q.get("maxResults") || 250))) });
    }
    if ((m = pad.match(/^\/calendars\/([^/]+)\/events\/([^/]+)(\/move)?$/))) {
      const calId = decodeURIComponent(m[1]);
      const evId = decodeURIComponent(m[2]);
      const map = nep.afspraken[calId];
      if (!map) return fout(404, "notFound");
      const cal = nep.agendas.find((a) => a.id === calId);
      const schrijf = cal.accessRole === "owner" || cal.accessRole === "writer";
      const e = map.get(evId);
      if (!e) return fout(404, "notFound");
      if (methode === "GET") return antwoord(200, e);
      if (!schrijf) return fout(403, "forbidden");
      if (methode === "DELETE") {
        if (e.status === "cancelled") return fout(410, "deleted", "Resource has been deleted");
        e.status = "cancelled";
        return antwoord(204);
      }
      if (methode === "PATCH") {
        if (e.status === "cancelled" && body.status !== "confirmed") return fout(404, "notFound");
        Object.assign(e, body);
        return antwoord(200, e);
      }
      if (methode === "POST" && m[3]) {
        if (e.status === "cancelled") return fout(404, "notFound");
        const doel = q.get("destination");
        if (!nep.afspraken[doel]) return fout(404, "notFound");
        const dcal = nep.agendas.find((a) => a.id === doel);
        if (dcal.accessRole !== "owner" && dcal.accessRole !== "writer") return fout(403, "forbidden");
        if (e.eventType && e.eventType !== "default") return fout(400, "invalid", "Event type cannot be moved");
        map.delete(evId);
        nep.afspraken[doel].set(evId, e);
        return antwoord(200, e);
      }
    }
    return fout(400, "badRequest");
  }

  // fetch-vervanger
  nep.fetch = async (url, init = {}) => {
    const u = new URL(url);
    const methode = (init.method || "GET").toUpperCase();
    const pad = u.pathname.replace(/^\/calendar\/v3/, "");
    nep.log.push({ methode, pad, query: Object.fromEntries(u.searchParams) });
    const auth = (init.headers && init.headers.Authorization) || "";
    const i = nep.storingen.findIndex((s) => (!s.methode || s.methode === methode) && (!s.pad || s.pad.test(pad)));
    const storing = i >= 0 ? nep.storingen.splice(i, 1)[0] : null;
    if (storing && !storing.toch) {
      if (storing.status === 0) throw new TypeError("Failed to fetch");
      return fout(storing.status, storing.reden);
    }
    if (!nep.geldigeTokens.has(auth.replace(/^Bearer /, ""))) return fout(401, "authError");
    const body = init.body ? JSON.parse(init.body) : undefined;
    const r = voerUit(methode, pad, u.searchParams, body);
    if (storing) {
      if (storing.status === 0) throw new TypeError("Failed to fetch");
      return fout(storing.status, storing.reden);
    }
    return r;
  };

  return nep;
}
