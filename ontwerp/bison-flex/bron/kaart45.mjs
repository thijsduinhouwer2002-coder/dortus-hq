// Winkelplaatje hernoemen en meldingen versie 2 (voor en na), Daan 8 nov. In de winkel: meldingen op plek 4, hernoemen op plek 5
// (zo loopt NUM naar NUMBER op volgorde). Gebruik, vanuit bron/: node kaart45.mjs 4 ../winkel-5-hernoemen.png  of  node kaart45.mjs 5 ../winkel-4-meldingen.png
// Schermen komen ongewijzigd uit de IDE-test (tak schermen, map jetbrains-bison-flex/main, run 42488013080), alleen bijgesneden.
// Snede [x, y, b, h] in pixels van het origineel (2880 bij 1800). Regel n staat in deze schermen op y = 538 + (n - 9) * 44.
import { createRequire } from 'module'; const require = createRequire(import.meta.url); const { chromium } = require('playwright');
import fs from 'fs';
const [,, nr, out] = process.argv;
const b = await chromium.launch();
const p0 = await b.newPage();
async function snij(bestand, [x, y, w, h]) {
  const bron = 'data:image/png;base64,' + fs.readFileSync(bestand).toString('base64');
  return p0.evaluate(async ({ bron, x, y, w, h }) => {
    const img = new Image(); img.src = bron; await img.decode();
    const c = document.createElement('canvas'); c.width = w; c.height = h;
    c.getContext('2d').drawImage(img, x, y, w, h, 0, 0, w, h);
    return c.toDataURL('image/png');
  }, { bron, x, y, w, h });
}
const icoon = 'data:image/svg+xml;base64,' + fs.readFileSync('icon.svg').toString('base64');

const basis = `
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1200px;height:760px;overflow:hidden}
body{font-family:Inter,sans-serif;color:#EEF0F6;position:relative;
 background:
  radial-gradient(620px 420px at 8% 92%, rgba(53,116,240,.30), transparent 70%),
  radial-gradient(560px 380px at 96% 6%, rgba(230,109,23,.30), transparent 70%),
  linear-gradient(160deg,#151826 0%,#0D0F18 100%);}
.grain{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.035) 1px,transparent 1px);background-size:22px 22px}
.brand{display:flex;align-items:center;gap:12px;font-weight:600;font-size:17px;letter-spacing:.02em;color:#C9CDDA}
.brand img{width:34px;height:34px}
.chip{display:inline-block;margin-top:26px;font:800 12px Inter;letter-spacing:.1em;border-radius:6px;padding:5px 9px;color:#1A1206;background:linear-gradient(90deg,#FFB067,#FF8A3D)}
h1{margin-top:14px;font-weight:800;font-size:46px;line-height:1.06;letter-spacing:-.025em}
h1 .o{color:#FF8A3D}h1 .b{color:#6E9BFF}
.sub{margin-top:18px;font-size:19px;color:#AEB3C4;line-height:1.45}
.sub code{font-family:'JetBrains Mono';color:#fff;font-size:17px}
.card{position:absolute;border-radius:14px;overflow:hidden;background:#fff;
 box-shadow:0 30px 60px -20px rgba(0,0,0,.75),0 0 0 1px rgba(255,255,255,.10)}
.bar{height:34px;display:flex;align-items:center;gap:8px;padding:0 14px;background:#F2F3F5;border-bottom:1px solid #E3E4E8;font:500 13px Inter;color:#22252B}
.bar .rechts{margin-left:auto;font:600 12px Inter;color:#6C707E}
.ft{font:700 11px 'JetBrains Mono';width:16px;height:16px;border-radius:3px;display:grid;place-items:center;color:#fff}
.ft.y{background:#E66D17}.ft.l{background:#3574F0}
.card img{display:block}
.hl{position:absolute;border-radius:5px;box-shadow:0 0 0 2px #FF8A3D,0 0 18px 3px rgba(255,140,60,.55)}
.key{position:absolute;display:flex;gap:6px;align-items:center;font:600 14px Inter;color:#fff;white-space:nowrap}
.key b{font:700 13px 'JetBrains Mono';background:#F3F4F8;color:#151826;border-radius:6px;padding:5px 9px;box-shadow:0 2px 0 #9AA0B4}
.key code{font:700 14px 'JetBrains Mono'}
.key s{color:#8E93A6}
svg.arc{position:absolute;inset:0;pointer-events:none;overflow:visible}
`;

let html;
if (nr === '4') {
  // calc.y links in het scherm, calc.l rechts. calc.y regel 8 tot 27, calc.l regel 9 tot 14.
  const sy = 0.62, sl = 0.46;
  const Y = { snede: [84, 472, 916, 876] }, L = { snede: [1446, 516, 1204, 220] };
  const cy = await snij('scherm-licht-hernoemd.png', Y.snede), cl = await snij('scherm-licht-hernoemd.png', L.snede);
  const yw = Math.round(916 * sy), lw = Math.round(1204 * sl);
  html = `<!doctype html><html><head><meta charset="utf-8"><style>${basis}
  .tekst{position:absolute;left:64px;top:56px;width:500px}
  #cy{left:${1136 - yw}px;top:56px;width:${yw}px}
  #cl{left:64px;top:400px;width:${lw}px}
  </style></head><body>
  <div class="grain"></div>
  <div class="tekst">
    <div class="brand"><img src="${icoon}">Bison &amp; Flex for JetBrains IDEs</div>
    <span class="chip">PRO</span>
    <h1>Rename once.<br><span class="o">Both files</span> follow.</h1>
    <p class="sub">Shift+F6 on a token changes its <code>%token</code>, every rule that uses it and the <code>return</code> in your scanner.</p>
  </div>
  <div class="card" id="cy"><div class="bar"><span class="ft y">Y</span>calc.y</div><img src="${cy}" width="${yw}"></div>
  <div class="card" id="cl"><div class="bar"><span class="ft l">L</span>calc.l</div><img src="${cl}" width="${lw}"></div>
  <div class="hl" id="h1"></div><div class="hl" id="h2"></div><div class="hl" id="h3"></div>
  <svg class="arc" width="1200" height="760"><defs>
   <linearGradient id="g" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#6E9BFF"/><stop offset="1" stop-color="#FF8A3D"/></linearGradient>
   <marker id="m" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#FF8A3D"/></marker>
  </defs></svg>
  <div class="key" id="k"><b>Shift</b>+<b>F6</b>&nbsp;&nbsp;<code><s>NUM</s> → NUMBER</code>&nbsp;&nbsp;<span style="color:#AEB3C4;font-weight:500">3 places, 2 files</span></div>
  <script>
  function box(id, card, s, snede, x0, x1, yc) {
    const r = document.getElementById(card).getBoundingClientRect(), el = document.getElementById(id), h = 30 * s * 1.25;
    const L = r.left + (x0 - snede[0]) * s - 5, T = r.top + 34 + (yc - snede[1]) * s - h / 2, W = (x1 - x0) * s + 10;
    Object.assign(el.style, { left: L + 'px', top: T + 'px', width: W + 'px', height: h + 'px' });
    return { l: L, r: L + W, t: T, b: T + h, x: L + W / 2, y: T + h / 2 };
  }
  const a = box('h1', 'cl', ${sl}, [${L.snede}], 2489, 2582, 626);
  const t = box('h2', 'cy', ${sy}, [${Y.snede}], 329, 422, 538);
  const e = box('h3', 'cy', ${sy}, [${Y.snede}], 281, 374, 1286);
  const k = document.getElementById('k'); k.style.left = '64px'; k.style.top = (document.getElementById('cl').getBoundingClientRect().bottom + 30) + 'px';
  </script></body></html>`;
} else {
  // voor: regel 14 tot 27 met de grijze regel term en het Alt+Enter-menu; na: dezelfde regels nadat de snelle oplossing draaide.
  const snede = [84, 736, 896, 616], s = 490 / 896;
  const voor = await snij('scherm-licht-melding-menu-term.png', snede), na = await snij('scherm-licht-melding-na.png', snede);
  html = `<!doctype html><html><head><meta charset="utf-8"><style>${basis}
  .tekst{position:absolute;left:64px;top:56px;width:1072px}
  #cv{left:64px;top:300px;width:490px}#cn{left:646px;top:300px;width:490px}
  .lab{font:800 11px Inter;letter-spacing:.08em;border-radius:5px;padding:3px 7px;margin-left:auto}
  .lab.v{color:#7A5200;background:#FFE8B3}.lab.n{color:#0D4D26;background:#C9F2D6}
  </style></head><body>
  <div class="grain"></div>
  <div class="tekst">
    <div class="brand"><img src="${icoon}">Bison &amp; Flex for JetBrains IDEs</div>
    <span class="chip">PRO</span>
    <h1>Dead rules? <span class="o">Gone</span> with Alt+Enter.</h1>
    <p class="sub">Unused rules and tokens turn grey as you type. One quick fix removes them.</p>
  </div>
  <div class="card" id="cv"><div class="bar"><span class="ft y">Y</span>calc.y<span class="lab v">BEFORE</span></div><img src="${voor}" width="490"></div>
  <div class="card" id="cn"><div class="bar"><span class="ft y">Y</span>calc.y<span class="lab n">AFTER</span></div><img src="${na}" width="490"></div>
  <div class="hl" id="h1"></div>
  <div class="key" id="k" style="flex-direction:column;gap:4px"><b>Alt</b><span>+</span><b>Enter</b></div>
  <svg class="arc" width="1200" height="760"><defs><marker id="m" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="#FF8A3D"/></marker></defs>
   <path id="p" fill="none" stroke="#FF8A3D" stroke-width="3.5" stroke-linecap="round" marker-end="url(#m)"/></svg>
  <script>
  const r = document.getElementById('cv').getBoundingClientRect(), s = ${s};
  // regel 20 (term) op y 1022, tekst x 216 tot 296
  const h = 30 * s * 1.25, el = document.getElementById('h1');
  Object.assign(el.style, { left: (r.left + (214 - 84) * s - 5) + 'px', top: (r.top + 34 + (1022 - 736) * s - h / 2) + 'px', width: (84 * s + 10) + 'px', height: h + 'px' });
  const k = document.getElementById('k'), kb = k.getBoundingClientRect();
  k.style.left = (600 - kb.width / 2) + 'px'; const ky = r.top + 34 + (1022 - 736) * s - kb.height / 2 - 40; k.style.top = ky + 'px';
  const y = ky + kb.height + 24;
  document.getElementById('p').setAttribute('d', 'M 582 ' + y + ' L 616 ' + y);
  </script></body></html>`;
}
const p = await b.newPage({ viewport: { width: 1200, height: 760 }, deviceScaleFactor: 2 });
await p.setContent(html, { waitUntil: 'networkidle' });
await p.waitForTimeout(400);
await p.screenshot({ path: out });
await b.close();
