// Rekenkern: van de transacties van één bestelling naar neutrale boekingsregels.
// Ontwerp: ontwerp-rekenkern.md deel 2. Geen netwerk, geen boekhoudpakket, alles in centen.
import { naarKleinsteEenheid } from "./bedrag.ts";
import type { BestellingTransacties, SkuTransactie } from "./endpoints.ts";

export type Soort =
  | "omzet" | "korting" | "terugbetaling" | "korting_terug" | "overig_omzet"
  | "verzendkosten" | "commissie" | "belasting_op_kosten" | "belasting"
  | "omzet_totaal" | "verzendkosten_totaal" | "kosten_en_belasting_totaal"
  | "verschil";

export interface Boekingsregel {
  /** orderId/statementId/skuId/volgnummer: alle regels van één SKU-transactie delen hem. */
  sleutel: string;
  soort: Soort;
  bedragCenten: number;
  valuta: string;
  orderId: string;
  statementId: string;
  skuId: string;
  bronVeld: string;
}

export interface Boekingen {
  regels: Boekingsregel[];
  waarschuwingen: string[];
}

const OMZET_SOORT: Record<string, Soort> = {
  subtotal_before_discount_amount: "omzet",
  seller_discount_amount: "korting",
  refund_subtotal_before_discount_amount: "terugbetaling",
  seller_discount_refund_amount: "korting_terug",
};

type Veld = { veld: string; centen: number; soort: Soort };

/** Leest een totaalveld: undefined of "" is onbekend (null), anders centen. */
function totaal(waarde: unknown, valuta: string, naam: string, w: string[]): number | null {
  if (waarde === undefined || waarde === null || waarde === "") return null;
  if (typeof waarde !== "string") {
    w.push(`${naam}: geen tekst, behandeld als onbekend`);
    return null;
  }
  try {
    return naarKleinsteEenheid(waarde, valuta);
  } catch {
    w.push(`${naam}: ongeldig bedrag "${waarde}", behandeld als onbekend`);
    return null;
  }
}

/** Leest de velden van een uitsplitsing. null als er geen bruikbaar object is. */
function uitsplitsing(
  obj: unknown,
  valuta: string,
  naam: string,
  soortVan: (veld: string) => Soort,
  overslaan: Set<string>,
  w: string[],
): Veld[] | null {
  if (obj === null || typeof obj !== "object" || Array.isArray(obj)) return null;
  const uit: Veld[] = [];
  for (const [veld, waarde] of Object.entries(obj as Record<string, unknown>)) {
    if (overslaan.has(veld)) continue;
    if (waarde === undefined || waarde === "") continue;
    if (typeof waarde !== "string") {
      w.push(`${naam}.${veld}: geen bedrag, overgeslagen`);
      continue;
    }
    let centen: number;
    try {
      centen = naarKleinsteEenheid(waarde, valuta);
    } catch {
      w.push(`${naam}.${veld}: ongeldig bedrag "${waarde}", overgeslagen`);
      continue;
    }
    uit.push({ veld, centen, soort: soortVan(veld) });
  }
  return uit;
}

const som = (v: Veld[]) => v.reduce((s, x) => s + x.centen, 0);

/**
 * Kiest per groep: losse regels als de uitsplitsing op de cent sluit (of het totaal onbekend is),
 * anders het totaal als één regel. Geeft de som van de groep terug, of null als hij onbekend is.
 */
function groep(
  naam: string,
  totaalVeld: string,
  totaalCenten: number | null,
  delen: Veld[] | null,
  totaalSoort: Soort,
  voeg: (soort: Soort, centen: number, bron: string) => void,
  w: string[],
): number | null {
  if (delen === null && totaalCenten === null) {
    w.push(`${naam}: geen totaal en geen uitsplitsing`);
    return null;
  }
  if (delen !== null && totaalCenten === null) {
    w.push(`${naam}: totaal ${totaalVeld} onbekend, uitsplitsing gebruikt`);
    for (const d of delen) voeg(d.soort, d.centen, d.veld);
    return som(delen);
  }
  if (delen !== null && som(delen) === totaalCenten) {
    for (const d of delen) voeg(d.soort, d.centen, d.veld);
    return totaalCenten;
  }
  const s = delen === null ? "geen" : String(som(delen));
  w.push(`${naam}: uitsplitsing (${s}) sluit niet op ${totaalVeld} (${totaalCenten}), totaal geboekt`);
  voeg(totaalSoort, totaalCenten!, totaalVeld);
  return totaalCenten;
}

const isBelastingOpKosten = (veld: string) => /(_tax|_tax_amount)$/.test(veld);

export function boekingsregels(b: BestellingTransacties): Boekingen {
  const valuta = typeof b.currency === "string" ? b.currency : "";
  if (!/^[A-Za-z]{3}$/.test(valuta)) throw new Error(`bestelling ${b.order_id ?? "?"}: ongeldige munt "${String(b.currency)}"`);
  const orderId = String(b.order_id ?? "");
  const regels: Boekingsregel[] = [];
  const w: string[] = [];
  const volgnummers = new Map<string, number>();
  const skus: SkuTransactie[] = Array.isArray(b.sku_transactions) ? b.sku_transactions : [];

  for (const t of skus) {
    const statementId = String(t.statement_id ?? "");
    const skuId = String(t.sku_id ?? "");
    const basis = `${orderId}/${statementId}/${skuId}`;
    const nr = volgnummers.get(basis) ?? 0;
    volgnummers.set(basis, nr + 1);
    const sleutel = `${basis}/${nr}`;
    const pre = `sku ${skuId} (afrekening ${statementId})`;
    const voeg = (soort: Soort, centen: number, bronVeld: string) => {
      if (centen !== 0) regels.push({ sleutel, soort, bedragCenten: centen, valuta, orderId, statementId, skuId, bronVeld });
    };

    const omzet = groep(
      `${pre} omzet`, "revenue_amount", totaal(t.revenue_amount, valuta, `${pre} revenue_amount`, w),
      uitsplitsing(t.revenue_breakdown, valuta, `${pre} revenue_breakdown`, (v) => OMZET_SOORT[v] ?? "overig_omzet", new Set(), w),
      "omzet_totaal", voeg, w,
    );
    const verzending = groep(
      `${pre} verzending`, "shipping_cost_amount", totaal(t.shipping_cost_amount, valuta, `${pre} shipping_cost_amount`, w),
      uitsplitsing(t.shipping_cost_breakdown, valuta, `${pre} shipping_cost_breakdown`, () => "verzendkosten", new Set(["supplementary_component"]), w),
      "verzendkosten_totaal", voeg, w,
    );
    const ftb = t.fee_tax_breakdown;
    let kostenDelen: Veld[] | null = null;
    if (ftb !== null && typeof ftb === "object" && !Array.isArray(ftb)) {
      const fee = uitsplitsing(ftb.fee, valuta, `${pre} fee`, (v) => (isBelastingOpKosten(v) ? "belasting_op_kosten" : "commissie"), new Set(), w);
      const tax = uitsplitsing(ftb.tax, valuta, `${pre} tax`, () => "belasting", new Set(), w);
      if (fee !== null || tax !== null) kostenDelen = [...(fee ?? []), ...(tax ?? [])];
    }
    const kosten = groep(
      `${pre} kosten en belasting`, "fee_tax_amount", totaal(t.fee_tax_amount, valuta, `${pre} fee_tax_amount`, w),
      kostenDelen, "kosten_en_belasting_totaal", voeg, w,
    );

    const afrekening = totaal(t.settlement_amount, valuta, `${pre} settlement_amount`, w);
    if (omzet === null || verzending === null || kosten === null || afrekening === null) {
      w.push(`${pre}: controle op settlement_amount overgeslagen (bedrag onbekend)`);
      continue;
    }
    const verschil = afrekening - (omzet + verzending + kosten);
    if (verschil !== 0) {
      w.push(`${pre}: regels tellen op tot ${omzet + verzending + kosten}, settlement_amount is ${afrekening}; verschil ${verschil} geboekt`);
      voeg("verschil", verschil, "settlement_amount");
    }
  }

  const kop = totaal(b.settlement_amount, valuta, "kop settlement_amount", w);
  if (kop === null) {
    w.push("kop: controle op settlement_amount overgeslagen (bedrag onbekend)");
  } else {
    const alles = regels.reduce((s, r) => s + r.bedragCenten, 0);
    if (alles !== kop) w.push(`kop: alle regels samen ${alles}, settlement_amount van de bestelling is ${kop}; niet geboekt, alleen gemeld`);
  }
  if (typeof b.total_count === "number" && b.total_count !== skus.length) {
    w.push(`total_count is ${b.total_count}, maar er zijn ${skus.length} SKU-transacties`);
  }
  return { regels, waarschuwingen: w };
}
