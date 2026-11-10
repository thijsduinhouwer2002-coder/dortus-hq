// Basis van de schermen (ontwerp-schermen.md versie 3): sessie, csrf, state, keuze-cookie, escapen, kopregels, stijl.
// Toetsen (c)-deel cookie wissen, (j) herkomst, (k)-deel sessie, (l), (m), (q). De routes volgen in deel 1b.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import {
  csrfKlopt, csrfVan, herkomstKlopt, maakState, stateKlopt, leesCookies, leesKeuze, leesMbState, leesSessie, maakKeuze, maakMbState, maakSessie,
  SESSIE_DUUR, wisCookie, zetCookie, type SessieSleutels,
} from "../src/web/sessie.ts";
import { CSP, esc, html, Html, naar, pagina } from "../src/web/html.ts";
import { CSS, KLEUREN, STIJL_PAD, stijlAntwoord } from "../src/web/stijl.ts";

const NU = 1_762_750_000;
const bos: SessieSleutels = { huidig: "s1", sleutels: { s1: new Uint8Array(32).fill(7), s2: new Uint8Array(32).fill(9) } };
const ADRES = "https://klopt.dortus.com";

test("sessie: heen en terug, vals, verlopen, andere sleutel, sleutelwissel", async () => {
  const c = await maakSessie(bos, "w-1", NU);
  assert.equal(await leesSessie(bos, c, NU), "w-1");
  assert.equal(await leesSessie(bos, c, NU + SESSIE_DUUR), null, "verlopen");
  const [v, w, t, m] = c.split(".");
  assert.equal(await leesSessie(bos, [v, "w-2", t, m].join("."), NU), null, "andere winkel");
  assert.equal(await leesSessie(bos, [v, w, String(Number(t) + 999), m].join("."), NU), null, "langer gemaakt");
  assert.equal(await leesSessie(bos, [v, w, t, m.slice(0, -1) + (m.endsWith("A") ? "B" : "A")].join("."), NU), null);
  assert.equal(await leesSessie(bos, undefined, NU), null);
  assert.equal(await leesSessie(bos, "rommel", NU), null);
  assert.equal(await leesSessie({ huidig: "s1", sleutels: { s1: new Uint8Array(32).fill(1) } }, c, NU), null, "andere sleutel");
  // Na een wissel naar s2 blijft een cookie van s1 geldig zolang s1 in de bos staat.
  assert.equal(await leesSessie({ ...bos, huidig: "s2" }, c, NU), "w-1");
  assert.equal(await leesSessie({ huidig: "s2", sleutels: { s2: bos.sleutels.s2 } }, c, NU), null);
  await assert.rejects(maakSessie(bos, "w.1", NU));
  await assert.rejects(maakSessie({ huidig: "k", sleutels: { k: new Uint8Array(16) } }, "w-1", NU), "te korte sleutel");
  assert.equal(await leesSessie(bos, ["__proto__", w, t, m].join("."), NU), null);
  assert.equal(await leesSessie(bos, await maakMbState(bos, "abc", "w-1", NU), NU), null, "Moneybird-state is geen sessie");
});

test("state: onvoorspelbaar, 43 tekens, vergelijken", () => {
  const a = maakState(), b = maakState();
  assert.notEqual(a, b);
  assert.match(a, /^[A-Za-z0-9_-]{43}$/);
  assert.equal(stateKlopt(a, a), true);
  assert.equal(stateKlopt(a, b), false);
  assert.equal(stateKlopt(undefined, a), false);
  assert.equal(stateKlopt(a, null), false);
});

test("csrf: hoort bij precies dit cookie", async () => {
  const c = await maakSessie(bos, "w-1", NU);
  const t = await csrfVan(bos, c);
  assert.equal(await csrfKlopt(bos, c, t), true);
  assert.equal(await csrfKlopt(bos, await maakSessie(bos, "w-2", NU), t), false);
  assert.equal(await csrfKlopt(bos, c, ""), false);
  assert.equal(await csrfKlopt(bos, c, null), false);
  assert.equal(await csrfKlopt(bos, undefined, t), false);
  assert.equal(await csrfKlopt(bos, "x9.a.b.c", t), false, "onbekende versie gooit niet");
});

test("(j) herkomst: Origin, anders Referer, geen van beide is nee", () => {
  const r = (kop: Record<string, string>) => new Request(`${ADRES}/app/x`, { method: "POST", headers: kop });
  assert.equal(herkomstKlopt(r({ origin: ADRES }), ADRES), true);
  assert.equal(herkomstKlopt(r({ origin: "https://boos.example" }), ADRES), false);
  assert.equal(herkomstKlopt(r({ origin: "https://boos.example", referer: `${ADRES}/app` }), ADRES), false, "Origin gaat voor");
  assert.equal(herkomstKlopt(r({ referer: `${ADRES}/app` }), ADRES), true);
  assert.equal(herkomstKlopt(r({ referer: "https://klopt.dortus.com.boos.example/app" }), ADRES), false);
  assert.equal(herkomstKlopt(r({}), ADRES), false);
});

test("Moneybird-state hoort bij de winkel", async () => {
  const c = await maakMbState(bos, "abc123", "w-1", NU);
  assert.equal(await leesMbState(bos, c, "w-1", NU), "abc123");
  assert.equal(await leesMbState(bos, c, "w-2", NU), null, "andere winkel");
  assert.equal(await leesMbState(bos, c, "w-1", NU + 601), null, "na 10 minuten weg");
  const d = c.split(".");
  assert.equal(await leesMbState(bos, [d[0], "abc124", d[2], d[3], d[4]].join("."), "w-1", NU), null);
  assert.equal(await leesMbState(bos, [d[0], d[1], d[2], String(NU + 9999), d[4]].join("."), "w-1", NU), null, "langer gemaakt");
  assert.equal(await leesMbState(bos, undefined, "w-1", NU), null);
});

test("keuze-cookie: versleuteld, met vlag, verloopt, niet te vervalsen", async () => {
  const k = { tokens: { accessToken: "GEHEIM-TT" }, shops: [{ id: "1", cipher: "c1", naam: "A" }, { id: "2", cipher: "c2", naam: "B" }], openId: "o1", stateKlopte: false };
  const c = await maakKeuze(bos, k, NU);
  assert.ok(!c.includes("GEHEIM") && !atob(c.split(".")[2].replace(/-/g, "+").replace(/_/g, "/")).includes("GEHEIM"), "niet leesbaar");
  const terug = await leesKeuze(bos, c, NU);
  assert.equal(terug?.stateKlopte, false);
  assert.deepEqual(terug?.shops.map((s) => s.id), ["1", "2"]);
  assert.equal(await leesKeuze(bos, c, NU + 601), null, "na 10 minuten weg");
  const d = c.split(".");
  const midden = Math.floor(d[2].length / 2);
  const ander = d[2][midden] === "A" ? "B" : "A";
  assert.equal(await leesKeuze(bos, [d[0], d[1], d[2].slice(0, midden) + ander + d[2].slice(midden + 1)].join("."), NU), null);
  assert.equal(await leesKeuze(bos, ["s2", d[1], d[2]].join("."), NU), null, "versie hoort bij de sleutel");
  assert.equal(await leesKeuze(bos, "a.b", NU), null);
});

test("(a)-deel en (c)-deel: cookies zijn __Host-, HttpOnly, Secure, Lax; wissen met Max-Age=0", () => {
  const z = zetCookie("__Host-klopt", "x", 60);
  for (const deel of ["Path=/", "HttpOnly", "Secure", "SameSite=Lax", "Max-Age=60"]) assert.ok(z.includes(deel), deel);
  assert.ok(!/Domain=/i.test(z));
  assert.ok(wisCookie("__Host-klopt_tt").includes("Max-Age=0"));
  assert.throws(() => zetCookie("a", "x; Domain=boos.example", 1));
  assert.throws(() => naar("https://boos.example/"));
  assert.throws(() => naar("//boos.example/app"));
  assert.equal(naar("https://moneybird.com/oauth/authorize?x=1").status, 302);
  const r = new Request(ADRES, { headers: { cookie: "a=1; __Host-klopt=v.w.1.m; a=2" } });
  assert.deepEqual(leesCookies(r), { a: "1", "__Host-klopt": "v.w.1.m" });
});

test("(l) escapen: invoer wordt nooit HTML", () => {
  const naam = `<script>alert("x")</script>' & "`;
  const h = html`<p title="${naam}">${naam}</p>${[naam, html`<b>${naam}</b>`]}`;
  assert.ok(!h.tekst.includes("<script>"));
  assert.ok(h.tekst.includes("&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;&#39; &amp; &quot;"));
  assert.ok(h.tekst.includes("<b>&lt;script&gt;"), "geneste Html blijft HTML, de inhoud niet");
  assert.equal(esc(null), "");
  assert.equal(html`${false}${undefined}`.tekst, "");
});

test("(m) kopregels, geen inline stijl, stijl.css bestaat", async () => {
  const r = pagina({ titel: "T <x>", inhoud: html`<p>hoi</p>`, stap: { nu: 1, van: 3 }, cookies: [zetCookie("a", "b", 1), zetCookie("c", "d", 1)] });
  assert.equal(r.headers.get("content-security-policy"), CSP);
  assert.equal(r.headers.get("x-content-type-options"), "nosniff");
  assert.equal(r.headers.get("cache-control"), "no-store");
  assert.equal(r.headers.get("referrer-policy"), "same-origin");
  assert.ok(r.headers.get("strict-transport-security"));
  assert.equal(r.headers.getSetCookie().length, 2);
  const tekst = await r.text();
  assert.ok(tekst.includes("Stap 1 van 3"));
  assert.ok(tekst.includes(`href="${STIJL_PAD}"`));
  assert.ok(tekst.includes("T &lt;x&gt; · Klopt"));
  assert.ok(!/<style|style=|<script/i.test(tekst), "geen inline stijl of script");
  assert.ok(!CSP.includes("unsafe-inline"));
  assert.ok(CSP.includes("form-action 'self' https://moneybird.com"));
  const s = stijlAntwoord();
  assert.equal(s.headers.get("content-type"), "text/css; charset=utf-8");
  assert.ok(s.headers.get("cache-control")!.includes("max-age"));
  const d = naar("/app", [zetCookie("a", "b", 1)]);
  assert.equal(d.status, 302);
  assert.equal(d.headers.get("location"), "/app");
  assert.equal(d.headers.get("cache-control"), "no-store");
});

test("(q) kleuren gelijk aan 'Stijl voor de bouw' in ontwerp.md", () => {
  const ontwerp = readFileSync(new URL("../ontwerp.md", import.meta.url), "utf8");
  const blok = ontwerp.slice(ontwerp.indexOf("### Stijl voor de bouw"), ontwerp.indexOf("### Moet in de bouw"));
  const kleurregel = blok.split("\n").find((r) => r.includes("**Kleuren:**"))!;
  const inOntwerp = new Set([...kleurregel.matchAll(/`(#[0-9A-Fa-f]{6})`/g)].map((m) => m[1].toUpperCase()));
  const inStijl = new Set(Object.values(KLEUREN).map((x) => x.toUpperCase()));
  inStijl.delete("#FFFFFF"); // "kaart wit" staat er als woord
  assert.deepEqual([...inStijl].sort(), [...inOntwerp].sort());
  for (const kleur of inOntwerp) assert.ok(CSS.toUpperCase().includes(kleur), `${kleur} gebruikt in de CSS`);
  assert.ok(CSS.includes("tabular-nums"));
  assert.ok(CSS.includes("border-radius:14px") && CSS.includes("border-radius:10px"));
});
