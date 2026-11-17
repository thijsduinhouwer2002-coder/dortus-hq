import json,csv,sys,statistics as st
from datetime import datetime,date
S=sys.argv[1]
kaart={x['appid']:x for x in csv.DictReader(open('/home/claude/dortus-hq/platformen/verkenner/data/steam-desktop-kaart-2026-11-16.csv'))}
vol={x['appid']:x['volgers'] for x in csv.DictReader(open('/home/claude/dortus-hq/platformen/steam/marketing/data/volgers-binnenkort-2026-11-16.csv'))}
for l in open('/home/claude/dortus-hq/platformen/verkenner/data/steam-volgers-2026-11-16.jsonl'):
    j=json.loads(l)
    if j.get('volgers') is not None: vol.setdefault(j['appid'],str(j['volgers']))
fests=[date(2024,2,5),date(2024,6,10),date(2024,10,14),date(2025,2,24),date(2025,6,9),date(2025,10,13),date(2026,2,23),date(2026,6,15),date(2026,10,19)]
def pd(s):
    for f in ('%b %d, %Y','%d %b, %Y','%B %d, %Y'):
        try: return datetime.strptime(s,f).date()
        except: pass
    return None
rows=[]
for l in open(S+'/apps.jsonl'):
    j=json.loads(l)
    dr=j.get('demo_release')
    if not dr: continue
    d=pd(dr.get('date','')); 
    if not d or dr.get('coming_soon'): continue
    rel=j.get('release') or {}
    r=None if rel.get('coming_soon') else pd(rel.get('date',''))
    k=kaart[j['appid']]
    # eerste Next Fest op of na demodatum, vóór de uitgave
    F=next((f for f in fests if f>=d),None)
    if F and r and r<F: F=None
    gap=(F-d).days if F else None
    rows.append(dict(appid=j['appid'],naam=j['naam'],demo=str(d),uit=str(r) if r else 'binnenkort',fest=str(F) if F else '',dagen_voor_fest=gap if gap is not None else '',reviews=k['reviews_totaal'],volgers=vol.get(j['appid'],''),prijs=k['prijs_usd'],lijkt_op_hats=k['lijkt_op_hats']))
w=csv.DictWriter(open(S+'/demo-timing.csv','w'),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
def band(g):
    if g=='' : return 'geen Next Fest tussen demo en uitgave'
    if g<=3: return '0-3 dagen voor fest'
    if g<=21: return '4-21 dagen'
    if g<=90: return '22-90 dagen'
    return '91+ dagen'
print('n met demodatum',len(rows))
for soort in ('uit','binnenkort'):
    print('==',soort)
    groups={}
    for x in rows:
        isuit = x['uit']!='binnenkort'
        if (soort=='uit')!=isuit: continue
        if isuit and x['uit']>'2026-09-16': continue  # minstens 2 maanden uit
        if isuit and x['demo']<'2024-07-31': continue
        val=int(x['reviews'] or 0) if isuit else (int(x['volgers']) if x['volgers'] not in ('','None') else None)
        if val is None: continue
        groups.setdefault(band(x['dagen_voor_fest']),[]).append(val)
    for b,v in sorted(groups.items()):
        v=sorted(v); 
        print(f"{b:45s} n={len(v):3d} mediaan={st.median(v):7.1f} p75={v[int(len(v)*0.75)] if v else 0:6d} aandeel>=100={sum(1 for a in v if a>=100)/len(v):.0%}")
