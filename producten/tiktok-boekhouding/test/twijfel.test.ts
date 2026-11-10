// Toets (h) en (l) uit ontwerp-betalen.md, punt 7: twijfel aan de stand van het abonnement (punt 2, stap 5).
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { nepFetch, type NepAntwoord } from "./hulp.ts";
import { Budget } from "../src/budget.ts";
import { abonnementVoorRun, heeftTwijfel, TWIJFEL_NA } from "../src/polar/twijfel.ts";

const NU = 1_800_000_000;
const MICRO = 1_000_000;
const INST = { api: "https://sandbox-api.polar.sh", token: "oat_x", productId: "p", webhookSecret: "whsec_x" };
const iso = (s: number) => new Date(s * 1000).toISOString();
const kolom = (a: Record<string, unknown>) => JSON.stringify(a);
const actiefState = (tot: number) => ({ id: "cus-1", external_id: "w1", deleted_at: null, active_subscriptions: [{ id: "sub-1", metadata: { winkel: "w1" }, current_period_end: iso(tot), cancel_at_period_end: false }] });

function opzet(antwoorden: NepAntwoord[], k: string | null, opties: { wachtRecent?: boolean; budget?: Budget; polar?: typeof INST | undefined } = {}) {
  const db = new NepD1("w1");
  db.sqlite.prepare("UPDATE winkels SET abonnement = ? WHERE id = 'w1'").run(k);
  const nep = nepFetch(antwoorden);
  const log: string[] = [];
  const budget = opties.budget ?? new Budget(50);
  const teller = budget.opslagTeller();
  const run = () => abonnementVoorRun({
    db: db as any, winkel: "w1", kolom: k, wachtRecent: opties.wachtRecent ?? false, nu: NU,
    polar: "polar" in opties ? opties.polar : INST, budget, fetchFn: nep.fn, slaap: async () => {}, neem: () => teller.neem(), log: (r) => log.push(r),
  });
  const abonnement = () => JSON.parse((db.sqlite.prepare("SELECT abonnement FROM winkels WHERE id = 'w1'").get() as any).abonnement ?? "null");
  return { db, run, verzoeken: nep.verzoeken, log, budget, abonnement };
}

test("(h) wanneer twijfel: verlenging gemist, stand oud bij actief, stand oud terwijl er een recente afrekening wacht", () => {
  const vers = NU * MICRO, oud = (NU - TWIJFEL_NA - 1) * MICRO;
  assert.equal(heeftTwijfel(kolom({ actief: true, tot: NU + 100, stand: vers }), false, NU), false);
  assert.equal(heeftTwijfel(kolom({ actief: true, tot: NU - 1, stand: vers }), false, NU), true, "tot voorbij");
  assert.equal(heeftTwijfel(kolom({ actief: true, tot: NU + 100, stand: oud }), false, NU), true, "gemiste intrekking");
  assert.equal(heeftTwijfel(kolom({ actief: false, stand: oud }), false, NU), false, "niets wacht: geen reden");
  assert.equal(heeftTwijfel(kolom({ actief: false, stand: oud }), true, NU), true);
  assert.equal(heeftTwijfel(null, true, NU), true, "nooit opgevraagd en er wacht iets");
  assert.equal(heeftTwijfel(kolom({ actief: false, stand: vers }), true, NU), false, "net opgevraagd: niet elke run opnieuw");
});

test("(h, l) twijfel: één opvraging uit de pot, stand geschreven, actief als Polar het zegt", async () => {
  const o = opzet([{ json: actiefState(NU + 30 * 86400) }], kolom({ actief: true, tot: NU - 10, stand: 5 }));
  const over = o.budget.overVoorNieuw;
  assert.equal(await o.run(), true);
  assert.equal(o.verzoeken.length, 1);
  assert.equal(o.verzoeken[0].url.pathname, "/v1/customers/external/w1/state");
  assert.equal(o.budget.overVoorNieuw, over - 2, "1 verzoek naar Polar plus 1 D1-query, uit dezelfde pot");
  const a = o.abonnement();
  assert.deepEqual([a.actief, a.tot, a.stand], [true, NU + 30 * 86400, NU * MICRO]);
});

test("(h) geen twijfel: geen verzoek, de kolom beslist", async () => {
  const o = opzet([{ json: {} }], kolom({ actief: true, tot: NU + 100, stand: NU * MICRO }));
  assert.equal(await o.run(), true);
  assert.equal(o.verzoeken.length, 0);
});

test("(h) Polar weg (5xx, 429, netwerk) of niet ingesteld: alleen gratis boeken, geen winkelfout, wel een logregel; 401 met ALARM", async () => {
  for (const [naam, antwoord, alarm] of [
    ["500", { status: 500, json: {} }, false],
    ["429 lang", { status: 429, json: {}, headers: { "retry-after": "60" } }, false],
    ["netwerk", { fout: new TypeError("fetch failed") }, false],
    ["401", { status: 401, json: { error: "invalid_token" } }, true],
  ] as Array<[string, NepAntwoord, boolean]>) {
    const k = kolom({ actief: true, tot: NU + 100, stand: 1 });
    const o = opzet([antwoord], k);
    assert.equal(await o.run(), false, naam);
    assert.equal(o.log.length, 1, naam);
    assert.equal(o.log[0].startsWith("ALARM"), alarm, naam);
    assert.equal(JSON.stringify(o.abonnement()), JSON.stringify(JSON.parse(k)), `${naam}: niets geschreven`);
  }
  const zonder = opzet([{ json: {} }], kolom({ actief: true, tot: NU - 1, stand: 1 }), { polar: undefined });
  assert.equal(await zonder.run(), false);
  assert.equal(zonder.verzoeken.length, 0);
  assert.ok(zonder.log[0].startsWith("ALARM"));
});

test("(h) opvraging schrijft niet over een nieuwere stand (bijv. een webhook die net binnenkwam)", async () => {
  const nieuwer = (NU + 50) * MICRO;
  const o = opzet([{ status: 404, json: { error: "ResourceNotFound" } }], kolom({ actief: true, tot: NU - 1, stand: 1 }));
  o.db.sqlite.prepare("UPDATE winkels SET abonnement = ? WHERE id = 'w1'").run(kolom({ actief: true, tot: NU + 999, stand: nieuwer }));
  assert.equal(await o.run(), false, "Polar zegt geen klant; de uitkomst van deze aanroep volgt de opvraging");
  assert.deepEqual([o.abonnement().actief, o.abonnement().stand], [true, nieuwer], "D1 houdt de nieuwere stand");
});
