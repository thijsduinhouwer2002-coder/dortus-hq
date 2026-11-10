// Toets (h), punt 5 van ontwerp-d1-worker.md: een 401 midden in de run geeft één keer verversen aan de juiste kant.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { bos, app } from "./ontkoppel-hulp.ts";
import { inst, T0, wereld } from "./wereld.ts";
import { versleutel } from "../src/d1/tokens.ts";
import { consumer, type Omgeving } from "../src/worker.ts";

const NU = T0 + 10 * 86400;
const rij = (db: NepD1) => db.sqlite.prepare("SELECT * FROM winkels WHERE id = 'a'").get() as Record<string, any>;

async function opzet(tt401: number, mb401: number) {
  const db = new NepD1();
  const tt = await versleutel(bos, "a", JSON.stringify({ accessToken: "tt-a", accessTokenVerlooptOp: NU + 86400, refreshToken: "tt-r", refreshTokenVerlooptOp: NU + 100 * 86400 }));
  const mb = await versleutel(bos, "a", JSON.stringify({ accessToken: "mb-a", refreshToken: "mb-r", scope: "documents" }));
  db.sqlite.prepare(`INSERT INTO winkels (id, shop_id, shop_cipher, tt_tokens, mb_tokens, instellingen) VALUES ('a', 's', 'c', ?, ?, ?)`).run(tt, mb, JSON.stringify(inst()));
  const w = wereld();
  w.voegToe("901", T0 + 86400, "PAID", [10]);
  const tel = { ttVervers: 0, mbVervers: 0 };
  const fn = (async (input: any, init: any = {}) => {
    const u = String(input);
    if (u.includes("auth.tiktok-shops.com")) {
      tel.ttVervers++;
      return new Response(JSON.stringify({ code: 0, message: "Success", request_id: "r", data: { access_token: `tt-a${tel.ttVervers + 1}`, access_token_expire_in: NU + 86400, refresh_token: "tt-r2", refresh_token_expire_in: NU + 100 * 86400, open_id: "o", seller_name: "n", seller_base_region: "NL", user_type: 0, granted_scopes: [] } }));
    }
    if (u.includes("/oauth/token")) { tel.mbVervers++; return new Response(JSON.stringify({ access_token: "mb-a2", refresh_token: "mb-r2", scope: "documents" })); }
    if (u.includes("moneybird") && mb401 > 0) { mb401--; return new Response(JSON.stringify({ error: "verlopen" }), { status: 401 }); }
    if (!u.includes("moneybird") && u.includes("/finance/") && tt401 > 0) { tt401--; return new Response(JSON.stringify({ code: 105002, message: "token verlopen", request_id: "r" }), { status: 401 }); }
    return w.fn(input, init);
  }) as typeof fetch;
  const log: string[] = [];
  const o: Omgeving = { db: db as any, wachtrij: { sendBatch: async () => {} }, fetchFn: fn, log: (r) => log.push(r), sleutels: bos, tiktokApp: { appKey: "k", appSecret: "s" }, moneybirdApp: app, slaap: async () => {} };
  return { db, w, tel, o, log };
}

test("(h) één 401 van TikTok midden in de run: alleen TikTok ververst, run gaat door", async () => {
  const { db, w, tel, o } = await opzet(1, 0);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  assert.deepEqual(tel, { ttVervers: 1, mbVervers: 0 });
  assert.equal(rij(db).tt_versie, 1);
  assert.equal(rij(db).mb_versie, 0);
  assert.equal(rij(db).winkelfout, null);
  assert.equal(w.docs.size, 1, "na het verversen toch geboekt");
});

test("(h) twee keer 401 van TikTok: koppeling_verlopen aan de kant van TikTok, Moneybird niet ververst", async () => {
  const { db, tel, o } = await opzet(2, 0);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  const f = JSON.parse(rij(db).winkelfout);
  assert.deepEqual([f.soort, f.kant], ["koppeling_verlopen", "tiktok"]);
  assert.deepEqual(tel, { ttVervers: 1, mbVervers: 0 });
  assert.equal(rij(db).mb_versie, 0);
});

test("(h) twee keer 401 van Moneybird: koppeling_verlopen aan de kant van Moneybird, TikTok niet ververst", async () => {
  const { db, tel, o } = await opzet(0, 2);
  assert.equal(await consumer({ winkel: "a" }, o, NU), "verwerkt");
  const f = JSON.parse(rij(db).winkelfout);
  assert.deepEqual([f.soort, f.kant], ["koppeling_verlopen", "moneybird"]);
  assert.deepEqual(tel, { ttVervers: 0, mbVervers: 1 });
  assert.equal(rij(db).tt_versie, 0);
});
