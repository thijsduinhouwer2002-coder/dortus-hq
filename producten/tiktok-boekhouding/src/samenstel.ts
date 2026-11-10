// Product-laag stap "een afrekening samenstellen" (ontwerp-productlaag.md, punten 1 tot 7). Zuiver: de aanroeper
// haalt de transacties en bestellingen op (in porties, binnen het budget) en geeft ze hier mee.
import { boekingsregels } from "../../tiktok-shop-basis/src/boekingen.ts";
import { naarKleinsteEenheid } from "../../tiktok-shop-basis/src/bedrag.ts";
import type { AfrekeningKop, BestellingTransacties, Transactie } from "../../tiktok-shop-basis/src/endpoints.ts";
import type { RegelInvoer } from "./moneybird/memoriaal.ts";

export interface Samenstelling {
  status: "compleet" | "onvolledig" | "fout_gegevens";
  reden?: string;
  regels: RegelInvoer[];
  waarschuwingen: string[];
  /** payable_amount van de kop: wat op de bank komt. */
  uitbetaaldCenten?: number;
  /** Bestellingen die nog (opnieuw) opgehaald moeten worden voor deze afrekening. */
  ontbrekend: string[];
}

/** Leeg of ontbrekend is onbekend (null), niet 0. */
function bedrag(s: unknown, valuta: string): number | null {
  if (s === undefined || s === null || s === "") return null;
  return naarKleinsteEenheid(String(s), valuta);
}

/** De bestellingen van deze afrekening, elk één keer (één bestelling kan twee keer in een afrekening staan). */
export function bestellingenVan(transacties: Transactie[]): string[] {
  return [...new Set(transacties.filter((t) => t.type === "ORDER" && t.order_id).map((t) => String(t.order_id)))];
}

/** Telt een bewaard antwoord voor deze afrekening? Alleen als het een SKU-transactie met dit statementId heeft. */
export function bruikbaar(b: BestellingTransacties | undefined, statementId: string): boolean {
  return !!b && Array.isArray(b.sku_transactions) && b.sku_transactions.some((s) => String(s.statement_id) === statementId);
}

export function stelSamen(statementId: string, kop: AfrekeningKop | undefined, transacties: Transactie[], bestellingen: Map<string, BestellingTransacties>): Samenstelling {
  const leeg = (status: Samenstelling["status"], reden: string, ontbrekend: string[] = []): Samenstelling => ({ status, reden, regels: [], waarschuwingen: [], ontbrekend });
  if (!kop) return leeg("onvolledig", "kop van de afrekening ontbreekt");
  if (!kop.currency || !/^\d+$/.test(String(kop.total_count ?? ""))) return leeg("onvolledig", "kop zonder munt of aantal transacties");
  const valuta = String(kop.currency).toUpperCase();
  if (valuta !== "EUR") return leeg("fout_gegevens", `versie 1 werkt alleen met EUR, deze afrekening is in ${kop.currency}`);
  if (Number(kop.total_count) !== transacties.length) return leeg("onvolledig", `TikTok meldt ${kop.total_count} transacties, er kwamen er ${transacties.length}`);

  const ids = transacties.map((t) => String(t.id));
  if (new Set(ids).size !== ids.length) return leeg("onvolledig", "TikTok gaf een transactie dubbel; opnieuw ophalen");

  const ontbrekend = bestellingenVan(transacties).filter((id) => !bruikbaar(bestellingen.get(id), statementId));
  if (ontbrekend.length) return leeg("onvolledig", `${ontbrekend.length} bestelling(en) nog niet opgehaald`, ontbrekend);

  const regels: RegelInvoer[] = [];
  const w: string[] = [];
  const voeg = (soort: RegelInvoer["soort"], c: number) => { if (c !== 0) regels.push({ soort, bedragCenten: c, statementId, valuta }); };
  let somTransacties = 0;
  let uit: number | null = null;

  try {
    // ORDER: per bestelling één keer de rekenkern, vergelijken met de som van haar transacties in deze afrekening.
    for (const orderId of bestellingenVan(transacties)) {
      const eigen = transacties.filter((t) => t.type === "ORDER" && String(t.order_id) === orderId);
      let doel = 0;
      let aanpassing = 0;
      for (const t of eigen) {
        const s = bedrag(t.settlement_amount, valuta);
        if (s === null) return leeg("fout_gegevens", `transactie ${t.id} van bestelling ${orderId} heeft geen settlement_amount`);
        doel += s;
        aanpassing += bedrag(t.adjustment_amount, valuta) ?? 0;
      }
      somTransacties += doel;
      const b = boekingsregels(bestellingen.get(orderId)!);
      // Kop-waarschuwingen van de rekenkern vervallen: hier vergelijken we met de transactie van déze afrekening.
      // Waarschuwingen over SKU's van een andere afrekening horen daar, niet hier.
      for (const x of b.waarschuwingen) {
        if (x.startsWith("kop:")) continue;
        const m = /\(afrekening ([^)]*)\)/.exec(x);
        if (m && m[1] && m[1] !== statementId) continue;
        w.push(`bestelling ${orderId}: ${x}`);
      }
      const hier = b.regels.filter((r) => r.statementId === statementId);
      for (const r of hier) {
        if (r.valuta !== valuta) return leeg("fout_gegevens", `bestelling ${orderId} is in ${r.valuta}, de afrekening in ${valuta}`);
        voeg(r.soort, r.bedragCenten);
      }
      const som = hier.reduce((a, r) => a + r.bedragCenten, 0);
      let rest = doel - som;
      let correctie = 0;
      if (rest !== 0 && aanpassing !== 0) {
        correctie = aanpassing;
        voeg("correctie", aanpassing); // GOK: teken en of het al in settlement_amount zit (zie ontwerp)
        rest -= aanpassing;
      }
      if (rest !== 0) {
        voeg("verschil", rest);
        w.push(`bestelling ${orderId}: regels ${som}, transacties in deze afrekening ${doel}${correctie ? `, correctie ${correctie} geboekt` : ""}; ${rest} apart gezet als verschil`);
      }
    }
    // Andere transacties: één correctie per transactie.
    for (const t of transacties) {
      if (t.type === "ORDER" && t.order_id) continue;
      if (t.type === "ORDER") w.push(`transactie ${t.id}: ORDER zonder order_id, geboekt als correctie`);
      if (t.type === "RESERVE") {
        const r = bedrag(t.reserve_amount, valuta);
        if (r === null) return leeg("fout_gegevens", `reservering ${t.id} zonder reserve_amount`);
        voeg("correctie", r);
        w.push(`reservering ${t.id} (${r}) geboekt als correctie; hoort volgens TikTok alleen bij VK en VS`);
        continue;
      }
      let s = bedrag(t.settlement_amount, valuta);
      if (s === null) {
        s = bedrag(t.adjustment_amount, valuta);
        if (s === null) return leeg("fout_gegevens", `aanpassing ${t.id} (${t.type}) heeft geen bedrag`);
        w.push(`aanpassing ${t.id} (${t.type}): settlement_amount leeg, adjustment_amount ${s} gebruikt`);
      }
      somTransacties += s;
      voeg("correctie", s);
    }
    const totaal = bedrag(kop.total_settlement_amount, valuta);
    if (totaal === null) w.push("afrekening: total_settlement_amount leeg, controle op het totaal overgeslagen");
    else if (totaal !== somTransacties) w.push(`afrekening: transacties samen ${somTransacties}, total_settlement_amount ${totaal}`);
    uit = bedrag(kop.payable_amount, valuta);
    if (uit === null) w.push("afrekening: payable_amount leeg, uitbetaald bedrag onbekend");
  } catch (e) {
    return leeg("fout_gegevens", `gegevens van TikTok niet te lezen: ${(e as Error).message}`);
  }

  return { status: "compleet", regels, waarschuwingen: w, ontbrekend: [], ...(uit === null ? {} : { uitbetaaldCenten: uit }) };
}
