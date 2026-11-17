# Verhaal 28: hoe vaak en wanneer plaatsen, binnen hetzelfde TikTok-account.
# Leest tiktok-lengte-2026-11-17.csv (verhaal 27). Het tijdstip komt uit het id:
# de bovenste 32 bits van een TikTok-id zijn de Unix-tijd van plaatsen (UTC).
# ratio = views gedeeld door de mediaan van de 10 filmpjes ervoor en 10 erna (zelfde account).
# Gebruik: python3 tiktok-ritme-analyse.py tiktok-lengte-2026-11-17.csv
import csv, sys, collections, statistics as st, datetime as dt

rows = list(csv.DictReader(open(sys.argv[1])))
acc = collections.defaultdict(list)
for r in rows:
    r['t'] = int(r['id']) >> 32
    r['ratio'] = float(r['ratio']); r['views'] = float(r['views']); r['ref'] = float(r['ref'])
    acc[r['account']].append(r)
for l in acc.values():
    l.sort(key=lambda r: r['t'])
    for i, r in enumerate(l):
        r['gap'] = (r['t'] - l[i-1]['t']) / 3600 if i else None
        r['gapna'] = (l[i+1]['t'] - r['t']) / 3600 if i + 1 < len(l) else None
        r['vorige'] = l[i-1]['ratio'] if i else None

def tab(naam, groepen, sleutel):
    print('\n==', naam)
    print('groep | n | accounts | mediaan ratio | 3x+ | onder 0,5 | mediaan van accountmedianen (accounts met 5+)')
    for g, f in groepen:
        sel = [r for r in rows if f(r)]
        if not sel: continue
        per = collections.defaultdict(list)
        for r in sel: per[r['account']].append(r['ratio'])
        am = [st.median(v) for v in per.values() if len(v) >= 5]
        print(g, '|', len(sel), '|', len(per), '|', round(st.median(r['ratio'] for r in sel), 2), '|',
              f"{100*sum(r['ratio']>=3 for r in sel)/len(sel):.0f}%", '|',
              f"{100*sum(r['ratio']<0.5 for r in sel)/len(sel):.0f}%", '|',
              (round(st.median(am), 2), len(am), sum(x > 1 for x in am)) if am else '-')

G = lambda lo, hi: (lambda r: r['gap'] is not None and lo <= r['gap'] < hi)
tab('A. uren sinds het vorige filmpje', [
    ('<2 u', G(0, 2)), ('2-8 u', G(2, 8)), ('8-20 u', G(8, 20)), ('20-28 u (dagelijks)', G(20, 28)),
    ('28-52 u', G(28, 52)), ('52-100 u', G(52, 100)), ('4-7 d', G(100, 168)), ('7-14 d', G(168, 336)),
    ('14-60 d', G(336, 1440)), ('60 d+', G(1440, 1e9))], 'gap')

tab('B. na het vorige filmpje (prestatie vorige)', [
    ('vorige <0,5', lambda r: r['vorige'] is not None and r['vorige'] < 0.5),
    ('vorige 0,5-1', lambda r: r['vorige'] is not None and 0.5 <= r['vorige'] < 1),
    ('vorige 1-2', lambda r: r['vorige'] is not None and 1 <= r['vorige'] < 2),
    ('vorige 2-3', lambda r: r['vorige'] is not None and 2 <= r['vorige'] < 3),
    ('vorige 3-10', lambda r: r['vorige'] is not None and 3 <= r['vorige'] < 10),
    ('vorige 10+', lambda r: r['vorige'] is not None and r['vorige'] >= 10)], 'vorige')

tab('B2. na een hit (vorige 3+), naar uren ertussen', [
    ('hit, <20 u erna', lambda r: r['vorige'] and r['vorige'] >= 3 and r['gap'] < 20),
    ('hit, 20-52 u erna', lambda r: r['vorige'] and r['vorige'] >= 3 and 20 <= r['gap'] < 52),
    ('hit, 52 u+ erna', lambda r: r['vorige'] and r['vorige'] >= 3 and r['gap'] >= 52)], '')

tab('A2. uren tot het volgende filmpje (wordt een filmpje opgegeten door een snel volgend?)', [
    ('volgende <8 u', lambda r: r['gapna'] is not None and r['gapna'] < 8),
    ('volgende 8-28 u', lambda r: r['gapna'] is not None and 8 <= r['gapna'] < 28),
    ('volgende 28-100 u', lambda r: r['gapna'] is not None and 28 <= r['gapna'] < 100),
    ('volgende 100 u+', lambda r: r['gapna'] is not None and r['gapna'] >= 100)], '')

# C. per week: aantal filmpjes tegen de views per filmpje en de som (in eigen-mediaan-eenheden)
print('\n== C. per kalenderweek (UTC), alleen weken met 1+ filmpje')
wk = collections.defaultdict(list)
for r in rows:
    d = dt.datetime.fromtimestamp(r['t'], dt.UTC).isocalendar()
    wk[(r['account'], d[0], d[1])].append(r)
bins = [(1, 1), (2, 2), (3, 4), (5, 7), (8, 14), (15, 999)]
print('filmpjes in de week | weken | accounts | mediaan ratio per filmpje | mediaan som ratio per week | mediaan van accountmedianen ratio')
for lo, hi in bins:
    ws = [v for v in wk.values() if lo <= len(v) <= hi]
    if not ws: continue
    per = collections.defaultdict(list)
    for v in ws: per[v[0]['account']].append(st.median(r['ratio'] for r in v))
    am = [st.median(x) for x in per.values() if len(x) >= 3]
    print(f'{lo}-{hi}', '|', len(ws), '|', len(per), '|', round(st.median(r['ratio'] for v in ws for r in v), 2), '|',
          round(st.median(sum(r['ratio'] for r in v) for v in ws), 2), '|', (round(st.median(am), 2), len(am)) if am else '-')

# C2. binnen een account: weken met meer filmpjes dan de eigen mediaan tegen minder
print('\n== C2. per account: week met meer dan gewoonlijk vs minder (mediaan ratio per filmpje, som)')
for a in sorted(acc):
    ws = [v for k, v in wk.items() if k[0] == a]
    if len(ws) < 15: continue
    m = st.median(len(v) for v in ws)
    veel = [v for v in ws if len(v) > m]; weinig = [v for v in ws if len(v) < m]; gelijk = [v for v in ws if len(v) == m]
    f = lambda vs: (round(st.median(r['ratio'] for v in vs for r in v), 2), round(st.median(sum(r['ratio'] for r in v) for v in vs), 1)) if vs else '-'
    print(a, 'weken', len(ws), 'mediaan per week', m, '| meer', len(veel), f(veel), '| gelijk', len(gelijk), f(gelijk), '| minder', len(weinig), f(weinig))

# D. uur van plaatsen (UTC), binnen account: per account ratio per blok van 4 uur
print('\n== D. blok van 4 uur UTC, per account mediaan (accounts met 10+ in het blok)')
blok = lambda r: dt.datetime.fromtimestamp(r['t'], dt.UTC).hour // 4
tab('D. blok van 4 uur UTC (op een hoop)', [(f'{4*b:02d}-{4*b+4:02d} UTC', (lambda b: lambda r: blok(r) == b)(b)) for b in range(6)], '')
print('\nper account: gewoon blok (meeste filmpjes) tegen andere blokken')
for a in sorted(acc):
    l = acc[a]; c = collections.Counter(blok(r) for r in l); hoofd = c.most_common(1)[0][0]
    rest = [r['ratio'] for r in l if blok(r) != hoofd]; h = [r['ratio'] for r in l if blok(r) == hoofd]
    if len(rest) >= 15:
        print(a, 'gewoon', f'{4*hoofd:02d}-{4*hoofd+4:02d}', len(h), round(st.median(h), 2), '| ander blok', len(rest), round(st.median(rest), 2))

# E. weekdag
wd = lambda r: dt.datetime.fromtimestamp(r['t'], dt.UTC).weekday()
tab('E. weekdag (UTC)', [(n, (lambda i: lambda r: wd(r) == i)(i)) for i, n in enumerate(['ma', 'di', 'wo', 'do', 'vr', 'za', 'zo'])], '')

# F. na een pauze van 14+ dagen: de eerste 5 filmpjes
print('\n== F. na een pauze van 14+ dagen: filmpje 1 tot 5 erna (ratio)')
for k in range(5):
    v = []
    for l in acc.values():
        for i, r in enumerate(l):
            if r['gap'] and r['gap'] >= 336 and i + k < len(l):
                v.append(l[i+k]['ratio'])
    if v: print('filmpje', k+1, 'n', len(v), 'mediaan', round(st.median(v), 2), '3x+', f'{100*sum(x>=3 for x in v)/len(v):.0f}%')

# G. ijkpunt in de tijd in plaats van in filmpjes: mediaan views van het eigen account
# van 30 tot 120 dagen ervoor en erna (de drukke periode zelf telt niet mee).
print('\n== G. dichtheid tegen een ijkpunt buiten de eigen periode (views / mediaan views 30-120 d ervoor en erna)')
for l in acc.values():
    for r in l:
        ref = [x['views'] for x in l if 30*86400 <= abs(x['t'] - r['t']) <= 120*86400]
        r['ref2'] = st.median(ref) if len(ref) >= 10 else None
        r['dicht'] = sum(1 for x in l if abs(x['t'] - r['t']) <= 3.5*86400)  # filmpjes in de week eromheen
        r['dicht_ref'] = None
    for r in l:
        omg = [x['dicht'] for x in l if 30*86400 <= abs(x['t'] - r['t']) <= 120*86400]
        r['dicht_ref'] = st.median(omg) if len(omg) >= 10 else None
sel = [r for r in rows if r['ref2'] and r['dicht_ref']]
def toon(naam, f):
    s = [r for r in sel if f(r)]
    if len(s) < 20: return
    per = collections.defaultdict(list)
    for r in s: per[r['account']].append(r['views'] / r['ref2'])
    am = [st.median(v) for v in per.values() if len(v) >= 10]
    print(naam, '| n', len(s), '| mediaan', round(st.median(r['views']/r['ref2'] for r in s), 2), '| accountmedianen', (round(st.median(am), 2), len(am), sum(x > 1 for x in am)) if am else '-')
toon('week veel drukker dan gewoon (2x+)', lambda r: r['dicht'] >= 2*r['dicht_ref'])
toon('week drukker (1,25-2x)', lambda r: 1.25*r['dicht_ref'] <= r['dicht'] < 2*r['dicht_ref'])
toon('week gewoon (0,8-1,25x)', lambda r: 0.8*r['dicht_ref'] <= r['dicht'] < 1.25*r['dicht_ref'])
toon('week rustiger (onder 0,8x)', lambda r: r['dicht'] < 0.8*r['dicht_ref'])

# H. kleine accounts: mediaan views van het ijkpunt onder 2.000
print('\n== H. alleen kleine stukken (ref onder 2.000 views): uren sinds vorige')
klein = [r for r in rows if r['ref'] < 2000]
for g, f in [('<20 u', G(0, 20)), ('20-28 u', G(20, 28)), ('28-100 u', G(28, 100)), ('100 u+', G(100, 1e9))]:
    s = [r for r in klein if f(r)]
    print(g, len(s), len({r['account'] for r in s}), round(st.median(r['ratio'] for r in s), 2), f"{100*sum(r['ratio']>=3 for r in s)/len(s):.0f}%")
