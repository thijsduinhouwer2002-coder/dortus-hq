// Proef: avatar van Mila op echte openbare pagina's van Blender Extensions en het Obsidian-forum.
// Alleen in de eigen browser vervangen, er wordt niets verstuurd. Abel, 10 nov 2026.
const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const d=f=>'data:image/png;base64,'+fs.readFileSync(M+f).toString('base64');
const av=d('avatar-512-v2.png');
(async()=>{const b=await chromium.launch();
// 1. Blender Extensions: wachtrijpagina van Click Joints
{const p=await b.newPage({viewport:{width:1280,height:900},deviceScaleFactor:2});
await p.goto('https://extensions.blender.org/approval-queue/click-joints/',{waitUntil:'networkidle',timeout:60000});
const n=await p.evaluate(av=>{let n=0;document.querySelectorAll('img').forEach(i=>{if(/blank-profile-pic/.test(i.src)){i.src=av;n++;}});return n;},av);
console.log('blender vervangen',n);
await p.waitForTimeout(800);
await p.screenshot({path:M+'proef/blender-wachtrij-voor-na.png',fullPage:false});
// uitsnede rond de eerste avatar
const r=await p.evaluate(()=>{const i=[...document.querySelectorAll('img.profile-avatar')][0];if(!i)return null;const r=i.getBoundingClientRect();return r&& {x:r.x,y:r.y,w:r.width,h:r.height};});
console.log('blender rect',JSON.stringify(r));
if(r){await p.evaluate(()=>window.scrollTo(0,0));await p.screenshot({path:M+'proef/blender-avatar-uitsnede.png',fullPage:true,clip:{x:Math.max(0,r.x-40),y:r.y+0-80,width:700,height:200}});}
await p.close();}
// 2. Obsidian-forum: de draad van Rollwright, licht en donker
for (const scheme of ['light','dark']){const p=await b.newPage({viewport:{width:1100,height:700},colorScheme:scheme,deviceScaleFactor:2});
await p.goto('https://forum.obsidian.md/t/rollwright-roll-dice-and-random-tables-in-your-notes-where-a-natural-20-lands-in-gold/121721',{waitUntil:'load',timeout:60000});await p.waitForTimeout(4000);
const n=await p.evaluate(av=>{let n=0;document.querySelectorAll('img').forEach(i=>{if(/letter_avatar_proxy\/v4\/letter\/t\/bc79bd/.test(i.src)||(i.alt||'').includes('Thijs.Dortus')){i.src=av;i.removeAttribute('srcset');n++;}});return n;},av);
console.log('obsidian',scheme,'vervangen',n);
await p.waitForTimeout(800);
await p.screenshot({path:M+`proef/obsidian-draad-${scheme}.png`});
await p.close();}
await b.close();})();
