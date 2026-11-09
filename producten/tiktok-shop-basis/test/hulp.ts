import { readFileSync } from "node:fs";
import { TikTokClient } from "../src/client.ts";

export function voorbeeld(naam: string): any {
  return JSON.parse(readFileSync(new URL(`./voorbeelden/${naam}.json`, import.meta.url), "utf8"));
}

export interface Verzoek {
  url: URL;
  method: string;
  headers: Record<string, string>;
  body?: string;
}

/** Nep-fetch: geeft de antwoorden in volgorde terug en onthoudt elk verzoek. */
export function nepFetch(antwoorden: Array<{ status?: number; json?: unknown; headers?: Record<string, string>; tekst?: string }>) {
  const verzoeken: Verzoek[] = [];
  let i = 0;
  const fn = (async (input: any, init: any = {}) => {
    verzoeken.push({ url: new URL(String(input)), method: init.method ?? "GET", headers: init.headers ?? {}, body: init.body });
    const a = antwoorden[Math.min(i++, antwoorden.length - 1)];
    const body = a.tekst ?? JSON.stringify(a.json);
    return new Response(body, { status: a.status ?? 200, headers: a.headers });
  }) as typeof fetch;
  return { fn, verzoeken };
}

export const APP = { appKey: "123abc", appSecret: "geheim-secret" };

export function nepClient(antwoorden: Parameters<typeof nepFetch>[0]) {
  const nep = nepFetch(antwoorden);
  const slapen: number[] = [];
  const client = new TikTokClient({
    ...APP,
    fetchFn: nep.fn,
    nu: () => 1625484268,
    slaap: async (ms) => {
      slapen.push(ms);
    },
  });
  return { client, verzoeken: nep.verzoeken, slapen };
}
