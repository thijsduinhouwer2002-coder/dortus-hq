// Webhook-ingang van TikTok (ontwerp-d1-worker.md, versie 3e, en punt 7 (b)). Alleen type 6 (verkoper trekt de app in)
// doet iets: die winkel meteen ontkoppelen. Handtekening (GEZIEN, docs "Header and signature verification"): kop
// `Authorization` = hex(HMAC-SHA256(app_key + ruwe body, app_secret)), kleine letters, zonder "Bearer".

import { Budget } from "./budget.ts";
import { ontkoppelOpShopId } from "./d1/ontkoppel.ts";
import type { Omgeving } from "./worker.ts";

export const WEBHOOK_PAD = "/tiktok/webhook";
export const MAX_BODY = 64 * 1024;
const WEBHOOK_BUDGET = 50;

const tekst = (status: number, body = "") => new Response(body, { status });

/** Over de ruwe bytes (app_key ervoor), zodat een BOM of ongeldige UTF-8 niet stil verandert wat getekend is. */
export async function handtekening(appKey: string, appSecret: string, rauw: string | Uint8Array): Promise<string> {
  const enc = new TextEncoder();
  const sleutel = await crypto.subtle.importKey("raw", enc.encode(appSecret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const kop = enc.encode(appKey);
  const body = typeof rauw === "string" ? enc.encode(rauw) : rauw;
  const data = new Uint8Array(kop.length + body.length);
  data.set(kop, 0);
  data.set(body, kop.length);
  const mac = new Uint8Array(await crypto.subtle.sign("HMAC", sleutel, data));
  return Array.from(mac, (b) => b.toString(16).padStart(2, "0")).join("");
}

/** Vergelijken in constante tijd (bij gelijke lengte). */
export function gelijk(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let verschil = 0;
  for (let i = 0; i < a.length; i++) verschil |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return verschil === 0;
}

export async function webhook(request: Request, o: Omgeving, nu: number): Promise<Response> {
  const url = new URL(request.url);
  if (url.pathname !== WEBHOOK_PAD) return tekst(404);
  if (request.method !== "POST") return tekst(405);

  // Ruwe body, begrensd. Content-Length kan liegen of ontbreken, dus ook de echte lengte controleren.
  if (Number(request.headers.get("content-length") ?? 0) > MAX_BODY) return tekst(413);
  const bytes = new Uint8Array(await request.arrayBuffer());
  if (bytes.length > MAX_BODY) return tekst(413);

  // Zonder app key of secret valt er niets te controleren: nooit doorlaten.
  if (!o.tiktokApp.appKey || !o.tiktokApp.appSecret) {
    o.log("webhook: TIKTOK_APP_KEY of TIKTOK_APP_SECRET ontbreekt");
    return tekst(500);
  }
  // Handtekening eerst, over de ruwe bytes, vóór JSON.
  const kop = request.headers.get("authorization") ?? "";
  const verwacht = await handtekening(o.tiktokApp.appKey, o.tiktokApp.appSecret, bytes);
  if (!kop || !gelijk(kop, verwacht)) return tekst(401);
  const rauw = new TextDecoder().decode(bytes);

  let bericht: unknown;
  try {
    bericht = JSON.parse(rauw);
  } catch {
    return tekst(400);
  }
  if (bericht === null || typeof bericht !== "object" || Array.isArray(bericht)) return tekst(400);
  const b = bericht as Record<string, unknown>;
  const type = Number(b.type);

  if (type === 6) {
    const shopId = b.shop_id;
    // Alleen tekst met cijfers: een JSON-getal van 19 cijfers is al afgerond door JSON.parse.
    if (typeof shopId !== "string" || !/^\d{1,40}$/.test(shopId)) {
      o.log("webhook type 6: shop_id ontbreekt of is geen tekst met cijfers");
      return tekst(400);
    }
    try {
      const uit = await ontkoppelOpShopId(o.db, shopId, "webhook_6", nu, new Budget(WEBHOOK_BUDGET), {
        app: o.moneybirdApp, sleutels: o.sleutels, fetchFn: o.fetchFn, log: o.log,
      });
      if (!uit.ontkoppeld) o.log(`webhook type 6: shop_id ${shopId} onbekend of al ontkoppeld`);
      return tekst(200, "ok");
    } catch (e) {
      o.log(`webhook type 6: ontkoppelen van shop_id ${shopId} mislukt of niet afgemaakt (kijk of ontkoppeld_op gezet is): ${String((e as Error)?.message ?? e)}`);
      return tekst(500);
    }
  }
  if (type === 7) {
    const shopId = typeof b.shop_id === "string" && /^\d{1,40}$/.test(b.shop_id) ? b.shop_id : "?";
    o.log(`webhook type 7: koppeling van shop_id ${shopId} verloopt binnenkort`);
    return tekst(200, "ok");
  }
  return tekst(200, "ok");
}
