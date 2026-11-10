// Toetsen (m) en (n, deel ontkoppelen) uit ontwerp-d1-worker.md, punt 7: ontkoppelen, wissen en Moneybird intrekken.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { Budget } from "../src/budget.ts";
import { ontkoppel, ontkoppelOpShopId } from "../src/d1/ontkoppel.ts";
import { DAG, NU, deps, nepRevoke, rij, taken, tel, vulWinkel } from "./ontkoppel-hulp.ts";

const TABELLEN = ["statussen", "transacties", "bestellingen", "sloten"];
const KALE_RIJ = ["id", "ontkoppeld_op", "taken", "mb_tokens", "polar_klant"];

test("(m) na ontkoppel: geen rijen meer, alleen de kale rij; andere winkel ongemoeid; alles in één budget van 50", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1", { polar: "polar-1" });
  await vulWinkel(db, "w2");
  const w2Voor = rij(db, "w2");
  const revoke = nepRevoke(500); // intrekken lukt niet: mb_tokens en polar_klant blijven bij een open taak
  const { d } = deps(revoke.fn);
  const budget = new Budget(50);
  const q0 = db.queries;
  const u = await ontkoppel(db, "w1", "knop", NU, budget, d);
  assert.deepEqual(u, { ontkoppeld: true, intrekken: "later" });
  const gebruikt = db.queries - q0 + revoke.verzoeken.length;
  assert.equal(gebruikt, 3, "één batch, één fetch, één update");
  assert.equal(budget.over, 50 - gebruikt, "D1 en fetch uit dezelfde pot");

  for (const t of TABELLEN) assert.equal(tel(db, t, "w1"), 0, t);
  const r = rij(db, "w1")!;
  assert.equal(r.ontkoppeld_op, NU);
  assert.equal(r.tt_tokens, null);
  assert.equal(r.shop_id, null);
  for (const [k, v] of Object.entries(r)) {
    if (KALE_RIJ.includes(k)) continue;
    assert.ok(v === null || v === 0, `kolom ${k} is niet leeg: ${v}`);
  }
  assert.ok(r.mb_tokens, "intrekken staat open: versleuteld token blijft");
  assert.equal(r.polar_klant, "polar-1", "opzeggen staat open: klant-id blijft");
  assert.deepEqual(taken(db, "w1"), { reden: "knop", intrekken: { pogingen: 1, eerste_poging: NU, laatste_poging: NU }, opzeggen: { voor: NU, pogingen: 0 } });

  assert.deepEqual(rij(db, "w2"), w2Voor, "andere winkel ongemoeid");
  for (const t of TABELLEN) assert.ok(tel(db, t, "w2") > 0, t);
});

test("(m) zonder Moneybird-tokens: geen fetch en geen taak intrekken; opzeggen staat klaar", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1", { mb: false });
  const revoke = nepRevoke();
  const budget = new Budget(50);
  assert.deepEqual(await ontkoppel(db, "w1", "knop", NU, budget, deps(revoke.fn).d), { ontkoppeld: true, intrekken: "geen" });
  assert.equal(revoke.verzoeken.length, 0);
  assert.equal(budget.over, 49);
  assert.deepEqual(taken(db, "w1"), { reden: "knop", opzeggen: { voor: NU, pogingen: 0 } });
});

test("(m) idempotent: al ontkoppeld of onbekend doet niets en geeft geen fout", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1");
  const revoke = nepRevoke();
  const { d } = deps(revoke.fn);
  await ontkoppel(db, "w1", "knop", NU, new Budget(50), d);
  const na = rij(db, "w1");
  assert.deepEqual(await ontkoppel(db, "w1", "webhook", NU + 5, new Budget(50), d), { ontkoppeld: false });
  assert.deepEqual(await ontkoppel(db, "w9", "knop", NU, new Budget(50), d), { ontkoppeld: false });
  assert.deepEqual(rij(db, "w1"), na);
  assert.equal(rij(db, "w9"), undefined);
  assert.equal(revoke.verzoeken.length, 1, "geen tweede intrekpoging");
});

test("(n) intrekken 200: refresh token met app-gegevens naar /oauth/revoke, token en taak weg", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1");
  const revoke = nepRevoke(200);
  assert.equal((await ontkoppel(db, "w1", "knop", NU, new Budget(50), deps(revoke.fn).d)).intrekken, "gelukt");
  assert.equal(revoke.verzoeken[0].url, "https://moneybird.com/oauth/revoke");
  assert.deepEqual(revoke.verzoeken[0].body, { client_id: "cid", client_secret: "geheim", token: "GEHEIM-r-w1" });
  assert.equal(rij(db, "w1")!.mb_tokens, null);
  assert.deepEqual(taken(db, "w1"), { reden: "knop", opzeggen: { voor: NU, pogingen: 0 } }, "opzeggen staat klaar voor het betaalstuk");
});

for (const s of [500, 429, "netwerk"] as const) {
  test(`(n) intrekken ${s}: taak blijft staan met eerste poging, token blijft versleuteld`, async () => {
    const db = new NepD1();
    await vulWinkel(db, "w1");
    const { d, alarmen } = deps(nepRevoke(s).fn);
    assert.equal((await ontkoppel(db, "w1", "knop", NU, new Budget(50), d)).intrekken, "later");
    assert.match(String(rij(db, "w1")!.mb_tokens), /^v1\./);
    assert.equal(taken(db, "w1").intrekken.eerste_poging, NU);
    assert.deepEqual(alarmen(), []);
  });
}

test("(n) intrekken 403: ALARM, token en taak weg, niet herhalen", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1");
  const { d, alarmen } = deps(nepRevoke(403).fn);
  assert.equal((await ontkoppel(db, "w1", "knop", NU, new Budget(50), d)).intrekken, "alarm");
  assert.equal(alarmen().length, 1);
  assert.match(alarmen()[0], /403/);
  assert.equal(rij(db, "w1")!.mb_tokens, null);
  assert.equal(taken(db, "w1").intrekken, undefined);
});

test("(n) budget op vóór de fetch: niets verstuurd, taak blijft zonder poging", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1");
  const revoke = nepRevoke();
  assert.equal((await ontkoppel(db, "w1", "knop", NU, new Budget(1), deps(revoke.fn).d)).intrekken, "uitgesteld");
  assert.equal(revoke.verzoeken.length, 0);
  assert.deepEqual(taken(db, "w1").intrekken, { pogingen: 0 });
  assert.equal(rij(db, "w1")!.ontkoppeld_op, NU, "ontkoppelen zelf is wel gebeurd");
});

test("webhook-hulp ontkoppelOpShopId: bekende shop_id ontkoppelt, onbekende of dubbele doet niets", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1");
  await vulWinkel(db, "w2");
  const { d } = deps(nepRevoke().fn);
  assert.deepEqual(await ontkoppelOpShopId(db, "shop-onbekend", "webhook", NU, new Budget(50), d), { ontkoppeld: false });
  const budget = new Budget(50);
  assert.equal((await ontkoppelOpShopId(db, "shop-w1", "webhook", NU, budget, d)).ontkoppeld, true);
  assert.equal(budget.over, 46, "opzoeken plus ontkoppelen");
  assert.equal(taken(db, "w1").reden, "webhook");
  assert.deepEqual(await ontkoppelOpShopId(db, "shop-w1", "webhook", NU + DAG, new Budget(50), d), { ontkoppeld: false }, "dubbele webhook");
  assert.equal(rij(db, "w2")!.ontkoppeld_op, null);
  const plan = JSON.stringify(db.sqlite.prepare("EXPLAIN QUERY PLAN SELECT id FROM winkels WHERE shop_id = ? AND ontkoppeld_op IS NULL").all("x"));
  assert.match(plan, /winkels_shop_id/);
});
