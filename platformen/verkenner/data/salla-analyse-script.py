# Vera 15 nov 2026: analyse van salla-haal-script.py. Lichting = maand van de oudste review (alleen apps met 1+ review).
import json,sys,statistics as st,collections as C
a=json.load(open(sys.argv[1]))
print('apps',len(a),'zonder review',sum(1 for x in a if not x['reviews']['count']))
betaald=lambda x: not x['plan'].get('is_free')
print('betaald',sum(betaald(x) for x in a))
eerste=C.Counter((x.get('oudste') or '')[:7] for x in a if x.get('oudste'))
print('apps per maand eerste review:',[(k,eerste[k]) for k in sorted(eerste) if k>='2025-01'])
comp=C.Counter(x['company']['name'] for x in a)
cfirst={}
for x in a:
    if x.get('oudste'):
        c=x['company']['name']; cfirst[c]=min(cfirst.get(c,'9'),x['oudste'])
def s(lst,n):
    v=[x['reviews']['count'] for x in lst]
    if not v: print(n,0);return
    print(f"{n}: n={len(v)} mediaan={st.median(v)} 5+={sum(y>=5 for y in v)} 10+={sum(y>=10 for y in v)} ({100*sum(y>=10 for y in v)/len(v):.0f}%) 30+={sum(y>=30 for y in v)} betaald={sum(betaald(x) for x in lst)} betaald10+={sum(1 for x in lst if betaald(x) and x['reviews']['count']>=10)}")
for lo,hi,n in [('2024-01','2024-07','2024 H1'),('2024-07','2025-01','2024 H2'),('2025-01','2025-07','2025 H1'),('2025-07','2026-01','2025 H2'),('2026-01','2026-05','jan-apr 2026'),('2026-05','2026-09','mei-aug 2026'),('2026-09','2027','sep-nov 2026')]:
    l=[x for x in a if x.get('oudste') and lo<=x['oudste']<hi]; s(l,n)
    s([x for x in l if cfirst[x['company']['name']]>=lo],'   nieuwe makers')
print('top jonge (eerste review >= 2025-05):')
for x in sorted([x for x in a if (x.get('oudste') or '')>='2025-05'],key=lambda x:-x['reviews']['count'])[:15]:
    print(' ',x['reviews']['count'],x['oudste'],x['id'],x['company']['name'],'| apps',comp[x['company']['name']],'|',x['plan'].get('prefix'),x['plan'].get('is_free'))
rv=C.Counter(d[:7] for x in a for d in x.get('revdata1',[]))
print('top makers',comp.most_common(8))
