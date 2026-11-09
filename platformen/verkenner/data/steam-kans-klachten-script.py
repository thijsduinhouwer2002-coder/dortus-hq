"""Negatieve reviews (meest nuttig) van de openbare communitypagina, per app, en een telling van soorten klachten.
Gebruik: python3 -I steam-kans-klachten-script.py <uitbestand.json> appid appid ..."""
import re,html,json,sys,time,urllib.request
KL={'bugs/crash/save weg':r'bug|crash|glitch|broken|save (file|got|was)|lost (my )?(save|progress)|freez',
'vertaling slecht':r'translat|machine|mtl|english is|grammar',
'balans/grind/te traag':r'balanc|grind|tedious|slow|stuck|progress(ion)? (is|feels)|too long|wall',
'te veel micromanagement/klikken':r'micro|manag|click(ing)? (too|a lot)|have to (click|manage)|not (really )?idle|active',
'te weinig inhoud/kort':r'content|short|nothing to do|repetitive|boring|shallow|empty',
'neemt scherm of pc in beslag':r'cpu|gpu|fps|performance|lag|ram|memory|screen space|resolution|window|monitor|taskbar|fullscreen',
'betaalmodel/dlc/winkel':r'dlc|microtransaction|premium|pay|cash|gacha|mtx|price',
'onaf/early access/beloftes':r'early access|unfinished|beta|abandon|no update|dev(s|eloper)? (left|gone)|rushed'}
out=sys.argv[1];R={}
for a in sys.argv[2:]:
    h=urllib.request.urlopen(urllib.request.Request(f'https://steamcommunity.com/app/{a}/negativereviews/?browsefilter=toprated&l=english',headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf-8','replace')
    t=[re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',html.unescape(m))).strip() for m in re.findall(r'apphub_CardTextContent">\s*<div class="date_posted">[^<]*</div>(.*?)</div>',h,re.S)]
    R[a]={'n':len(t),'tel':{k:sum(1 for x in t if re.search(rx,x.lower())) for k,rx in KL.items()},'teksten':t}
    print(a,len(t),R[a]['tel']);time.sleep(2)
json.dump(R,open(out,'w'))
