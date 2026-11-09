// Handtekening voor de TikTok Shop API (HMAC-SHA256).
// Bron: https://partner.tiktokshop.com/docv2/page/sign-your-api-request
// Alleen Web Crypto, zodat het in Node 22 en in Cloudflare Workers werkt.

const UITGESLOTEN = new Set(["sign", "access_token"]);

export interface TeTekenen {
  /** Het pad zonder domein, bijvoorbeeld /authorization/202309/shops */
  path: string;
  /** Ruwe (niet gecodeerde) queryparameters. */
  query: Record<string, string>;
  /** Precies de tekst die als body wordt verstuurd, of leeg. */
  body?: string;
  /** Waarde van de kop content-type, als die er is. */
  contentType?: string;
}

/** De tekst die getekend wordt, zonder het secret eromheen. */
export function tekenTekst(req: TeTekenen): string {
  const sleutels = Object.keys(req.query)
    .filter((k) => !UITGESLOTEN.has(k))
    .sort();
  let tekst = req.path;
  for (const k of sleutels) tekst += k + req.query[k];
  const soort = (req.contentType ?? "").split(";")[0].trim().toLowerCase();
  if (soort !== "multipart/form-data" && req.body) tekst += req.body;
  return tekst;
}

function naarHex(buf: ArrayBuffer): string {
  return Array.from(new Uint8Array(buf), (b) => b.toString(16).padStart(2, "0")).join("");
}

export async function hmacSha256Hex(sleutel: string, bericht: string): Promise<string> {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    enc.encode(sleutel),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  return naarHex(await crypto.subtle.sign("HMAC", key, enc.encode(bericht)));
}

/** Maakt de waarde voor de queryparameter `sign`. */
export async function maakHandtekening(req: TeTekenen, appSecret: string): Promise<string> {
  return hmacSha256Hex(appSecret, appSecret + tekenTekst(req) + appSecret);
}
