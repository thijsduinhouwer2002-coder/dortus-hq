// Superhive: banner (uitsnede van Mila's Steam-achtergrond v3, scherp opnieuw getekend uit de svg) en proef op een echte openbare winkelpagina.
// Alleen in de eigen browser vervangen, er wordt niets verstuurd. Abel, 10 nov 2026.
const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const Y0=+(process.env.Y0||270); // bovenrand van de uitsnede in de 1920x1200-tekening
(async()=>{const b=await chromium.launch();
// 1. svg op 2400x1500 tekenen, strook van 2400x660 (verhouding 1200x330 van Superhive) uitsnijden
{const p=await b.newPage({viewport:{width:2400,height:1500}});
const svg=fs.readFileSync(M+'steam-achtergrond-1920-v3.svg','utf8');
await p.setContent(`<html><body style="margin:0"><img id=i src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}" style="width:2400px;height:1500px;display:block"></body></html>`);
await p.waitForTimeout(500);
await p.screenshot({path:M+'superhive-banner-2400x660.png',clip:{x:0,y:Math.round(Y0*1.25),width:2400,height:660}});
await p.close();}
const d=f=>'data:image/png;base64,'+fs.readFileSync(M+f).toString('base64');
const ban=d('superhive-banner-2400x660.png'),av=d('avatar-512-v2.png');
for(const [w,h,naam,mob] of [[1920,760,'1920',0],[1280,700,'1280',0],[390,700,'telefoon',1]]){
const p=await b.newPage(mob?{viewport:{width:w,height:h},deviceScaleFactor:2,isMobile:true}:{viewport:{width:w,height:h},deviceScaleFactor:1});
await p.goto('https://superhivemarket.com/creators/blenderguru',{waitUntil:'load',timeout:60000});await p.waitForTimeout(1500);
await p.evaluate(([ban,av])=>{
document.querySelector('.shop-banner div').style.backgroundImage=`url(${ban})`;
document.querySelectorAll('img.creator-avatar,img.avatar').forEach(i=>i.src=av);
document.querySelector('.shop-title').textContent='Dortus';
document.querySelector('.shop-sub-title').textContent='Small, focused Blender tools that fill a real gap. Questions or a bug? Use Contact Creator.';
const a=document.querySelector('.shop-header-inner ul a');if(a){a.firstChild.textContent='https://dortus.com';}
document.querySelectorAll('.card-title').forEach((t,k)=>{if(k==0)t.textContent='Click Joints';});
document.querySelectorAll('.card-creator-and-category a.text-reset:first-child').forEach(a=>a.textContent='Dortus');
// cookie- of andere meldingen weg
document.querySelectorAll('[class*=cookie],[id*=cookie]').forEach(e=>e.remove());
},[ban,av]);
await p.waitForTimeout(800);
await p.screenshot({path:M+`proef/superhive-winkel-${naam}.png`});
await p.close();}
await b.close();})();
