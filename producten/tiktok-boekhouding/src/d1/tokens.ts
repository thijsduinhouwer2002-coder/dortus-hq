// Tokens van TikTok en Moneybird in D1 (ontwerp-d1-worker.md, punt 5 en punt 7: kolommen tt_tokens, mb_tokens, tt_versie, mb_versie).
// Versleuteld met AES-GCM (WebCrypto): nieuwe IV van 12 bytes per keer, winkel-id als AAD, sleutelversie vooraan in de tekst.
// Verversen als het access token binnen een uur verloopt; opslaan voorwaardelijk op de versie; na een 401 één keer verversen.
import { ververs as ttVervers, verlooptBinnen, type AppGegevens, type Tokens } from "../../../tiktok-shop-basis/src/auth.ts";
import { ververs as mbVervers, type MoneybirdTokens, type OAuthApp } from "../moneybird/oauth.ts";
import { isBudgetOp, type Budget } from "../budget.ts";
import { Ontkoppeld } from "../opslag.ts";
import { WinkelStop } from "../ophalen.ts";
import type { D1 } from "./opslag.ts";

/** Verversen als het access token binnen zoveel seconden verloopt. */
export const VERVERS_MARGE = 3600;
/** Waarschuwen als het refresh token van TikTok binnen zoveel seconden verloopt. */
export const WAARSCHUW_MARGE = 14 * 24 * 3600;

// ---- versleutelen ----

/** Sleutels per versie. In productie komen de ruwe 32 bytes uit een Worker-secret. `huidig` is de versie om mee te versleutelen. */
export interface Sleutelbos {
  huidig: string;
  sleutels: Record<string, CryptoKey | Uint8Array>;
}

const geimporteerd = new WeakMap<Uint8Array, Promise<CryptoKey>>();

function sleutel(bos: Sleutelbos, versie: string): Promise<CryptoKey> {
  if (!Object.hasOwn(bos.sleutels, versie)) throw new Error(`onbekende sleutelversie ${versie}`);
  const k = bos.sleutels[versie];
  if (!(k instanceof Uint8Array)) return Promise.resolve(k);
  if (k.length !== 32) throw new Error(`sleutel ${versie} is geen 32 bytes`);
  let p = geimporteerd.get(k);
  if (!p) {
    p = crypto.subtle.importKey("raw", k, { name: "AES-GCM" }, false, ["encrypt", "decrypt"]);
    geimporteerd.set(k, p);
  }
  return p;
}

const naarB64 = (b: Uint8Array) => btoa(Array.from(b, (x) => String.fromCharCode(x)).join(""));
const vanB64 = (s: string) => Uint8Array.from(atob(s), (c) => c.charCodeAt(0));
const VERSIE = /^[A-Za-z0-9_-]+$/;

/** Geeft `<versie>.<iv b64>.<data b64>`. De winkel-id gaat mee als AAD: dezelfde tekst bij een andere winkel ontsleutelt niet. */
export async function versleutel(bos: Sleutelbos, winkel: string, tekst: string): Promise<string> {
  if (!VERSIE.test(bos.huidig)) throw new Error("sleutelversie mag alleen letters, cijfers, _ en - bevatten");
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const data = await crypto.subtle.encrypt(
    { name: "AES-GCM", iv, additionalData: new TextEncoder().encode(winkel) },
    await sleutel(bos, bos.huidig),
    new TextEncoder().encode(tekst),
  );
  return `${bos.huidig}.${naarB64(iv)}.${naarB64(new Uint8Array(data))}`;
}

/** Faalt bij onbekende versie, verkeerde winkel (AAD) of aangepaste tekst. */
export async function ontsleutel(bos: Sleutelbos, winkel: string, opgeslagen: string): Promise<string> {
  const delen = opgeslagen.split(".");
  if (delen.length !== 3) throw new Error("versleutelde tokens hebben een onbekende vorm");
  const [versie, iv, data] = delen;
  const uit = await crypto.subtle.decrypt(
    { name: "AES-GCM", iv: vanB64(iv), additionalData: new TextEncoder().encode(winkel) },
    await sleutel(bos, versie),
    vanB64(data),
  );
  return new TextDecoder().decode(uit);
}

// ---- soorten ----

/** Wat per soort verschilt: kolommen, verversen en verloopmomenten (Unix-seconden). */
export interface TokenSoort<T> {
  kolom: "tt" | "mb";
  ververs(refreshToken: string, fetchFn: typeof fetch): Promise<T>;
  refreshToken(t: T): string;
  /** Verloopmoment van het access token; undefined is "verloopt niet". */
  accessVerlooptOp(t: T): number | undefined;
  /** Alleen TikTok: refresh token verloopt, dan waarschuwen. */
  refreshVerlooptOp?(t: T): number | undefined;
}

export function tiktokSoort(app: AppGegevens): TokenSoort<Tokens> {
  return {
    kolom: "tt",
    ververs: (r, f) => ttVervers(app, r, f),
    refreshToken: (t) => t.refreshToken,
    accessVerlooptOp: (t) => t.accessTokenVerlooptOp,
    refreshVerlooptOp: (t) => t.refreshTokenVerlooptOp,
  };
}

export function moneybirdSoort(app: OAuthApp): TokenSoort<MoneybirdTokens> {
  return {
    kolom: "mb",
    ververs: (r, f) => mbVervers(app, r, f),
    refreshToken: (t) => t.refreshToken,
    accessVerlooptOp: (t) => t.verlooptOp,
  };
}

/** Herkent een 401 van TikTok (token verlopen) of Moneybird (koppeling verlopen). */
export function is401(e: unknown): boolean {
  const x = e as { httpStatus?: unknown; soort?: unknown };
  return x?.httpStatus === 401 || x?.soort === "koppeling_verlopen" || x?.soort === "token_verlopen";
}

/** Netwerk, 5xx, 429 of budget op: niet de koppeling, maar later opnieuw. */
function tijdelijk(e: unknown): boolean {
  if (isBudgetOp(e)) return true;
  const s = Number((e as { httpStatus?: unknown })?.httpStatus);
  if (s === 429 || s >= 500) return true;
  return /\((5\d\d|429)\)/.test(String((e as Error)?.message));
}

export interface TokenUitkomst<T> {
  tokens: T;
  /** Gezet als het refresh token van TikTok binnen 14 dagen verloopt: de verkoper moet opnieuw koppelen. */
  waarschuwing?: "refresh_token_verloopt";
}

export interface TokenDeps<T> {
  db: D1;
  winkel: string;
  soort: TokenSoort<T>;
  sleutels: Sleutelbos;
  /** Het ene budget van de aanroep: D1 via `opslagTeller`, verversen via `omhul`. */
  budget: Budget;
  fetchFn?: typeof fetch;
  /** Unix-seconden. */
  nu?: () => number;
  /** Wachttijd vóór de tweede blik in D1 als het refresh token geweigerd werd (een andere aanroep kan net aan het opslaan zijn). */
  wachtMs?: number;
}

/** Tokens van één soort voor één winkel, binnen één aanroep. */
export class TokenBron<T> {
  private huidig: { tokens: T; versie: number } | undefined;
  private readonly d: TokenDeps<T>;
  private readonly teller: { neem(): void; neemAfmaken(): void };
  private readonly kolom: string;
  private readonly versieKolom: string;

  constructor(d: TokenDeps<T>) {
    this.d = d;
    this.teller = d.budget.opslagTeller();
    // Alleen deze twee waarden, dus veilig in de SQL.
    this.kolom = d.soort.kolom === "tt" ? "tt_tokens" : "mb_tokens";
    this.versieKolom = d.soort.kolom === "tt" ? "tt_versie" : "mb_versie";
  }

  private nu(): number {
    return this.d.nu ? this.d.nu() : Math.floor(Date.now() / 1000);
  }

  /** Vers uit D1 lezen en ontsleutelen. Ontkoppeld of geen rij: `Ontkoppeld`; geen tokens: `koppeling_verlopen`. */
  async lees(): Promise<{ tokens: T; versie: number }> {
    this.teller.neem();
    const rij = await this.d.db
      .prepare(`SELECT ${this.kolom} AS t, ${this.versieKolom} AS v FROM winkels WHERE id = ? AND ontkoppeld_op IS NULL`)
      .bind(this.d.winkel)
      .first<{ t: string | null; v: number }>();
    if (!rij) throw new Ontkoppeld(`winkel ${this.d.winkel} bestaat niet in D1 of is ontkoppeld`);
    if (!rij.t) throw new WinkelStop("koppeling_verlopen", new Error(`geen ${this.kolom} voor winkel ${this.d.winkel}`));
    const tokens = JSON.parse(await ontsleutel(this.d.sleutels, this.d.winkel, rij.t)) as T;
    this.huidig = { tokens, versie: Number(rij.v) };
    return this.huidig;
  }

  /** Voorwaardelijk opslaan. Geeft false als een andere aanroep al opsloeg (versie veranderd) of de winkel ontkoppeld is. */
  async bewaar(tokens: T, versie: number): Promise<boolean> {
    const tekst = await versleutel(this.d.sleutels, this.d.winkel, JSON.stringify(tokens));
    this.teller.neemAfmaken();
    const r = await this.d.db
      .prepare(`UPDATE winkels SET ${this.kolom} = ?, ${this.versieKolom} = ${this.versieKolom} + 1 WHERE id = ? AND ${this.versieKolom} = ? AND ontkoppeld_op IS NULL`)
      .bind(tekst, this.d.winkel, versie)
      .run();
    if (r.meta.changes !== 1) return false;
    this.huidig = { tokens, versie: versie + 1 };
    return true;
  }

  /** Tokens om te gebruiken; ververst als het access token binnen een uur verloopt. */
  async geef(): Promise<TokenUitkomst<T>> {
    const h = this.huidig ?? (await this.lees());
    const op = this.d.soort.accessVerlooptOp(h.tokens);
    const t = op !== undefined && verlooptBinnen(op, VERVERS_MARGE, this.nu()) ? await this.verversVanaf(h) : h.tokens;
    return this.metWaarschuwing(t);
  }

  /** Voert `doe` uit met geldige tokens; bij een 401 één keer verversen en opnieuw, daarna winkelfout `koppeling_verlopen`. */
  async met<R>(doe: (tokens: T) => Promise<R>): Promise<R> {
    const { tokens } = await this.geef();
    try {
      return await doe(tokens);
    } catch (e) {
      if (!is401(e)) throw e;
    }
    const nieuw = await this.verversVanaf(this.huidig!);
    try {
      return await doe(nieuw);
    } catch (e) {
      if (is401(e)) throw new WinkelStop("koppeling_verlopen", e as Error);
      throw e;
    }
  }

  private metWaarschuwing(tokens: T): TokenUitkomst<T> {
    const op = this.d.soort.refreshVerlooptOp?.(tokens);
    return op !== undefined && verlooptBinnen(op, WAARSCHUW_MARGE, this.nu()) ? { tokens, waarschuwing: "refresh_token_verloopt" } : { tokens };
  }

  /** Verversen vanaf de gelezen versie. Heeft een andere aanroep intussen ververst, dan diens tokens (geen fout). */
  private async verversVanaf(oud: { tokens: T; versie: number }): Promise<T> {
    const fetchFn = this.d.budget.omhul(this.d.fetchFn ?? fetch);
    let nieuw: T;
    try {
      nieuw = await this.d.soort.ververs(this.d.soort.refreshToken(oud.tokens), fetchFn);
    } catch (e) {
      if (tijdelijk(e)) throw e;
      // Refresh token geweigerd: misschien heeft een andere aanroep het al gebruikt. Dan staat er een nieuwere versie in D1.
      for (let i = 0; i < 2; i++) {
        if (i) await new Promise((r) => setTimeout(r, this.d.wachtMs ?? 1500));
        const vers = await this.lees();
        if (vers.versie !== oud.versie) return vers.tokens;
      }
      throw new WinkelStop("koppeling_verlopen", e as Error);
    }
    if (await this.bewaar(nieuw, oud.versie)) return nieuw;
    // changes = 0: een andere aanroep was eerder, of de winkel is ontkoppeld (dan gooit lees `Ontkoppeld`).
    return (await this.lees()).tokens;
  }
}
