# Maakt per richting een scherm op ware grootte (1920x1080, schaal 100%): strip uit het sfeerbeeld op halve hoogte, echte UI-maten.
import re,sys,pathlib
here=pathlib.Path(__file__).parent
def strip(naam):
    s=(here.parent/f'{naam}-sfeer.html').read_text()
    m=re.search(r'<svg class="strip".*?</svg>',s,re.S).group(0)
    m=m.replace('viewBox="480 90 960 210"','viewBox="0 90 1920 210"')
    return m
CSS='''html,body{margin:0;width:1920px;height:1080px;overflow:hidden;font-family:"Segoe UI",system-ui,sans-serif}
.desk{position:absolute;inset:0;background:radial-gradient(1300px 700px at 60% 20%,#3d7fd0,#1d4f9c 55%,#123a7a)}
.win{position:absolute;left:300px;top:36px;width:1320px;height:930px;background:#fff;border-radius:8px;box-shadow:0 18px 50px #0006;overflow:hidden;color:#222}
.bar{height:34px;background:#f3f3f3;border-bottom:1px solid #ddd;display:flex;align-items:center;padding:0 14px;font-size:12px;color:#333}
.bar b{margin-left:auto;font-weight:400;letter-spacing:14px;color:#555}
.doc{padding:48px 220px;font:16px/1.8 "Segoe UI",sans-serif;color:#333}
.doc h1{font-size:26px;margin:0 0 18px}
.doc p{margin:0 0 16px}
svg.strip{position:absolute;left:0;bottom:48px;width:1920px;height:210px}
.task{position:absolute;left:0;right:0;bottom:0;height:48px;background:#202020f2;border-top:1px solid #ffffff14;display:flex;justify-content:center;align-items:center;gap:12px}
.task span{width:28px;height:28px;border-radius:6px;background:#ffffff22}
.task .s{width:200px;border-radius:15px;background:#ffffff18;color:#ddd;font-size:13px;line-height:30px;padding-left:28px;box-sizing:border-box;height:30px}
.task .on{box-shadow:0 3px 0 -1px #6cb8ff}
.clock{position:absolute;right:14px;bottom:8px;color:#fff;font-size:12px;text-align:right;line-height:1.35}
.hud{position:absolute;right:20px;bottom:262px;color:#ffe9c2;font:600 14px Georgia,serif;text-align:right;text-shadow:0 1px 4px #000,0 0 10px #000a}
.hud small{display:block;font:400 11px Georgia,serif;letter-spacing:.12em;text-transform:uppercase;opacity:.85}
.paper{position:absolute;background:#f3e8cf;color:#3b2a1a;font:14px/1.4 Georgia,serif;box-shadow:0 6px 16px #0007;border-radius:2px}
.paper em{display:block;font:600 10px Georgia,serif;letter-spacing:.16em;text-transform:uppercase;color:#8a6410;font-style:normal;margin-bottom:3px}
.btn{display:inline-block;margin:8px 6px 0 0;padding:4px 10px;border:1.5px solid #6b4a24;border-radius:3px;font:13px Georgia,serif;color:#3b2a1a;background:#fff8e6}
.btn.k{background:#6b4a24;color:#fff3dc}
.menu{position:absolute;right:16px;bottom:62px;display:flex;gap:6px}
.menu i{width:30px;height:30px;border-radius:50%;background:#f3e8cfee;box-shadow:0 2px 6px #0008;display:grid;place-items:center;font:600 14px Georgia,serif;color:#3b2a1a;font-style:normal}
'''
TEKST='''<div class="doc"><h1>Q4 planning: notes for Thursday</h1><p>We start the week with the vendor review. The main question is whether we keep the current hosting contract or move the two smaller services to the new provider before January. Costs are roughly equal; the difference is support hours.</p><p>Second, the hiring plan. Two roles are open. The first interview round is booked for next Tuesday and Wednesday, and we still need one more person on the panel for the design role.</p><p>Third, the budget for events. Last year we spent most of it in the spring; this year we want to spread it out and keep a small reserve for things that come up during the year.</p><p>Action items: confirm the panel, send the vendor the questions list, and update the shared sheet with the October numbers before the meeting.</p><p>Open questions: who owns the reserve, and do we need sign-off from finance for anything under the limit?</p></div>'''
def page(naam,titel,ui):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="desk"></div><div class="win"><div class="bar">{titel}<b>–▢✕</b></div>{TEKST}</div>
{ui if naam!='hol' else ui.split('</div>',1)[0]+'</div>'}{strip(naam)}{ui if naam!='hol' else ui.split('</div>',1)[1]}
<div class="task"><span style="background:#3aa0ff"></span><span class="s">Search</span><span style="background:#f2c94c"></span><span class="on" style="background:#2b6fdb"></span><span style="background:#1e7a3c"></span><span class="on" style="background:#7a2c3a"></span></div>
<div class="clock">17:42<br>9-11-2026</div></body></html>'''
UI={
'kerker':('Q4 planning.docx · Word','''<div class="hud"><small>Floor 14 · The Salt Mines</small>Party of 3 · 2 h 10 min underground today</div>
<div class="paper" style="left:1120px;bottom:268px;width:230px;padding:10px 12px;transform:rotate(-2deg)"><em>Found while you worked</em><b>Lantern of the Deep Choir</b><br>Lights two extra floors.</div>
<div class="menu"><i>⚔</i><i>✦</i><i>≡</i></div>'''),
'hol':('Q4 planning.docx · Word','''<div style="position:absolute;left:0;right:0;bottom:48px;height:186px;background:linear-gradient(#6b4328 0 25%,#5a3720 25% 55%,#482a17 55% 78%,#371f10 78%);border-top:6px solid #4f7a32;z-index:-0"></div><div class="hud"><small>The Hollow · depth 3</small>148 gold · 6 heroes in today · 2 fled</div>
<div class="paper" style="left:930px;bottom:262px;width:250px;padding:10px 12px;transform:rotate(1.5deg)"><em style="color:#9b2c1c">Returning · visit 4</em><b>Bram the Thrice-Fled</b><br>Scar over the left eye. Grudge: slimes.</div>
<div class="paper" style="right:16px;bottom:58px;padding:6px 8px;display:flex;gap:6px;font-size:12px;text-align:center"><div style="width:52px">⛏<br>Dig 3</div><div style="width:52px">▲<br>Spikes 12</div><div style="width:52px">●<br>Slime 20</div><div style="width:52px">☠<br>Bones 30</div></div>'''),
'karavaan':('Q4 planning.docx · Word','''<div class="hud"><small>Tuesday · day 2 of 5</small>214 km to Varenna · 3 wagons · 86 silver</div>
<div class="paper" style="left:880px;bottom:250px;width:300px;padding:12px 14px;transform:rotate(-2deg)"><span style="position:absolute;right:10px;top:6px;font:12px Georgia;color:#8a6410">later ✕</span><em>Postcard · near Ostwick</em>The bridge is gone. The ferryman wants 12 silver, or we take the hill road: one day longer, but the hill villages buy wool.<br><span class="btn k">Pay the ferry</span><span class="btn">Hill road</span></div>
<div class="menu"><i>⚖</i><i>✉</i><i>≡</i></div>'''),
}
for n,(t,u) in UI.items():
    (here/f'{n}-scherm.html').write_text(page(n,t,u))
