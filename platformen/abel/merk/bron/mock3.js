const { chromium } = require('playwright');const fs=require('fs');
const M='/home/claude/dortus-hq/platformen/abel/merk/';
const av='data:image/png;base64,'+fs.readFileSync(M+'avatar-184.png').toString('base64');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:700}});
await p.goto(process.argv[2],{waitUntil:'networkidle',timeout:60000});await p.waitForTimeout(1500);
const info=await p.evaluate((av)=>{
 const q=s=>document.querySelector(s);const out=[];
 document.querySelectorAll('.playerAvatarAutoSizeInner img, .playerAvatar img').forEach(i=>{out.push('img '+i.className);i.src=av;i.srcset='';});
 document.querySelectorAll('.profile_avatar_frame').forEach(e=>e.remove());
 const n=q('.actual_persona_name');if(n)n.textContent='Dortus';
 const h=q('.header_real_name');if(h)h.innerHTML='<img class="profile_flag" src="https://community.fastly.steamstatic.com/public/images/countryflags/nl.gif"> Netherlands';
 const s=q('.profile_summary');if(s)s.innerHTML="Dortus makes small games and focused tools.<br>Our first game, Hats of the Fallen, is a tiny dungeon on your taskbar: heroes come for the slime's treasure, and he keeps their hats.<br>Made by Thijs in the Netherlands. Questions or bugs: thijs@dortus.com";
 const bg=q('.profile_page.has_profile_background');if(bg){bg.style.backgroundImage='none';bg.classList.remove('has_profile_background');}
 document.querySelectorAll('.profile_animated_background, video').forEach(e=>e.remove());
 document.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.width>1000&&getComputedStyle(e).backgroundImage.includes('url('))e.style.backgroundImage='none';});document.body.style.background='#1b2838';
const lvl=q('.persona_level');if(lvl)lvl.style.visibility='hidden';
 document.querySelectorAll('.profile_header_badgeinfo, .profile_customization_area, .profile_rightcol, .profile_leftcol').forEach(e=>e.style.visibility='hidden');
 return out.join(',')+' '+!!n+' '+!!s;},av);
console.log(info);await p.screenshot({path:process.argv[3],clip:{x:0,y:100,width:1280,height:420}});await b.close();})();
