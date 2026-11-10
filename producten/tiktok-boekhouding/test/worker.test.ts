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

// Standaard een actief abonnement: deze toetsen gaan over budget en tokens, niet over de gratis grens. Sinds deel 2 van het
// betaalstuk leest de Worker het abonnement uit `winkels.abonnement` (niet meer `magBoeken` uit de instellingen).
const ACTIEF = JSON.stringify({ actief: true, tot: NU + 30 * 86400, id: "sub", opgezegd: false, stand: 1 });
async function winkel(db: NepD1, w: string, extra: { volgende_run?: number; snel_teller?: number; ontkoppeld?: boolean; abonnement?: string | null } = {}) {
  const tt = await versleutel(bos, w, JSON.stringify({ accessToken: "tt-a", accessTokenVerlooptOp: NU + 86400, refreshToken: "tt-r", refreshTokenVerlooptOp: NU + 100 * 86400 }));
  const mb = await versleutel(bos, w, JSON.stringify({ accessToken: "mb-a", refreshToken: "mb-r", scope: "documents" }));
  db.sqlite
    .prepare(`INSERT INTO winkels (id, shop_id, shop_cipher, tt_tokens, mb_tokens, instellingen, volgende_run, snel_teller, ontkoppeld_op, abonnement) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`)
    .run(w, `shop-${w}`, `cipher-${w}`, tt, mb, JSON.stringify(inst()), extra.volgende_run ?? 0, extra.snel_teller ?? 0, extra.ontkoppeld ? NU - 10 : null, extra.abonnement === undefined ? ACTIEF : extra.abonnement);
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
    if (/^SELECT\b[^;]*\b(tt|mb)_tokens\b[^;]*FROM winkels/.test(sql)) {
      tokenLezingen++;
      const slot = db.sqlite.prepare("SELECT tot FROM sloten WHERE winkel = 'a' AND statement_id = ?").get(WINKELSLOT) as any;
      assert.ok(slot && slot.tot > NU, "tokens gelezen zonder winkelslot");
    }
    return prepare(sql);
  }) as any;
  const { o } = omgeving(db, w.fn);
  const [x, y] = await Promise.all([consumer({ winkel: "a" }, o, NU), consumer({ winkel: "a" }, o, NU)]);
  assert.deepEqual([x, y].sort(), ["slot_bezet", "verwerkt"]);
  assert.equal(tokenLezingen, 1); // winkelrij en beide tokens in één query (TokenBron.vanRij)
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

test("(h) consumer: geen TikTok-tokens in de winkelrij: koppeling_verlopen aan de kant van TikTok, niets verstuurd", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  db.sqlite.prepare("UPDATE winkels SET tt_tokens = NULL WHERE id = 'a'").run();
  const w = wereld();
  const { o } = omgeving(db, w.fn);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  const f = JSON.parse(rij(db, "a").winkelfout);
  assert.deepEqual([f.soort, f.kant], ["koppeling_verlopen", "tiktok"]);
  assert.equal(w.urls.length, 0);
});

test("(h) consumer: een D1-query minder per token dan vroeger (één leesquery op winkels vóór het werk)", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  const w = wereld();
  w.voegToe("703", T0 + 86400, "PAID", [10]);
  const selects: string[] = [];
  const prepare = db.prepare.bind(db);
  db.prepare = ((sql: string) => { if (/^SELECT\b[^;]*FROM winkels/.test(sql)) selects.push(sql); return prepare(sql); }) as any;
  const { o } = omgeving(db, w.fn);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  assert.equal(selects.filter((q) => /tt_tokens|mb_tokens|shop_cipher/.test(q)).length, 1, selects.join("\n"));
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

test("(h) 401 van Moneybird midden in de run: één keer verversen en opnieuw in dezelfde aanroep (TokenBron.met)", async () => {
  const db = new NepD1();
  await winkel(db, "a");
  const w = wereld();
  w.voegToe("704", T0 + 86400, "PAID", [10]);
  let ververst = 0;
  let eerste401 = true;
  const fn = (async (input: any, init: any = {}) => {
    const u = String(input);
    if (u.includes("/oauth/token")) { ververst++; return new Response(JSON.stringify({ access_token: "mb-a2", refresh_token: "mb-r2", scope: "documents" })); }
    if (u.includes("moneybird") && eerste401) { eerste401 = false; return new Response(JSON.stringify({ error: "verlopen" }), { status: 401 }); }
    return w.fn(input, init);
  }) as typeof fetch;
  const { o } = omgeving(db, fn);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  assert.equal(ververst, 1);
  assert.equal(rij(db, "a").winkelfout, null);
  assert.equal(rij(db, "a").mb_versie, 1);
  assert.equal(w.docs.size, 1, "na het verversen toch geboekt");
});

// (j) Meten in de toets zelf, na een opwarmrun.
async function meetCpu() {
  const ronde = async () => {
    const db = new NepD1();
    await winkel(db, "a");
    const w = wereld();
    w.voegToe("801", T0 + 86400, "PAID", Array(30).fill(12.5));
    return omgeving(db, w.fn).o;
  };
  await consumer({ winkel: "a" }, await ronde(), NU); // opwarmen
  const metingen: number[] = [];
  let st = "";
  for (let i = 0; i < 3; i++) {
    const o = await ronde();
    const start = process.cpuUsage();
    const uit = await consumer({ winkel: "a" }, o, NU);
    const d = process.cpuUsage(start);
    if (uit !== "verwerkt") throw new Error(`consumer gaf ${uit}`);
    st = String((o.db as any).sqlite.prepare("SELECT status FROM statussen").get()?.status);
    metingen.push((d.user + d.system) / 1000);
  }
  return { ms: Math.min(...metingen), metingen, st };
}
test("(j) CPU van één consumer-aanroep met 30 bestellingen onder 5 ms in Node", async (t) => {
  const cpu = await meetCpu();
  const cpuTekst = `${cpu.ms.toFixed(2)} ms (beste van 3: ${cpu.metingen.map((m) => m.toFixed(2)).join(", ")}; inclusief nagebootste D1 op node:sqlite en nep-fetch; status na de aanroep: ${cpu.st})`;
  console.log(`(j) CPU consumer-aanroep met 30 bestellingen: ${cpuTekst}`);
  // Besluit Jet: boven 5 ms een bekende fout (todo), maar de assert loopt wel echt.
  if (cpu.ms >= 5) t.todo("CPU boven 5 ms in Node, risico bij Tess");
  assert.ok(cpu.ms < 5, `CPU ${cpuTekst}`);
});

test("(betalen deel 2) consumer: abonnement komt uit winkels.abonnement, niet uit magBoeken in de instellingen", async () => {
  for (const [naam, kolom, verwacht] of [
    ["geen abonnement", null, "wacht_op_abonnement"],
    ["tot voorbij", JSON.stringify({ actief: true, tot: NU - 1, stand: 1 }), "wacht_op_abonnement"],
    ["kapotte JSON", "{", "wacht_op_abonnement"],
    ["actief", ACTIEF, "geboekt"],
  ] as const) {
    const db = new NepD1();
    await winkel(db, "a", { abonnement: kolom }); // instellingen hebben magBoeken: true, dat telt niet
    const w = wereld();
    w.voegToe("801", T0 + 86400, "PAID", Array(31).fill(10));
    const { o } = omgeving(db, w.fn);
    for (let i = 0; i < 4; i++) await consumer({ winkel: "a" }, o, NU + i * 1000);
    const st = db.sqlite.prepare("SELECT status FROM statussen WHERE statement_id = '801'").get() as { status: string } | undefined;
    assert.equal(st?.status, verwacht, naam);
  }
});
