// De stijl van Daan (ontwerp.md, "Stijl voor de bouw"), als één CSS-bestand op `/app/stijl.css`.
// Geen inline stijl: de CSP staat dat niet toe. Verhoog STIJL_VERSIE bij elke wijziging, zodat de cache vernieuwt.

export const STIJL_VERSIE = "2";
export const STIJL_PAD = `/app/stijl.css?v=${STIJL_VERSIE}`;

export const KLEUREN = {
  papier: "#F5F3EE",
  kaart: "#FFFFFF",
  inkt: "#17161C",
  zacht: "#6B6875",
  lijn: "#E4E1DA",
  paars: "#4F3BD1",
  goed: "#0B6E3F",
  goedVlak: "#E3F5EA",
  apart: "#9A5B00",
  apartVlak: "#FFF3D6",
  fout: "#C2261F",
  foutVlak: "#FDE8E6",
  wachtVlak: "#ECE9FF",
} as const;

const k = KLEUREN;

export const CSS = `@font-face{font-family:Inter;src:url(/fonts/inter-latin-400-normal.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:Inter;src:url(/fonts/inter-latin-600-normal.woff2) format("woff2");font-weight:600;font-display:swap}
@font-face{font-family:Inter;src:url(/fonts/inter-latin-700-normal.woff2) format("woff2");font-weight:700;font-display:swap}
@font-face{font-family:Inter;src:url(/fonts/inter-latin-800-normal.woff2) format("woff2");font-weight:800;font-display:swap}
*{box-sizing:border-box}
html{background:${k.papier};color:${k.inkt};font:16px/1.5 Inter,system-ui,sans-serif}
body{margin:0}
.kop{display:flex;align-items:center;gap:12px;padding:16px 24px;border-bottom:1px solid ${k.lijn};background:${k.kaart}}
.merk{font-weight:700;color:${k.paars}}
.vlak{max-width:880px;margin:0 auto;padding:32px 16px}
.stap{color:${k.zacht};font-size:14px;margin:0 0 8px}
h1{font-size:28px;line-height:1.2;margin:0 0 8px}
p{margin:0 0 12px}
.zacht{color:${k.zacht}}
.kaart{background:${k.kaart};border:1px solid ${k.lijn};border-radius:14px;padding:24px}
.blokken{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:24px 0}
.knop{display:inline-block;border:0;border-radius:10px;padding:12px 18px;font:600 16px Inter,system-ui,sans-serif;cursor:pointer;text-decoration:none}
.knop-hoofd{background:${k.paars};color:#fff}
.knop-gewoon{background:${k.kaart};color:${k.inkt};border:1px solid ${k.lijn}}
a{color:${k.paars}}
.pil{display:inline-block;border-radius:999px;padding:2px 10px;font-size:13px;font-weight:600}
.pil-goed{color:${k.goed};background:${k.goedVlak}}
.pil-apart{color:${k.apart};background:${k.apartVlak}}
.pil-fout{color:${k.fout};background:${k.foutVlak}}
.pil-wacht{color:${k.paars};background:${k.wachtVlak}}
.stip{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px}
.stip-goed{background:${k.goed}}
.stip-uit{background:${k.lijn}}
.staat{text-align:center;max-width:520px;margin:48px auto}
.teken{font-size:48px;color:${k.paars}}
.bedrag{font-variant-numeric:tabular-nums;text-align:right}
.lijst{list-style:none;padding:0;margin:0}
.lijst li{padding:12px 0;border-top:1px solid ${k.lijn}}
.verborgen{display:none}
.melding{background:${k.apartVlak};color:${k.apart};border-radius:10px;padding:12px 16px;margin:16px 0}
fieldset{border:0;padding:0;margin:0}
legend{font-weight:600;margin-bottom:8px}
@media (max-width:600px){.blokken{grid-template-columns:1fr}.knop{display:block;width:100%;text-align:center}.kop{padding:12px 16px}}
`;

export function stijlAntwoord(): Response {
  return new Response(CSS, {
    headers: {
      "content-type": "text/css; charset=utf-8",
      "cache-control": "public, max-age=31536000, immutable",
      "x-content-type-options": "nosniff",
    },
  });
}
