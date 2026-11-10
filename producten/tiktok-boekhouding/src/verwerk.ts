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
import { beginVanMaand, GRATIS_PER_MAAND, maandVan, somVanMaand, vorigeMaand } from "./telling.ts";

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
  /**
   * Abonnement actief (ontwerp-betalen.md, punt 2: `actief` en `tot` > nu): geen gratis grens. Zonder boekt een afrekening
   * alleen als de maand (zonder deze afrekening) plus haar bestellingen hoogstens 30 is, en alleen in de lopende of vorige
   * maand; anders `wacht_op_abonnement` of `wacht_ouder`. De Worker zet dit uit `winkels.abonnement`, nooit uit de
   * opgeslagen instellingen.
   */
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
/** Ouder dan de vorige maand en geen abonnement (ontwerp-betalen.md, punt 2 stap 1 en 4b): telt als af, alleen de knop haalt hem terug. */
export const WACHT_OUDER = "wacht_ouder";
const AF = [...GEBOEKT, "fout", "fout_gegevens", WACHT_OUDER];
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
  let open = (await d.opslag.leesOpen(NIET_AF)).filter((o) => o.statementTime >= inst.startdatum);
  // Maandwissel (stap 4b): alleen zonder abonnement en alleen als er iets openstaat van vóór de vorige maand (kost dan één
  // batch). Wat `wacht_ouder` wordt, gaat uit de lijst van deze run.
  if (!inst.magBoeken) {
    const grens = beginVanMaand(vorigeMaand(d.nu()));
    if (open.some((o) => o.statementTime < grens)) {
      const weg = new Set(await d.opslag.maandwissel(grens));
      if (weg.size) open = open.filter((o) => !weg.has(o.statementId));
    }
  }
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
    // Stap 4 (ontwerp-betalen.md, punt 2): gezet zodra deze poging de telling invoegde en de status van daarvoor niet
    // geboekt was. Dan gaat de rij weg bij `faal` (een weigering uit boekAfrekening: niets aangemaakt) en bij `terug()`,
    // in dezelfde schrijfactie als de status.
    let wisRij = false;
    // Bij "opnieuw" blijft een geboekte status staan tot het nieuwe resultaat er is; een fout komt erbij.
    const faal = async (status: string, reden: string): Promise<AfrekeningUitkomst> => {
      if (herstel && oud && GEBOEKT.includes(oud.status)) {
        const { opnieuwSinds: _o, pogingen: _p, eerstePoging: _e, ...rest } = basis;
        await d.opslag.schrijfStatus(id, { ...rest, opnieuwFout: `${status}: ${reden}` });
        return { status: oud.status };
      }
      const { opnieuwSinds: _o, ...rest } = basis;
      await d.opslag.schrijfStatus(id, { ...rest, status, reden, sinds: d.nu(), pogingen: 0, eerstePoging: undefined }, wisRij);
      return { status };
    };

    if (!herstel || !oud || !GEBOEKT.includes(oud.status)) {
      const ps = String(a.payment_status);
      if (ps === "PROCESSING") return zet("wacht_op_uitbetaling");
      if (ps === "FAILED") return zet("uitbetaling_mislukt");
      if (!UITBETAALD.includes(ps)) return zet("onbekende_uitbetaalstatus", { reden: `onbekende uitbetaalstatus ${ps}` });
    }

    // Stap 0 (ontwerp-betalen.md, punt 2): vrijgesteld van de grens is een afrekening die al geboekt, onzeker of "boeking
    // gestart" was, of al een rij in de telling heeft: zoeken op kenmerk en herstellen mogen nooit stilvallen.
    const tellingen = inst.magBoeken ? undefined : await d.opslag.leesTelling();
    // `vrijSql`: alleen abonnement of status gaat als vrijstelling naar de SQL van stap 3; een bestaande rij vangt
    // INSERT OR IGNORE daar zelf op, zodat een achterlopende cache nooit zonder grens laat invoegen.
    const vrijSql = inst.magBoeken || (oud !== undefined && (GEBOEKT.includes(oud.status) || oud.status === "onzeker")) || gelezen?.reden === BOEKING_GESTART;
    const vrij = vrijSql || tellingen!.has(id);
    const maand = maandVan(tijd);
    const som = tellingen ? somVanMaand(tellingen, maand, id) : 0;
    if (!vrij) {
      // Stap 1, vóór het ophalen (geen verzoek naar TikTok). Ouder dan de vorige maand: `wacht_ouder`, ook na de knop:
      // gratis ruimte geldt alleen voor de lopende en vorige maand (toets g). Met abonnement is `vrij` al waar.
      if (maand < vorigeMaand(d.nu())) return zet(WACHT_OUDER, { opnieuwSinds: undefined, pogingen: 0, eerstePoging: undefined });
      // Maand al vol: wachten zonder verzoek, alleen als Get Statements omzet boven 0 geeft. Anders misschien zonder
      // bestellingen, en die mag altijd: stap 2 telt het precies.
      if (som >= GRATIS_PER_MAAND && metOmzet(a)) return zet("wacht_op_abonnement", { opnieuwSinds: undefined });
    }

    let s: Ophaling;
    try {
      // Stap 2: na de transacties, vóór de losse bestellingen. Past de afrekening niet meer in de maand, dan niet ophalen.
      const wacht = vrij ? undefined : (n: number) => n > 0 && som + n > GRATIS_PER_MAAND;
      s = await haalSamen(d, id, { reserve: RESERVE_BOEKING + 2, ...(herstel ? { sinds: oud!.opnieuwSinds } : {}), ...(wacht ? { wachtBij: wacht } : {}) });
    } catch (e) {
      if (e instanceof WinkelStop) return { stop: true, winkel: { soort: e.soort, bericht: e.message } };
      throw e;
    }
    if (s.status === "bezig_met_ophalen") {
      if (!(herstel && oud && GEBOEKT.includes(oud.status))) await zet("bezig_met_ophalen", { reden: s.reden });
      return { stop: true, budgetOp: true };
    }
    if (s.status === "wacht_grens") return zet("wacht_op_abonnement", { opnieuwSinds: undefined });
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
    const invoer: AfrekeningInvoer = { statementId: id, statementTime: tijd, valuta: "EUR", regels: s.regels, ...(s.uitbetaaldCenten !== undefined ? { uitbetaaldCenten: s.uitbetaaldCenten } : {}) };
    const afdruk = await vingerafdruk(invoer, inst.koppeling, inst.administratie.id);
    if (herstel && oud?.documentId && oud.vingerafdruk === afdruk && GEBOEKT.includes(oud.status)) return zet(oud.status, { uitkomst: "ongewijzigd", opnieuwSinds: undefined, pogingen: 0, eerstePoging: undefined });
    // "Boeking gestart" in dezelfde schrijfactie als de slotcontrole (ontwerp-d1-worker.md, punt 1). Stopt de aanroep
    // tussen de POST en de echte status, dan blijft hij onzeker: 10 minuten wachten, dan zoeken op kenmerk.
    const { opnieuwFout: _of, reden: _rd, vorigeStatus: _vs, ...kaal } = basis;
    const gestart: AfrekeningStatus = { ...kaal, status: "onzeker", reden: BOEKING_GESTART, sinds: d.nu(), ...(oud ? { vorigeStatus: oud.status } : {}) };
    // Stap 3 (ontwerp-betalen.md, punt 2): de telling vastleggen in één batch vóór die van startBoeking, met de grens in de
    // SQL. Vrijgesteld (stap 0): geen grens. Een rij van een eerdere poging telt in de SQL als vrijstelling (INSERT OR IGNORE).
    const telling = await d.opslag.legTellingVast(id, d.eigenaar, {
      maand, bestellingen: s.bestellingen ?? 0, vrij: vrijSql, grens: GRATIS_PER_MAAND, minTot: d.nu() + SLOT_MARGE,
    });
    if (!telling.slot) return { stop: true }; // slot verloren: niets schrijven (zelfde vangnet als bij startBoeking)
    if (!telling.rij) return zet("wacht_op_abonnement", { opnieuwSinds: undefined }); // grens bereikt: niets verstuurd, bestellingen staan bewaard
    // Stap 4: de rij gaat alleen weg als deze poging hem invoegde en de status van daarvoor niet geboekt was.
    wisRij = telling.ingevoegd && !(oud !== undefined && GEBOEKT.includes(oud.status));
    const tot = await d.opslag.startBoeking(id, d.eigenaar, gestart, d.nu() + SLOT_MARGE);
    if (tot === null || tot - d.nu() < SLOT_MARGE) {
      // Er is niets gestart. Alleen weg zolang het slot nog van ons is: anders kan een andere aanroep op deze rij boeken.
      if (wisRij) await d.opslag.wisTelling(id, d.eigenaar);
      return { stop: true }; // vangnet: niet schrijven zonder geldig slot
    }
    // Niets verstuurd (budget op, of Moneybird weigerde de hele winkel): de status van daarvoor terug, en de telling weg in
    // dezelfde schrijfactie als deze poging hem invoegde.
    const terug = async () => d.opslag.zetTerug(id, gelezen, wisRij);

    let b;
    try {
      b = await boekAfrekening(d.moneybird, inst.administratie, invoer, inst.koppeling, { ...(oud?.documentId ? { bekendId: oud.documentId } : {}), btwToegestaan: inst.btwToegestaan });
    } catch (e) {
      // boekAfrekening gooit alleen vóór de POST of bij een weigering: er is niets aangemaakt (een POST die misschien
      // aankwam geeft `onzeker` en gooit niet). Budget op en winkelstop: `terug()`; een weigering: `faal`; beide wissen
      // de telling mee (stap 4). Een onbekende fout gooit door met "boeking gestart": de rij blijft (te ruim is veilig).
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

/** Get Statements geeft omzet boven 0: dan zeker bestellingen. Ontbreekt het veld of is het 0, dan misschien niet. */
function metOmzet(a: Afrekening): boolean {
  const r = Number(a.revenue_amount);
  return Number.isFinite(r) && r > 0;
}
