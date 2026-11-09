// Toetsen voor D1Opslag (ontwerp-d1-worker.md, "Af als" c, d, e-deel, i-deel, k). De rest (a, b, f, g, h, j, opruimen per cron) volgt in deel 2.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { D1Opslag, MAX_RIJ } from "../src/d1/opslag.ts";
import { Budget, isBudgetOp } from "../src/budget.ts";

const best = (n: number) => ({ antwoord: { order_id: String(n) } as any, opgehaaldOp: 100 + n });
const status = (s: string, extra: Record<string, unknown> = {}) => ({ status: s, sinds: 1, statementTime: 1700000000, ...extra });

test("(c) slot: twee eigenaars, één krijgt het; verlopen slot gaat over; slotTot leest vers", async () => {
  const db = new NepD1();
  const a = new D1Opslag(db, "w1", new Budget(50));
  const b = new D1Opslag(db, "w1", new Budget(50));
  assert.equal(await a.neemSlot("s1", "A", 1300, 1000), true);
  assert.equal(await b.neemSlot("s1", "B", 1300, 1000), false);
  assert.equal(await a.neemSlot("s1", "A", 1400, 1000), true, "eigen slot verlengen mag");
  assert.equal(await b.neemSlot("s1", "B", 1700, 1500), true, "verlopen slot gaat over");
  assert.equal(await a.slotTot("s1", "A"), null);
  assert.equal(await b.slotTot("s1", "B"), 1700);
  db.sqlite.prepare("UPDATE sloten SET tot = 99").run();
  assert.equal(await b.slotTot("s1", "B"), 99, "buiten de opslag om gewijzigd, toch vers gelezen");
  await a.geefSlotTerug("s1", "A");
  assert.equal(await b.slotTot("s1", "B"), 99, "een ander kan mijn slot niet teruggeven");
});

test("(c) neemSlot leegt het geheugen: daarna weer vers uit D1", async () => {
  const db = new NepD1();
  const o = new D1Opslag(db, "w1", new Budget(50));
  assert.equal(await o.leesBestelling("s1", "1"), undefined);
  db.sqlite.prepare("INSERT INTO bestellingen VALUES ('w1','s1','1',?,5)").run(JSON.stringify(best(1)));
  assert.equal(await o.leesBestelling("s1", "1"), undefined, "uit het geheugen");
  await o.neemSlot("s1", "A", 2000, 1000);
  assert.deepEqual(await o.leesBestelling("s1", "1"), best(1));
});

test("(d) wachtrij gaat mee met schrijfStatus in één batch; eigen schrijfacties terug te lezen; 30 bestellingen ≤ 8 queries", async () => {
  const db = new NepD1();
  const o = new D1Opslag(db, "w1", new Budget(50));
  await o.neemSlot("s1", "A", 2000, 1000);
  await o.leesStatus("s1");
  for (let i = 1; i <= 30; i++) {
    assert.equal(await o.leesBestelling("s1", String(i)), undefined);
    await o.schrijfBestelling("s1", String(i), best(i));
  }
  await o.schrijfTransacties("s1", { kop: undefined, transacties: [], opgehaaldOp: 7 });
  assert.deepEqual(await o.leesBestelling("s1", "3"), best(3), "eigen schrijfactie");
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM bestellingen").get() as any).n), 0, "nog niets geschreven");
  await o.schrijfStatus("s1", status("compleet"));
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM bestellingen").get() as any).n), 30);
  assert.equal(await o.slotTot("s1", "A"), 2000);
  await o.geefSlotTerug("s1", "A");
  assert.ok(db.queries <= 8, `queries ${db.queries}`);
  assert.equal(o.schrijfacties, 32);
});

test("(d) een batch die faalt laat niets half achter en de wachtrij blijft staan", async () => {
  const db = new NepD1();
  const o = new D1Opslag(db, "w1", new Budget(50));
  await o.leesBestelling("s1", "1");
  await o.schrijfBestelling("s1", "1", best(1));
  await o.schrijfBestelling("s1", "2", best(2));
  db.faalBijStatement = 2; // de status
  await assert.rejects(o.schrijfStatus("s1", status("compleet")));
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM bestellingen").get() as any).n), 0);
  assert.equal(await new D1Opslag(db, "w1", new Budget(50)).leesStatus("s1"), undefined);
  await o.schrijfStatus("s1", status("compleet"));
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM bestellingen").get() as any).n), 2);
});

test("(e) budget: nieuw werk weigert bij de reserve, afmaken gaat door", async () => {
  const db = new NepD1();
  const budget = new Budget(4);
  budget.reserve = 2;
  db.sqlite.prepare("INSERT INTO winkels (id, shop_id, shop_cipher) VALUES ('w1','x','y')").run();
  const o = new D1Opslag(db, "w1", budget);
  await o.leesStatus("s1");
  await o.leesBestelling("s1", "1");
  await o.schrijfBestelling("s1", "1", best(1));
  await assert.rejects(o.leesStatus("s2"), (e) => isBudgetOp(e));
  await o.schrijfStatus("s1", status("compleet"));
  await o.schrijfMarkering(5);
  assert.equal(await o.leesMarkering(), 5, "markering uit het geheugen, geen query");
  await assert.rejects(o.schrijfStatus("s1", status("geboekt")), (e) => isBudgetOp(e), "echt op");
});

test("(k) twee winkels in één database zien elkaars rijen niet", async () => {
  const db = new NepD1();
  const a = new D1Opslag(db, "w1", new Budget(50));
  const b = new D1Opslag(db, "w2", new Budget(50));
  await a.neemSlot("s1", "A", 2000, 1000);
  assert.equal(await b.neemSlot("s1", "B", 2000, 1000), true);
  await a.leesBestelling("s1", "1");
  await a.schrijfBestelling("s1", "1", best(1));
  await a.schrijfStatus("s1", status("onvolledig"));
  assert.equal(await b.leesStatus("s1"), undefined);
  assert.equal(await b.leesBestelling("s1", "1"), undefined);
  assert.deepEqual(await b.leesOpen(["onvolledig"]), []);
  assert.deepEqual(await a.leesOpen(["onvolledig"]), [{ statementId: "s1", statementTime: 1700000000 }]);
});

test("(i) af: bewaarde bestellingen en transacties weg, status blijft; wacht_op_abonnement houdt ze; te grote rij niet bewaard", async () => {
  const db = new NepD1();
  const o = new D1Opslag(db, "w1", new Budget(50));
  const n = (t: string) => Number((db.sqlite.prepare(`SELECT count(*) n FROM ${t}`).get() as any).n);
  await o.leesBestelling("s1", "1");
  await o.schrijfBestelling("s1", "1", best(1));
  await o.schrijfTransacties("s1", { kop: undefined, transacties: [], opgehaaldOp: 7 });
  await o.schrijfStatus("s1", status("wacht_op_abonnement"));
  assert.equal(n("bestellingen"), 1);
  await o.schrijfStatus("s1", status("geboekt", { opnieuwSinds: 9 }));
  assert.equal(n("bestellingen"), 1, "opnieuw boeken loopt nog: bewaren");
  await o.schrijfStatus("s1", status("geboekt"));
  assert.equal(n("bestellingen"), 0);
  assert.equal(n("transacties"), 0);
  assert.equal((await o.leesStatus("s1"))?.status, "geboekt");
  assert.equal(await o.leesBestelling("s1", "1"), undefined);
  const groot = { antwoord: { order_id: "9", x: "a".repeat(MAX_RIJ) } as any, opgehaaldOp: 1 };
  await o.leesBestelling("s2", "9");
  await o.schrijfBestelling("s2", "9", groot);
  assert.equal((await o.leesBestelling("s2", "9"))?.opgehaaldOp, 1, "wel in het geheugen van deze aanroep");
  await o.schrijfStatus("s2", status("onvolledig"));
  assert.equal(n("bestellingen"), 0, "te groot: niet bewaard, batch faalt niet");
});

test("markering op een winkel die niet bestaat geeft een fout", async () => {
  const o = new D1Opslag(new NepD1(), "w9", new Budget(50));
  await assert.rejects(o.schrijfMarkering(5), /bestaat niet/);
});

test("budget met reserve: overVoorNieuw laat de reserve buiten de boekingscontrole", () => {
  const b = new Budget(50);
  b.reserve = 6;
  assert.equal(b.over, 50);
  assert.equal(b.overVoorNieuw, 44);
});

test("leesOpen pakt ook opnieuw_sinds; (k) indexen worden gebruikt", async () => {
  const db = new NepD1();
  const o = new D1Opslag(db, "w1", new Budget(50));
  await o.schrijfStatus("s1", status("geboekt", { opnieuwSinds: 5 }));
  await o.schrijfStatus("s2", status("geboekt"));
  assert.deepEqual((await o.leesOpen(["onvolledig"])).map((x) => x.statementId), ["s1"]);
  const plan = JSON.stringify(db.sqlite.prepare("EXPLAIN QUERY PLAN SELECT statement_id, statement_time FROM statussen WHERE winkel = ? AND (status IN (?) OR opnieuw_sinds IS NOT NULL)").all("w1", "onvolledig"));
  assert.match(plan, /statussen_opnieuw|statussen_status/);
  assert.match(JSON.stringify(db.sqlite.prepare("EXPLAIN QUERY PLAN SELECT id FROM winkels WHERE volgende_run <= ?").all(5)), /winkels_volgende_run/);
});
