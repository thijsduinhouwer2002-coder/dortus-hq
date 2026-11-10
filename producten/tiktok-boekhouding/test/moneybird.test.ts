import { test } from "node:test";
import assert from "node:assert/strict";
import { nepClient, nepFetch, voorbeeld } from "./hulp.ts";
import { maakMemoriaal, datumNL, tekstNaarCenten, type AfrekeningInvoer, type Koppeling } from "../src/moneybird/memoriaal.ts";
import { boekAfrekening } from "../src/moneybird/boeken.ts";
import { MoneybirdFout } from "../src/moneybird/fouten.ts";
import { wachttijdMs } from "../src/moneybird/client.ts";
import { administraties, grootboekrekeningen, btwTarieven, controleerKoppeling } from "../src/moneybird/lezen.ts";
import { inlogLink, wisselCode, ververs, trekIn } from "../src/moneybird/oauth.ts";
import { boekingsregels } from "../../tiktok-shop-basis/src/boekingen.ts";

const S = "7300000000000000001";
const T_10NOV = 1794312000; // 2026-11-10 12:00 UTC
const koppeling: Koppeling = {
  per: {
    omzet: { grootboekId: "100" }, korting: { grootboekId: "101" }, verzendkosten: { grootboekId: "200" },
    commissie: { grootboekId: "300" }, belasting_op_kosten: { grootboekId: "301" }, correctie: { grootboekId: "400" }, verschil: { grootboekId: "900" },
  },
  tegenrekeningId: "500",
};
const invoer = (regels: AfrekeningInvoer["regels"], extra: Partial<AfrekeningInvoer> = {}): AfrekeningInvoer => ({ statementId: S, statementTime: T_10NOV, valuta: "EUR", regels, ...extra });
const r = (soort: any, bedragCenten: number) => ({ soort, bedragCenten, statementId: S });
const ADM = { id: "123", periodLockedUntil: null };
const STANDAARD = invoer([r("omzet", 21000), r("omzet", 4000), r("korting", -1000), r("verzendkosten", -700), r("commissie", -2150), r("correctie", 0), r("verschil", 5)]);

test("(a) memoriaal: één regel per soort, tekstbedragen, credit/debet, tegenrekening, letterlijke body", () => {
  const m = maakMemoriaal(STANDAARD, koppeling);
  assert.deepEqual(m.body, {
    general_journal_document: {
      reference: `TikTokShop-${S}`,
      date: "2026-11-10",
      general_journal_document_entries_attributes: [
        { ledger_account_id: "100", debit: "0.00", credit: "250.00", description: `TikTok Shop omzet, afrekening ${S}`, row_order: 1 },
        { ledger_account_id: "101", debit: "10.00", credit: "0.00", description: `TikTok Shop korting van de winkel, afrekening ${S}`, row_order: 2 },
        { ledger_account_id: "200", debit: "7.00", credit: "0.00", description: `TikTok Shop verzendkosten, afrekening ${S}`, row_order: 3 },
        { ledger_account_id: "300", debit: "21.50", credit: "0.00", description: `TikTok Shop commissie en kosten, afrekening ${S}`, row_order: 4 },
        { ledger_account_id: "900", debit: "0.00", credit: "0.05", description: `TikTok Shop verschil, apart gezet, afrekening ${S}`, row_order: 5 },
        { ledger_account_id: "500", debit: "211.55", credit: "0.00", description: `TikTok Shop te ontvangen, afrekening ${S}`, row_order: 6 },
      ],
    },
  });
  const debet = m.regels.reduce((a, x) => a + x.debetCenten, 0), credit = m.regels.reduce((a, x) => a + x.creditCenten, 0);
  assert.equal(debet, credit);
  assert.equal(m.totaalCenten, 21155);
  assert.deepEqual(m.waarschuwingen, []);
});

test("(a) negatief totaal zet de tegenrekening op credit; totaal 0 geeft geen tegenregel", () => {
  const neg = maakMemoriaal(invoer([r("correctie", -1234)]), koppeling);
  assert.deepEqual(neg.regels.at(-1), { grootboekId: "500", debetCenten: 0, creditCenten: 1234, omschrijving: `TikTok Shop te ontvangen, afrekening ${S}` });
  const nul = maakMemoriaal(invoer([r("omzet", 500), r("korting", -500)]), koppeling);
  assert.equal(nul.regels.length, 2);
  assert.ok(nul.regels.every((x) => x.grootboekId !== "500"));
  assert.equal(maakMemoriaal(invoer([r("omzet", 0)]), koppeling).regels.length, 0);
});

test("(a) datum in Nederlandse tijd, ook bij de jaarwisseling", () => {
  assert.equal(datumNL(Date.UTC(2026, 11, 31, 23, 30) / 1000), "2027-01-01");
  assert.equal(datumNL(Date.UTC(2026, 6, 31, 22, 30) / 1000), "2026-08-01"); // zomertijd +2
  assert.equal(datumNL(Date.UTC(2026, 6, 31, 21, 30) / 1000), "2026-07-31");
});

test("(b) invoerfouten geven een fout zonder enig verzoek", async () => {
  const gevallen: Array<[AfrekeningInvoer, Koppeling, string, any?]> = [
    [invoer([r("belasting", -100)]), koppeling, "instelling"],
    [STANDAARD, { ...koppeling, tegenrekeningId: "" }, "instelling"],
    [invoer([r("omzet", 100)], { valuta: "GBP" }), koppeling, "invoer"],
    [invoer([{ soort: "omzet", bedragCenten: 100, statementId: "999" }]), koppeling, "invoer"],
    [invoer([r("omzet", 100)]), { ...koppeling, per: { ...koppeling.per, omzet: { grootboekId: "100", btwTariefId: "7" } } }, "btw_nog_niet_getest"],
  ];
  for (const [inv, k, soort] of gevallen) {
    const { client, verzoeken } = nepClient([{ json: [] }]);
    await assert.rejects(boekAfrekening(client, ADM, inv, k), (e: any) => e instanceof MoneybirdFout && e.soort === soort);
    assert.equal(verzoeken.length, 0);
  }
  // met de vlag mag het btw-tarief mee
  const m = maakMemoriaal(invoer([r("omzet", 100)]), { ...koppeling, per: { omzet: { grootboekId: "100", btwTariefId: "7" } } }, { btwToegestaan: true });
  assert.equal(m.body.general_journal_document.general_journal_document_entries_attributes[0].tax_rate_id, "7");
});

test("(b) afgesloten periode: fout zonder schrijven, maar een gelijke boeking blijft ongewijzigd", async () => {
  const dicht = { id: "123", periodLockedUntil: "2026-11-10" };
  const a = nepClient([{ json: [] }]);
  await assert.rejects(boekAfrekening(a.client, dicht, STANDAARD, koppeling), (e: any) => e.soort === "periode_afgesloten");
  assert.deepEqual(a.verzoeken.map((v) => v.method), ["GET"]);
  const doc = alsDocument(STANDAARD);
  const b = nepClient([{ json: [doc] }]);
  assert.equal((await boekAfrekening(b.client, dicht, STANDAARD, koppeling)).uitkomst, "ongewijzigd");
  // 422 in_locked_period van Moneybird zelf
  const c = nepClient([{ json: [] }, { status: 422, json: { error: "in locked period", symbolic: { id: "in_locked_period" } } }]);
  await assert.rejects(boekAfrekening(c.client, ADM, STANDAARD, koppeling), (e: any) => e.soort === "periode_afgesloten");
});

const mbBedrag = (c: number) => { const s = (c / 100).toString(); return s.includes(".") ? s : `${s}.0`; };

/** Zoals Moneybird een geboekt document teruggeeft: bedragen als "100.0", id's als tekst. */
function alsDocument(inv: AfrekeningInvoer, id = "503332872610907545") {
  const m = maakMemoriaal(inv, koppeling);
  return {
    id, administration_id: 123, reference: m.kenmerk, date: m.datum,
    general_journal_document_entries: m.regels.map((x, i) => ({ id: String(600 + i), ledger_account_id: x.grootboekId, debit: mbBedrag(x.debetCenten), credit: mbBedrag(x.creditCenten), description: x.omschrijving, row_order: i + 1 })),
  };
}

test("(c) niets gevonden: zoeken op kenmerk en één POST met de body; id uit het docs-antwoord", async () => {
  const { client, verzoeken } = nepClient([{ json: [] }, { status: 201, json: voorbeeld("gjd-post-201") }]);
  const res = await boekAfrekening(client, ADM, STANDAARD, koppeling);
  assert.deepEqual(res, { uitkomst: "aangemaakt", id: "503332872610907545", waarschuwingen: [] });
  assert.equal(verzoeken[0].url.pathname, "/api/v2/123/documents/general_journal_documents.json");
  assert.equal(verzoeken[0].url.searchParams.get("filter"), `reference:TikTokShop-${S}`);
  assert.equal(verzoeken[0].headers.authorization, "Bearer tok");
  assert.equal(verzoeken[1].method, "POST");
  assert.deepEqual(JSON.parse(verzoeken[1].body!), maakMemoriaal(STANDAARD, koppeling).body);
});

test("(c) gevonden en gelijk (bedragen als \"100.0\"): geen schrijfactie", async () => {
  const doc = alsDocument(STANDAARD);
  assert.equal(doc.general_journal_document_entries[0].credit, "250.0");
  const { client, verzoeken } = nepClient([{ json: [doc] }]);
  const res = await boekAfrekening(client, ADM, STANDAARD, koppeling);
  assert.equal(res.uitkomst, "ongewijzigd");
  assert.deepEqual(verzoeken.map((v) => v.method), ["GET"]);
});

test("(c) gevonden en anders: één PATCH met _destroy voor elk oud regel-id plus de nieuwe regels", async () => {
  const doc = alsDocument(invoer([r("omzet", 21000)]));
  const { client, verzoeken } = nepClient([{ json: [doc] }, { json: doc }]);
  const res = await boekAfrekening(client, ADM, STANDAARD, koppeling);
  assert.equal(res.uitkomst, "vervangen");
  assert.equal(verzoeken[1].method, "PATCH");
  assert.equal(verzoeken[1].url.pathname, `/api/v2/123/documents/general_journal_documents/${doc.id}.json`);
  const e = JSON.parse(verzoeken[1].body!).general_journal_document.general_journal_document_entries_attributes;
  assert.deepEqual(e.slice(0, 2), [{ id: "600", _destroy: true }, { id: "601", _destroy: true }]);
  assert.deepEqual(e.slice(2), maakMemoriaal(STANDAARD, koppeling).body.general_journal_document.general_journal_document_entries_attributes);
});

test("(c) twee met hetzelfde kenmerk: dubbel zonder schrijven; ander kenmerk (deel-tekst) telt niet mee", async () => {
  const doc = alsDocument(STANDAARD);
  const a = nepClient([{ json: [doc, { ...doc, id: "2" }] }]);
  await assert.rejects(boekAfrekening(a.client, ADM, STANDAARD, koppeling), (e: any) => e.soort === "dubbel");
  assert.equal(a.verzoeken.length, 1);
  const b = nepClient([{ json: [{ ...doc, reference: `TikTokShop-${S}0` }] }, { status: 201, json: { id: "77" } }]);
  assert.equal((await boekAfrekening(b.client, ADM, STANDAARD, koppeling)).uitkomst, "aangemaakt");
});

test("(c) bekendId: eerst GET op dat id; bij 404 terug naar zoeken op kenmerk", async () => {
  const doc = alsDocument(STANDAARD, "42");
  const a = nepClient([{ json: doc }]);
  assert.equal((await boekAfrekening(a.client, ADM, STANDAARD, koppeling, { bekendId: "42" })).uitkomst, "ongewijzigd");
  assert.equal(a.verzoeken[0].url.pathname, "/api/v2/123/documents/general_journal_documents/42.json");
  const b = nepClient([{ status: 404, json: { error: "not found" } }, { json: [] }, { status: 201, json: { id: "43" } }]);
  const res = await boekAfrekening(b.client, ADM, STANDAARD, koppeling, { bekendId: "42" });
  assert.deepEqual([res.uitkomst, res.id], ["aangemaakt", "43"]);
  assert.deepEqual(b.verzoeken.map((v) => v.method), ["GET", "GET", "POST"]);
});

test("(c) alles 0: geen POST; met bestaande boeking leeg_maar_geboekt zonder schrijven", async () => {
  const leeg = invoer([r("omzet", 0)]);
  const a = nepClient([{ json: [] }]);
  assert.equal((await boekAfrekening(a.client, ADM, leeg, koppeling)).uitkomst, "leeg");
  const b = nepClient([{ json: [alsDocument(STANDAARD)] }]);
  assert.equal((await boekAfrekening(b.client, ADM, leeg, koppeling)).uitkomst, "leeg_maar_geboekt");
  assert.equal(b.verzoeken.length, 1);
});

test("(d) GET met 500 wordt herhaald, POST en PATCH met 500 of netwerkfout niet en geven onzeker", async () => {
  const a = nepClient([{ status: 500 }, { status: 502 }, { json: [] }, { status: 500, json: { error: "x" } }]);
  const res = await boekAfrekening(a.client, ADM, STANDAARD, koppeling);
  assert.equal(res.uitkomst, "onzeker");
  assert.deepEqual(a.verzoeken.map((v) => v.method), ["GET", "GET", "GET", "POST"]);
  assert.deepEqual(a.slapen, [1000, 2000]);
  const b = nepClient([{ json: [alsDocument(invoer([r("omzet", 1)]))] }, { fout: new Error("verbinding weg") }]);
  const rb = await boekAfrekening(b.client, ADM, STANDAARD, koppeling);
  assert.equal(rb.uitkomst, "onzeker");
  assert.equal(b.verzoeken.length, 2);
  const c = nepClient([{ status: 500 }]);
  await assert.rejects(c.client.roep("GET", "/123/tax_rates"), (e: any) => e.soort === "server");
  assert.equal(c.verzoeken.length, 3);
});

test("(d) 429 wordt herhaald, ook bij POST; Retry-After als tijdstip of seconden, tussen 1 en 60 s", async () => {
  const nu = 1_800_000_000;
  const { client, verzoeken, slapen } = nepClient([{ json: [] }, { status: 429, headers: { "retry-after": String(nu + 7) } }, { status: 201, json: { id: "9" } }], nu);
  assert.equal((await boekAfrekening(client, ADM, STANDAARD, koppeling)).uitkomst, "aangemaakt");
  assert.deepEqual(verzoeken.map((v) => v.method), ["GET", "POST", "POST"]);
  assert.deepEqual(slapen, [7000]);
  assert.equal(wachttijdMs("5", nu), 5000);
  assert.equal(wachttijdMs(String(nu + 600), nu), 60000);
  assert.equal(wachttijdMs(String(nu - 3), nu), 1000);
  assert.equal(wachttijdMs(null, nu), 5000);
});

test("(e) foutsoorten: 401, 402, 403, 422 met tekst", async () => {
  for (const [status, soort] of [[401, "koppeling_verlopen"], [402, "geen_abonnement"], [403, "geblokkeerd"], [404, "niet_gevonden"]] as const) {
    const { client } = nepClient([{ status, json: { error: "x" } }]);
    await assert.rejects(client.roep("GET", "/administrations"), (e: any) => e.soort === soort && e.httpStatus === status);
  }
  const { client } = nepClient([{ status: 422, json: { error: "Ledger account is not allowed", symbolic: { ledger_account_id: "invalid" } } }]);
  await assert.rejects(client.roep("POST", "/123/documents/general_journal_documents", { body: {} }), (e: any) => e.soort === "geweigerd" && e.message.includes("Ledger account is not allowed"));
});

test("(f) een gebruikt id als getal geeft een fout; administration_id als klein getal mag", async () => {
  // Gewijzigd na kan-punt 1 van de code-controleur: bij een id als getal in het 201-antwoord staat de boeking er
  // waarschijnlijk al, dus onzeker (met de fout erbij) in plaats van een gewone fout.
  const a = nepClient([{ json: [] }, { status: 201, json: { id: 503332872610907545 } }]);
  const ra = await boekAfrekening(a.client, ADM, STANDAARD, koppeling);
  assert.equal(ra.uitkomst, "onzeker");
  assert.equal(ra.fout?.soort, "antwoord");
  const doc = alsDocument(STANDAARD);
  (doc.general_journal_document_entries[0] as any).ledger_account_id = 100;
  const b = nepClient([{ json: [doc] }]);
  await assert.rejects(boekAfrekening(b.client, ADM, STANDAARD, koppeling), (e: any) => e.soort === "antwoord");
  const c = nepClient([{ json: voorbeeld("administrations-get") }]);
  const lijst = await administraties(c.client);
  assert.deepEqual(lijst.map((x) => x.id), ["179423564548016036", "123"]);
  assert.equal(lijst[1].periodLockedUntil, null);
});

test("(g) OAuth: inloglink, code inwisselen en verversen form-encoded", async () => {
  const app = { clientId: "cid", clientSecret: "geheim", redirectUri: "https://dortus.com/tiktok-boekhouding/moneybird" };
  const u = new URL(inlogLink(app, "st8"));
  assert.equal(u.origin + u.pathname, "https://moneybird.com/oauth/authorize");
  assert.deepEqual(Object.fromEntries(u.searchParams), { client_id: "cid", redirect_uri: app.redirectUri, response_type: "code", scope: "documents settings", state: "st8" });
  const antwoord = { access_token: "b3f3", token_type: "bearer", refresh_token: "9ef3", scope: "documents", created_at: 1471524338 };
  const nep = nepFetch([{ json: antwoord }, { json: { ...antwoord, expires_in: 3600 } }]);
  const t = await wisselCode(app, "1192", nep.fn);
  assert.deepEqual(t, { accessToken: "b3f3", refreshToken: "9ef3", scope: "documents" });
  assert.equal(nep.verzoeken[0].url.href, "https://moneybird.com/oauth/token");
  assert.equal(nep.verzoeken[0].headers["content-type"], "application/x-www-form-urlencoded");
  assert.deepEqual(Object.fromEntries(new URLSearchParams(nep.verzoeken[0].body)), { client_id: "cid", client_secret: "geheim", code: "1192", redirect_uri: app.redirectUri, grant_type: "authorization_code" });
  const t2 = await ververs(app, "9ef3", nep.fn);
  assert.equal(t2.verlooptOp, 1471524338 + 3600);
  assert.deepEqual(Object.fromEntries(new URLSearchParams(nep.verzoeken[1].body)), { client_id: "cid", client_secret: "geheim", grant_type: "refresh_token", refresh_token: "9ef3" });
  const fout = nepFetch([{ status: 401, json: { error: "invalid_grant", error_description: "The provided authorization grant is invalid" } }]);
  await assert.rejects(ververs(app, "x", fout.fn), /invalid/);
});

test("(h) lijsten met de docs-voorbeelden; grootboek in één verzoek; btw met filter", async () => {
  const a = nepClient([{ json: voorbeeld("ledger-accounts-get") }]);
  const rek = await grootboekrekeningen(a.client, "123");
  assert.equal(rek.length, 30);
  assert.equal(a.verzoeken.length, 1);
  assert.equal(a.verzoeken[0].url.search, "");
  const b = nepClient([{ json: voorbeeld("tax-rates-get") }]);
  const btw = await btwTarieven(b.client, "123");
  assert.equal(b.verzoeken[0].url.searchParams.get("filter"), "tax_rate_type:general_journal_document,active:true");
  assert.deepEqual(btw[0], { id: "503332790641624203", naam: "21% btw", percentage: "21.0" });
});

test("(h) controleerKoppeling keurt verkeerde rekeningen af", async () => {
  const a = nepClient([{ json: voorbeeld("ledger-accounts-get") }]);
  const rek = await grootboekrekeningen(a.client, "123");
  const id = (naam: string) => rek.find((x) => x.naam === naam)!.id;
  const goed: Koppeling = { per: { omzet: { grootboekId: id("Omzet") }, commissie: { grootboekId: id("Verkoopkosten") } }, tegenrekeningId: id("Overige vorderingen") };
  assert.deepEqual(controleerKoppeling(goed, rek), []);
  const kapot = rek.map((x) => (x.naam === "Verkoopkosten" ? { ...x, toegestaan: ["purchase_invoice"] } : x));
  const fout = controleerKoppeling({ ...goed, tegenrekeningId: id("Crediteuren"), per: { ...goed.per, verschil: { grootboekId: "1" } } }, kapot);
  assert.equal(fout.length, 3);
  assert.ok(fout.some((f) => f.includes("mag niet in een memoriaalboeking")));
  assert.ok(fout.some((f) => f.includes("geen vlottende activa")));
  assert.ok(fout.some((f) => f.includes("bestaat niet")));
});

test("(i) uitbetaald wijkt af: wel geboekt, waarschuwing met beide bedragen", async () => {
  const { client } = nepClient([{ json: [] }, { status: 201, json: { id: "5" } }]);
  const res = await boekAfrekening(client, ADM, { ...STANDAARD, uitbetaaldCenten: 21000 }, koppeling);
  assert.equal(res.uitkomst, "aangemaakt");
  assert.deepEqual(res.waarschuwingen, ["Uitbetaald 210.00 EUR, geboekt 211.55 EUR: verschil -1.55 EUR wordt niet geboekt."]);
});

test("aansluiting op de rekenkern: regels van boekingsregels() gaan zo door", () => {
  const bestelling: any = {
    order_id: "576", currency: "EUR", settlement_amount: "18.5",
    sku_transactions: [{ sku_id: "1", statement_id: S, settlement_amount: "18.5", revenue_amount: "25", revenue_breakdown: { subtotal_before_discount_amount: "25" },
      shipping_cost_amount: "-4", shipping_cost_breakdown: { actual_shipping_fee_amount: "-4" }, fee_tax_amount: "-2.5", fee_tax_breakdown: { fee: { platform_commission_amount: "-2.5" }, tax: {} } }],
  };
  const b = boekingsregels(bestelling);
  assert.deepEqual(b.waarschuwingen, []);
  const m = maakMemoriaal(invoer(b.regels.map((x) => ({ soort: x.soort, bedragCenten: x.bedragCenten, statementId: x.statementId }))), koppeling);
  assert.equal(m.totaalCenten, 1850);
  assert.equal(tekstNaarCenten("18,5"), 1850);
  assert.throws(() => tekstNaarCenten("1.234"));
});

test("controleur ronde 1: 201 met onleesbaar antwoord geeft onzeker, ook bij PATCH", async () => {
  const nep = nepFetch([{ json: [] }]);
  let i = 0;
  const fn = (async (u: any, init: any) => {
    i++;
    if (i === 1) return nep.fn(u, init);
    return new Response("<html>", { status: 201 });
  }) as typeof fetch;
  const { MoneybirdClient } = await import("../src/moneybird/client.ts");
  const client = new MoneybirdClient({ accessToken: "tok", fetchFn: fn, slaap: async () => {} });
  const res = await boekAfrekening(client, ADM, STANDAARD, koppeling);
  assert.equal(res.uitkomst, "onzeker");
  assert.equal(res.fout?.soort, "server");
  assert.equal(i, 2);
  const b = nepClient([{ json: [alsDocument(invoer([r("omzet", 1)]))] }, { status: 503, json: { error: "down" } }]);
  assert.equal((await boekAfrekening(b.client, ADM, STANDAARD, koppeling)).uitkomst, "onzeker");
  assert.equal(b.verzoeken.length, 2);
});

test("controleur ronde 1: 422 met error als object en 400 geven leesbare tekst", async () => {
  const a = nepClient([{ status: 422, json: { error: { debit: ["is not valid"] } } }]);
  await assert.rejects(a.client.roep("POST", "/123/x", { body: {} }), (e: any) => e.soort === "geweigerd" && e.message.includes('"debit":["is not valid"]') && !e.message.includes("[object Object]"));
  const b = nepClient([{ status: 400, json: { error: "General Journal Document is required", symbolic: { general_journal_document: "required" } } }]);
  await assert.rejects(b.client.roep("POST", "/123/x", { body: {} }), (e: any) => e.soort === "geweigerd" && e.message.includes("is required"));
});

test("controleur ronde 1: bekendId met een ander kenmerk wordt niet vervangen maar valt terug op zoeken", async () => {
  const ander = { ...alsDocument(STANDAARD, "42"), reference: "TikTokShop-999" };
  const { client, verzoeken } = nepClient([{ json: ander }, { json: [] }, { status: 201, json: { id: "43" } }]);
  const res = await boekAfrekening(client, ADM, STANDAARD, koppeling, { bekendId: "42" });
  assert.deepEqual([res.uitkomst, res.id], ["aangemaakt", "43"]);
  assert.deepEqual(verzoeken.map((v) => v.method), ["GET", "GET", "POST"]);
});

test("controleur ronde 1: zelfde aantal regels maar 1 cent, rekening, omschrijving of datum anders geeft PATCH", async () => {
  const aanpassingen: Array<(d: any) => void> = [
    (d) => { d.general_journal_document_entries[0].credit = "250.01"; },
    (d) => { d.general_journal_document_entries[1].ledger_account_id = "999"; },
    (d) => { d.general_journal_document_entries[2].description = "met de hand aangepast"; },
    (d) => { d.general_journal_document_entries[5].debit = "211.56"; },
    (d) => { d.date = "2026-11-11"; },
  ];
  for (const pas of aanpassingen) {
    const doc = alsDocument(STANDAARD);
    pas(doc);
    const { client, verzoeken } = nepClient([{ json: [doc] }, { json: doc }]);
    assert.equal((await boekAfrekening(client, ADM, STANDAARD, koppeling)).uitkomst, "vervangen");
    assert.equal(verzoeken[1].method, "PATCH");
  }
  // volgorde volgens row_order, niet volgens het antwoord
  const doc = alsDocument(STANDAARD);
  doc.general_journal_document_entries.reverse();
  const { client } = nepClient([{ json: [doc] }]);
  assert.equal((await boekAfrekening(client, ADM, STANDAARD, koppeling)).uitkomst, "ongewijzigd");
});

test("controleur ronde 1: tijd in milliseconden, munt per regel en id's uit letters geven een invoer- of instellingfout", () => {
  assert.throws(() => maakMemoriaal(invoer([r("omzet", 100)], { statementTime: T_10NOV * 1000 }), koppeling), (e: any) => e.soort === "invoer");
  assert.throws(() => maakMemoriaal(invoer([{ ...r("omzet", 100), valuta: "GBP" }]), koppeling), (e: any) => e.soort === "invoer");
  assert.doesNotThrow(() => maakMemoriaal(invoer([{ ...r("omzet", 100), valuta: "EUR" }]), koppeling));
  assert.throws(() => maakMemoriaal(invoer([r("omzet", 100)]), { ...koppeling, per: { omzet: { grootboekId: "omzet" } } }), (e: any) => e.soort === "instelling");
  assert.throws(() => maakMemoriaal(invoer([r("omzet", 100)]), { ...koppeling, tegenrekeningId: "abc" }), (e: any) => e.soort === "instelling");
  assert.throws(() => tekstNaarCenten(100 as any));
});

test("OAuth: intrekken stuurt token en app-gegevens", async () => {
  const app = { clientId: "cid", clientSecret: "geheim", redirectUri: "https://x" };
  const nep = nepFetch([{ json: {} }, { status: 403, json: { error: "unauthorized_client" } }]);
  await trekIn(app, "b3f3", nep.fn);
  assert.equal(nep.verzoeken[0].url.href, "https://moneybird.com/oauth/revoke");
  assert.deepEqual(Object.fromEntries(new URLSearchParams(nep.verzoeken[0].body)), { client_id: "cid", client_secret: "geheim", token: "b3f3" });
  await assert.rejects(trekIn(app, "x", nep.fn), /403/);
});

test("controleur ronde 2: lege btwTariefId is geen btw; zoeken zonder lijst is een antwoordfout", async () => {
  const m = maakMemoriaal(invoer([r("omzet", 100)]), { ...koppeling, per: { omzet: { grootboekId: "100", btwTariefId: "" } } });
  assert.equal("tax_rate_id" in m.body.general_journal_document.general_journal_document_entries_attributes[0], false);
  const { client, verzoeken } = nepClient([{ json: { fout: "geen lijst" } }]);
  await assert.rejects(boekAfrekening(client, ADM, STANDAARD, koppeling), (e: any) => e.soort === "antwoord");
  assert.equal(verzoeken.length, 1);
});
