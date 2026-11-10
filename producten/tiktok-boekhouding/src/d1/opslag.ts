// D1-versie van de interface Opslag (ontwerp-d1-worker.md, punt 2). Eén exemplaar per winkel en per aanroep.
// Lezen per afrekening in één batch, schrijven gebundeld met de volgende statuswissel, slot altijd vers.
import { GEBOEKT } from "../verwerk.ts";
import { Ontkoppeld, type AfrekeningStatus, type BewaardeBestelling, type BewaardeTransacties, type Opslag, type TellingVast } from "../opslag.ts";

/** Het deel van de D1-API dat we gebruiken (Cloudflare D1Database), zodat de tests een nagebootste versie kunnen geven. */
export interface D1Statement {
  bind(...waarden: unknown[]): D1Statement;
  all<T = Record<string, unknown>>(): Promise<{ results: T[] }>;
  run(): Promise<{ meta: { changes: number } }>;
  first<T = Record<string, unknown>>(): Promise<T | null>;
}
export interface D1 {
  prepare(sql: string): D1Statement;
  batch(stmts: D1Statement[]): Promise<Array<{ results?: unknown[]; meta: { changes: number } }>>;
}
/** Budget uit src/budget.ts: `neem` voor nieuw werk, `neemAfmaken` voor schrijven. */
export interface Teller {
  neem(): void;
  neemAfmaken(): void;
}

/** Afgerond: bewaarde bestellingen en transacties mogen weg (ontwerp punt 3), dezelfde lijst als in verwerk.ts.
 * `wacht_op_abonnement` hoort er niet bij; `fout` en `fout_gegevens` blijven staan tot het opruimen per cron. */
export const AF = GEBOEKT;
/** Een rij boven deze grootte wordt niet bewaard (D1: hoogstens 2 MB per rij). */
export const MAX_RIJ = 1_500_000;

interface Geheugen {
  transacties?: BewaardeTransacties;
  bestellingen: Map<string, BewaardeBestelling>;
}

export class D1Opslag implements Opslag {
  private wachtrij: D1Statement[] = [];
  private geheugen = new Map<string, Geheugen>();
  private markering: { waarde: number | undefined } | undefined;
  /** Gezet zodra D1 "ontkoppeld" meldt (punt 7): daarna geen slot meer en geen enkele schrijfactie. */
  private ontkoppeld = false;
  schrijfacties = 0;

  private readonly db: D1;
  private readonly winkel: string;
  private readonly teller: Teller;

  constructor(db: D1, winkel: string, teller: Teller) {
    this.db = db;
    this.winkel = winkel;
    this.teller = teller;
  }

  // ---- slot ----
  async neemSlot(id: string, eigenaar: string, tot: number, nu: number): Promise<boolean> {
    if (this.ontkoppeld) return false;
    this.teller.neem();
    // Na het slot alles vers; staat er nog iets in de wachtrij (na een mislukte batch), dan blijft het geheugen staan.
    if (!this.wachtrij.length) this.geheugen.delete(id);
    const r = await this.db
      .prepare(
        // Ontkoppelde (of onbekende) winkel: geen rij, dus geen slot, ook als er nog geen slotrij was (punt 7).
        `INSERT INTO sloten (winkel, statement_id, eigenaar, tot)
         SELECT ?, ?, ?, ? WHERE EXISTS (SELECT 1 FROM winkels WHERE id = ? AND ontkoppeld_op IS NULL)
         ON CONFLICT(winkel, statement_id) DO UPDATE SET eigenaar = excluded.eigenaar, tot = excluded.tot
         WHERE sloten.tot <= ? OR sloten.eigenaar = excluded.eigenaar`,
      )
      .bind(this.winkel, id, eigenaar, tot, this.winkel, nu)
      .run();
    return r.meta.changes === 1;
  }

  async slotTot(id: string, eigenaar: string): Promise<number | null> {
    return this.slotMetSchrijven(id, eigenaar, []);
  }

  /** Punt 1: status "boeking gestart" alleen als het slot nog tot `minTot` van ons is, in dezelfde batch als die controle. */
  async startBoeking(id: string, eigenaar: string, s: AfrekeningStatus, minTot: number): Promise<number | null> {
    const st = this.db
      .prepare(
        `INSERT INTO statussen (winkel, statement_id, status, statement_time, opnieuw_sinds, gegevens)
         SELECT ?, ?, ?, ?, ?, ? WHERE EXISTS (SELECT 1 FROM sloten WHERE winkel = ? AND statement_id = ? AND eigenaar = ? AND tot >= ?)
         ON CONFLICT(winkel, statement_id) DO UPDATE SET status = excluded.status, statement_time = excluded.statement_time,
         opnieuw_sinds = excluded.opnieuw_sinds, gegevens = excluded.gegevens`,
      )
      .bind(this.winkel, id, s.status, s.statementTime ?? null, s.opnieuwSinds ?? null, JSON.stringify(s), this.winkel, id, eigenaar, minTot);
    const tot = await this.slotMetSchrijven(id, eigenaar, [st]);
    if (tot !== null && tot >= minTot) this.schrijfacties++;
    return tot;
  }

  /** Slot vers lezen (met `ontkoppeld_op`), na de wachtrij en `ervoor` in dezelfde batch. */
  private async slotMetSchrijven(id: string, eigenaar: string, ervoor: D1Statement[]): Promise<number | null> {
    if (this.ontkoppeld) return null;
    const lees = this.db
      .prepare(`SELECT s.eigenaar, s.tot FROM sloten s JOIN winkels w ON w.id = s.winkel AND w.ontkoppeld_op IS NULL WHERE s.winkel = ? AND s.statement_id = ?`)
      .bind(this.winkel, id);
    const uit = await this.batchMetWachtrij([...ervoor, lees]);
    const rij = (uit.at(-1)?.results?.[0] ?? null) as { eigenaar: string; tot: number } | null;
    return rij && rij.eigenaar === eigenaar ? Number(rij.tot) : null;
  }

  async geefSlotTerug(id: string, eigenaar: string): Promise<void> {
    if (this.ontkoppeld) return; // niets meer om naar te schrijven
    await this.batchMetWachtrij([this.db.prepare(`DELETE FROM sloten WHERE winkel = ? AND statement_id = ? AND eigenaar = ?`).bind(this.winkel, id, eigenaar)]);
  }

  // ---- status ----
  async leesStatus(id: string): Promise<AfrekeningStatus | undefined> {
    this.teller.neem();
    const rij = await this.db.prepare(`SELECT gegevens FROM statussen WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id).first<{ gegevens: string }>();
    return rij ? (JSON.parse(rij.gegevens) as AfrekeningStatus) : undefined;
  }

  async schrijfStatus(id: string, s: AfrekeningStatus, wisTelling = false): Promise<void> {
    this.schrijfacties++;
    const st = this.db
      .prepare(
        `INSERT INTO statussen (winkel, statement_id, status, statement_time, opnieuw_sinds, gegevens) VALUES (?, ?, ?, ?, ?, ?)
         ON CONFLICT(winkel, statement_id) DO UPDATE SET status = excluded.status, statement_time = excluded.statement_time,
         opnieuw_sinds = excluded.opnieuw_sinds, gegevens = excluded.gegevens`,
      )
      .bind(this.winkel, id, s.status, s.statementTime ?? null, s.opnieuwSinds ?? null, JSON.stringify(s));
    const extra = [st];
    if (wisTelling) extra.push(this.db.prepare(`DELETE FROM telling WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id));
    if (AF.includes(s.status) && s.opnieuwSinds === undefined) {
      // Met opnieuwSinds loopt "opnieuw boeken" nog (staat via leesOpen op de lijst): dan niets weggooien.
      // Af: wat voor deze afrekening nog in de wachtrij of in D1 staat hoeft niet meer bewaard (opnieuw boeken haalt opnieuw op).
      extra.push(
        this.db.prepare(`DELETE FROM bestellingen WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id),
        this.db.prepare(`DELETE FROM transacties WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id),
      );
      this.geheugen.delete(id);
    }
    await this.batchMetWachtrij(extra);
  }

  async wisStatus(id: string): Promise<void> {
    this.schrijfacties++;
    await this.batchMetWachtrij([this.db.prepare(`DELETE FROM statussen WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id)]);
  }

  // ---- transacties en bestellingen ----
  private async laad(id: string): Promise<Geheugen> {
    const g = this.geheugen.get(id);
    if (g) return g;
    this.teller.neem();
    const [t, b] = await this.db.batch([
      this.db.prepare(`SELECT gegevens FROM transacties WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id),
      this.db.prepare(`SELECT order_id, gegevens FROM bestellingen WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id),
    ]);
    const nieuw: Geheugen = { bestellingen: new Map() };
    const tr = (t.results?.[0] ?? null) as { gegevens: string } | null;
    if (tr) nieuw.transacties = JSON.parse(tr.gegevens);
    for (const r of (b.results ?? []) as Array<{ order_id: string; gegevens: string }>) nieuw.bestellingen.set(r.order_id, JSON.parse(r.gegevens));
    this.geheugen.set(id, nieuw);
    return nieuw;
  }

  async leesTransacties(id: string) {
    const t = (await this.laad(id)).transacties;
    return t ? structuredClone(t) : undefined;
  }

  async leesBestelling(id: string, orderId: string) {
    const b = (await this.laad(id)).bestellingen.get(orderId);
    return b ? structuredClone(b) : undefined;
  }

  async schrijfTransacties(id: string, t: BewaardeTransacties): Promise<void> {
    this.schrijfacties++;
    (await this.geheugenVoorSchrijven(id)).transacties = structuredClone(t);
    const json = JSON.stringify(t);
    if (json.length > MAX_RIJ) return; // alleen in het geheugen van deze aanroep; te groot om te bewaren
    this.wachtrij.push(
      this.db
        .prepare(`INSERT INTO transacties (winkel, statement_id, gegevens, opgehaald_op) VALUES (?, ?, ?, ?) ON CONFLICT(winkel, statement_id) DO UPDATE SET gegevens = excluded.gegevens, opgehaald_op = excluded.opgehaald_op`)
        .bind(this.winkel, id, json, t.opgehaaldOp),
    );
  }

  async schrijfBestelling(id: string, orderId: string, b: BewaardeBestelling): Promise<void> {
    this.schrijfacties++;
    (await this.geheugenVoorSchrijven(id)).bestellingen.set(orderId, structuredClone(b));
    const json = JSON.stringify(b);
    if (json.length > MAX_RIJ) return;
    this.wachtrij.push(
      this.db
        .prepare(`INSERT INTO bestellingen (winkel, statement_id, order_id, gegevens, opgehaald_op) VALUES (?, ?, ?, ?, ?) ON CONFLICT(winkel, statement_id, order_id) DO UPDATE SET gegevens = excluded.gegevens, opgehaald_op = excluded.opgehaald_op`)
        .bind(this.winkel, id, orderId, json, b.opgehaaldOp),
    );
  }

  private async geheugenVoorSchrijven(id: string): Promise<Geheugen> {
    // Schrijven zonder eerst te lezen komt in verwerk.ts niet voor; laad dan toch, zodat het geheugen compleet blijft.
    return this.geheugen.get(id) ?? (await this.laad(id));
  }

  // ---- lijst en markering ----
  async leesOpen(open: string[]) {
    this.teller.neem();
    const plekken = open.map(() => "?").join(", ") || "''";
    const r = await this.db
      .prepare(`SELECT statement_id, statement_time FROM statussen WHERE winkel = ? AND (status IN (${plekken}) OR opnieuw_sinds IS NOT NULL)`)
      .bind(this.winkel, ...open)
      .all<{ statement_id: string; statement_time: number }>();
    return r.results.map((x) => ({ statementId: x.statement_id, statementTime: Number(x.statement_time) }));
  }

  /** Eén keer uit D1, daarna uit het geheugen (ontwerp: verwerk.ts leest hem aan het eind opnieuw). */
  async leesMarkering(): Promise<number | undefined> {
    if (this.markering) return this.markering.waarde;
    this.teller.neem();
    const r = await this.db.prepare(`SELECT markering FROM winkels WHERE id = ?`).bind(this.winkel).first<{ markering: number | null }>();
    this.markering = { waarde: r?.markering ?? undefined };
    return this.markering.waarde;
  }

  async schrijfMarkering(t: number): Promise<void> {
    this.schrijfacties++;
    const [r] = await this.batchMetWachtrij([this.db.prepare(`UPDATE winkels SET markering = ? WHERE id = ? AND ontkoppeld_op IS NULL`).bind(t, this.winkel)]);
    if (r.meta.changes !== 1) {
      this.ontkoppeld = true;
      throw new Ontkoppeld(`winkel ${this.winkel} bestaat niet in D1 of is ontkoppeld; markering niet bewaard`);
    }
    this.markering = { waarde: t };
  }

  /** Aan het eind van de aanroep: wat nog in de wachtrij staat wegschrijven. */
  async klaar(extra: D1Statement[] = []): Promise<void> {
    if (this.ontkoppeld) return;
    if (this.wachtrij.length || extra.length) await this.batchMetWachtrij(extra);
  }

  // ---- telling (ontwerp-betalen.md, punt 2 stap 3 en 4) ----
  async legTellingVast(id: string, eigenaar: string, t: TellingVast): Promise<{ rij: boolean; ingevoegd: boolean; slot: boolean }> {
    this.schrijfacties++;
    const [ins, lees] = await this.batchMetWachtrij([
      this.db
        .prepare(
          `INSERT OR IGNORE INTO telling (winkel, statement_id, maand, bestellingen)
           SELECT ?, ?, ?, ? WHERE EXISTS (SELECT 1 FROM sloten WHERE winkel = ? AND statement_id = ? AND eigenaar = ? AND tot >= ?)
           AND (? OR ? = 0 OR (SELECT COALESCE(SUM(bestellingen), 0) FROM telling WHERE winkel = ? AND maand = ? AND statement_id <> ?) + ? <= ?)`,
        )
        .bind(this.winkel, id, t.maand, t.bestellingen, this.winkel, id, eigenaar, t.minTot, t.vrij ? 1 : 0, t.bestellingen, this.winkel, t.maand, id, t.bestellingen, t.grens),
      this.db
        .prepare(
          `SELECT EXISTS (SELECT 1 FROM telling WHERE winkel = ? AND statement_id = ?) AS rij,
           EXISTS (SELECT 1 FROM sloten WHERE winkel = ? AND statement_id = ? AND eigenaar = ? AND tot >= ?) AS slot`,
        )
        .bind(this.winkel, id, this.winkel, id, eigenaar, t.minTot),
    ]);
    const r = ((lees.results ?? [])[0] ?? {}) as { rij?: number; slot?: number };
    return { rij: Number(r.rij) === 1, ingevoegd: ins.meta.changes === 1, slot: Number(r.slot) === 1 };
  }

  async wisTelling(id: string, eigenaar: string): Promise<void> {
    this.schrijfacties++;
    await this.batchMetWachtrij([
      this.db
        .prepare(`DELETE FROM telling WHERE winkel = ? AND statement_id = ? AND EXISTS (SELECT 1 FROM sloten WHERE winkel = ? AND statement_id = ? AND eigenaar = ?)`)
        .bind(this.winkel, id, this.winkel, id, eigenaar),
    ]);
  }

  async zetTerug(id: string, vorige: AfrekeningStatus | undefined, wisTelling: boolean): Promise<void> {
    this.schrijfacties++;
    const status = vorige
      ? this.db
          .prepare(
            `INSERT INTO statussen (winkel, statement_id, status, statement_time, opnieuw_sinds, gegevens) VALUES (?, ?, ?, ?, ?, ?)
             ON CONFLICT(winkel, statement_id) DO UPDATE SET status = excluded.status, statement_time = excluded.statement_time,
             opnieuw_sinds = excluded.opnieuw_sinds, gegevens = excluded.gegevens`,
          )
          .bind(this.winkel, id, vorige.status, vorige.statementTime ?? null, vorige.opnieuwSinds ?? null, JSON.stringify(vorige))
      : this.db.prepare(`DELETE FROM statussen WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id);
    const extra = [status];
    if (wisTelling) extra.push(this.db.prepare(`DELETE FROM telling WHERE winkel = ? AND statement_id = ?`).bind(this.winkel, id));
    await this.batchMetWachtrij(extra);
  }

  /** Wachtrij plus `extra` in één batch (één transactie). Afmaken: mag de reserve gebruiken. */
  private async batchMetWachtrij(extra: D1Statement[]) {
    if (this.ontkoppeld) throw new Ontkoppeld();
    this.teller.neemAfmaken();
    const stmts = [...this.wachtrij, ...extra];
    let uit;
    try {
      uit = await this.db.batch(stmts);
    } catch (e) {
      // Trigger uit het schema (punt 7): de hele batch is weggevallen. Nette stop, geen fout en geen onzeker.
      if (/ontkoppeld/.test(String((e as Error)?.message))) {
        this.ontkoppeld = true;
        this.wachtrij = [];
        this.geheugen.clear();
        throw new Ontkoppeld();
      }
      throw e;
    }
    this.wachtrij = []; // pas na gelukte batch: bij een fout blijft alles staan voor een volgende poging
    return uit.slice(stmts.length - extra.length);
  }
}
