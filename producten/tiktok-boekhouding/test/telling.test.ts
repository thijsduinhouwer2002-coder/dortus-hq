// Toets (d), deel maand en n, uit ontwerp-betalen.md, punt 7.
import { test } from "node:test";
import assert from "node:assert/strict";
import { maandVan, telBestellingen } from "../src/telling.ts";

const utc = (s: string) => Date.parse(s) / 1000;

test("(d) maand in Europe/Amsterdam: 31 dec 23:30 UTC telt als januari, 30 nov 22:59 UTC nog november", () => {
  assert.equal(maandVan(utc("2026-12-31T23:30:00Z")), "2027-01");
  assert.equal(maandVan(utc("2026-12-31T22:59:59Z")), "2026-12");
  assert.equal(maandVan(utc("2026-11-30T22:59:59Z")), "2026-11");
  assert.equal(maandVan(utc("2026-11-30T23:00:00Z")), "2026-12");
  // Zomertijd: 31 mei 22:00 UTC is 1 juni 00:00 in Amsterdam.
  assert.equal(maandVan(utc("2026-05-31T22:00:00Z")), "2026-06");
  assert.equal(maandVan(utc("2026-05-31T21:59:59Z")), "2026-05");
});

test("(d) n: unieke order_id van ORDER-transacties; andere typen en ORDER zonder order_id tellen niet", () => {
  const t = (type: string, order_id?: string) => ({ id: `${type}-${order_id}`, type, order_id }) as any;
  assert.equal(telBestellingen([t("ORDER", "1"), t("ORDER", "1"), t("ORDER", "2"), t("SHIPPING_FEE", "3"), t("ORDER"), t("RESERVE")]), 2);
  assert.equal(telBestellingen([]), 0, "afrekening zonder bestellingen telt 0");
  assert.equal(telBestellingen([t("ADJUSTMENT")]), 0);
});
