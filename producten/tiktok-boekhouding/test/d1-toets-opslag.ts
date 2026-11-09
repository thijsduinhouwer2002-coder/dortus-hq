// D1Opslag op een nagebootste D1, met de velden van GeheugenOpslag die de bestaande toetsen lezen (aantallen en
// markering, vers uit SQLite). Voor toets (a): zelfde toetsen, zelfde uitkomsten.
import { NepD1 } from "./d1-nep.ts";
import { D1Opslag } from "../src/d1/opslag.ts";
import { Budget } from "../src/budget.ts";
import type { AfrekeningStatus, BewaardeBestelling, BewaardeTransacties, Opslag } from "../src/opslag.ts";

export class D1ToetsOpslag implements Opslag {
  readonly db: NepD1;
  readonly binnen: D1Opslag;
  constructor(db = new NepD1("w1"), winkel = "w1") {
    this.db = db;
    // Eigen teller voor D1: toets (a) gaat over dezelfde uitkomsten; de gedeelde pot van 50 toetst (b) apart.
    this.binnen = new D1Opslag(db, winkel, new Budget(100_000));
  }
  private tel(tabel: string) {
    return Number((this.db.sqlite.prepare(`SELECT count(*) AS n FROM ${tabel}`).get() as { n: number }).n);
  }
  get statussen() { return { size: this.tel("statussen") }; }
  get bestellingen() { return { size: this.tel("bestellingen") }; }
  get transacties() { return { size: this.tel("transacties") }; }
  get sloten() { return { size: this.tel("sloten") }; }
  get markering() {
    const r = this.db.sqlite.prepare("SELECT markering FROM winkels WHERE id = 'w1'").get() as { markering: number | null } | undefined;
    return r?.markering ?? undefined;
  }
  get schrijfacties() { return this.binnen.schrijfacties; }

  neemSlot(id: string, eigenaar: string, tot: number, nu: number) { return this.binnen.neemSlot(id, eigenaar, tot, nu); }
  slotTot(id: string, eigenaar: string) { return this.binnen.slotTot(id, eigenaar); }
  geefSlotTerug(id: string, eigenaar: string) { return this.binnen.geefSlotTerug(id, eigenaar); }
  startBoeking(id: string, eigenaar: string, s: AfrekeningStatus, minTot: number) { return this.binnen.startBoeking(id, eigenaar, s, minTot); }
  leesStatus(id: string) { return this.binnen.leesStatus(id); }
  schrijfStatus(id: string, s: AfrekeningStatus) { return this.binnen.schrijfStatus(id, s); }
  wisStatus(id: string) { return this.binnen.wisStatus(id); }
  leesBestelling(id: string, orderId: string) { return this.binnen.leesBestelling(id, orderId); }
  schrijfBestelling(id: string, orderId: string, b: BewaardeBestelling) { return this.binnen.schrijfBestelling(id, orderId, b); }
  leesTransacties(id: string) { return this.binnen.leesTransacties(id); }
  schrijfTransacties(id: string, t: BewaardeTransacties) { return this.binnen.schrijfTransacties(id, t); }
  leesOpen(open: string[]) { return this.binnen.leesOpen(open); }
  leesMarkering() { return this.binnen.leesMarkering(); }
  schrijfMarkering(t: number) { return this.binnen.schrijfMarkering(t); }
}
