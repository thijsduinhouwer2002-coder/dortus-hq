import { test } from "node:test";
import assert from "node:assert/strict";
import { haalTokens, ververs, inlogLink, maakState, stateKlopt, verlooptBinnen } from "../src/auth.ts";
import { TikTokApiError } from "../src/fouten.ts";
import { APP, nepFetch, voorbeeld } from "./hulp.ts";

test("auth_code inwisselen: juiste url, parameters en uitlezen van het docs-antwoord", async () => {
  const nep = nepFetch([{ json: voorbeeld("token-get") }]);
  const t = await haalTokens(APP, "TTP_FeBoANmHP3yqdoUI9fZOCw", nep.fn);
  const v = nep.verzoeken[0];
  assert.equal(v.url.origin + v.url.pathname, "https://auth.tiktok-shops.com/api/v2/token/get");
  assert.equal(v.method, "GET");
  assert.equal(v.url.searchParams.get("grant_type"), "authorized_code");
  assert.equal(v.url.searchParams.get("auth_code"), "TTP_FeBoANmHP3yqdoUI9fZOCw");
  assert.equal(v.url.searchParams.get("app_key"), "123abc");
  assert.equal(v.url.searchParams.get("app_secret"), APP.appSecret);
  assert.equal(v.url.searchParams.get("sign"), null);
  assert.equal(t.accessTokenVerlooptOp, 1660556783);
  assert.equal(t.refreshTokenVerlooptOp, 1691487031);
  assert.equal(t.sellerName, "Test Seller");
  assert.equal(t.userType, 0);
  assert.deepEqual(t.grantedScopes, ["seller.affiliate_collaboration.read", "seller.affiliate_collaboration.write"]);
});

test("verversen: grant_type refresh_token en eigen pad", async () => {
  const nep = nepFetch([{ json: voorbeeld("token-get") }]);
  await ververs(APP, "TTP_C2XWDN63ON-FOHJSMR0WSG", nep.fn);
  const v = nep.verzoeken[0];
  assert.equal(v.url.origin + v.url.pathname, "https://auth.tiktok-shops.com/api/v2/token/refresh");
  assert.equal(v.url.searchParams.get("app_key"), APP.appKey);
  assert.equal(v.url.searchParams.get("app_secret"), APP.appSecret);
  assert.equal(v.url.searchParams.get("grant_type"), "refresh_token");
  assert.equal(v.url.searchParams.get("refresh_token"), "TTP_C2XWDN63ON-FOHJSMR0WSG");
});

test("36004004 geeft soort auth_code_ongeldig, zonder het secret in de fout", async () => {
  const nep = nepFetch([{ json: { code: 36004004, message: "Invalid auth code.", request_id: "R1" } }]);
  await assert.rejects(haalTokens(APP, "oud", nep.fn), (e: unknown) => {
    assert.ok(e instanceof TikTokApiError);
    assert.equal(e.soort, "auth_code_ongeldig");
    assert.equal(e.requestId, "R1");
    assert.ok(!e.message.includes(APP.appSecret));
    return true;
  });
});

test("verlooptBinnen met de waarde uit de docs (tijdstip, geen duur)", () => {
  const op = 1660556783;
  assert.equal(verlooptBinnen(op, 3600, op - 1800), true);
  assert.equal(verlooptBinnen(op, 3600, op - 7200), false);
});

test("inloglink voor EU en VS", () => {
  assert.equal(inlogLink("7123", "abc"), "https://services.tiktokshop.com/open/authorize?service_id=7123&state=abc");
  assert.ok(inlogLink("7123", "abc", "US").startsWith("https://services.us.tiktokshop.com/open/authorize?"));
});

test("state is willekeurig en wordt streng vergeleken", () => {
  const s = maakState();
  assert.match(s, /^[0-9a-f]{32}$/);
  assert.notEqual(s, maakState());
  assert.equal(stateKlopt(s, s), true);
  assert.equal(stateKlopt(s, s.slice(0, -1) + (s.endsWith("0") ? "1" : "0")), false);
  assert.equal(stateKlopt(s, null), false);
  assert.equal(stateKlopt(s, ""), false);
});

test("netwerkfout bij tokens geeft eigen fout zonder secret", async () => {
  const kapot = (async () => {
    throw new Error("fetch failed https://auth.tiktok-shops.com/?app_secret=" + APP.appSecret);
  }) as typeof fetch;
  await assert.rejects(haalTokens(APP, "c", kapot), (e: unknown) => {
    assert.ok(e instanceof TikTokApiError);
    assert.ok(!e.message.includes(APP.appSecret));
    return true;
  });
});

test("code 0 zonder tokens geeft een fout in plaats van lege velden", async () => {
  const nep = nepFetch([{ json: { code: 0, message: "success", request_id: "R", data: { open_id: "1" } } }]);
  await assert.rejects(haalTokens(APP, "c", nep.fn), /zonder access_token/);
});
