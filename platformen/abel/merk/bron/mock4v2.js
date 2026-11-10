const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const av='data:image/png;base64,'+fs.readFileSync(M+'avatar-512-v2.png').toString('base64');
(async()=>{const b=await chromium.launch();
for (const scheme of ['light','dark']){const p=await b.newPage({viewport:{width:1280,height:520},colorScheme:scheme});
await p.goto('https://github.com/thijsduinhouwer2002-coder/rollwright',{waitUntil:'domcontentloaded',timeout:60000});await p.waitForTimeout(2500);
const n=await p.evaluate((av)=>{let n=0;document.querySelectorAll('img').forEach(i=>{if(/avatars\.githubusercontent\.com\/u\/295318200|identicon|\/u\/295318200/.test(i.src)||/thijsduinhouwer/.test(i.alt||'')){i.src=av;i.srcset='';n++;}});
const ab=[...document.querySelectorAll('div,p,span')].filter(x=>x.children.length==0).find(x=>/No description/.test(x.textContent));if(ab)ab.textContent='Roll dice right in your Obsidian notes: click to reroll, roll on your own tables and lists, a roll log per session.';return n;},av);
console.log(scheme,n);await p.screenshot({path:`${M}proef/github-repo-${scheme}.png`});await p.close();}
await b.close();})();
