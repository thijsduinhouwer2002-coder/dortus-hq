const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2560,height:1400}});
await p.goto('https://store.steampowered.com/developer/klei',{waitUntil:'networkidle',timeout:60000});await p.waitForTimeout(1500);
console.log(JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('*')].map(e=>{const r=e.getBoundingClientRect(),c=getComputedStyle(e);return [e.className.toString().slice(0,50),Math.round(r.top),Math.round(r.left),Math.round(r.width),c.backgroundColor,c.backgroundImage.slice(0,60)]}).filter(a=>a[1]>760&&a[1]<830&&(a[4]!='rgba(0, 0, 0, 0)'||a[5]!='none')))));
await b.close();})();
