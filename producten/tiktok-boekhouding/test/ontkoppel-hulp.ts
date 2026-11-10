// Hulp voor de toetsen van ontkoppelen en opruimen (ontwerp-d1-worker.md, punt 7, toetsen l tot o).
import { NepD1 } from "./d1-nep.ts";
import { versleutel, type Sleutelbos } from "../src/d1/tokens.ts";
import type { IntrekDeps } from "../src/d1/ontkoppel.ts";

export const NU = 1_800_000_000;
export const DAG = 24 * 3600;
export const bos: Sleutelbos = { huidig: "v1", sleutels: { v1: crypto.getRandomValues(new Uint8Array(32)) } };
export const app = { clientId: "cid", clientSecret: "geheim", redirectUri: "https://x" };

/** Nagebootste Moneybird voor /oauth/revoke: antwoorden op volgorde, daarna steeds de laatste. */
export function nepRevoke(...statussen: Array<number | "netwerk">) {
  const verzoeken: Array<{ url: string; body: Record<string, string> }> = [];
  const lijst = statussen.length ? statussen : [200];
  const fn = (async (input: any, init: any = {}) => {
    verzoeken.push({ url: String(input), body: Object.fromEntries(new URLSearchParams(String(init.body))) });
    const s = lijst[Math.min(verzoeken.length - 1, lijst.length - 1)];
    if (s === "netwerk") throw new TypeError("fetch failed");
    return new Response(s === 200 ? "{}" : JSON.stringify({ error: "x" }), { status: s });
  }) as typeof fetch;
  return { fn, verzoeken };
}

export function deps(fetchFn: typeof fetch) {
  const log: string[] = [];
  const d: IntrekDeps = { app, sleutels: bos, fetchFn, log: (r) => log.push(r) };
  return { d, log, alarmen: () => log.filter((r) => r.startsWith("ALARM")) };
}

/** Een volledig gekoppelde winkel met rijen in alle vier de tabellen. */
export async function vulWinkel(db: NepD1, w: string, opties: { mb?: boolean; polar?: string } = {}) {
  const mb = opties.mb === false ? null : await versleutel(bos, w, JSON.stringify({ accessToken: `GEHEIM-a-${w}`, refreshToken: `GEHEIM-r-${w}`, scope: "documents" }));
  const tt = await versleutel(bos, w, JSON.stringify({ accessToken: "GEHEIM-tt" }));
  db.sqlite
    .prepare(
      `INSERT INTO winkels (id, shop_id, shop_cipher, tt_tokens, mb_tokens, tt_versie, mb_versie, administratie, instellingen, markering, winkelfout, winkelfout_sinds, volgende_run, snel_teller, polar_klant)
       VALUES (?, ?, ?, ?, ?, 3, 2, 'adm-1', '{"startdatum":1}', 77, NULL, NULL, 123, 4, ?)
       ON CONFLICT(id) DO UPDATE SET tt_tokens = excluded.tt_tokens, mb_tokens = excluded.mb_tokens, tt_versie = 3, mb_versie = 2,
       administratie = 'adm-1', instellingen = excluded.instellingen, markering = 77, volgende_run = 123, snel_teller = 4, polar_klant = excluded.polar_klant`,
    )
    .run(w, `shop-${w}`, `cipher-${w}`, tt, mb, opties.polar ?? null);
  db.sqlite.prepare("INSERT INTO statussen VALUES (?, 's1', 'geboekt', 1, NULL, '{}')").run(w);
  db.sqlite.prepare("INSERT INTO statussen VALUES (?, 's2', 'onvolledig', 2, NULL, '{}')").run(w);
  db.sqlite.prepare("INSERT INTO transacties VALUES (?, 's2', '{}', 1)").run(w);
  db.sqlite.prepare("INSERT INTO bestellingen VALUES (?, 's2', 'o1', '{}', 1)").run(w);
  db.sqlite.prepare("INSERT INTO sloten VALUES (?, '__winkel', 'run-x', 999999999999)").run(w);
}

export const tel = (db: NepD1, tabel: string, w: string) => Number((db.sqlite.prepare(`SELECT count(*) n FROM ${tabel} WHERE winkel = ?`).get(w) as any).n);
export const rij = (db: NepD1, w: string) => db.sqlite.prepare("SELECT * FROM winkels WHERE id = ?").get(w) as Record<string, any> | undefined;
export const taken = (db: NepD1, w: string) => JSON.parse(String(rij(db, w)?.taken ?? "null"));
