// Affiliate-commissie in het memoriaal (ontwerp-affiliate.md, eisen c, d, e).
import { test } from "node:test";
import assert from "node:assert/strict";
import { maakMemoriaal, SOORTEN, type AfrekeningInvoer, type Koppeling } from "../src/moneybird/memoriaal.ts";
import { MoneybirdFout } from "../src/moneybird/fouten.ts";
import { RGS_PER_SOORT } from "../src/moneybird/rgs.ts";

const S = "7300000000000000001";
const invoer = (regels: Array<[any, number]>): AfrekeningInvoer => ({ statementId: S, statementTime: 1794312000, valuta: "EUR", regels: regels.map(([soort, bedragCenten]) => ({ soort, bedragCenten, statementId: S })) });
const basis: Koppeling = { per: { omzet: { grootboekId: "100" }, commissie: { grootboekId: "300" } }, tegenrekeningId: "500" };

test("(c) affiliate-regel met eigen omschrijving, direct na de commissieregel", () => {
  const k: Koppeling = { ...basis, per: { ...basis.per, affiliate: { grootboekId: "310" } } };
  const m = maakMemoriaal(invoer([["omzet", 5000], ["affiliate", -300], ["commissie", -400]]), k);
  assert.deepEqual(m.regels.map((r) => [r.grootboekId, r.debetCenten, r.creditCenten, r.omschrijving]), [
    ["100", 0, 5000, `TikTok Shop omzet, afrekening ${S}`],
    ["300", 400, 0, `TikTok Shop commissie en kosten, afrekening ${S}`],
    ["310", 300, 0, `TikTok Shop affiliate-commissie (creators), afrekening ${S}`],
    ["500", 4300, 0, `TikTok Shop te ontvangen, afrekening ${S}`],
  ]);
  const i = SOORTEN.findIndex(([s]) => s === "commissie");
  assert.equal(SOORTEN[i + 1][0], "affiliate");
});

test("(d) zonder eigen rekening: terug op de commissierekening, zonder het btw-tarief van de commissie", () => {
  const m = maakMemoriaal(invoer([["omzet", 5000], ["affiliate", -300]]), basis);
  assert.deepEqual(m.regels[1], { grootboekId: "300", debetCenten: 300, creditCenten: 0, omschrijving: `TikTok Shop affiliate-commissie (creators), afrekening ${S}` });
  const metBtw: Koppeling = { ...basis, per: { ...basis.per, commissie: { grootboekId: "300", btwTariefId: "777" } } };
  const m2 = maakMemoriaal(invoer([["omzet", 5000], ["commissie", -400], ["affiliate", -300]]), metBtw, { btwToegestaan: true });
  assert.equal(m2.regels[1].btwTariefId, "777");
  assert.equal(m2.regels[2].btwTariefId, undefined);
  const e2 = m2.body.general_journal_document.general_journal_document_entries_attributes as any[];
  assert.equal("tax_rate_id" in e2[2], false);
});

test("(d) zonder rekening voor commissie en affiliate: de fout noemt de affiliate-commissie", () => {
  const k: Koppeling = { per: { omzet: { grootboekId: "100" } }, tegenrekeningId: "500" };
  assert.throws(() => maakMemoriaal(invoer([["omzet", 5000], ["affiliate", -300]]), k),
    (e: unknown) => e instanceof MoneybirdFout && e.message.includes("affiliate-commissie (creators)"));
});

test("(e) RGS-voorstel voor affiliate: WBedVkkCom, eigen naam, zoeken op naam", () => {
  assert.deepEqual(RGS_PER_SOORT.affiliate, { rgs: "WBedVkkCom", accountType: "expenses", naam: "Affiliate-commissie TikTok Shop (creators)", aanmaken: true, zoekOpNaam: true });
  assert.notEqual(RGS_PER_SOORT.affiliate.naam, RGS_PER_SOORT.commissie.naam);
});
