import { test } from "node:test";
import assert from "node:assert/strict";
import { boekingsregels } from "../src/boekingen.ts";
import type { BestellingTransacties } from "../src/endpoints.ts";
import { voorbeeld } from "./hulp.ts";

const somVan = (r: { bedragCenten: number }[]) => r.reduce((s, x) => s + x.bedragCenten, 0);
const kort = (r: { soort: string; bedragCenten: number; bronVeld: string }[]) => r.map((x) => [x.soort, x.bedragCenten, x.bronVeld]);

/** Zelfgemaakte sluitende SKU-transactie. */
function sku(extra: Record<string, unknown> = {}): any {
  return {
    sku_id: "11", statement_id: "900", quantity: "1",
    revenue_amount: "45.00",
    revenue_breakdown: {
      subtotal_before_discount_amount: "60.00", seller_discount_amount: "-5.00",
      refund_subtotal_before_discount_amount: "-12.00", seller_discount_refund_amount: "2.00",
      cod_service_fee_amount: "0",
    },
    shipping_cost_amount: "-4.50",
    shipping_cost_breakdown: {
      actual_shipping_fee_amount: "-6.00", customer_paid_shipping_fee_amount: "1.50",
      supplementary_component: { platform_shipping_fee_discount_amount: "20", fbt_fulfillment_fee_reimbursement_amount: "" },
    },
    fee_tax_amount: "-7.30",
    fee_tax_breakdown: {
      fee: { referral_fee_amount: "-4.00", transaction_fee_amount: "-1.00", platform_semi_managed_commission_fee_tax: "-0.80", affiliate_commission_amount: "" },
      tax: { vat_amount: "-1.50", gst_amount: "0" },
    },
    settlement_amount: "33.20",
    ...extra,
  };
}

function bestelling(skus: any[], extra: Record<string, unknown> = {}): BestellingTransacties {
  const totaal = skus.reduce((s, t) => s + Math.round(Number(t.settlement_amount) * 100), 0);
  return { order_id: "577", currency: "EUR", settlement_amount: (totaal / 100).toFixed(2), sku_transactions: skus, ...extra };
}

test("(b) docs-voorbeeld: groepstotalen, SKU-verschil, vier waarschuwingen, som 130,00 GBP", () => {
  const { regels, waarschuwingen } = boekingsregels(voorbeeld("get-transactions-by-order-202501").data);
  assert.deepEqual(kort(regels), [
    ["omzet", 21000, "subtotal_before_discount_amount"],
    ["korting", -1000, "seller_discount_amount"],
    ["verzendkosten_totaal", -7000, "shipping_cost_amount"],
    ["kosten_en_belasting_totaal", -3000, "fee_tax_amount"],
    ["verschil", 3000, "settlement_amount"],
  ]);
  assert.equal(somVan(regels), 13000);
  assert.ok(regels.every((r) => r.valuta === "GBP" && r.sleutel === "5793990727963214852/7238804564097517339/1636700041413599290/0"));
  assert.equal(waarschuwingen.length, 4, waarschuwingen.join("\n"));
  assert.match(waarschuwingen[0], /verzending/);
  assert.match(waarschuwingen[1], /kosten en belasting/);
  assert.match(waarschuwingen[2], /verschil 3000/);
  assert.match(waarschuwingen[3], /total_count is 2/);
});

test("(c) sluitende bestelling met twee SKU's: losse regels, juiste soorten, geen waarschuwing", () => {
  const b = bestelling([sku(), sku({ sku_id: "12" })]);
  const { regels, waarschuwingen } = boekingsregels(b);
  assert.deepEqual(waarschuwingen, []);
  assert.deepEqual(kort(regels.filter((r) => r.skuId === "11")), [
    ["omzet", 6000, "subtotal_before_discount_amount"],
    ["korting", -500, "seller_discount_amount"],
    ["terugbetaling", -1200, "refund_subtotal_before_discount_amount"],
    ["korting_terug", 200, "seller_discount_refund_amount"],
    ["verzendkosten", -600, "actual_shipping_fee_amount"],
    ["verzendkosten", 150, "customer_paid_shipping_fee_amount"],
    ["commissie", -400, "referral_fee_amount"],
    ["commissie", -100, "transaction_fee_amount"],
    ["belasting_op_kosten", -80, "platform_semi_managed_commission_fee_tax"],
    ["belasting", -150, "vat_amount"],
  ]);
  assert.equal(somVan(regels), 6640);
  assert.equal(b.settlement_amount, "66.40");
});

test("(d) onbekend nieuw veld komt mee als regel van zijn groep", () => {
  const t = sku({ revenue_amount: "46.00" });
  t.revenue_breakdown.nieuw_omzetveld_amount = "1.00";
  t.shipping_cost_amount = "-5.50";
  t.shipping_cost_breakdown.nieuwe_verzendtoeslag = "-1.00";
  // 46,00 − 5,50 − 7,30 = 33,20: de afrekening blijft gelijk.
  const { regels, waarschuwingen } = boekingsregels(bestelling([t]));
  assert.deepEqual(waarschuwingen, []);
  assert.deepEqual(kort(regels.filter((r) => r.bronVeld.startsWith("nieuw"))), [
    ["overig_omzet", 100, "nieuw_omzetveld_amount"],
    ["verzendkosten", -100, "nieuwe_verzendtoeslag"],
  ]);
});

test("(e) nul, lege tekst en ontbrekende velden in een uitsplitsing geven geen regel en geen fout", () => {
  const { regels, waarschuwingen } = boekingsregels(bestelling([sku()]));
  assert.deepEqual(waarschuwingen, []);
  for (const veld of ["cod_service_fee_amount", "gst_amount", "affiliate_commission_amount", "supplementary_component"]) {
    assert.ok(!regels.some((r) => r.bronVeld === veld), veld);
  }
});

test("(e2) groep zonder totaal en zonder uitsplitsing: geen regels, waarschuwing, SKU-controle overgeslagen", () => {
  const t = sku();
  delete t.fee_tax_amount;
  t.fee_tax_breakdown = "kapot";
  const { regels, waarschuwingen } = boekingsregels(bestelling([t]));
  assert.ok(!regels.some((r) => ["commissie", "belasting", "verschil"].includes(r.soort)));
  assert.ok(waarschuwingen.some((x) => /kosten en belasting: geen totaal en geen uitsplitsing/.test(x)));
  assert.ok(waarschuwingen.some((x) => /controle op settlement_amount overgeslagen/.test(x)));
});

test("(f) object of null in een uitsplitsing: overgeslagen met waarschuwing, groep valt terug op het totaal", () => {
  const t = sku();
  t.fee_tax_breakdown.fee.referral_fee_amount = { raar: 1 };
  t.fee_tax_breakdown.tax.vat_amount = null;
  const { regels, waarschuwingen } = boekingsregels(bestelling([t]));
  assert.ok(waarschuwingen.some((x) => /fee\.referral_fee_amount: geen bedrag/.test(x)));
  assert.ok(waarschuwingen.some((x) => /tax\.vat_amount: geen bedrag/.test(x)));
  assert.ok(waarschuwingen.some((x) => /kosten en belasting: uitsplitsing \(-180\) sluit niet op fee_tax_amount \(-730\), totaal geboekt/.test(x)));
  assert.deepEqual(kort(regels.filter((r) => r.soort.startsWith("kosten") || r.soort === "commissie")), [
    ["kosten_en_belasting_totaal", -730, "fee_tax_amount"],
  ]);
  assert.equal(somVan(regels), 3320);
});

test("(g) ongeldige of ontbrekende munt geeft een fout voor de bestelling", () => {
  assert.throws(() => boekingsregels(bestelling([sku()], { currency: "EURO" })), /ongeldige munt/);
  assert.throws(() => boekingsregels(bestelling([sku()], { currency: undefined })), /ongeldige munt/);
});

test("(h) omzet-uitsplitsing die niet sluit: omzet_totaal plus waarschuwing", () => {
  const t = sku({ revenue_amount: "50.00", settlement_amount: "38.20" });
  const { regels, waarschuwingen } = boekingsregels(bestelling([t]));
  assert.deepEqual(kort(regels.filter((r) => r.soort.includes("omzet") || r.soort.includes("korting") || r.soort === "terugbetaling")), [
    ["omzet_totaal", 5000, "revenue_amount"],
  ]);
  assert.equal(waarschuwingen.length, 1);
  assert.match(waarschuwingen[0], /omzet: uitsplitsing \(4500\) sluit niet op revenue_amount \(5000\)/);
});

test("(i) alleen de kop sluit niet: waarschuwing, geen verschil-regel", () => {
  const { regels, waarschuwingen } = boekingsregels(bestelling([sku()], { settlement_amount: "40.00" }));
  assert.ok(!regels.some((r) => r.soort === "verschil"));
  assert.deepEqual(waarschuwingen, ["kop: alle regels samen 3320, settlement_amount van de bestelling is 4000; niet geboekt, alleen gemeld"]);
});

test("(i2) lege totalen zijn onbekend, niet 0", () => {
  const leeg = sku({ settlement_amount: "" });
  let u = boekingsregels(bestelling([sku()], { sku_transactions: [leeg], settlement_amount: "" }));
  assert.ok(!u.regels.some((r) => r.soort === "verschil"));
  assert.ok(u.waarschuwingen.some((x) => /sku 11.*controle op settlement_amount overgeslagen/.test(x)));
  assert.ok(u.waarschuwingen.some((x) => /kop: controle op settlement_amount overgeslagen/.test(x)));
  assert.equal(somVan(u.regels), 3320);

  u = boekingsregels(bestelling([sku({ shipping_cost_amount: "" })]));
  assert.deepEqual(kort(u.regels.filter((r) => r.soort.startsWith("verzend"))), [
    ["verzendkosten", -600, "actual_shipping_fee_amount"],
    ["verzendkosten", 150, "customer_paid_shipping_fee_amount"],
  ]);
  assert.deepEqual(u.waarschuwingen, ["sku 11 (afrekening 900) verzending: totaal shipping_cost_amount onbekend, uitsplitsing gebruikt"]);
});

test("(j) dezelfde sku in twee afrekeningen: twee sleutels, gedeeld per transactie, stabiel", () => {
  const verkoop = sku();
  const retour = sku({ statement_id: "901" });
  const dubbel = sku();
  const b = bestelling([verkoop, retour, dubbel]);
  const een = boekingsregels(b).regels;
  const sleutels = [...new Set(een.map((r) => r.sleutel))];
  assert.deepEqual(sleutels, ["577/900/11/0", "577/901/11/0", "577/900/11/1"]);
  assert.equal(een.filter((r) => r.sleutel === "577/901/11/0").length, 10);
  assert.deepEqual(boekingsregels(structuredClone(b)).regels.map((r) => r.sleutel), een.map((r) => r.sleutel));
});

test("(k) JPY zonder decimalen", () => {
  const t = {
    sku_id: "1", statement_id: "2",
    revenue_amount: "1000", revenue_breakdown: { subtotal_before_discount_amount: "1000" },
    shipping_cost_amount: "-200", shipping_cost_breakdown: { actual_shipping_fee_amount: "-200" },
    fee_tax_amount: "-50", fee_tax_breakdown: { fee: { referral_fee_amount: "-50" }, tax: {} },
    settlement_amount: "750",
  };
  const { regels, waarschuwingen } = boekingsregels({ order_id: "9", currency: "JPY", settlement_amount: "750", sku_transactions: [t] });
  assert.deepEqual(waarschuwingen, []);
  assert.deepEqual(regels.map((r) => r.bedragCenten), [1000, -200, -50]);
});

test("onbekend totaal en onvolledige uitsplitsing: groep onbekend, geen omzet naar verschil", () => {
  for (const kapot of [{ x: 1 }, "50.001x", null]) {
    const t = sku({ revenue_amount: "" });
    t.revenue_breakdown = { subtotal_before_discount_amount: kapot, seller_discount_amount: "-5.00" };
    const { regels, waarschuwingen } = boekingsregels(bestelling([t], { settlement_amount: "33.20" }));
    assert.ok(!regels.some((r) => r.soort === "verschil"), String(kapot));
    assert.deepEqual(kort(regels.filter((r) => r.soort === "korting")), [["korting", -500, "seller_discount_amount"]]);
    assert.ok(waarschuwingen.some((x) => /omzet: totaal revenue_amount onbekend en uitsplitsing onvolledig, groep onbekend/.test(x)));
    assert.ok(waarschuwingen.some((x) => /controle op settlement_amount overgeslagen/.test(x)));
  }
  const leeg = sku({ revenue_amount: "", revenue_breakdown: {} });
  const u = boekingsregels(bestelling([leeg], { settlement_amount: "33.20" }));
  assert.ok(!u.regels.some((r) => r.soort === "verschil"));
  assert.ok(u.waarschuwingen.some((x) => /groep onbekend/.test(x)));
});

test("kapotte helft van fee_tax_breakdown: waarschuwing, en bij leeg totaal geen stille verschil-regel", () => {
  const t = sku({ fee_tax_amount: "" });
  t.fee_tax_breakdown.tax = "kapot";
  const { regels, waarschuwingen } = boekingsregels(bestelling([t]));
  assert.ok(waarschuwingen.some((x) => /tax: geen object, overgeslagen/.test(x)));
  assert.ok(waarschuwingen.some((x) => /kosten en belasting: totaal fee_tax_amount onbekend en uitsplitsing onvolledig/.test(x)));
  assert.ok(!regels.some((r) => r.soort === "verschil"));
  assert.equal(regels.filter((r) => r.soort === "commissie").length, 2);
});

test("te veel decimalen voor de munt: fout voor de hele bestelling", () => {
  assert.throws(() => boekingsregels(bestelling([sku({ settlement_amount: "33.200" })])), /decimalen/);
  const t = sku();
  t.fee_tax_breakdown.fee.referral_fee_amount = "-4.000";
  assert.throws(() => boekingsregels(bestelling([t])), /decimalen/);
});

test("kleine letters in de munt, total_count als tekst, ontbrekende ids en sku_transactions", () => {
  let u = boekingsregels(bestelling([sku()], { currency: "eur", total_count: "2" }));
  assert.ok(u.regels.every((r) => r.valuta === "EUR"));
  assert.deepEqual(u.waarschuwingen, ["total_count is 2, maar er zijn 1 SKU-transacties"]);
  u = boekingsregels(bestelling([sku({ statement_id: undefined })]));
  assert.ok(u.waarschuwingen.some((x) => /statement_id of sku_id ontbreekt/.test(x)));
  u = boekingsregels({ order_id: "1", currency: "EUR", settlement_amount: "0" } as any);
  assert.deepEqual(u.waarschuwingen, ["sku_transactions ontbreekt of is geen lijst"]);
});
