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

test("alleen-lezen agenda: zichtbaar, niet aan te vinken, met uitleg; de eigen kopie blijft", () => {
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

test("organisator met gasten: de vergadering blijft; een tweede vergadering-kopie staat niet aangevinkt maar kan wel", () => {
  const los = ev("Klantgesprek", "2026-11-24T14:00:00Z", "2026-11-24T15:00:00Z", { created: "2020-01-01T00:00:00Z" });
  const met = (created) => ev("Klantgesprek", "2026-11-24T14:00:00Z", "2026-11-24T15:00:00Z", {
    created,
    organizer: { email: eigen.id, self: true },
    attendees: [{ email: eigen.id, self: true }, { email: "klant@voorbeeld.com" }, { email: "zaal@resource.calendar.google.com", resource: true }],
  });
  const b = met("2026-02-01T00:00:00Z"), c = met("2026-03-01T00:00:00Z");
  const r1 = vindDubbelen([{ agenda: eigen, events: [los, b] }]);
  assert.equal(r1.groepen[0].items.find((i) => i.blijft).eventId, b.id, "de echte vergadering blijft, ook al is de losse kopie ouder");
  assert.deepEqual(teVerwijderen(r1.groepen), [{ agendaId: eigen.id, eventId: los.id }]);
  const r2 = vindDubbelen([{ agenda: eigen, events: [b, c] }]);
  const it = r2.groepen[0].items.find((i) => i.eventId === c.id);
  assert.equal(it.blijft, false);
  assert.equal(it.kan, true);
  assert.equal(it.aangevinkt, false);
  assert.equal(it.reden, REDENEN.gasten);
});

test("uitnodiging waar je gast bent blijft, ook als een losse Outlook-kopie ouder is", () => {
  const outlook = ev("Overleg baas", "2026-11-24T10:00:00Z", "2026-11-24T11:00:00Z", { created: "2020-01-01T00:00:00Z" });
  const uitnodiging = ev("Overleg baas", "2026-11-24T10:00:00Z", "2026-11-24T11:00:00Z", {
    created: "2026-05-01T00:00:00Z",
    organizer: { email: "baas@voorbeeld.com" },
    attendees: [{ email: "baas@voorbeeld.com", organizer: true }, { email: eigen.id, self: true }],
  });
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [outlook, uitnodiging] }]);
  assert.equal(groepen[0].items.find((i) => i.blijft).eventId, uitnodiging.id);
  assert.deepEqual(teVerwijderen(groepen), [{ agendaId: eigen.id, eventId: outlook.id }]);
});

test("twee uitnodigingen als gast: de verliezer staat niet aangevinkt, met reden", () => {
  const u = (created) => ev("Teamdag", "2026-11-30", "2026-12-01", {
    created, organizer: { email: "hr@voorbeeld.com" }, attendees: [{ email: "hr@voorbeeld.com" }, { self: true }],
  });
  const a = u("2026-01-01T00:00:00Z"), b = u("2026-02-01T00:00:00Z");
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [a, b] }]);
  const it = groepen[0].items.find((i) => i.eventId === b.id);
  assert.equal(it.aangevinkt, false);
  assert.equal(it.kan, true);
  assert.equal(it.reden, REDENEN.gast);
});

test("attendeesOmitted telt als gasten", () => {
  const a = ev("Groot overleg", "2026-11-24T12:00:00Z", "2026-11-24T13:00:00Z", { created: "2026-01-01T00:00:00Z", organizer: { self: true }, attendeesOmitted: true, attendees: [{ self: true }] });
  const b = ev("Groot overleg", "2026-11-24T12:00:00Z", "2026-11-24T13:00:00Z", { created: "2026-02-01T00:00:00Z", organizer: { self: true }, attendeesOmitted: true, attendees: [{ self: true }] });
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [a, b] }]);
  assert.deepEqual(teVerwijderen(groepen), []);
  assert.equal(groepen[0].items.find((i) => i.eventId === b.id).reden, REDENEN.gasten);
});

test("gedeelde agenda van een ander (writer): niet aangevinkt met waarschuwing; writer gaat voor reader", () => {
  const inTeam = ev("Retro", "2026-11-26T15:00:00Z", "2026-11-26T16:00:00Z", { created: "2026-01-01T00:00:00Z" });
  const inTeam2 = ev("Retro", "2026-11-26T15:00:00Z", "2026-11-26T16:00:00Z", { created: "2026-02-01T00:00:00Z" });
  const r = vindDubbelen([{ agenda: team, events: [inTeam, inTeam2] }]);
  const it = r.groepen[0].items.find((i) => i.eventId === inTeam2.id);
  assert.equal(it.kan, true);
  assert.equal(it.aangevinkt, false);
  assert.equal(it.reden, REDENEN.gedeeld);
  const inFeest = ev("Retro", "2026-11-26T15:00:00Z", "2026-11-26T16:00:00Z", { created: "2019-01-01T00:00:00Z" });
  const r2 = vindDubbelen([{ agenda: feest, events: [inFeest] }, { agenda: team, events: [inTeam] }]);
  assert.equal(r2.groepen[0].items.find((i) => i.blijft).agendaId, team.id);
});

test("verliezende vergadering met kopieën in twee agenda's: beide kopieën gaan mee, de winnaar met al zijn kopieën blijft", () => {
  const w = ev("Planning", "2026-11-27T09:00:00Z", "2026-11-27T10:00:00Z", { created: "2025-01-01T00:00:00Z", iCalUID: "win@x" });
  const wKopie = { ...ev("Planning", "2026-11-27T09:00:00Z", "2026-11-27T10:00:00Z"), iCalUID: "win@x" };
  const v = ev("Planning", "2026-11-27T09:00:00Z", "2026-11-27T10:00:00Z", { created: "2026-01-01T00:00:00Z", iCalUID: "verlies@x" });
  const vKopie = { ...ev("Planning", "2026-11-27T09:00:00Z", "2026-11-27T10:00:00Z"), iCalUID: "verlies@x" };
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [w, v] }, { agenda: werk, events: [wKopie, vKopie] }]);
  assert.equal(groepen[0].aantal, 2);
  assert.equal(groepen[0].items.filter((i) => i.blijft).length, 2);
  assert.deepEqual(teVerwijderen(groepen).map((x) => x.eventId).sort(), [v.id, vKopie.id].sort());
});

test("creator.self zonder organizer telt als eigen afspraak", () => {
  const a = ev("Eigen", "2026-11-28T09:00:00Z", "2026-11-28T10:00:00Z", { created: "2026-01-01T00:00:00Z", creator: { self: true }, attendees: [{ self: true }, { email: "x@y.z" }] });
  const b = ev("Eigen", "2026-11-28T09:00:00Z", "2026-11-28T10:00:00Z", { created: "2026-02-01T00:00:00Z", creator: { self: true }, attendees: [{ self: true }, { email: "x@y.z" }] });
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [a, b] }]);
  assert.equal(groepen[0].items.find((i) => i.eventId === b.id).reden, REDENEN.gasten);
});

test("verschoven keer van een reeks op hetzelfde moment als een andere keer: aparte identiteit", () => {
  const gewoon = ev("Les", "2026-12-08T19:00:00Z", "2026-12-08T20:00:00Z", { iCalUID: "les@x", recurringEventId: "r", originalStartTime: { dateTime: "2026-12-08T19:00:00Z" }, created: "2026-01-01T00:00:00Z" });
  const verschoven = ev("Les", "2026-12-08T19:00:00Z", "2026-12-08T20:00:00Z", { iCalUID: "les@x", recurringEventId: "r", originalStartTime: { dateTime: "2026-12-01T19:00:00Z" }, created: "2026-01-01T00:00:00Z" });
  const { groepen } = vindDubbelen([{ agenda: eigen, events: [gewoon, verschoven] }]);
  assert.equal(groepen.length, 1);
  assert.equal(groepen[0].aantal, 2);
  assert.equal(teVerwijderen(groepen).length, 1, "nooit allebei weg");
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
  assert.deepEqual(vindDubbelen({}).groepen, []);
  assert.deepEqual(vindDubbelen([{ agenda: eigen, events: {} }]).groepen, []);
  const a = ev("Z", "2026-11-29T08:00:00Z", "2026-11-29T09:00:00Z", { attendees: "x", organizer: "raar" });
  const b = ev("Z", "2026-11-29T08:00:00Z", "2026-11-29T09:00:00Z", { attendees: [null, 5] });
  assert.equal(vindDubbelen([{ agenda: eigen, events: [a, b] }]).groepen.length, 1);
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
