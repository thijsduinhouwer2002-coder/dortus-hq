// De drie endpoints die de basis nu kent. Velden heten zoals bij TikTok;
// bedragen blijven tekst (zie bedrag.ts).
// Bronnen: get-authorized-shops-202309, get-statements-202309,
// get-transactions-by-statement-202501 op partner.tiktokshop.com/docv2/page/

import type { TikTokClient } from "./client.ts";
import { allePaginas } from "./paginate.ts";

export interface Winkel {
  id: string;
  name: string;
  region: string;
  seller_type: string;
  cipher: string;
  code: string;
}

export interface Afrekening {
  id: string;
  statement_time: number;
  settlement_amount: string;
  currency: string;
  revenue_amount?: string;
  fee_amount: string;
  adjustment_amount: string;
  payment_status: string;
  payment_id?: string;
  [veld: string]: unknown;
}

export interface Transactie {
  id: string;
  type: string;
  order_id?: string;
  order_create_time?: number;
  settlement_amount: string;
  revenue_amount?: string;
  shipping_cost_amount?: string;
  fee_tax_amount?: string;
  adjustment_amount?: string;
  [veld: string]: unknown;
}

export interface AfrekeningKop {
  id: string;
  create_time: number;
  status: string;
  currency: string;
  payable_amount: string;
  total_settlement_amount: string;
  total_count: number;
  [veld: string]: unknown;
}

export async function geautoriseerdeWinkels(c: TikTokClient, accessToken: string): Promise<Winkel[]> {
  const a = await c.roep<{ shops?: Winkel[] }>({ method: "GET", path: "/authorization/202309/shops", accessToken });
  return a.data?.shops ?? [];
}

export interface AfrekeningFilter {
  /** Unix-seconden, inclusief. */
  vanaf?: number;
  /** Unix-seconden, exclusief. */
  tot?: number;
  status?: "PAID" | "FAILED" | "PROCESSING";
  sortOrder?: "ASC" | "DESC";
  pageSize?: number;
}

export function afrekeningen(c: TikTokClient, accessToken: string, shopCipher: string, f: AfrekeningFilter = {}): AsyncGenerator<Afrekening> {
  return allePaginas<Afrekening>(async (pageToken) => {
    const a = await c.roep<{ statements?: Afrekening[]; next_page_token?: string }>({
      method: "GET",
      path: "/finance/202309/statements",
      accessToken,
      shopCipher,
      query: {
        sort_field: "statement_time", // verplicht, enige toegestane waarde
        sort_order: f.sortOrder,
        statement_time_ge: f.vanaf,
        statement_time_lt: f.tot,
        payment_status: f.status,
        page_size: f.pageSize ?? 100,
        page_token: pageToken,
      },
    });
    return { items: a.data?.statements ?? [], nextPageToken: a.data?.next_page_token };
  });
}

export interface TransactiesUitkomst {
  kop: AfrekeningKop | undefined;
  transacties: Transactie[];
}

export async function transactiesVanAfrekening(
  c: TikTokClient,
  accessToken: string,
  shopCipher: string,
  statementId: string,
): Promise<TransactiesUitkomst> {
  if (!/^\d+$/.test(statementId)) throw new Error(`ongeldig statement_id: "${statementId}"`);
  let kop: AfrekeningKop | undefined;
  const transacties: Transactie[] = [];
  const it = allePaginas<Transactie>(async (pageToken) => {
    const a = await c.roep<any>({
      method: "GET",
      path: `/finance/202501/statements/${statementId}/statement_transactions`,
      accessToken,
      shopCipher,
      query: { sort_field: "order_create_time", page_size: 100, page_token: pageToken },
    });
    const { transactions, next_page_token, ...rest } = a.data ?? {};
    kop ??= rest as AfrekeningKop;
    return { items: transactions ?? [], nextPageToken: next_page_token };
  });
  for await (const t of it) transacties.push(t);
  return { kop, transacties };
}

// Transacties van één bestelling (get-transactions-by-order-202501). Geen paginering.
// Let op: de kop heet `fee_and_tax_amount`, per SKU heet hetzelfde `fee_tax_amount`.
export interface SkuTransactie {
  sku_id: string;
  sku_name?: string;
  product_name?: string;
  statement_id: string;
  quantity?: string;
  settlement_amount?: string;
  revenue_amount?: string;
  revenue_breakdown?: Record<string, unknown>;
  shipping_cost_amount?: string;
  shipping_cost_breakdown?: Record<string, unknown>;
  fee_tax_amount?: string;
  fee_tax_breakdown?: { fee?: Record<string, unknown>; tax?: Record<string, unknown>; [veld: string]: unknown };
  [veld: string]: unknown;
}

export interface BestellingTransacties {
  order_id: string;
  order_create_time?: number;
  currency: string;
  revenue_amount?: string;
  fee_and_tax_amount?: string;
  shipping_cost_amount?: string;
  settlement_amount?: string;
  total_count?: number;
  sku_transactions: SkuTransactie[];
  [veld: string]: unknown;
}

export async function transactiesVanBestelling(
  c: TikTokClient,
  accessToken: string,
  shopCipher: string,
  orderId: string,
): Promise<BestellingTransacties> {
  if (!/^\d+$/.test(orderId)) throw new Error(`ongeldig order_id: "${orderId}"`);
  const a = await c.roep<BestellingTransacties>({
    method: "GET",
    path: `/finance/202501/orders/${orderId}/statement_transactions`,
    accessToken,
    shopCipher,
  });
  const d = (a.data ?? {}) as BestellingTransacties;
  return { ...d, sku_transactions: d.sku_transactions ?? [] };
}
