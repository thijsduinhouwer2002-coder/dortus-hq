import json,statistics as st
from datetime import datetime
sc={x['sc']:x for x in json.load(open('platformen/verkenner/data/shopify-storecensus-2026-11-07.json'))}
sh=[x for x in json.load(open('platformen/verkenner/data/shopify-storecensus-shopifypaginas-2026-11-07.json')) if x['launched']]
def dt(s): return datetime.strptime(s,'%B %d, %Y')
rows=[]
for x in sh:
    c=sc[x['slug']]; rows.append(dict(slug=x['slug'],l=dt(x['launched']),r=x['reviews'],i=c['installs'],d30=c['d30'] if c['d30dir']=='gained' else -(c['d30'] or 0),dev=x['dev'],price=x['price']))
def grp(name,f):
    g=[r for r in rows if f(r)]
    if not g: print(name,0);return
    ratios=[r['i']/r['r'] for r in g if r['r']>0]
    print(f"{name}: n={len(g)} med installs={st.median([r['i'] for r in g])} med reviews={st.median([r['r'] for r in g])} 0rev={sum(r['r']==0 for r in g)} ({100*sum(r['r']==0 for r in g)/len(g):.0f}%) 100+={sum(r['i']>=100 for r in g)} | installs/review med={st.median(ratios) if ratios else None:.1f} q1={st.quantiles(ratios,n=4)[0] if len(ratios)>3 else 0:.1f} q3={st.quantiles(ratios,n=4)[2] if len(ratios)>3 else 0:.1f} (n={len(ratios)})")
grp('alles',lambda r:True)
grp('voor 2020',lambda r:r['l'].year<2020)
grp('2020-2023',lambda r:2020<=r['l'].year<=2023)
grp('2024',lambda r:r['l'].year==2024)
grp('2025',lambda r:r['l'].year==2025)
grp('jan-apr 2026',lambda r:r['l'].year==2026 and r['l'].month<=4)
grp('mei-aug 2026',lambda r:r['l'].year==2026 and 5<=r['l'].month<=8)
grp('sep-okt 2026',lambda r:r['l'].year==2026 and r['l'].month>=9)
# by installs band, among 2025-2026
for lo,hi in [(24,100),(100,300),(300,1000),(1000,10**7)]:
    grp(f'2025+ installs {lo}-{hi}',lambda r,lo=lo,hi=hi:r['l'].year>=2025 and lo<=r['i']<hi)
# reviews needed: among 2025+ apps with 100-200 installs, reviews dist
g=[r['r'] for r in rows if r['l'].year>=2025 and 100<=r['i']<200]; print('2025+ 100-199 installs, reviews:',sorted(g))
print('\nmei-aug 2026 apps met 100+ installs:')
for r in sorted([r for r in rows if r['l'].year==2026 and 5<=r['l'].month<=8 and r['i']>=100],key=lambda r:-r['i']): print(' ',r['slug'],r['l'].date(),r['i'],'inst',r['r'],'rev',r['dev'],'|',(r['price'] or '')[:50])
json.dump([dict(r,l=r['l'].strftime('%Y-%m-%d')) for r in rows],open('platformen/verkenner/data/shopify-storecensus-gekoppeld-2026-11-07.json','w'),indent=0)
