// Affiliate-commissie als eigen soort (ontwerp: producten/tiktok-boekhouding/ontwerp-affiliate.md, eisen a, b, g, h).
import { test } from "node:test";
import assert from "node:assert/strict";
import { boekingsregels, soortVanKostenveld } from "../src/boekingen.ts";
import type { BestellingTransacties } from "../src/endpoints.ts";
import { voorbeeld } from "./hulp.ts";

function bestelling(fee: Record<string, string>): BestellingTransacties {
  const feeCenten = Object.values(fee).reduce((s, v) => s + Math.round(Number(v || 0) * 100), 0);
  const settlement = 5000 + feeCenten;
  return {
    order_id: "577", currency: "EUR", settlement_amount: (settlement / 100).toFixed(2),
    sku_transactions: [{
      sku_id: "11", statement_id: "900", quantity: "1",
      revenue_amount: "50.00", revenue_breakdown: { subtotal_before_discount_amount: "50.00" },
      shipping_cost_amount: "0", shipping_cost_breakdown: {},
      fee_tax_amount: (feeCenten / 100).toFixed(2), fee_tax_breakdown: { fee, tax: {} },
      settlement_amount: (settlement / 100).toFixed(2),
    }],
  } as any;
}
const per = (b: ReturnType<typeof boekingsregels>) => b.regels.filter((r) => r.soort !== "omzet").map((r) => [r.soort, r.bedragCenten, r.bronVeld]);

test("(a) affiliate en platformcommissie: twee regels, som klopt, geen waarschuwing", () => {
  const b = boekingsregels(bestelling({ affiliate_commission_amount: "-3.00", platform_commission_amount: "-4.00" }));
  assert.deepEqual(per(b), [["affiliate", -300, "affiliate_commission_amount"], ["commissie", -400, "platform_commission_amount"]]);
  assert.equal(b.regels.reduce((s, r) => s + r.bedragCenten, 0), 4300);
  assert.deepEqual(b.waarschuwingen, []);
});

test("(b) externe affiliate-marketing en meebetaalde creator-bonus blijven commissie van TikTok", () => {
  assert.equal(soortVanKostenveld("external_affiliate_marketing_fee_amount"), "commissie");
  assert.equal(soortVanKostenveld("cofunded_creator_bonus_amount"), "commissie");
  const b = boekingsregels(bestelling({ external_affiliate_marketing_fee_amount: "-1.00", cofunded_creator_bonus_amount: "-2.00" }));
  assert.deepEqual(per(b).map((r) => r[0]), ["commissie", "commissie"]);
});

test("(g) tap_shop_ads_commission en alle affiliate_-velden worden affiliate; een veld op _tax blijft btw op kosten", () => {
  for (const v of ["tap_shop_ads_commission", "affiliate_commission_amount", "affiliate_partner_commission_amount", "affiliate_ads_commission_amount",
    "affiliate_commission_amount_before_pit", "affiliate_commission_deposit", "affiliate_commission_release"]) assert.equal(soortVanKostenveld(v), "affiliate", v);
  assert.equal(soortVanKostenveld("affiliate_x_tax"), "belasting_op_kosten");
  assert.equal(soortVanKostenveld("affiliate_x_tax_amount"), "belasting_op_kosten");
  assert.equal(soortVanKostenveld("platform_semi_managed_commission_fee_tax"), "belasting_op_kosten");
});

test("(h) nul of leeg geeft geen affiliate-regel; docs-voorbeeld sluit niet en boekt dus alleen het totaal, zoals vóór de wijziging", () => {
  const docs = boekingsregels(voorbeeld("get-transactions-by-order-202501").data);
  assert.equal(docs.regels.filter((r) => r.soort === "affiliate").length, 0);
  const b = boekingsregels(bestelling({ affiliate_commission_amount: "0", affiliate_commission_deposit: "", platform_commission_amount: "-4.00" }));
  assert.deepEqual(per(b).map((r) => r[0]), ["commissie"]);
});
