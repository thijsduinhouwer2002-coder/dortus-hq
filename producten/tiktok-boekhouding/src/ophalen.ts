// Product-laag, deel 2a (ontwerp-productlaag.md): een afrekening ophalen binnen het budget, en de proef (eis a).
// Boeken (verwerkWinkel, statustabel, slot, Moneybird) staat in verwerk.ts.
import { MAX_POGINGEN, type TikTokClient } from "../../tiktok-shop-basis/src/client.ts";
import { afrekeningen, transactiesVanAfrekening, transactiesVanBestelling, type Afrekening } from "../../tiktok-shop-basis/src/endpoints.ts";
import { TikTokApiError, type FoutSoort } from "../../tiktok-shop-basis/src/fouten.ts";
import { isBudgetOp, RESERVE_BOEKING, type Budget } from "./budget.ts";
import type { MbSoort } from "./moneybird/memoriaal.ts";
import type { Opslag } from "./opslag.ts";
import { bestellingenVan, bruikbaar, stelSamen, type Samenstelling } from "./samenstel.ts";
import { slankeBestelling, slankeKop, slankeTransacties } from "./slank.ts";

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

export function winkelStop(e: unknown): WinkelStop | null {
  if (e instanceof TikTokApiError && WINKEL_STOP.includes(e.soort)) return new WinkelStop(e.soort, e);
  return null;
}

export type Ophaling =
  | Samenstelling
  | { status: "bezig_met_ophalen"; reden: string; regels: []; waarschuwingen: []; ontbrekend: string[] }
  /** `wachtBij` gaf true: de losse bestellingen zijn niet opgehaald (ontwerp-betalen.md, punt 2 stap 2). */
  | { status: "wacht_grens"; reden: string; regels: []; waarschuwingen: []; ontbrekend: string[] };

export interface OphaalOpties {
  /** Zoveel verzoeken moeten over blijven vóór een nieuwe bestelling (12 bij boeken, 0 bij de proef). */
  reserve: number;
  /** "Opnieuw sinds T": alleen bestellingen opgehaald op of na T tellen. */
  sinds?: number;
  /** Gratis grens (stap 2): met `n` bestellingen in de transacties; true = niet verder ophalen, `wacht_grens`. */
  wachtBij?: (n: number) => boolean;
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
    // en tokens verversen). Lukt het dan nog niet, dan lukt het nooit. Queries naar de opslag (D1) tellen hier niet:
    // die komen elke aanroep terug, dus een afrekening die daardoor niet past, past nooit.
    const vers = d.budget.overVoorNieuw + d.budget.opslag >= d.budget.totaal - d.budget.reserve - VERS_MARGE;
    try {
      ({ kop, transacties } = await transactiesVanAfrekening(d.tiktok, d.accessToken, d.shopCipher, statementId));
      // Meteen slank maken (punt 3): rekenen en bewaren zien dezelfde velden.
      kop = slankeKop(kop);
      transacties = slankeTransacties(transacties);
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
  if (o.wachtBij?.(bestellingenVan(transacties).length)) return { status: "wacht_grens", reden: "gratis grens van de maand bereikt", regels: [], waarschuwingen: [], ontbrekend };

  const mislukt: string[] = [];
  for (let i = 0; i < ontbrekend.length; i++) {
    const id = ontbrekend[i];
    // Eén bestelling kost tot MAX_POGINGEN verzoeken (herhalen bij 429 of 5xx); de reserve mag daar niet onder zakken.
    if (d.budget.overVoorNieuw <= o.reserve + (o.reserve > 0 ? MAX_POGINGEN - 1 : 0)) return bezig(`budget op, nog ${ontbrekend.length - i} bestelling(en) op te halen`, ontbrekend.slice(i));
    let antwoord;
    try {
      antwoord = slankeBestelling(await transactiesVanBestelling(d.tiktok, d.accessToken, d.shopCipher, id));
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
    if (o.reserve > 0 && s.status === "compleet" && d.budget.overVoorNieuw < Math.max(o.reserve, RESERVE_BOEKING)) return bezig("compleet, maar te weinig budget over voor de boeking");
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

export const UITBETAALD = ["PAID", "SETTLED"];
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
