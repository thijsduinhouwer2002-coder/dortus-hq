// Winkelplaatje 2 tot 5 (Daan). Gebruik, vanuit bron/: node kaart.mjs kaarten.json <nummer> <uit.png>
// Het scherm komt ongewijzigd uit de IDE-test (tak schermen), alleen bijgesneden met "snede" [x, y, b, h] in pixels van het origineel.
import { createRequire } from 'module'; const require = createRequire(import.meta.url); const { chromium } = require('playwright');
import fs from 'fs';
const [,, cfgPad, nr, out] = process.argv;
const k = JSON.parse(fs.readFileSync(cfgPad, 'utf8'))[nr];
const b = await chromium.launch();
// bijsnijden in de browser zelf, zodat er geen extra programma nodig is
const p0 = await b.newPage();
const bron = 'data:image/png;base64,' + fs.readFileSync(k.scherm).toString('base64');
const [x, y, w, h] = k.snede;
const snede = await p0.evaluate(async ({ bron, x, y, w, h }) => {
  const img = new Image(); img.src = bron; await img.decode();
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  c.getContext('2d').drawImage(img, x, y, w, h, 0, 0, w, h);
  return c.toDataURL('image/png');
}, { bron, x, y, w, h });
let s = fs.readFileSync('kaart.html', 'utf8')
  .replace('LAYOUT', k.layout).replace('CHIPKLASSE', k.chip.toLowerCase()).replace('CHIPTEKST', k.chip.toUpperCase())
  .replace('KOP', k.kop).replace('SUB', k.sub).replace('SCHERM', snede)
  .replace('src="icon.svg"', 'src="data:image/svg+xml;base64,' + fs.readFileSync('icon.svg').toString('base64') + '"');
const p = await b.newPage({ viewport: { width: 1200, height: 760 }, deviceScaleFactor: 2 });
await p.setContent(s, { waitUntil: 'networkidle' });
await p.waitForTimeout(300);
await p.screenshot({ path: out });
await b.close();
