// Routes van Moneybird bij scherm 1 (ontwerp-schermen.md versie 3, stap 3 tot 5): inloggen starten, terugkeer met
// tokens opslaan (de nieuwe toestemming wint, het vervangen paar intrekken), administratie kiezen. Opgeslagen tokens
// alleen onder het winkelslot via TokenBron; verse tokens uit een code mogen daarbuiten.
import { D1Opslag } from "../d1/opslag.ts";
import { moneybirdSoort, ontsleutel, tijdelijk, TokenBron, versleutel } from "../d1/tokens.ts";
import { MoneybirdClient } from "../moneybird/client.ts";
import { administraties, type Administratie } from "../moneybird/lezen.ts";
import { inlogLink as mbInlogLink, trekIn, wisselCode, type MoneybirdTokens } from "../moneybird/oauth.ts";
import { WINKELSLOT } from "../worker.ts";
import { formulier, foutTekst, instellingenVan, postKlopt, sessieVan, toon, WEB_SLOT_DUUR, type Ctx, type Sessie, type WinkelRij } from "./basis.ts";
import { naar } from "./html.ts";
import { evenGeduld, foutBijKoppelen, gekoppeld, kiesAdministratie, koppelScherm, nietVoorJou, uitgelogd, type Scherm } from "./schermen.ts";
import { csrfVan, KORT, leesMbState, maakMbState, maakState, MB_STATE_COOKIE, stateKlopt, wisCookie, zetCookie } from "./sessie.ts";

const geweigerd = () => new Response("Geweigerd", { status: 403 });
const metStatus = (s: Scherm, status: number): Scherm => ({ ...s, status });
export const winkelnaam = (rij: WinkelRij) => String(instellingenVan(rij).winkelnaam ?? "") || "je winkel";
const bruikbaar = (lijst: Administratie[]) => lijst.filter((a) => a.land.toUpperCase() === "NL" && a.valuta.toUpperCase() === "EUR");

/** POST /app/moneybird/start: state gebonden aan de winkel in een kort cookie, door naar Moneybird. */
export async function moneybirdStart(c: Ctx): Promise<Response> {
  const form = await formulier(c);
  const s = await sessieVan(c);
  if (!s) return toon(metStatus(uitgelogd(), 401));
  if (!(await postKlopt(c, s.cookie, form))) return geweigerd();
  const state = maakState();
  const cookie = await maakMbState(c.o.sessie, state, s.winkel.id, c.nu);
  return naar(mbInlogLink(c.o.moneybirdApp, state), [zetCookie(MB_STATE_COOKIE, cookie, KORT)]);
}

function mbClient(c: Ctx, accessToken: string): MoneybirdClient {
  return new MoneybirdClient({ accessToken, fetchFn: c.fetch, nu: () => c.nu, slaap: async () => {} });
}

async function trekInMetAlarm(c: Ctx, winkel: string, refreshToken: string, wat: string): Promise<void> {
  try {
    await trekIn(c.o.moneybirdApp, refreshToken, c.fetch);
  } catch (e) {
    c.o.log(`ALARM winkel ${winkel}: ${wat} Moneybird-paar niet ingetrokken (${foutTekst(e)}); trek de koppeling handmatig in`);
  }
}

/** GET /app/moneybird/terug. Eerst sessie, dan state van deze winkel; elke terugkeer wist het state-cookie. */
export async function moneybirdTerug(c: Ctx): Promise<Response> {
  const wis = wisCookie(MB_STATE_COOKIE);
  const q = c.url.searchParams;
  const s = await sessieVan(c);
  if (!s) return toon(metStatus(uitgelogd(), 400), [wis]);
  const state = await leesMbState(c.o.sessie, c.cookies[MB_STATE_COOKIE], s.winkel.id, c.nu);
  if (!stateKlopt(state ?? undefined, q.get("state"))) return toon(metStatus(foutBijKoppelen("Moneybird", "anders"), 400), [wis]);
  const code = q.get("code");
  if (q.get("error") || !code) {
    const melding = "Je gaf Moneybird geen toestemming. Probeer het opnieuw als je wilt.";
    return toon(koppelScherm({ winkelnaam: winkelnaam(s.winkel), csrf: await csrfVan(c.o.sessie, s.cookie), melding }), [wis]);
  }

  let nieuw: MoneybirdTokens;
  try {
    nieuw = await wisselCode(c.o.moneybirdApp, code, c.fetch);
  } catch (e) {
    c.o.log(`web: Moneybird-terugkeer mislukt: ${foutTekst(e)}`);
    return toon(foutBijKoppelen("Moneybird", tijdelijk(e) ? "andere_kant" : "anders"), [wis]);
  }

  const opgeslagen = await slaMbTokensOp(c, s.winkel, nieuw);
  if (opgeslagen === "ontkoppeld") return toon(uitgelogd(), [wis]);
  if (opgeslagen === "mislukt") return toon(foutBijKoppelen("Moneybird", "anders"), [wis]);

  let lijst: Administratie[];
  try {
    lijst = await administraties(mbClient(c, nieuw.accessToken));
  } catch (e) {
    c.o.log(`web: Moneybird-administraties lezen mislukt: ${foutTekst(e)}`);
    return toon(foutBijKoppelen("Moneybird", tijdelijk(e) ? "andere_kant" : "anders"), [wis]);
  }
  return naAdministraties(c, s, lijst, [wis]);
}

/**
 * Voorwaardelijk op mb_versie, hoogstens 3 keer (een verversing van de consumer tussen lezen en schrijven). Gelukt: het
 * vervangen paar intrekken als zijn refresh token anders is. Na 3 keer mislukt: het verse paar intrekken.
 */
export async function slaMbTokensOp(c: Ctx, rij: WinkelRij, nieuw: MoneybirdTokens): Promise<"ok" | "ontkoppeld" | "mislukt"> {
  const tekst = await versleutel(c.o.sleutels, rij.id, JSON.stringify(nieuw));
  let oud = { t: rij.mb_tokens, v: Number(rij.mb_versie) };
  for (let poging = 0; poging < 3; poging++) {
    c.teller.neem();
    const r = await c.o.db
      .prepare(`UPDATE winkels SET mb_tokens = ?, mb_versie = mb_versie + 1 WHERE id = ? AND mb_versie = ? AND ontkoppeld_op IS NULL`)
      .bind(tekst, rij.id, oud.v)
      .run();
    if (r.meta.changes === 1) {
      if (oud.t) {
        try {
          const vorig = JSON.parse(await ontsleutel(c.o.sleutels, rij.id, oud.t)) as MoneybirdTokens;
          if (vorig.refreshToken && vorig.refreshToken !== nieuw.refreshToken) await trekInMetAlarm(c, rij.id, vorig.refreshToken, "vervangen");
        } catch (e) {
          c.o.log(`ALARM winkel ${rij.id}: vervangen Moneybird-paar onleesbaar (${foutTekst(e)}); trek de koppeling handmatig in`);
        }
      }
      return "ok";
    }
    c.teller.neem();
    const vers = await c.o.db.prepare(`SELECT mb_tokens AS t, mb_versie AS v FROM winkels WHERE id = ? AND ontkoppeld_op IS NULL`).bind(rij.id).first<{ t: string | null; v: number }>();
    if (!vers) {
      await trekInMetAlarm(c, rij.id, nieuw.refreshToken, "vers (winkel ontkoppeld)");
      return "ontkoppeld";
    }
    oud = { t: vers.t, v: Number(vers.v) };
  }
  await trekInMetAlarm(c, rij.id, nieuw.refreshToken, "vers (niet op te slaan)");
  return "mislukt";
}

/** Opslaan in de vorm die de consumer leest (`AdministratieInfo`), en de kolom gelijk houden. */
async function slaAdministratieOp(c: Ctx, winkel: string, a: Administratie | null): Promise<void> {
  c.teller.neemAfmaken();
  await c.o.db
    .prepare(
      a
        ? `UPDATE winkels SET administratie = ?, instellingen = json_set(coalesce(instellingen, '{}'), '$.administratie', json(?)) WHERE id = ? AND ontkoppeld_op IS NULL`
        : `UPDATE winkels SET administratie = NULL, instellingen = json_remove(coalesce(instellingen, '{}'), '$.administratie') WHERE id = ? AND ontkoppeld_op IS NULL`,
    )
    .bind(...(a ? [a.id, JSON.stringify({ id: a.id, periodLockedUntil: a.periodLockedUntil }), winkel] : [winkel]))
    .run();
}

/** Nul, één of meer bruikbare administraties; een opgeslagen administratie die niet meer in de lijst staat wordt leeggemaakt. */
async function naAdministraties(c: Ctx, s: Sessie, lijst: Administratie[], cookies: string[]): Promise<Response> {
  const nl = bruikbaar(lijst);
  const huidig = s.winkel.administratie;
  if (huidig && nl.some((a) => a.id === huidig)) return naar("/app", cookies);
  if (huidig) await slaAdministratieOp(c, s.winkel.id, null);
  if (nl.length === 0) return toon(nietVoorJou({ soort: lijst.length ? "geen_nl_administratie" : "geen_administratie" }), cookies);
  if (nl.length === 1) {
    await slaAdministratieOp(c, s.winkel.id, nl[0]);
    return naar("/app", cookies);
  }
  return toon(kiesAdministratie(nl.map((a) => ({ id: a.id, naam: a.naam })), await csrfVan(c.o.sessie, s.cookie)), cookies);
}

/** Iets doen onder het winkelslot (60 s). Bezet: null. Het slot gaat altijd terug. */
export async function onderSlot<R>(c: Ctx, winkel: string, doe: () => Promise<R>): Promise<{ uit: R } | null> {
  const opslag = new D1Opslag(c.o.db, winkel, c.teller);
  const eigenaar = c.o.eigenaar?.() ?? `web-${crypto.randomUUID()}`;
  if (!(await opslag.neemSlot(WINKELSLOT, eigenaar, c.nu + WEB_SLOT_DUUR, c.nu))) return null;
  try {
    return { uit: await doe() };
  } finally {
    c.teller.neemAfmaken();
    await c.o.db.prepare(`DELETE FROM sloten WHERE winkel = ? AND statement_id = ? AND eigenaar = ?`).bind(winkel, WINKELSLOT, eigenaar).run();
  }
}

/** Administraties met de opgeslagen tokens, onder het slot (TokenBron ververst en doet bij een 401 één nieuwe poging). */
async function lijstOnderSlot(c: Ctx, s: Sessie): Promise<{ uit: Administratie[] } | null> {
  return onderSlot(c, s.winkel.id, async () => {
    const bron = new TokenBron({ db: c.o.db, winkel: s.winkel.id, soort: moneybirdSoort(c.o.moneybirdApp), sleutels: c.o.sleutels, budget: c.budget, fetchFn: c.o.fetchFn, nu: () => c.nu, log: c.o.log });
    await bron.vanRij(s.winkel.mb_tokens, s.winkel.mb_versie);
    return bron.met((t) => administraties(mbClient(c, t.accessToken)));
  });
}

/** GET /app met Moneybird-tokens maar zonder administratie: keuzescherm (of meteen opslaan bij één). */
export async function kiesAdministratieScherm(c: Ctx, s: Sessie): Promise<Response> {
  let r: { uit: Administratie[] } | null;
  try {
    r = await lijstOnderSlot(c, s);
  } catch (e) {
    c.o.log(`web: administraties lezen voor winkel ${s.winkel.id} mislukt: ${foutTekst(e)}`);
    return toon(foutBijKoppelen("Moneybird", tijdelijk(e) ? "andere_kant" : "anders"));
  }
  if (!r) return toon(evenGeduld());
  const uit = await naAdministraties(c, s, r.uit, []);
  return uit.status === 302 ? toon(gekoppeld(winkelnaam(s.winkel))) : uit;
}

/** POST /app/moneybird/administratie: de lijst opnieuw ophalen onder het slot; alleen een id uit die lijst. */
export async function moneybirdAdministratie(c: Ctx): Promise<Response> {
  const form = await formulier(c);
  const s = await sessieVan(c);
  if (!s) return toon(metStatus(uitgelogd(), 401));
  if (!(await postKlopt(c, s.cookie, form))) return geweigerd();
  let r: { uit: Administratie[] } | null;
  try {
    r = await lijstOnderSlot(c, s);
  } catch (e) {
    c.o.log(`web: administraties lezen voor winkel ${s.winkel.id} mislukt: ${foutTekst(e)}`);
    return toon(foutBijKoppelen("Moneybird", tijdelijk(e) ? "andere_kant" : "anders"));
  }
  if (!r) return toon(evenGeduld());
  const keuze = bruikbaar(r.uit).find((a) => a.id === form.get("administratie"));
  if (!keuze) return toon(metStatus(foutBijKoppelen("Moneybird", "anders"), 400));
  await slaAdministratieOp(c, s.winkel.id, keuze);
  return naar("/app");
}
