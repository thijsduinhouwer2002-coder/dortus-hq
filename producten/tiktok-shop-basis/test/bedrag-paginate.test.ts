import { test } from "node:test";
import assert from "node:assert/strict";
import { naarKleinsteEenheid } from "../src/bedrag.ts";
import { allePaginas, verzamel } from "../src/paginate.ts";

test("bedragen naar kleinste munteenheid", () => {
  assert.equal(naarKleinsteEenheid("12.34", "EUR"), 1234);
  assert.equal(naarKleinsteEenheid("-30", "GBP"), -3000);
  assert.equal(naarKleinsteEenheid("0.1", "EUR"), 10);
  assert.equal(naarKleinsteEenheid("1500", "JPY"), 1500);
  assert.equal(naarKleinsteEenheid("-0", "EUR"), 0);
});

test("te veel decimalen of rare tekst geeft een fout", () => {
  assert.throws(() => naarKleinsteEenheid("1.234", "EUR"));
  assert.throws(() => naarKleinsteEenheid("1.5", "JPY"));
  assert.throws(() => naarKleinsteEenheid("12,34", "EUR"));
  assert.throws(() => naarKleinsteEenheid("", "EUR"));
  assert.throws(() => naarKleinsteEenheid("1e5", "EUR"));
  assert.throws(() => naarKleinsteEenheid("99999999999999999", "EUR"));
});

test("paginering stopt bij lege en bij ontbrekende next_page_token", async () => {
  let n = 0;
  const leeg = await verzamel(allePaginas(async (t) => (n++ === 0 ? { items: [1], nextPageToken: "a" } : { items: [t === "a" ? 2 : -1], nextPageToken: "" })));
  assert.deepEqual(leeg, [1, 2]);
  const weg = await verzamel(allePaginas(async () => ({ items: [7] })));
  assert.deepEqual(weg, [7]);
});

test("paginering stopt bij de bovengrens", async () => {
  let keer = 0;
  await assert.rejects(
    verzamel(allePaginas(async () => (keer++, { items: [], nextPageToken: "altijd" }), 5)),
    /meer dan 5/,
  );
  assert.equal(keer, 5);
});
