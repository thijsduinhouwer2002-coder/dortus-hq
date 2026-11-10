// Webhook van Polar (ontwerp-betalen.md, punt 3). Schrijft alleen naar `winkels.abonnement` en `polar_klant`; doet geen
// verzoeken naar buiten (antwoord binnen 2 seconden). Logt alleen eventtype, winkelsleutel en webhook-id.
//
// Handtekening: Standard Webhooks (GEZIEN, polar.sh/docs/integrate/webhooks/delivery.md en de spec). Getekend wordt
// `webhook-id + "." + webhook-timestamp + "." + ruwe body`, HMAC-SHA256, base64, in de kop als `v1,<base64>`, eventueel
// meerdere gescheiden door spaties. Sleutel: secrets van vóór 8 sep 2026 gebruiken de UTF-8-bytes van de hele `whsec_...`
// tekst, latere de base64-gedecodeerde rest na `whsec_`. We proberen beide, zoals de SDK's van Polar.
//
// Payloads (OpenAPI 2026-10, componenten WebhookCustomerStateChangedPayload en WebhookSubscription*Payload): verplicht
// `type`, `timestamp` (date-time, tijdstip van het event), `api_version` en `data`. `customer.state_changed`: `data` is
// CustomerState (`id`, `external_id`, `deleted_at`, `active_subscriptions`). `subscription.*`: `data` is Subscription
// (`id`, `status`, `metadata`, `customer` met `external_id`).
import type { Omgeving } from "../worker.ts";
import type { D1Statement } from "../d1/opslag.ts";
import { microVan, schrijfStand, schrijfVlag, standUitState, type PolarKlantStand } from "./abonnement.ts";
import { POLAR_VERSIE } from "./client.ts";

export const POLAR_WEBHOOK_PAD = "/polar/webhook";
export const MAX_BODY = 64 * 1024;
/** Tijdvenster op de kop `webhook-timestamp`, beide kanten op (zoals de bibliotheek van Standard Webhooks). */
export const VENSTER = 5 * 60;
/** Sleutel van een winkel: niet leeg, niet absurd lang. */
const SLEUTEL = /^[\x21-\x7e]{1,200}$/;

const tekst = (status: number, body = "") => new Response(body, { status });

const enc = new TextEncoder();

function base64NaarBytes(b64: string): Uint8Array | null {
  try {
    return Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
  } catch {
    return null;
  }
}

function bytesNaarBase64(b: Uint8Array): string {
  let s = "";
  for (const x of b) s += String.fromCharCode(x);
  return btoa(s);
}

/** De sleutels die we proberen: (a) base64 van de rest na `whsec_`, (b) UTF-8 van de hele tekst. */
export function sleutelsVan(secret: string): Uint8Array[] {
  const uit: Uint8Array[] = [];
  const a = base64NaarBytes(secret.startsWith("whsec_") ? secret.slice(6) : secret);
  if (a && a.length) uit.push(a);
  uit.push(enc.encode(secret));
  return uit;
}

/** `v1,<base64>` voor één sleutel, over de ruwe bytes van de body. */
export async function tekenPolar(sleutel: Uint8Array, id: string, tijd: string, body: Uint8Array): Promise<string> {
  const k = await crypto.subtle.importKey("raw", sleutel, { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const kop = enc.encode(`${id}.${tijd}.`);
  const data = new Uint8Array(kop.length + body.length);
  data.set(kop, 0);
  data.set(body, kop.length);
  return `v1,${bytesNaarBase64(new Uint8Array(await crypto.subtle.sign("HMAC", k, data)))}`;
}

/** Vergelijken in constante tijd (bij gelijke lengte; de lengte van een handtekening is geen geheim). */
export function gelijk(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let verschil = 0;
  for (let i = 0; i < a.length; i++) verschil |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return verschil === 0;
}

/** Klopt de handtekening? Geeft de reden als tekst als het niet klopt (voor het log), anders null. */
export async function controleer(secret: string, koppen: Headers, body: Uint8Array, nu: number): Promise<string | null> {
  const id = koppen.get("webhook-id") ?? "";
  const tijd = koppen.get("webhook-timestamp") ?? "";
  const kop = koppen.get("webhook-signature") ?? "";
  if (!id || !tijd || !kop) return "kop ontbreekt";
  if (!/^\d{1,12}$/.test(tijd) || Math.abs(nu - Number(tijd)) > VENSTER) return "buiten het tijdvenster";
  const gegeven = kop.split(" ").filter((h) => h.startsWith("v1,"));
  let goed = false;
  for (const sleutel of sleutelsVan(secret)) {
    const verwacht = await tekenPolar(sleutel, id, tijd, body);
    // Alles nalopen, niet stoppen bij de eerste die klopt.
    for (const h of gegeven) if (gelijk(h, verwacht)) goed = true;
  }
  return goed ? null : "handtekening klopt niet";
}

export async function polarWebhook(request: Request, o: Omgeving, nu: number): Promise<Response> {
  const url = new URL(request.url);
  if (url.pathname !== POLAR_WEBHOOK_PAD) return tekst(404);
  if (request.method !== "POST") return tekst(405);

  if (Number(request.headers.get("content-length") ?? 0) > MAX_BODY) return tekst(413);
  const bytes = new Uint8Array(await request.arrayBuffer());
  if (bytes.length > MAX_BODY) return tekst(413);

  const secret = o.polar?.webhookSecret;
  if (!secret) {
    o.log("ALARM polar-webhook: POLAR_WEBHOOK_SECRET ontbreekt");
    return tekst(500);
  }
  const webhookId = (request.headers.get("webhook-id") ?? "").slice(0, 100);
  const reden = await controleer(secret, request.headers, bytes, nu);
  if (reden) {
    // Een verkeerd secret laat Polar het endpoint na 10 fouten uitzetten: moet opvallen.
    o.log(`ALARM polar-webhook ${webhookId || "?"}: geweigerd (${reden})`);
    return tekst(403);
  }

  // Versie vast: met een andere versie lezen we misschien velden verkeerd. Niets doen; de volgende twijfel herstelt het.
  const versie = request.headers.get("webhook-api-version");
  if (versie !== POLAR_VERSIE) {
    o.log(`polar-webhook ${webhookId}: api-versie ${String(versie).slice(0, 20)} in plaats van ${POLAR_VERSIE}, niets gedaan`);
    return tekst(202);
  }

  let bericht: unknown;
  try {
    bericht = JSON.parse(new TextDecoder().decode(bytes));
  } catch {
    return tekst(400);
  }
  if (bericht === null || typeof bericht !== "object" || Array.isArray(bericht)) return tekst(400);
  const b = bericht as { type?: unknown; timestamp?: unknown; data?: any };
  const type = typeof b.type === "string" ? b.type.slice(0, 60) : "?";
  const data = b.data && typeof b.data === "object" ? b.data : undefined;
  const log = (winkel: string, wat: string) => o.log(`polar-webhook ${type} winkel ${winkel} ${webhookId}: ${wat}`);

  const isAbonnementEvent = ["subscription.past_due", "subscription.active", "subscription.uncanceled", "subscription.updated"].includes(type);
  if (type !== "customer.state_changed" && !isAbonnementEvent) return tekst(202);

  // Volgorde: het tijdstip van het event uit de body, niet de kop (die wordt bij elke herhaling vernieuwd).
  const stand = microVan(b.timestamp);
  if (stand === null || !data) {
    log("?", "timestamp of data ontbreekt, niets gedaan");
    return tekst(202);
  }

  let winkel: string;
  let schrijf: D1Statement;
  if (type === "customer.state_changed") {
    const state = data as PolarKlantStand;
    winkel = typeof state.external_id === "string" ? state.external_id : "";
    if (!SLEUTEL.test(winkel)) {
      log("?", "geen winkelsleutel (external_id), niets gedaan");
      return tekst(202);
    }
    schrijf = schrijfStand(o.db, winkel, standUitState(state, winkel, stand), typeof state.id === "string" ? state.id : null);
  } else {
    // Van welke winkel: `metadata.winkel`, anders `customer.external_id`. Een event met de sleutel van een andere winkel
    // in de metadata raakt deze winkel dus niet, ook als de klant dezelfde is.
    const mw = data.metadata?.winkel;
    const ext = data.customer?.external_id;
    winkel = mw !== undefined && mw !== null ? String(mw) : typeof ext === "string" ? ext : "";
    if (!SLEUTEL.test(winkel)) {
      log("?", "geen winkelsleutel (metadata.winkel of customer.external_id), niets gedaan");
      return tekst(202);
    }
    let vlag: boolean;
    if (type === "subscription.past_due") vlag = true;
    else if (type === "subscription.updated" && data.status !== "active") return tekst(202); // alleen status active wist de vlag
    else vlag = false;
    schrijf = schrijfVlag(o.db, winkel, vlag, stand);
  }

  try {
    const r = await schrijf.run();
    log(winkel, r.meta.changes === 1 ? "verwerkt" : "niets geschreven (onbekend, ontkoppeld, oud of dubbel)");
    return tekst(202);
  } catch (e) {
    log(winkel, `D1 mislukt, Polar probeert opnieuw: ${String((e as Error)?.message ?? e).slice(0, 200)}`);
    return tekst(500);
  }
}
