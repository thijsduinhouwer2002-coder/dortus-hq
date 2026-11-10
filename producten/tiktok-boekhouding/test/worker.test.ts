// Toetsen (h) en (j) uit ontwerp-d1-worker.md: de Worker (cron en consumer) op een nagebootste D1 en fetch.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { bos, app } from "./ontkoppel-hulp.ts";
import { inst, T0, wereld } from "./wereld.ts";
import { versleutel } from "../src/d1/tokens.ts";
import { consumer, cron, kantVan, GEWOON, LEASE, SNEL, WINKELSLOT, type Omgeving } from "../src/worker.ts";
import worker from "../src/worker.ts";

const NU = T0 + 10 * 86400;
const rij = (db: NepD1, w: string) => db.sqlite.prepare("SELECT * FROM winkels WHERE id = ?").get(w) as Record<string, any>;

async function winkel(db: NepD1, w: string, extra: { volgende_run?: number; snel_teller?: number; ontkoppeld?: boolean } = {}) {
  const tt = await versleutel(bos, w, JSON.stringify({ accessToken: "tt-a", accessTokenVerlooptOp: NU + 86400, refreshToken: "tt-r", refreshTokenVerlooptOp: NU + 100 * 86400 }));
  const mb = await versleutel(bos, w, JSON.stringify({ accessToken: "mb-a", refreshToken: "mb-r", scope: "documents" }));
  db.sqlite
    .prepare(`INSERT INTO winkels (id, shop_id, shop_cipher, tt_tokens, mb_tokens, instellingen, volgende_run, snel_teller, ontkoppeld_op) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`)
    .run(w, `shop-${w}`, `cipher-${w}`, tt, mb, JSON.stringify(inst()), extra.volgende_run ?? 0, extra.snel_teller ?? 0, extra.ontkoppeld ? NU - 10 : null);
}

function omgeving(db: NepD1, fetchFn: typeof fetch) {
  const log: string[] = [];
  const verstuurd: any[][] = [];
  const volgorde: string[] = [];
  const o: Omgeving = {
    db: db as any,
    wachtrij: { sendBatch: async (b) => { volgorde.push("sendBatch"); verstuurd.push(b); } },
    fetchFn, log: (r) => log.push(r), sleutels: bos,
    tiktokApp: { appKey: "k", appSecret: "s" }, moneybirdApp: app, slaap: async () => {},
  };
  return { o, log, verstuurd, volgorde };
}

test("(h) cron: alleen winkels aan de beurt, hoogstens 100, sendBatch vóór de lease, lease 30 minuten", async () => {
  const db = new NepD1();
  for (let i = 0; i < 105; i++) await winkel(db, `w${i}`, { volgende_run: NU - 1000 + i });
  await winkel(db, "toekomst", { volgende_run: NU + 60 });
  await winkel(db, "weg", { ontkoppeld: true });
  const { o, verstuurd, volgorde } = omgeving(db, wereld().fn);
  const batch = db.batch.bind(db);
  db.batch = (async (s: any) => { volgorde.push("batch"); return batch(s); }) as any;
  const uit = await cron(o, NU);
  assert.equal(uit.verstuurd, 100);
  assert.equal(verstuurd.length, 1);
  const ids = verstuurd[0].map((b: any) => b.body.winkel);
  assert.equal(ids.length, 100);
  assert.ok(!ids.includes("toekomst") && !ids.includes("weg") && !ids.includes("w104"));
  assert.deepEqual(volgorde.slice(0, 2), ["sendBatch", "batch"]);
  assert.equal(rij(db, "w0").volgende_run, NU + LEASE);
  assert.equal(rij(db, "w104").volgende_run, NU - 1000 + 104);
  assert.equal(rij(db, "toekomst").volgende_run, NU + 60);
});

test("(h) cron: mislukt sendBatch, dan geen lease (winkel blijft aan de beurt)", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  const { o, log } = omgeving(db, wereld().fn);
  o.wachtrij = { sendBatch: async () => { throw new Error("wachtrij stuk"); } };
  await cron(o, NU);
  assert.equal(rij(db, "a").volgende_run, 0);
  assert.ok(log.some((r) => r.includes("wachtrij stuk")));
});

test("(h) consumer: winkelslot bezet geeft niets doen", async () => {
  const db = new NepD1();
  await winkel(db, "a", { volgende_run: NU + LEASE });
  db.sqlite.prepare("INSERT INTO sloten VALUES ('a', ?, 'ander', ?)").run(WINKELSLOT, NU + 600);
  const w = wereld();
  const { o } = omgeving(db, w.fn);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "slot_bezet");
  assert.equal(w.urls.length, 0);
  assert.equal(rij(db, "a").volgende_run, NU + LEASE);
  assert.equal((db.sqlite.prepare("SELECT eigenaar FROM sloten WHERE winkel = 'a'").get() as any).eigenaar, "ander");
});

test("(h) consumer: twee tegelijk voor één winkel, maar één werkt; tokens alleen onder het winkelslot", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  const w = wereld();
  w.voegToe("701", T0 + 86400, "PAID", [10, 20]);
  let tokenLezingen = 0;
  const prepare = db.prepare.bind(db);
  db.prepare = ((sql: string) => {
    if (/SELECT (tt|mb)_tokens/.test(sql)) {
      tokenLezingen++;
      const slot = db.sqlite.prepare("SELECT tot FROM sloten WHERE winkel = 'a' AND statement_id = ?").get(WINKELSLOT) as any;
      assert.ok(slot && slot.tot > NU, "tokens gelezen zonder winkelslot");
    }
    return prepare(sql);
  }) as any;
  const { o } = omgeving(db, w.fn);
  const [x, y] = await Promise.all([consumer({ winkel: "a" }, o, NU), consumer({ winkel: "a" }, o, NU)]);
  assert.deepEqual([x, y].sort(), ["slot_bezet", "verwerkt"]);
  assert.equal(tokenLezingen, 2); // één keer TikTok, één keer Moneybird
  assert.equal(w.urls.filter((u) => u.includes("/statements") && !u.includes("statement_transactions")).length, 1);
  assert.equal(db.sqlite.prepare("SELECT count(*) n FROM sloten WHERE statement_id = ?").get(WINKELSLOT)!.n, 0, "winkelslot terug");
  assert.equal(rij(db, "a").volgende_run, NU + GEWOON);
});

test("(h) consumer: 15 minuten als het budget op raakt, na 8 keer snel weer 6 uur", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  const w = wereld();
  w.voegToe("702", T0 + 86400, "PAID", Array(60).fill(10)); // past niet in één budget
  const { o } = omgeving(db, w.fn);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  assert.equal(rij(db, "a").volgende_run, NU + SNEL);
  assert.equal(rij(db, "a").snel_teller, 1);
  db.sqlite.prepare("UPDATE winkels SET snel_teller = 8").run();
  w.voegToe("703", T0 + 2 * 86400, "PAID", Array(60).fill(10));
  await consumer({ winkel: "a" }, o, NU + 1000);
  assert.equal(rij(db, "a").volgende_run, NU + 1000 + GEWOON);
  assert.equal(rij(db, "a").snel_teller, 0);
});

test("(h) consumer: winkelfout met kant; ontkoppeld netjes stoppen", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  db.sqlite.prepare("UPDATE winkels SET mb_tokens = NULL WHERE id = 'a'").run();
  const { o } = omgeving(db, wereld().fn);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  const f = JSON.parse(rij(db, "a").winkelfout);
  assert.deepEqual([f.soort, f.kant], ["koppeling_verlopen", "moneybird"]);
  assert.equal(rij(db, "a").volgende_run, NU + GEWOON);

  await winkel(db, "b", { ontkoppeld: true });
  assert.equal(await consumer({ winkel: "b" }, o, NU), "slot_bezet"); // neemSlot weigert bij een ontkoppelde winkel
  assert.equal(kantVan("server", "tiktok"), "tiktok");
  assert.equal(kantVan("server", "moneybird"), "moneybird");
  assert.equal(kantVan("token_verlopen", "moneybird"), "tiktok");
});

test("(h) bericht altijd bevestigd, ook als iets gooit; consumer gooit nooit", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  const { o, log } = omgeving(db, (async () => { throw new Error("boem"); }) as any);
  db.batch = (async () => { throw new Error("D1 stuk"); }) as any;
  assert.equal(await consumer({ winkel: "a" }, o, NU), "fout");
  assert.ok(log.length > 0);
  // De dunne export: kapotte env, toch ack.
  let acks = 0;
  await worker.queue({ messages: [{ body: { winkel: "a" }, ack: () => acks++ }, { body: { winkel: "b" }, ack: () => acks++ }] }, { TOKEN_SLEUTELS: "geen json" } as any);
  assert.equal(acks, 2);
});

test("(j) CPU van één consumer-aanroep met 30 bestellingen (doel onder 5 ms in Node)", async () => {
  const ronde = async () => {
    const db = new NepD1();
    await winkel(db, "a");
    const w = wereld();
    w.voegToe("801", T0 + 86400, "PAID", Array(30).fill(12.5));
    const { o } = omgeving(db, w.fn);
    return { db, o };
  };
  const warm = await ronde();
  await consumer({ winkel: "a" }, warm.o, NU); // opwarmen
  const metingen: number[] = [];
  let st = "";
  for (let i = 0; i < 3; i++) {
    const { o } = await ronde();
    const start = process.cpuUsage();
    const uit = await consumer({ winkel: "a" }, o, NU);
    const d = process.cpuUsage(start);
    assert.equal(uit, "verwerkt");
    st = String((o.db as any).sqlite.prepare("SELECT status FROM statussen").get()?.status);
    metingen.push((d.user + d.system) / 1000);
  }
  const ms = Math.min(...metingen);
  console.log(`(j) CPU consumer-aanroep met 30 bestellingen: ${ms.toFixed(2)} ms (beste van 3: ${metingen.map((m) => m.toFixed(2)).join(", ")}; inclusief nagebootste D1 op node:sqlite en nep-fetch; status na de aanroep: ${st})`);
  if (ms >= 5) console.log(`(j) LET OP: boven het doel van 5 ms; risico voor Tess`);
});
