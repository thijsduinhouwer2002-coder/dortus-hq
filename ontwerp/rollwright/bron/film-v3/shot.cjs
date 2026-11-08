const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
await p.goto('file://'+__dirname+'/render.html');await p.waitForTimeout(800);
const ts=process.argv.slice(3).map(Number);const out=process.argv[2];
for(let i=0;i<ts.length;i++){await p.evaluate(t=>render(t),ts[i]);await p.evaluate(()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>i.onload=r))));
await p.screenshot({path:out.replace('%d',String(i).padStart(4,'0'))})}await b.close()})();
