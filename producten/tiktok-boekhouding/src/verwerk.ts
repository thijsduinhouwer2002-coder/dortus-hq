// Product-laag, deel 2b (ontwerp-productlaag.md): boeken. Een gewone run loopt de afrekeningen langs vanaf de markering
// (ontwerp, "Boeken" en de statustabel). Ophalen en de proef staan in ophalen.ts.
import { afrekeningen, type Afrekening } from "../../tiktok-shop-basis/src/endpoints.ts";
import { isBudgetOp, RESERVE_BOEKING } from "./budget.ts";
import { isOntkoppeld, type AfrekeningStatus, type Opslag } from "./opslag.ts";
import type { MoneybirdClient } from "./moneybird/client.ts";
import { MoneybirdFout } from "./moneybird/fouten.ts";
import { boekAfrekening, type AdministratieInfo } from "./moneybird/boeken.ts";
import type { AfrekeningInvoer, Koppeling, MbSoort } from "./moneybird/memoriaal.ts";
import { haalSamen, UITBETAALD, WinkelStop, winkelStop, type Ophaling, type TikTokDeps } from "./ophalen.ts";

export { haalSamen, proef, WinkelStop, type OphaalOpties, type Ophaling, type ProefAfrekening, type ProefUitkomst, type TikTokDeps } from "./ophalen.ts";
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

export const GEBOEKT = ["geboekt", "geboekt_met_waarschuwing", "leeg", "leeg_maar_geboekt"];
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
// `instelling` en `btw_nog_niet_getest` komen uit de instellingen (bijv. geen rekening gekozen): winkel stil tot het klopt,
// dan boekt alles vanzelf, in plaats van elke afrekening apart `fout`.
const MB_WINKEL_STOP = ["koppeling_verlopen", "geen_abonnement", "geblokkeerd", "te_veel_verzoeken", "server", "niet_gevonden", "instelling", "btw_nog_niet_getest"];
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
    // Winkel ontkoppeld (ontwerp-d1-worker.md, punt 7): nette stop, niets meer schrijven, ook geen markering.
    if (isOntkoppeld(e)) return { ...uit, winkel: { soort: "ontkoppeld", bericht: "winkel is ontkoppeld; er wordt niets meer geboekt" } };
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
  try {
    if (nieuw !== (await d.opslag.leesMarkering())) await d.opslag.schrijfMarkering(Math.max(nieuw, markering));
  } catch (e) {
    // Ook hier (al ontkoppeld vóór de run, of niets per afrekening geschreven): nette stop, geen fout.
    if (isOntkoppeld(e)) return { ...uit, winkel: { soort: "ontkoppeld", bericht: "winkel is ontkoppeld; er wordt niets meer geboekt" } };
    throw e;
  }
  return uit;
}

export const BOEKING_GESTART = "boeking gestart";

/** Status "boeking gestart" van een afgebroken aanroep: verder als de status van daarvoor (zonder de tussenvelden). */
function naAfbraak(s: AfrekeningStatus | undefined): AfrekeningStatus | undefined {
  if (!s || s.status !== "onzeker" || s.reden !== BOEKING_GESTART) return s;
  const { vorigeStatus, reden: _r, ...rest } = s;
  return typeof vorigeStatus === "string" ? { ...rest, status: vorigeStatus } : { ...rest, status: "onzeker" };
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
  // Af en geen knop gedrukt: geen enkel verzoek, ook niet na een gewijzigde koppeling (eis h).
  // Ook na een knopdruk wacht onzeker 10 minuten: Moneybird cachet GET, dus een aangekomen POST kan nog onvindbaar zijn.
  const nietsTeDoen = (s: AfrekeningStatus | undefined): AfrekeningUitkomst | null => {
    if (s && AF.includes(s.status) && s.opnieuwSinds === undefined) return { status: s.status };
    if (s?.status === "onzeker" && d.nu() - s.sinds < ONZEKER_WACHT) return { status: "onzeker" };
    return null;
  };
  const vroeg = nietsTeDoen(await d.opslag.leesStatus(id)); // spaart een slot
  if (vroeg) return vroeg;

  if (!(await d.opslag.neemSlot(id, d.eigenaar, d.nu() + SLOT_DUUR, d.nu()))) return {}; // bezet: niets doen, niets schrijven
  try {
    // Opnieuw lezen ná het slot: een andere run of de knop kan intussen geschreven hebben (geen dubbele POST zonder bekendId).
    const gelezen = await d.opslag.leesStatus(id);
    const niets = nietsTeDoen(gelezen);
    if (niets) return niets;
    // Na een afbraak tijdens het boeken (status "boeking gestart", ouder dan 10 minuten): verder met de status van
    // daarvoor, zodat een mislukte "opnieuw boeken" weer geboekt met opnieuwFout wordt. boekAfrekening zoekt eerst op
    // kenmerk of bekendId, dus een POST die er toch staat wordt gevonden en niet herhaald.
    const oud = naAfbraak(gelezen);
    const herstel = oud?.opnieuwSinds !== undefined;
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
      s = await haalSamen(d, id, { reserve: RESERVE_BOEKING + 2, ...(herstel ? { sinds: oud!.opnieuwSinds } : {}) });
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
    // "Boeking gestart" in dezelfde schrijfactie als de slotcontrole (ontwerp-d1-worker.md, punt 1). Stopt de aanroep
    // tussen de POST en de echte status, dan blijft hij onzeker: 10 minuten wachten, dan zoeken op kenmerk.
    const { opnieuwFout: _of, reden: _rd, vorigeStatus: _vs, ...kaal } = basis;
    const gestart: AfrekeningStatus = { ...kaal, status: "onzeker", reden: BOEKING_GESTART, sinds: d.nu(), ...(oud ? { vorigeStatus: oud.status } : {}) };
    const tot = await d.opslag.startBoeking(id, d.eigenaar, gestart, d.nu() + SLOT_MARGE);
    if (tot === null || tot - d.nu() < SLOT_MARGE) return { stop: true }; // vangnet: niet schrijven zonder geldig slot
    // Niets verstuurd (budget op, of Moneybird weigerde de hele winkel): de status van daarvoor terug.
    const terug = async () => (gelezen ? d.opslag.schrijfStatus(id, gelezen) : d.opslag.wisStatus(id));

    let b;
    try {
      b = await boekAfrekening(d.moneybird, inst.administratie, invoer, inst.koppeling, { ...(oud?.documentId ? { bekendId: oud.documentId } : {}), btwToegestaan: inst.btwToegestaan });
    } catch (e) {
      if (isBudgetOp(e)) {
        await terug();
        return { stop: true, budgetOp: true }; // niets verstuurd: geen onzeker
      }
      if (e instanceof MoneybirdFout) {
        if (MB_WINKEL_STOP.includes(e.soort)) {
          await terug();
          return { stop: true, winkel: { soort: e.soort, bericht: e.message } };
        }
        // Gegevens van deze afrekening kloppen niet (bijv. tijd of bedrag): vast, alleen deze afrekening.
        if (e.soort === "invoer") return faal("fout_gegevens", e.message);
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
