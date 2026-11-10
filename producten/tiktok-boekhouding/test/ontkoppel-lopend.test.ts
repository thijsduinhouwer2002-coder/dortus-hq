// Toets (l) uit ontwerp-d1-worker.md, punt 7: ontkoppelen terwijl verwerkWinkel nog loopt.
import { test } from "node:test";
import assert from "node:assert/strict";
import { TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { MoneybirdClient } from "../src/moneybird/client.ts";
import { Budget } from "../src/budget.ts";
import { D1Opslag } from "../src/d1/opslag.ts";
import { ontkoppel } from "../src/d1/ontkoppel.ts";
import { winkelsAanDeBeurt } from "../src/d1/winkels.ts";
import { verwerkWinkel, type BoekDeps } from "../src/verwerk.ts";
import { versleutel } from "../src/d1/tokens.ts";
import { NepD1 } from "./d1-nep.ts";
import { inst, T0, wereld } from "./wereld.ts";
import { bos, deps, nepRevoke } from "./ontkoppel-hulp.ts";

type Wereld = ReturnType<typeof wereld>;
const NU = T0 + 10 * 86400;

function boekDeps(w: Wereld, opslag: D1Opslag, fetchFn: typeof fetch): BoekDeps {
  const budget = new Budget(100);
  const f = budget.omhul(fetchFn);
  return {
    tiktok: new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: f, nu: () => NU, slaap: async () => {} }),
    moneybird: new MoneybirdClient({ accessToken: "m", fetchFn: f, nu: () => NU, slaap: async () => {} }),
    accessToken: "t", shopCipher: "c", opslag, budget, nu: () => NU, eigenaar: `run-${NU}`,
  };
}

async function opzet() {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10, 20]);
  w.voegToe("7002", T0 + 2 * 86400, "PAID", [30]);
  const db = new NepD1("w1", "w2");
  db.sqlite.prepare("UPDATE winkels SET mb_tokens = ?, volgende_run = 5").run(await versleutel(bos, "w1", JSON.stringify({ accessToken: "a", refreshToken: "r" })));
  const revoke = nepRevoke(200);
  const knop = () => ontkoppel(db, "w1", "knop", NU, new Budget(50), deps(revoke.fn).d);
  const opslag = new D1Opslag(db, "w1", new Budget(100_000));
  const posts = () => w.urls.filter((u) => u.startsWith("POST MB")).length;
  const rijen = () => ["statussen", "transacties", "bestellingen", "sloten"].reduce((n, t) => n + Number((db.sqlite.prepare(`SELECT count(*) n FROM ${t} WHERE winkel = 'w1'`).get() as any).n), 0);
  return { w, db, revoke, knop, opslag, posts, rijen };
}

async function naAfloop(o: Awaited<ReturnType<typeof opzet>>, r: Awaited<ReturnType<typeof verwerkWinkel>>) {
  await o.opslag.klaar();
  assert.equal(r.winkel?.soort, "ontkoppeld");
  assert.equal(o.rijen(), 0, "na afloop van de aanroep geen rijen van de winkel terug in D1");
  assert.equal(o.revoke.verzoeken.length, 1, "Moneybird ingetrokken");
  assert.deepEqual(await winkelsAanDeBeurt(o.db, NU, new Budget(50).opslagTeller()), ["w2"], "cron pakt de winkel niet meer op");
}

test("(l) ontkoppelen tijdens het ophalen van bestellingen: geen POST, niets terug in D1", async () => {
  const o = await opzet();
  let gedaan = false;
  const fn = (async (i: any, init: any) => {
    if (!gedaan && String(i).includes("/orders/")) { gedaan = true; await o.knop(); }
    return o.w.fn(i, init);
  }) as typeof fetch;
  const r = await verwerkWinkel(boekDeps(o.w, o.opslag, fn), inst());
  assert.equal(o.posts(), 0);
  await naAfloop(o, r);
});

test("(l) ontkoppelen na het ophalen, vlak voor de laatste slotcontrole: geen POST", async () => {
  const o = await opzet();
  const echt = o.opslag.startBoeking.bind(o.opslag);
  o.opslag.startBoeking = async (...a) => { await o.knop(); return echt(...a); };
  const r = await verwerkWinkel(boekDeps(o.w, o.opslag, o.w.fn), inst());
  assert.equal(o.posts(), 0);
  await naAfloop(o, r);
});

test("(l) ontkoppelen tussen twee afrekeningen, de tweede had nog geen slotrij: alleen de eerste geboekt", async () => {
  const o = await opzet();
  const echt = o.opslag.neemSlot.bind(o.opslag);
  o.opslag.neemSlot = async (id, ...a) => { if (id === "7002") await o.knop(); return echt(id, ...a); };
  const r = await verwerkWinkel(boekDeps(o.w, o.opslag, o.w.fn), inst());
  assert.equal(o.posts(), 1, "7001 was al geboekt vóór de klik");
  assert.ok(!o.w.urls.some((u) => u.includes("/statements/7002/")), "7002 niet meer opgehaald");
  await naAfloop(o, r);
});

test("(l) cron-query gebruikt de gedeeltelijke index en slaat ontkoppelde winkels over", async () => {
  const db = new NepD1("w1", "w2");
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 1 WHERE id = 'w1'").run();
  const budget = new Budget(50);
  assert.deepEqual(await winkelsAanDeBeurt(db, 10, budget.opslagTeller()), ["w2"]);
  assert.equal(budget.over, 49);
  const plan = JSON.stringify(db.sqlite.prepare("EXPLAIN QUERY PLAN SELECT id FROM winkels WHERE volgende_run <= ? AND ontkoppeld_op IS NULL ORDER BY volgende_run LIMIT ?").all(10, 100));
  assert.match(plan, /winkels_volgende_run/);
});
