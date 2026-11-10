// Proef GitHub: repopagina Rollwright zoals hij wordt na stap 1 tot 3 van accounts/github.md
// (avatar v2, About met beschrijving, website en topics). Alleen in de eigen browser vervangen. Abel, 10 nov 2026 run 7.
const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const av='data:image/png;base64,'+fs.readFileSync(M+'avatar-512-v2.png').toString('base64');
(async()=>{const b=await chromium.launch();
for (const scheme of ['light','dark']){const p=await b.newPage({viewport:{width:1280,height:560},colorScheme:scheme});
await p.goto('https://github.com/thijsduinhouwer2002-coder/rollwright',{waitUntil:'domcontentloaded',timeout:60000});await p.waitForTimeout(3000);
const r=await p.evaluate((av)=>{let n=0;document.querySelectorAll('img').forEach(i=>{if(/\/u\/295318200|identicon/.test(i.src)||/thijsduinhouwer/.test(i.alt||'')){i.src=av;i.srcset='';n++;}});
 const el=[...document.querySelectorAll('*')].filter(x=>/^\s*No description, website, or topics provided\.?\s*$/.test(x.textContent)).pop();
 let ok=false;
 if(el){ok=true;let q=el.parentElement;for(let k=0;k<3&&q;k++){q.style.fontStyle="normal";q=q.parentElement;}
  const topics=['obsidian-plugin','obsidian','dice','ttrpg','dnd'].map(t=>`<a class="topic-tag topic-tag-link" style="display:inline-block;margin:0 4px 6px 0;padding:0 10px;font-size:12px;line-height:22px;border-radius:2em;background:var(--bgColor-accent-muted,#ddf4ff);color:var(--fgColor-accent,#0969da);font-weight:500;text-decoration:none">${t}</a>`).join('');
  el.outerHTML=`<p class="f4 my-3" style="font-style:normal">Roll dice right in your Obsidian notes: click to reroll, roll on your own tables and lists, a roll log per session.</p>
  <div class="my-3 d-flex flex-items-center"><a style="font-weight:600;color:var(--fgColor-accent,#0969da);font-size:14px" href="#">dortus.com/rollwright/</a></div>
  <div class="my-3">${topics}</div>`;}
 return [n,ok];},av);
console.log(scheme,JSON.stringify(r));await p.waitForTimeout(500);await p.screenshot({path:`${M}proef/github-repo-${scheme}.png`});await p.close();}
await b.close();})();
