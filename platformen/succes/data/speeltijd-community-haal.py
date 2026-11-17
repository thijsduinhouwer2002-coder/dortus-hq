# Fenna verhaal 22: meest behulpzame reviews (Engelse filter) van de Steam-communitypagina, met speeltijd.
# appreviews stuurt door naar de voorpagina (zie steam-desktop-haal-script.py), dus de openbare communitypagina, rustig.
# Gebruik: python3 -I speeltijd-community-haal.py <appids-bestand (jsonl met appid) of komma-lijst> <uitmap> <pagina's>
import json, re, html, sys, time, os, urllib.request, urllib.parse
src, OUT, PAGES = sys.argv[1], sys.argv[2], int(sys.argv[3])
apps=[json.loads(l)['appid'] for l in open(src)] if os.path.exists(src) else src.split(',')
os.makedirs(OUT,exist_ok=True)
def get(u):
    for t in range(3):
        try: return urllib.request.urlopen(u,timeout=30).read().decode('utf-8','replace')
        except Exception: time.sleep(10)
    return ''
def parse(h):
    out=[]
    for card in h.split('class="apphub_Card ')[1:]:
        t=re.search(r'<div class="title">([^<]*)</div>',card)
        hr=re.search(r'<div class="hours">\s*([\d,.]+) hrs on record(?:\s*\(([\d,.]+) hrs at review time\))?',card)
        dp=re.search(r'<div class="date_posted">Posted: ([^<]*)</div>',card)
        card=re.sub(r'<div class="date_posted">.*?</div>','',card,flags=re.S)
        tx=re.search(r'<div class="apphub_CardTextContent">(.*?)</div>',card,re.S)
        nh=re.search(r'([\d,]+) (?:people|person) found this review helpful',card)
        if not t: continue
        txt=tx.group(1) if tx else ''
        txt=html.unescape(re.sub(r'<[^>]+>',' ',txt)); txt=re.sub(r'\s+',' ',txt).strip()
        f=lambda s: float(s.replace(',','')) if s else None
        out.append({'up':t.group(1).strip()=='Recommended','uur':f(hr.group(1)) if hr else None,'uur_bij_review':f(hr.group(2)) if hr else None,
                    'datum':dp.group(1) if dp else None,'nuttig':int(nh.group(1).replace(',','')) if nh else 0,'tekst':txt[:2000]})
    return out
for a in apps:
    if os.path.exists(f'{OUT}/{a}.json'): continue
    revs=[]; h=get(f'https://steamcommunity.com/app/{a}/reviews/?browsefilter=toprated&p=1&l=english')
    for p in range(1,PAGES+1):
        r=parse(h); revs+=r
        cur=re.search(r'name="userreviewscursor" value="([^"]*)"',h)
        if not r or not cur or p==PAGES: break
        q=urllib.parse.urlencode({'userreviewscursor':cur.group(1),'userreviewsoffset':10*p,'p':p+1,'numperpage':10,'browsefilter':'toprated','l':'english','appHubSubSection':10,'filterLanguage':'default','searchText':'','maxInappropriateScore':100,'forceanon':1})
        time.sleep(1.2); h=get(f'https://steamcommunity.com/app/{a}/homecontent/?{q}')
    json.dump({'appid':a,'reviews':revs},open(f'{OUT}/{a}.json','w'))
    time.sleep(1.0)
