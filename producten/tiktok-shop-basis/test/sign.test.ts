import { test } from "node:test";
import assert from "node:assert/strict";
import { maakHandtekening, tekenTekst } from "../src/sign.ts";

test("voorbeeld uit sign-your-api-request geeft de uitkomst uit de docs", async () => {
  const s = await maakHandtekening(
    { path: "/authorization/202309/shops", query: { app_key: "29a39d", timestamp: "1623812664" } },
    "e59af819cc",
  );
  assert.equal(s, "b596b73e0cc6de07ac26f036364178ab16b0a907af13d43f0a0cd2345f582dc8");
});

test("voorbeeld uit create-hash (zelf en door controleur met Python nagerekend)", async () => {
  const req = { path: "/authorization/202309/shops", query: { app_key: "123456", timestamp: "1234567890" } };
  assert.equal(tekenTekst(req), "/authorization/202309/shopsapp_key123456timestamp1234567890");
  assert.equal(
    await maakHandtekening(req, "abc000def111"),
    "c8767e4fd7a1b48a0ce3fd23197f058159ce11b53f1ae1ad6d1ec931a1da5540",
  );
});

test("sign en access_token tellen niet mee, volgorde maakt niet uit", async () => {
  const a = await maakHandtekening({ path: "/p", query: { timestamp: "1", app_key: "k" } }, "s");
  const b = await maakHandtekening({ path: "/p", query: { app_key: "k", sign: "x", access_token: "y", timestamp: "1" } }, "s");
  assert.equal(a, b);
});

test("body telt mee, behalve bij multipart", () => {
  const basis = { path: "/p", query: { a: "1" }, body: '{"x":1}' };
  assert.equal(tekenTekst({ ...basis, contentType: "application/json" }), '/pa1{"x":1}');
  assert.equal(tekenTekst({ ...basis, contentType: "multipart/form-data; boundary=abc" }), "/pa1");
});

test("ruwe waarden met / en + worden getekend zoals ze zijn", () => {
  assert.equal(tekenTekst({ path: "/p", query: { page_token: "ab/c+d=" } }), "/ppage_tokenab/c+d=");
});
