// meldWebhookAan: vorm uit de docs van Update Shop Webhook (GEZIEN 10 nov 2026), voor ontwerp-schermen.md stap 1.
import { test } from "node:test";
import assert from "node:assert/strict";
import { maakHandtekening } from "../src/sign.ts";
import { meldWebhookAan } from "../src/endpoints.ts";
import { APP, nepClient } from "./hulp.ts";

const DOCS_ANTWOORD = { code: 0, data: {}, message: "Success", request_id: "202203070749000101890810281E8C70B7" };

test("webhook aanmelden: PUT, pad, shop_cipher, body getekend en verstuurd", async () => {
  const { client, verzoeken } = nepClient([{ json: DOCS_ANTWOORD }]);
  await meldWebhookAan(client, "TTP_token", "ROW_cipher", "SELLER_DEAUTHORIZATION", "https://klopt.dortus.com/tiktok/webhook");
  const v = verzoeken[0];
  assert.equal(v.method, "PUT");
  assert.equal(v.url.origin, "https://open-api.tiktokglobalshop.com");
  assert.equal(v.url.pathname, "/event/202309/webhooks");
  assert.equal(v.url.searchParams.get("shop_cipher"), "ROW_cipher");
  assert.equal(v.headers["x-tts-access-token"], "TTP_token");
  assert.match(v.headers["content-type"], /application\/json/);
  assert.deepEqual(JSON.parse(v.body!), { address: "https://klopt.dortus.com/tiktok/webhook", event_type: "SELLER_DEAUTHORIZATION" });
  const query = Object.fromEntries(v.url.searchParams);
  assert.equal(query.sign, await maakHandtekening({ path: v.url.pathname, query, body: v.body, contentType: "application/json" }, APP.appSecret));
});

test("webhook aanmelden: fout van TikTok wordt een fout, ongeldig adres gaat niet de deur uit", async () => {
  const { client, verzoeken } = nepClient([{ json: { code: 36009004, message: "Invalid parameter", request_id: "x", data: {} } }]);
  await assert.rejects(meldWebhookAan(client, "t", "c", "UPCOMING_AUTHORIZATION_EXPIRATION", "https://a.example/w"));
  assert.equal(verzoeken.length, 1);
  await assert.rejects(meldWebhookAan(client, "t", "c", "SELLER_DEAUTHORIZATION", "ftp://a.example"));
  await assert.rejects(meldWebhookAan(client, "t", "c", "SELLER_DEAUTHORIZATION", "https://a.example/" + "x".repeat(238)), "256 tekens");
  assert.equal(verzoeken.length, 1);
});

test("webhook aanmelden: precies 255 tekens mag", async () => {
  const { client, verzoeken } = nepClient([{ json: DOCS_ANTWOORD }]);
  const adres = "https://a.example/" + "x".repeat(237);
  assert.equal(adres.length, 255);
  await meldWebhookAan(client, "t", "c", "SELLER_DEAUTHORIZATION", adres);
  assert.equal(verzoeken.length, 1);
});
