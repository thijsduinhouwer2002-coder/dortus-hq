// Punt 7 met punt 5: ontkoppelen tussen het verversen bij Moneybird en het opslaan. Het nieuwe paar wordt meteen ingetrokken.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { Budget } from "../src/budget.ts";
import { Ontkoppeld } from "../src/opslag.ts";
import { WinkelStop } from "../src/ophalen.ts";
import { TokenBron, moneybirdSoort, ontsleutel } from "../src/d1/tokens.ts";
import { ontkoppel } from "../src/d1/ontkoppel.ts";
import { app, bos, deps, nepRevoke, NU } from "./ontkoppel-hulp.ts";

/** Nagebootste Moneybird: /oauth/token geeft een nieuw paar, maar vlak voor het antwoord wordt de winkel ontkoppeld. */
async function opzet(tussendoor: (db: NepD1) => Promise<unknown>, revokeStatus = 200) {
  const db = new NepD1("w1");
  const verzoeken: Array<{ pad: string; body: Record<string, string> }> = [];
  const fn = (async (input: any, init: any = {}) => {
    const pad = new URL(String(input)).pathname;
    const body = Object.fromEntries(new URLSearchParams(String(init.body)));
    verzoeken.push({ pad, body });
    if (pad === "/oauth/token") {
      await tussendoor(db);
      return new Response(JSON.stringify({ access_token: "GEHEIM-a2", refresh_token: "GEHEIM-r2", scope: "documents", expires_in: 7200, created_at: NU }), { status: 200 });
    }
    return new Response("{}", { status: revokeStatus });
  }) as typeof fetch;
  const log: string[] = [];
  const budget = new Budget(50);
  const maak = () => new TokenBron({ db, winkel: "w1", soort: moneybirdSoort(app), sleutels: bos, budget, fetchFn: fn, nu: () => NU, log: (r) => log.push(r) });
  assert.equal(await maak().bewaar({ accessToken: "GEHEIM-a1", refreshToken: "GEHEIM-r1", scope: "documents", verlooptOp: NU + 60 }, 0), true);
  return { db, verzoeken, log, budget, maak };
}

const ontkoppelTussendoor = async (db: NepD1) => ontkoppel(db, "w1", "knop", NU, new Budget(50), deps(nepRevoke(200).fn).d);

test("(punt 7) ontkoppeld tussen verversen en opslaan: nieuw refresh token ingetrokken, niets in D1, Ontkoppeld", async () => {
  const o = await opzet(ontkoppelTussendoor);
  await assert.rejects(o.maak().geef(), (e: unknown) => e instanceof Ontkoppeld && !(e instanceof WinkelStop));
  const revokes = o.verzoeken.filter((v) => v.pad === "/oauth/revoke");
  assert.equal(revokes.length, 1);
  assert.deepEqual(revokes[0].body, { client_id: "cid", client_secret: "geheim", token: "GEHEIM-r2" }, "het nieuwe token");
  const r = o.db.sqlite.prepare("SELECT * FROM winkels WHERE id = 'w1'").get() as any;
  assert.ok(!JSON.stringify(r).includes("GEHEIM"));
  // mb_tokens staat er nog alleen voor de taak intrekken van ontkoppel, en bevat het oude paar
  if (r.mb_tokens) assert.equal(JSON.parse(await ontsleutel(bos, "w1", r.mb_tokens)).refreshToken, "GEHEIM-r1");
  assert.deepEqual(o.log, []);
  assert.equal(o.budget.over, 50 - 6, "bewaar vooraf, lezen, verversen, opslaan, lezen, intrekken: alles in hetzelfde budget");
});

test("(punt 7) rij bestaat niet meer tijdens verversen: ook dan ingetrokken en Ontkoppeld", async () => {
  const o = await opzet(async (db) => db.sqlite.prepare("DELETE FROM winkels WHERE id = 'w1'").run());
  await assert.rejects(o.maak().geef(), (e: unknown) => e instanceof Ontkoppeld);
  assert.equal(o.verzoeken.filter((v) => v.pad === "/oauth/revoke" && v.body.token === "GEHEIM-r2").length, 1);
});

test("(punt 7) intrekken van het nieuwe paar mislukt: ALARM, toch Ontkoppeld en nooit koppeling_verlopen", async () => {
  const o = await opzet(ontkoppelTussendoor, 500);
  await assert.rejects(o.maak().geef(), (e: unknown) => e instanceof Ontkoppeld && !(e instanceof WinkelStop));
  assert.equal(o.log.length, 1);
  assert.match(o.log[0], /^ALARM winkel w1/);
});
