const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720},deviceScaleFactor:2});
for(const [f,t,o] of [['a-r.html',8.9,'poster-a.png'],['b-r.html',6.0,'poster-b.png']]){await p.goto('file://'+__dirname+'/'+f);await p.waitForTimeout(800);
await p.evaluate(t=>render(t),t);await p.waitForTimeout(400);await p.screenshot({path:o})}await b.close()})();
