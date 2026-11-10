// De stijl van Daan (ontwerp.md, "Stijl voor de bouw"), als één CSS-bestand op `/app/stijl.css`.
// Geen inline stijl: de CSP staat dat niet toe. Verhoog STIJL_VERSIE bij elke wijziging, zodat de cache vernieuwt.

export const STIJL_VERSIE = "4";
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
/** Tegel van Moneybird in de schets van Daan (`kunst/maak.py`); geen merkkleur uit hun huisstijl, alleen een letter. */
const TEGEL_MB = "#1E6FD9";

export const CSS = `@font-face{font-family:Inter;src:url(/fonts/inter-latin-400-normal.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:Inter;src:url(/fonts/inter-latin-600-normal.woff2) format("woff2");font-weight:600;font-display:swap}
@font-face{font-family:Inter;src:url(/fonts/inter-latin-700-normal.woff2) format("woff2");font-weight:700;font-display:swap}
@font-face{font-family:Inter;src:url(/fonts/inter-latin-800-normal.woff2) format("woff2");font-weight:800;font-display:swap}
*{box-sizing:border-box}
html{background:${k.papier};color:${k.inkt};font:15px/1.45 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
body{margin:0}
.kop{display:flex;align-items:center;gap:14px;padding:18px 32px;border-bottom:1px solid ${k.lijn};background:${k.kaart}}
.merk{display:flex;align-items:center;gap:10px;font-weight:700;font-size:17px;letter-spacing:-.01em}
.logo{width:30px;height:30px}
.vlak{max-width:860px;margin:0 auto;padding:36px 32px 48px}
.stap{margin-left:auto;font-size:13px;font-weight:500;padding:4px 10px;border-radius:99px;background:${k.papier};border:1px solid ${k.lijn}}
h1{font-size:28px;line-height:1.15;letter-spacing:-.02em;margin:0 0 6px}
h1+.zacht{font-size:16px}
p{margin:0 0 12px}
.zacht{color:${k.zacht}}
.kaart{background:${k.kaart};border:1px solid ${k.lijn};border-radius:14px;padding:24px}
.blokken{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:24px 0}
.knop{display:inline-block;border:0;border-radius:10px;padding:11px 18px;font:600 15px Inter,system-ui,sans-serif;cursor:pointer;text-decoration:none}
.knop-hoofd{background:${k.paars};color:#fff}
.knop-gewoon{background:${k.kaart};color:${k.inkt};border:1px solid ${k.lijn}}
a{color:${k.paars}}
.pil{display:inline-block;align-self:flex-start;border-radius:999px;padding:3px 10px;font-size:13px;font-weight:600;margin:0}
.koppel{display:flex;align-items:center;gap:16px;margin:28px 0 12px}
.koppel+.klein{margin:0 0 22px}
.koppel>.kaart{flex:1;padding:26px;display:flex;flex-direction:column;gap:14px}
.koppel form{margin:0}
.pijl{color:${k.zacht};font-size:20px}
.dienst{display:flex;align-items:center;gap:12px}
.dienst h2{font-size:17px;margin:0}
.dienst p{margin:0;font-size:14px;color:${k.zacht}}
.tegel{flex:none;width:44px;height:44px;border-radius:11px;color:#fff;display:grid;place-items:center;font-weight:800;font-size:20px}
.tegel-tt{background:${k.inkt}}
.tegel-mb{background:${TEGEL_MB}}
.klein{font-size:13px;color:${k.zacht};margin:0}
.pil-goed{color:${k.goed};background:${k.goedVlak}}
.pil-apart{color:${k.apart};background:${k.apartVlak}}
.pil-fout{color:${k.fout};background:${k.foutVlak}}
.pil-wacht{color:${k.paars};background:${k.wachtVlak}}
.stip{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px}
.stip-goed{background:${k.goed}}
.stip-uit{background:${k.lijn}}
.staat{text-align:center;max-width:560px;margin:24px auto;padding:34px 26px;display:flex;flex-direction:column;align-items:center;gap:10px;min-height:270px;justify-content:center}
.staat h1{font-size:17px;margin:0}
.staat p{font-size:14px;max-width:320px;margin:0}
.staat .knop{margin-top:6px}
.teken{width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font-weight:800;font-size:16px}
.teken-paars{background:${k.wachtVlak};color:${k.paars}}
.teken-fout{background:${k.foutVlak};color:${k.fout};font-size:24px}
.logo-groot{width:56px;height:56px}
.bedrag{font-variant-numeric:tabular-nums;text-align:right}
.lijst{list-style:none;padding:0;margin:0}
.lijst li{padding:12px 0;border-top:1px solid ${k.lijn}}
.verborgen{display:none}
.melding{background:${k.apartVlak};color:${k.apart};border-radius:10px;padding:12px 16px;margin:16px 0}
fieldset{border:0;padding:0;margin:0}
legend{font-weight:600;margin-bottom:8px}
@media (max-width:600px){.blokken{grid-template-columns:1fr}.koppel{flex-direction:column;align-items:stretch}.pijl{align-self:center;transform:rotate(90deg)}.knop{display:block;width:100%;text-align:center}.kop{padding:14px 16px}.vlak{padding:22px 16px 40px}h1{font-size:23px}}
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
