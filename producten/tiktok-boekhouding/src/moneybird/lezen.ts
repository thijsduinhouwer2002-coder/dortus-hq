// Lezen uit Moneybird: administraties, grootboekrekeningen en btw-tarieven. Ontwerp: ontwerp-moneybird.md deel 2.
import type { MoneybirdClient } from "./client.ts";
import { administratieId, idTekst } from "./fouten.ts";
import type { Koppeling } from "./memoriaal.ts";

export interface Administratie {
  id: string;
  naam: string;
  valuta: string;
  land: string;
  periodLockedUntil: string | null;
}

export interface Grootboekrekening {
  id: string;
  naam: string;
  soort: string;
  actief: boolean;
  toegestaan: string[];
}

export interface BtwTarief {
  id: string;
  naam: string;
  percentage: string;
}

export async function administraties(client: MoneybirdClient): Promise<Administratie[]> {
  const lijst = await client.roep<any[]>("GET", "/administrations");
  return lijst.map((a) => ({ id: administratieId(a.id), naam: String(a.name ?? ""), valuta: String(a.currency ?? ""), land: String(a.country ?? ""), periodLockedUntil: a.period_locked_until ?? null }));
}

/** Dit endpoint kent geen paginering: alles in één verzoek. */
export async function grootboekrekeningen(client: MoneybirdClient, adm: string): Promise<Grootboekrekening[]> {
  const lijst = await client.roep<any[]>("GET", `/${adm}/ledger_accounts`);
  return lijst.map((r) => ({ id: idTekst(r.id, "ledger_account id"), naam: String(r.name ?? ""), soort: String(r.account_type ?? ""), actief: r.active !== false, toegestaan: Array.isArray(r.allowed_document_types) ? r.allowed_document_types : [] }));
}

export async function btwTarieven(client: MoneybirdClient, adm: string): Promise<BtwTarief[]> {
  const lijst = await client.roep<any[]>("GET", `/${adm}/tax_rates`, { query: { filter: "tax_rate_type:general_journal_document,active:true" } });
  return lijst.map((t) => ({ id: idTekst(t.id, "tax_rate id"), naam: String(t.name ?? ""), percentage: String(t.percentage ?? "") }));
}

/** Problemen met de gekozen rekeningen, in gewone woorden; een lege lijst is goed. */
export function controleerKoppeling(koppeling: Koppeling, rekeningen: Grootboekrekening[]): string[] {
  const perId = new Map(rekeningen.map((r) => [r.id, r]));
  const fouten: string[] = [];
  const kijk = (id: string, wat: string) => {
    const r = perId.get(id);
    if (!r) fouten.push(`${wat}: rekening ${id} bestaat niet (meer) in Moneybird`);
    else if (!r.actief) fouten.push(`${wat}: rekening "${r.naam}" staat uit`);
    else if (!r.toegestaan.includes("general_journal_document")) fouten.push(`${wat}: rekening "${r.naam}" mag niet in een memoriaalboeking`);
    return r;
  };
  for (const [soort, k] of Object.entries(koppeling.per)) if (k) kijk(k.grootboekId, soort);
  const t = kijk(koppeling.tegenrekeningId, "tegenrekening");
  if (t && t.soort !== "current_assets") fouten.push(`tegenrekening: "${t.naam}" is geen vlottende activa (current_assets)`);
  return fouten;
}
