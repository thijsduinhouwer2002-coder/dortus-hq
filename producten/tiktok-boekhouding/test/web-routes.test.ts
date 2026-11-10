// Deel 1b van de schermen (ontwerp-schermen.md versie 3, "Af als"): de routes via de router, Request erin en Response
// eruit, met nagebootste TikTok, Moneybird en D1. Toetsen (a) tot (p); (q) en de basis van (j), (l), (m) staan in web-basis.
import { test } from "node:test";
import assert from "node:assert/strict";
import { NepD1 } from "./d1-nep.ts";
import { router, type WebOmgeving } from "../src/web/router.ts";
import { csrfVan, maakSessie, SESSIE_COOKIE, TT_STATE_COOKIE, MB_STATE_COOKIE, KEUZE_COOKIE, maakMbState, type SessieSleutels } from "../src/web/sessie.ts";
import { ontsleutel, type Sleutelbos } from "../src/d1/tokens.ts";
import { NOOIT } from "../src/web/basis.ts";
import { winkelsAanDeBeurt } from "../src/d1/winkels.ts";

const NU = 1_794_000_000;
const ADRES = "https://klopt.dortus.com";
const bos: SessieSleutels = { huidig: "s1", sleutels: { s1: new Uint8Array(32).fill(7) } };
const sleutels: Sleutelbos = { huidig: "k1", sleutels: { k1: new Uint8Array(32).fill(3) } };
const GEHEIM = ["APPSECRET", "MBSECRET", "TT-ACCESS", "TT-REFRESH", "MB-ACCESS", "MB-REFRESH"];

type Shop = { id: string; name: string; region: string; cipher: string };

function wereld() {
  const w = {
    shops: [{ id: "111", name: "Bloem & Co", region: "NL", cipher: "C111" }] as Shop[],
    ttToken: 200 as number,
    ttRegio: "NL",
    webhookFout: false,
    mbToken: 200 as number,
    mbRefresh: "MB-REFRESH-1",
    adms: [{ id: 501, name: "Bloem BV", currency: "EUR", country: "NL", period_locked_until: null }] as any[],
    admsStatus: 200,
    ttTeller: 0,
    verzoeken: [] as string[],
    koppen: [] as string[],
    ingetrokken: [] as string[],
  };
  const json = (data: unknown, status = 200) => new Response(JSON.stringify(data), { status });
  const fn = (async (input: any, init: any = {}) => {
    const u = new URL(String(input));
    const m = init.method ?? "GET";
    w.verzoeken.push(`${m} ${u.hostname} ${u.pathname}`);
    w.koppen.push(JSON.stringify(init.headers ?? {}));
    if (u.hostname === "auth.tiktok-shops.com") {
      if (w.ttToken !== 200) return json({ code: 1, message: "storing" }, w.ttToken);
      const n = ++w.ttTeller;
      return json({ code: 0, message: "success", request_id: "r", data: {
        access_token: `TT-ACCESS-${n}`, access_token_expire_in: NU + 7 * 86400, refresh_token: `TT-REFRESH-${n}`, refresh_token_expire_in: NU + 60 * 86400,
        open_id: "open-1", seller_name: "Bloem & Co", seller_base_region: w.ttRegio, user_type: 0, granted_scopes: ["seller.finance.info"] } });
    }
    if (u.hostname === "open-api.tiktokglobalshop.com") {
      if (u.pathname === "/authorization/202309/shops") return json({ code: 0, message: "Success", request_id: "r", data: { shops: w.shops.map((s) => ({ ...s, seller_type: "LOCAL", code: "X" })) } });
      if (u.pathname === "/event/202309/webhooks") return w.webhookFout ? json({ code: 1, message: "storing" }, 500) : json({ code: 0, message: "Success", request_id: "r", data: {} });
    }
    if (u.hostname === "moneybird.com") {
      if (u.pathname === "/oauth/token") {
        if (w.mbToken !== 200) return json({ error: "server_error" }, w.mbToken);
        return json({ access_token: "MB-ACCESS-1", token_type: "bearer", refresh_token: w.mbRefresh, scope: "documents settings", created_at: NU });
      }
      if (u.pathname === "/oauth/revoke") { w.ingetrokken.push(new URLSearchParams(init.body).get("token")!); return json({}); }
      if (u.pathname === "/api/v2/administrations.json") return w.admsStatus === 200 ? json(w.adms) : json({ error: "x" }, w.admsStatus);
    }
    throw new Error(`onverwacht ${m} ${u}`);
  }) as typeof fetch;
  return { w, fn };
}

function omgeving(fn: typeof fetch, db = new NepD1()) {
  const log: string[] = [];
  const o: WebOmgeving = {
    db: db as any, wachtrij: { sendBatch: async () => {} }, fetchFn: fn, log: (r) => log.push(r), sleutels,
    tiktokApp: { appKey: "KEY", appSecret: "APPSECRET" },
    moneybirdApp: { clientId: "cid", clientSecret: "MBSECRET", redirectUri: `${ADRES}/app/moneybird/terug` },
    sessie: bos, tiktokServiceId: "7000", appAdres: ADRES,
  };
  return { o, db, log };
}

interface Vraag { cookies?: Record<string, string>; form?: Record<string, string>; origin?: string | null }
function verzoek(methode: string, pad: string, v: Vraag = {}): Request {
  const h = new Headers();
  if (v.cookies) h.set("cookie", Object.entries(v.cookies).map(([k, x]) => `${k}=${x}`).join("; "));
  if (methode === "POST" && v.origin !== null) h.set("origin", v.origin ?? ADRES);
  if (v.form) h.set("content-type", "application/x-www-form-urlencoded");
  return new Request(ADRES + pad, { method: methode, headers: h, body: v.form ? new URLSearchParams(v.form).toString() : undefined });
}
const koekjes = (r: Response) => r.headers.getSetCookie();
const koekje = (r: Response, naam: string) => koekjes(r).find((c) => c.startsWith(naam + "="))?.split(";")[0].slice(naam.length + 1);

async function vraag(o: WebOmgeving, methode: string, pad: string, v: Vraag = {}) {
  const r = await router(verzoek(methode, pad, v), o, NU);
  const tekst = await r.text();
  return { r, tekst };
}

function controleerGeheim(tekst: string, log: string[]) {
  for (const g of GEHEIM) {
    assert.ok(!tekst.includes(g), `geheim ${g} in de HTML`);
    assert.ok(!log.join("\n").includes(g), `geheim ${g} in de log`);
  }
}

/** TikTok-terugkeer met kloppende state; geeft de sessie-cookie. */
async function koppelTikTok(o: WebOmgeving) {
  const start = await vraag(o, "GET", "/app/tiktok/start");
  const state = koekje(start.r, TT_STATE_COOKIE)!;
  assert.match(start.r.headers.get("location")!, /^https:\/\/services\.tiktokshop\.com\/open\/authorize\?service_id=7000&state=/);
  return vraag(o, "GET", `/app/tiktok/terug?code=abc&state=${state}`, { cookies: { [TT_STATE_COOKIE]: state } });
}

const rijen = (db: NepD1) => db.sqlite.prepare("SELECT * FROM winkels").all() as any[];

test("(a) TikTok-terugkeer met kloppende state: één rij, versleuteld, sessie, 302; tweede keer zelfde rij, versie hoger", async () => {
  const { w, fn } = wereld();
  const { o, db, log } = omgeving(fn);
  const { r, tekst } = await koppelTikTok(o);
  assert.equal(r.status, 302);
  assert.equal(r.headers.get("location"), "/app");
  const sessie = koekjes(r).find((c) => c.startsWith(SESSIE_COOKIE + "="))!;
  assert.match(sessie, /HttpOnly/);
  assert.match(sessie, /Secure/);
  assert.match(sessie, /SameSite=Lax/);
  assert.ok(koekjes(r).some((c) => c.startsWith(`${TT_STATE_COOKIE}=;`) && /Max-Age=0/.test(c)), "state-cookie gewist");
  let [rij] = rijen(db);
  assert.equal(rijen(db).length, 1);
  assert.equal(rij.shop_id, "111");
  assert.equal(rij.volgende_run, NOOIT);
  assert.ok(!rij.tt_tokens.includes("TT-ACCESS"));
  assert.equal(JSON.parse(await ontsleutel(sleutels, rij.id, rij.tt_tokens)).accessToken, "TT-ACCESS-1");
  assert.equal(JSON.parse(rij.instellingen).winkelnaam, "Bloem & Co");
  assert.equal(JSON.parse(rij.instellingen).webhooks, 1);
  assert.equal(w.verzoeken.filter((v) => v.includes("/event/202309/webhooks")).length, 2);
  controleerGeheim(tekst, log);
  await koppelTikTok(o);
  assert.equal(rijen(db).length, 1);
  [rij] = rijen(db);
  assert.equal(rij.tt_versie, 1);
  assert.equal(JSON.parse(await ontsleutel(sleutels, rij.id, rij.tt_tokens)).accessToken, "TT-ACCESS-2");
});

test("(b) terugkeer zonder state (installeren uit de App Store): tokens opgeslagen, geen sessie, 'Open Klopt als'", async () => {
  const { fn } = wereld();
  const { o, db } = omgeving(fn);
  const { r, tekst } = await vraag(o, "GET", "/app/tiktok/terug?code=abc");
  assert.equal(r.status, 200);
  assert.equal(koekje(r, SESSIE_COOKIE), undefined);
  assert.match(tekst, /Open Klopt als Bloem &amp; Co/);
  assert.equal(rijen(db).length, 1);
});

test("(c) state onjuist bij TikTok en Moneybird: 400, geen tokenwissel, state-cookie gewist", async () => {
  const { w, fn } = wereld();
  const { o } = omgeving(fn);
  const a = await vraag(o, "GET", "/app/tiktok/terug?code=abc&state=vals", { cookies: { [TT_STATE_COOKIE]: "echt" } });
  assert.equal(a.r.status, 400);
  assert.ok(koekjes(a.r).some((c) => c.startsWith(`${TT_STATE_COOKIE}=;`)));
  const b = await vraag(o, "GET", "/app/tiktok/terug?code=abc&state=x");
  assert.equal(b.r.status, 400, "geen cookie");
  assert.equal(w.verzoeken.length, 0);
  const k = await koppelTikTok(o);
  const sessie = koekje(k.r, SESSIE_COOKIE)!;
  const voor = w.verzoeken.length;
  const winkel = sessie.split(".")[1];
  const mb = await maakMbState(bos, "goedestate", winkel, NU);
  const c = await vraag(o, "GET", "/app/moneybird/terug?code=x&state=anders", { cookies: { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: mb } });
  assert.equal(c.r.status, 400);
  assert.ok(koekjes(c.r).some((x) => x.startsWith(`${MB_STATE_COOKIE}=;`) && /Max-Age=0/.test(x)));
  assert.equal(w.verzoeken.length, voor);
});

test("(d) weigering: geen tokenwissel, zachte zin (TikTok error en code=null, Moneybird access_denied)", async () => {
  const { w, fn } = wereld();
  const { o } = omgeving(fn);
  for (const q of ["error=auth_denied&state=x", "code=null&state=x", "code="]) {
    const { r, tekst } = await vraag(o, "GET", `/app/tiktok/terug?${q}`);
    assert.equal(r.status, 200);
    assert.match(tekst, /Je gaf TikTok Shop geen toestemming/);
  }
  assert.equal(w.verzoeken.length, 0);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const voor = w.verzoeken.length;
  const mb = await maakMbState(bos, "st", sessie.split(".")[1], NU);
  const { tekst } = await vraag(o, "GET", "/app/moneybird/terug?error=access_denied&state=st", { cookies: { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: mb } });
  assert.match(tekst, /Je gaf Moneybird geen toestemming/);
  assert.match(tekst, /Koppel Moneybird/);
  assert.equal(w.verzoeken.length, voor);
});

test("(e) fout van TikTok of Moneybird (5xx): foutstaat zonder 'vanzelf opnieuw', niets opgeslagen", async () => {
  const { w, fn } = wereld();
  const { o, db } = omgeving(fn);
  w.ttToken = 503;
  const { r, tekst } = await vraag(o, "GET", "/app/tiktok/terug?code=abc");
  assert.equal(r.status, 502);
  assert.match(tekst, /ligt niet aan jou/);
  assert.ok(!/vanzelf/i.test(tekst));
  assert.equal(rijen(db).length, 0);
  w.ttToken = 200;
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  w.mbToken = 500;
  const mb = await maakMbState(bos, "st", sessie.split(".")[1], NU);
  const m = await vraag(o, "GET", "/app/moneybird/terug?code=x&state=st", { cookies: { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: mb } });
  assert.equal(m.r.status, 502);
  assert.match(m.tekst, /Moneybird gaf geen antwoord/);
  assert.equal(rijen(db)[0].mb_tokens, null);
});

test("(f) geen NL-winkel: nog niet voor jou met land; meer NL-winkels: keuzescherm en strenge keuze", async () => {
  const { w, fn } = wereld();
  const { o, db } = omgeving(fn);
  w.shops = [{ id: "9", name: "Blume", region: "DE", cipher: "C9" }];
  w.ttRegio = "DE";
  let { tekst } = await vraag(o, "GET", "/app/tiktok/terug?code=abc");
  assert.match(tekst, /Duitsland/);
  assert.match(tekst, /mailto:thijs@dortus\.com\?subject=Wachtlijst%20Klopt%3A%20Duitsland/);
  assert.equal(rijen(db).length, 0);

  w.shops = [{ id: "1", name: "Eén", region: "NL", cipher: "C1" }, { id: "2", name: "Twee", region: "NL", cipher: "C2" }, { id: "3", name: "Drie", region: "BE", cipher: "C3" }];
  const start = await vraag(o, "GET", "/app/tiktok/start");
  const state = koekje(start.r, TT_STATE_COOKIE)!;
  const k = await vraag(o, "GET", `/app/tiktok/terug?code=abc&state=${state}`, { cookies: { [TT_STATE_COOKIE]: state } });
  assert.match(k.tekst, /Kies je winkel/);
  assert.ok(!k.tekst.includes("Drie"));
  assert.equal(rijen(db).length, 0, "keuzescherm slaat nog niets op");
  const keuze = koekje(k.r, KEUZE_COOKIE)!;
  const csrf = await csrfVan(bos, keuze);
  assert.equal((await vraag(o, "POST", "/app/tiktok/kies", { cookies: { [KEUZE_COOKIE]: keuze }, form: { shop: "3", csrf } })).r.status, 400, "buiten de lijst");
  assert.equal((await vraag(o, "POST", "/app/tiktok/kies", { cookies: { [KEUZE_COOKIE]: keuze }, form: { shop: "2", csrf: "vals" } })).r.status, 403);
  assert.equal(rijen(db).length, 0);
  const goed = await vraag(o, "POST", "/app/tiktok/kies", { cookies: { [KEUZE_COOKIE]: keuze }, form: { shop: "2", csrf } });
  assert.equal(goed.r.status, 302);
  assert.ok(koekje(goed.r, SESSIE_COOKIE));
  assert.ok(koekjes(goed.r).some((c) => c.startsWith(`${KEUZE_COOKIE}=;`)));
  assert.deepEqual(rijen(db).map((r) => r.shop_cipher), ["C2"]);

  // Keuze na een terugkeer zonder state: opgeslagen, maar geen sessie.
  const z = await vraag(o, "GET", "/app/tiktok/terug?code=abc");
  const keuze2 = koekje(z.r, KEUZE_COOKIE)!;
  const z2 = await vraag(o, "POST", "/app/tiktok/kies", { cookies: { [KEUZE_COOKIE]: keuze2 }, form: { shop: "1", csrf: await csrfVan(bos, keuze2) } });
  assert.equal(z2.r.status, 200);
  assert.equal(koekje(z2.r, SESSIE_COOKIE), undefined);
  assert.match(z2.tekst, /Open Klopt als Eén/);
  assert.equal(rijen(db).length, 2);
});

test("(g) twee TikTok-terugkeren tegelijk: één rij, tokens te ontsleutelen met het id van die rij", async () => {
  const { fn } = wereld();
  const db = new NepD1();
  const { o } = omgeving(fn, db);
  const orig = db.prepare.bind(db);
  let haak = true;
  (db as any).prepare = (sql: string) => {
    if (haak && /^\s*INSERT INTO winkels/.test(sql)) {
      haak = false;
      db.sqlite.prepare("INSERT INTO winkels (id, shop_id, shop_cipher, volgende_run) VALUES ('ander', '111', 'C111', ?)").run(NOOIT);
    }
    return orig(sql);
  };
  const { r } = await vraag(o, "GET", "/app/tiktok/terug?code=abc");
  assert.equal(r.status, 200);
  const alle = rijen(db);
  assert.equal(alle.length, 1);
  assert.equal(alle[0].id, "ander");
  assert.equal(JSON.parse(await ontsleutel(sleutels, "ander", alle[0].tt_tokens)).accessToken, "TT-ACCESS-1");
});

test("(g) Moneybird: verversing tussendoor laat de nieuwe toestemming winnen en trekt het vervangen paar in; gelijk refresh token niet", async () => {
  const { w, fn } = wereld();
  const db = new NepD1();
  const { o } = omgeving(fn, db);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const id = sessie.split(".")[1];
  const { versleutel } = await import("../src/d1/tokens.ts");
  db.sqlite.prepare("UPDATE winkels SET mb_tokens = ?, mb_versie = 4 WHERE id = ?").run(await versleutel(sleutels, id, JSON.stringify({ accessToken: "a", refreshToken: "OUD-4", scope: "" })), id);
  // Haak: tussen het lezen (sessie) en schrijven ververst de consumer naar versie 5.
  const orig = db.prepare.bind(db);
  let haak = true;
  const vers5 = await versleutel(sleutels, id, JSON.stringify({ accessToken: "b", refreshToken: "OUD-5", scope: "" }));
  (db as any).prepare = (sql: string) => {
    if (haak && /^\s*UPDATE winkels SET mb_tokens/.test(sql)) { haak = false; db.sqlite.prepare("UPDATE winkels SET mb_tokens = ?, mb_versie = 5 WHERE id = ?").run(vers5, id); }
    return orig(sql);
  };
  const mb = await maakMbState(bos, "st", id, NU);
  const { r } = await vraag(o, "GET", "/app/moneybird/terug?code=x&state=st", { cookies: { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: mb } });
  assert.equal(r.status, 302);
  const rij = rijen(db)[0];
  assert.equal(rij.mb_versie, 6);
  assert.equal(JSON.parse(await ontsleutel(sleutels, id, rij.mb_tokens)).refreshToken, "MB-REFRESH-1");
  assert.deepEqual(w.ingetrokken, ["OUD-5"]);
  // Nog eens met hetzelfde refresh token: niets intrekken.
  w.ingetrokken.length = 0;
  const mb2 = await maakMbState(bos, "st2", id, NU);
  await vraag(o, "GET", "/app/moneybird/terug?code=y&state=st2", { cookies: { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: mb2 } });
  assert.deepEqual(w.ingetrokken, []);
});

test("(h) opnieuw koppelen wist een TikTok-winkelfout (niet Moneybird), wekt een winkel die aan staat; nieuw blijft uit", async () => {
  const { fn } = wereld();
  const { o, db } = omgeving(fn);
  await koppelTikTok(o);
  assert.deepEqual(await winkelsAanDeBeurt(db as any, NU + 10 ** 9, { neem() {} }), [], "nieuwe rij niet aan de beurt");
  const id = rijen(db)[0].id;
  db.sqlite.prepare(`UPDATE winkels SET volgende_run = ?, winkelfout = '{"soort":"koppeling_verlopen","bericht":"x","kant":"tiktok"}', winkelfout_sinds = 5 WHERE id = ?`).run(NU + 9999, id);
  await koppelTikTok(o);
  let rij = rijen(db)[0];
  assert.equal(rij.winkelfout, null);
  assert.equal(rij.winkelfout_sinds, null);
  assert.equal(rij.volgende_run, NU, "gewekt");
  db.sqlite.prepare(`UPDATE winkels SET winkelfout = '{"soort":"koppeling_verlopen","bericht":"x","kant":"moneybird"}', winkelfout_sinds = 5 WHERE id = ?`).run(id);
  await koppelTikTok(o);
  rij = rijen(db)[0];
  assert.match(rij.winkelfout, /moneybird/);
  assert.equal(rij.winkelfout_sinds, 5);
});

test("(i) Moneybird-terugkeer: sessie en eigen state nodig; administraties nul, één, meer, buiten NL/EUR; id buiten lijst geweigerd", async () => {
  const { w, fn } = wereld();
  const { o, db } = omgeving(fn);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const id = sessie.split(".")[1];
  const terug = async (st: string, winkel = id, metSessie = true) => vraag(o, "GET", `/app/moneybird/terug?code=c&state=${st}`, {
    cookies: { ...(metSessie ? { [SESSIE_COOKIE]: sessie } : {}), [MB_STATE_COOKIE]: await maakMbState(bos, st, winkel, NU) } });
  assert.equal((await terug("s0", id, false)).r.status, 400, "zonder sessie");
  assert.equal((await terug("s1", "andere-winkel")).r.status, 400, "state van een andere winkel");

  // Eén: meteen opgeslagen in de vorm die de consumer leest.
  let r = await terug("s2");
  assert.equal(r.r.status, 302);
  let rij = rijen(db)[0];
  assert.equal(rij.administratie, "501");
  assert.deepEqual(JSON.parse(rij.instellingen).administratie, { id: "501", periodLockedUntil: null });

  // Verdwenen en geen NL/EUR meer: leeggemaakt, "geen Nederlandse administratie in euro".
  w.adms = [{ id: 777, name: "GmbH", currency: "EUR", country: "DE", period_locked_until: null }];
  r = await terug("s3");
  assert.match(r.tekst, /Geen Nederlandse administratie in euro/);
  rij = rijen(db)[0];
  assert.equal(rij.administratie, null);
  assert.equal(JSON.parse(rij.instellingen).administratie, undefined);
  w.adms = [];
  assert.match((await terug("s4")).tekst, /We vonden geen Moneybird-administratie/);

  // Meer: keuzescherm; POST met id buiten de lijst geweigerd, daarna goed.
  w.adms = [
    { id: 601, name: "Een BV", currency: "EUR", country: "NL", period_locked_until: "2026-06-30" },
    { id: 602, name: "Twee BV", currency: "EUR", country: "NL", period_locked_until: null },
    { id: 603, name: "Dollar", currency: "USD", country: "NL", period_locked_until: null },
  ];
  r = await terug("s5");
  assert.match(r.tekst, /Kies je administratie/);
  assert.ok(!r.tekst.includes("Dollar"));
  const csrf = await csrfVan(bos, sessie);
  assert.equal((await vraag(o, "POST", "/app/moneybird/administratie", { cookies: { [SESSIE_COOKIE]: sessie }, form: { administratie: "603", csrf } })).r.status, 400);
  assert.equal(rijen(db)[0].administratie, null);
  const kies = await vraag(o, "POST", "/app/moneybird/administratie", { cookies: { [SESSIE_COOKIE]: sessie }, form: { administratie: "601", csrf } });
  assert.equal(kies.r.status, 302);
  rij = rijen(db)[0];
  assert.deepEqual(JSON.parse(rij.instellingen).administratie, { id: "601", periodLockedUntil: "2026-06-30" });
  assert.match((await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } })).tekst, /Gekoppeld/);
  assert.equal(db.sqlite.prepare("SELECT count(*) AS n FROM sloten").get()!.n, 0, "slot terug");
});

test("(j) POST zonder geldige csrf, met vreemde Origin of zonder Origin en Referer: 403, niets geschreven", async () => {
  const { w, fn } = wereld();
  const { o, db } = omgeving(fn);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const csrf = await csrfVan(bos, sessie);
  const voor = w.verzoeken.length;
  for (const v of [{ form: { csrf: "vals" } }, { form: { csrf }, origin: "https://kwaad.example" }, { form: { csrf }, origin: null }]) {
    for (const pad of ["/app/moneybird/start", "/app/moneybird/administratie"]) {
      const { r } = await vraag(o, "POST", pad, { cookies: { [SESSIE_COOKIE]: sessie }, ...v });
      assert.equal(r.status, 403, `${pad} ${JSON.stringify(v)}`);
    }
  }
  assert.equal(w.verzoeken.length, voor);
  assert.equal(rijen(db)[0].mb_tokens, null);
  const goed = await vraag(o, "POST", "/app/moneybird/start", { cookies: { [SESSIE_COOKIE]: sessie }, form: { csrf } });
  assert.equal(goed.r.status, 302);
  assert.ok(koekje(goed.r, MB_STATE_COOKIE));
});

test("(k) zonder, met vals of verlopen cookie, of ontkoppeld: 'Open Klopt vanuit TikTok Shop', zonder winkelgegevens", async () => {
  const { fn } = wereld();
  const { o, db } = omgeving(fn);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const id = sessie.split(".")[1];
  const verlopen = await maakSessie(bos, id, NU - 31 * 86400);
  for (const c of [undefined, sessie.slice(0, -2) + "xx", verlopen]) {
    const { tekst } = await vraag(o, "GET", "/app", c ? { cookies: { [SESSIE_COOKIE]: c } } : {});
    assert.match(tekst, /Open Klopt vanuit TikTok Shop/);
    assert.ok(!tekst.includes("Bloem") && !tekst.includes(id));
  }
  db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 1, shop_id = NULL WHERE id = ?").run(id);
  const { tekst } = await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } });
  assert.match(tekst, /Open Klopt vanuit TikTok Shop/);
  assert.ok(!tekst.includes("Bloem"));
});

test("(l) winkelnaam met <script> en aanhalingstekens komt ge-escaped in de HTML", async () => {
  const { w, fn } = wereld();
  const { o } = omgeving(fn);
  w.shops = [{ id: "111", name: `<script>x</script>"'`, region: "NL", cipher: "C111" }];
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const { tekst } = await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } });
  assert.ok(!tekst.includes("<script>"));
  assert.ok(tekst.includes("&lt;script&gt;x&lt;/script&gt;&quot;&#39;"));
});

test("(m) kopregels op elke pagina, geen inline stijl, stijl.css bestaat; onbekend pad 404", async () => {
  const { fn } = wereld();
  const { o } = omgeving(fn);
  for (const pad of ["/app", "/app/niet-voor-jou?voor=exact", "/app/tiktok/terug?code=abc"]) {
    const { r, tekst } = await vraag(o, "GET", pad);
    assert.ok(r.headers.get("content-security-policy")?.includes("default-src 'self'"), pad);
    assert.equal(r.headers.get("x-content-type-options"), "nosniff");
    assert.equal(r.headers.get("cache-control"), "no-store");
    assert.ok(!/<style|style=/i.test(tekst));
  }
  const css = await vraag(o, "GET", "/app/stijl.css");
  assert.equal(css.r.status, 200);
  assert.match(css.r.headers.get("content-type")!, /text\/css/);
  assert.equal((await vraag(o, "GET", "/app/bestaat-niet")).r.status, 404);
  assert.equal((await vraag(o, "GET", "/app/niet-voor-jou?voor=iets")).r.status, 404);
  assert.equal((await vraag(o, "GET", "/app/tiktok/kies")).r.status, 405);
});

test("(n) webhooks mislukt: koppelen gaat door met webhooks 0, volgende opening probeert onder het slot; gelukt niet nog eens", async () => {
  const { w, fn } = wereld();
  const { o, db, log } = omgeving(fn);
  w.webhookFout = true;
  const { r } = await koppelTikTok(o);
  assert.equal(r.status, 302);
  assert.equal(JSON.parse(rijen(db)[0].instellingen).webhooks, 0);
  assert.ok(log.some((l) => l.includes("webhooks aanmelden")));
  const sessie = koekje(r, SESSIE_COOKIE)!;
  w.webhookFout = false;
  const tel = () => w.verzoeken.filter((v) => v.includes("/event/202309/webhooks")).length;
  const voor = tel();
  await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } });
  assert.equal(tel(), voor + 2);
  assert.equal(JSON.parse(rijen(db)[0].instellingen).webhooks, 1);
  await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } });
  assert.equal(tel(), voor + 2, "niet nog eens");
  assert.equal(db.sqlite.prepare("SELECT count(*) AS n FROM sloten").get()!.n, 0);
});

test("(n2) slot bezet: 'Even geduld' bij de administratiekeuze, geen verzoek; webhook-poging wordt overgeslagen", async () => {
  const { w, fn } = wereld();
  const { o, db } = omgeving(fn);
  w.webhookFout = true;
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const id = sessie.split(".")[1];
  const { versleutel } = await import("../src/d1/tokens.ts");
  db.sqlite.prepare("UPDATE winkels SET mb_tokens = ? WHERE id = ?").run(await versleutel(sleutels, id, JSON.stringify({ accessToken: "a", refreshToken: "r", scope: "" })), id);
  db.sqlite.prepare("INSERT INTO sloten (winkel, statement_id, eigenaar, tot) VALUES (?, '__winkel', 'consumer', ?)").run(id, NU + 600);
  const voor = w.verzoeken.length;
  const { r, tekst } = await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } });
  assert.equal(r.status, 503);
  assert.match(tekst, /Even geduld/);
  const csrf = await csrfVan(bos, sessie);
  assert.match((await vraag(o, "POST", "/app/moneybird/administratie", { cookies: { [SESSIE_COOKIE]: sessie }, form: { administratie: "501", csrf } })).tekst, /Even geduld/);
  assert.equal(w.verzoeken.length, voor);
  assert.equal(db.sqlite.prepare("SELECT eigenaar FROM sloten").get()!.eigenaar, "consumer", "slot van een ander blijft staan");
});

test("(o) elke route binnen het budget van 50; geheimen nooit in HTML of log", async () => {
  const { w, fn } = wereld();
  const db = new NepD1();
  const { o, log } = omgeving(fn, db);
  let fetches = 0;
  o.fetchFn = (async (i: any, x: any) => { fetches++; return fn(i, x); }) as typeof fetch;
  const telVoor = async (doe: () => Promise<{ tekst: string }>) => {
    const q0 = db.queries, f0 = fetches;
    const { tekst } = await doe();
    controleerGeheim(tekst, log);
    return db.queries - q0 + fetches - f0;
  };
  let sessie = "";
  const n1 = await telVoor(async () => { const k = await koppelTikTok(o); sessie = koekje(k.r, SESSIE_COOKIE)!; return k; });
  assert.ok(n1 <= 12, `TikTok-terugkeer ${n1}`);
  const id = sessie.split(".")[1];
  w.adms = [{ id: 1, name: "A", currency: "EUR", country: "NL" }, { id: 2, name: "B", currency: "EUR", country: "NL" }];
  db.sqlite.prepare(`UPDATE winkels SET mb_tokens = ?, mb_versie = 1 WHERE id = ?`).run(await (await import("../src/d1/tokens.ts")).versleutel(sleutels, id, JSON.stringify({ accessToken: "a", refreshToken: "MB-REFRESH-0", scope: "" })), id);
  const n2 = await telVoor(async () => vraag(o, "GET", `/app/moneybird/terug?code=c&state=st`, { cookies: { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: await maakMbState(bos, "st", id, NU) } }));
  assert.ok(n2 <= 10, `Moneybird-terugkeer ${n2}`);
  const n3 = await telVoor(() => vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } }));
  assert.ok(n3 <= 10, `/app ${n3}`);
});

test("(p) Moneybird-link vraagt documents en settings; scherm 1 noemt de rechten en heeft de Exact-link", async () => {
  const { fn } = wereld();
  const { o } = omgeving(fn);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const { tekst } = await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } });
  assert.match(tekst, /Stap 1 van 3/);
  assert.match(tekst, /boekingen te maken en je grootboekrekeningen te lezen en aan te maken/);
  assert.match(tekst, /href="\/app\/niet-voor-jou\?voor=exact"/);
  const { r } = await vraag(o, "POST", "/app/moneybird/start", { cookies: { [SESSIE_COOKIE]: sessie }, form: { csrf: await csrfVan(bos, sessie) } });
  const loc = r.headers.get("location")!;
  assert.match(loc, /^https:\/\/moneybird\.com\/oauth\/authorize\?/);
  assert.match(loc, /scope=documents\+settings/);
  assert.match((await vraag(o, "GET", "/app/niet-voor-jou?voor=exact")).tekst, /Wachtlijst%20Klopt%3A%20Exact/);
});

test("uitloggen: alleen met csrf van ons eigen adres, wist het cookie", async () => {
  const { fn } = wereld();
  const { o } = omgeving(fn);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  assert.equal((await vraag(o, "POST", "/app/uit", { cookies: { [SESSIE_COOKIE]: sessie }, form: { csrf: "x" } })).r.status, 403);
  const { r } = await vraag(o, "POST", "/app/uit", { cookies: { [SESSIE_COOKIE]: sessie }, form: { csrf: await csrfVan(bos, sessie) } });
  assert.ok(koekjes(r).some((c) => c.startsWith(`${SESSIE_COOKIE}=;`) && /Max-Age=0/.test(c)));
});

test("moet-punt controleur: opgeslagen tokens worden onder het slot vers gelezen, niet uit de rij van de sessie", async () => {
  const { w, fn } = wereld();
  const db = new NepD1();
  const { o } = omgeving(fn, db);
  w.webhookFout = true;
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  w.webhookFout = false;
  const id = sessie.split(".")[1];
  const { versleutel } = await import("../src/d1/tokens.ts");
  db.sqlite.prepare("UPDATE winkels SET mb_tokens = ?, mb_versie = 1 WHERE id = ?").run(await versleutel(sleutels, id, JSON.stringify({ accessToken: "MB-OUD", refreshToken: "r1", scope: "" })), id);
  // Haak: tussen de sessie-SELECT en het slot ververst de consumer beide paren.
  const ttNieuw = await versleutel(sleutels, id, JSON.stringify({ accessToken: "TTVERS", accessTokenVerlooptOp: NU + 86400 * 5, refreshToken: "x", refreshTokenVerlooptOp: NU + 86400 * 50, openId: "open-1" }));
  const mbNieuw = await versleutel(sleutels, id, JSON.stringify({ accessToken: "MBVERS", refreshToken: "r2", scope: "" }));
  const orig = db.prepare.bind(db);
  let haak = true;
  (db as any).prepare = (sql: string) => {
    if (haak && /INSERT INTO sloten/.test(sql)) {
      haak = false;
      db.sqlite.prepare("UPDATE winkels SET tt_tokens = ?, tt_versie = tt_versie + 1, mb_tokens = ?, mb_versie = mb_versie + 1 WHERE id = ?").run(ttNieuw, mbNieuw, id);
    }
    return orig(sql);
  };
  const voor = w.koppen.length;
  await vraag(o, "GET", "/app", { cookies: { [SESSIE_COOKIE]: sessie } });
  const nieuw = w.koppen.slice(voor).join("\n") + w.verzoeken.slice(voor).join("\n");
  assert.ok(nieuw.includes("TTVERS"), "webhooks met het verse TikTok-token");
  assert.ok(!nieuw.includes("TT-ACCESS-1"));
  haak = true;
  (db as any).prepare = (sql: string) => {
    if (haak && /INSERT INTO sloten/.test(sql)) {
      haak = false;
      db.sqlite.prepare("UPDATE winkels SET mb_tokens = ?, mb_versie = mb_versie + 1 WHERE id = ?").run(mbNieuw, id);
    }
    return orig(sql);
  };
  db.sqlite.prepare("UPDATE winkels SET mb_tokens = ? WHERE id = ?").run(await versleutel(sleutels, id, JSON.stringify({ accessToken: "MB-OUD", refreshToken: "r1", scope: "" })), id);
  const v2 = w.koppen.length;
  await vraag(o, "POST", "/app/moneybird/administratie", { cookies: { [SESSIE_COOKIE]: sessie }, form: { administratie: "501", csrf: await csrfVan(bos, sessie) } });
  const k = w.koppen.slice(v2).join("\n");
  assert.ok(k.includes("MBVERS") && !k.includes("MB-OUD"), "administraties met het verse Moneybird-token");
});

test("Moneybird opslaan: na 3 keer een andere versie het verse paar intrekken; winkel ontkoppeld: vers paar intrekken en sessie wissen", async () => {
  const { w, fn } = wereld();
  const db = new NepD1();
  const { o, log } = omgeving(fn, db);
  const sessie = koekje((await koppelTikTok(o)).r, SESSIE_COOKIE)!;
  const id = sessie.split(".")[1];
  const orig = db.prepare.bind(db);
  (db as any).prepare = (sql: string) => {
    if (/^\s*UPDATE winkels SET mb_tokens/.test(sql)) db.sqlite.prepare("UPDATE winkels SET mb_versie = mb_versie + 1 WHERE id = ?").run(id);
    return orig(sql);
  };
  const terug = async (st: string) => vraag(o, "GET", `/app/moneybird/terug?code=c&state=${st}`, { cookies: { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: await maakMbState(bos, st, id, NU) } });
  const a = await terug("a");
  assert.equal(a.r.status, 502);
  assert.deepEqual(w.ingetrokken, ["MB-REFRESH-1"]);
  assert.equal(rijen(db)[0].mb_tokens, null);
  w.ingetrokken.length = 0;
  (db as any).prepare = (sql: string) => {
    if (/^\s*UPDATE winkels SET mb_tokens/.test(sql)) db.sqlite.prepare("UPDATE winkels SET ontkoppeld_op = 1, shop_id = NULL WHERE id = ?").run(id);
    return orig(sql);
  };
  const b = await terug("b");
  assert.match(b.tekst, /Open Klopt vanuit TikTok Shop/);
  assert.ok(koekjes(b.r).some((c) => c.startsWith(`${SESSIE_COOKIE}=;`)));
  assert.deepEqual(w.ingetrokken, ["MB-REFRESH-1"]);
  controleerGeheim(b.tekst, log);
});

test("herkomst op /app/tiktok/kies en /app/uit: vreemde Origin of geen Origin is 403", async () => {
  const { w, fn } = wereld();
  const { o, db } = omgeving(fn);
  w.shops = [{ id: "1", name: "Een", region: "NL", cipher: "C1" }, { id: "2", name: "Twee", region: "NL", cipher: "C2" }];
  const z = await vraag(o, "GET", "/app/tiktok/terug?code=abc");
  const keuze = koekje(z.r, KEUZE_COOKIE)!;
  const csrf = await csrfVan(bos, keuze);
  for (const origin of ["https://kwaad.example", null]) {
    assert.equal((await vraag(o, "POST", "/app/tiktok/kies", { cookies: { [KEUZE_COOKIE]: keuze }, form: { shop: "1", csrf }, origin })).r.status, 403);
    assert.equal((await vraag(o, "POST", "/app/uit", { form: {}, origin })).r.status, 403);
  }
  assert.equal(rijen(db).length, 0);
});
