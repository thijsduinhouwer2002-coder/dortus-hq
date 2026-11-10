// Minder bewaren (punt 3 van ontwerp-d1-worker.md, vondst controleur 10 nov): alleen de velden die samenstel en
// boekingsregels gebruiken, geen productnamen. Dezelfde uitkomst met en zonder de weggelaten velden.
import { test } from "node:test";
import assert from "node:assert/strict";
import { TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { boekingsregels } from "../../tiktok-shop-basis/src/boekingen.ts";
import { Budget } from "../src/budget.ts";
import { haalSamen, type TikTokDeps } from "../src/verwerk.ts";
import { stelSamen } from "../src/samenstel.ts";
import { BESTELLING, KOP, SKU, TRANSACTIE, slankeBestelling, slankeKop, slankeTransacties } from "../src/slank.ts";
import { D1ToetsOpslag } from "./d1-toets-opslag.ts";
import { readFileSync } from "node:fs";

const voorbeeld = (naam: string): any => JSON.parse(readFileSync(new URL(`../../tiktok-shop-basis/test/voorbeelden/${naam}`, import.meta.url), "utf8"));

const PRIVE = ["sku_name", "product_name", "buyer_note", "sku_image"];

/** Docs-voorbeeld plus velden die we nooit willen bewaren, ook op plekken die we niet kennen. */
function volleBestelling(): any {
  const b = structuredClone(voorbeeld("get-transactions-by-order-202501.json").data);
  b.buyer_note = "graag snel";
  for (const s of b.sku_transactions) s.sku_image = "https://voorbeeld/plaatje.png";
  return b;
}

test("slank: bestelling zonder productnaam, SKU-naam en onbekende velden, uitsplitsingen heel", () => {
  const vol = volleBestelling();
  const slank = slankeBestelling(vol);
  const tekst = JSON.stringify(slank);
  for (const v of PRIVE) assert.ok(!tekst.includes(`"${v}"`), `${v} hoort er niet in`);
  // Het docs-voorbeeld heeft deze echt (anders toetst dit niets).
  assert.ok(JSON.stringify(vol).includes('"product_name"') && JSON.stringify(vol).includes('"sku_name"'));
  assert.deepEqual(slank.sku_transactions[0].revenue_breakdown, vol.sku_transactions[0].revenue_breakdown);
  assert.deepEqual(slank.sku_transactions[0].fee_tax_breakdown, vol.sku_transactions[0].fee_tax_breakdown);
  assert.deepEqual(slank.sku_transactions[0].shipping_cost_breakdown, vol.sku_transactions[0].shipping_cost_breakdown);
  // Het origineel blijft ongemoeid.
  assert.equal(vol.sku_transactions[0].product_name, "Test Product name");
});

test("slank: boekingsregels geven precies hetzelfde met en zonder de weggelaten velden", () => {
  const vol = volleBestelling();
  assert.deepEqual(boekingsregels(slankeBestelling(vol)), boekingsregels(vol));
  // Ook als er iets mis is (geen lijst, regel zonder statement_id, geen munt): zelfde waarschuwing of fout.
  const zonderId = volleBestelling();
  delete zonderId.sku_transactions[0].statement_id;
  assert.deepEqual(boekingsregels(slankeBestelling(zonderId)), boekingsregels(zonderId));
  const geenMunt = volleBestelling();
  delete geenMunt.currency;
  assert.throws(() => boekingsregels(slankeBestelling(geenMunt)), (e: Error) => { assert.throws(() => boekingsregels(geenMunt), { message: e.message }); return true; });
  const geenLijst = { order_id: "1", currency: "EUR", sku_transactions: "kapot" } as any;
  assert.equal(slankeBestelling(geenLijst).sku_transactions, "kapot");
});

test("slank: samenstellen geeft hetzelfde tot en met compleet, ook met RESERVE, aanpassing en extra velden", () => {
  // Eigen EUR-afrekening (de docs-afrekening is GBP en stopt meteen): één bestelling, een reservering en een aanpassing.
  const statementId = "7001";
  const b = volleBestelling();
  b.order_id = "5001";
  b.currency = "EUR";
  for (const s of b.sku_transactions) s.statement_id = statementId;
  const transactions: any[] = [
    { id: "t1", type: "ORDER", order_id: "5001", settlement_amount: b.settlement_amount, buyer_note: "x" },
    { id: "t2", type: "RESERVE", settlement_amount: "", reserve_amount: "-2", reserve_id: "r9", reserve_status: "x" },
    { id: "t3", type: "SHIPPING_FEE_ADJUSTMENT", settlement_amount: "", adjustment_amount: "-5" },
  ];
  const totaal = String(Number(b.settlement_amount) - 2 - 5);
  const kopVol: any = { id: statementId, create_time: 1, status: "SETTLED", currency: "EUR", payable_amount: totaal, total_settlement_amount: totaal, total_count: 3, verkoper_naam: "Winkel BV" };
  const best = new Map<string, any>([["5001", b]]);
  const slankBest = new Map([...best].map(([k, x]) => [k, slankeBestelling(x)]));
  const kop = slankeKop(kopVol)!;
  const trans = slankeTransacties(transactions);
  const tekst = JSON.stringify({ kop, trans });
  for (const v of ["verkoper_naam", "buyer_note", "reserve_id", "reserve_status"]) assert.ok(!tekst.includes(v), `${v} hoort er niet in`);
  const vol = stelSamen(statementId, kopVol, transactions, best);
  assert.equal(vol.status, "compleet", JSON.stringify(vol));
  assert.deepEqual(stelSamen(statementId, kop, trans, slankBest), vol);
  assert.equal(slankeKop(undefined), undefined);
});

test("slank: in D1 staat na het ophalen geen productnaam of SKU-naam", async () => {
  const opslag = new D1ToetsOpslag();
  const b = volleBestelling();
  b.order_id = "5001";
  b.currency = "EUR";
  for (const s of b.sku_transactions) s.statement_id = "7001";
  // Kop en transactie met een onbekend veld; bedrag van de transactie gelijk aan de bestelling.
  const trans = [{ id: "t1", type: "ORDER", order_id: "5001", settlement_amount: b.settlement_amount, buyer_note: "x" }];
  const ok = (data: any) => new Response(JSON.stringify({ code: 0, message: "Success", request_id: "r", data }), { status: 200 });
  const fn = (async (input: any) => {
    const u = new URL(String(input));
    if (u.pathname.startsWith("/finance/202501/statements/")) return ok({ id: "7001", create_time: 1, status: "SETTLED", currency: "EUR", payable_amount: b.settlement_amount, total_settlement_amount: b.settlement_amount, total_count: 1, product_name: "x", transactions: trans });
    if (u.pathname.startsWith("/finance/202501/orders/")) return ok(b);
    throw new Error(`onverwacht ${u.pathname}`);
  }) as typeof fetch;
  const budget = new Budget(45);
  const tiktok = new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: budget.omhul(fn), nu: () => 1_800_000_000, slaap: async () => {} });
  const d: TikTokDeps = { tiktok, accessToken: "t", shopCipher: "c", opslag, budget, nu: () => 1_800_000_000 };
  const s = await haalSamen(d, "7001", { reserve: 0 });
  assert.equal(s.status, "compleet", JSON.stringify(s));
  await opslag.binnen.klaar();
  const rijen = [
    ...(opslag.db.sqlite.prepare("SELECT gegevens FROM bestellingen").all() as Array<{ gegevens: string }>),
    ...(opslag.db.sqlite.prepare("SELECT gegevens FROM transacties").all() as Array<{ gegevens: string }>),
  ];
  assert.equal(rijen.length, 2, "één bestelling en één transactielijst bewaard");
  for (const r of rijen) for (const v of PRIVE) assert.ok(!r.gegevens.includes(`"${v}"`), `${v} staat in D1`);
  // Tweede keer uit D1 (nieuwe opslag op dezelfde database, dus echt gelezen uit SQLite, zonder TikTok): zelfde uitkomst.
  const d2: TikTokDeps = { ...d, opslag: new D1ToetsOpslag(opslag.db), tiktok: new TikTokClient({ appKey: "k", appSecret: "s", fetchFn: (async () => { throw new Error("geen TikTok verwacht"); }) as typeof fetch, nu: () => 1_800_000_000, slaap: async () => {} }) };
  const opnieuw = await haalSamen(d2, "7001", { reserve: 0 });
  assert.deepEqual(opnieuw, s);
});

test("slank: elk TikTok-veld dat samenstel of boekingsregels noemt, staat in een lijst (anders valt het stil weg)", () => {
  const bron = ["../../tiktok-shop-basis/src/boekingen.ts", "../src/samenstel.ts"].map((f) => readFileSync(new URL(f, import.meta.url), "utf8")).join("\n");
  // Velden binnen de uitsplitsingen: die blijven heel, dus hoeven niet in een lijst.
  const binnenUitsplitsing = new Set(["subtotal_before_discount_amount", "seller_discount_amount", "refund_subtotal_before_discount_amount", "seller_discount_refund_amount", "supplementary_component"]);
  const lijsten = new Set<string>([...KOP, ...TRANSACTIE, ...BESTELLING, ...SKU, "sku_transactions"]);
  const tiktokAchtig = /(_amount|_id|_breakdown|_count|_transactions|_component|_time)$/;
  const namen = [...new Set(bron.match(/\b[a-z]+(?:_[a-z]+)+\b/g) ?? [])].filter((n) => tiktokAchtig.test(n));
  assert.ok(namen.length > 10, "grep vond te weinig, toets klopt niet meer");
  const mist = namen.filter((n) => !lijsten.has(n) && !binnenUitsplitsing.has(n));
  assert.deepEqual(mist, [], `nieuwe velden: zet ze in src/slank.ts of in binnenUitsplitsing`);
});
