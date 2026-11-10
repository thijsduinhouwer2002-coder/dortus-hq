// Toets (d), deel maand en n, uit ontwerp-betalen.md, punt 7.
import { test } from "node:test";
import assert from "node:assert/strict";
import { maandVan, telBestellingen } from "../src/telling.ts";

const utc = (s: string) => Date.parse(s) / 1000;

test("(d) maand in Europe/Amsterdam: 31 dec 23:30 UTC telt als januari, 30 nov 22:59 UTC nog november", () => {
  assert.equal(maandVan(utc("2026-12-31T23:30:00Z")), "2027-01");
  assert.equal(maandVan(utc("2026-12-31T22:59:59Z")), "2026-12");
  assert.equal(maandVan(utc("2026-11-30T22:59:59Z")), "2026-11");
  assert.equal(maandVan(utc("2026-11-30T23:00:00Z")), "2026-12");
  // Zomertijd: 31 mei 22:00 UTC is 1 juni 00:00 in Amsterdam.
  assert.equal(maandVan(utc("2026-05-31T22:00:00Z")), "2026-06");
  assert.equal(maandVan(utc("2026-05-31T21:59:59Z")), "2026-05");
});

test("(d) n: unieke order_id van ORDER-transacties; andere typen en ORDER zonder order_id tellen niet", () => {
  const t = (type: string, order_id?: string) => ({ id: `${type}-${order_id}`, type, order_id }) as any;
  assert.equal(telBestellingen([t("ORDER", "1"), t("ORDER", "1"), t("ORDER", "2"), t("SHIPPING_FEE", "3"), t("ORDER"), t("RESERVE")]), 2);
  assert.equal(telBestellingen([]), 0, "afrekening zonder bestellingen telt 0");
  assert.equal(telBestellingen([t("ADJUSTMENT")]), 0);
});

// --- (d) en (e) op de opslag zelf: grens in de SQL, slot, terug in één schrijfactie ----------------------------------
import { GeheugenOpslag, type Opslag } from "../src/opslag.ts";
import { D1Opslag } from "../src/d1/opslag.ts";
import { Budget } from "../src/budget.ts";
import { NepD1 } from "./d1-nep.ts";
import { D1ToetsOpslag } from "./d1-toets-opslag.ts";

const NU = 1_800_000_000;
const t = (bestellingen: number, extra: Partial<{ maand: string; vrij: boolean }> = {}) => ({ maand: "2026-11", bestellingen, vrij: false, grens: 30, minTot: NU, ...extra });

for (const [naam, maak] of [["geheugen", () => new GeheugenOpslag()], ["D1", () => new D1ToetsOpslag()]] as Array<[string, () => Opslag]>) {
  test(`(d) grens in de opslag (${naam}): 30 precies wel, 31 niet, 0 altijd, andere maand los, vrij zonder grens, eigen rij telt niet dubbel`, async () => {
    const o = maak();
    const leg = async (id: string, n: number, extra = {}) => {
      await o.neemSlot(id, "run", NU + 300, NU);
      return o.legTellingVast(id, "run", t(n, extra));
    };
    assert.deepEqual(await leg("a", 20), { rij: true, ingevoegd: true, slot: true });
    assert.deepEqual(await leg("b", 11), { rij: false, ingevoegd: false, slot: true }, "20 + 11 = 31");
    assert.deepEqual(await leg("b", 10), { rij: true, ingevoegd: true, slot: true }, "20 + 10 = 30");
    assert.deepEqual(await leg("c", 0), { rij: true, ingevoegd: true, slot: true }, "zonder bestellingen altijd");
    assert.deepEqual(await leg("d", 1), { rij: false, ingevoegd: false, slot: true });
    assert.deepEqual(await leg("e", 5, { maand: "2026-12" }), { rij: true, ingevoegd: true, slot: true }, "andere maand");
    assert.deepEqual(await leg("f", 99, { vrij: true }), { rij: true, ingevoegd: true, slot: true }, "abonnement of vrijstelling");
    assert.deepEqual(await leg("a", 20), { rij: true, ingevoegd: false, slot: true }, "rij van een eerdere poging: wel rij, niet ingevoegd");
    // De maand staat nu op 20 + 10 + 99 = 129 (door de vrijstelling): zonder bestellingen mag nog steeds, één niet.
    assert.deepEqual(await leg("g", 0), { rij: true, ingevoegd: true, slot: true }, "0 bestellingen ook boven 30");
    assert.deepEqual(await leg("h", 1), { rij: false, ingevoegd: false, slot: true });
  });

  test(`(e) wisTelling alleen met eigen slot; schrijfStatus met wis haalt de rij in dezelfde schrijfactie weg (${naam})`, async () => {
    const o = maak();
    const heeft = (id: string) => ((o as any).telling as Map<string, unknown>).has(id);
    await o.neemSlot("p", "run", NU + 300, NU);
    await o.legTellingVast("p", "run", t(4));
    await o.neemSlot("p", "ander", NU + 900, NU + 400); // ons slot verlopen, een ander nam het
    await o.wisTelling("p", "run");
    assert.equal(heeft("p"), true, "slot van een ander: rij blijft (die aanroep kan erop boeken)");
    await o.wisTelling("p", "ander");
    assert.equal(heeft("p"), false);
    await o.neemSlot("q", "run", NU + 300, NU);
    await o.legTellingVast("q", "run", t(4));
    await o.schrijfStatus("q", { status: "fout", sinds: NU });
    assert.equal(heeft("q"), true, "zonder wis blijft hij");
    await o.schrijfStatus("q", { status: "fout", sinds: NU }, true);
    assert.equal(heeft("q"), false);
    assert.equal((await o.leesStatus("q"))?.status, "fout");
  });

  test(`(d, e) slot vereist en zetTerug (${naam}): zonder geldig slot geen rij; terug zet status en wist de rij samen`, async () => {
    const o = maak();
    assert.deepEqual(await o.legTellingVast("x", "run", t(1)), { rij: false, ingevoegd: false, slot: false });
    await o.neemSlot("x", "ander", NU + 300, NU);
    assert.deepEqual(await o.legTellingVast("x", "run", t(1)), { rij: false, ingevoegd: false, slot: false }, "slot van een ander");
    await o.neemSlot("y", "run", NU + 300, NU);
    await o.legTellingVast("y", "run", t(3));
    await o.schrijfStatus("y", { status: "onzeker", sinds: NU });
    await o.zetTerug("y", { status: "wacht_op_uitbetaling", sinds: 1 }, false);
    assert.equal((await o.leesStatus("y"))?.status, "wacht_op_uitbetaling");
    assert.equal(((o as any).telling as Map<string, unknown>).has("y"), true, "zonder wis blijft de rij");
    await o.zetTerug("y", undefined, true);
    assert.equal(await o.leesStatus("y"), undefined);
    assert.equal(((o as any).telling as Map<string, unknown>).has("y"), false);
  });
}

test("(d) twee aanroepen tegelijk komen samen niet boven 30 (D1, grens in de SQL)", async () => {
  const db = new NepD1("w1");
  const a = new D1Opslag(db as any, "w1", new Budget(100));
  const b = new D1Opslag(db as any, "w1", new Budget(100));
  await a.neemSlot("s1", "A", NU + 300, NU);
  await b.neemSlot("s2", "B", NU + 300, NU);
  const [ra, rb] = await Promise.all([a.legTellingVast("s1", "A", t(20)), b.legTellingVast("s2", "B", t(20))]);
  assert.equal(Number(ra.ingevoegd) + Number(rb.ingevoegd), 1);
  const som = Number((db.sqlite.prepare("SELECT SUM(bestellingen) s FROM telling WHERE winkel = 'w1'").get() as any).s);
  assert.equal(som, 20);
});

test("(e) zetTerug in D1 is één batch (status en telling samen)", async () => {
  const db = new NepD1("w1");
  const o = new D1Opslag(db as any, "w1", new Budget(100));
  await o.neemSlot("s1", "A", NU + 300, NU);
  await o.legTellingVast("s1", "A", t(2));
  await o.schrijfStatus("s1", { status: "onzeker", sinds: NU });
  const q0 = db.queries;
  db.faalBijStatement = 1; // de DELETE uit telling faalt: dan mag ook de status niet weg zijn
  await assert.rejects(o.zetTerug("s1", undefined, true));
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM statussen WHERE statement_id = 's1'").get() as any).n), 1, "alles of niets");
  await o.zetTerug("s1", undefined, true);
  assert.equal(Number((db.sqlite.prepare("SELECT count(*) n FROM telling").get() as any).n), 0);
  assert.equal(db.queries - q0, 2, "elke poging één batch");
});
