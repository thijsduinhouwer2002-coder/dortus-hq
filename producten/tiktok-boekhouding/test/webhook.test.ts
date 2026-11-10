// Toets (o), webhook-deel (ontwerp-d1-worker.md, versie 3e): handtekening, type 6 ontkoppelt, de rest doet niets.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { app, bos, nepRevoke, NU, rij, tel, vulWinkel } from "./ontkoppel-hulp.ts";
import { gelijk, handtekening, MAX_BODY, webhook, WEBHOOK_PAD } from "../src/webhook.ts";
import worker, { type Omgeving } from "../src/worker.ts";

const APP = { appKey: "abcdef", appSecret: "123" };
const SHOP = "7495540735365777507";

async function opzet(fetchFn = nepRevoke().fn) {
  const db = new NepD1();
  await vulWinkel(db, "w1");
  db.sqlite.prepare("UPDATE winkels SET shop_id = ? WHERE id = 'w1'").run(SHOP);
  const log: string[] = [];
  const o: Omgeving = {
    db: db as any, wachtrij: { sendBatch: async () => {} }, fetchFn, log: (r) => log.push(r), sleutels: bos,
    tiktokApp: APP, moneybirdApp: app, slaap: async () => {},
  };
  return { db, o, log };
}

async function verzoek(body: string, opties: { kop?: string | null; pad?: string; methode?: string } = {}) {
  const kop = opties.kop === undefined ? await handtekening(APP.appKey, APP.appSecret, body) : opties.kop;
  const headers: Record<string, string> = { "content-type": "application/json" };
  if (kop !== null) headers.authorization = kop;
  return new Request(`https://klopt.example${opties.pad ?? WEBHOOK_PAD}`, { method: opties.methode ?? "POST", headers, body: (opties.methode ?? "POST") === "GET" ? undefined : body });
}

const type6 = (shop: unknown = SHOP) => JSON.stringify({ type: 6, tts_notification_id: "7380066284010030891", shop_id: shop, timestamp: 1718305585, data: {} });

test("(o) handtekening: rekenvoorbeeld uit de docs van TikTok", async () => {
  const body = '{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}';
  assert.equal(await handtekening("abcdef", "123", body), "5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05");
  assert.ok(gelijk("abc", "abc"));
  assert.ok(!gelijk("abc", "abd"));
  assert.ok(!gelijk("abc", "abcd"));
});

test("(o) type 6 met bekende shop_id: winkel ontkoppeld, Moneybird ingetrokken, 200", async () => {
  const revoke = nepRevoke();
  const { db, o } = await opzet(revoke.fn);
  const r = await webhook(await verzoek(type6()), o, NU);
  assert.equal(r.status, 200);
  assert.ok(rij(db, "w1")!.ontkoppeld_op, "ontkoppeld_op gezet");
  assert.equal(tel(db, "statussen", "w1"), 0);
  assert.equal(revoke.verzoeken.length, 1);
  assert.match(revoke.verzoeken[0].url, /oauth\/revoke/);
});

test("(o) type 6 dubbel of onbekend: 200 en niets veranderd", async () => {
  const revoke = nepRevoke();
  const { db, o, log } = await opzet(revoke.fn);
  assert.equal((await webhook(await verzoek(type6()), o, NU)).status, 200);
  const na = JSON.stringify(rij(db, "w1"));
  assert.equal((await webhook(await verzoek(type6()), o, NU + 5)).status, 200);
  assert.equal(JSON.stringify(rij(db, "w1")), na, "tweede keer niets veranderd");
  assert.equal(revoke.verzoeken.length, 1);
  assert.equal((await webhook(await verzoek(type6("123")), o, NU)).status, 200);
  assert.ok(log.some((r) => r.includes("123") && r.includes("onbekend")));
});

test("(o) verkeerde of ontbrekende handtekening: 401 en niets veranderd", async () => {
  const revoke = nepRevoke();
  const { db, o } = await opzet(revoke.fn);
  const voor = JSON.stringify(rij(db, "w1"));
  const goed = await handtekening(APP.appKey, APP.appSecret, type6());
  assert.equal((await webhook(await verzoek(type6(), { kop: null }), o, NU)).status, 401);
  assert.equal((await webhook(await verzoek(type6(), { kop: "" }), o, NU)).status, 401);
  assert.equal((await webhook(await verzoek(type6(), { kop: `Bearer ${goed}` }), o, NU)).status, 401);
  assert.equal((await webhook(await verzoek(type6(), { kop: goed.toUpperCase() }), o, NU)).status, 401);
  // Handtekening van een andere body (spatie erbij): ruwe body telt.
  assert.equal((await webhook(await verzoek(type6() + " ", { kop: goed }), o, NU)).status, 401);
  // Goede handtekening met het verkeerde secret.
  assert.equal((await webhook(await verzoek(type6(), { kop: await handtekening(APP.appKey, "fout", type6()) }), o, NU)).status, 401);
  assert.equal(JSON.stringify(rij(db, "w1")), voor);
  assert.equal(revoke.verzoeken.length, 0);
});

test("(o) pad, methode, grootte, kapotte JSON en shop_id als getal", async () => {
  const { db, o, log } = await opzet();
  const voor = JSON.stringify(rij(db, "w1"));
  assert.equal((await webhook(await verzoek(type6(), { pad: "/iets" }), o, NU)).status, 404);
  assert.equal((await webhook(await verzoek("", { methode: "GET" }), o, NU)).status, 405);
  const groot = JSON.stringify({ type: 6, shop_id: SHOP, x: "a".repeat(MAX_BODY) });
  assert.equal((await webhook(await verzoek(groot), o, NU)).status, 413);
  assert.equal((await webhook(await verzoek("{kapot"), o, NU)).status, 400);
  assert.equal((await webhook(await verzoek("[1]"), o, NU)).status, 400);
  // 19 cijfers als JSON-getal: afgerond door JSON.parse, dus weigeren (nooit een verkeerde winkel ontkoppelen).
  const alsGetal = `{"type":6,"shop_id":${SHOP},"timestamp":1}`;
  assert.equal((await webhook(await verzoek(alsGetal), o, NU)).status, 400);
  assert.equal((await webhook(await verzoek(JSON.stringify({ type: 6 })), o, NU)).status, 400);
  assert.equal(JSON.stringify(rij(db, "w1")), voor);
  assert.ok(!log.some((r) => r.includes("a".repeat(20))), "geen body in het log");
});

test("(o) type 7 en andere typen: 200, niets veranderd; type 7 logt alleen de shop_id", async () => {
  const revoke = nepRevoke();
  const { db, o, log } = await opzet(revoke.fn);
  const voor = JSON.stringify(rij(db, "w1"));
  assert.equal((await webhook(await verzoek(JSON.stringify({ type: 7, shop_id: SHOP, data: { expiration_time: 1 } })), o, NU)).status, 200);
  assert.equal((await webhook(await verzoek(JSON.stringify({ type: 1, shop_id: SHOP, data: { order_id: "9" } })), o, NU)).status, 200);
  assert.equal((await webhook(await verzoek(JSON.stringify({ type: "6x", shop_id: SHOP })), o, NU)).status, 200);
  assert.equal(JSON.stringify(rij(db, "w1")), voor);
  assert.equal(revoke.verzoeken.length, 0);
  assert.deepEqual(log, [`webhook type 7: koppeling van shop_id ${SHOP} verloopt binnenkort`]);
});

test("(o) type 6 als tekst werkt ook; D1 onbereikbaar geeft 500", async () => {
  const { db, o } = await opzet();
  const r = await webhook(await verzoek(JSON.stringify({ type: "6", shop_id: SHOP })), o, NU);
  assert.equal(r.status, 200);
  assert.ok(rij(db, "w1")!.ontkoppeld_op);
  const { o: o2, log } = await opzet();
  o2.db = { prepare: () => { throw new Error("D1 weg"); }, batch: async () => { throw new Error("D1 weg"); } } as any;
  assert.equal((await webhook(await verzoek(type6()), o2, NU)).status, 500);
  assert.ok(log.some((r) => r.includes("mislukt")));
});

test("(o) export default fetch: env onbruikbaar geeft 500, anders naar de webhook", async () => {
  const r = await worker.fetch(await verzoek(type6()), { TOKEN_SLEUTELS: "geen json" } as any);
  assert.equal(r.status, 500);
});
