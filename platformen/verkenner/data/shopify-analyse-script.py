import json,datetime,statistics as st,collections
d=[x for x in json.load(open('/tmp/claude-0/sh/s6000.json')) if x.get('ok') and x.get('launched')]
for x in d: x['dt']=datetime.datetime.strptime(x['launched'],'%B %d, %Y')
print('ok met datum',len(d))
c=collections.Counter(x['dt'].strftime('%Y') for x in d); print(sorted(c.items()))
c=collections.Counter(x['dt'].strftime('%Y-%m') for x in d if x['dt'].year>=2025); print(sorted(c.items()))
def paid(p):
    p=(p or '').lower()
    return not (p.startswith('free free') or p=='free')
def rep(name,g):
    r=[x['reviews'] for x in g]
    if not g: return
    print(f"{name}: n={len(g)} mediaan rev={st.median(r)} 0rev={sum(v==0 for v in r)/len(g):.0%} >=5={sum(v>=5 for v in r)/len(g):.0%} >=10={sum(v>=10 for v in r)/len(g):.0%} >=25={sum(v>=25 for v in r)/len(g):.0%} >=50={sum(v>=50 for v in r)/len(g):.0%} betaald={sum(paid(x['price']) for x in g)/len(g):.0%}")
for a,b,n in [((2026,5,1),(2026,9,1),'mei-aug 2026'),((2025,11,1),(2026,5,1),'nov25-apr26'),((2025,1,1),(2025,11,1),'jan-okt 2025'),((2024,1,1),(2025,1,1),'2024'),((2020,1,1),(2024,1,1),'2020-2023')]:
    g=[x for x in d if datetime.datetime(*a)<=x['dt']<datetime.datetime(*b)]; rep(n,g)
