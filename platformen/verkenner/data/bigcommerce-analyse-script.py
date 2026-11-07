import json,sys,statistics as st,collections
R=[json.loads(l) for l in open(sys.argv[1])]; R=[r for r in R if r.get('createdOn')]
def num(x):
    try: return float(str(x).replace('$','').replace(',',''))
    except: return 0.0
def betaald(r): return num(r.get('monthlyPrice'))>0 or num(r.get('upfrontPrice'))>0
d=lambda r:r['createdOn'][:7]
rv=lambda r:(r.get('reviewCount') if isinstance(r.get('reviewCount'),int) else (r.get('appReviewCount') or 0))
print('n',len(R),'betaald',sum(map(betaald,R)),'unifiedBilling',collections.Counter(str(r.get('unifiedBilling')) for r in R))
print('pricingType',collections.Counter(r.get('pricingType') for r in R).most_common(8))
print('per jaar',sorted(collections.Counter(d(r)[:4] for r in R).items()))
print('per maand 2025+',sorted(collections.Counter(d(r) for r in R if d(r)>='2025').items()))
def stats(g,n):
    if not g: print(n,'leeg');return
    a=sorted(rv(r) for r in g)
    print(f"{n}: n={len(g)} mediaan reviews={st.median(a)} 0={sum(x==0 for x in a)/len(a):.0%} 1+={sum(x>=1 for x in a)/len(a):.0%} 5+={sum(x>=5 for x in a)/len(a):.0%} 20+={sum(x>=20 for x in a)/len(a):.0%} max={a[-1]}")
for a,b in [('2025-01','2025-06'),('2025-07','2025-12'),('2026-01','2026-04'),('2026-05','2026-08')]:
    g=[r for r in R if a<=d(r)<=b]
    stats([r for r in g if betaald(r)],f'{a}..{b} betaald'); stats([r for r in g if not betaald(r)],f'{a}..{b} gratis/proef')
stats([r for r in R if d(r)<'2024'],'voor 2024 alles')
print('mediaan maandprijs betaald 2025+',st.median([num(r.get('monthlyPrice')) for r in R if betaald(r) and d(r)>='2025' and num(r.get('monthlyPrice'))>0]))
top=sorted([r for r in R if d(r)>='2025'],key=lambda r:-rv(r))[:10]
for r in top: print(rv(r),d(r),r.get('pricing'),r['title'][:60])
