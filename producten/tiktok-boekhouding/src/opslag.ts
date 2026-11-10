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

/** De winkel is ontkoppeld (ontwerp-d1-worker.md, punt 7): de opslag weigert elke schrijfactie. Nette stop, geen fout. */
export class Ontkoppeld extends Error {
  readonly ontkoppeld = true;
  constructor(bericht = "winkel is ontkoppeld; niets meer geschreven") {
    super(bericht);
    this.name = "Ontkoppeld";
  }
}

export function isOntkoppeld(e: unknown): e is Ontkoppeld {
  return (e as { ontkoppeld?: unknown })?.ontkoppeld === true;
}

export interface Opslag {
  /** true als het slot nu van `eigenaar` is (nieuw, of het oude was verlopen). */
  neemSlot(statementId: string, eigenaar: string, totSeconden: number, nu: number): Promise<boolean>;
  /** Tot wanneer het slot van `eigenaar` geldig is, of null als het niet (meer) van hem is. */
  slotTot(statementId: string, eigenaar: string): Promise<number | null>;
  geefSlotTerug(statementId: string, eigenaar: string): Promise<void>;
  /**
   * "Boeking gestart" (ontwerp-d1-worker.md, punt 1): schrijft `s` alleen als het slot van `eigenaar` nog minstens tot
   * `minTot` geldt, in dezelfde schrijfactie als die controle. Geeft terug tot wanneer het slot geldt (null: niet van hem).
   */
  startBoeking(statementId: string, eigenaar: string, s: AfrekeningStatus, minTot: number): Promise<number | null>;
  leesStatus(statementId: string): Promise<AfrekeningStatus | undefined>;
  /** `wisTelling`: de telling van deze afrekening in dezelfde schrijfactie weg (stap 4 bij `faal`, ontwerp-betalen.md). */
  schrijfStatus(statementId: string, s: AfrekeningStatus, wisTelling?: boolean): Promise<void>;
  /** Alleen om "boeking gestart" terug te draaien als er eerder geen status was. */
  wisStatus(statementId: string): Promise<void>;
  leesBestelling(statementId: string, orderId: string): Promise<BewaardeBestelling | undefined>;
  schrijfBestelling(statementId: string, orderId: string, b: BewaardeBestelling): Promise<void>;
  leesTransacties(statementId: string): Promise<BewaardeTransacties | undefined>;
  schrijfTransacties(statementId: string, t: BewaardeTransacties): Promise<void>;
  /** Afrekeningen op de eigen lijst (ze houden de markering niet vast) en afrekeningen met "opnieuw sinds". */
  leesOpen(open: string[]): Promise<Array<{ statementId: string; statementTime: number }>>;
  leesMarkering(): Promise<number | undefined>;
  schrijfMarkering(statementTime: number): Promise<void>;
  /**
   * Stap 3 van ontwerp-betalen.md, punt 2: de telling vastleggen, alleen als het slot van `eigenaar` nog tot `minTot` geldt
   * en (`vrij`, of `bestellingen` is 0, of de som van de maand zonder deze afrekening plus `bestellingen` hoogstens `grens` is). In één schrijfactie
   * (D1: één batch, één transactie), zodat twee aanroepen tegelijk samen niet over de grens komen. `rij`: er staat nu een
   * rij voor deze afrekening (ook een van een eerdere poging); `ingevoegd`: deze aanroep voegde hem in; `slot`: het slot
   * gold nog tot `minTot` (zo niet, dan is "geen rij" geen grens maar een verloren slot).
   */
  legTellingVast(statementId: string, eigenaar: string, t: TellingVast): Promise<{ rij: boolean; ingevoegd: boolean; slot: boolean }>;
  /** Telling van deze afrekening weg (stap 4: alleen als deze poging hem invoegde), en alleen zolang het slot nog van `eigenaar` is. */
  wisTelling(statementId: string, eigenaar: string): Promise<void>;
  /** `terug()` van stap 4: status van daarvoor terug (of weg) en, als `wisTelling`, de telling weg, in één schrijfactie. */
  zetTerug(statementId: string, vorige: AfrekeningStatus | undefined, wisTelling: boolean): Promise<void>;
  /**
   * De telling van de winkel (afrekening naar maand en bestellingen), voor stap 0 tot 2. D1: één query per aanroep, daarna
   * bijgehouden bij eigen schrijfacties. Mag iets achterlopen: stap 3 (de SQL) beslist.
   */
  leesTelling(): Promise<Map<string, { maand: string; bestellingen: number }>>;
  /**
   * Maandwissel (stap 4b): `wacht_op_abonnement` met `statement_time` vóór `grens` en zonder knop wordt `wacht_ouder`,
   * bewaarde transacties en bestellingen daarvan weg. Geeft de omgezette afrekeningen terug.
   */
  maandwissel(grens: number): Promise<string[]>;
}

export interface TellingVast {
  maand: string;
  bestellingen: number;
  /** Abonnement actief of vrijgesteld: geen grens. */
  vrij: boolean;
  grens: number;
  minTot: number;
}

export class GeheugenOpslag implements Opslag {
  readonly sloten = new Map<string, { eigenaar: string; tot: number }>();
  readonly statussen = new Map<string, AfrekeningStatus>();
  readonly bestellingen = new Map<string, BewaardeBestelling>();
  readonly transacties = new Map<string, BewaardeTransacties>();
  readonly telling = new Map<string, { maand: string; bestellingen: number }>();
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
  async startBoeking(id: string, eigenaar: string, s: AfrekeningStatus, minTot: number) {
    const tot = await this.slotTot(id, eigenaar);
    if (tot !== null && tot >= minTot) await this.schrijfStatus(id, s);
    return tot;
  }
  async leesStatus(id: string) {
    const s = this.statussen.get(id);
    return s ? structuredClone(s) : undefined;
  }
  async schrijfStatus(id: string, s: AfrekeningStatus, wisTelling = false) {
    this.schrijfacties++;
    this.statussen.set(id, structuredClone(s));
    if (wisTelling) this.telling.delete(id);
    if (s.status === "wacht_ouder" && s.opnieuwSinds === undefined) this.wisBewaard(id);
  }
  private wisBewaard(id: string) {
    this.transacties.delete(id);
    for (const k of [...this.bestellingen.keys()]) if (k.startsWith(`${id}/`)) this.bestellingen.delete(k);
  }
  async leesTelling() {
    return new Map([...this.telling].map(([k, v]) => [k, { ...v }]));
  }
  async maandwissel(grens: number) {
    this.schrijfacties++;
    const ids: string[] = [];
    for (const [id, s] of this.statussen) {
      if (s.status === "wacht_op_abonnement" && (s.statementTime ?? Infinity) < grens && s.opnieuwSinds === undefined) {
        this.statussen.set(id, { ...s, status: "wacht_ouder" });
        this.wisBewaard(id);
        ids.push(id);
      }
    }
    return ids;
  }
  async wisStatus(id: string) {
    this.schrijfacties++;
    this.statussen.delete(id);
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
  async legTellingVast(id: string, eigenaar: string, t: TellingVast) {
    this.schrijfacties++;
    const tot = await this.slotTot(id, eigenaar);
    let ingevoegd = false;
    if (tot !== null && tot >= t.minTot && !this.telling.has(id)) {
      const som = [...this.telling].filter(([k, r]) => k !== id && r.maand === t.maand).reduce((n, [, r]) => n + r.bestellingen, 0);
      if (t.vrij || t.bestellingen === 0 || som + t.bestellingen <= t.grens) {
        this.telling.set(id, { maand: t.maand, bestellingen: t.bestellingen });
        ingevoegd = true;
      }
    }
    return { rij: this.telling.has(id), ingevoegd, slot: tot !== null && tot >= t.minTot };
  }
  async wisTelling(id: string, eigenaar: string) {
    this.schrijfacties++;
    if (this.sloten.get(id)?.eigenaar === eigenaar) this.telling.delete(id);
  }
  async zetTerug(id: string, vorige: AfrekeningStatus | undefined, wisTelling: boolean) {
    this.schrijfacties++;
    if (vorige) this.statussen.set(id, structuredClone(vorige));
    else this.statussen.delete(id);
    if (wisTelling) this.telling.delete(id);
  }
}
