import { readFileSync } from "node:fs";
import { MoneybirdClient } from "../src/moneybird/client.ts";

export function voorbeeld(naam: string): any {
  return JSON.parse(readFileSync(new URL(`./voorbeelden/${naam}.json`, import.meta.url), "utf8"));
}

export interface Verzoek { url: URL; method: string; headers: Record<string, string>; body?: string }
export type NepAntwoord = { status?: number; json?: unknown; headers?: Record<string, string>; fout?: Error };

export function nepFetch(antwoorden: NepAntwoord[]) {
  const verzoeken: Verzoek[] = [];
  let i = 0;
  const fn = (async (input: any, init: any = {}) => {
    verzoeken.push({ url: new URL(String(input)), method: init.method ?? "GET", headers: init.headers ?? {}, body: init.body });
    const a = antwoorden[Math.min(i++, antwoorden.length - 1)];
    if (a.fout) throw a.fout;
    const status = a.status ?? 200;
    return new Response(status === 204 ? null : JSON.stringify(a.json ?? null), { status, headers: a.headers });
  }) as typeof fetch;
  return { fn, verzoeken };
}

export function nepClient(antwoorden: NepAntwoord[], nu = 1_800_000_000) {
  const nep = nepFetch(antwoorden);
  const slapen: number[] = [];
  const client = new MoneybirdClient({ accessToken: "tok", fetchFn: nep.fn, nu: () => nu, slaap: async (ms) => { slapen.push(ms); } });
  return { client, verzoeken: nep.verzoeken, slapen };
}
