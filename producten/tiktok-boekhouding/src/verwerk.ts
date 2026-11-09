// Product-laag, deel 2a (ontwerp-productlaag.md): een afrekening ophalen binnen het budget, en de proef (eis a).
// Boeken (verwerkWinkel, statustabel, slot, Moneybird) volgt in deel 2b.
import { MAX_POGINGEN, type TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { afrekeningen, transactiesVanAfrekening, transactiesVanBestelling, type Afrekening } from "../../tiktok-shop-basis/src/endpoints.ts";
import { TikTokApiError, type FoutSoort } from "../../tiktok-shop-basis/src/fouten.ts";
import { isBudgetOp, RESERVE_BOEKING, type Budget } from "./budget.ts";
import type { AfrekeningStatus, Opslag } from "./opslag.ts";
import type { MoneybirdClient } from "./moneybird/client.ts";
import { MoneybirdFout } from "./moneybird/fouten.ts";
import { boekAfrekening, type AdministratieInfo } from "./moneybird/boeken.ts";
import { bestellingenVan, bruikbaar, stelSamen, type Samenstelling } from "./samenstel.ts";
import type { AfrekeningInvoer, Koppeling, MbSoort } from "./moneybird/memoriaal.ts";

export interface TikTokDeps {
  tiktok: TikTokClient;
  accessToken: string;
  shopCipher: string;
  opslag: Opslag;
  budget: Budget;
  /** Unix-seconden. */
  nu: () => number;
}

/** TikTok-fouten die de hele winkel stilzetten (ontwerp, "Fouten die de hele winkel stilzetten"). */
const WINKEL_STOP: FoutSoort[] = ["token_verlopen", "geen_toegang", "handtekening_fout", "auth_code_ongeldig", "te_veel_verzoeken", "server"];

export class WinkelStop extends Error {
  readonly soort: string;
  readonly oorzaak: Error;
  constructor(soort: string, oorzaak: Error) {
    super(`${soort}: ${oorzaak.message}`);
    this.soort = soort;
    this.oorzaak = oorzaak;
    this.name = "WinkelStop";
  }
}

function winkelStop(e: unknown): WinkelStop | null {
  if (e instanceof TikTokApiError && WINKEL_STOP.includes(e.soort)) return new WinkelStop(e.soort, e);
  return null;
}

export type Ophaling = Samenstelling | { status: "bezig_met_ophalen"; reden: string; regels: []; waarschuwingen: []; ontbrekend: string[] };

export interface OphaalOpties {
  /** Zoveel verzoeken moeten over blijven vóór een nieuwe bestelling (12 bij boeken, 0 bij de proef). */
  reserve: number;
  /** "Opnieuw sinds T": alleen bestellingen opgehaald op of na T tellen. */
  sinds?: number;
}

/**
 * Haalt de transacties van een afrekening op, daarna elke ontbrekende bestelling één keer (bewaard per afrekening en
 * bestelling), en stelt samen. Gooit WinkelStop; BudgetOp wordt `bezig_met_ophalen` (niets verloren, volgende aanroep verder).
 */
export async function haalSamen(d: TikTokDeps, statementId: string, o: OphaalOpties): Promise<Ophaling> {
  const bezig = (reden: string, ontbrekend: string[] = []): Ophaling => ({ status: "bezig_met_ophalen", reden, regels: [], waarschuwingen: [], ontbrekend });
  // Bewaarde transacties (van een eerdere aanroep, na T en niet ouder dan een dag) besparen alle pagina's.
  const bewaard = await d.opslag.leesTransacties(statementId);
  let kop, transacties;
  let nieuw = false;
  if (bewaard && (o.sinds === undefined || bewaard.opgehaaldOp > o.sinds) && d.nu() - bewaard.opgehaaldOp < BEWAAR_TRANSACTIES) {
    ({ kop, transacties } = bewaard);
  } else {
    // "Vers": aan het begin van deze afrekening was (bijna) het hele budget er nog (marge voor de lijst met afrekeningen
    // en tokens verversen). Lukt het dan nog niet, dan lukt het nooit.
    const vers = d.budget.over >= d.budget.totaal - VERS_MARGE;
    try {
      ({ kop, transacties } = await transactiesVanAfrekening(d.tiktok, d.accessToken, d.shopCipher, statementId));
    } catch (e) {
      // Met een vol budget lukt het nooit: dan onvolledig, zodat de grens van 5 runs of 24 uur geldt (geen eindeloze stilstand).
      if (isBudgetOp(e)) return vers ? { status: "onvolledig", reden: "afrekening te groot voor één aanroep (te veel transactiepagina's)", regels: [], waarschuwingen: [], ontbrekend: [] } : bezig("budget op bij de transacties van de afrekening");
      const stop = winkelStop(e);
      if (stop) throw stop;
      if (e instanceof TikTokApiError) return { status: "onvolledig", reden: `transacties niet opgehaald: TikTok fout ${e.code}`, regels: [], waarschuwingen: [], ontbrekend: [] };
      return { status: "fout_gegevens", reden: `transacties niet te lezen: ${(e as Error).message}`, regels: [], waarschuwingen: [], ontbrekend: [] };
    }
    nieuw = true;
  }

  const telt = (b: Awaited<ReturnType<Opslag["leesBestelling"]>>) => !!b && bruikbaar(b.antwoord, statementId) && (o.sinds === undefined || b.opgehaaldOp > o.sinds);
  const bestellingen = new Map();
  for (const id of bestellingenVan(transacties)) {
    const b = await d.opslag.leesBestelling(statementId, id);
    if (telt(b)) bestellingen.set(id, b!.antwoord);
  }
  // Eerst de controles die geen bestelling nodig hebben (munt, total_count, dubbele transactie): spaart budget.
  const voor = stelSamen(statementId, kop, transacties, bestellingen);
  // Bewaren pas na de controles: een lijst die "onvolledig" is zonder ontbrekende bestellingen (aantal, dubbele id,
  // kop zonder munt) wordt niet bewaard, zodat de volgende aanroep opnieuw ophaalt.
  if (nieuw && !(voor.status === "onvolledig" && !voor.ontbrekend.length)) await d.opslag.schrijfTransacties(statementId, { kop, transacties, opgehaaldOp: d.nu() });
  if (!(voor.status === "onvolledig" && voor.ontbrekend.length)) return klaar(voor);
  const ontbrekend = voor.ontbrekend;

  const mislukt: string[] = [];
  for (let i = 0; i < ontbrekend.length; i++) {
    const id = ontbrekend[i];
    // Eén bestelling kost tot MAX_POGINGEN verzoeken (herhalen bij 429 of 5xx); de reserve mag daar niet onder zakken.
    if (d.budget.over <= o.reserve + (o.reserve > 0 ? MAX_POGINGEN - 1 : 0)) return bezig(`budget op, nog ${ontbrekend.length - i} bestelling(en) op te halen`, ontbrekend.slice(i));
    let antwoord;
    try {
      antwoord = await transactiesVanBestelling(d.tiktok, d.accessToken, d.shopCipher, id);
    } catch (e) {
      if (isBudgetOp(e)) return bezig(`budget op, nog ${ontbrekend.length - i} bestelling(en) op te halen`, ontbrekend.slice(i));
      const stop = winkelStop(e);
      if (stop) throw stop;
      if (e instanceof TikTokApiError) {
        mislukt.push(`${id} (TikTok fout ${e.code})`);
        continue;
      }
      // Geen TikTok-fout maar onze eigen controle (bijv. ongeldig order_id): vast, niet opnieuw proberen.
      return { status: "fout_gegevens", reden: `bestelling ${id}: ${(e as Error).message}`, regels: [], waarschuwingen: [], ontbrekend: [] };
    }
    await d.opslag.schrijfBestelling(statementId, id, { antwoord, opgehaaldOp: d.nu() });
    if (bruikbaar(antwoord, statementId)) bestellingen.set(id, antwoord);
    else mislukt.push(`${id} (antwoord zonder regels van deze afrekening)`);
  }
  if (mislukt.length) return { status: "onvolledig", reden: `bestelling(en) niet opgehaald: ${mislukt.join(", ")}`, regels: [], waarschuwingen: [], ontbrekend: mislukt.map((m) => m.split(" ")[0]) };

  return klaar(stelSamen(statementId, kop, transacties, bestellingen));

  // Bij boeken (reserve > 0): compleet telt pas als er nog genoeg over is voor één boeking, anders volgende aanroep.
  function klaar(s: Samenstelling): Ophaling {
    if (o.reserve > 0 && s.status === "compleet" && d.budget.over < Math.max(o.reserve, RESERVE_BOEKING)) return bezig("compleet, maar te weinig budget over voor de boeking");
    return s;
  }
}

/** Bewaarde transacties gelden een dag; daarna (of na "opnieuw sinds T") opnieuw ophalen. */
const BEWAAR_TRANSACTIES = 24 * 3600;
/** Verzoeken die vóór een afrekening al op mogen zijn om hem nog als "vers" te zien (lijst met afrekeningen, tokens). */
const VERS_MARGE = 5;

export interface ProefAfrekening {
  statementId: string;
  statementTime: number;
  paymentStatus: string;
  /** "nog niet uitbetaald" bij PROCESSING. */
  label?: string;
  status: Ophaling["status"];
  reden?: string;
  perSoort: Partial<Record<MbSoort, number>>;
  uitbetaaldCenten?: number;
  waarschuwingen: string[];
}

export interface ProefUitkomst {
  /** true als het budget op was: het scherm toont "nog bezig", de volgende aanroep gaat verder. */
  nogBezig: boolean;
  afrekeningen: ProefAfrekening[];
}

const UITBETAALD = ["PAID", "SETTLED"];
const MAX_DOORZOEKEN = 50;

/**
 * Proef (eis a): de laatste 3 uitbetaalde afrekeningen als regels per soort. Geen rekeningen, geen startdatum, geen
 * abonnement en nooit Moneybird (die client krijgt de proef niet eens). Gooit WinkelStop.
 */
export async function proef(d: TikTokDeps): Promise<ProefUitkomst> {
  const betaald: Afrekening[] = [];
  const nogNiet: Afrekening[] = [];
  try {
    let gezien = 0;
    for await (const a of afrekeningen(d.tiktok, d.accessToken, d.shopCipher, { sortOrder: "DESC", pageSize: 20 })) {
      if (UITBETAALD.includes(String(a.payment_status))) betaald.push(a);
      else if (a.payment_status === "PROCESSING") nogNiet.push(a);
      if (betaald.length >= 3 || ++gezien >= MAX_DOORZOEKEN) break;
    }
  } catch (e) {
    if (isBudgetOp(e)) return { nogBezig: true, afrekeningen: [] };
    throw winkelStop(e) ?? e;
  }
  const lijst = [...betaald, ...nogNiet.slice(0, Math.max(0, 3 - betaald.length))];

  const uit: ProefAfrekening[] = [];
  let nogBezig = false;
  for (const a of lijst) {
    const s = nogBezig ? null : await haalSamen(d, String(a.id), { reserve: 0 });
    if (!s || s.status === "bezig_met_ophalen") nogBezig = true;
    const perSoort: ProefAfrekening["perSoort"] = {};
    for (const r of s?.regels ?? []) perSoort[r.soort] = (perSoort[r.soort] ?? 0) + r.bedragCenten;
    uit.push({
      statementId: String(a.id),
      statementTime: Number(a.statement_time),
      paymentStatus: String(a.payment_status),
      ...(a.payment_status === "PROCESSING" ? { label: "nog niet uitbetaald" } : {}),
      status: s?.status ?? "bezig_met_ophalen",
      ...(s?.reden ? { reden: s.reden } : s ? {} : { reden: "budget op" }),
      perSoort,
      ...(s && "uitbetaaldCenten" in s && s.uitbetaaldCenten !== undefined ? { uitbetaaldCenten: s.uitbetaaldCenten } : {}),
      waarschuwingen: s?.waarschuwingen ?? [],
    });
  }
  return { nogBezig, afrekeningen: uit };
}

// ---------------------------------------------------------------------------------------------------------------
// Deel 2b: boeken. Een gewone run loopt de afrekeningen langs vanaf de markering (ontwerp, "Boeken" en de statustabel).

export interface BoekDeps extends TikTokDeps {
  moneybird: MoneybirdClient;
  /** Uniek per Worker-aanroep: eigenaar van de sloten. */
  eigenaar: string;
}

export interface Instellingen {
  /** Unix-seconden: afrekeningen daarvoor worden niet opgehaald en niet geboekt. */
  startdatum: number;
  /** Abonnement betaald (of binnen de gratis grens): mag schrijven naar Moneybird. */
  magBoeken: boolean;
  administratie: AdministratieInfo;
  koppeling: Koppeling;
  btwToegestaan?: boolean;
}

export interface WinkelFout {
  soort: string;
  bericht: string;
}

export interface RunUitkomst {
  /** Gezet als de hele winkel stilstaat (koppeling verlopen, geen abonnement, ...). De aanroeper bewaart en toont hem. */
  winkel?: WinkelFout;
  /** true als het budget op was: de volgende aanroep gaat verder. */
  budgetOp: boolean;
  verwerkt: Array<{ statementId: string; status: string }>;
}

const GEBOEKT = ["geboekt", "geboekt_met_waarschuwing", "leeg", "leeg_maar_geboekt"];
const AF = [...GEBOEKT, "fout", "fout_gegevens"];
/** Eigen lijst: elke run nakijken, houdt de markering niet vast. wacht_op_abonnement staat erop, zodat betalen meteen boekt. */
const OPEN = ["wacht_op_uitbetaling", "uitbetaling_mislukt", "onbekende_uitbetaalstatus", "onzeker", "wacht_op_abonnement"];
const SLOT_DUUR = 300;
const SLOT_MARGE = 60;
const ONZEKER_WACHT = 600;
const MAX_POGINGEN_RUNS = 5;
const MAX_POGINGEN_DUUR = 24 * 3600;
/** Hoort bij de vingerafdruk: ophogen als de manier van boeken verandert. */
export const CODE_VERSIE = "1";
// `invoer` en `btw_nog_niet_getest` komen uit de instellingen (bijv. geen rekening gekozen): winkel stil tot het klopt,
// dan boekt alles vanzelf, in plaats van elke afrekening apart `fout`.
const MB_WINKEL_STOP = ["koppeling_verlopen", "geen_abonnement", "geblokkeerd", "te_veel_verzoeken", "server", "niet_gevonden", "invoer", "btw_nog_niet_getest"];
/** Alles wat niet af is komt elke run terug, ook als het vóór de markering ligt (bijv. eerst FAILED, later onvolledig). */
const NIET_AF = [...OPEN, "bezig_met_ophalen", "onvolledig"];

export async function vingerafdruk(invoer: AfrekeningInvoer, koppeling: Koppeling, administratieId: string): Promise<string> {
  const regels = [...invoer.regels].map((r) => [r.soort, r.bedragCenten]).sort((a, b) => String(a[0]).localeCompare(String(b[0])) || Number(a[1]) - Number(b[1]));
  const per = Object.keys(koppeling.per).sort().map((k) => [k, koppeling.per[k as MbSoort]?.grootboekId ?? "", koppeling.per[k as MbSoort]?.btwTariefId ?? ""]);
  const tekst = JSON.stringify([CODE_VERSIE, administratieId, invoer.statementTime, invoer.uitbetaaldCenten ?? null, regels, per, koppeling.tegenrekeningId]);
  const h = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(tekst));
  return [...new Uint8Array(h)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

/** Knoppen "opnieuw boeken" en "opnieuw proberen": markering op de afrekening; de volgende run haalt opnieuw op. */
export async function opnieuw(d: Pick<TikTokDeps, "opslag" | "nu">, statementId: string): Promise<void> {
  // Met slot, zodat een lopende run de knopdruk niet overschrijft.
  const eigenaar = `knop-${statementId}-${d.nu()}`;
  if (!(await d.opslag.neemSlot(statementId, eigenaar, d.nu() + 30, d.nu()))) throw new Error("deze afrekening wordt nu verwerkt; probeer het zo opnieuw");
  try {
    const st = await d.opslag.leesStatus(statementId);
    if (!st) throw new Error(`afrekening ${statementId} is nog niet verwerkt`);
    if (st.status === "onzeker") throw new Error("de boeking wordt nog gecontroleerd; de app kijkt binnen 10 minuten zelf opnieuw");
    const { opnieuwFout: _weg, ...rest } = st;
    await d.opslag.schrijfStatus(statementId, { ...rest, opnieuwSinds: d.nu(), pogingen: 0, eerstePoging: undefined });
  } finally {
    await d.opslag.geefSlotTerug(statementId, eigenaar);
  }
}

/**
 * Startdatum vervroegd (uit `voor_startdatum` komen): de aanroeper roept dit aan bij het opslaan van de instelling,
 * zodat de markering teruggaat en de eerdere afrekeningen alsnog worden opgehaald.
 */
export async function vervroegStartdatum(opslag: Opslag, nieuweStart: number): Promise<void> {
  const m = await opslag.leesMarkering();
  if (m === undefined || nieuweStart < m) await opslag.schrijfMarkering(nieuweStart);
}

export async function verwerkWinkel(d: BoekDeps, inst: Instellingen): Promise<RunUitkomst> {
  const uit: RunUitkomst = { budgetOp: false, verwerkt: [] };
  const markering = Math.max((await d.opslag.leesMarkering()) ?? inst.startdatum, inst.startdatum);
  const open = (await d.opslag.leesOpen(NIET_AF)).filter((o) => o.statementTime >= inst.startdatum);
  const vanaf = Math.min(markering, ...open.map((o) => o.statementTime));
  const openIds = new Set(open.map((o) => o.statementId));

  // Eerste afrekening die de markering vasthoudt (nieuw, bezig of onvolledig); undefined = alles tot nu af.
  let houdVast: number | undefined;
  let laatste: number | undefined;
  let bezigMet: number | undefined;
  const lijst = afrekeningen(d.tiktok, d.accessToken, d.shopCipher, { vanaf, sortOrder: "ASC" });
  try {
    for await (const a of lijst) {
      const id = String(a.id);
      const tijd = Number(a.statement_time);
      if (tijd < markering && !openIds.has(id)) { laatste = tijd; continue; } // af en voor de markering: geen verzoek
      bezigMet = tijd;
      const r = await verwerkAfrekening(d, inst, a);
      bezigMet = undefined;
      laatste = tijd;
      if (r.stop) {
        houdVast ??= tijd;
        if (r.winkel) uit.winkel = r.winkel;
        if (r.budgetOp) uit.budgetOp = true;
        break;
      }
      if (r.status) uit.verwerkt.push({ statementId: id, status: r.status });
      if (r.status && !AF.includes(r.status) && !OPEN.includes(r.status)) houdVast ??= tijd;
      if (!r.status) houdVast ??= tijd; // slot bezet: later opnieuw
    }
  } catch (e) {
    if (isBudgetOp(e)) uit.budgetOp = true;
    else {
      const stop = winkelStop(e);
      if (!stop) throw e;
      uit.winkel = { soort: stop.soort, bericht: stop.message };
    }
    // Een fout midden in een afrekening houdt die afrekening vast; tussen twee afrekeningen de volgende.
    houdVast ??= bezigMet ?? (laatste === undefined ? markering : laatste + 1);
  }
  const nieuw = houdVast ?? (laatste === undefined ? markering : laatste + 1);
  // Nooit terug: wat vóór de markering niet af is, staat via NIET_AF toch op de lijst.
  if (nieuw !== (await d.opslag.leesMarkering())) await d.opslag.schrijfMarkering(Math.max(nieuw, markering));
  return uit;
}

interface AfrekeningUitkomst {
  /** Nieuwe status, of undefined als er niets gedaan is (slot bezet, of niets te doen). */
  status?: string;
  stop?: boolean;
  budgetOp?: boolean;
  winkel?: WinkelFout;
}

async function verwerkAfrekening(d: BoekDeps, inst: Instellingen, a: Afrekening): Promise<AfrekeningUitkomst> {
  const id = String(a.id);
  const tijd = Number(a.statement_time);
  const oud = await d.opslag.leesStatus(id);
  const herstel = oud?.opnieuwSinds !== undefined;
  // Af en geen knop gedrukt: geen enkel verzoek, ook niet na een gewijzigde koppeling (eis h).
  if (oud && AF.includes(oud.status) && !herstel) return { status: oud.status };
  // Ook na een knopdruk: Moneybird cachet GET, dus binnen 10 minuten kan een aangekomen POST nog onvindbaar zijn.
  if (oud?.status === "onzeker" && d.nu() - oud.sinds < ONZEKER_WACHT) return { status: "onzeker" };

  if (!(await d.opslag.neemSlot(id, d.eigenaar, d.nu() + SLOT_DUUR, d.nu()))) return {}; // bezet: niets doen, niets schrijven
  try {
    const basis = { ...(oud ?? {}), statementTime: tijd } as AfrekeningStatus;
    const zet = async (status: string, extra: Partial<AfrekeningStatus> = {}): Promise<AfrekeningUitkomst> => {
      const { opnieuwFout: _a, reden: _r, ...rest } = basis;
      await d.opslag.schrijfStatus(id, { ...rest, status, sinds: d.nu(), ...extra });
      return { status };
    };
    // Bij "opnieuw" blijft een geboekte status staan tot het nieuwe resultaat er is; een fout komt erbij.
    const faal = async (status: string, reden: string): Promise<AfrekeningUitkomst> => {
      if (herstel && oud && GEBOEKT.includes(oud.status)) {
        const { opnieuwSinds: _o, pogingen: _p, eerstePoging: _e, ...rest } = basis;
        await d.opslag.schrijfStatus(id, { ...rest, opnieuwFout: `${status}: ${reden}` });
        return { status: oud.status };
      }
      const { opnieuwSinds: _o, ...rest } = basis;
      await d.opslag.schrijfStatus(id, { ...rest, status, reden, sinds: d.nu(), pogingen: 0, eerstePoging: undefined });
      return { status };
    };

    if (!herstel || !oud || !GEBOEKT.includes(oud.status)) {
      const ps = String(a.payment_status);
      if (ps === "PROCESSING") return zet("wacht_op_uitbetaling");
      if (ps === "FAILED") return zet("uitbetaling_mislukt");
      if (!UITBETAALD.includes(ps)) return zet("onbekende_uitbetaalstatus", { reden: `onbekende uitbetaalstatus ${ps}` });
    }

    let s: Ophaling;
    try {
      s = await haalSamen(d, id, { reserve: RESERVE_BOEKING, ...(herstel ? { sinds: oud!.opnieuwSinds } : {}) });
    } catch (e) {
      if (e instanceof WinkelStop) return { stop: true, winkel: { soort: e.soort, bericht: e.message } };
      throw e;
    }
    if (s.status === "bezig_met_ophalen") {
      if (!(herstel && oud && GEBOEKT.includes(oud.status))) await zet("bezig_met_ophalen", { reden: s.reden });
      return { stop: true, budgetOp: true };
    }
    if (s.status === "fout_gegevens") return faal("fout_gegevens", s.reden ?? "");
    if (s.status === "onvolledig") {
      const pogingen = (oud?.pogingen ?? 0) + 1;
      const eerste = oud?.eerstePoging ?? d.nu();
      if (pogingen >= MAX_POGINGEN_RUNS || d.nu() - eerste >= MAX_POGINGEN_DUUR) return faal("fout", `${s.reden} (na ${pogingen} pogingen)`);
      if (herstel && oud && GEBOEKT.includes(oud.status)) {
        await d.opslag.schrijfStatus(id, { ...basis, pogingen, eerstePoging: eerste, opnieuwFout: `onvolledig: ${s.reden}` });
        return { status: oud.status };
      }
      await d.opslag.schrijfStatus(id, { ...basis, status: "onvolledig", reden: s.reden, sinds: d.nu(), pogingen, eerstePoging: eerste });
      return { status: "onvolledig" };
    }

    // Compleet.
    if (!inst.magBoeken) return zet("wacht_op_abonnement");
    const invoer: AfrekeningInvoer = { statementId: id, statementTime: tijd, valuta: "EUR", regels: s.regels, ...(s.uitbetaaldCenten !== undefined ? { uitbetaaldCenten: s.uitbetaaldCenten } : {}) };
    const afdruk = await vingerafdruk(invoer, inst.koppeling, inst.administratie.id);
    if (herstel && oud?.documentId && oud.vingerafdruk === afdruk && GEBOEKT.includes(oud.status)) return zet(oud.status, { uitkomst: "ongewijzigd", opnieuwSinds: undefined, pogingen: 0, eerstePoging: undefined });
    const tot = await d.opslag.slotTot(id, d.eigenaar);
    if (tot === null || tot - d.nu() < SLOT_MARGE) return { stop: true }; // vangnet: niet schrijven zonder geldig slot

    let b;
    try {
      b = await boekAfrekening(d.moneybird, inst.administratie, invoer, inst.koppeling, { ...(oud?.documentId ? { bekendId: oud.documentId } : {}), btwToegestaan: inst.btwToegestaan });
    } catch (e) {
      if (isBudgetOp(e)) return { stop: true, budgetOp: true }; // niets verstuurd: niets schrijven, geen onzeker
      if (e instanceof MoneybirdFout) {
        if (MB_WINKEL_STOP.includes(e.soort)) return { stop: true, winkel: { soort: e.soort, bericht: e.message } };
        return faal("fout", `${e.soort}: ${e.message}`);
      }
      throw e;
    }
    const w = [...s.waarschuwingen, ...b.waarschuwingen];
    const extra = { uitkomst: b.uitkomst, ...(b.id ? { documentId: b.id } : {}), vingerafdruk: afdruk, waarschuwingen: w, opnieuwSinds: undefined, pogingen: 0, eerstePoging: undefined };
    if (b.uitkomst === "onzeker") return zet("onzeker", { ...extra, vingerafdruk: undefined, reden: b.fout?.message });
    if (b.uitkomst === "leeg" || b.uitkomst === "leeg_maar_geboekt") return zet(b.uitkomst, extra);
    return zet(w.length ? "geboekt_met_waarschuwing" : "geboekt", extra);
  } finally {
    await d.opslag.geefSlotTerug(id, d.eigenaar);
  }
}
