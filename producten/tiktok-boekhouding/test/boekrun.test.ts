import { test } from "node:test";
import assert from "node:assert/strict";
import { TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { MoneybirdClient } from "../src/moneybird/client.ts";
import { Budget } from "../src/budget.ts";
import type { GeheugenOpslag } from "../src/opslag.ts";
import { maakOpslag } from "./opslag-keuze.ts";
import { opnieuw, vervroegStartdatum, verwerkWinkel, type BoekDeps } from "../src/verwerk.ts";
import { inst, koppeling, T0, wereld } from "./wereld.ts";


function deps(w: ReturnType<typeof wereld>, opslag: GeheugenOpslag, nu = T0 + 10 * 86400, totaal = 45): BoekDeps & { opslag: GeheugenOpslag } {
  const budget = new Budget(totaal);
  const f = budget.omhul(w.fn);
  return {
    tiktok: new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    moneybird: new MoneybirdClient({ accessToken: "m", fetchFn: f, nu: () => nu, slaap: async () => {} }),
    accessToken: "t", shopCipher: "c", opslag, budget, nu: () => nu, eigenaar: `run-${nu}`,
  };
}
const status = async (o: GeheugenOpslag, id: string) => (await o.leesStatus(id))?.status;
const mbVerzoeken = (w: ReturnType<typeof wereld>) => w.urls.filter((u) => u.includes(" MB ")).length;

test("(b) voor de startdatum geen verzoek; PAID en SETTLED geboekt, PROCESSING, FAILED en onbekend niet; FAILED later PAID wordt geboekt", async () => {
  const w = wereld();
  w.voegToe("7000", T0 - 86400, "PAID", [10]);
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  w.voegToe("7002", T0 + 2 * 86400, "SETTLED", [20]);
  w.voegToe("7003", T0 + 3 * 86400, "PROCESSING", [30]);
  const mislukt = w.voegToe("7004", T0 + 4 * 86400, "FAILED", [40]);
  w.voegToe("7005", T0 + 5 * 86400, "RARE_STATUS", [50]);
  const o = maakOpslag();
  const r = await verwerkWinkel(deps(w, o), inst());
  assert.equal(r.winkel, undefined);
  assert.deepEqual(r.verwerkt.map((x) => x.status), ["geboekt", "geboekt", "wacht_op_uitbetaling", "uitbetaling_mislukt", "onbekende_uitbetaalstatus"]);
  assert.equal(w.urls.some((u) => u.includes("7000")), false);
  assert.equal(w.docs.size, 2);
  mislukt.status = "PAID";
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400), inst());
  assert.equal(await status(o, "7004"), "geboekt");
  assert.equal(w.docs.size, 3);
});

test("(c, j) boete als correctie, dezelfde bestelling in twee afrekeningen zonder verschil", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10, 20], [{ id: "p1", type: "PLATFORM_PENALTY", settlement_amount: "-5" }]);
  // terugbetaling van bestelling 5001 in een latere afrekening: zelfde order, nieuwe SKU-transactie
  const b = w.best.get("5001");
  b.sku_transactions.push({ ...b.sku_transactions[0], statement_id: "7002", settlement_amount: "-9.00", revenue_amount: "-10", revenue_breakdown: { subtotal_before_discount_amount: "-10" }, fee_tax_amount: "1", fee_tax_breakdown: { fee: { platform_commission_amount: "1" }, tax: {} } });
  w.afr.push({ id: "7002", time: T0 + 2 * 86400, status: "PAID", trans: [{ id: "x2", type: "ORDER", order_id: "5001", settlement_amount: "-9" }] });
  const o = maakOpslag();
  await verwerkWinkel(deps(w, o), inst());
  assert.equal(await status(o, "7001"), "geboekt");
  assert.equal(await status(o, "7002"), "geboekt");
  const docs = [...w.docs.values()];
  const tweede = docs.find((d) => d.reference === "TikTokShop-7002");
  assert.equal(tweede.general_journal_document_entries.some((e: any) => e.ledger_account_id === "204"), false);
  const eerste = docs.find((d) => d.reference === "TikTokShop-7001");
  assert.ok(eerste.general_journal_document_entries.some((e: any) => e.ledger_account_id === "203" && e.debit === "5.00"));
});

test("(d) aanpassing zonder enig bedrag: fout_gegevens, niet geboekt", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10], [{ id: "a1", type: "CHARGE_BACK", settlement_amount: "" }]);
  const o = maakOpslag();
  await verwerkWinkel(deps(w, o), inst());
  assert.equal(await status(o, "7001"), "fout_gegevens");
  assert.equal(w.docs.size, 0);
});

test("(d, f) zonder abonnement: 30 bestellingen per maand gratis (precies 30 wel), daarboven wacht_op_abonnement zonder Moneybird; na betalen geboekt", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", Array(20).fill(10));
  w.voegToe("7002", T0 + 2 * 86400, "PAID", Array(10).fill(10));
  w.voegToe("7003", T0 + 3 * 86400, "PAID", [10]);
  const o = maakOpslag();
  for (let i = 0; i < 8; i++) await verwerkWinkel(deps(w, o, T0 + 10 * 86400 + i * 1000), inst({ magBoeken: false }));
  assert.equal(await status(o, "7001"), "geboekt");
  assert.equal(await status(o, "7002"), "geboekt", "20 + 10 = 30: precies op de grens mag");
  assert.equal(await status(o, "7003"), "wacht_op_abonnement", "31e bestelling: afrekening in zijn geheel op wacht");
  assert.equal(w.docs.size, 2);
  const t = (o as any).telling as Map<string, { maand: string; bestellingen: number }>;
  assert.deepEqual([...t.keys()].sort(), ["7001", "7002"]);
  assert.equal(t.get("7001")!.maand, "2026-11");
  assert.equal(t.get("7001")!.bestellingen, 20);
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400), inst());
  assert.equal(await status(o, "7003"), "geboekt", "met abonnement geen grens");
  assert.equal(((o as any).telling as Map<string, unknown>).size, 3, "betaalde afrekening telt ook mee");
});

test("(e) telling: weg bij terug (Moneybird weigert de winkel), blijft bij geboekt en bij opnieuw boeken; onzeker gaat niet op wacht", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", Array(30).fill(10));
  w.voegToe("7002", T0 + 2 * 86400, "PAID", [10]);
  const o = maakOpslag();
  const telling = () => (o as any).telling as Map<string, unknown>;
  // Eerst ophalen (30 bestellingen kosten meer dan één aanroep), dan bij het boeken een 401 van Moneybird.
  for (let i = 0; i < 8 && mbVerzoeken(w) === 0; i++) {
    w.mbStatus.volgende = 401;
    await verwerkWinkel(deps(w, o, T0 + 10 * 86400 + i * 1000), inst({ magBoeken: false }));
  }
  assert.ok(mbVerzoeken(w) > 0, "boeken geprobeerd");
  assert.equal(await status(o, "7001"), "bezig_met_ophalen", "status van daarvoor (vorige run) terug");
  assert.equal(telling().size, 0, "terug: rij van deze poging weg");
  for (let i = 0; i < 6; i++) await verwerkWinkel(deps(w, o, T0 + 10 * 86400 + 5000 + i * 1000), inst({ magBoeken: false }));
  assert.equal(await status(o, "7001"), "geboekt");
  assert.equal(await status(o, "7002"), "wacht_op_abonnement", "maand vol");
  assert.ok(telling().has("7001"), "geboekt: rij blijft");
  // Opnieuw boeken van een geboekte afrekening in een volle maand: vrijgesteld, nooit op wacht, rij blijft.
  await opnieuw({ opslag: o, nu: () => T0 + 12 * 86400 }, "7001");
  for (let i = 0; i < 6; i++) await verwerkWinkel(deps(w, o, T0 + 12 * 86400 + 10 + i * 1000), inst({ magBoeken: false }));
  assert.ok(["geboekt", "geboekt_met_waarschuwing"].includes(String(await status(o, "7001"))));
  assert.ok(telling().has("7001"));
  assert.equal(telling().size, 1, "nooit dubbel");
});

for (const [http, soort] of [[401, "koppeling_verlopen"], [402, "geen_abonnement"], [403, "geblokkeerd"]] as const) {
  test(`(g) Moneybird ${http}: winkel stil, run stopt, volgende run boekt de rest zonder gat`, async () => {
    const w = wereld();
    w.voegToe("7001", T0 + 86400, "PAID", [10]);
    w.voegToe("7002", T0 + 2 * 86400, "PAID", [20]);
    const o = maakOpslag();
    w.mbStatus.volgende = http;
    const r = await verwerkWinkel(deps(w, o), inst());
    assert.equal(r.winkel?.soort, soort);
    assert.equal(await status(o, "7002"), undefined);
    assert.equal(w.docs.size, 0);
    const r2 = await verwerkWinkel(deps(w, o, T0 + 11 * 86400), inst());
    assert.equal(r2.winkel, undefined);
    assert.equal(await status(o, "7001"), "geboekt");
    assert.equal(await status(o, "7002"), "geboekt");
    assert.equal(w.docs.size, 2);
  });
}

test("(h) tweede run: geboekt geeft geen verzoek, ook niet na een andere koppeling; opnieuw boeken geeft ongewijzigd of vervangen", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  const o = maakOpslag();
  await verwerkWinkel(deps(w, o), inst());
  const voor = w.urls.length;
  const ander = { ...koppeling, per: { ...koppeling.per, omzet: { grootboekId: "299" } } };
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400), inst({ koppeling: ander }));
  assert.equal(w.urls.slice(voor).filter((u) => u.includes("7001") || u.includes(" MB ")).length, 0);
  // knop zonder wijziging: ongewijzigd zonder Moneybird
  await opnieuw(deps(w, o, T0 + 12 * 86400), "7001");
  const mb = mbVerzoeken(w);
  await verwerkWinkel(deps(w, o, T0 + 12 * 86400 + 5), inst());
  assert.equal((await o.leesStatus("7001"))?.uitkomst, "ongewijzigd");
  assert.equal(mbVerzoeken(w), mb);
  // knop na een andere koppeling: vervangen, zelfde document
  await opnieuw(deps(w, o, T0 + 13 * 86400), "7001");
  await verwerkWinkel(deps(w, o, T0 + 13 * 86400 + 5), inst({ koppeling: ander }));
  const st = await o.leesStatus("7001");
  assert.equal(st?.uitkomst, "vervangen");
  assert.equal(st?.opnieuwSinds, undefined);
  assert.equal(w.docs.size, 1);
  assert.ok([...w.docs.values()][0].general_journal_document_entries.some((e: any) => e.ledger_account_id === "299"));
});

test("(i) slot bezet: niets gedaan en niets geschreven; onzeker van 5 minuten overgeslagen, van 11 minuten opnieuw", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  const o = maakOpslag();
  const nu = T0 + 10 * 86400;
  await o.neemSlot("7001", "ander", nu + 300, nu);
  await verwerkWinkel(deps(w, o, nu), inst());
  assert.equal(await status(o, "7001"), undefined);
  assert.equal(w.urls.filter((u) => u.includes("7001")).length, 0);
  assert.equal(o.statussen.size + o.bestellingen.size + o.transacties.size, 0); // niets over deze afrekening geschreven
  assert.equal(o.markering, T0 + 86400); // markering blijft op deze afrekening
  await o.geefSlotTerug("7001", "ander");
  await o.schrijfStatus("7001", { status: "onzeker", sinds: nu, statementTime: T0 + 86400 });
  await verwerkWinkel(deps(w, o, nu + 300), inst());
  assert.equal(await status(o, "7001"), "onzeker");
  assert.equal(mbVerzoeken(w), 0);
  await verwerkWinkel(deps(w, o, nu + 660), inst());
  assert.equal(await status(o, "7001"), "geboekt");
  assert.equal(w.docs.size, 1);
});

test("(e, j) 90 bestellingen boeken over vier aanroepen; opnieuw boeken houdt geboekt tot het af is", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", Array.from({ length: 90 }, () => 10));
  const o = maakOpslag();
  const st: string[] = [];
  // per aanroep: lijst 1, transacties 1 (alleen de eerste keer), dan bestellingen tot er 14 over zijn: 29, 30, 30, 1
  for (let i = 0; i < 4; i++) { await verwerkWinkel(deps(w, o, T0 + 10 * 86400 + i), inst()); st.push(String(await status(o, "7001"))); }
  assert.deepEqual(st, ["bezig_met_ophalen", "bezig_met_ophalen", "bezig_met_ophalen", "geboekt"]);
  assert.equal(new Set(w.urls.filter((u) => u.includes("/orders/"))).size, 90);
  assert.equal(w.docs.size, 1);
  await opnieuw(deps(w, o, T0 + 11 * 86400), "7001");
  const st2: string[] = [];
  for (let i = 1; i <= 4; i++) { await verwerkWinkel(deps(w, o, T0 + 11 * 86400 + i), inst()); st2.push(String(await status(o, "7001"))); }
  assert.deepEqual(st2, ["geboekt", "geboekt", "geboekt", "geboekt"]);
  assert.equal(w.docs.size, 1);
  assert.equal((await o.leesStatus("7001"))?.uitkomst, "ongewijzigd");
  assert.equal(w.urls.filter((u) => u.includes("/orders/")).length, 180);
});

test("(j) tijdelijke fout: onvolledig, na 5 runs fout; markering blijft staan tot dan", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  w.tiktokFout.set("5001", 36009003);
  const o = maakOpslag();
  const st: string[] = [];
  for (let i = 0; i < 5; i++) { await verwerkWinkel(deps(w, o, T0 + 10 * 86400 + i * 600), inst()); st.push(String(await status(o, "7001"))); }
  assert.deepEqual(st, ["onvolledig", "onvolledig", "onvolledig", "onvolledig", "fout"]);
  assert.match((await o.leesStatus("7001"))!.reden!, /na 5 pogingen/);
  assert.ok(o.markering! > T0 + 86400);
});

test("TikTok-token verlopen: winkel stil, niets geschreven over de afrekening", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  w.tiktokFout.set("5001", 105002);
  const o = maakOpslag();
  const r = await verwerkWinkel(deps(w, o), inst());
  assert.equal(r.winkel?.soort, "token_verlopen");
  assert.equal(await status(o, "7001"), undefined);
});

test("afgesloten periode: fout met melding, run gaat door met de volgende", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  w.voegToe("7002", T0 + 40 * 86400, "PAID", [10]);
  const o = maakOpslag();
  await verwerkWinkel(deps(w, o, T0 + 50 * 86400), inst({ administratie: { id: "1", periodLockedUntil: "2026-11-20" } }));
  assert.equal(await status(o, "7001"), "fout");
  assert.match((await o.leesStatus("7001"))!.reden!, /periode_afgesloten/);
  assert.equal(await status(o, "7002"), "geboekt");
});

test("eerst FAILED, later PAID met een tijdelijke fout: blijft terugkomen tot fout of geboekt (markering voorbij)", async () => {
  const w = wereld();
  const a = w.voegToe("7001", T0 + 86400, "FAILED", [10]);
  w.voegToe("7002", T0 + 2 * 86400, "PAID", [20]);
  const o = maakOpslag();
  await verwerkWinkel(deps(w, o), inst());
  assert.ok(o.markering! > T0 + 2 * 86400);
  a.status = "PAID";
  w.tiktokFout.set("5001", 36009003);
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400), inst());
  assert.equal(await status(o, "7001"), "onvolledig");
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400 + 600), inst());
  assert.equal((await o.leesStatus("7001"))?.pogingen, 2);
  w.tiktokFout.clear();
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400 + 1200), inst());
  assert.equal(await status(o, "7001"), "geboekt");
  assert.equal(w.docs.size, 2);
});

test("onzeker: de knop weigert, en ook met een opnieuw-markering wacht de run 10 minuten", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  const o = maakOpslag();
  const nu = T0 + 10 * 86400;
  await o.schrijfStatus("7001", { status: "onzeker", sinds: nu, statementTime: T0 + 86400 });
  await assert.rejects(() => opnieuw(deps(w, o, nu + 10), "7001"), /gecontroleerd/);
  await o.schrijfStatus("7001", { status: "onzeker", sinds: nu, statementTime: T0 + 86400, opnieuwSinds: nu + 10 });
  await verwerkWinkel(deps(w, o, nu + 20), inst());
  assert.equal(mbVerzoeken(w), 0);
  assert.equal(await status(o, "7001"), "onzeker");
});

test("knop terwijl een run de afrekening vasthoudt: geweigerd, niets geschreven", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  const o = maakOpslag();
  await verwerkWinkel(deps(w, o), inst());
  const nu = T0 + 11 * 86400;
  await o.neemSlot("7001", "run-x", nu + 300, nu);
  await assert.rejects(() => opnieuw(deps(w, o, nu), "7001"), /wordt nu verwerkt/);
  assert.equal((await o.leesStatus("7001"))?.opnieuwSinds, undefined);
});

test("startdatum vervroegen: eerdere afrekeningen worden alsnog geboekt", async () => {
  const w = wereld();
  w.voegToe("7000", T0 - 86400, "PAID", [10]);
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  const o = maakOpslag();
  await verwerkWinkel(deps(w, o), inst());
  assert.equal(w.docs.size, 1);
  await vervroegStartdatum(o, T0 - 2 * 86400);
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400), inst({ startdatum: T0 - 2 * 86400 }));
  assert.equal(await status(o, "7000"), "geboekt");
  assert.equal(await status(o, "7001"), "geboekt");
  assert.equal(w.docs.size, 2);
});

test("geen rekening gekozen: winkelfout instellingen, geen fout per afrekening; daarna boekt alles vanzelf", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  w.voegToe("7002", T0 + 2 * 86400, "PAID", [10]);
  const o = maakOpslag();
  const zonder = { ...koppeling, per: { omzet: { grootboekId: "201" } } };
  const r = await verwerkWinkel(deps(w, o), inst({ koppeling: zonder }));
  assert.equal(r.winkel?.soort, "instelling");
  assert.notEqual(await status(o, "7001"), "fout");
  await verwerkWinkel(deps(w, o, T0 + 11 * 86400), inst());
  assert.equal(await status(o, "7001"), "geboekt");
  assert.equal(await status(o, "7002"), "geboekt");
});

test("twee runs om elkaar heen: B boekt tussen de lezing en het slot van A, A doet daarna geen Moneybird-verzoek", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", [10]);
  const o = maakOpslag();
  const nu = T0 + 10 * 86400;
  // A leest (nog niets) en wacht; B verwerkt alles zodra A om het slot vraagt.
  const echtNeem = o.neemSlot.bind(o);
  let eerst = true;
  let naB = -1;
  o.neemSlot = async (id, eig, tot, n) => {
    if (eerst && eig === "run-A") { eerst = false; await verwerkWinkel({ ...deps(w, o, nu), eigenaar: "run-B" }, inst()); naB = mbVerzoeken(w); }
    return echtNeem(id, eig, tot, n);
  };
  await verwerkWinkel({ ...deps(w, o, nu), eigenaar: "run-A" }, inst());
  assert.ok(naB > 0);
  assert.equal(mbVerzoeken(w), naB); // A doet niets meer bij Moneybird (de echte Moneybird cachet zoeken)
  assert.equal(w.urls.filter((u) => u.startsWith("POST MB")).length, 1);
  assert.equal(w.docs.size, 1);
  assert.equal(await status(o, "7001"), "geboekt");
});

test("(e) opnieuw boeken van een geboekte afrekening zonder rij in een volle maand: vrijgesteld; bij terug blijft de nieuwe rij (vorige status geboekt)", async () => {
  const w = wereld();
  w.voegToe("7001", T0 + 86400, "PAID", Array(30).fill(10));
  w.voegToe("7002", T0 + 2 * 86400, "PAID", [10]);
  const o = maakOpslag();
  const telling = () => (o as any).telling as Map<string, unknown>;
  for (let i = 0; i < 8; i++) await verwerkWinkel(deps(w, o, T0 + 10 * 86400 + i * 1000), inst());
  assert.equal(await status(o, "7002"), "geboekt");
  // Geboekt vóór deel 2: geen rij in telling.
  const sqlite = (o as any).db?.sqlite;
  if (sqlite) sqlite.prepare("DELETE FROM telling WHERE statement_id = '7002'").run();
  else telling().delete("7002");
  assert.equal(telling().has("7002"), false);
  // Opnieuw boeken met een andere tegenrekening (dus echt opnieuw), zonder abonnement, en Moneybird weigert de winkel.
  await opnieuw({ opslag: o, nu: () => T0 + 12 * 86400 }, "7002");
  const anders = inst({ magBoeken: false, koppeling: { ...koppeling, tegenrekeningId: "501" } });
  for (let i = 0; i < 4 && telling().has("7002") === false; i++) {
    w.mbStatus.volgende = 401;
    await verwerkWinkel(deps(w, o, T0 + 12 * 86400 + 10 + i * 1000), anders);
  }
  assert.equal(await status(o, "7002"), "geboekt", "nooit op wacht door de grens");
  assert.ok(telling().has("7002"), "rij ingevoegd en bij terug blijven staan (vorige status was geboekt)");
});
