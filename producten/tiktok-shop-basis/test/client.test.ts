import { test } from "node:test";
import assert from "node:assert/strict";
import { TikTokApiError } from "../src/fouten.ts";
import { maakHandtekening } from "../src/sign.ts";
import { geautoriseerdeWinkels, afrekeningen, transactiesVanAfrekening } from "../src/endpoints.ts";
import { verzamel } from "../src/paginate.ts";
import { APP, nepClient, voorbeeld } from "./hulp.ts";

test("winkels: docs-antwoord, token in de kop en niet in de query, geldige handtekening", async () => {
  const { client, verzoeken } = nepClient([{ json: voorbeeld("get-authorized-shops-202309") }]);
  const winkels = await geautoriseerdeWinkels(client, "TTP_token");
  assert.equal(winkels.length, 1);
  assert.equal(winkels[0].cipher, "GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3");
  assert.equal(winkels[0].region, "GB");
  const v = verzoeken[0];
  assert.equal(v.url.origin, "https://open-api.tiktokglobalshop.com");
  assert.equal(v.url.pathname, "/authorization/202309/shops");
  assert.equal(v.headers["x-tts-access-token"], "TTP_token");
  assert.equal(v.url.searchParams.get("access_token"), null);
  assert.equal(v.url.searchParams.get("timestamp"), "1625484268");
  assert.equal(v.url.searchParams.get("shop_cipher"), null);
  const query = Object.fromEntries(v.url.searchParams);
  assert.equal(query.sign, await maakHandtekening({ path: v.url.pathname, query }, APP.appSecret));
});

test("afrekeningen: verplichte sortering, filters, page_token ruw getekend en gecodeerd verstuurd", async () => {
  const eerste = voorbeeld("get-statements-202309");
  const tweede = structuredClone(eerste);
  tweede.data.next_page_token = "";
  tweede.data.statements[0].id = "2";
  const { client, verzoeken } = nepClient([{ json: eerste }, { json: tweede }]);
  const lijst = await verzamel(afrekeningen(client, "t", "ROW_cipher", { vanaf: 1777420800, tot: 1777507200, status: "PAID" }));
  assert.deepEqual(lijst.map((s) => s.id), ["7238804564097517339", "2"]);
  assert.equal(lijst[0].currency, "GBP");
  assert.equal(lijst[0].settlement_amount, "100");
  assert.equal(verzoeken.length, 2);
  const [v1, v2] = verzoeken;
  assert.equal(v1.url.pathname, "/finance/202309/statements");
  assert.equal(v1.url.searchParams.get("sort_field"), "statement_time");
  assert.equal(v1.url.searchParams.get("shop_cipher"), "ROW_cipher");
  assert.equal(v1.url.searchParams.get("statement_time_ge"), "1777420800");
  assert.equal(v1.url.searchParams.get("payment_status"), "PAID");
  assert.equal(v1.url.searchParams.get("page_token"), null);
  assert.equal(v1.url.searchParams.has("sort_order"), false);
  const token = eerste.data.next_page_token as string;
  assert.ok(token.includes("/") && token.includes("+"));
  assert.equal(v2.url.searchParams.get("page_token"), token);
  assert.ok(!v2.url.search.includes("+"), "plus moet gecodeerd in de url staan");
  const query = Object.fromEntries(v2.url.searchParams);
  assert.equal(query.sign, await maakHandtekening({ path: v2.url.pathname, query }, APP.appSecret));
});

test("transacties per afrekening: kop en transacties uit het docs-antwoord", async () => {
  const doc = voorbeeld("get-transactions-by-statement-202501");
  doc.data.next_page_token = undefined; // stop na één pagina
  const c2 = nepClient([{ json: doc }]);
  const u = await transactiesVanAfrekening(c2.client, "t", "ROW_c", "7238804564097517339");
  assert.equal(c2.verzoeken[0].url.pathname, "/finance/202501/statements/7238804564097517339/statement_transactions");
  assert.equal(c2.verzoeken[0].url.searchParams.get("sort_field"), "order_create_time");
  assert.equal(u.kop?.id, "7238804564097517339");
  assert.equal(u.kop?.currency, "GBP");
  assert.equal(u.transacties.length, doc.data.transactions.length);
  assert.equal(u.transacties[0].type, doc.data.transactions[0].type);
  assert.ok("fee_tax_breakdown" in u.transacties[0]);
});

test("ongeldig statement_id wordt geweigerd voor er iets verstuurd wordt", async () => {
  const { client, verzoeken } = nepClient([{ json: {} }]);
  await assert.rejects(transactiesVanAfrekening(client, "t", "c", "../x"));
  assert.equal(verzoeken.length, 0);
});

test("429 met Retry-After: 3 pogingen, dan fout te_veel_verzoeken", async () => {
  const { client, verzoeken, slapen } = nepClient([
    { status: 429, headers: { "retry-after": "0" }, json: { code: 36009002, message: "Too many requests", request_id: "R" } },
  ]);
  await assert.rejects(geautoriseerdeWinkels(client, "t"), (e: unknown) => {
    assert.ok(e instanceof TikTokApiError);
    assert.equal(e.soort, "te_veel_verzoeken");
    return true;
  });
  assert.equal(verzoeken.length, 3);
  assert.deepEqual(slapen, [0, 0]);
});

test("zonder Retry-After oplopend wachten; tweede poging gelukt geeft gewoon het antwoord", async () => {
  const { client, verzoeken, slapen } = nepClient([
    { status: 503, tekst: "storing" },
    { json: voorbeeld("get-authorized-shops-202309") },
  ]);
  const w = await geautoriseerdeWinkels(client, "t");
  assert.equal(w.length, 1);
  assert.equal(verzoeken.length, 2);
  assert.deepEqual(slapen, [1000]);
});

test("105002 geeft token_verlopen zonder herhaling; message en request_id staan in de fout", async () => {
  const { client, verzoeken } = nepClient([{ json: { code: 105002, message: "Expired credentials", request_id: "REQ9" } }]);
  await assert.rejects(geautoriseerdeWinkels(client, "t"), (e: unknown) => {
    assert.ok(e instanceof TikTokApiError);
    assert.equal(e.soort, "token_verlopen");
    assert.equal(e.requestId, "REQ9");
    assert.match(e.message, /Expired credentials/);
    return true;
  });
  assert.equal(verzoeken.length, 1);
});

test("105005 en 106001 krijgen hun eigen soort", async () => {
  for (const [code, soort] of [[105005, "geen_toegang"], [106001, "handtekening_fout"], [36009004, "overig"]] as const) {
    const { client } = nepClient([{ json: { code, message: "m", request_id: "r" } }]);
    await assert.rejects(geautoriseerdeWinkels(client, "t"), (e: any) => e.soort === soort);
  }
});

test("body wordt precies zo getekend als verstuurd", async () => {
  const { client, verzoeken } = nepClient([{ json: { code: 0, data: {}, request_id: "r" } }]);
  await client.roep({ method: "POST", path: "/x/202309/y", accessToken: "t", body: { b: 2, a: "é" } });
  const v = verzoeken[0];
  const query = Object.fromEntries(v.url.searchParams);
  assert.equal(v.body, '{"b":2,"a":"é"}');
  assert.equal(query.sign, await maakHandtekening({ path: v.url.pathname, query, body: v.body, contentType: "application/json" }, APP.appSecret));
});

test("5xx drie keer mislukt geeft soort server na 3 pogingen", async () => {
  const { client, verzoeken, slapen } = nepClient([{ status: 502, tekst: "bad gateway" }]);
  await assert.rejects(geautoriseerdeWinkels(client, "t"), (e: any) => e.soort === "server");
  assert.equal(verzoeken.length, 3);
  assert.deepEqual(slapen, [1000, 2000]);
});
