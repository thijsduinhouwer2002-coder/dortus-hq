import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { RGS_PER_SOORT, RGS_TEGENREKENING } from "../src/moneybird/rgs.ts";
import { SOORTEN } from "../src/moneybird/memoriaal.ts";

const lijst = new Map(
  readFileSync(new URL("./voorbeelden/rgs35-uittreksel.tsv", import.meta.url), "utf8").split("\n").filter((r) => r && !r.startsWith("#")).map((r) => {
    const [code, nummer, omschrijving, dc, nivo, inactief] = r.split("\t");
    return [code, { nummer, omschrijving, dc, nivo, inactief }];
  }),
);

test("RGS: elke soort heeft een voorstel", () => {
  for (const [soort] of SOORTEN) assert.ok(RGS_PER_SOORT[soort], soort);
});

test("RGS: elke code staat actief in de definitieve RGS 3.5-lijst, met het juiste soort rekening", () => {
  for (const [soort, v] of [...Object.entries(RGS_PER_SOORT), ["tegenrekening", RGS_TEGENREKENING] as const]) {
    const r = lijst.get(v.rgs);
    assert.ok(r, `${soort}: ${v.rgs} staat niet in RGS 3.5`);
    assert.notEqual(r!.inactief, "1", `${soort}: ${v.rgs} is inactief`);
    assert.ok(["4", "5"].includes(r!.nivo), `${soort}: ${v.rgs} is geen boekbaar niveau`);
    // W = winst-en-verlies (omzet of kosten), B = balans
    if (v.rgs.startsWith("W")) assert.ok(["revenue", "expenses", "direct_costs", "other_income_expenses"].includes(v.accountType), soort);
    else assert.ok(["current_assets", "current_liabilities"].includes(v.accountType), soort);
    if (v.rgs.startsWith("WOmz")) assert.equal(v.accountType, "revenue", soort);
  }
});
