// Dubbele afspraken vinden over meerdere agenda's heen. Zuivere functie, geen netwerk.
// Ontwerp: producten/chrome-1/ontwerp.md, punt 3 "Dubbelen".
//
// Invoer: [{ agenda: { id, accessRole, primary?, summary? }, events: [Google Calendar event, ...] }]
//   events komen uit events.list met singleEvents=true (dus losse keren, geen hoofdafspraak).
// Uitvoer: { groepen: [...], overgeslagen: { geannuleerd, soort, geenTijd, geenTitel, dubbelIngelezen } }
//
// Regels:
// 1. Kopieën van dezelfde vergadering (zelfde iCalUID en zelfde begin) in verschillende agenda's
//    zijn één afspraak, geen dubbel: weghalen bij de organisator zegt hem af voor alle gasten.
// 2. Dubbel = verschillende iCalUID, zelfde titel (hoofdletters, spaties, leestekens en accenten
//    tellen niet), zelfde begin en eind. Tijden vergelijken als moment (offset maakt niet uit);
//    hele dagen op datum. Een hele dag en een afspraak met tijd zijn nooit dubbel.
// 3. Per groep blijft er één: in een agenda die de gebruiker bezit (owner), dan de hoofdagenda,
//    dan de oudste (created). De rest staat aangevinkt, behalve wat niet mag of riskant is.

export const SOORTEN_MEE = new Set(["default", "fromGmail"]); // verjaardagen, focustijd e.d. doen niet mee
const SCHRIJVEN = new Set(["owner", "writer"]);

export const REDENEN = {
  alleenLezen: "Deze agenda mag je alleen bekijken, dus hier kun je niets weghalen.",
  gasten: "Jij hebt deze afspraak gemaakt en er zijn gasten. Weghalen zegt hem voor hen af, daarom staat hij niet aangevinkt.",
};

export function normaliseerTitel(titel) {
  if (titel === null || titel === undefined) return "";
  return String(titel)
    .normalize("NFKD")
    .replace(/\p{M}+/gu, "")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, "");
}

// Geeft { heleDag, begin, eind } met vergelijkbare sleutels, of null als de tijd niet te lezen is.
export function tijdSleutel(ev) {
  const s = ev && ev.start, e = ev && ev.end;
  if (!s || !e) return null;
  if (s.date || e.date) {
    if (!s.date || !e.date) return null;
    if (!/^\d{4}-\d{2}-\d{2}$/.test(s.date) || !/^\d{4}-\d{2}-\d{2}$/.test(e.date)) return null;
    return { heleDag: true, begin: s.date, eind: e.date };
  }
  const b = Date.parse(s.dateTime), t = Date.parse(e.dateTime);
  if (!Number.isFinite(b) || !Number.isFinite(t)) return null;
  return { heleDag: false, begin: String(b), eind: String(t) };
}

function rang(item) {
  // lager is beter
  return [
    item.accessRole === "owner" ? 0 : 1,
    item.primary ? 0 : 1,
    Number.isFinite(item.gemaakt) ? item.gemaakt : Number.MAX_SAFE_INTEGER,
    item.agendaId + "\u0000" + item.eventId, // vaste volgorde bij gelijkspel
  ];
}
function vergelijk(a, b) {
  const ra = rang(a), rb = rang(b);
  for (let i = 0; i < ra.length; i++) {
    if (ra[i] < rb[i]) return -1;
    if (ra[i] > rb[i]) return 1;
  }
  return 0;
}

function ikBenOrganisatorMetGasten(ev) {
  const org = ev.organizer;
  const ik = !!(org && org.self) || ev.creator?.self === true && !org;
  if (!ik) return false;
  const anderen = (ev.attendees || []).filter((a) => !a.self && !a.resource);
  return anderen.length > 0;
}

export function vindDubbelen(agendas) {
  const overgeslagen = { geannuleerd: 0, soort: 0, geenTijd: 0, geenTitel: 0, dubbelIngelezen: 0 };
  const gezien = new Set();
  // tijd+titel -> Map(identiteit -> [items])
  const kandidaten = new Map();

  for (const blok of agendas || []) {
    const agenda = blok && blok.agenda;
    if (!agenda || !agenda.id) continue;
    for (const ev of blok.events || []) {
      if (!ev || !ev.id) continue;
      const uniek = agenda.id + "\u0000" + ev.id;
      if (gezien.has(uniek)) { overgeslagen.dubbelIngelezen++; continue; }
      gezien.add(uniek);
      if (ev.status === "cancelled") { overgeslagen.geannuleerd++; continue; }
      if (!SOORTEN_MEE.has(ev.eventType || "default")) { overgeslagen.soort++; continue; }
      const tijd = tijdSleutel(ev);
      if (!tijd) { overgeslagen.geenTijd++; continue; }
      const titel = normaliseerTitel(ev.summary);
      // Zonder titel niet groeperen: twee lege blokken op hetzelfde moment zijn vaak bewust (bezet).
      if (!titel) { overgeslagen.geenTitel++; continue; }

      const sleutel = [tijd.heleDag ? "d" : "t", tijd.begin, tijd.eind, titel].join("|");
      // Identiteit: zelfde vergadering = zelfde iCalUID op hetzelfde moment (losse keren van een reeks
      // delen de iCalUID, daarom telt het begin mee). Zonder iCalUID is elke afspraak zichzelf.
      const identiteit = ev.iCalUID ? "u:" + ev.iCalUID : "e:" + uniek;
      const item = {
        agendaId: agenda.id,
        agendaNaam: agenda.summaryOverride || agenda.summary || agenda.id,
        accessRole: agenda.accessRole || "reader",
        primary: !!agenda.primary,
        eventId: ev.id,
        iCalUID: ev.iCalUID || null,
        titel: ev.summary,
        gemaakt: Date.parse(ev.created),
        recurringEventId: ev.recurringEventId || null,
        gastenRisico: ikBenOrganisatorMetGasten(ev),
        heleDag: tijd.heleDag,
        start: ev.start,
        end: ev.end,
      };
      if (!kandidaten.has(sleutel)) kandidaten.set(sleutel, new Map());
      const perId = kandidaten.get(sleutel);
      if (!perId.has(identiteit)) perId.set(identiteit, []);
      perId.get(identiteit).push(item);
    }
  }

  const groepen = [];
  for (const [sleutel, perId] of kandidaten) {
    if (perId.size < 2) continue; // alleen kopieën van één vergadering: geen dubbel
    // Elke identiteit is één "afspraak"; kies welke blijft.
    const afspraken = [...perId.values()].map((items) => {
      const gesorteerd = [...items].sort(vergelijk);
      return { items: gesorteerd, beste: gesorteerd[0] };
    });
    afspraken.sort((a, b) => vergelijk(a.beste, b.beste));
    const items = [];
    afspraken.forEach((afspraak, i) => {
      const blijft = i === 0;
      for (const it of afspraak.items) {
        const kan = SCHRIJVEN.has(it.accessRole);
        let reden = null;
        if (!blijft && !kan) reden = REDENEN.alleenLezen;
        else if (!blijft && it.gastenRisico) reden = REDENEN.gasten;
        items.push({
          ...it,
          blijft,
          kan: !blijft && kan,
          aangevinkt: !blijft && kan && !it.gastenRisico,
          reden,
        });
      }
    });
    const eerste = afspraken[0].beste;
    groepen.push({
      sleutel,
      titel: eerste.titel,
      heleDag: eerste.heleDag,
      start: eerste.start,
      end: eerste.end,
      aantal: afspraken.length,
      moment: eerste.heleDag ? Date.parse(eerste.start.date + "T00:00:00Z") : Date.parse(eerste.start.dateTime),
      items,
    });
  }
  groepen.sort((a, b) => a.moment - b.moment || (a.sleutel < b.sleutel ? -1 : a.sleutel > b.sleutel ? 1 : 0));
  return { groepen, overgeslagen };
}

// Wat er weg gaat als de gebruiker op "Opruimen" klikt: alleen aangevinkte items die mogen.
export function teVerwijderen(groepen) {
  const uit = [];
  for (const g of groepen || []) for (const it of g.items) if (it.aangevinkt && it.kan && !it.blijft) uit.push({ agendaId: it.agendaId, eventId: it.eventId });
  return uit;
}
