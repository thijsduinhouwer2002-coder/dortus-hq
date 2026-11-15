import json,sys,statistics as st,collections as C
R=[json.loads(l) for l in open(sys.argv[1])]
R=[r for r in R if r.get('created') and r['installs'] is not None]
print('apps met data',len(R))
cat=C.Counter(c for r in R for c in r['cat']); print(cat.most_common(15))
mon=C.Counter(r['created'][:7] for r in R); print(sorted(mon.items())[-24:])
def stats(L,t):
    if not L: print(t,'leeg');return
    I=sorted(r['installs'] for r in L)
    print(f"{t}: n={len(I)} mediaan={st.median(I)} 10+={sum(i>=10 for i in I)/len(I):.0%} 50+={sum(i>=50 for i in I)/len(I):.0%} 250+={sum(i>=250 for i in I)/len(I):.0%} 1000+={sum(i>=1000 for i in I)}")
for lo,hi,t in [('2026-05','2026-09','mei-aug 2026'),('2026-01','2026-05','jan-apr 2026'),('2025-07','2026-01','jul-dec 2025'),('2000','2025-07','voor jul 2025')]:
    L=[r for r in R if lo<=r['created'][:7]<hi]
    stats(L,t)
    stats([r for r in L if 'GAMES' in r['cat'] or any('GAME' in c for c in r['cat'])],'  spellen')
    stats([r for r in L if 'MODERATOR' in r['cat']],'  moderator')
own=C.Counter(r['owner'] for r in R if r['created']>='2026-05'); print('makers mei+',len(own), own.most_common(5))
print('top nieuw',sorted([(r['installs'],r['url'],r['created'][:10],r['cat']) for r in R if r['created']>='2026-05'],reverse=True)[:12])
