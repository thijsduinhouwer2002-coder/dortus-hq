# Analyse van OpenCart-extensies per lichting. Gebruik: python3 opencart-analyse-script.py BESTAND.jsonl VAN(YYYY-MM-DD) TOT
import json,sys,statistics as st
from datetime import datetime
from collections import Counter
f,a,b=sys.argv[1],sys.argv[2],sys.argv[3]
rows=[json.loads(l) for l in open(f)]
ok=[r for r in rows if r.get('ok')]
def dt(s): return datetime.strptime(s,'%d %b %Y').strftime('%Y-%m-%d')
sel=[r for r in ok if a<=dt(r['created'])<=b]
print('pagina\'s',len(rows),'leesbaar',len(ok),'in periode',len(sel))
def pr(r):
    p=r.get('price') or ''
    try: return float(p.replace('$','').replace(',',''))
    except: return 0.0
paid=[r for r in sel if r['kind']=='Sales' and pr(r)>0]
free=[r for r in sel if r['kind']=='Downloads']
for naam,g in [('betaald',paid),('gratis',free)]:
    c=sorted(r['count'] for r in g)
    if not c: continue
    n=len(c)
    print(f"\n{naam}: n={n} mediaan={st.median(c)} gem={sum(c)/n:.1f} 0={sum(x==0 for x in c)/n:.0%} 1+={sum(x>=1 for x in c)/n:.0%} 5+={sum(x>=5 for x in c)/n:.0%} 10+={sum(x>=10 for x in c)/n:.0%} 20+={sum(x>=20 for x in c)/n:.0%} 100+={sum(x>=100 for x in c)/n:.0%} som={sum(c)}")
    top=sorted(g,key=lambda r:-r['count'])[:8]
    for r in top: print('  ',r['count'],r.get('price'),r['created'],r.get('maker'),'|',(r.get('title') or '')[:70])
if paid:
    ps=[pr(r) for r in paid]; print('\nprijs mediaan',st.median(ps))
    omzet=sum(pr(r)*r['count'] for r in paid); print('bruto omzet alle betaalde in periode $%.0f'%omzet)
    mk=Counter(r.get('maker') for r in paid); print('makers betaald',len(mk),'top',mk.most_common(5))
    nieuw=[r for r in paid if r.get('member_since') and dt(r['member_since'])>=str(int(a[:4])-1)+a[4:]]
    c=sorted(r['count'] for r in nieuw)
    if c: print(f"betaald van nieuwe makers (lid sinds {int(a[:4])-1}{a[4:]}+): n={len(c)} mediaan={st.median(c)} 10+={sum(x>=10 for x in c)} max={max(c)}")
    m=Counter(dt(r['created'])[:7] for r in sel); print('per maand alle nieuwe',sorted(m.items()))
    m=Counter(dt(r['created'])[:7] for r in paid); print('per maand betaald',sorted(m.items()))
