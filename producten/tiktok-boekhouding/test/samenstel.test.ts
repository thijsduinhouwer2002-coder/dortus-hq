import { test } from "node:test";
import assert from "node:assert/strict";
import { stelSamen, bestellingenVan, bruikbaar } from "../src/samenstel.ts";

const S = "7300000000000000001";
const kop = (n: number, extra: any = {}): any => ({ id: S, create_time: 1794312000, status: "SETTLED", currency: "EUR", payable_amount: "", total_settlement_amount: "", total_count: n, ...extra });
const orderT = (id: string, orderId: string, settlement: string, extra: any = {}): any => ({ id, type: "ORDER", order_id: orderId, settlement_amount: settlement, ...extra });
/** Sluitende bestelling: omzet, verzending en commissie per SKU, voor één afrekening. */
const bestelling = (orderId: string, omzet: string, verz: string, comm: string, statementId = S): any => {
  const som = (Number(omzet) + Number(verz) + Number(comm)).toFixed(2);
  return {
    order_id: orderId, currency: "EUR", settlement_amount: som,
    sku_transactions: [{ sku_id: "1", statement_id: statementId, settlement_amount: som, revenue_amount: omzet, revenue_breakdown: { subtotal_before_discount_amount: omzet },
      shipping_cost_amount: verz, shipping_cost_breakdown: { actual_shipping_fee_amount: verz }, fee_tax_amount: comm, fee_tax_breakdown: { fee: { platform_commission_amount: comm }, tax: {} } }],
  };
};
const som = (s: any) => s.regels.reduce((a: number, r: any) => a + r.bedragCenten, 0);

test("(c) twee bestellingen en een boete: rekenkern-regels plus één correctie, som sluit, geen waarschuwing", () => {
  const tr = [orderT("1", "A", "18.5"), orderT("2", "B", "7"), { id: "3", type: "PLATFORM_PENALTY", settlement_amount: "-5" }];
  const best = new Map([["A", bestelling("A", "25", "-4", "-2.5")], ["B", bestelling("B", "10", "-2", "-1")]]);
  const s = stelSamen(S, kop(3, { total_settlement_amount: "20.5", payable_amount: "20.5" }), tr, best);
  assert.equal(s.status, "compleet");
  assert.deepEqual(s.waarschuwingen, []);
  assert.equal(som(s), 2050);
  assert.equal(s.uitbetaaldCenten, 2050);
  assert.deepEqual(s.regels.filter((r) => r.soort === "correctie").map((r) => r.bedragCenten), [-500]);
  assert.ok(s.regels.every((r) => r.statementId === S && r.valuta === "EUR"));
});

test("(c) dezelfde bestelling twee keer in de afrekening: één keer opgehaald en één keer geboekt", () => {
  const tr = [orderT("1", "A", "30"), orderT("2", "A", "-11.5")];
  assert.deepEqual(bestellingenVan(tr), ["A"]);
  const b = bestelling("A", "25", "-4", "-2.5");
  const s = stelSamen(S, kop(2), tr, new Map([["A", b]]));
  assert.equal(s.status, "compleet");
  assert.equal(s.regels.filter((r) => r.soort === "omzet").length, 1);
  assert.equal(som(s), 1850);
  assert.deepEqual(s.waarschuwingen, []);
});

test("(c) adjustment_amount op de bestelling wordt correctie; wat overblijft verschil met waarschuwing", () => {
  const b = bestelling("A", "25", "-4", "-2.5"); // 18.50
  const a = stelSamen(S, kop(1), [orderT("1", "A", "20.2", { adjustment_amount: "1.7" })], new Map([["A", b]]));
  assert.deepEqual(a.regels.filter((r) => r.soort === "correctie").map((r) => r.bedragCenten), [170]);
  assert.equal(a.regels.some((r) => r.soort === "verschil"), false);
  assert.equal(som(a), 2020);
  const c = stelSamen(S, kop(1), [orderT("1", "A", "21", { adjustment_amount: "1.7" })], new Map([["A", b]]));
  assert.deepEqual(c.regels.filter((r) => r.soort === "verschil").map((r) => r.bedragCenten), [80]);
  assert.equal(som(c), 2100);
  assert.equal(c.waarschuwingen.length, 1);
  // sluit al zonder aanpassing: geen correctie die met een verschil wordt opgeheven
  const d = stelSamen(S, kop(1), [orderT("1", "A", "18.5", { adjustment_amount: "1.7" })], new Map([["A", b]]));
  assert.equal(d.regels.some((r) => r.soort === "correctie" || r.soort === "verschil"), false);
});

test("(d) aanpassing met leeg settlement_amount valt terug op adjustment_amount; zonder beide fout_gegevens", () => {
  const a = stelSamen(S, kop(1), [{ id: "9", type: "SHIPPING_FEE_ADJUSTMENT", settlement_amount: "", adjustment_amount: "-3.25" } as any], new Map());
  assert.equal(a.status, "compleet");
  assert.deepEqual(a.regels.map((r) => [r.soort, r.bedragCenten]), [["correctie", -325]]);
  assert.equal(a.waarschuwingen.length, 1);
  const b = stelSamen(S, kop(1), [{ id: "9", type: "OTHER_ADJUSTMENT", settlement_amount: "" } as any], new Map());
  assert.equal(b.status, "fout_gegevens");
});

test("(d) aantal ongelijk aan total_count, of geen kop: onvolledig en geen regels", () => {
  const a = stelSamen(S, kop(2), [orderT("1", "A", "1")], new Map([["A", bestelling("A", "1", "0", "0")]]));
  assert.equal(a.status, "onvolledig");
  assert.equal(a.regels.length, 0);
  assert.equal(stelSamen(S, undefined, [], new Map()).status, "onvolledig");
});

test("(j) ontbrekende of verouderde bestelling (zonder SKU van deze afrekening) moet opnieuw opgehaald worden", () => {
  const oud = bestelling("A", "25", "-4", "-2.5", "7300000000000000000");
  assert.equal(bruikbaar(oud, S), false);
  const s = stelSamen(S, kop(2), [orderT("1", "A", "18.5"), orderT("2", "B", "1")], new Map([["A", oud]]));
  assert.equal(s.status, "onvolledig");
  assert.deepEqual(s.ontbrekend, ["A", "B"]);
});

test("(j) bestelling over twee afrekeningen: de tweede neemt alleen haar eigen regels, zonder verschil", () => {
  const b = bestelling("A", "25", "-4", "-2.5");
  const S2 = "7300000000000000002";
  b.sku_transactions.push({ ...b.sku_transactions[0], sku_id: "1", statement_id: S2, settlement_amount: "-25", revenue_amount: "-25", revenue_breakdown: { refund_subtotal_before_discount_amount: "-25" }, shipping_cost_amount: "0", shipping_cost_breakdown: {}, fee_tax_amount: "0", fee_tax_breakdown: { fee: {}, tax: {} } });
  const s = stelSamen(S2, kop(1, { id: S2 }), [orderT("1", "A", "-25")], new Map([["A", b]]));
  assert.equal(s.status, "compleet");
  assert.deepEqual(s.regels.map((r) => [r.soort, r.bedragCenten, r.statementId]), [["terugbetaling", -2500, S2]]);
  assert.deepEqual(s.waarschuwingen, []);
});

test("vaste fout van de gegevens (andere munt, onleesbaar bedrag) geeft fout_gegevens", () => {
  const b = { ...bestelling("A", "25", "-4", "-2.5"), currency: "GBP" };
  assert.equal(stelSamen(S, kop(1), [orderT("1", "A", "18.5")], new Map([["A", b]])).status, "fout_gegevens");
  assert.equal(stelSamen(S, kop(1), [orderT("1", "A", "abc")], new Map([["A", bestelling("A", "1", "0", "0")]])).status, "fout_gegevens");
});

test("afrekening telt niet op met total_settlement_amount: waarschuwing, wel compleet", () => {
  const s = stelSamen(S, kop(1, { total_settlement_amount: "30" }), [orderT("1", "A", "18.5")], new Map([["A", bestelling("A", "25", "-4", "-2.5")]]));
  assert.equal(s.status, "compleet");
  assert.equal(s.waarschuwingen.length, 1);
});
