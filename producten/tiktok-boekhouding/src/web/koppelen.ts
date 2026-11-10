// Routes van TikTok bij scherm 1 (ontwerp-schermen.md versie 3, "Scherm 1, koppelen", stap 1): inloggen starten,
// terugkeer, winkel kiezen, en de webhooks aanmelden. Tokens die net uit een code komen worden hier buiten het winkelslot
// opgeslagen (bewust: de nieuwe toestemming van de verkoper wint altijd, zie de kop van src/d1/tokens.ts).
import { haalTokens, inlogLink, type Tokens } from "../../../tiktok-shop-basis/src/auth.ts";
import { geautoriseerdeWinkels, meldWebhookAan, type Winkel } from "../../../tiktok-shop-basis/src/endpoints.ts";
import { tijdelijk, versleutel } from "../d1/tokens.ts";
import { WEBHOOK_PAD } from "../webhook.ts";
import { formulier, foutTekst, NOOIT, postKlopt, snelleTikTok, toon, type Ctx } from "./basis.ts";
import { naar } from "./html.ts";
import { foutBijKoppelen, kiesWinkel, nietVoorJou, openAls, weigeringTikTok, type Scherm } from "./schermen.ts";
import { csrfVan, KEUZE_COOKIE, KORT, leesKeuze, maakKeuze, maakSessie, maakState, SESSIE_COOKIE, SESSIE_DUUR, stateKlopt, TT_STATE_COOKIE, wisCookie, zetCookie } from "./sessie.ts";

/** Een keuze-cookie groter dan dit weigeren (browsers houden ±4096 bytes per cookie aan). */
export const MAX_KEUZE = 3800;

const metStatus = (s: Scherm, status: number): Scherm => ({ ...s, status });

/** Alleen wat TokenBron nodig heeft; scopes en verkopersgegevens hoeven niet in D1 of het keuze-cookie. */
function teBewaren(t: Tokens): Tokens {
  return { ...t, grantedScopes: [], sellerName: "", sellerBaseRegion: "", userType: 0 };
}

/** GET /app/tiktok/start: eigen state in een kort cookie, door naar het inlogscherm van TikTok. */
export function tiktokStart(c: Ctx): Response {
  const state = maakState();
  return naar(inlogLink(c.o.tiktokServiceId, state), [zetCookie(TT_STATE_COOKIE, state, KORT)]);
}

/** GET /app/tiktok/terug. Elke terugkeer wist het state-cookie, ook een mislukte. */
export async function tiktokTerug(c: Ctx): Promise<Response> {
  const wis = wisCookie(TT_STATE_COOKIE);
  const q = c.url.searchParams;
  const code = q.get("code");
  if (q.get("error") || !code || code === "null") return toon(weigeringTikTok(), [wis]);
  const state = q.get("state");
  if (state !== null && !stateKlopt(c.cookies[TT_STATE_COOKIE], state)) return toon(metStatus(foutBijKoppelen("TikTok", "anders"), 400), [wis]);
  const stateKlopte = state !== null;

  let tokens: Tokens, shops: Winkel[];
  try {
    tokens = await haalTokens(c.o.tiktokApp, code, c.fetch);
    shops = await geautoriseerdeWinkels(snelleTikTok(c), tokens.accessToken);
  } catch (e) {
    c.o.log(`web: TikTok-terugkeer mislukt: ${foutTekst(e)}`);
    return toon(foutBijKoppelen("TikTok", tijdelijk(e) ? "andere_kant" : "anders"), [wis]);
  }

  const nl = shops.filter((s) => String(s.region).toUpperCase() === "NL" && s.id && s.cipher);
  if (nl.length === 0) return toon(nietVoorJou({ soort: "land", land: tokens.sellerBaseRegion || shops[0]?.region || "?" }), [wis]);
  if (nl.length === 1) return klaarMetWinkel(c, nl[0], tokens, stateKlopte, [wis]);

  const keuze = await maakKeuze(
    c.o.sessie,
    { tokens: teBewaren(tokens), shops: nl.map((s) => ({ id: s.id, cipher: s.cipher, naam: s.name })), openId: tokens.openId, stateKlopte },
    c.nu,
  );
  if (keuze.length > MAX_KEUZE) {
    c.o.log(`web: keuze-cookie te groot (${keuze.length} tekens, ${nl.length} winkels)`);
    return toon(foutBijKoppelen("TikTok", "anders"), [wis]);
  }
  return toon(kiesWinkel(nl.map((s) => ({ id: s.id, naam: s.name })), await csrfVan(c.o.sessie, keuze)), [wis, zetCookie(KEUZE_COOKIE, keuze, KORT)]);
}

/** POST /app/tiktok/kies: alleen een shop-id uit het keuze-cookie, met de csrf van dat cookie. */
export async function tiktokKies(c: Ctx): Promise<Response> {
  const form = await formulier(c);
  const waarde = c.cookies[KEUZE_COOKIE];
  if (!(await postKlopt(c, waarde, form))) return new Response("Geweigerd", { status: 403 });
  const keuze = await leesKeuze(c.o.sessie, waarde, c.nu);
  const shop = keuze?.shops.find((s) => s.id === form.get("shop"));
  if (!keuze || !shop) return toon(metStatus(foutBijKoppelen("TikTok", "anders"), 400), [wisCookie(KEUZE_COOKIE)]);
  const tokens = { ...(keuze.tokens as Tokens), openId: keuze.openId };
  return klaarMetWinkel(c, { id: shop.id, cipher: shop.cipher, name: shop.naam, region: "NL", seller_type: "", code: "" }, tokens, keuze.stateKlopte, [wisCookie(KEUZE_COOKIE)]);
}

/** Opslaan, webhooks aanmelden, en een sessie alleen bij een kloppende state (anders "Open Klopt als ..."). */
async function klaarMetWinkel(c: Ctx, shop: Winkel, tokens: Tokens, stateKlopte: boolean, cookies: string[]): Promise<Response> {
  const naam = shop.name || tokens.sellerName || "je winkel";
  const id = await slaWinkelOp(c, shop, naam, tokens);
  await meldWebhooksAan(c, id, tokens.accessToken, shop.cipher);
  if (!stateKlopte) return toon(openAls(naam), cookies);
  return naar("/app", [...cookies, zetCookie(SESSIE_COOKIE, await maakSessie(c.o.sessie, id, c.nu), SESSIE_DUUR)]);
}

/**
 * Bestaande gekoppelde rij: nieuwe tokens (versie +1), winkelfout van TikTok weg, een winkel die aan staat meteen wekken.
 * Geen rij: INSERT met volgende_run NOOIT. Botst de INSERT op de unieke index (twee terugkeren tegelijk), dan het id van
 * de andere lezen, opnieuw versleutelen met dat id (AAD) en bijwerken. Geeft de winkel-id.
 */
export async function slaWinkelOp(c: Ctx, shop: Winkel, naam: string, tokens: Tokens): Promise<string> {
  const json = JSON.stringify(teBewaren(tokens));
  for (let ronde = 0; ronde < 3; ronde++) {
    c.teller.neem();
    const rij = await c.o.db
      .prepare(`SELECT id, json_extract(instellingen, '$.open_id') AS open_id FROM winkels WHERE shop_id = ? AND ontkoppeld_op IS NULL`)
      .bind(shop.id)
      .first<{ id: string; open_id: string | null }>();
    if (rij) {
      if (rij.open_id && tokens.openId && rij.open_id !== tokens.openId) c.o.log(`web: winkel ${rij.id} gekoppeld door een andere TikTok-gebruiker (open_id veranderd)`);
      c.teller.neem();
      const r = await c.o.db
        .prepare(
          `UPDATE winkels SET tt_tokens = ?, tt_versie = tt_versie + 1, shop_cipher = ?,
             instellingen = json_set(coalesce(instellingen, '{}'), '$.winkelnaam', ?, '$.open_id', ?),
             winkelfout_sinds = CASE WHEN json_extract(winkelfout, '$.kant') = 'tiktok' THEN NULL ELSE winkelfout_sinds END,
             winkelfout = CASE WHEN json_extract(winkelfout, '$.kant') = 'tiktok' THEN NULL ELSE winkelfout END,
             volgende_run = CASE WHEN volgende_run < ? THEN ? ELSE volgende_run END
           WHERE id = ? AND ontkoppeld_op IS NULL`,
        )
        .bind(await versleutel(c.o.sleutels, rij.id, json), shop.cipher, naam, tokens.openId, NOOIT, c.nu, rij.id)
        .run();
      if (r.meta.changes === 1) return rij.id;
      continue; // net ontkoppeld: opnieuw, dan wordt het een nieuwe rij
    }
    const id = crypto.randomUUID();
    c.teller.neem();
    const r = await c.o.db
      .prepare(
        `INSERT INTO winkels (id, shop_id, shop_cipher, tt_tokens, instellingen, volgende_run)
         VALUES (?, ?, ?, ?, json_object('winkelnaam', ?, 'open_id', ?), ?) ON CONFLICT DO NOTHING`,
      )
      .bind(id, shop.id, shop.cipher, await versleutel(c.o.sleutels, id, json), naam, tokens.openId, NOOIT)
      .run();
    if (r.meta.changes === 1) return id;
    // Botsing: een andere terugkeer was eerder. De volgende ronde leest die rij en werkt hem bij.
  }
  throw new Error(`winkel ${shop.id} opslaan lukte niet na 3 rondes`);
}

/** Beide webhooks; gelukt zet `$.webhooks` op 1, mislukt op 0 (de volgende opening van /app probeert opnieuw). */
export async function meldWebhooksAan(c: Ctx, winkel: string, accessToken: string, cipher: string): Promise<boolean> {
  let gelukt = true;
  try {
    const t = snelleTikTok(c);
    const adres = new URL(WEBHOOK_PAD, c.o.appAdres).toString();
    await meldWebhookAan(t, accessToken, cipher, "SELLER_DEAUTHORIZATION", adres);
    await meldWebhookAan(t, accessToken, cipher, "UPCOMING_AUTHORIZATION_EXPIRATION", adres);
  } catch (e) {
    gelukt = false;
    c.o.log(`web: webhooks aanmelden voor winkel ${winkel} mislukt: ${foutTekst(e)}`);
  }
  c.teller.neemAfmaken();
  await c.o.db
    .prepare(`UPDATE winkels SET instellingen = json_set(coalesce(instellingen, '{}'), '$.webhooks', ?) WHERE id = ? AND ontkoppeld_op IS NULL`)
    .bind(gelukt ? 1 : 0, winkel)
    .run();
  return gelukt;
}
