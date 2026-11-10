// Toets (i), deel cron, uit ontwerp-betalen.md, punt 7: de taak `opzeggen` uitvoeren met zegOp (deel 3).
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { Budget } from "../src/budget.ts";
import { ontkoppel } from "../src/d1/ontkoppel.ts";
import { OPZEGGEN_PER_AANROEP, OPZEGGEN_WACHT, ruimOntkoppeldOp } from "../src/d1/opruimen.ts";
import { DAG, NU, deps, nepRevoke, rij, taken, vulWinkel } from "./ontkoppel-hulp.ts";

const INST = { api: "https://sandbox-api.polar.sh", token: "oat_x", productId: "p", webhookSecret: "whsec_x" };
const lijst = (items: unknown[]) => ({ items, pagination: { total_count: items.length, max_page: 1 } });

/** Nagebootste Polar: GET de lijst, PATCH opzeggen, met een vaste status per soort. */
function nepPolar(o: { lijst?: number; patch?: number; items?: unknown[] } = {}) {
  const verzoeken: Array<{ methode: string; pad: string }> = [];
  const fn = (async (input: any, init: any = {}) => {
    const u = new URL(String(input));
    const methode = init.method ?? "GET";
    verzoeken.push({ methode, pad: u.pathname + u.search });
    if (methode === "GET") return new Response(JSON.stringify(lijst(o.items ?? [{ id: "sub-1", metadata: {}, cancel_at_period_end: false }])), { status: o.lijst ?? 200 });
    return new Response(JSON.stringify({ id: "sub-1" }), { status: o.patch ?? 200 });
  }) as typeof fetch;
  return { fn, verzoeken };
}

async function ontkoppeldBetaald(db: NepD1, w: string) {
  await vulWinkel(db, w, { mb: false, betaald: true, polar: `cus-${w}` });
  await ontkoppel(db, w, "knop", NU, new Budget(50), deps(nepRevoke().fn).d);
  assert.ok(taken(db, w).opzeggen, "taak opzeggen staat klaar");
}

test("(i) cron: opzeggen lukt: taak weg, polar_klant leeg, kale rij mag daarna weg", async () => {
  const db = new NepD1();
  await ontkoppeldBetaald(db, "w1");
  const p = nepPolar();
  const d = deps(p.fn);
  const u = await ruimOntkoppeldOp(db, NU + 60, new Budget(50), { ...d.d, polar: INST });
  assert.equal(u.opgezegd, 1);
  assert.deepEqual(p.verzoeken.map((v) => v.methode), ["GET", "PATCH"]);
  assert.ok(p.verzoeken[0].pad.includes("external_customer_id=w1"));
  const r = rij(db, "w1");
  assert.ok(!r || (r.polar_klant === null && taken(db, "w1").opzeggen === undefined), "taak en klant weg (of de kale rij is al weg)");
  assert.equal(d.alarmen().length, 0);
});

test("(i) cron: 5xx is later: pogingen +1, fout bewaard, ALARM; binnen het uur geen nieuwe poging", async () => {
  const db = new NepD1();
  await ontkoppeldBetaald(db, "w1");
  const p = nepPolar({ patch: 503 });
  const d = deps(p.fn);
  await ruimOntkoppeldOp(db, NU + 60, new Budget(50), { ...d.d, polar: INST });
  const t = taken(db, "w1").opzeggen;
  assert.equal(t.pogingen, 1);
  assert.equal(t.laatste_poging, NU + 60);
  assert.match(t.laatste_fout, /503/);
  assert.ok(rij(db, "w1")!.polar_klant, "klant blijft tot het lukt");
  const n = p.verzoeken.length;
  await ruimOntkoppeldOp(db, NU + 60 + OPZEGGEN_WACHT - 1, new Budget(50), { ...d.d, polar: INST });
  assert.equal(p.verzoeken.length, n, "binnen het uur niet opnieuw");
  // Volgende dag lukt het wel.
  const ok = nepPolar();
  const u = await ruimOntkoppeldOp(db, NU + DAG, new Budget(50), { ...deps(ok.fn).d, polar: INST });
  assert.equal(u.opgezegd, 1);
});

test("(i) cron: 403 AlreadyCanceled en 404 tellen als gelukt; al opgezegd abonnement krijgt geen PATCH", async () => {
  for (const [naam, o] of [
    ["403 AlreadyCanceled", { patch: 403 }],
    ["lijst 404", { lijst: 404 }],
    ["al opgezegd", { items: [{ id: "sub-1", metadata: {}, cancel_at_period_end: true }] }],
  ] as const) {
    const db = new NepD1();
    await ontkoppeldBetaald(db, "w1");
    const p = nepPolar(o);
    // 403 moet de code AlreadyCanceledSubscription dragen: nagebootst via een eigen fetch.
    const fn = naam.startsWith("403")
      ? ((async (i: any, init: any = {}) => ((init.method ?? "GET") === "PATCH" ? new Response(JSON.stringify({ error: "AlreadyCanceledSubscription" }), { status: 403 }) : p.fn(i, init))) as typeof fetch)
      : p.fn;
    const u = await ruimOntkoppeldOp(db, NU + 60, new Budget(50), { ...deps(fn).d, polar: INST });
    assert.equal(u.opgezegd, 1, naam);
    if (naam === "al opgezegd") assert.deepEqual(p.verzoeken.map((v) => v.methode), ["GET"]);
  }
});

test("(i) cron: zonder Polar-instellingen geen verzoek, taak blijft (ALARM na dag 23); hoogstens 3 winkels per aanroep", async () => {
  const db = new NepD1();
  await ontkoppeldBetaald(db, "w1");
  const p = nepPolar();
  await ruimOntkoppeldOp(db, NU + 60, new Budget(50), deps(p.fn).d);
  assert.equal(p.verzoeken.length, 0);
  assert.ok(taken(db, "w1").opzeggen);

  const db2 = new NepD1();
  for (const w of ["a", "b", "c", "d", "e"]) await ontkoppeldBetaald(db2, w);
  const p2 = nepPolar();
  const u = await ruimOntkoppeldOp(db2, NU + 60, new Budget(50), { ...deps(p2.fn).d, polar: INST });
  assert.equal(u.opgezegd, OPZEGGEN_PER_AANROEP);
});

test("(i, l) cron: budget op tijdens opzeggen schrijft niets voor die winkel (uitgesteld) en gaat de volgende keer verder", async () => {
  const db = new NepD1();
  await ontkoppeldBetaald(db, "w1");
  const p = nepPolar();
  const u = await ruimOntkoppeldOp(db, NU + 60, new Budget(3), { ...deps(p.fn).d, polar: INST });
  assert.equal(u.budgetOp, true);
  assert.equal(taken(db, "w1").opzeggen.pogingen, 0, "uitgesteld telt niet als poging");
});
