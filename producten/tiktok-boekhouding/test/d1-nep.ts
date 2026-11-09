// Nagebootste D1 op node:sqlite (ontwerp-d1-worker.md, "Af als"): zelfde SQL, telt queries (batch is één),
// en kan een batch laten mislukken om "alles of niets" te toetsen.
import { DatabaseSync } from "node:sqlite";
import { readFileSync } from "node:fs";

export interface D1Resultaat<T = Record<string, unknown>> { results: T[]; meta: { changes: number }; success: true }

export class NepStatement {
  readonly db: NepD1;
  readonly sql: string;
  readonly waarden: unknown[];
  constructor(db: NepD1, sql: string, waarden: unknown[] = []) {
    this.db = db;
    this.sql = sql;
    this.waarden = waarden;
  }
  bind(...w: unknown[]) { return new NepStatement(this.db, this.sql, w); }
  voer(): D1Resultaat {
    const st = this.db.sqlite.prepare(this.sql);
    const w = this.waarden.map((x) => (x === undefined ? null : x)) as any[];
    if (/^\s*(select|with)/i.test(this.sql) || /returning/i.test(this.sql)) return { results: st.all(...w) as any, meta: { changes: 0 }, success: true };
    const r = st.run(...w);
    return { results: [], meta: { changes: Number(r.changes) }, success: true };
  }
  async all<T>() { this.db.tel(); return this.voer() as D1Resultaat<T>; }
  async run() { this.db.tel(); return this.voer(); }
  async first<T>() { this.db.tel(); return (this.voer().results[0] ?? null) as T | null; }
}

export class NepD1 {
  readonly sqlite = new DatabaseSync(":memory:");
  queries = 0;
  /** Zet op een getal n: de batch faalt bij statement n (0-geteld). Eén keer. */
  faalBijStatement: number | undefined;
  constructor() {
    this.sqlite.exec(readFileSync(new URL("../src/d1/schema.sql", import.meta.url), "utf8"));
  }
  tel() { this.queries++; }
  prepare(sql: string) { return new NepStatement(this, sql); }
  async batch(stmts: NepStatement[]) {
    this.tel();
    this.sqlite.exec("BEGIN");
    try {
      const uit = stmts.map((s, i) => {
        if (this.faalBijStatement === i) { this.faalBijStatement = undefined; throw new Error("nagebootste D1-fout"); }
        return s.voer();
      });
      this.sqlite.exec("COMMIT");
      return uit;
    } catch (e) {
      this.sqlite.exec("ROLLBACK");
      throw e;
    }
  }
}
