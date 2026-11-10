const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const BG=process.argv[2],OUT=process.argv[3],KOP=process.argv[4],LOGO=process.argv[5];
const d=f=>'data:image/png;base64,'+fs.readFileSync(M+f).toString('base64');
(async()=>{const b=await chromium.launch();
for (const w of [1920,1280,1024]){const p=await b.newPage({viewport:{width:w,height:1300}});
await p.goto('https://store.steampowered.com/developer/klei',{waitUntil:'networkidle',timeout:60000});await p.waitForTimeout(1500);
await p.evaluate(([bg,logo,kop,av])=>{document.querySelectorAll('*').forEach(e=>{const s=getComputedStyle(e).backgroundImage;if(s.includes('2253be96'))e.style.backgroundImage=`url(${bg})`;});
document.querySelectorAll('img').forEach(i=>{if(i.src.includes('23089ea2'))i.src=logo;if(i.src.includes('2253be96'))i.style.visibility='hidden';});
document.querySelector('.background_header_ctn').style.backgroundImage=`url(${kop})`;document.querySelector('img.curator_avatar').src=av;
const h=[...document.querySelectorAll('*')].find(e=>e.children.length==0&&e.textContent.trim()=='Klei'&&e.getBoundingClientRect().top<250);if(h)h.textContent='Dortus';
document.querySelectorAll('a').forEach(a=>{const r=a.getBoundingClientRect();if(r.top>150&&r.top<300&&a.querySelector('svg'))a.style.display='none';if(/Official Website/.test(a.textContent)){a.innerHTML='dortus.com';a.style.display='';}});
document.querySelectorAll('*').forEach(e=>{if(e.children.length==0&&/^[\d,]+$/.test(e.textContent.trim())&&e.getBoundingClientRect().top<320)e.textContent='0';});
},[d(BG),d(LOGO),d(KOP),d('avatar-184.png')]);
await p.waitForTimeout(1000);await p.screenshot({path:`${M}proef/${OUT}-${w}.png`,clip:{x:0,y:100,width:w,height:1200}});await p.close();}
await b.close();})();
