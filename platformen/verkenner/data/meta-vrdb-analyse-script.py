import json,statistics as st,collections
rs={};
for l in open('meta-horizon-vrdb-2026-11-08.jsonl'):
    x=json.loads(l); rs[x['id']]=x
R=list(rs.values()); print('uniek',len(R))
def m(d): return (d.get('release_date_clean') or '')[:7]
c=collections.Counter(m(x) for x in R); print(sorted(c.items()))
def stats(L,lab):
    if not L: print(lab,0); return
    rc=sorted((x['rating_count'] or 0) for x in L)
    n=len(rc); med=st.median(rc)
    p=lambda t: round(100*sum(1 for v in rc if v>=t)/n,1)
    print(f"{lab}: n={n} mediaan={med} 0={p(0)-p(1):.0f}% 5+={p(5)}% 10+={p(10)}% 50+={p(50)}% 100+={p(100)}% top={rc[-5:]}")
coh=[x for x in R if '2026-05'<=m(x)<='2026-08']
stats(coh,'alles mei-aug 2026')
paid=[x for x in coh if (x['usd'] or 0)>0]; free=[x for x in coh if not (x['usd'] or 0)]
stats(paid,'betaald'); stats(free,'gratis')
for cat in ['Games','Apps']:
    stats([x for x in paid if x['category']==cat],'betaald '+cat)
stats([x for x in R if '2025-11'<=m(x)<='2026-02' and (x['usd'] or 0)>0],'betaald nov25-feb26')
pr=[x['usd']/100 for x in paid]; print('mediaanprijs',st.median(pr))
# geschatte verkoop met 110 per rating
s=sorted(paid,key=lambda x:-(x['rating_count'] or 0))
for x in s[:12]: print(x['rating_count'],x['usd'],x['category'],x['name'],'|',x['developer'],m(x))
# devs: number of apps per dev in whole store sample
dc=collections.Counter(x['developer'] for x in coh); print('makers',len(dc),'met 1 app',sum(1 for v in dc.values() if v==1))
