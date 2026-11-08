const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 800 }, deviceScaleFactor: +process.argv[3] || 1.5 });
  await p.goto('file://' + __dirname + '/poster.html');
  await p.waitForTimeout(1500);
  await p.screenshot({ path: process.argv[2] });
  await b.close();
})();
