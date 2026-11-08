const {chromium}=require('playwright');const fs=require('fs');
const OUT=process.argv[2]||'premiere-uxp-nieuw.json';
(async()=>{const b=await chromium.launch();const p=await b.newPage();const items={};
p.on('response',async r=>{if(r.url().includes('ccext-public.adobe.io/unauth/v3/extensions')){try{const d=await r.json();for(const it of d.items)items[it.id]=it;}catch(e){}}});
await p.goto('https://exchange.adobe.com/apps/browse/cc?product=PPRO&listingType=plugins&sort=MOST_RECENT',{waitUntil:'networkidle',timeout:60000}).catch(e=>{});
await p.waitForTimeout(4000);
for(let i=0;i<130;i++){
  const n=Object.keys(items).length; fs.writeFileSync(OUT,JSON.stringify(Object.values(items)));
  const nxt=p.getByText('Next',{exact:true}).last();
  try{await nxt.click({timeout:8000});}catch(e){console.log('stop',i,e.message.slice(0,80));break;}
  await p.waitForTimeout(2500);
  if(i%10==0)console.log(i,Object.keys(items).length);
}
fs.writeFileSync(OUT,JSON.stringify(Object.values(items)));console.log('klaar',Object.keys(items).length);await b.close();})();
