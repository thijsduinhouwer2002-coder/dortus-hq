// Proef: logo van Mila op de echte afrekenpagina van Polar (Rollwright Skins).
// Eén bezoek, zoals elke koper; niets ingevuld, alleen in de eigen browser het logo vervangen. Abel, 10 nov 2026.
const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const av='data:image/png;base64,'+fs.readFileSync(M+'avatar-512-v2.png').toString('base64');
const url=process.argv[2];
(async()=>{const b=await chromium.launch();
for (const [naam,vp] of [['desktop',{width:1280,height:800}],['telefoon',{width:390,height:844}]]){
const p=await b.newPage({viewport:vp,deviceScaleFactor:2,colorScheme:'light'});
await p.goto(url,{waitUntil:'load',timeout:60000});await p.waitForTimeout(5000);
const info=await p.evaluate(av=>{const out=[];document.querySelectorAll('img').forEach(i=>{const r=i.getBoundingClientRect();out.push([i.src.slice(0,80),Math.round(r.width),Math.round(r.height),Math.round(r.top)]);
 if(/logo\.dev|avatar|organization/i.test(i.src)||(r.width<=64&&r.top<200&&r.width>0)){i.src=av;i.removeAttribute('srcset');}});document.querySelectorAll('div,span').forEach(e=>{const r=e.getBoundingClientRect();if(e.textContent.trim()==='D'&&r.width>10&&r.width<=48&&r.top<200){e.innerHTML=`<img src="${av}" style="width:100%;height:100%;border-radius:50%;display:block">`;e.style.padding='0';out.push(['letter-D vervangen',Math.round(r.width)]);}});
 return out;},av);
console.log(naam,JSON.stringify(info));
await p.waitForTimeout(800);await p.screenshot({path:M+`proef/polar-afrekenen-${naam}.png`});await p.close();}
await b.close();})();
