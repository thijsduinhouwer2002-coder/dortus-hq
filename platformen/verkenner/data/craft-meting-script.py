import json,statistics as st,collections,sys
P=json.load(open(sys.argv[1]))['plugins']
isfree=lambda e: e.get('price') in (None,0,'0','0.00')
def soort(p):
    f=[isfree(e) for e in p['editions']]
    return 'gratis' if all(f) else ('freemium' if any(f) else 'betaald')
def prijs(p): 
    ps=[float(e['price']) for e in p['editions'] if not isfree(e)]; return min(ps) if ps else 0
def dt(p): return (p['dateApproved'] or {'date':'0000-00'})['date'][:7]
MASS='Justinholt.com Incorporated'
def stats(g,naam):
    if not g: print(naam,'leeg');return
    a=sorted(p['activeInstalls'] for p in g)
    print(f"{naam}: n={len(g)} mediaan={st.median(a)} 0={sum(x==0 for x in a)/len(a):.0%} 10+={sum(x>=10 for x in a)/len(a):.0%} 50+={sum(x>=50 for x in a)/len(a):.0%} 100+={sum(x>=100 for x in a)/len(a):.0%} max={a[-1]}")
print('soorten',collections.Counter(soort(p) for p in P))
for a,b in [('2025-01','2025-06'),('2025-07','2025-12'),('2026-01','2026-04'),('2026-05','2026-08')]:
    g=[p for p in P if a<=dt(p)<=b]
    print(f'--- {a}..{b} n={len(g)} waarvan massamaker {sum(p["developerName"]==MASS for p in g)}')
    for s in ('betaald','freemium','gratis'):
        stats([p for p in g if soort(p)==s],' '+s+' (alles)')
        stats([p for p in g if soort(p)==s and p['developerName']!=MASS],' '+s+' (zonder massamaker)')
# zuiver betaald, makers met eerste plugin 2025+: installs*prijs (bovengrens, telt ook proefinstallaties)
dev=collections.defaultdict(list)
for p in P: dev[p['developerId']].append(p)
first={k:min(dt(p) for p in v) for k,v in dev.items()}
rows=[]
for k,v in dev.items():
    if first[k]<'2025': continue
    b=[p for p in v if soort(p)=='betaald']
    if b: rows.append((sum(p['activeInstalls']*prijs(p) for p in b),v[0]['developerName'],[(p['name'],dt(p),p['activeInstalls'],prijs(p)) for p in b]))
rows.sort(reverse=True)
print('nieuwe makers met zuiver betaald:',len(rows),'mediaan bovengrens bruto $',st.median([r[0] for r in rows]))
for r in rows[:12]: print(round(r[0]),r[1],r[2][:3])
print('mediaanprijs zuiver betaald mei-aug 2026',st.median([prijs(p) for p in P if '2026-05'<=dt(p)<='2026-08' and soort(p)=='betaald']))
print('per maand 2026',sorted(collections.Counter(dt(p) for p in P if dt(p)>='2026').items()))
print('per maand 2026 zonder massamaker',sorted(collections.Counter(dt(p) for p in P if dt(p)>='2026' and p['developerName']!=MASS).items()))
