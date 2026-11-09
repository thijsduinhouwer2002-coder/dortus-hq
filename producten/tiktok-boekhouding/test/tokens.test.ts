// Toets (g) uit ontwerp-d1-worker.md: tokens versleuteld in D1, verversen, tegelijk, 401, sleutels, ontkoppeld.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { Budget } from "../src/budget.ts";
import { Ontkoppeld } from "../src/opslag.ts";
import { WinkelStop } from "../src/ophalen.ts";
import { TokenBron, moneybirdSoort, ontsleutel, tiktokSoort, versleutel, type Sleutelbos, type TokenSoort } from "../src/d1/tokens.ts";
import type { Tokens } from "../../tiktok-shop-basis/src/auth.ts";

const NU = 1_800_000_000;
const DAG = 24 * 3600;
const bos: Sleutelbos = { huidig: "v1", sleutels: { v1: crypto.getRandomValues(new Uint8Array(32)) } };

function tokens(n: number, accessOver: number, refreshOver = 60 * DAG): Tokens {
  return {
    accessToken: `GEHEIM-access-${n}`, accessTokenVerlooptOp: NU + accessOver,
    refreshToken: `GEHEIM-refresh-${n}`, refreshTokenVerlooptOp: NU + refreshOver,
    openId: "o", sellerName: "s", sellerBaseRegion: "NL", userType: 0, grantedScopes: [],
  };
}

/** Nagebootste TikTok: verversen geeft een nieuw paar en maakt het oude refresh token ongeldig. */
function nepTikTok(start: number) {
  const server = { geldig: `GEHEIM-refresh-${start}`, n: start, geslaagd: 0, aanroepen: 0 };
  const soort: TokenSoort<Tokens> = {
    kolom: "tt",
    refreshToken: (t) => t.refreshToken,
    accessVerlooptOp: (t) => t.accessTokenVerlooptOp,
    refreshVerlooptOp: (t) => t.refreshTokenVerlooptOp,
    async ververs(r, fetchFn) {
      server.aanroepen++;
      await fetchFn("https://nep/ververs"); // telt in het budget
      await new Promise((x) => setTimeout(x, 5));
      if (r !== server.geldig) throw Object.assign(new Error("refresh token ongeldig"), { httpStatus: 400 });
      server.n++;
      server.geslaagd++;
      server.geldig = `GEHEIM-refresh-${server.n}`;
      return tokens(server.n, 4 * 3600);
    },
  };
  return { server, soort };
}
const nepFetch = (async () => new Response("{}")) as typeof fetch;

async function opzet(accessOver: number, refreshOver?: number) {
  const db = new NepD1("w1", "w2");
  const { server, soort } = nepTikTok(1);
  const maak = (budget = new Budget(50)) => new TokenBron({ db, winkel: "w1", soort, sleutels: bos, budget, fetchFn: nepFetch, nu: () => NU });
  assert.equal(await maak().bewaar(tokens(1, accessOver, refreshOver), 0), true);
  return { db, server, maak };
}

const fout401 = () => Object.assign(new Error("401"), { httpStatus: 401 });

test("(g) de tekst van het token staat nergens in D1", async () => {
  const { db, maak } = await opzet(4 * 3600);
  await maak().geef();
  const alles = JSON.stringify(db.sqlite.prepare("SELECT * FROM winkels").all());
  assert.ok(!alles.includes("GEHEIM"), alles);
  assert.match(String((db.sqlite.prepare("SELECT tt_tokens t FROM winkels WHERE id='w1'").get() as any).t), /^v1\.[^.]+\.[^.]+$/);
  const b = await maak().lees();
  assert.equal(b.tokens.accessToken, "GEHEIM-access-1");
});

test("(g) verversen binnen een uur, niet daarbuiten; D1 en verversen tellen in het budget", async () => {
  const buiten = await opzet(3601);
  assert.equal((await buiten.maak().geef()).tokens.accessToken, "GEHEIM-access-1");
  assert.equal(buiten.server.aanroepen, 0);

  const binnen = await opzet(3600);
  const budget = new Budget(50);
  const u = await binnen.maak(budget).geef();
  assert.equal(u.tokens.accessToken, "GEHEIM-access-2");
  assert.equal(binnen.server.geslaagd, 1);
  assert.equal(budget.over, 47, "lezen, verversen, opslaan");
  assert.equal(budget.opslag, 2);
  const rij = binnen.db.sqlite.prepare("SELECT tt_versie v FROM winkels WHERE id='w1'").get() as any;
  assert.equal(Number(rij.v), 2);
  assert.equal((await binnen.maak().lees()).tokens.accessToken, "GEHEIM-access-2", "het nieuwe paar staat vast");
});

test("(g) waarschuwing als het refresh token binnen 14 dagen verloopt", async () => {
  assert.equal((await (await opzet(4 * 3600, 14 * DAG)).maak().geef()).waarschuwing, "refresh_token_verloopt");
  assert.equal((await (await opzet(4 * 3600, 15 * DAG)).maak().geef()).waarschuwing, undefined);
});

test("(g) roterend refresh token: een eerdere aanroep ververste al, deze leest opnieuw in plaats van koppeling_verlopen", async () => {
  // Gelijktijdig verversen is bij roterende tokens niet veilig; daarvoor zorgt het winkelslot. Hier na elkaar.
  const { db, server, maak } = await opzet(60);
  const a = maak();
  await a.lees();
  const b = await maak().geef();
  const a2 = await a.geef();
  assert.equal(server.geslaagd, 1);
  assert.equal(a2.tokens.accessToken, "GEHEIM-access-2");
  assert.equal(b.tokens.accessToken, "GEHEIM-access-2");
  assert.equal(Number((db.sqlite.prepare("SELECT tt_versie v FROM winkels WHERE id='w1'").get() as any).v), 2);
});

test("(g) twee aanroepen tegelijk bij een server die het oude refresh token laat staan: opslaan één keer, de ander leest opnieuw", async () => {
  const { db } = await opzet(60);
  let n = 10;
  const soort: TokenSoort<Tokens> = { kolom: "tt", refreshToken: (t) => t.refreshToken, accessVerlooptOp: (t) => t.accessTokenVerlooptOp, ververs: async () => tokens(++n, 4 * 3600) };
  const bron = () => new TokenBron({ db, winkel: "w1", soort, sleutels: bos, budget: new Budget(50), fetchFn: nepFetch, nu: () => NU });
  const [a, b] = await Promise.all([bron().geef(), bron().geef()]);
  assert.equal(a.tokens.accessToken, b.tokens.accessToken);
  assert.equal(Number((db.sqlite.prepare("SELECT tt_versie v FROM winkels WHERE id='w1'").get() as any).v), 2);
});

test("(g) 401: één keer verversen en opnieuw; tweede 401 geeft koppeling_verlopen", async () => {
  const { server, maak } = await opzet(4 * 3600);
  const gebruikt: string[] = [];
  const goed = await maak().met(async (t) => {
    gebruikt.push(t.accessToken);
    if (gebruikt.length === 1) throw fout401();
    return "ok";
  });
  assert.equal(goed, "ok");
  assert.deepEqual(gebruikt, ["GEHEIM-access-1", "GEHEIM-access-2"]);

  const bron = maak();
  await assert.rejects(
    bron.met(async () => { throw fout401(); }),
    (e: unknown) => e instanceof WinkelStop && e.soort === "koppeling_verlopen",
  );
  assert.equal(server.geslaagd, 2, "per aanroep één keer verversen");
});

test("(g) verkeerde winkel (AAD), onbekende versie of andere sleutel: ontsleutelen faalt", async () => {
  const tekst = await versleutel(bos, "w1", "geheim");
  assert.equal(await ontsleutel(bos, "w1", tekst), "geheim");
  await assert.rejects(ontsleutel(bos, "w2", tekst));
  await assert.rejects(ontsleutel(bos, "w1", tekst.replace(/^v1\./, "v2.")), /onbekende sleutelversie/);
  const anders: Sleutelbos = { huidig: "v1", sleutels: { v1: crypto.getRandomValues(new Uint8Array(32)) } };
  await assert.rejects(ontsleutel(anders, "w1", tekst));
  // Sleutelwissel: oude tekst blijft leesbaar zolang v1 er nog is, nieuwe tekst gaat met v2.
  const nieuw: Sleutelbos = { huidig: "v2", sleutels: { v1: bos.sleutels.v1, v2: crypto.getRandomValues(new Uint8Array(32)) } };
  assert.equal(await ontsleutel(nieuw, "w1", tekst), "geheim");
  assert.match(await versleutel(nieuw, "w1", "x"), /^v2\./);
  const a = await versleutel(bos, "w1", "geheim");
  assert.notEqual(a, tekst, "nieuwe IV per keer");
});

test("(g) ontkoppelde winkel: verversen slaat niets op en geeft Ontkoppeld", async () => {
  const { db, maak } = await opzet(60);
  const bron = maak();
  await bron.lees();
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 5 WHERE id = 'w1'").run();
  const voor = db.sqlite.prepare("SELECT tt_tokens, tt_versie FROM winkels WHERE id='w1'").get();
  await assert.rejects(bron.geef(), (e: unknown) => e instanceof Ontkoppeld);
  assert.deepEqual(db.sqlite.prepare("SELECT tt_tokens, tt_versie FROM winkels WHERE id='w1'").get(), voor);
  assert.equal(await maak().bewaar(tokens(9, 9999), 1), false);
  await assert.rejects(maak().lees(), (e: unknown) => e instanceof Ontkoppeld);
});

// ---- tijdelijke fouten bij verversen (controleur): netwerk, 5xx, 429 en een 200 zonder token zijn geen koppeling_verlopen ----
const ttApp = { appKey: "k", appSecret: "s" };
const mbApp = { clientId: "c", clientSecret: "s", redirectUri: "https://x" };
const antwoorden: Record<string, () => Promise<Response>> = {
  netwerk: async () => { throw new TypeError("fetch failed"); },
  "500": async () => new Response("kapot", { status: 500 }),
  "429": async () => new Response(JSON.stringify({ error: "te veel" }), { status: 429 }),
  "200 zonder token": async () => new Response(JSON.stringify({ code: 0, data: {} }), { status: 200 }),
};

async function bronMet(kolom: "tt" | "mb", fetchFn: typeof fetch) {
  const db = new NepD1("w1");
  const soort: TokenSoort<any> = kolom === "tt" ? tiktokSoort(ttApp) : moneybirdSoort(mbApp);
  const maak = () => new TokenBron<any>({ db, winkel: "w1", soort, sleutels: bos, budget: new Budget(50), fetchFn, nu: () => NU });
  const start = kolom === "tt" ? tokens(1, 60) : { accessToken: "GEHEIM-mb-a", refreshToken: "GEHEIM-mb-r", scope: "documents", verlooptOp: NU + 60 };
  assert.equal(await maak().bewaar(start, 0), true);
  return { db, maak };
}

for (const kolom of ["tt", "mb"] as const) {
  for (const [naam, antwoord] of Object.entries(antwoorden)) {
    test(`(g) ${kolom} verversen met ${naam}: tijdelijke fout, geen koppeling_verlopen, niets opgeslagen`, async () => {
      const { db, maak } = await bronMet(kolom, antwoord as typeof fetch);
      await assert.rejects(maak().geef(), (e: unknown) => !(e instanceof WinkelStop));
      assert.equal(Number((db.sqlite.prepare(`SELECT ${kolom}_versie v FROM winkels`).get() as any).v), 1);
    });
  }
}

test("(g) echte weigering bij verversen (Moneybird 400 invalid_grant): koppeling_verlopen", async () => {
  const { maak } = await bronMet("mb", (async () => new Response(JSON.stringify({ error: "invalid_grant" }), { status: 400 })) as typeof fetch);
  await assert.rejects(maak().geef(), (e: unknown) => e instanceof WinkelStop && e.soort === "koppeling_verlopen");
});

test("(g) Moneybird geeft geen nieuw refresh_token: het oude blijft bewaard", async () => {
  const f = (async () => new Response(JSON.stringify({ access_token: "GEHEIM-mb-a2", scope: "documents", expires_in: 7200, created_at: NU }), { status: 200 })) as typeof fetch;
  const { maak } = await bronMet("mb", f);
  const u = await maak().geef();
  assert.equal(u.tokens.accessToken, "GEHEIM-mb-a2");
  assert.equal(u.tokens.refreshToken, "GEHEIM-mb-r");
  assert.equal((await maak().lees()).tokens.refreshToken, "GEHEIM-mb-r");
});
