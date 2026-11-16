# Vera 16 nov 2026 run 07:31: volgers per review, zuiver. Gebruik: python3 -I analyse3.py kaart.csv volgers.jsonl
# Regels voor 05:30 UTC (run 05:31) zijn met de hand gekozen en tellen niet mee in de steekproef.
# Per app geldt de laatste geldige meting.
import csv, json, sys, statistics as st
k = {r['appid']: r for r in csv.DictReader(open(sys.argv[1]))}
v, hand = {}, set()
for l in open(sys.argv[2]):
    d = json.loads(l)
    if d['volgers'] is None: continue
    if d['gemeten'] < '2026-11-16 05:30': hand.add(d['appid'])
    v[d['appid']] = d['volgers']
v = {a: x for a, x in v.items() if a in k}
print('apps met meting op de kaart:', len(v))
def q(xs):
    xs = sorted(xs); n = len(xs)
    return f"n={n} mediaan={st.median(xs):.2f} p25={xs[n//4]:.2f} p75={xs[3*n//4]:.2f}" if n else 'leeg'
def band(xs):
    n = len(xs)
    if not n: return 'leeg'
    p = lambda c: f"{100*sum(1 for x in xs if c(x))/n:.0f}%"
    return f"n={n} mediaan={st.median(xs):g} <10:{p(lambda x:x<10)} 10-99:{p(lambda x:10<=x<100)} 100-999:{p(lambda x:100<=x<1000)} 1000+:{p(lambda x:x>=1000)}"
pool = [a for a, r in k.items() if r['binnenkort'] != 'True' and r['releasedatum'].startswith('2026') and r['gratis'] != 'True']
st_uit = [a for a in pool if a in v and a not in hand]
print('UIT 2026 betaald, pool', len(pool), 'willekeurig gemeten', len(st_uit))
print('  volgers:', band([v[a] for a in st_uit]))
R = lambda a: int(k[a]['reviews_totaal'] or 0)
for m in (5, 10, 20):
    print(f'  volgers per review, {m}+ reviews:', q([v[a]/R(a) for a in st_uit if R(a) >= m]))
print('  reviews per volger, 20+ volgers:', q([R(a)/v[a] for a in st_uit if v[a] >= 20]))
for lo, hi in [(0,10),(10,100),(100,1000),(1000,10**9)]:
    xs = [R(a) for a in st_uit if lo <= v[a] < hi]
    print(f'  volgers {lo}-{hi}: reviews mediaan', st.median(xs) if xs else '-', 'n=', len(xs), 'bereik', (min(xs), max(xs)) if xs else '')
bk = [a for a, r in k.items() if r['binnenkort'] == 'True']
bk2 = [a for a in bk if int(k[a]['lijkt_op_hats']) >= 2]
bk01 = [a for a in bk if int(k[a]['lijkt_op_hats']) < 2]
print('BINNENKORT lijkt 2+ gemeten', sum(a in v for a in bk2), 'van', len(bk2), band([v[a] for a in bk2 if a in v]))
s01 = [a for a in bk01 if a in v and a not in hand]
print('BINNENKORT lijkt 0-1 willekeurig', len(s01), 'van', len(bk01), band([v[a] for a in s01]))
print('  boven 300:', sum(v[a] >= 300 for a in s01), ' boven 100:', sum(v[a] >= 100 for a in s01))
for g, xs in [('2+', [a for a in bk2 if a in v]), ('0-1', s01)]:
    d = [v[a] for a in xs if k[a]['demo'] == 'True']; z = [v[a] for a in xs if k[a]['demo'] != 'True']
    print(f'  demo {g}: met', band(d), '| zonder', band(z))
print('Top aangekondigd (alle gemeten):')
for a in sorted([a for a in bk if a in v], key=lambda a: -v[a])[:12]:
    print(f"  {k[a]['naam']} ({a}) {v[a]} demo {k[a]['demo']} lijkt {k[a]['lijkt_op_hats']} uitgever {k[a]['uitgever']}")
