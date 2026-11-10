const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2560,height:1200}});
await p.goto('https://store.steampowered.com/developer/klei',{waitUntil:'networkidle',timeout:60000});
console.log(JSON.stringify(await p.evaluate(()=>{let e=document.elementFromPoint(100,800);const out=[];while(e){const c=getComputedStyle(e);out.push([e.tagName,e.className.toString().slice(0,40),c.backgroundColor]);e=e.parentElement;}return out;})));
await b.close();})();
