const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const d=f=>'data:image/png;base64,'+fs.readFileSync(M+f).toString('base64');
const kop=process.argv[2]||'steam-kop-1500x220.png';const out=process.argv[3]||'mock';
(async()=>{const b=await chromium.launch();
for (const w of [1280,1024]){const p=await b.newPage({viewport:{width:w,height:420}});
await p.goto('https://store.steampowered.com/developer/klei',{waitUntil:'networkidle',timeout:60000});
await p.evaluate(([kopd,av])=>{document.querySelector('.background_header_ctn').style.backgroundImage=`url(${kopd})`;
document.querySelector('img.curator_avatar').src=av;
const h=[...document.querySelectorAll('*')].find(e=>e.children.length==0&&e.textContent.trim()=='Klei'&&e.getBoundingClientRect().top<250);if(h)h.textContent='Dortus';
document.querySelectorAll('a').forEach(a=>{if(/Official Website/.test(a.textContent))a.innerHTML='dortus.com';});
document.querySelectorAll('a').forEach(a=>{const r=a.getBoundingClientRect();if(r.top>150&&r.top<300&&a.querySelector('svg')&&!/dortus/.test(a.textContent))a.style.display='none';});
document.querySelectorAll('a,div').forEach(e=>{if(/^[\d,]+$/.test(e.textContent.trim())&&e.children.length==0)e.textContent='0';});
},[d(kop),d('avatar-184.png')]);
await p.waitForTimeout(800);await p.screenshot({path:`${out}-${w}.png`,clip:{x:0,y:100,width:w,height:320}});await p.close();}
await b.close();})();
