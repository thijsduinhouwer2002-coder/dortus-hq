import json,sys,statistics as st,collections
R=[r for r in json.load(open(sys.argv[1])) if r.get('stats')]
def soort(r):
    pr=[e['price'] for e in r['editions']] or [x for x in (r['price_range'] or []) if x is not None]
    if not pr: return 'gratis'
    return 'freemium' if any(p==0 for p in pr) else 'betaald'
def prijs(r):
    pr=[e['price'] for e in r['editions'] if e['price']] or [x for x in (r['price_range'] or []) if x]
    return min(pr) if pr else 0
d=lambda r:(r['first'] or r['stats']['created'] or '0000')[:7]
print('soorten',collections.Counter(soort(r) for r in R))
print('per jaar',sorted(collections.Counter(d(r)[:4] for r in R).items()))
print('per maand 2025-26',sorted(collections.Counter(d(r) for r in R if d(r)>='2025').items()))
def stats(g,n):
    if not g: print(n,'leeg');return
    t=sorted(r['stats']['downloads']['total'] for r in g); m=sorted(r['stats']['downloads']['monthly'] for r in g)
    print(f"{n}: n={len(g)} mediaan totaal={st.median(t)} 100+={sum(x>=100 for x in t)/len(t):.0%} 500+={sum(x>=500 for x in t)/len(t):.0%} | mediaan per maand={st.median(m)} max={t[-1]}")
for a,b in [('2025-01','2025-06'),('2025-07','2025-12'),('2026-01','2026-04'),('2026-05','2026-08')]:
    g=[r for r in R if a<=d(r)<=b]
    for s in ('betaald','freemium','gratis'): stats([r for r in g if soort(r)==s],f'{a}..{b} {s}')
stats([r for r in R if d(r)<'2024' and soort(r)=='betaald'],'voor 2024 betaald')
print('makers',len({r['seller'] for r in R}))
top=sorted([r for r in R if soort(r)!='gratis' and d(r)>='2025'],key=lambda r:-r['stats']['downloads']['total'])[:12]
for r in top: print(r['seller'],r['slug'],d(r),soort(r),prijs(r),r['stats']['downloads'])
print('mediaanprijs betaald 2025+',st.median([prijs(r) for r in R if soort(r)=='betaald' and d(r)>='2025']))
