# Lengte van een TikTok tegen views, binnen hetzelfde account.
# Per filmpje: views gedeeld door de mediaan van de 10 filmpjes ervoor en 10 erna (zelfde account).
# Gebruik: python3 tiktok-lengte-analyse.py <map met csv per account> <uit.csv>
import csv, sys, os, statistics as st, time
map_, uit = sys.argv[1], sys.argv[2]
nu = time.time()
B = [(0,10,'<10 s'),(10,15,'10-15 s'),(15,20,'15-20 s'),(20,30,'20-30 s'),(30,45,'30-45 s'),(45,60,'45-60 s'),(60,9999,'60+ s')]
def bak(d):
    for a,b,n in B:
        if a <= d < b: return n
alle = []
for f in sorted(os.listdir(map_)):
    h = f[:-4]
    rows = [r for r in csv.DictReader(open(os.path.join(map_, f))) if r['ts'] and r['views'] and r['duur']]
    rows.sort(key=lambda r: int(r['ts']))
    v = [int(r['views']) for r in rows]
    for i, r in enumerate(rows):
        if nu - int(r['ts']) < 14*86400: continue
        buren = v[max(0,i-10):i] + v[i+1:i+11]
        if len(buren) < 10: continue
        ref = st.median(buren)
        if ref <= 0: continue
        alle.append(dict(account=h, id=r['id'], datum=time.strftime('%Y-%m-%d', time.gmtime(int(r['ts']))),
                         duur=int(float(r['duur'])), views=int(r['views']), ref=ref, ratio=round(int(r['views'])/ref,3),
                         saves=int(r['saves'] or 0), likes=int(r['likes'] or 0),
                         vraag=int('?' in r['tekst'][:80]), tekst=r['tekst'][:80]))
with open(uit,'w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(alle[0].keys())); w.writeheader(); w.writerows(alle)
print('filmpjes', len(alle), 'accounts', len({a['account'] for a in alle}))
print('\nAlle filmpjes samen:')
print('bak       n    mediaan_ratio  aandeel>=3x  aandeel<0.5x  saves/1000views')
for a,b,n in B:
    x = [r for r in alle if bak(r['duur'])==n]
    if not x: continue
    rr = [r['ratio'] for r in x]
    sv = st.median([1000*r['saves']/r['views'] for r in x if r['views']>0])
    print(f"{n:8} {len(x):5} {st.median(rr):8.2f} {sum(q>=3 for q in rr)/len(rr):10.0%} {sum(q<0.5 for q in rr)/len(rr):10.0%} {sv:10.1f}")
print('\nPer account (mediaan ratio per bak, alleen bakken met 8+ filmpjes), dan mediaan over accounts:')
per = {}
for h in sorted({a['account'] for a in alle}):
    x = [r for r in alle if r['account']==h]
    md = st.median([r['duur'] for r in x])
    line = f"{h:22} n={len(x):4} mediaanduur={md:5.0f}  "
    for a,b,n in B:
        y = [r['ratio'] for r in x if bak(r['duur'])==n]
        if len(y) >= 8:
            per.setdefault(n, []).append(st.median(y)); line += f"{n}:{st.median(y):.2f}({len(y)}) "
    print(line)
for a,b,n in B:
    if n in per: print(n, 'accounts', len(per[n]), 'mediaan', round(st.median(per[n]),2), 'boven 1:', sum(q>1 for q in per[n]))
