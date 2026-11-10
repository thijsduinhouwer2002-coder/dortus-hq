// Plaatjes van de echte schermen voor Daan (ontwerp-schermen.md, laatste stap van deel 1). Draait de router met
// nagebootste TikTok, Moneybird en D1 op een lokale server en maakt met Playwright plaatjes op 1280 en 390 breed.
// Gebruik: node schermen/maak.ts <uitmap>. In GitHub Actions: .github/workflows/tiktok-boekhouding-schermen.yml.
import { createServer } from "node:http";
import { readFileSync, mkdirSync } from "node:fs";
import { createRequire } from "node:module";
import { NepD1 } from "../test/d1-nep.ts";
import { router, type WebOmgeving } from "../src/web/router.ts";
import { toon } from "../src/web/basis.ts";
import { evenGeduld, foutBijKoppelen, nietVoorJou, uitgelogd } from "../src/web/schermen.ts";
import { maakMbState, SESSIE_COOKIE, MB_STATE_COOKIE, TT_STATE_COOKIE } from "../src/web/sessie.ts";
import { versleutel } from "../src/d1/tokens.ts";

// Via require, zodat ook een Playwright uit NODE_PATH gevonden wordt (lokaal) en een uit npm install (Actions).
const { chromium } = createRequire(import.meta.url)("playwright");
const uit = process.argv[2] ?? "schermen/uit";
mkdirSync(uit, { recursive: true });
const NU = Math.floor(Date.now() / 1000);
const ADRES = "http://127.0.0.1:8789";
const bos = { huidig: "s1", sleutels: { s1: new Uint8Array(32).fill(7) } };
const sleutels = { huidig: "k1", sleutels: { k1: new Uint8Array(32).fill(3) } };

// Nagebootste wereld: één winkel in NL, of twee, of een Duitse; administraties naar keuze.
const w = {
  shops: [{ id: "111", name: "Bloem & Co", region: "NL", cipher: "C111" }],
  adms: [{ id: 501, name: "Bloem & Co BV", currency: "EUR", country: "NL", period_locked_until: null }] as any[],
};
const json = (d: unknown, s = 200) => new Response(JSON.stringify(d), { status: s });
const nepFetch = (async (input: any, init: any = {}) => {
  const u = new URL(String(input));
  if (u.hostname === "auth.tiktok-shops.com")
    return json({ code: 0, message: "ok", request_id: "r", data: { access_token: "a", access_token_expire_in: NU + 86400 * 7, refresh_token: "r", refresh_token_expire_in: NU + 86400 * 60, open_id: "o", seller_name: "Bloem & Co", seller_base_region: w.shops[0].region, user_type: 0, granted_scopes: [] } });
  if (u.pathname === "/authorization/202309/shops") return json({ code: 0, message: "ok", request_id: "r", data: { shops: w.shops.map((s) => ({ ...s, seller_type: "LOCAL", code: "X" })) } });
  if (u.pathname === "/event/202309/webhooks") return json({ code: 0, message: "ok", request_id: "r", data: {} });
  if (u.pathname === "/oauth/token") return json({ access_token: "mb", refresh_token: "mbr", scope: "documents settings", created_at: NU });
  if (u.pathname === "/oauth/revoke") return json({});
  if (u.pathname === "/api/v2/administrations.json") return json(w.adms);
  throw new Error(`onverwacht ${init.method ?? "GET"} ${u}`);
}) as typeof fetch;

const db = new NepD1();
const o: WebOmgeving = {
  db: db as any, wachtrij: { sendBatch: async () => {} }, fetchFn: nepFetch, log: (r) => console.log(r), sleutels,
  tiktokApp: { appKey: "k", appSecret: "s" }, moneybirdApp: { clientId: "c", clientSecret: "s", redirectUri: `${ADRES}/app/moneybird/terug` },
  sessie: bos, tiktokServiceId: "7000", appAdres: ADRES,
};

// Losse staten die je niet zomaar via de stroom bereikt: via /plaatje/<naam>.
const LOS: Record<string, () => Response> = {
  "fout-tiktok": () => toon(foutBijKoppelen("TikTok", "andere_kant")),
  "fout-moneybird": () => toon(foutBijKoppelen("Moneybird", "anders")),
  "even-geduld": () => toon(evenGeduld()),
  "niet-voor-jou-geen-administratie": () => toon(nietVoorJou({ soort: "geen_administratie" })),
  uitgelogd: () => toon(uitgelogd()),
};
const LETTERS = new URL("../public/fonts/", import.meta.url);

const server = createServer(async (req, res) => {
  const pad = req.url ?? "/";
  let antw: Response;
  if (pad.startsWith("/fonts/")) {
    try {
      antw = new Response(readFileSync(new URL(pad.slice(7).replace(/[^a-z0-9.-]/gi, ""), LETTERS)), { headers: { "content-type": "font/woff2" } });
    } catch {
      antw = new Response("", { status: 404 });
    }
  } else if (pad.startsWith("/plaatje/")) {
    antw = LOS[pad.slice(9)]?.() ?? new Response("", { status: 404 });
  } else {
    const body = req.method === "POST" ? await new Promise<string>((r) => { let b = ""; req.on("data", (c) => (b += c)); req.on("end", () => r(b)); }) : undefined;
    antw = await router(new Request(ADRES + pad, { method: req.method, headers: req.headers as any, body }), o, NU);
  }
  // Cookies zet de browser hier niet zelf (http, __Host- vraagt https); de plaatjes krijgen ze via addCookies.
  res.writeHead(antw.status, Object.fromEntries([...antw.headers.entries()].filter(([k]) => k !== "set-cookie" && k !== "strict-transport-security")));
  res.end(Buffer.from(await antw.arrayBuffer()));
});
await new Promise<void>((r) => server.listen(8789, "127.0.0.1", r));

// Cookies voor de schermen achter een sessie: de TikTok-terugkeer direct via de router (state klopt).
async function sessieVoor(): Promise<string> {
  const r = await router(new Request(`${ADRES}/app/tiktok/terug?code=x&state=st`, { headers: { cookie: `${TT_STATE_COOKIE}=st` } }), o, NU);
  return r.headers.getSetCookie().find((c) => c.startsWith(SESSIE_COOKIE + "="))!.split(";")[0].split("=")[1];
}

const browser = await chromium.launch();
const breedtes = [1280, 390];
async function foto(naam: string, pad: string, cookie?: Record<string, string>) {
  for (const breed of breedtes) {
    const ctx = await browser.newContext({ viewport: { width: breed, height: breed > 600 ? 800 : 844 }, deviceScaleFactor: 2 });
    if (cookie) await ctx.addCookies(Object.entries(cookie).map(([name, value]) => ({ name, value, domain: "127.0.0.1", path: "/", secure: true, httpOnly: true, sameSite: "Lax" as const })));
    const page = await ctx.newPage();
    const fouten: string[] = [];
    // Alleen fouten van onderdelen (stijl, letters, plaatjes); een 502 of 503 van de pagina zelf hoort bij die staat.
    page.on("response", (r: any) => { if (r.status() >= 400 && r.request().resourceType() !== "document") fouten.push(`${r.status()} ${r.url()}`); });
    page.on("console", (m: any) => { if (m.type() === "error" && !m.text().startsWith("Failed to load resource")) fouten.push(m.text()); });
    await page.goto(ADRES + pad);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: `${uit}/${naam}-${breed}.png`, fullPage: true });
    if (fouten.length) console.log(`LET OP ${naam} ${breed}: ${fouten.join(" | ")}`);
    await ctx.close();
  }
  console.log(`klaar: ${naam}`);
}

const sessie = await sessieVoor();
const id = sessie.split(".")[1];
await foto("1-koppelen", "/app", { [SESSIE_COOKIE]: sessie });
await foto("1b-niet-voor-jou-exact", "/app/niet-voor-jou?voor=exact");
await foto("1c-open-als", "/app/tiktok/terug?code=x");

// Meer administraties: keuzescherm (Moneybird-tokens gezet, geen administratie).
w.adms = [...w.adms, { id: 502, name: "Bloem Holding BV", currency: "EUR", country: "NL", period_locked_until: null }];
db.sqlite.prepare("UPDATE winkels SET mb_tokens = ?, mb_versie = 1 WHERE id = ?").run(await versleutel(sleutels, id, JSON.stringify({ accessToken: "mb", refreshToken: "mbr", scope: "" })), id);
await foto("1d-kies-administratie", "/app", { [SESSIE_COOKIE]: sessie });
db.sqlite.prepare("UPDATE winkels SET administratie = '501', instellingen = json_set(instellingen, '$.administratie', json('{\"id\":\"501\",\"periodLockedUntil\":null}')) WHERE id = ?").run(id);
await foto("1e-gekoppeld", "/app", { [SESSIE_COOKIE]: sessie });

// Moneybird geweigerd: scherm 1 met de zachte melding.
db.sqlite.prepare("UPDATE winkels SET mb_tokens = NULL, administratie = NULL WHERE id = ?").run(id);
await foto("1f-moneybird-geweigerd", "/app/moneybird/terug?error=access_denied&state=mb", { [SESSIE_COOKIE]: sessie, [MB_STATE_COOKIE]: await maakMbState(bos, "mb", id, NU) });

// Twee NL-winkels: keuzescherm; een Duitse: nog niet voor jou.
w.shops = [{ id: "201", name: "Bloem & Co", region: "NL", cipher: "C201" }, { id: "202", name: "Bloem Outlet", region: "NL", cipher: "C202" }];
await foto("1g-kies-winkel", "/app/tiktok/terug?code=x");
w.shops = [{ id: "301", name: "Blumen Haus", region: "DE", cipher: "C301" }];
await foto("1h-niet-voor-jou-land", "/app/tiktok/terug?code=x");
await foto("1i-weigering-tiktok", "/app/tiktok/terug?error=auth_denied&code=null");
for (const naam of Object.keys(LOS)) await foto(`4-${naam}`, `/plaatje/${naam}`);

await browser.close();
server.close();
