// Getekende aanroepen naar de TikTok Shop API.
// Bronnen: https://partner.tiktokshop.com/docv2/page/common-parameters
//          https://partner.tiktokshop.com/docv2/page/common-errors

import { maakHandtekening } from "./sign.ts";
import { TikTokApiError, opnieuwProberen } from "./fouten.ts";

export const API_BASIS = "https://open-api.tiktokglobalshop.com";
export const MAX_POGINGEN = 3; // in totaal, dus 2 herhalingen

export interface ClientOpties {
  appKey: string;
  appSecret: string;
  basisUrl?: string;
  fetchFn?: typeof fetch;
  /** Huidige tijd in seconden; te vervangen in tests. */
  nu?: () => number;
  /** Wachten in milliseconden; te vervangen in tests. */
  slaap?: (ms: number) => Promise<void>;
}

export interface Aanroep {
  method: "GET" | "POST" | "PUT" | "DELETE";
  path: string;
  accessToken?: string;
  shopCipher?: string;
  query?: Record<string, string | number | undefined>;
  body?: unknown;
}

export interface Antwoord<T> {
  data: T;
  requestId: string;
}

function wachttijd(poging: number, retryAfter: string | null): number {
  if (retryAfter !== null) {
    const s = Number(retryAfter);
    if (Number.isFinite(s) && s >= 0) return Math.min(s, 60) * 1000;
  }
  return 1000 * 2 ** (poging - 1); // 1 s, 2 s
}

export class TikTokClient {
  private readonly o: Required<ClientOpties>;

  constructor(opties: ClientOpties) {
    this.o = {
      basisUrl: API_BASIS,
      fetchFn: (...a) => fetch(...a),
      nu: () => Math.floor(Date.now() / 1000),
      slaap: (ms) => new Promise((r) => setTimeout(r, ms)),
      ...opties,
    };
  }

  async roep<T>(a: Aanroep): Promise<Antwoord<T>> {
    let laatste: TikTokApiError | undefined;
    for (let poging = 1; poging <= MAX_POGINGEN; poging++) {
      const { fout, antwoord, retryAfter } = await this.eenPoging<T>(a);
      if (antwoord) return antwoord;
      laatste = fout!;
      if (!opnieuwProberen(laatste) || poging === MAX_POGINGEN) break;
      await this.o.slaap(wachttijd(poging, retryAfter));
    }
    throw laatste!;
  }

  private async eenPoging<T>(a: Aanroep): Promise<{ antwoord?: Antwoord<T>; fout?: TikTokApiError; retryAfter: string | null }> {
    // Ruwe waarden voor de handtekening; de url krijgt ze gecodeerd.
    const query: Record<string, string> = {};
    for (const [k, v] of Object.entries(a.query ?? {})) if (v !== undefined && v !== "") query[k] = String(v);
    if (a.shopCipher) query.shop_cipher = a.shopCipher;
    query.app_key = this.o.appKey;
    query.timestamp = String(this.o.nu());

    // De body wordt één keer tekst; precies die tekst wordt getekend en verstuurd.
    const body = a.body === undefined ? undefined : JSON.stringify(a.body);
    const contentType = "application/json";
    query.sign = await maakHandtekening({ path: a.path, query, body, contentType }, this.o.appSecret);

    const headers: Record<string, string> = { "content-type": contentType };
    if (a.accessToken) headers["x-tts-access-token"] = a.accessToken;
    const url = `${this.o.basisUrl}${a.path}?${new URLSearchParams(query).toString()}`;

    let res: Response;
    try {
      res = await this.o.fetchFn(url, { method: a.method, headers, body });
    } catch (e) {
      // Budget op (product-laag): er is niets verstuurd, dus geen netwerkfout en niet herhalen.
      if ((e as { budgetOp?: unknown })?.budgetOp === true) throw e;
      return { fout: new TikTokApiError(-1, `netwerkfout: ${(e as Error).message}`, "", 503), retryAfter: null };
    }
    const retryAfter = res.headers.get("retry-after");
    let json: any = null;
    try {
      json = await res.json();
    } catch {
      /* geen JSON, hieronder als fout behandeld */
    }
    if (res.ok && json && json.code === 0) {
      return { antwoord: { data: json.data as T, requestId: String(json.request_id ?? "") }, retryAfter };
    }
    const code = Number(json?.code ?? -1);
    const bericht = String(json?.message ?? `HTTP ${res.status} zonder JSON`);
    return { fout: new TikTokApiError(code, bericht, String(json?.request_id ?? ""), res.status), retryAfter };
  }
}
