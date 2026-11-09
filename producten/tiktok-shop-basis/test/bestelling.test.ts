import { test } from "node:test";
import assert from "node:assert/strict";
import { maakHandtekening } from "../src/sign.ts";
import { transactiesVanBestelling } from "../src/endpoints.ts";
import { APP, nepClient, voorbeeld } from "./hulp.ts";

test("transacties van een bestelling: docs-antwoord, pad, shop_cipher, token en handtekening", async () => {
  const doc = voorbeeld("get-transactions-by-order-202501");
  const { client, verzoeken } = nepClient([{ json: doc }]);
  const b = await transactiesVanBestelling(client, "TTP_t", "ROW_c", "5793990727963214852");
  const v = verzoeken[0];
  assert.equal(verzoeken.length, 1);
  assert.equal(v.method, "GET");
  assert.equal(v.url.pathname, "/finance/202501/orders/5793990727963214852/statement_transactions");
  assert.equal(v.url.searchParams.get("shop_cipher"), "ROW_c");
  assert.equal(v.url.searchParams.get("page_token"), null);
  assert.equal(v.headers["x-tts-access-token"], "TTP_t");
  const query = Object.fromEntries(v.url.searchParams);
  assert.equal(query.sign, await maakHandtekening({ path: v.url.pathname, query }, APP.appSecret));
  assert.equal(b.order_id, "5793990727963214852");
  assert.equal(b.currency, "GBP");
  assert.equal(b.fee_and_tax_amount, "-30");
  assert.equal(b.settlement_amount, "130");
  assert.equal(b.total_count, 2);
  assert.equal(b.sku_transactions.length, 1);
  const s = b.sku_transactions[0];
  assert.equal(s.statement_id, "7238804564097517339");
  assert.equal(s.fee_tax_amount, "-30");
  assert.equal(s.revenue_breakdown?.subtotal_before_discount_amount, "210");
  assert.equal(s.fee_tax_breakdown?.tax?.vat_amount, "0");
  assert.ok("supplementary_component" in (s.shipping_cost_breakdown ?? {}));
});

test("bestelling zonder sku_transactions geeft een lege lijst", async () => {
  const { client } = nepClient([{ json: { code: 0, message: "Success", request_id: "x", data: { order_id: "1", currency: "EUR" } } }]);
  const b = await transactiesVanBestelling(client, "t", "c", "1");
  assert.deepEqual(b.sku_transactions, []);
});

test("ongeldig order_id wordt geweigerd voor er iets verstuurd wordt", async () => {
  const { client, verzoeken } = nepClient([{ json: {} }]);
  await assert.rejects(transactiesVanBestelling(client, "t", "c", "../x"), /ongeldig order_id/);
  await assert.rejects(transactiesVanBestelling(client, "t", "c", ""), /ongeldig order_id/);
  assert.equal(verzoeken.length, 0);
});
