import { test } from "node:test";
import assert from "node:assert/strict";
import { maakGoogle, maakAuthUrl, leesToken, GoogleFout, WACHTTIJDEN_MS, SCOPES } from "../ext/lib/google.js";
import { maakNepGoogle } from "./nep-google.js";

function opzet(opties) {
  const nep = maakNepGoogle(opties);
  nep.agenda("ik@voorbeeld.nl", "owner", { primary: true });
  nep.agenda("werk#team@group.calendar.google.com", "writer");
  nep.agenda("feestdagen", "reader");
  const geslapen = [];
  let tokens = 0;
  const g = maakGoogle({
    fetch: nep.fetch,
    haalToken: async () => { tokens++; return [...nep.geldigeTokens][0]; },
    slaap: async (ms) => { geslapen.push(ms); },
  });
  return { nep, g, geslapen, tokens: () => tokens };
}
const afspraak = (id, dag = "2026-11-20", titel = id) => ({ id, summary: titel, start: { dateTime: `${dag}T10:00:00+01:00` }, end: { dateTime: `${dag}T11:00:00+01:00` } });

// ---------- inloggen ----------

test("auth-URL: impliciete flow, beide scopes, state, stil met prompt=none", () => {
  const u = new URL(maakAuthUrl({ clientId: "c1", redirectUri: "https://abc.chromiumapp.org/", state: "s1", stil: true }));
  assert.equal(u.searchParams.get("response_type"), "token");
  assert.equal(u.searchParams.get("scope"), SCOPES.join(" "));
  assert.equal(u.searchParams.get("state"), "s1");
  assert.equal(u.searchParams.get("prompt"), "none");
  assert.equal(new URL(maakAuthUrl({ clientId: "c1", redirectUri: "r", state: "s" })).searchParams.get("prompt"), null);
  assert.throws(() => maakAuthUrl({ clientId: "c1", redirectUri: "r" }));
});

test("token lezen: goed, verlooptijd een minuut eerder", () => {
  const r = leesToken(`https://abc.chromiumapp.org/#access_token=T&expires_in=3599&state=s1&scope=${encodeURIComponent(SCOPES.join(" "))}`, "s1", 1000);
  assert.equal(r.token, "T");
  assert.equal(r.verlooptOp, 1000 + 3539 * 1000);
  assert.equal(leesToken("https://a.chromiumapp.org/#access_token=T&expires_in=30&state=s1", "s1", 1000).verlooptOp, 1000);
});

test("token lezen: verkeerde state, fout van Google, geen token, scope niet gegeven, rommel", () => {
  const vang = (url) => { try { leesToken(url, "s1", 0); return null; } catch (e) { assert.ok(e instanceof GoogleFout); assert.equal(e.soort, "inloggen"); return e.reden; } };
  assert.equal(vang("https://a.chromiumapp.org/#access_token=T&state=ANDERS"), "state");
  assert.equal(vang("https://a.chromiumapp.org/#error=access_denied&state=s1"), "access_denied");
  assert.equal(vang("https://a.chromiumapp.org/?error=interaction_required"), "interaction_required");
  assert.equal(vang("https://a.chromiumapp.org/#state=s1"), "geen_token");
  assert.equal(vang(`https://a.chromiumapp.org/#access_token=T&state=s1&scope=${encodeURIComponent(SCOPES[1])}`), "scope");
  assert.equal(vang("geen url"), "geen_url");
});

// ---------- lezen ----------

test("agenda's met accessRole, over meer pagina's", async () => {
  const { g } = opzet({ paginaGrootte: 2 });
  const a = await g.agendas();
  assert.deepEqual(a.map((x) => x.accessRole), ["owner", "writer", "reader"]);
});

test("afspraken over meer pagina's, ook met een lege pagina met nextPageToken", async () => {
  const { nep, g } = opzet({ paginaGrootte: 3, legePagina: true });
  for (let i = 0; i < 8; i++) nep.afspraak("ik@voorbeeld.nl", afspraak(`e${i}`, `2026-11-${10 + i}`));
  const r = await g.afspraken("ik@voorbeeld.nl", { timeMin: "2026-11-01T00:00:00Z" });
  assert.equal(r.items.length, 8);
  assert.equal(r.timeZone, "Europe/Amsterdam");
  const lijst = nep.log.filter((l) => l.pad.endsWith("/events"));
  assert.ok(lijst.length >= 4);
  assert.equal(lijst[0].query.singleEvents, "true");
  assert.equal(lijst[0].query.maxResults, "2500");
});

test("agenda-id met # en @ wordt goed gecodeerd", async () => {
  const { nep, g } = opzet();
  nep.afspraak("werk#team@group.calendar.google.com", afspraak("w1"));
  const r = await g.afspraken("werk#team@group.calendar.google.com");
  assert.equal(r.items.length, 1);
  assert.ok(nep.log.at(-1).pad.includes("werk%23team%40group"));
});

test("API die steeds een nextPageToken geeft loopt niet eindeloos", async () => {
  const g = maakGoogle({ fetch: async () => ({ status: 200, ok: true, json: async () => ({ items: [], nextPageToken: "x" }) }), haalToken: async () => "t", slaap: async () => {} });
  await assert.rejects(g.afspraken("a"), (e) => e.reden === "te_veel_paginas");
});

// ---------- wijzigen ----------

test("verwijderen: sendUpdates=none standaard, terugzetten met status=confirmed", async () => {
  const { nep, g } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  await g.verwijder("ik@voorbeeld.nl", "e1");
  assert.equal(nep.log.at(-1).query.sendUpdates, "none");
  assert.equal((await g.afspraken("ik@voorbeeld.nl")).items.length, 0);
  await g.zetTerug("ik@voorbeeld.nl", "e1");
  assert.equal((await g.afspraken("ik@voorbeeld.nl")).items.length, 1);
  await g.verwijder("ik@voorbeeld.nl", "e1", { mailGasten: true });
  assert.equal(nep.log.at(-1).query.sendUpdates, "all");
});

test("verwijderen: 500 na uitvoeren, herhaling geeft 410: telt als gelukt, niets dubbel", async () => {
  const { nep, g, geslapen } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  nep.storingen.push({ methode: "DELETE", status: 500, reden: "backendError", toch: true });
  assert.equal(await g.verwijder("ik@voorbeeld.nl", "e1"), true);
  assert.deepEqual(geslapen, [1000]);
});

test("verwijderen van een al verwijderde afspraak (410): telt als gelukt; echt onbekende id (404): niet_gevonden", async () => {
  const { nep, g } = opzet();
  nep.afspraak("ik@voorbeeld.nl", { ...afspraak("e1"), status: "cancelled" });
  assert.equal(await g.verwijder("ik@voorbeeld.nl", "e1"), true);
  await assert.rejects(g.verwijder("ik@voorbeeld.nl", "bestaatniet"), (e) => e.soort === "niet_gevonden");
});

test("eerste stille inloggen mislukt: GoogleFout inloggen met melding, geen kale fout", async () => {
  const nep = maakNepGoogle();
  nep.agenda("a");
  const g = maakGoogle({ fetch: nep.fetch, haalToken: async () => { throw new Error("interaction_required"); }, slaap: async () => {} });
  await assert.rejects(g.agendas(), (e) => e instanceof GoogleFout && e.soort === "inloggen" && /Opnieuw verbinden/.test(e.message));
  const g2 = maakGoogle({ fetch: nep.fetch, haalToken: async () => "", slaap: async () => {} });
  await assert.rejects(g2.agendas(), (e) => e.soort === "inloggen");
});

test("wijziging kwam aan maar antwoord bleef uit: melding onzeker, niet 'niet veranderd'", async () => {
  const { nep, g } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  nep.storingen.push({ methode: "PATCH", status: 503, reden: "backendError", toch: true });
  for (let i = 0; i < 4; i++) nep.storingen.push({ methode: "PATCH", status: 503, reden: "backendError" });
  await assert.rejects(g.wijzig("ik@voorbeeld.nl", "e1", { colorId: "5" }), (e) => e.soort === "onzeker" && !/niet veranderd/.test(e.message));
  assert.equal(nep.afspraken["ik@voorbeeld.nl"].get("e1").colorId, "5");
});

test("lezen bij aanhoudende 429: melding over ophalen, niet over wijzigen", async () => {
  const { nep, g } = opzet();
  for (let i = 0; i < 5; i++) nep.storingen.push({ status: 429, reden: "rateLimitExceeded" });
  await assert.rejects(g.agendas(), (e) => e.soort === "quota_lezen" && !/wijzigen/.test(e.message));
});

test("verplaatsen: naar alleen-lezen agenda 403, verjaardag 400", async () => {
  const { nep, g } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  nep.afspraak("ik@voorbeeld.nl", { ...afspraak("b1"), eventType: "birthday" });
  await assert.rejects(g.verplaats("ik@voorbeeld.nl", "e1", "feestdagen"), (e) => e.soort === "geen_toegang");
  await assert.rejects(g.verplaats("ik@voorbeeld.nl", "b1", "werk#team@group.calendar.google.com"), (e) => e.soort === "onbekend" && e.status === 400);
});

test("opnieuw proberen bij 429, 403 rateLimitExceeded, userRateLimitExceeded, 503 en geen netwerk", async () => {
  const { nep, g, geslapen } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  nep.storingen.push({ status: 429, reden: "rateLimitExceeded" }, { status: 403, reden: "rateLimitExceeded" }, { status: 403, reden: "userRateLimitExceeded" }, { status: 0 });
  const r = await g.wijzig("ik@voorbeeld.nl", "e1", { colorId: "5" });
  assert.equal(r.colorId, "5");
  assert.deepEqual(geslapen, WACHTTIJDEN_MS);
});

test("blijvende 503 bij lezen: na 4 keer opnieuw een melding in gewone woorden", async () => {
  const { nep, g } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  for (let i = 0; i < 5; i++) nep.storingen.push({ status: 503, reden: "backendError" });
  await assert.rejects(g.haal("ik@voorbeeld.nl", "e1"), (e) => e.soort === "netwerk" && /niet veranderd/.test(e.message));
  assert.equal(nep.afspraken["ik@voorbeeld.nl"].get("e1").colorId, undefined);
});

test("403 quotaExceeded: meteen stoppen, niet opnieuw proberen", async () => {
  const { nep, g, geslapen } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  nep.storingen.push({ status: 403, reden: "quotaExceeded" });
  await assert.rejects(g.verwijder("ik@voorbeeld.nl", "e1"), (e) => e.soort === "quota" && /later opnieuw/.test(e.message));
  assert.deepEqual(geslapen, []);
  assert.equal(nep.afspraken["ik@voorbeeld.nl"].get("e1").status, "confirmed");
});

test("401: stil een nieuw token en dan verder; tweede 401 meteen erna: opnieuw verbinden", async () => {
  const { nep, g, tokens } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  await g.haal("ik@voorbeeld.nl", "e1"); // eerste token
  nep.geldigeTokens = new Set(["tok2"]); // token verlopen
  const r = await g.wijzig("ik@voorbeeld.nl", "e1", { summary: "nieuw" });
  assert.equal(r.summary, "nieuw");
  assert.equal(tokens(), 2);
  nep.storingen.push({ status: 401, reden: "authError" }, { status: 401, reden: "authError" });
  await assert.rejects(g.haal("ik@voorbeeld.nl", "e1"), (e) => e.soort === "inloggen");
});

test("401 en stil inloggen lukt niet: soort inloggen", async () => {
  const nep = maakNepGoogle();
  nep.agenda("a");
  let n = 0;
  const g = maakGoogle({ fetch: nep.fetch, haalToken: async () => { if (n++ === 0) return "tok1"; throw new Error("interaction_required"); }, slaap: async () => {} });
  nep.geldigeTokens = new Set();
  await assert.rejects(g.agendas(), (e) => e.soort === "inloggen");
});

test("403 forbidden in een alleen-lezen agenda: geen_toegang", async () => {
  const { nep, g } = opzet();
  nep.afspraak("feestdagen", afspraak("kerst"));
  await assert.rejects(g.verwijder("feestdagen", "kerst"), (e) => e.soort === "geen_toegang");
});

test("verplaatsen en terug met move", async () => {
  const { nep, g } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  await g.verplaats("ik@voorbeeld.nl", "e1", "werk#team@group.calendar.google.com");
  assert.ok(nep.afspraken["werk#team@group.calendar.google.com"].has("e1"));
  assert.equal(nep.log.at(-1).query.destination, "werk#team@group.calendar.google.com");
  await g.verplaats("werk#team@group.calendar.google.com", "e1", "ik@voorbeeld.nl");
  assert.ok(nep.afspraken["ik@voorbeeld.nl"].has("e1"));
});

test("verplaatsen: time-out na uitvoeren, herhaling 404, maar staat al in doel: gelukt", async () => {
  const { nep, g } = opzet();
  nep.afspraak("ik@voorbeeld.nl", afspraak("e1"));
  nep.storingen.push({ methode: "POST", status: 0, toch: true });
  const r = await g.verplaats("ik@voorbeeld.nl", "e1", "werk#team@group.calendar.google.com");
  assert.equal(r.id, "e1");
  assert.ok(nep.afspraken["werk#team@group.calendar.google.com"].has("e1"));
});

test("verplaatsen: 404 zonder herhaling blijft een fout (afspraak was er niet)", async () => {
  const { g } = opzet();
  await assert.rejects(g.verplaats("ik@voorbeeld.nl", "bestaatniet", "werk#team@group.calendar.google.com"), (e) => e.soort === "niet_gevonden");
});

test("antwoord zonder json (proxy-pagina) bij 500 wordt netwerk na herhalingen", async () => {
  const g = maakGoogle({ fetch: async () => ({ status: 502, ok: false, json: async () => { throw new Error("html"); } }), haalToken: async () => "t", slaap: async () => {} });
  await assert.rejects(g.agendas(), (e) => e.soort === "netwerk");
});
