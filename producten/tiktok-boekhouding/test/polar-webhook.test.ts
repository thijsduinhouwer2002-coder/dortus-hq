// Toetsen (a), (b), (c, webhook-deel) en (k) uit ontwerp-betalen.md, punt 7: de webhook van Polar.
import { test } from "node:test";
import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import { NepD1 } from "./d1-nep.ts";
import { app, bos, NU, rij } from "./ontkoppel-hulp.ts";
import { MAX_BODY, POLAR_WEBHOOK_PAD, controleer, polarWebhook, sleutelsVan, tekenPolar } from "../src/polar/webhook.ts";
import worker, { type Omgeving } from "../src/worker.ts";

// Toetsvector van Standard Webhooks/Svix (ontwerp-betalen.md, punt 3).
const SECRET = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw";
const enc = new TextEncoder();

async function opzet() {
  const db = new NepD1("w1", "w2");
  const log: string[] = [];
  const verzoekenNaarBuiten: string[] = [];
  const o: Omgeving = {
    db: db as any, wachtrij: { sendBatch: async () => {} }, log: (r) => log.push(r), sleutels: bos,
    fetchFn: (async (u: any) => { verzoekenNaarBuiten.push(String(u)); throw new Error("geen verzoeken naar buiten"); }) as typeof fetch,
    tiktokApp: { appKey: "k", appSecret: "s" }, moneybirdApp: app, slaap: async () => {},
    polar: { api: "https://sandbox-api.polar.sh", token: "tok", productId: "prod", webhookSecret: SECRET },
  };
  return { db, o, log, verzoekenNaarBuiten };
}

const iso = (s: number, micro = 0) => new Date(s * 1000).toISOString().replace(/\.\d{3}Z$/, `.${String(micro).padStart(6, "0")}Z`);
const abo = (db: NepD1, w: string) => JSON.parse(String(rij(db, w)!.abonnement ?? "null"));

interface Sub { id: string; winkel?: string | number; eind: number; opgezegd?: boolean }
const sub = (s: Sub) => ({
  id: s.id, created_at: iso(NU - 100), modified_at: null, metadata: s.winkel === undefined ? {} : { winkel: s.winkel }, status: "active",
  amount: 1500, currency: "eur", recurring_interval: "month", current_period_start: iso(s.eind - 30 * 86400), current_period_end: iso(s.eind),
  trial_start: null, trial_end: null, cancel_at_period_end: s.opgezegd ?? false, canceled_at: null, started_at: iso(NU - 100), ends_at: null,
  product_id: "prod", discount_id: null, seats: null, units: null, meters: [],
});
function stateChanged(tijd: string, opties: { winkel?: string | null; subs?: Sub[]; verwijderd?: boolean; klant?: string } = {}) {
  return JSON.stringify({
    type: "customer.state_changed", timestamp: tijd, api_version: "2026-10",
    data: {
      id: opties.klant ?? "cus-1", type: "individual", external_id: opties.winkel === undefined ? "w1" : opties.winkel,
      email: "geheim@voorbeeld.nl", name: "Geheime Naam", deleted_at: opties.verwijderd ? iso(NU) : null,
      active_subscriptions: (opties.subs ?? []).map(sub), granted_benefits: [], active_meters: [],
    },
  });
}
function abonnementEvent(type: string, tijd: string, opties: { winkel?: string; extern?: string | null; status?: string } = {}) {
  return JSON.stringify({
    type, timestamp: tijd, api_version: "2026-10",
    data: {
      id: "sub-1", status: opties.status ?? (type === "subscription.past_due" ? "past_due" : "active"),
      metadata: opties.winkel === undefined ? {} : { winkel: opties.winkel },
      customer: { id: "cus-1", external_id: opties.extern === undefined ? "w1" : opties.extern, email: "geheim@voorbeeld.nl" },
      current_period_end: iso(NU + 30 * 86400), cancel_at_period_end: false,
    },
  });
}

interface VerzoekOpties { kopTijd?: number; id?: string; handtekening?: string | null; versie?: string | null; secret?: string; schema?: 0 | 1; pad?: string; zonder?: string }
async function verzoek(body: string, opties: VerzoekOpties = {}) {
  const id = opties.id ?? "msg_1";
  const tijd = String(opties.kopTijd ?? NU);
  const sleutel = sleutelsVan(opties.secret ?? SECRET)[opties.schema ?? 0];
  const sig = opties.handtekening === undefined ? await tekenPolar(sleutel, id, tijd, enc.encode(body)) : opties.handtekening;
  const headers: Record<string, string> = { "content-type": "application/json", "webhook-id": id, "webhook-timestamp": tijd };
  if (sig !== null) headers["webhook-signature"] = sig;
  if (opties.versie !== null) headers["webhook-api-version"] = opties.versie ?? "2026-10";
  if (opties.zonder) delete headers[opties.zonder];
  return new Request(`https://klopt.example${opties.pad ?? POLAR_WEBHOOK_PAD}`, { method: "POST", headers, body });
}

const status = async (o: Omgeving, body: string, opties: VerzoekOpties = {}, nu = NU) => (await polarWebhook(await verzoek(body, opties), o, nu)).status;

// --- (a) handtekening ----------------------------------------------------------------------------------------------

test("(a) beide toetsvectoren, nagerekend met node:crypto", async () => {
  const id = "msg_p5jXN8AQM9LWM0D4loKWxJek";
  const tijd = "1614265330";
  const body = enc.encode('{"test": 2432232314}');
  const [a, b] = sleutelsVan(SECRET);
  assert.equal(await tekenPolar(a, id, tijd, body), "v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=");
  assert.equal(await tekenPolar(b, id, tijd, body), "v1,TcxlhK9b6UD6iVI1ZU2tTqp8PEVfYRseNNfa6b+LcUg=");
  const zelf = (k: Buffer) => "v1," + createHmac("sha256", k).update(`${id}.${tijd}.{"test": 2432232314}`).digest("base64");
  assert.equal(zelf(Buffer.from(SECRET.slice(6), "base64")), "v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=");
  assert.equal(zelf(Buffer.from(SECRET, "utf8")), "v1,TcxlhK9b6UD6iVI1ZU2tTqp8PEVfYRseNNfa6b+LcUg=");
  // De hele controle met de vectoren, met de tijd van de vector als "nu".
  for (const sig of ["v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=", "v1,TcxlhK9b6UD6iVI1ZU2tTqp8PEVfYRseNNfa6b+LcUg="]) {
    const koppen = new Headers({ "webhook-id": id, "webhook-timestamp": tijd, "webhook-signature": sig });
    assert.equal(await controleer(SECRET, koppen, body, 1614265330), null);
  }
});

test("(a) webhook met sleutelschema (a) en met (b) wordt allebei verwerkt", async () => {
  for (const schema of [0, 1] as const) {
    const { db, o } = await opzet();
    assert.equal(await status(o, stateChanged(iso(NU), { subs: [{ id: "sub-1", eind: NU + 1000 }] }), { schema }), 202);
    assert.equal(abo(db, "w1").actief, true, `schema ${schema}`);
  }
});

test("(a) meerdere handtekeningen in de kop: één goede is genoeg", async () => {
  const { db, o } = await opzet();
  const body = stateChanged(iso(NU), { subs: [{ id: "sub-1", eind: NU + 1000 }] });
  const goed = await tekenPolar(sleutelsVan(SECRET)[0], "msg_1", String(NU), enc.encode(body));
  const fout = "v1,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=";
  assert.equal(await status(o, body, { handtekening: `${fout} v2,iets ${goed}` }), 202, "achteraan");
  assert.equal(abo(db, "w1").actief, true);
  for (const kop of [`${goed} ${fout}`, `${fout} ${goed} v1,BBBB`]) {
    const { db: db2, o: o2 } = await opzet();
    assert.equal(await status(o2, body, { handtekening: kop }), 202, kop);
    assert.equal(abo(db2, "w1").actief, true, "vooraan en in het midden");
  }
});

test("(a) verkeerd secret, buiten 5 minuten, ontbrekende kop of andere body: 403 met ALARM en niets veranderd", async () => {
  const { db, o, log } = await opzet();
  const body = stateChanged(iso(NU), { subs: [{ id: "sub-1", eind: NU + 1000 }] });
  const voor = JSON.stringify(rij(db, "w1"));
  const gevallen: VerzoekOpties[] = [
    { secret: "whsec_" + Buffer.from("ander geheim van 32 tekens lang!").toString("base64") },
    { secret: "whsec_ander" },
    { kopTijd: NU - 301 },
    { kopTijd: NU + 301 },
    { zonder: "webhook-signature" },
    { zonder: "webhook-id" },
    { zonder: "webhook-timestamp" },
    { handtekening: "" },
    { handtekening: "v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=" },
  ];
  for (const g of gevallen) assert.equal(await status(o, body, g), 403, JSON.stringify(g));
  // Getekend over een andere body (spatie erbij): ruwe body telt.
  const anders = await tekenPolar(sleutelsVan(SECRET)[0], "msg_1", String(NU), enc.encode(body + " "));
  assert.equal(await status(o, body, { handtekening: anders }), 403);
  assert.equal(JSON.stringify(rij(db, "w1")), voor);
  assert.equal(log.filter((r) => r.startsWith("ALARM")).length, gevallen.length + 1);
  // Precies op de rand van 5 minuten mag nog.
  assert.equal(await status(o, body, { kopTijd: NU - 300 }), 202);
});

test("(a) zonder secret: 500 met ALARM, niets veranderd", async () => {
  const { db, o, log } = await opzet();
  o.polar = undefined;
  const voor = JSON.stringify(rij(db, "w1"));
  assert.equal(await status(o, stateChanged(iso(NU), { subs: [{ id: "sub-1", eind: NU + 1000 }] })), 500);
  assert.equal(JSON.stringify(rij(db, "w1")), voor);
  assert.ok(log.some((r) => r.startsWith("ALARM") && r.includes("POLAR_WEBHOOK_SECRET")));
});

// --- (b) state_changed ---------------------------------------------------------------------------------------------

test("(b) state_changed zet actief, tot, id, opgezegd, stand en polar_klant; geen verzoek naar buiten, geen e-mail in het log", async () => {
  const { db, o, log, verzoekenNaarBuiten } = await opzet();
  const eind = NU + 30 * 86400;
  assert.equal(await status(o, stateChanged(iso(NU, 123456), { subs: [{ id: "sub-1", eind, opgezegd: true }] })), 202);
  assert.deepEqual(abo(db, "w1"), { actief: true, tot: eind, id: "sub-1", opgezegd: true, stand: NU * 1_000_000 + 123456 });
  assert.equal(rij(db, "w1")!.polar_klant, "cus-1");
  assert.equal(rij(db, "w2")!.abonnement, null, "andere winkel ongemoeid");
  assert.equal(verzoekenNaarBuiten.length, 0);
  assert.ok(!log.some((r) => r.includes("geheim@") || r.includes("Geheime")), "geen e-mail of naam in het log");
  assert.ok(log.some((r) => r.includes("customer.state_changed") && r.includes("w1") && r.includes("msg_1")));
  // In SQL leesbaar zoals punt 2 het gebruikt.
  const actief = db.sqlite.prepare("SELECT json_extract(abonnement, '$.actief') = 1 AND json_extract(abonnement, '$.tot') > ? a FROM winkels WHERE id = 'w1'").get(NU) as any;
  assert.equal(actief.a, 1);
});

test("(b) oude of dubbele webhook doet niets; een herhaalde oude met nieuwe kop-tijd verliest van een nieuwere", async () => {
  const { db, o } = await opzet();
  const oud = stateChanged(iso(NU), { subs: [{ id: "sub-oud", eind: NU + 1000 }] });
  const nieuw = stateChanged(iso(NU, 1), { subs: [] }); // één microseconde later: abonnement weg
  assert.equal(await status(o, oud, { id: "msg_oud" }), 202);
  assert.equal(abo(db, "w1").id, "sub-oud");
  assert.equal(await status(o, nieuw, { id: "msg_nieuw", kopTijd: NU + 10 }, NU + 10), 202);
  const naNieuw = JSON.stringify(rij(db, "w1"));
  assert.equal(abo(db, "w1").actief, false);
  // Polar herhaalt de oude: zelfde body en id, nieuwe kop-tijd (geldig getekend).
  assert.equal(await status(o, oud, { id: "msg_oud", kopTijd: NU + 600 }, NU + 600), 202);
  assert.equal(JSON.stringify(rij(db, "w1")), naNieuw, "oude herhaling wint niet");
  // Dubbel van de nieuwe.
  assert.equal(await status(o, nieuw, { id: "msg_nieuw", kopTijd: NU + 700 }, NU + 700), 202);
  assert.equal(JSON.stringify(rij(db, "w1")), naNieuw);
});

test("(b) onbekende of ontkoppelde winkel en ontbrekende sleutel: 202, niets geschreven", async () => {
  const { db, o, log } = await opzet();
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = ? WHERE id = 'w2'").run(NU);
  const voor = JSON.stringify(db.sqlite.prepare("SELECT * FROM winkels ORDER BY id").all());
  const subs = [{ id: "sub-1", eind: NU + 1000 }];
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: "w9", subs })), 202);
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: "w2", subs })), 202);
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: null, subs })), 202);
  assert.equal(await status(o, abonnementEvent("subscription.past_due", iso(NU), { extern: "w2" })), 202);
  assert.equal(await status(o, abonnementEvent("subscription.past_due", iso(NU), { winkel: "w9" })), 202);
  assert.equal(JSON.stringify(db.sqlite.prepare("SELECT * FROM winkels ORDER BY id").all()), voor);
  assert.equal(rij(db, "w9"), undefined);
  assert.ok(log.some((r) => r.includes("w9") && r.includes("niets geschreven")));
});

test("(b) andere of ontbrekende webhook-api-version: 202 en niets gedaan", async () => {
  const { db, o, log } = await opzet();
  const body = stateChanged(iso(NU), { subs: [{ id: "sub-1", eind: NU + 1000 }] });
  assert.equal(await status(o, body, { versie: "2026-11" }), 202);
  assert.equal(await status(o, body, { versie: null }), 202);
  assert.equal(rij(db, "w1")!.abonnement, null);
  assert.ok(log.some((r) => r.includes("2026-11")));
});

test("(b) verwijderde klant of geen abonnement: niet actief", async () => {
  const { db, o } = await opzet();
  await status(o, stateChanged(iso(NU), { subs: [{ id: "sub-1", eind: NU + 1000 }] }));
  await status(o, stateChanged(iso(NU + 1), { verwijderd: true, subs: [{ id: "sub-1", eind: NU + 1000 }] }));
  assert.deepEqual(abo(db, "w1"), { actief: false, tot: null, id: null, opgezegd: false, stand: (NU + 1) * 1_000_000 });
});

// --- (c) keuze en andere winkel ------------------------------------------------------------------------------------

test("(c) keuze in de webhook: abonnement met metadata.winkel van deze winkel, niet dat van een andere", async () => {
  const { db, o } = await opzet();
  const subs = [{ id: "sub-w2", winkel: "w2", eind: NU + 9000 }, { id: "sub-w1", winkel: "w1", eind: NU + 1000 }];
  await status(o, stateChanged(iso(NU), { subs }));
  assert.equal(abo(db, "w1").id, "sub-w1");
  assert.equal(abo(db, "w1").tot, NU + 1000);
});

test("(c) past_due voor een andere winkel (metadata.winkel w2, klant w1) doet niets bij w1", async () => {
  const { db, o } = await opzet();
  assert.equal(await status(o, abonnementEvent("subscription.past_due", iso(NU), { winkel: "w2", extern: "w1" })), 202);
  assert.equal(rij(db, "w1")!.abonnement, null);
  assert.equal(abo(db, "w2").betalingMislukt, true, "hij is van w2");
});

// --- (k) vlag betalingMislukt --------------------------------------------------------------------------------------

test("(k) past_due zet de vlag; active, uncanceled en updated(active) wissen hem; updated met andere status niet", async () => {
  const { db, o } = await opzet();
  let t = NU;
  const zet = async () => assert.equal(await status(o, abonnementEvent("subscription.past_due", iso(++t))), 202);
  await zet();
  assert.equal(abo(db, "w1").betalingMislukt, true);
  assert.equal(await status(o, abonnementEvent("subscription.updated", iso(++t), { status: "past_due" })), 202);
  assert.equal(abo(db, "w1").betalingMislukt, true, "updated met status past_due laat de vlag staan");
  for (const [type, extra] of [["subscription.active", {}], ["subscription.uncanceled", {}], ["subscription.updated", { status: "active" }]] as const) {
    await zet();
    assert.equal(await status(o, abonnementEvent(type, iso(++t), extra)), 202);
    assert.equal(abo(db, "w1").betalingMislukt, false, type);
  }
  // Via metadata.winkel zonder external_id op de klant.
  assert.equal(await status(o, abonnementEvent("subscription.past_due", iso(++t), { winkel: "w1", extern: null })), 202);
  assert.equal(abo(db, "w1").betalingMislukt, true);
  // Oudere active dan de laatste past_due: doet niets.
  assert.equal(await status(o, abonnementEvent("subscription.active", iso(NU))), 202);
  assert.equal(abo(db, "w1").betalingMislukt, true);
});

test("(k) state_changed wist de vlag niet, past_due raakt actief en tot niet; elke soort heeft zijn eigen stand", async () => {
  const { db, o } = await opzet();
  const eind = NU + 30 * 86400;
  await status(o, stateChanged(iso(NU + 10), { subs: [{ id: "sub-1", eind }] }));
  // past_due met een oudere tijd dan de laatste state_changed: wordt toch gezet (eigen stand).
  assert.equal(await status(o, abonnementEvent("subscription.past_due", iso(NU + 5))), 202);
  assert.deepEqual(abo(db, "w1"), { actief: true, tot: eind, id: "sub-1", opgezegd: false, stand: (NU + 10) * 1_000_000, betalingMislukt: true, vlagStand: (NU + 5) * 1_000_000 });
  await status(o, stateChanged(iso(NU + 20), { subs: [{ id: "sub-1", eind: eind + 1 }] }));
  assert.equal(abo(db, "w1").betalingMislukt, true, "state_changed laat de vlag staan");
  assert.equal(abo(db, "w1").tot, eind + 1);
});

// --- rest ----------------------------------------------------------------------------------------------------------

test("pad, methode, 413, kapotte JSON, andere events en ontbrekende timestamp", async () => {
  const { db, o } = await opzet();
  const voor = JSON.stringify(rij(db, "w1"));
  assert.equal(await status(o, "{}", { pad: "/polar/iets" }), 404);
  assert.equal((await polarWebhook(new Request(`https://k${POLAR_WEBHOOK_PAD}`), o, NU)).status, 405);
  const groot = JSON.stringify({ type: "customer.state_changed", x: "a".repeat(MAX_BODY) });
  assert.equal(await status(o, groot), 413);
  assert.equal(await status(o, "{kapot"), 400);
  assert.equal(await status(o, JSON.stringify({ type: "order.paid", timestamp: iso(NU), data: { customer: { external_id: "w1" } } })), 202);
  assert.equal(await status(o, JSON.stringify({ type: "customer.state_changed", data: { external_id: "w1", active_subscriptions: [] } })), 202);
  assert.equal(await status(o, JSON.stringify({ type: "customer.state_changed", timestamp: "gisteren", data: { external_id: "w1" } })), 202);
  assert.equal(JSON.stringify(rij(db, "w1")), voor);
});

test("D1 faalt: 500 (Polar probeert opnieuw)", async () => {
  const { o, log } = await opzet();
  o.db = { prepare: () => ({ bind: () => ({ run: async () => { throw new Error("D1 weg"); } }) }), batch: async () => { throw new Error("D1 weg"); } } as any;
  assert.equal(await status(o, stateChanged(iso(NU), { subs: [] })), 500);
  assert.equal(await status(o, abonnementEvent("subscription.past_due", iso(NU))), 500);
  assert.ok(log.some((r) => r.includes("D1 mislukt")));
});

test("export default fetch: /polar/webhook gaat naar de Polar-webhook", async () => {
  const db = new NepD1("w1");
  const nu = Math.floor(Date.now() / 1000);
  const env = {
    DB: db, WACHTRIJ: { sendBatch: async () => {} }, TOKEN_SLEUTELS: JSON.stringify({ v1: Buffer.alloc(32).toString("base64") }), TOKEN_SLEUTEL_HUIDIG: "v1",
    TIKTOK_APP_KEY: "k", TIKTOK_APP_SECRET: "s", MONEYBIRD_CLIENT_ID: "c", MONEYBIRD_CLIENT_SECRET: "g", MONEYBIRD_REDIRECT_URI: "https://x",
    POLAR_WEBHOOK_SECRET: SECRET,
  };
  const r = await worker.fetch(await verzoek(stateChanged(iso(nu), { subs: [{ id: "sub-1", eind: nu + 1000 }] }), { kopTijd: nu }), env as any);
  assert.equal(r.status, 202);
  assert.equal(abo(db, "w1").actief, true);
  // Zonder secret in de env: 500.
  const r2 = await worker.fetch(await verzoek(stateChanged(iso(nu), { subs: [] }), { kopTijd: nu }), { ...env, POLAR_WEBHOOK_SECRET: undefined } as any);
  assert.equal(r2.status, 500);
});

test("ALARM: state_changed met een lopend, niet opgezegd abonnement voor een ontkoppelde of onbekende winkel", async () => {
  const { db, o, log } = await opzet();
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = ? WHERE id = 'w2'").run(NU);
  const alarmen = () => log.filter((r) => r.startsWith("ALARM"));
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: "w2", subs: [{ id: "sub-1", eind: NU + 1000 }] })), 202);
  assert.equal(alarmen().length, 1);
  assert.match(alarmen()[0], /w2/);
  assert.ok(!alarmen()[0].includes("geheim@"), "geen e-mail in het log");
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: "w9", subs: [{ id: "sub-1", winkel: "w9", eind: NU + 1000 }] })), 202);
  assert.equal(alarmen().length, 2, "onbekende winkel ook");
  // Geen ALARM: opgezegd, geen abonnement, abonnement van een andere winkel, of een gewone oude webhook bij een gekoppelde winkel.
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: "w2", subs: [{ id: "sub-1", eind: NU + 1000, opgezegd: true }] })), 202);
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: "w2", subs: [] })), 202);
  assert.equal(await status(o, stateChanged(iso(NU), { winkel: "w2", subs: [{ id: "sub-x", winkel: "w1", eind: NU + 1000 }] })), 202);
  await status(o, stateChanged(iso(NU + 5), { subs: [{ id: "sub-1", eind: NU + 1000 }] }));
  assert.equal(await status(o, stateChanged(iso(NU), { subs: [{ id: "sub-1", eind: NU + 1000 }] })), 202);
  assert.equal(alarmen().length, 2);
  assert.equal(rij(db, "w2")!.abonnement, null, "niets geschreven");
});
