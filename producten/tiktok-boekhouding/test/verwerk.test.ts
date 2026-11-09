import { test } from "node:test";
import assert from "node:assert/strict";
import { TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { MoneybirdClient } from "../src/moneybird/client.ts";
import { Budget, BudgetOp } from "../src/budget.ts";
import { GeheugenOpslag } from "../src/opslag.ts";
import { haalSamen, proef, WinkelStop, type TikTokDeps } from "../src/verwerk.ts";

// Nagebootste TikTok: afrekeningen met transacties en bestellingen, antwoorden in de vorm van de docs ({code, data, request_id}).
interface NepAfrekening { id: string; time: number; status: string; trans: any[]; kop?: any }
function nepTikTok(lijst: NepAfrekening[], bestellingen: Map<string, any>, fouten: Map<string, { code: number; http?: number }> = new Map()) {
  const urls: string[] = [];
  const ok = (data: any) => new Response(JSON.stringify({ code: 0, message: "Success", request_id: "r", data }), { status: 200 });
  const fn = (async (input: any) => {
    const u = new URL(String(input));
    urls.push(u.pathname);
    let m;
    if (u.pathname === "/finance/202309/statements") {
      return ok({ statements: lijst.map((a) => ({ id: a.id, statement_time: a.time, payment_status: a.status, currency: "EUR", settlement_amount: "0", fee_amount: "0", adjustment_amount: "0" })) });
    }
    if ((m = /^\/finance\/202501\/statements\/(\d+)\/statement_transactions$/.exec(u.pathname))) {
      const a = lijst.find((x) => x.id === m![1])!;
      const tot = a.trans.reduce((s, t) => s + Math.round(Number(t.settlement_amount) * 100), 0) / 100;
      return ok({ id: a.id, create_time: a.time, status: "SETTLED", currency: "EUR", payable_amount: String(tot), total_settlement_amount: String(tot), total_count: a.trans.length, ...a.kop, transactions: a.trans });
    }
    if ((m = /^\/finance\/202501\/orders\/(\d+)\/statement_transactions$/.exec(u.pathname))) {
      const f = fouten.get(m[1]);
      if (f) return new Response(JSON.stringify({ code: f.code, message: "fout", request_id: "r" }), { status: f.http ?? 200 });
      return ok(bestellingen.get(m[1]));
    }
    if (u.hostname.includes("moneybird")) return new Response("[]", { status: 200 });
    throw new Error(`onverwacht: ${u.pathname}`);
  }) as typeof fetch;
  return { fn, urls };
}

const bestelling = (orderId: string, statementId: string, omzet: number): any => {
  const comm = -Math.round(omzet * 10) / 100;
  const som = (omzet + comm).toFixed(2);
  return {
    order_id: orderId, currency: "EUR", settlement_amount: som,
    sku_transactions: [{ sku_id: "1", statement_id: statementId, settlement_amount: som, revenue_amount: String(omzet), revenue_breakdown: { subtotal_before_discount_amount: String(omzet) },
      shipping_cost_amount: "0", shipping_cost_breakdown: {}, fee_tax_amount: String(comm), fee_tax_breakdown: { fee: { platform_commission_amount: String(comm) }, tax: {} } }],
  };
};
const orderT = (id: string, orderId: string, b: any): any => ({ id, type: "ORDER", order_id: orderId, settlement_amount: b.settlement_amount });

function deps(fetchFn: typeof fetch, opslag = new GeheugenOpslag(), totaal = 45, nu = 1_800_000_000): TikTokDeps & { opslag: GeheugenOpslag } {
  const budget = new Budget(totaal);
  const tiktok = new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: budget.omhul(fetchFn), nu: () => nu, slaap: async () => {} });
  return { tiktok, accessToken: "t", shopCipher: "c", opslag, budget, nu: () => nu };
}

/** Afrekening met n bestellingen van elk 10 euro omzet. */
function maak(id: string, time: number, status: string, n: number, bestellingen: Map<string, any>, start = 1): NepAfrekening {
  const trans = [];
  for (let i = start; i < start + n; i++) {
    const oid = String(5000 + i);
    const b = bestelling(oid, id, 10);
    bestellingen.set(oid, b);
    trans.push(orderT(`${id}${i}`, oid, b));
  }
  return { id, time, status, trans };
}

test("budget: telt elk verzoek en gooit BudgetOp vóór het verzoek vertrekt", async () => {
  const b = new Budget(2);
  let verstuurd = 0;
  const f = b.omhul((async () => { verstuurd++; return new Response("{}"); }) as typeof fetch);
  await f("https://x");
  await f("https://x");
  await assert.rejects(() => f("https://x"), BudgetOp);
  assert.equal(verstuurd, 2);
  assert.equal(b.over, 0);
});

test("budget op bij een herhaling (na 429): BudgetOp blijft, geen server en geen onzeker", async () => {
  const te429 = (async () => new Response(JSON.stringify({ code: 36009002, message: "te veel", request_id: "r" }), { status: 429 })) as typeof fetch;
  const b1 = new Budget(1);
  const tt = new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: b1.omhul(te429), slaap: async () => {} });
  await assert.rejects(() => tt.roep({ method: "GET", path: "/x" }), BudgetOp);
  const b2 = new Budget(1);
  const mb = new MoneybirdClient({ accessToken: "t", fetchFn: b2.omhul((async () => new Response("{}", { status: 429 })) as typeof fetch), nu: () => 1, slaap: async () => {} });
  await assert.rejects(() => mb.roep("POST", "/1/documents/general_journal_documents", { body: {} }), BudgetOp);
});

test("afrekening die met een vol budget niet past: onvolledig in plaats van eindeloos bezig", async () => {
  const best = new Map();
  const a = maak("7001", 300, "PAID", 1, best);
  const altijdOp = (async () => { throw new BudgetOp(); }) as typeof fetch;
  const s = await haalSamen(deps(altijdOp), "7001", { reserve: 12 });
  assert.equal(s.status, "onvolledig");
  assert.match(s.reden!, /te groot/);
});

test("boeken: compleet maar te weinig budget voor de boeking geeft bezig, de volgende aanroep compleet zonder nieuw ophalen", async () => {
  const best = new Map();
  const a = maak("7001", 300, "PAID", 2, best);
  const nep = nepTikTok([a], best);
  const opslag = new GeheugenOpslag();
  const d = deps(nep.fn, opslag, 17); // 1 + 2 = 3 verzoeken, dan 14 over: genoeg om op te halen, de boeking past nog
  assert.equal((await haalSamen(d, "7001", { reserve: 12 })).status, "compleet");
  const krap = deps(nep.fn, opslag, 11);
  assert.equal((await haalSamen(krap, "7001", { reserve: 12 })).status, "bezig_met_ophalen");
  assert.equal(krap.budget.over, 11);
});

test("budget op in de clients: geen netwerkfout, geen herhaling, geen onzeker", async () => {
  const b = new Budget(0);
  const tt = new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: b.omhul(fetch), slaap: async () => {} });
  await assert.rejects(() => tt.roep({ method: "GET", path: "/x" }), BudgetOp);
  const mb = new MoneybirdClient({ accessToken: "t", fetchFn: b.omhul(fetch), slaap: async () => {} });
  await assert.rejects(() => mb.roep("POST", "/1/documents/general_journal_documents", { body: {} }), BudgetOp);
});

test("(a) proef zonder koppeling: drie afrekeningen als regels per soort, nul verzoeken naar Moneybird", async () => {
  const best = new Map();
  const lijst = [maak("7001", 300, "PAID", 2, best, 1), maak("7002", 200, "SETTLED", 1, best, 3), maak("7003", 150, "PROCESSING", 1, best, 4), maak("7004", 100, "PAID", 1, best, 5), maak("7005", 50, "PAID", 1, best, 6)];
  const nep = nepTikTok(lijst, best);
  const d = deps(nep.fn);
  const p = await proef(d);
  assert.equal(p.nogBezig, false);
  assert.deepEqual(p.afrekeningen.map((a) => a.statementId), ["7001", "7002", "7004"]);
  assert.ok(p.afrekeningen.every((a) => a.status === "compleet" && a.waarschuwingen.length === 0));
  assert.deepEqual(p.afrekeningen[0].perSoort, { omzet: 2000, commissie: -200 });
  assert.equal(p.afrekeningen[0].uitbetaaldCenten, 1800);
  assert.equal(nep.urls.some((u) => u.includes("moneybird")), false);
});

test("(a) proef met een klein budget: nog bezig, de volgende aanroep gaat verder zonder dubbel ophalen", async () => {
  const best = new Map();
  const lijst = [maak("7001", 300, "PAID", 3, best, 1), maak("7002", 200, "PAID", 3, best, 4), maak("7003", 100, "PAID", 3, best, 7)];
  const nep = nepTikTok(lijst, best);
  const opslag = new GeheugenOpslag();
  const p1 = await proef(deps(nep.fn, opslag, 7)); // lijst 1, 7001 4, 7002 1 + 1
  assert.equal(p1.nogBezig, true);
  assert.equal(p1.afrekeningen[0].status, "compleet");
  const p2 = await proef(deps(nep.fn, opslag));
  assert.equal(p2.nogBezig, false);
  assert.ok(p2.afrekeningen.every((a) => a.status === "compleet"));
  assert.equal(new Set(nep.urls.filter((u) => u.includes("/orders/"))).size, nep.urls.filter((u) => u.includes("/orders/")).length);
});

test("(a) proef: minder dan drie uitbetaald, dan ook PROCESSING met label", async () => {
  const best = new Map();
  const lijst = [maak("7001", 300, "PROCESSING", 1, best, 1), maak("7002", 200, "PAID", 1, best, 2), maak("7003", 100, "FAILED", 1, best, 3)];
  const p = await proef(deps(nepTikTok(lijst, best).fn));
  assert.deepEqual(p.afrekeningen.map((a) => [a.statementId, a.label]), [["7002", undefined], ["7001", "nog niet uitbetaald"]]);
});

test("(e) 90 bestellingen over drie aanroepen: geen bestelling twee keer opgehaald, pas samengesteld als alles er is", async () => {
  const best = new Map();
  const a = maak("7001", 300, "PAID", 90, best);
  const nep = nepTikTok([a], best);
  const opslag = new GeheugenOpslag();
  const uitkomsten = [];
  for (let i = 0; i < 3; i++) uitkomsten.push(await haalSamen(deps(nep.fn, opslag), "7001", { reserve: 12 }));
  assert.deepEqual(uitkomsten.map((u) => u.status), ["bezig_met_ophalen", "bezig_met_ophalen", "compleet"]);
  const orders = nep.urls.filter((u) => u.includes("/orders/"));
  assert.equal(orders.length, 90);
  assert.equal(new Set(orders).size, 90);
  assert.equal(uitkomsten[2].regels.reduce((s, r) => s + r.bedragCenten, 0), 90 * 900);
  // reserve plus 2 herhalingen gerespecteerd: eerste aanroep 45 - 1 (transacties) - 14 = 30 bestellingen,
  // tweede 45 - 14 = 31 (transacties bewaard, dus geen pagina's opnieuw), derde de rest
  assert.equal(uitkomsten[0].ontbrekend.length, 60);
  assert.equal(uitkomsten[1].ontbrekend.length, 29);
  assert.equal(nep.urls.filter((u) => u.includes("/statements/")).length, 1);
});

test("(e) budget loopt over meer afrekeningen in één aanroep; budget op midden in een afrekening verliest niets", async () => {
  const best = new Map();
  const lijst = [maak("7001", 300, "PAID", 3, best, 1), maak("7002", 200, "PAID", 3, best, 4)];
  const nep = nepTikTok(lijst, best);
  const opslag = new GeheugenOpslag();
  const d = deps(nep.fn, opslag, 6);
  assert.equal((await haalSamen(d, "7001", { reserve: 0 })).status, "compleet"); // 4 verzoeken
  const tweede = await haalSamen(d, "7002", { reserve: 0 }); // 1 transacties + 1 bestelling, dan op
  assert.equal(tweede.status, "bezig_met_ophalen");
  assert.equal(d.budget.over, 0);
  const leeg = await haalSamen(d, "7002", { reserve: 0 });
  assert.equal(leeg.status, "bezig_met_ophalen");
  const d2 = deps(nep.fn, opslag, 6);
  assert.equal((await haalSamen(d2, "7002", { reserve: 0 })).status, "compleet");
  assert.equal(nep.urls.filter((u) => u.includes("/orders/")).length, 6);
});

test("(e) mislukte bestelling midden in een portie: onvolledig, de volgende run haalt alleen die opnieuw", async () => {
  const best = new Map();
  const a = maak("7001", 300, "PAID", 3, best);
  const fouten = new Map([["5002", { code: 36009003 }]]);
  const nep = nepTikTok([a], best, fouten);
  const opslag = new GeheugenOpslag();
  const u1 = await haalSamen(deps(nep.fn, opslag), "7001", { reserve: 0 });
  assert.equal(u1.status, "onvolledig");
  assert.match(u1.reden!, /5002 \(TikTok fout 36009003\)/);
  assert.deepEqual(u1.ontbrekend, ["5002"]);
  fouten.clear();
  const voor = nep.urls.length;
  const u2 = await haalSamen(deps(nep.fn, opslag), "7001", { reserve: 0 });
  assert.equal(u2.status, "compleet");
  assert.deepEqual(nep.urls.slice(voor).filter((u) => u.includes("/orders/")), ["/finance/202501/orders/5002/statement_transactions"]);
});

test("winkelfouten zetten de winkel stil: verlopen token en geen toegang", async () => {
  const best = new Map();
  const a = maak("7001", 300, "PAID", 1, best);
  for (const [code, soort] of [[105002, "token_verlopen"], [105005, "geen_toegang"]] as const) {
    const nep = nepTikTok([a], best, new Map([["5001", { code }]]));
    await assert.rejects(() => haalSamen(deps(nep.fn), "7001", { reserve: 0 }), (e: any) => e instanceof WinkelStop && e.soort === soort);
  }
});

test("bewaarde bestelling van een andere afrekening telt niet; 'opnieuw sinds T' haalt opnieuw op", async () => {
  const best = new Map();
  const a = maak("7001", 300, "PAID", 1, best);
  const nep = nepTikTok([a], best);
  const opslag = new GeheugenOpslag();
  // oud antwoord: alleen een SKU-transactie van een eerdere afrekening
  await opslag.schrijfBestelling("7001", "5001", { antwoord: bestelling("5001", "6999", 10), opgehaaldOp: 1 });
  assert.equal((await haalSamen(deps(nep.fn, opslag, 45, 100), "7001", { reserve: 0 })).status, "compleet");
  assert.equal(nep.urls.filter((u) => u.includes("/orders/")).length, 1);
  // nogmaals zonder sinds: uit de opslag; met sinds na het ophalen: opnieuw
  await haalSamen(deps(nep.fn, opslag, 45, 200), "7001", { reserve: 0 });
  assert.equal(nep.urls.filter((u) => u.includes("/orders/")).length, 1);
  await haalSamen(deps(nep.fn, opslag, 45, 300), "7001", { reserve: 0, sinds: 150 });
  assert.equal(nep.urls.filter((u) => u.includes("/orders/")).length, 2);
});

test("aantal ongelijk aan total_count: onvolledig, geen bestelling nodig om dat te weten", async () => {
  const best = new Map();
  const a = maak("7001", 300, "PAID", 2, best);
  a.kop = { total_count: 3 };
  const s = await haalSamen(deps(nepTikTok([a], best).fn), "7001", { reserve: 0 });
  assert.equal(s.status, "onvolledig");
  assert.match(s.reden!, /3 transacties/);
});
