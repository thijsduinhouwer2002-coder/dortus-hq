// Eén afrekening boeken of vervangen in Moneybird, zonder dubbel te boeken. Ontwerp: ontwerp-moneybird.md deel 3.
import type { MoneybirdClient } from "./client.ts";
import { MoneybirdFout, idTekst } from "./fouten.ts";
import { maakMemoriaal, tekstNaarCenten, type AfrekeningInvoer, type Koppeling, type Memoriaal, type MemoriaalOpties } from "./memoriaal.ts";

export type Uitkomst = "aangemaakt" | "vervangen" | "ongewijzigd" | "onzeker" | "leeg" | "leeg_maar_geboekt";

export interface BoekResultaat {
  uitkomst: Uitkomst;
  id?: string;
  waarschuwingen: string[];
  /** Bij `onzeker`: de fout; de product-laag controleert pas na minstens 10 minuten opnieuw via het kenmerk. */
  fout?: MoneybirdFout;
}

export interface BoekOpties extends MemoriaalOpties {
  /** Document-id uit een eerder 201-antwoord; Moneybird cachet GET, dus zoeken op kenmerk is de terugval. */
  bekendId?: string;
}

export interface AdministratieInfo {
  id: string;
  periodLockedUntil: string | null;
}

const PAD = (adm: string) => `/${adm}/documents/general_journal_documents`;

export async function boekAfrekening(client: MoneybirdClient, adm: AdministratieInfo, invoer: AfrekeningInvoer, koppeling: Koppeling, opties: BoekOpties = {}): Promise<BoekResultaat> {
  const m = maakMemoriaal(invoer, koppeling, opties); // alle invoercontroles vóór de eerste aanroep
  const w = m.waarschuwingen;
  const bestaand = await vind(client, adm.id, m.kenmerk, opties.bekendId);

  if (m.regels.length === 0) return bestaand ? { uitkomst: "leeg_maar_geboekt", id: idTekst(bestaand.id, "document id"), waarschuwingen: w } : { uitkomst: "leeg", waarschuwingen: w };

  if (bestaand) {
    const id = idTekst(bestaand.id, "document id");
    if (gelijk(bestaand, m)) return { uitkomst: "ongewijzigd", id, waarschuwingen: w };
    controleerPeriode(m.datum, adm.periodLockedUntil);
    const oud = (bestaand.general_journal_document_entries ?? []).map((e: any) => ({ id: idTekst(e.id, "regel id"), _destroy: true }));
    const body = { general_journal_document: { ...m.body.general_journal_document, general_journal_document_entries_attributes: [...oud, ...m.body.general_journal_document.general_journal_document_entries_attributes] } };
    try {
      await client.roep("PATCH", `${PAD(adm.id)}/${id}`, { body });
    } catch (e) {
      if (e instanceof MoneybirdFout && e.soort === "server") return { uitkomst: "onzeker", id, waarschuwingen: w, fout: e };
      throw e;
    }
    return { uitkomst: "vervangen", id, waarschuwingen: w };
  }

  controleerPeriode(m.datum, adm.periodLockedUntil);
  let antwoord: any;
  try {
    antwoord = await client.roep("POST", PAD(adm.id), { body: m.body });
  } catch (e) {
    if (e instanceof MoneybirdFout && e.soort === "server") return { uitkomst: "onzeker", waarschuwingen: w, fout: e };
    throw e;
  }
  try {
    return { uitkomst: "aangemaakt", id: idTekst(antwoord?.id, "document id"), waarschuwingen: w };
  } catch (e) {
    // De boeking staat er waarschijnlijk, maar zonder bruikbaar id: onzeker, niet opnieuw POSTen.
    return { uitkomst: "onzeker", waarschuwingen: w, fout: e as MoneybirdFout };
  }
}

export function controleerPeriode(datum: string, periodLockedUntil: string | null): void {
  if (periodLockedUntil && datum <= periodLockedUntil) {
    throw new MoneybirdFout("periode_afgesloten", `De periode tot en met ${periodLockedUntil} is afgesloten in Moneybird; afrekening van ${datum} kan niet geboekt of vervangen worden.`);
  }
}

async function vind(client: MoneybirdClient, adm: string, kenmerk: string, bekendId?: string): Promise<any | null> {
  if (bekendId) {
    try {
      const doc = await client.roep<any>("GET", `${PAD(adm)}/${idTekst(bekendId, "bekendId")}`);
      // Vangnet: alleen een document met precies ons kenmerk mag vervangen worden.
      if (doc?.reference === kenmerk) return doc;
    } catch (e) {
      if (!(e instanceof MoneybirdFout && e.soort === "niet_gevonden")) throw e;
    }
  }
  const lijst = await client.roep<any[]>("GET", PAD(adm), { query: { filter: `reference:${kenmerk}` } });
  if (!Array.isArray(lijst)) throw new MoneybirdFout("antwoord", "zoeken op kenmerk gaf geen lijst terug");
  const precies = lijst.filter((d) => d?.reference === kenmerk);
  if (precies.length > 1) throw new MoneybirdFout("dubbel", `Er staan ${precies.length} boekingen met kenmerk ${kenmerk} in Moneybird; verwijder er zelf één, de app boekt niet verder.`);
  return precies[0] ?? null;
}

/** Zelfde datum, kenmerk en regels (rekening, debet en credit in centen, omschrijving, in volgorde). Btw telt niet mee: staat uit tot de sandbox-test. */
function gelijk(doc: any, m: Memoriaal): boolean {
  if (doc.reference !== m.kenmerk || doc.date !== m.datum) return false;
  const oud = [...(doc.general_journal_document_entries ?? [])].sort((a: any, b: any) => (a.row_order ?? 0) - (b.row_order ?? 0));
  if (oud.length !== m.regels.length) return false;
  return oud.every((e: any, i: number) => {
    const n = m.regels[i];
    return idTekst(e.ledger_account_id, "ledger_account_id") === n.grootboekId && tekstNaarCenten(e.debit) === n.debetCenten && tekstNaarCenten(e.credit) === n.creditCenten && (e.description ?? "") === n.omschrijving;
  });
}
