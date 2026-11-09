// Toetsen voor deel 2a van ontwerp-d1-worker.md: "boeking gestart" (punt 1, toets f), één pot van 50 met D1 (toets b)
// en de triggers voor ontkoppelen (punt 7, alleen de opslagkant).
import { test } from "node:test";
import assert from "node:assert/strict";
import { TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { MoneybirdClient } from "../src/moneybird/client.ts";
import { Budget, BudgetOp } from "../src/budget.ts";
import { GeheugenOpslag, isOntkoppeld, type Opslag } from "../src/opslag.ts";
import { D1Opslag } from "../src/d1/opslag.ts";
import { opnieuw, verwerkWinkel, type BoekDeps } from "../src/verwerk.ts";
import { NepD1 } from "./d1-nep.ts";
import { inst, koppeling, T0, wereld } from "./wereld.ts";

type Wereld = ReturnType<typeof wereld>;

/** Eén Budget(50) met reserve 6 voor fetch én D1, zoals in de consumer (ontwerp, "Eén pot van 50"). */
function aanroep(w: Wereld, db: NepD1, nu: number) {
  const budget = new Budget(50);
  budget.reserve = 6;
  let fetches = 0;
  const f = budget.omhul((async (i: any, init: any) => { fetches++; return w.fn(i, init); }) as typeof fetch);
  const opslag = new D1Opslag(db, "w1", budget.opslagTeller());
  const deps: BoekDeps = {
    tiktok: new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    moneybird: new MoneybirdClient({ accessToken: "m", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    accessToken: "t", shopCipher: "c", opslag, budget, nu: () => nu, eigenaar: `run-${nu}`,
  };
  return { deps, opslag, fetches: () => fetches };
}

function gewoon(w: Wereld, opslag: Opslag, nu: number, fetchFn = w.fn): BoekDeps {
  const budget = new Budget(45);
  const f = budget.omhul(fetchFn);
  return {
    tiktok: new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    moneybird: new MoneybirdClient({ accessToken: "m", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    accessToken: "t", shopCipher: "c", opslag, budget, nu: () => nu, eigenaar: `run-${nu}`,
  };
}

const posts = (w: Wereld) => w.urls.filter((u) => u.startsWith("POST MB")).length;
const opslagen: Array<[string, () => Opslag]> = [["geheugen", () => new GeheugenOpslag()], ["D1", () => new D1Opslag(new NepD1("w1"), "w1", new Budget(100_000))]];

test("(b) fetch en D1 samen nooit boven 50 per aanroep, ook met 6 afrekeningen van 30 bestellingen; alles geboekt, niets dubbel", async () => {
  const w = wereld();
  for (let i = 0; i < 6; i++) w.voegToe(String(7001 + i), T0 + (i + 1) * 86400, "PAID", Array.from({ length: 30 }, () => 10));
  const db = new NepD1("w1");
  let aanroepen = 0;
  for (; aanroepen < 20 && w.docs.size < 6; aanroepen++) {
    const a = aanroep(w, db, T0 + 10 * 86400 + aanroepen * 60);
    const q0 = db.queries;
    await verwerkWinkel(a.deps, inst());
    await a.opslag.klaar();
    const totaal = a.fetches() + db.queries - q0;
    assert.ok(totaal <= 50, `aanroep ${aanroepen}: ${a.fetches()} fetch + ${db.queries - q0} D1 = ${totaal}`);
  }
  assert.equal(w.docs.size, 6, `na ${aanroepen} aanroepen`);
  assert.equal(posts(w), 6);
  const orders = w.urls.filter((u) => u.includes("/orders/"));
  assert.equal(orders.length, 180);
  assert.equal(new Set(orders).size, 180, "geen bestelling twee keer opgehaald");
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM bestellingen").get() as any).n), 0, "na boeken weg");
});

test("(b) afrekening met 30 bestellingen kost hoogstens 8 D1-queries", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", Array.from({ length: 30 }, () => 10));
  const db = new NepD1("w1");
  const o = new D1Opslag(db, "w1", new Budget(100_000));
  const d = gewoon(w, o, T0 + 10 * 86400);
  (d as any).budget = new Budget(100);
  d.tiktok = new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: d.budget.omhul(w.fn), nu: d.nu, slaap: async () => {} });
  d.moneybird = new MoneybirdClient({ accessToken: "m", fetchFn: d.budget.omhul(w.fn), nu: d.nu, slaap: async () => {} });
  await verwerkWinkel(d, inst());
  assert.equal(w.docs.size, 1);
  // buiten de afrekening: markering lezen, open lijst lezen, markering schrijven
  assert.ok(db.queries - 3 <= 8, `queries voor de afrekening: ${db.queries - 3}`);
});

for (const [naam, maak] of opslagen) {
  test(`(f, ${naam}) afbraak tussen POST en status: onzeker "boeking gestart", 10 minuten geen POST, daarna ongewijzigd via kenmerk`, async () => {
    const w = wereld();
    w.voegToe("7001", T0 + 86400, "PAID", [10]);
    const o = maak();
    const nu = T0 + 10 * 86400;
    const echt = o.schrijfStatus.bind(o);
    o.schrijfStatus = async (id, s) => { if (s.status === "geboekt") throw new Error("aanroep afgebroken (CPU-grens)"); return echt(id, s); };
    await assert.rejects(verwerkWinkel(gewoon(w, o, nu), inst()), /afgebroken/);
    o.schrijfStatus = echt;
    assert.equal(posts(w), 1);
    const st = await o.leesStatus("7001");
    assert.equal(st?.status, "onzeker");
    assert.equal(st?.reden, "boeking gestart");
    await verwerkWinkel(gewoon(w, o, nu + 300), inst());
    assert.equal(posts(w), 1, "binnen 10 minuten geen tweede POST");
    await verwerkWinkel(gewoon(w, o, nu + 660), inst());
    assert.equal(posts(w), 1);
    const na = await o.leesStatus("7001");
    assert.equal(na?.status, "geboekt");
    assert.equal(na?.uitkomst, "ongewijzigd");
    assert.equal(na?.vorigeStatus, undefined);
    assert.equal(w.docs.size, 1);
  });

  test(`(${naam}) budget op in boekAfrekening: de oude status komt terug, geen onzeker`, async () => {
    const w = wereld();
    w.voegToe("7001", T0 + 86400, "PAID", [10]);
    const o = maak();
    const nu = T0 + 10 * 86400;
    const op = (async (i: any, init: any) => { if (String(i).includes("moneybird")) throw new BudgetOp(); return w.fn(i, init); }) as typeof fetch;
    const r = await verwerkWinkel(gewoon(w, o, nu, op), inst());
    assert.equal(r.budgetOp, true);
    assert.equal(await o.leesStatus("7001"), undefined, "er was geen status: weer geen status");
    await o.schrijfStatus("7001", { status: "onvolledig", reden: "x", sinds: nu, statementTime: T0 + 86400, pogingen: 1 });
    await verwerkWinkel(gewoon(w, o, nu + 1, op), inst());
    assert.deepEqual(await o.leesStatus("7001"), { status: "onvolledig", reden: "x", sinds: nu, statementTime: T0 + 86400, pogingen: 1 });
    await verwerkWinkel(gewoon(w, o, nu + 2), inst());
    assert.equal((await o.leesStatus("7001"))?.status, "geboekt");
  });

  test(`(${naam}) mislukte "opnieuw boeken" na een afbraak wordt weer geboekt met opnieuwFout, geen fout`, async () => {
    const w = wereld();
    w.voegToe("7001", T0 + 86400, "PAID", [10]);
    const o = maak();
    const nu = T0 + 10 * 86400;
    await verwerkWinkel(gewoon(w, o, nu), inst());
    const docId = (await o.leesStatus("7001"))?.documentId;
    await opnieuw(gewoon(w, o, nu + 100), "7001");
    // afbraak vlak na "boeking gestart", vóór Moneybird
    const start = o.startBoeking.bind(o);
    o.startBoeking = async (...a) => { await start(...a); throw new Error("aanroep afgebroken"); };
    // andere koppeling, anders is het "ongewijzigd" zonder boeking
    const ander = inst({ koppeling: { ...koppeling, per: { ...koppeling.per, omzet: { grootboekId: "299" } } } });
    await assert.rejects(verwerkWinkel(gewoon(w, o, nu + 200), ander), /afgebroken/);
    o.startBoeking = start;
    const tussen = await o.leesStatus("7001");
    assert.equal(tussen?.status, "onzeker");
    assert.equal(tussen?.vorigeStatus, "geboekt");
    assert.equal(tussen?.opnieuwSinds, nu + 100);
    w.mbStatus.volgende = 422;
    await verwerkWinkel(gewoon(w, o, nu + 900), ander);
    const na = await o.leesStatus("7001");
    assert.equal(na?.status, "geboekt");
    assert.match(String(na?.opnieuwFout), /geweigerd/);
    assert.equal(na?.documentId, docId);
    assert.equal(na?.vorigeStatus, undefined);
  });
}

test("(punt 7) trigger: na ontkoppeld_op faalt een batch met status of wachtrij en zet niets terug; neemSlot geeft geen slot", async () => {
  const db = new NepD1("w1");
  const n = (t: string) => Number((db.sqlite.prepare(`SELECT count(*) n FROM ${t}`).get() as any).n);
  const o = new D1Opslag(db, "w1", new Budget(50));
  assert.equal(await o.neemSlot("s1", "A", 2000, 1000), true);
  await o.leesBestelling("s1", "1");
  await o.schrijfBestelling("s1", "1", { antwoord: { order_id: "1" } as any, opgehaaldOp: 1 });
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 5 WHERE id = 'w1'").run();
  await assert.rejects(o.schrijfStatus("s1", { status: "onvolledig", sinds: 1 }), (e) => isOntkoppeld(e));
  assert.equal(n("bestellingen") + n("statussen"), 0);
  assert.equal(await o.slotTot("s1", "A"), null, "geen slot meer");
  await o.geefSlotTerug("s1", "A"); // nette stop: geen fout
  // een verse opslag, zonder slotrij voor s2: toch geen slot
  const vers = new D1Opslag(db, "w1", new Budget(50));
  assert.equal(await vers.neemSlot("s2", "B", 2000, 1000), false);
  assert.equal(await vers.slotTot("s1", "A"), null);
  await assert.rejects(vers.schrijfStatus("s2", { status: "geboekt", sinds: 1 }), (e) => isOntkoppeld(e));
  assert.throws(() => db.sqlite.prepare("INSERT INTO transacties VALUES ('w1','s3','{}',1)").run(), /ontkoppeld/);
  assert.throws(() => db.sqlite.prepare("INSERT INTO sloten VALUES ('w2','s3','x',1)").run(), /ontkoppeld/, "ook zonder rij in winkels");
  assert.equal(n("statussen") + n("sloten") + n("transacties"), 1, "alleen het slot van vóór het ontkoppelen");
});

test("(punt 7) ontkoppeld tijdens verwerkWinkel: nette stop, geen POST, geen fout of onzeker, niets van de afrekening in D1", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10, 20]);
  const db = new NepD1("w1");
  const fn = (async (i: any, init: any) => {
    if (String(i).includes("/orders/")) db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 1 WHERE id = 'w1'").run();
    return w.fn(i, init);
  }) as typeof fetch;
  const r = await verwerkWinkel(gewoon(w, new D1Opslag(db, "w1", new Budget(100_000)), T0 + 10 * 86400, fn), inst());
  assert.equal(r.winkel?.soort, "ontkoppeld");
  assert.equal(posts(w), 0);
  for (const t of ["statussen", "bestellingen", "transacties"]) assert.equal(Number((db.sqlite.prepare(`SELECT count(*) n FROM ${t}`).get() as any).n), 0, t);
});

test("(punt 7) al ontkoppeld vóór de run: nette stop met winkelfout ontkoppeld, geen gooi, geen POST", async () => {
  const w = wereld();
  w.voegToe("7002", T0 + 86400, "PAID", [10, 20]);
  const db = new NepD1("w1");
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 1 WHERE id = 'w1'").run();
  const r = await verwerkWinkel(gewoon(w, new D1Opslag(db, "w1", new Budget(100_000)), T0 + 10 * 86400, w.fn), inst());
  assert.equal(r.winkel?.soort, "ontkoppeld");
  assert.equal(posts(w), 0);
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM statussen").get() as any).n), 0);
});
