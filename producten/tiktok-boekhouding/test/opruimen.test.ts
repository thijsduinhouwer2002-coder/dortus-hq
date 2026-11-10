// Toetsen (n, deel cron) en het cron-deel van (o) uit ontwerp-d1-worker.md, punt 7: opruimen na ontkoppelen.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { Budget } from "../src/budget.ts";
import { ontkoppel } from "../src/d1/ontkoppel.ts";
import { ruimOntkoppeldOp } from "../src/d1/opruimen.ts";
import { winkelfoutStatement } from "../src/d1/winkels.ts";
import { DAG, NU, deps, nepRevoke, rij, taken, tel, vulWinkel } from "./ontkoppel-hulp.ts";

/** Ontkoppelde winkel waarvan intrekken met 500 mislukte. */
async function metOpenIntrekken(db: NepD1, w: string) {
  await vulWinkel(db, w, { polar: `polar-${w}` });
  await ontkoppel(db, w, "knop", NU, new Budget(50), deps(nepRevoke(500).fn).d);
}
const betaalstukKlaar = (db: NepD1, w: string) => db.sqlite.prepare("UPDATE winkels SET taken = json_remove(taken, '$.opzeggen'), polar_klant = NULL WHERE id = ?").run(w);
const betaalstukMislukt = (db: NepD1, w: string, op: number) =>
  db.sqlite.prepare("UPDATE winkels SET taken = json_set(taken, '$.opzeggen.pogingen', 1, '$.opzeggen.laatste_poging', ?, '$.opzeggen.laatste_fout', 'Polar 500') WHERE id = ?").run(op, w);

test("(n) cron: 5xx laat de taak staan en de cron probeert opnieuw; 200 maakt het token leeg", async () => {
  const db = new NepD1();
  await metOpenIntrekken(db, "w1");
  const eerst = deps(nepRevoke(503).fn);
  await ruimOntkoppeldOp(db, NU + 3600, new Budget(50), eerst.d);
  assert.equal(taken(db, "w1").intrekken.pogingen, 2);
  assert.equal(taken(db, "w1").intrekken.eerste_poging, NU, "eerste poging blijft");
  assert.ok(rij(db, "w1")!.mb_tokens);
  const revoke = nepRevoke(200);
  const u = await ruimOntkoppeldOp(db, NU + 7200, new Budget(50), deps(revoke.fn).d);
  assert.equal(u.ingetrokken, 1);
  assert.equal(revoke.verzoeken[0].body.token, "GEHEIM-r-w1");
  assert.equal(rij(db, "w1")!.mb_tokens, null);
  assert.equal(taken(db, "w1").intrekken, undefined);
  assert.ok(taken(db, "w1").opzeggen, "opzeggen staat nog klaar: rij blijft");
});

test("(n) cron: na 7 dagen sinds de eerste poging toch leeg plus ALARM, zonder nog een verzoek", async () => {
  const db = new NepD1();
  await metOpenIntrekken(db, "w1");
  const vlak = nepRevoke(500);
  await ruimOntkoppeldOp(db, NU + 7 * DAG - 1, new Budget(50), deps(vlak.fn).d);
  assert.equal(vlak.verzoeken.length, 1, "net onder 7 dagen nog geprobeerd");
  const revoke = nepRevoke(500);
  const { d, alarmen } = deps(revoke.fn);
  await ruimOntkoppeldOp(db, NU + 7 * DAG, new Budget(50), d);
  assert.equal(revoke.verzoeken.length, 0);
  assert.equal(alarmen().length, 1);
  assert.match(alarmen()[0], /7 dagen/);
  assert.equal(rij(db, "w1")!.mb_tokens, null);
  assert.equal(taken(db, "w1").intrekken, undefined);
});

test("(n) cron: 403 niet herhalen; hoogstens 5 intrekpogingen per aanroep, binnen het budget", async () => {
  const db = new NepD1();
  for (let i = 1; i <= 7; i++) await metOpenIntrekken(db, `w${i}`);
  const revoke = nepRevoke(403);
  const { d, alarmen } = deps(revoke.fn);
  const budget = new Budget(50);
  const q0 = db.queries;
  await ruimOntkoppeldOp(db, NU + 60, budget, d);
  assert.equal(revoke.verzoeken.length, 5);
  assert.equal(alarmen().length, 5);
  assert.equal(db.queries - q0, 2, "één leesbatch, één schrijfbatch");
  assert.equal(budget.over, 50 - 7);
  await ruimOntkoppeldOp(db, NU + 120, new Budget(50), d);
  assert.equal(revoke.verzoeken.length, 7, "alleen de twee die nog over waren");
  await ruimOntkoppeldOp(db, NU + 180, new Budget(50), d);
  assert.equal(revoke.verzoeken.length, 7, "403 wordt niet herhaald");
});

test("(o) cron: kale rij weg zodra beide taken klaar zijn", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1", { polar: "polar-1" });
  await vulWinkel(db, "w2");
  await ontkoppel(db, "w1", "knop", NU, new Budget(50), deps(nepRevoke(200).fn).d);
  const { d } = deps(nepRevoke().fn);
  await ruimOntkoppeldOp(db, NU + 60, new Budget(50), d);
  assert.ok(rij(db, "w1"), "opzeggen staat nog open");
  betaalstukKlaar(db, "w1");
  await ruimOntkoppeldOp(db, NU + 120, new Budget(50), d);
  assert.equal(rij(db, "w1"), undefined);
  assert.ok(rij(db, "w2"), "gekoppelde winkel blijft");
  assert.equal(tel(db, "statussen", "w2"), 2);
});

test("(o) cron: uiterlijk dag 23 weg als alleen intrekken nog openstaat; daarvoor niet", async () => {
  const db = new NepD1();
  await metOpenIntrekken(db, "w1");
  betaalstukKlaar(db, "w1");
  // intrekken blijft hangen (bijvoorbeeld de 7-dagenregel nog niet gedraaid): taak handmatig vers houden
  db.sqlite.prepare("UPDATE winkels SET taken = json_set(taken, '$.intrekken.eerste_poging', ?) WHERE id = 'w1'").run(NU + 22 * DAG);
  const { d } = deps(nepRevoke(500).fn);
  await ruimOntkoppeldOp(db, NU + 23 * DAG - 1, new Budget(50), d);
  assert.ok(rij(db, "w1"));
  await ruimOntkoppeldOp(db, NU + 23 * DAG, new Budget(50), d);
  assert.equal(rij(db, "w1"), undefined);
});

test("(o) cron: mislukte opzegging blijft staan na dag 23, met elke dag één ALARM", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1", { polar: "polar-1" });
  await ontkoppel(db, "w1", "knop", NU, new Budget(50), deps(nepRevoke(200).fn).d);
  betaalstukMislukt(db, "w1", NU + DAG);
  const { d, alarmen } = deps(nepRevoke().fn);
  await ruimOntkoppeldOp(db, NU + DAG + 60, new Budget(50), d);
  assert.equal(alarmen().length, 1, "meteen bij de mislukte poging");
  assert.match(alarmen()[0], /Polar/);
  await ruimOntkoppeldOp(db, NU + DAG + 900, new Budget(50), d);
  assert.equal(alarmen().length, 1, "niet elke cron, één keer per dag");
  for (let dag = 2; dag <= 30; dag++) await ruimOntkoppeldOp(db, NU + dag * DAG + 60, new Budget(50), d);
  assert.equal(alarmen().length, 30);
  const r = rij(db, "w1")!;
  assert.ok(r, "ook na dag 23 blijft de rij");
  assert.equal(r.polar_klant, "polar-1");
  betaalstukKlaar(db, "w1");
  await ruimOntkoppeldOp(db, NU + 31 * DAG, new Budget(50), d);
  assert.equal(rij(db, "w1"), undefined);
});

test("(o) cron: met polar_klant en opzegging nooit geprobeerd: rij blijft na dag 23 met ALARM per dag", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1", { polar: "polar-1" });
  await ontkoppel(db, "w1", "knop", NU, new Budget(50), deps(nepRevoke(200).fn).d);
  const { d, alarmen } = deps(nepRevoke().fn);
  await ruimOntkoppeldOp(db, NU + 22 * DAG, new Budget(50), d);
  assert.equal(alarmen().length, 0, "vóór dag 23 nog geen alarm");
  await ruimOntkoppeldOp(db, NU + 23 * DAG, new Budget(50), d);
  assert.equal(alarmen().length, 1);
  assert.match(alarmen()[0], /23 dagen/);
  assert.ok(rij(db, "w1"));
  await ruimOntkoppeldOp(db, NU + 30 * DAG, new Budget(50), d);
  assert.equal(alarmen().length, 2);
  assert.equal(rij(db, "w1")!.polar_klant, "polar-1");
});

test("(o) cron: zonder polar_klant geen taak opzeggen; rij weg op dag 23 (of zodra intrekken klaar is)", async () => {
  const db = new NepD1();
  await vulWinkel(db, "w1");
  await ontkoppel(db, "w1", "knop", NU, new Budget(50), deps(nepRevoke(500).fn).d);
  assert.deepEqual(Object.keys(taken(db, "w1")).sort(), ["intrekken", "reden"], "geen opzeggen");
  db.sqlite.prepare("UPDATE winkels SET taken = json_set(taken, '$.intrekken.eerste_poging', ?) WHERE id = 'w1'").run(NU + 22 * DAG);
  const { d, alarmen } = deps(nepRevoke(500).fn);
  await ruimOntkoppeldOp(db, NU + 23 * DAG - 1, new Budget(50), d);
  assert.ok(rij(db, "w1"));
  await ruimOntkoppeldOp(db, NU + 23 * DAG, new Budget(50), d);
  assert.equal(rij(db, "w1"), undefined);
  assert.deepEqual(alarmen(), []);

  await vulWinkel(db, "w2");
  await ontkoppel(db, "w2", "knop", NU, new Budget(50), deps(nepRevoke(200).fn).d);
  assert.deepEqual(taken(db, "w2"), { reden: "knop" });
  await ruimOntkoppeldOp(db, NU + 60, new Budget(50), d);
  assert.equal(rij(db, "w2"), undefined, "intrekken klaar en niets op te zeggen: meteen weg");
});

test("(o) cron: budget op bij de schrijfbatch of vooraf geeft budgetOp, geen fout", async () => {
  const db = new NepD1();
  await metOpenIntrekken(db, "w1");
  const revoke = nepRevoke(200);
  const { d } = deps(revoke.fn);
  assert.equal((await ruimOntkoppeldOp(db, NU + 60, new Budget(0), d)).budgetOp, true);
  const u = await ruimOntkoppeldOp(db, NU + 60, new Budget(2), d); // leesbatch en één fetch, dan is de pot leeg
  assert.equal(u.budgetOp, true);
  assert.equal(revoke.verzoeken.length, 1);
  assert.ok(taken(db, "w1").intrekken, "niets geschreven: taak staat er nog, de volgende cron herhaalt (200)");
  const plan = JSON.stringify(db.sqlite.prepare("EXPLAIN QUERY PLAN SELECT id FROM winkels WHERE ontkoppeld_op IS NULL AND winkelfout_sinds <= ?").all(5));
  assert.match(plan, /winkels_winkelfout_sinds/);
});

test("(o) cron: vangnet wist rijen die toch bleven staan, hoogstens 20 winkels per aanroep", async () => {
  const db = new NepD1();
  for (let i = 1; i <= 22; i++) {
    const w = `w${i}`;
    await vulWinkel(db, w, { mb: false });
    // Nagebootst: ontkoppeld_op gezet zonder te wissen, alsof de rijen er toch nog staan.
    db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = ?, taken = '{\"opzeggen\":{\"voor\":1,\"pogingen\":0}}' WHERE id = ?").run(NU, w);
  }
  await vulWinkel(db, "levend");
  const { d } = deps(nepRevoke().fn);
  await ruimOntkoppeldOp(db, NU + 60, new Budget(50), d);
  const over = (t: string) => Number((db.sqlite.prepare(`SELECT count(DISTINCT winkel) n FROM ${t} WHERE winkel <> 'levend'`).get() as any).n);
  for (const t of ["statussen", "transacties", "bestellingen", "sloten"]) assert.equal(over(t), 2, t);
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM winkels WHERE shop_id IS NOT NULL AND id <> 'levend'").get() as any).n), 2);
  await ruimOntkoppeldOp(db, NU + 120, new Budget(50), d);
  for (const t of ["statussen", "transacties", "bestellingen", "sloten"]) assert.equal(over(t), 0, t);
  assert.equal(rij(db, "w1")!.shop_id, null);
  assert.equal(rij(db, "w1")!.instellingen, null);
  assert.equal(tel(db, "statussen", "levend"), 2, "gekoppelde winkel ongemoeid");
  assert.equal(rij(db, "levend")!.shop_id, "shop-levend");
});

test("(o) cron: 21 dagen koppeling_verlopen aan de kant van TikTok wordt ontkoppelen; onder de 21 niet", async () => {
  const db = new NepD1();
  for (const w of ["tt", "kort", "mb", "hersteld"]) await vulWinkel(db, w);
  const zet = async (w: string, kant: "tiktok" | "moneybird", nu: number) => db.batch([winkelfoutStatement(db, w, { soort: "koppeling_verlopen", bericht: "x", kant }, nu)]);
  await zet("tt", "tiktok", NU);
  await zet("tt", "tiktok", NU + 10 * DAG); // zelfde fout opnieuw: sinds blijft
  assert.equal(rij(db, "tt")!.winkelfout_sinds, NU);
  await zet("kort", "tiktok", NU + 1);
  await zet("mb", "moneybird", NU);
  await zet("hersteld", "tiktok", NU);
  await db.batch([winkelfoutStatement(db, "hersteld", null, NU + 5 * DAG)]); // run lukte weer
  await zet("hersteld", "tiktok", NU + 6 * DAG);
  assert.equal(rij(db, "hersteld")!.winkelfout_sinds, NU + 6 * DAG, "onderbroken: telt opnieuw");

  const revoke = nepRevoke(200);
  const { d } = deps(revoke.fn);
  const u = await ruimOntkoppeldOp(db, NU + 21 * DAG, new Budget(50), d);
  assert.equal(u.ontkoppeld, 1);
  assert.equal(rij(db, "tt")!.ontkoppeld_op, NU + 21 * DAG);
  assert.equal(taken(db, "tt").reden, "koppeling_verlopen_21_dagen");
  assert.equal(tel(db, "statussen", "tt"), 0);
  assert.equal(revoke.verzoeken.length, 1, "Moneybird-toegang ook ingetrokken");
  for (const w of ["kort", "mb", "hersteld"]) assert.equal(rij(db, w)!.ontkoppeld_op, null, w);
  await ruimOntkoppeldOp(db, NU + 21 * DAG + 1, new Budget(50), d);
  assert.equal(rij(db, "kort")!.ontkoppeld_op, NU + 21 * DAG + 1);
});
