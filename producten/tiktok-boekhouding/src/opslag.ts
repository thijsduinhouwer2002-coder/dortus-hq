// Opslag van de product-laag (ontwerp-productlaag.md, kop "Slot en opslag"). Interface plus een versie in het geheugen
// voor de tests; de echte versie komt in D1 (voorwaardelijke INSERT voor het slot), niet in deze stap.
import type { AfrekeningKop, BestellingTransacties, Transactie } from "../../tiktok-shop-basis/src/endpoints.ts";

export interface BewaardeBestelling {
  antwoord: BestellingTransacties;
  /** Unix-seconden: wanneer opgehaald. "Opnieuw boeken sinds T" telt alleen wat na T is opgehaald. */
  opgehaaldOp: number;
}

/** Kop en transacties van een afrekening, zodat een grote afrekening niet elke aanroep opnieuw alle pagina's kost. */
export interface BewaardeTransacties {
  kop: AfrekeningKop | undefined;
  transacties: Transactie[];
  opgehaaldOp: number;
}

export interface AfrekeningStatus {
  status: string;
  reden?: string;
  /** Unix-seconden van de laatste wijziging. */
  sinds: number;
  documentId?: string;
  vingerafdruk?: string;
  /** Tijdelijke fouten: aantal runs en het moment van de eerste. */
  pogingen?: number;
  eerstePoging?: number;
  /** "Opnieuw boeken of proberen sinds T": gezet door de knop, weg als het af is. */
  opnieuwSinds?: number;
  /** Fout bij opnieuw boeken; de oude status (bijv. geboekt) blijft dan staan. */
  opnieuwFout?: string;
  statementTime?: number;
  [veld: string]: unknown;
}

export interface Opslag {
  /** true als het slot nu van `eigenaar` is (nieuw, of het oude was verlopen). */
  neemSlot(statementId: string, eigenaar: string, totSeconden: number, nu: number): Promise<boolean>;
  /** Tot wanneer het slot van `eigenaar` geldig is, of null als het niet (meer) van hem is. */
  slotTot(statementId: string, eigenaar: string): Promise<number | null>;
  geefSlotTerug(statementId: string, eigenaar: string): Promise<void>;
  leesStatus(statementId: string): Promise<AfrekeningStatus | undefined>;
  schrijfStatus(statementId: string, s: AfrekeningStatus): Promise<void>;
  leesBestelling(statementId: string, orderId: string): Promise<BewaardeBestelling | undefined>;
  schrijfBestelling(statementId: string, orderId: string, b: BewaardeBestelling): Promise<void>;
  leesTransacties(statementId: string): Promise<BewaardeTransacties | undefined>;
  schrijfTransacties(statementId: string, t: BewaardeTransacties): Promise<void>;
  /** Afrekeningen op de eigen lijst (ze houden de markering niet vast) en afrekeningen met "opnieuw sinds". */
  leesOpen(open: string[]): Promise<Array<{ statementId: string; statementTime: number }>>;
  leesMarkering(): Promise<number | undefined>;
  schrijfMarkering(statementTime: number): Promise<void>;
}

export class GeheugenOpslag implements Opslag {
  readonly sloten = new Map<string, { eigenaar: string; tot: number }>();
  readonly statussen = new Map<string, AfrekeningStatus>();
  readonly bestellingen = new Map<string, BewaardeBestelling>();
  readonly transacties = new Map<string, BewaardeTransacties>();
  markering: number | undefined;
  /** Aantal schrijfacties, voor toetsen als "niets geschreven". */
  schrijfacties = 0;

  async neemSlot(id: string, eigenaar: string, tot: number, nu: number) {
    const s = this.sloten.get(id);
    if (s && s.eigenaar !== eigenaar && s.tot > nu) return false;
    this.sloten.set(id, { eigenaar, tot });
    return true;
  }
  async slotTot(id: string, eigenaar: string) {
    const s = this.sloten.get(id);
    return s && s.eigenaar === eigenaar ? s.tot : null;
  }
  async geefSlotTerug(id: string, eigenaar: string) {
    if (this.sloten.get(id)?.eigenaar === eigenaar) this.sloten.delete(id);
  }
  async leesStatus(id: string) {
    const s = this.statussen.get(id);
    return s ? structuredClone(s) : undefined;
  }
  async schrijfStatus(id: string, s: AfrekeningStatus) {
    this.schrijfacties++;
    this.statussen.set(id, structuredClone(s));
  }
  async leesBestelling(id: string, orderId: string) {
    const b = this.bestellingen.get(`${id}/${orderId}`);
    return b ? structuredClone(b) : undefined;
  }
  async schrijfBestelling(id: string, orderId: string, b: BewaardeBestelling) {
    this.schrijfacties++;
    this.bestellingen.set(`${id}/${orderId}`, structuredClone(b));
  }
  async leesTransacties(id: string) {
    const t = this.transacties.get(id);
    return t ? structuredClone(t) : undefined;
  }
  async schrijfTransacties(id: string, t: BewaardeTransacties) {
    this.schrijfacties++;
    this.transacties.set(id, structuredClone(t));
  }
  async leesOpen(open: string[]) {
    return [...this.statussen].filter(([, s]) => open.includes(s.status) || s.opnieuwSinds !== undefined).map(([statementId, s]) => ({ statementId, statementTime: Number(s.statementTime) }));
  }
  async leesMarkering() {
    return this.markering;
  }
  async schrijfMarkering(t: number) {
    this.schrijfacties++;
    this.markering = t;
  }
}
