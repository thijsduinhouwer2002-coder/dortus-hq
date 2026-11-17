# Fenna verhaal 22: winkeltekst van bureaubladspellen ophalen (appdetails), rustig.
import csv, json, time, sys, urllib.request, os
KAART='platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv'
OUT=sys.argv[1]
r=list(csv.DictReader(open(KAART)))
s=[x for x in r if x['binnenkort']=='False' and int(x['reviews_totaal'] or 0)>=30 and x['soort_spel']!='programma of hulpmiddel']
have={}
if os.path.exists(OUT):
    for l in open(OUT): d=json.loads(l); have[d['appid']]=1
f=open(OUT,'a')
for x in s:
    a=x['appid']
    if a in have: continue
    u=f'https://store.steampowered.com/api/appdetails?appids={a}&l=english&cc=us'
    for t in range(3):
        try:
            d=json.load(urllib.request.urlopen(u,timeout=30)); break
        except Exception as e:
            time.sleep(20); d=None
    if not d or not d.get(a,{}).get('success'): continue
    g=d[a]['data']
    f.write(json.dumps({'appid':a,'naam':g.get('name'),'short':g.get('short_description',''),'about':g.get('about_the_game',''),'detailed':g.get('detailed_description',''),'release':g.get('release_date',{}).get('date'),'genres':[z['description'] for z in g.get('genres',[])],'reviews':x['reviews_totaal'],'pct':x['pct_positief'],'prijs':x['prijs_usd'],'soort':x['soort_spel']})+'\n'); f.flush()
    time.sleep(1.6)
