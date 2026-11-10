// Minder bewaren (punt 3 van ontwerp-d1-worker.md): van elk TikTok-antwoord houden we alleen de velden over die
// `samenstel` en `boekingsregels` lezen. Geen productnamen, geen SKU-namen, geen onbekende velden.
// We maken de antwoorden slank direct na het ophalen, dus rekenen en bewaren gebruiken precies dezelfde gegevens:
// wat na opslaan terugkomt kan nooit anders uitvallen dan wat vers is opgehaald.
// Uitsplitsingen (revenue_breakdown, shipping_cost_breakdown, fee_tax_breakdown) blijven heel: `boekingsregels` telt
// elk veld daarin mee als bedrag, ook velden die we niet kennen, en ze bevatten alleen bedragen.

import type { AfrekeningKop, BestellingTransacties, SkuTransactie, Transactie } from "../../tiktok-shop-basis/src/endpoints.ts";

const KOP = ["id", "create_time", "status", "currency", "payable_amount", "total_settlement_amount", "total_count"] as const;
const TRANSACTIE = ["id", "type", "order_id", "order_create_time", "settlement_amount", "revenue_amount", "shipping_cost_amount", "fee_tax_amount", "adjustment_amount"] as const;
const BESTELLING = ["order_id", "order_create_time", "currency", "revenue_amount", "fee_and_tax_amount", "shipping_cost_amount", "settlement_amount", "total_count"] as const;
const SKU = ["sku_id", "statement_id", "quantity", "settlement_amount", "revenue_amount", "revenue_breakdown", "shipping_cost_amount", "shipping_cost_breakdown", "fee_tax_amount", "fee_tax_breakdown"] as const;

function kies<T>(bron: unknown, velden: readonly string[]): T {
  // Geen object (bijv. null of een lijst): ongewijzigd doorgeven, dan geven de controles verderop dezelfde melding.
  if (bron === null || typeof bron !== "object" || Array.isArray(bron)) return bron as T;
  const b = bron as Record<string, unknown>;
  const uit: Record<string, unknown> = {};
  for (const v of velden) if (Object.prototype.hasOwnProperty.call(b, v)) uit[v] = b[v];
  return uit as T;
}

export function slankeKop(kop: AfrekeningKop | undefined): AfrekeningKop | undefined {
  return kop === undefined ? undefined : kies<AfrekeningKop>(kop, KOP);
}

export function slankeTransacties(t: Transactie[]): Transactie[] {
  return Array.isArray(t) ? t.map((x) => kies<Transactie>(x, TRANSACTIE)) : t;
}

export function slankeBestelling(b: BestellingTransacties): BestellingTransacties {
  if (b === null || typeof b !== "object" || Array.isArray(b)) return b;
  const uit = kies<BestellingTransacties>(b, BESTELLING);
  // sku_transactions altijd overnemen zoals het was (ook als het geen lijst is), alleen de regels zelf slank maken.
  if (Object.prototype.hasOwnProperty.call(b, "sku_transactions")) {
    uit.sku_transactions = Array.isArray(b.sku_transactions) ? b.sku_transactions.map((s) => kies<SkuTransactie>(s, SKU)) : b.sku_transactions;
  }
  return uit;
}
