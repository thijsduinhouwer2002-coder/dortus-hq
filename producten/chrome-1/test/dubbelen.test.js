import { test } from "node:test";
import assert from "node:assert/strict";
import { vindDubbelen, teVerwijderen, normaliseerTitel, tijdSleutel, REDENEN } from "../ext/lib/dubbelen.js";

const eigen = { id: "ik@voorbeeld.nl", accessRole: "owner", primary: true, summary: "Ik" };
const werk = { id: "werk123@group.calendar.google.com", accessRole: "owner", summary: "Werk (Outlook)" };
const team = { id: "team@group.calendar.google.com", accessRole: "writer", summary: "Team" };
const feest = { id: "nl.dutch#holiday@group.v.calendar.google.com", accessRole: "reader", summary: "Feestdagen" };

let n = 0;
function ev(titel, begin, eind, extra = {}) {
  n++;
  const heleDag = /^\d{4}-\d{2}-\d{2}$/.test(begin);
  return {
    id: "ev" + n,
    iCalUID: "uid" + n + "@google.com",
    status: "confirmed",
    summary: titel,
    created: "2026-01-01T00:00:00.000Z",
    start: heleDag ? { date: begin } : { dateTime: begin },
    end: heleDag ? { date: eind } : { dateTime: eind },
    ...extra,
  };
}

test("titel: hoofdletters, spaties, leestekens en accenten tellen niet", () => {
  assert.equal(normaliseerTitel("  Overleg: Café-team!  "), normaliseerTitel("overleg cafe team"));
  assert.equal(normaliseerTitel(undefined), "");
  assert.notEqual(normaliseerTitel("Overleg 1"), normaliseerTitel("Overleg 2"));
});

test("dubbel over twee agenda's heen, verschil in hoofdletters en offset, de eigen hoofdagenda blijft", () => {
  const a = ev("Tandarts", "2026-11-20T10:00:00+01:00", "2026-11-20T10:30:00+01:00");
  const b = ev("TANDARTS", "2026-11-20T09:00:00Z", "2026-11-20T09:30:00Z");
  const { groepen } = vindDubbelen([{ agenda: werk, events: [b] }, { agenda: eigen, events: [a] }]);
  assert.equal(groepen.length, 1);
  const g = groepen[0];
  assert.equal(g.aantal, 2);
  const blijft = g.items.find((i) => i.blijft);
  assert.equal(blijft.agendaId, eigen.id);
  assert.deepEqual(teVerwijderen(groepen), [{ agendaId: werk.id, eventId: b.id }]);
});

test("zelfde iCalUID in twee agenda's is dezelfde vergadering, geen dubbel", () => {
  const a = ev("Weekstart", "2026-11-23T09:00:00+01:00", "2026-11-23T10:00:00+01:00", { iCalUID: "zelfde@x" });
  const b = { ...ev("Weekstart", "2026-11-23T09:00:00+01:00", "2026-11-23T10:00:00+01:00"), iCalUID: "zelfde@x" };
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [a] }, { agenda: team, events: [b] }]);
  assert.equal(groepen.length, 0);
});

test("losse keren van één reeks (zelfde iCalUID, ander begin) zijn geen dubbelen; twee keer geïmporteerde reeks wel", () => {
  const reeksA = [1, 2, 3].map((d) => ev("Yoga", `2026-12-0${d}T19:00:00+01:00`, `2026-12-0${d}T20:00:00+01:00`, { iCalUID: "yoga@a", recurringEventId: "rA" }));
  const reeksB = [1, 2, 3].map((d) => ev("Yoga", `2026-12-0${d}T19:00:00+01:00`, `2026-12-0${d}T20:00:00+01:00`, { iCalUID: "yoga@b", recurringEventId: "rB" }));
  const alleenA = vindDubbelen([{ agenda: eigen, events: reeksA }]);
  assert.equal(alleenA.groepen.length, 0);
  const beide = vindDubbelen([{ agenda: eigen, events: [...reeksA, ...reeksB] }]);
  assert.equal(beide.groepen.length, 3);
  // groepen staan op volgorde van tijd
  assert.deepEqual(beide.groepen.map((g) => g.start.dateTime.slice(0, 10)), ["2026-12-01", "2026-12-02", "2026-12-03"]);
});

test("hele dag en afspraak met tijd zijn nooit dubbel; hele dagen op datum wel", () => {
  const dag = ev("Koningsdag", "2027-04-27", "2027-04-28");
  const tijd = ev("Koningsdag", "2027-04-27T00:00:00Z", "2027-04-28T00:00:00Z");
  assert.equal(vindDubbelen([{ agenda: eigen, events: [dag, tijd] }]).groepen.length, 0);
  const dag2 = ev("koningsdag", "2027-04-27", "2027-04-28");
  const r = vindDubbelen([{ agenda: eigen, events: [dag] }, { agenda: werk, events: [dag2] }]);
  assert.equal(r.groepen.length, 1);
  assert.equal(r.groepen[0].heleDag, true);
});

test("ander eind is geen dubbel", () => {
  const a = ev("Lunch", "2026-11-20T12:00:00Z", "2026-11-20T13:00:00Z");
  const b = ev("Lunch", "2026-11-20T12:00:00Z", "2026-11-20T12:30:00Z");
  assert.equal(vindDubbelen([{ agenda: eigen, events: [a, b] }]).groepen.length, 0);
});

test("alleen-lezen agenda: zichtbaar, niet aan te vinken, met uitleg; de schrijfbare kopie blijft niet per se", () => {
  const a = ev("Kerst", "2026-12-25", "2026-12-26");
  const b = ev("Kerst", "2026-12-25", "2026-12-26");
  const { groepen } = vindDubbelen([{ agenda: feest, events: [a] }, { agenda: eigen, events: [b] }]);
  assert.equal(groepen.length, 1);
  // eigen agenda (owner) blijft, feestdagen is alleen-lezen en kan dus niet weg
  const fe = groepen[0].items.find((i) => i.agendaId === feest.id);
  assert.equal(fe.blijft, false);
  assert.equal(fe.kan, false);
  assert.equal(fe.aangevinkt, false);
  assert.equal(fe.reden, REDENEN.alleenLezen);
  assert.deepEqual(teVerwijderen(groepen), []);
});

test("organisator met gasten: niet aangevinkt, wel aan te vinken", () => {
  const a = ev("Klantgesprek", "2026-11-24T14:00:00Z", "2026-11-24T15:00:00Z", { created: "2026-01-01T00:00:00Z" });
  const b = ev("Klantgesprek", "2026-11-24T14:00:00Z", "2026-11-24T15:00:00Z", {
    created: "2026-02-01T00:00:00Z",
    organizer: { email: eigen.id, self: true },
    attendees: [{ email: eigen.id, self: true }, { email: "klant@voorbeeld.com" }, { email: "zaal@resource.calendar.google.com", resource: true }],
  });
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [a, b] }]);
  const it = groepen[0].items.find((i) => i.eventId === b.id);
  assert.equal(it.blijft, false);
  assert.equal(it.kan, true);
  assert.equal(it.aangevinkt, false);
  assert.equal(it.reden, REDENEN.gasten);
});

test("alleen een zaal als gast telt niet als gasten", () => {
  const a = ev("Focus", "2026-11-24T08:00:00Z", "2026-11-24T09:00:00Z", { created: "2026-01-01T00:00:00Z" });
  const b = ev("Focus", "2026-11-24T08:00:00Z", "2026-11-24T09:00:00Z", {
    created: "2026-03-01T00:00:00Z",
    organizer: { self: true },
    attendees: [{ self: true }, { email: "zaal@resource.calendar.google.com", resource: true }],
  });
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [a, b] }]);
  assert.equal(groepen[0].items.find((i) => i.eventId === b.id).aangevinkt, true);
});

test("bij gelijkspel blijft de oudste", () => {
  const nieuw = ev("Sport", "2026-11-25T18:00:00Z", "2026-11-25T19:00:00Z", { created: "2026-06-01T00:00:00Z" });
  const oud = ev("Sport", "2026-11-25T18:00:00Z", "2026-11-25T19:00:00Z", { created: "2025-06-01T00:00:00Z" });
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [nieuw, oud] }]);
  assert.equal(groepen[0].items.find((i) => i.blijft).eventId, oud.id);
});

test("eigen agenda gaat voor writer-agenda, ook als die ouder is", () => {
  const inTeam = ev("Demo", "2026-11-26T10:00:00Z", "2026-11-26T11:00:00Z", { created: "2020-01-01T00:00:00Z" });
  const inWerk = ev("Demo", "2026-11-26T10:00:00Z", "2026-11-26T11:00:00Z", { created: "2026-01-01T00:00:00Z" });
  const { groepen } = vindDubbelen([{ agenda: team, events: [inTeam] }, { agenda: werk, events: [inWerk] }]);
  assert.equal(groepen[0].items.find((i) => i.blijft).agendaId, werk.id);
});

test("drie kopieën: één blijft, twee aangevinkt", () => {
  const evs = [1, 2, 3].map((i) => ev("Import", "2026-11-27T10:00:00Z", "2026-11-27T11:00:00Z", { created: `2026-0${i}-01T00:00:00Z` }));
  const { groepen } = vindDubbelen([{ agenda: eigen, events: evs }]);
  assert.equal(groepen[0].aantal, 3);
  assert.equal(teVerwijderen(groepen).length, 2);
  assert.equal(groepen[0].items.filter((i) => i.blijft).length, 1);
});

test("overslaan: geannuleerd, verjaardag, geen titel, kapotte tijd, twee keer ingelezen", () => {
  const goed1 = ev("X", "2026-11-28T10:00:00Z", "2026-11-28T11:00:00Z");
  const evs = [
    goed1,
    goed1, // zelfde id in zelfde agenda (overlappende pagina's)
    ev("X", "2026-11-28T10:00:00Z", "2026-11-28T11:00:00Z", { status: "cancelled" }),
    ev("X", "2026-11-28T10:00:00Z", "2026-11-28T11:00:00Z", { eventType: "birthday" }),
    ev("", "2026-11-28T10:00:00Z", "2026-11-28T11:00:00Z"),
    ev("   ", "2026-11-28T10:00:00Z", "2026-11-28T11:00:00Z"),
    { ...ev("X", "2026-11-28T10:00:00Z", "2026-11-28T11:00:00Z"), start: { dateTime: "kapot" } },
    { ...ev("X", "2026-11-28T10:00:00Z", "2026-11-28T11:00:00Z"), start: undefined },
    { ...ev("X", "2026-11-28", "2026-11-29"), end: { dateTime: "2026-11-29T00:00:00Z" } },
  ];
  const r = vindDubbelen([{ agenda: eigen, events: evs }]);
  assert.equal(r.groepen.length, 0);
  assert.deepEqual(r.overgeslagen, { geannuleerd: 1, soort: 1, geenTijd: 3, geenTitel: 2, dubbelIngelezen: 1 });
});

test("rare invoer breekt niets", () => {
  assert.deepEqual(vindDubbelen(undefined).groepen, []);
  assert.deepEqual(vindDubbelen([null, {}, { agenda: {} }, { agenda: eigen, events: [null, {}, { id: "x" }] }]).groepen, []);
  assert.deepEqual(teVerwijderen(undefined), []);
  assert.equal(tijdSleutel({}), null);
});

test("afspraak zonder iCalUID telt als zichzelf", () => {
  const a = { ...ev("Los", "2026-11-29T10:00:00Z", "2026-11-29T11:00:00Z"), iCalUID: undefined };
  const b = { ...ev("Los", "2026-11-29T10:00:00Z", "2026-11-29T11:00:00Z"), iCalUID: undefined };
  assert.equal(vindDubbelen([{ agenda: eigen, events: [a, b] }]).groepen.length, 1);
});

test("snel genoeg: 20.000 afspraken in minder dan 2 seconden", () => {
  const evs = [];
  for (let i = 0; i < 10000; i++) {
    const d = new Date(Date.UTC(2026, 0, 1) + i * 3600000).toISOString();
    const e = new Date(Date.UTC(2026, 0, 1) + i * 3600000 + 1800000).toISOString();
    evs.push(ev("Blok " + (i % 50), d, e));
  }
  const kopie = evs.map((e) => ({ ...e, id: e.id + "k", iCalUID: e.iCalUID + "k" }));
  const t = Date.now();
  const r = vindDubbelen([{ agenda: eigen, events: evs }, { agenda: werk, events: kopie }]);
  assert.ok(Date.now() - t < 2000);
  assert.equal(r.groepen.length, 10000);
});
