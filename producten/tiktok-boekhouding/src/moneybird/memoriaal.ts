// Van de boekingsregels van één TikTok-afrekening naar één memoriaalboeking in Moneybird. Zuiver, geen netwerk.
// Ontwerp: ontwerp-moneybird.md deel 1. Body volgens de OpenAPI van Moneybird
// (POST /{administration_id}/documents/general_journal_documents).

import type { Soort } from "../../../tiktok-shop-basis/src/boekingen.ts";
import { MoneybirdFout } from "./fouten.ts";

export type MbSoort = Soort | "correctie";

/** Vaste volgorde en omschrijving in gewone woorden. */
export const SOORTEN: Array<[MbSoort, string]> = [
  ["omzet", "omzet"],
  ["korting", "korting van de winkel"],
  ["terugbetaling", "terugbetaling aan klant"],
  ["korting_terug", "korting terug bij terugbetaling"],
  ["overig_omzet", "overige omzet"],
  ["omzet_totaal", "omzet (totaal)"],
  ["verzendkosten", "verzendkosten"],
  ["verzendkosten_totaal", "verzendkosten (totaal)"],
  ["commissie", "commissie en kosten"],
  ["affiliate", "affiliate-commissie (creators)"],
  ["belasting_op_kosten", "btw op kosten"],
  ["belasting", "belasting"],
  ["kosten_en_belasting_totaal", "kosten en belasting (totaal)"],
  ["correctie", "correctie van TikTok"],
  ["verschil", "verschil, apart gezet"],
];
const BEKEND = new Set(SOORTEN.map(([s]) => s));

export interface RegelInvoer {
  soort: MbSoort;
  bedragCenten: number;
  statementId: string;
  /** Munt van de regel (zoals de rekenkern hem geeft); als hij er is, moet hij gelijk zijn aan die van de afrekening. */
  valuta?: string;
}

export interface AfrekeningInvoer {
  statementId: string;
  /** statement_time van TikTok, Unix-seconden. */
  statementTime: number;
  valuta: string;
  /** Het bedrag dat op de bank kwam, als bekend. */
  uitbetaaldCenten?: number;
  regels: RegelInvoer[];
}

export interface Koppeling {
  per: Partial<Record<MbSoort, { grootboekId: string; btwTariefId?: string }>>;
  /** "Te ontvangen van TikTok Shop", vlottende activa. */
  tegenrekeningId: string;
}

export interface MemoriaalRegel {
  grootboekId: string;
  btwTariefId?: string;
  debetCenten: number;
  creditCenten: number;
  omschrijving: string;
}

export interface Memoriaal {
  kenmerk: string;
  datum: string;
  regels: MemoriaalRegel[];
  totaalCenten: number;
  waarschuwingen: string[];
  /** Klaar om te versturen; leeg als er niets te boeken is. */
  body: { general_journal_document: { reference: string; date: string; general_journal_document_entries_attributes: Array<Record<string, unknown>> } };
}

export interface MemoriaalOpties {
  /** Pas aan na de sandbox-test: wat Moneybird met tax_rate_id in een memoriaal doet is nog niet gezien. */
  btwToegestaan?: boolean;
}

export function kenmerkVan(statementId: string): string {
  return `TikTokShop-${statementId}`;
}

/** Datum van een Unix-tijd in Nederlandse tijd, als JJJJ-MM-DD. */
export function datumNL(unixSeconden: number): string {
  return new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Amsterdam", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date(unixSeconden * 1000));
}

/** Centen (geheel, niet negatief) naar "123.45". */
export function centenTekst(c: number): string {
  if (!Number.isSafeInteger(c) || c < 0) throw new MoneybirdFout("invoer", `ongeldig bedrag in centen: ${c}`);
  return `${Math.floor(c / 100)}.${String(c % 100).padStart(2, "0")}`;
}

/** "100.0", "0.0", "12.34" of "12,34" van Moneybird naar centen; meer dan twee decimalen is een fout. */
export function tekstNaarCenten(s: unknown): number {
  if (typeof s !== "string") throw new MoneybirdFout("antwoord", `bedrag van Moneybird is geen tekst: ${JSON.stringify(s)}`);
  const t = s.replace(",", ".");
  const m = /^(-?)(\d+)(?:\.(\d{1,2}))?$/.exec(t);
  if (!m) throw new MoneybirdFout("antwoord", `onverwacht bedrag van Moneybird: ${JSON.stringify(s)}`);
  const c = Number(m[2]) * 100 + Number((m[3] ?? "").padEnd(2, "0"));
  return m[1] === "-" ? -c : c;
}

export function maakMemoriaal(invoer: AfrekeningInvoer, koppeling: Koppeling, opties: MemoriaalOpties = {}): Memoriaal {
  if (!/^\d+$/.test(invoer.statementId)) throw new MoneybirdFout("invoer", `statementId moet uit cijfers bestaan: ${invoer.statementId}`);
  if (invoer.valuta !== "EUR") throw new MoneybirdFout("invoer", `versie 1 boekt alleen EUR, deze afrekening is in ${invoer.valuta}`);
  // Unix-seconden tussen 2015 en 2100; vangt milliseconden en lege waarden af.
  if (!Number.isFinite(invoer.statementTime) || invoer.statementTime < 1_420_070_400 || invoer.statementTime > 4_102_444_800) {
    throw new MoneybirdFout("invoer", `statementTime is geen Unix-tijd in seconden: ${invoer.statementTime}`);
  }
  if (!/^\d+$/.test(koppeling.tegenrekeningId ?? "") && koppeling.tegenrekeningId) throw new MoneybirdFout("instelling", `tegenrekening-id moet uit cijfers bestaan: ${koppeling.tegenrekeningId}`);
  if (!koppeling.tegenrekeningId) throw new MoneybirdFout("instelling", "geen tegenrekening (Te ontvangen van TikTok Shop) gekozen");

  const som = new Map<MbSoort, number>();
  for (const r of invoer.regels) {
    if (r.statementId !== invoer.statementId) throw new MoneybirdFout("invoer", `regel van afrekening ${r.statementId} hoort niet bij afrekening ${invoer.statementId}`);
    if (r.valuta !== undefined && r.valuta !== invoer.valuta) throw new MoneybirdFout("invoer", `regel in ${r.valuta} in een afrekening in ${invoer.valuta}`);
    if (!BEKEND.has(r.soort)) throw new MoneybirdFout("invoer", `onbekende soort: ${r.soort}`);
    if (!Number.isSafeInteger(r.bedragCenten)) throw new MoneybirdFout("invoer", `bedrag is geen geheel aantal centen: ${r.bedragCenten}`);
    som.set(r.soort, (som.get(r.soort) ?? 0) + r.bedragCenten);
  }

  const kenmerk = kenmerkVan(invoer.statementId);
  const regels: MemoriaalRegel[] = [];
  let totaal = 0;
  for (const [soort, naam] of SOORTEN) {
    const c = som.get(soort) ?? 0;
    if (c === 0) continue;
    // Affiliate zonder eigen rekening valt terug op de rekening van de commissie, nooit op het btw-tarief daarvan (ontwerp-affiliate.md).
    const k = koppeling.per[soort] ?? (soort === "affiliate" && koppeling.per.commissie?.grootboekId ? { grootboekId: koppeling.per.commissie.grootboekId } : undefined);
    if (!k?.grootboekId) throw new MoneybirdFout("instelling", `geen grootboekrekening gekozen voor "${naam}"`);
    // Een leeg btw-tarief (lege keuzelijst in instellingen) betekent: geen btw.
    if (!/^\d+$/.test(k.grootboekId) || (k.btwTariefId && !/^\d+$/.test(k.btwTariefId))) throw new MoneybirdFout("instelling", `rekening of btw-tarief bij "${naam}" moet een id uit cijfers zijn`);
    if (k.btwTariefId && !opties.btwToegestaan) throw new MoneybirdFout("btw_nog_niet_getest", `btw-tarief bij "${naam}" kan pas na de sandbox-test`);
    totaal += c;
    const regel: MemoriaalRegel = { grootboekId: k.grootboekId, debetCenten: c < 0 ? -c : 0, creditCenten: c > 0 ? c : 0, omschrijving: `TikTok Shop ${naam}, afrekening ${invoer.statementId}` };
    if (k.btwTariefId) regel.btwTariefId = k.btwTariefId;
    regels.push(regel);
  }
  if (totaal !== 0) {
    regels.push({ grootboekId: koppeling.tegenrekeningId, debetCenten: totaal > 0 ? totaal : 0, creditCenten: totaal < 0 ? -totaal : 0, omschrijving: `TikTok Shop te ontvangen, afrekening ${invoer.statementId}` });
  }

  const waarschuwingen: string[] = [];
  if (invoer.uitbetaaldCenten !== undefined && invoer.uitbetaaldCenten !== totaal) {
    waarschuwingen.push(`Uitbetaald ${centenMetTeken(invoer.uitbetaaldCenten)} EUR, geboekt ${centenMetTeken(totaal)} EUR: verschil ${centenMetTeken(invoer.uitbetaaldCenten - totaal)} EUR wordt niet geboekt.`);
  }

  const datum = datumNL(invoer.statementTime);
  const entries = regels.map((r, i) => {
    const e: Record<string, unknown> = { ledger_account_id: r.grootboekId, debit: centenTekst(r.debetCenten), credit: centenTekst(r.creditCenten), description: r.omschrijving, row_order: i + 1 };
    if (r.btwTariefId) e.tax_rate_id = r.btwTariefId;
    return e;
  });
  return { kenmerk, datum, regels, totaalCenten: totaal, waarschuwingen, body: { general_journal_document: { reference: kenmerk, date: datum, general_journal_document_entries_attributes: entries } } };
}

function centenMetTeken(c: number): string {
  return (c < 0 ? "-" : "") + centenTekst(Math.abs(c));
}
