// Nagebootste wereld voor boektoetsen (uit boekrun.test.ts gehaald, zodat ook de D1-toetsen hem gebruiken).
import type { Instellingen } from "../src/verwerk.ts";

// Nagebootste TikTok (vorm van de docs) en een kleine nagebootste Moneybird met memoriaalboekingen in het geheugen.
export const T0 = 1_794_000_000; // nov 2026
export interface Afr { id: string; time: number; status: string; trans: any[]; kop?: any }

export function wereld() {
  const afr: Afr[] = [];
  const best = new Map<string, any>();
  const tiktokFout = new Map<string, number>();
  const docs = new Map<string, any>();
  let volgendId = 9000;
  const mbStatus: { volgende?: number } = {};
  const urls: string[] = [];
  const json = (data: any, status = 200) => new Response(JSON.stringify(data), { status });
  const fn = (async (input: any, init: any = {}) => {
    const u = new URL(String(input));
    const methode = init.method ?? "GET";
    urls.push(`${methode} ${u.hostname.includes("moneybird") ? "MB" : "TT"} ${u.pathname}`);
    if (u.hostname.includes("moneybird")) {
      if (mbStatus.volgende) { const s = mbStatus.volgende; mbStatus.volgende = undefined; return json({ error: "x" }, s); }
      const m = /general_journal_documents(?:\/(\d+))?\.json$/.exec(u.pathname)!;
      if (methode === "GET" && !m[1]) {
        const ref = (u.searchParams.get("filter") ?? "").replace("reference:", "");
        return json([...docs.values()].filter((d) => d.reference === ref));
      }
      if (methode === "GET") return docs.has(m[1]) ? json(docs.get(m[1])) : json({ error: "niet" }, 404);
      const body = JSON.parse(init.body).general_journal_document;
      const regels = (body.general_journal_document_entries_attributes as any[]).filter((e) => !e._destroy).map((e, i) => ({ ...e, id: String(100 + i) }));
      if (methode === "POST") {
        const id = String(volgendId++);
        docs.set(id, { id, reference: body.reference, date: body.date, general_journal_document_entries: regels });
        return json(docs.get(id), 201);
      }
      if (methode === "PATCH") {
        docs.set(m[1], { ...docs.get(m[1]), date: body.date, general_journal_document_entries: regels });
        return json(docs.get(m[1]));
      }
    }
    const ok = (data: any) => json({ code: 0, message: "Success", request_id: "r", data });
    let m;
    if (u.pathname === "/finance/202309/statements") {
      const vanaf = Number(u.searchParams.get("statement_time_ge") ?? 0);
      return ok({ statements: afr.filter((a) => a.time >= vanaf).sort((a, b) => a.time - b.time).map((a) => ({ id: a.id, statement_time: a.time, payment_status: a.status, currency: "EUR", settlement_amount: "0", fee_amount: "0", adjustment_amount: "0" })) });
    }
    if ((m = /^\/finance\/202501\/statements\/(\d+)\/statement_transactions$/.exec(u.pathname))) {
      const a = afr.find((x) => x.id === m![1])!;
      const tot = a.trans.reduce((s, t) => s + Math.round(Number(t.settlement_amount) * 100), 0) / 100;
      return ok({ id: a.id, create_time: a.time, status: "SETTLED", currency: "EUR", payable_amount: String(tot), total_settlement_amount: String(tot), total_count: a.trans.length, ...a.kop, transactions: a.trans });
    }
    if ((m = /^\/finance\/202501\/orders\/(\d+)\/statement_transactions$/.exec(u.pathname))) {
      const f = tiktokFout.get(m[1]);
      if (f) return json({ code: f, message: "fout", request_id: "r" });
      return ok(best.get(m[1]));
    }
    throw new Error(`onverwacht ${u.pathname}`);
  }) as typeof fetch;

  let n = 0;
  const voegToe = (id: string, time: number, status: string, bedragen: number[], extra: any[] = []) => {
    const trans: any[] = [];
    for (const omzet of bedragen) {
      const oid = String(5000 + ++n);
      const comm = -Math.round(omzet * 10) / 100;
      const som = (omzet + comm).toFixed(2);
      best.set(oid, { order_id: oid, currency: "EUR", settlement_amount: som, sku_transactions: [{ sku_id: "1", statement_id: id, settlement_amount: som, revenue_amount: String(omzet), revenue_breakdown: { subtotal_before_discount_amount: String(omzet) }, shipping_cost_amount: "0", shipping_cost_breakdown: {}, fee_tax_amount: String(comm), fee_tax_breakdown: { fee: { platform_commission_amount: String(comm) }, tax: {} } }] });
      trans.push({ id: `${id}${n}`, type: "ORDER", order_id: oid, settlement_amount: som });
    }
    trans.push(...extra);
    afr.push({ id, time, status, trans });
    return afr[afr.length - 1];
  };
  return { afr, best, docs, urls, fn, voegToe, tiktokFout, mbStatus };
}

export const koppeling = { per: { omzet: { grootboekId: "201" }, commissie: { grootboekId: "202" }, correctie: { grootboekId: "203" }, verschil: { grootboekId: "204" } }, tegenrekeningId: "500" } as any;
export const inst = (extra: Partial<Instellingen> = {}): Instellingen => ({ startdatum: T0, magBoeken: true, administratie: { id: "1", periodLockedUntil: null }, koppeling, ...extra });
