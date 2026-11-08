const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:800},deviceScaleFactor:2});
await p.goto('file://'+__dirname+'/'+process.argv[2]);await p.waitForTimeout(800);await p.screenshot({path:process.argv[3]});await b.close()})();
