# Analyse BOOTH-tools per lichting op likes (wish_lists_count). Gebruik: python3 booth-analyse-script.py BESTAND VAN TOT
import json,sys,statistics as st,re
from collections import Counter
f,a,b=sys.argv[1:4]
rows=[json.loads(l) for l in open(f)]
ok=[r for r in rows if r.get('ok') and r.get('published')]
sel=[r for r in ok if a<=r['published'][:10]<=b and r.get('cat')=='3Dツール・システム']
print('regels',len(rows),'leesbaar',len(ok),'tools in periode',len(sel), 'andere cat',Counter(r.get('cat') for r in ok if a<=r['published'][:10]<=b and r.get('cat')!='3Dツール・システム').most_common(3))
def p(r):
    ps=[x for x in (r.get('prices') or []) if isinstance(x,int)]
    return min(ps) if ps else 0  # laagste prijs: gratis+steunvariant telt als gratis
paid=[r for r in sel if p(r)>0]; free=[r for r in sel if p(r)==0]
for naam,g in [('betaald',paid),('gratis',free)]:
    c=sorted(r['likes'] or 0 for r in g); n=len(c)
    if not n: continue
    print(f"\n{naam}: n={n} mediaan likes={st.median(c)} 10+={sum(x>=10 for x in c)/n:.0%} 50+={sum(x>=50 for x in c)/n:.0%} 100+={sum(x>=100 for x in c)/n:.0%} 500+={sum(x>=500 for x in c)/n:.0%} max={max(c)}")
    for r in sorted(g,key=lambda r:-(r['likes'] or 0))[:10]: print('  ',r['likes'],p(r),r['published'][:10],r['shop'],'|',r['name'][:70])
print('\nmediaanprijs betaald ¥',st.median([p(r) for r in paid]) if paid else None)
print('per maand',sorted(Counter(r['published'][:7] for r in sel).items()))
print('winkels',len(set(r['shop'] for r in sel)),Counter(r['shop'] for r in sel).most_common(4))
