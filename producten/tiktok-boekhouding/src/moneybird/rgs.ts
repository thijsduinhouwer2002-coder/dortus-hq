// Voorstel: welke RGS 3.5-code per soort, zodat de app een ontbrekende rekening met één klik kan aanmaken in Moneybird
// (POST ledger_accounts vraagt `rgs_code`, versie 3.5, GEZIEN in de OpenAPI van Moneybird). Codes nagekeken tegen de
// definitieve RGS 3.5-lijst (test/voorbeelden/rgs35-uittreksel.tsv). Toelichting en GOK's: ../../rgs-codes.md.
import type { MbSoort } from "./memoriaal.ts";

export type AccountType = "current_assets" | "current_liabilities" | "revenue" | "direct_costs" | "expenses" | "other_income_expenses";

export interface RgsVoorstel {
  rgs: string;
  accountType: AccountType;
  /** Naam van de nieuwe rekening in Moneybird. */
  naam: string;
  /** false: niet automatisch aanmaken, de verkoper kiest een bestaande rekening (bijv. btw). */
  aanmaken: boolean;
  /** true: vóór aanmaken alleen op naam zoeken, niet op RGS-code (de code deelt hij met een andere soort). */
  zoekOpNaam?: boolean;
}

const OMZET: RgsVoorstel = { rgs: "WOmzNohOlh", accountType: "revenue", naam: "Omzet TikTok Shop", aanmaken: true };
const KORTING: RgsVoorstel = { rgs: "WOmzKebVekVkh", accountType: "revenue", naam: "Kortingen TikTok Shop", aanmaken: true };
const VRACHT: RgsVoorstel = { rgs: "WBedVkkVrk", accountType: "expenses", naam: "Verzendkosten TikTok Shop", aanmaken: true };
const COMMISSIE: RgsVoorstel = { rgs: "WBedVkkCom", accountType: "expenses", naam: "Commissie en kosten TikTok Shop", aanmaken: true };

export const RGS_PER_SOORT: Record<MbSoort, RgsVoorstel> = {
  omzet: OMZET,
  terugbetaling: OMZET, // RGS heeft geen eigen code voor retouren; terugbetaling verlaagt de omzet
  overig_omzet: OMZET,
  omzet_totaal: OMZET,
  korting: KORTING,
  korting_terug: KORTING,
  verzendkosten: VRACHT,
  verzendkosten_totaal: VRACHT,
  commissie: COMMISSIE,
  kosten_en_belasting_totaal: COMMISSIE,
  // Zelfde code als commissie (dubbel mag, proef 1), eigen naam; zoeken op naam, anders vind je de commissierekening.
  affiliate: { rgs: "WBedVkkCom", accountType: "expenses", naam: "Affiliate-commissie TikTok Shop (creators)", aanmaken: true, zoekOpNaam: true },
  // GOK: of TikTok Nederlandse btw op de kosten rekent. Btw-rekeningen bestaan al in Moneybird: niet aanmaken.
  belasting_op_kosten: { rgs: "BSchBepBtwVoo", accountType: "current_liabilities", naam: "Voorbelasting", aanmaken: false },
  belasting: { rgs: "WBedVkkObs", accountType: "expenses", naam: "Belastingen TikTok Shop", aanmaken: true },
  correctie: { rgs: "WBedVkkOvr", accountType: "expenses", naam: "Correcties TikTok Shop", aanmaken: true },
  verschil: { rgs: "BVorTusTovTvp", accountType: "current_assets", naam: "Vraagposten TikTok Shop", aanmaken: true },
};

/** Tegenrekening "Te ontvangen van TikTok Shop". */
export const RGS_TEGENREKENING: RgsVoorstel = { rgs: "BVorOvrOvk", accountType: "current_assets", naam: "Te ontvangen van TikTok Shop", aanmaken: true };
