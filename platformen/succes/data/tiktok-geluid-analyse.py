# Verhaal 31 (Joris): welk geluid onder een TikTok werkt binnen hetzelfde account?
# Invoer: map met <account>.csv uit tiktok-geluid-haal.py.
# Elk filmpje wordt vergeleken met de mediaan van de 10 filmpjes ervoor en de 10 erna
# van hetzelfde account (zelfde werkwijze als verhaal 27, 28 en 30).
# Uitvoer: tabel per soort geluid + csv met alleen cijfers en soort (geen titels van geluiden).
# Gebruik: python3 tiktok-geluid-analyse.py <map> <uit.csv>
import csv, os, re, sys, statistics as st, time, random, collections

map_ = sys.argv[1]; uit = sys.argv[2]
NU = time.time(); GRENS = NU - 14 * 86400
ORIG = re.compile(r'^(original sound|som original|originalton|sonido original|origineel geluid|suara asli|'
                  r'оригинальный звук|son original|suono originale|oryginalny d|orijinal ses|âm thanh gốc|'
                  r'เสียงต้นฉบับ|オリジナル楽曲|原声|원본 사운드|الصوت الأصلي|ljud original|originalljud|originallyd)', re.I)
RUSTIG = re.compile(r'lo-?fi|chill|piano|ambient|calm|relax|acoustic|instrumental|healing|peaceful|soft|sleep|meditat|cozy|study', re.I)
EPISCH = re.compile(r'epic|cinematic|trailer|battle|metal|dramatic|heroic|war\b|invictus|dies|requiem', re.I)

def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())

alle = []
for f in sorted(os.listdir(map_)):
    if not f.endswith('.csv'): continue
    acc = f[:-4]
    rs = [r for r in csv.DictReader(open(os.path.join(map_, f))) if r['ts'] and r['views']]
    for r in rs: r['ts'] = int(r['ts']); r['views'] = int(r['views'])
    rs.sort(key=lambda r: r['ts'])
    for r in rs: alle.append((acc, r))

# hoe vaak komt een geluid (titel+maker) voor bij verschillende accounts in de set
gebruik = collections.defaultdict(set)
for acc, r in alle:
    if r['track'] and not ORIG.match(r['track']):
        gebruik[(r['track'].lower(), r['artists'].lower())].add(acc)

rijen = []
per = collections.defaultdict(list)
for acc, r in alle: per[acc].append(r)
for acc, rs in per.items():
    for i, r in enumerate(rs):
        if r['ts'] > GRENS: continue
        buren = [x['views'] for x in rs[max(0, i-10):i] + rs[i+1:i+11]]
        if len(buren) < 10: continue
        ref = st.median(buren)
        if ref <= 0: continue
        t = r['track']; a = r['artists']
        eigen_namen = {norm(r['uploader']), norm(r['channel']), norm(acc)} - {''}
        is_orig = bool(ORIG.match(t))
        van_zelf = any(n and (n in norm(a) or norm(a) in n) for n in eigen_namen) if a else False
        if not t: soort = 'onbekend'
        elif is_orig and van_zelf: soort = 'eigen'
        elif is_orig: soort = 'origineel_ander'
        elif r['album']: soort = 'muziek_album'
        else: soort = 'geluid_met_naam'
        muziekachtig = soort in ('muziek_album', 'geluid_met_naam')
        rijen.append(dict(account=acc, id=r['id'], datum=time.strftime('%Y-%m-%d', time.gmtime(r['ts'])),
                          jaar=time.gmtime(r['ts']).tm_year, views=r['views'], ratio=round(r['views']/ref, 3), soort=soort,
                          rustig=muziekachtig and bool(RUSTIG.search(t + ' ' + r['album'])),
                          episch=muziekachtig and bool(EPISCH.search(t + ' ' + r['album'])),
                          zelfde_geluid_andere_accounts=len(gebruik.get((t.lower(), a.lower()), set())) - 1 if muziekachtig else ''))

with open(uit, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rijen[0].keys())); w.writeheader(); w.writerows(rijen)

accs = sorted({r['account'] for r in rijen})
print('filmpjes', len(rijen), 'accounts', len(accs))
print(collections.Counter(r['soort'] for r in rijen))

def vergelijk(naam, ja, nee, rij=rijen, min_n=8):
    out = []; detail = []
    for a in accs:
        x = [r['ratio'] for r in rij if r['account'] == a and ja(r)]
        y = [r['ratio'] for r in rij if r['account'] == a and nee(r)]
        if len(x) >= min_n and len(y) >= min_n:
            out.append(st.median(x) / st.median(y)); detail.append((a, len(x), len(y), round(st.median(x)/st.median(y), 2)))
    X = [r['ratio'] for r in rij if ja(r)]; Y = [r['ratio'] for r in rij if nee(r)]
    if not out or not X or not Y:
        print(f'{naam:40s} te weinig'); return
    random.seed(1); bs = sorted(st.median([random.choice(out) for _ in out]) for _ in range(2000))
    h = lambda L: sum(1 for v in L if v >= 3) / len(L)
    print(f'{naam:40s} n={len(X):5d}/{len(Y):5d} | hit3x {h(X):4.0%} vs {h(Y):4.0%} | accounts {sum(1 for v in out if v>1)}/{len(out)} beter, '
          f'med {st.median(out):.2f} [{bs[50]:.2f}-{bs[1949]:.2f}]')
    return detail

E = lambda r: r['soort'] == 'eigen'
M = lambda r: r['soort'] in ('muziek_album', 'geluid_met_naam')
d1 = vergelijk('muziek (album of naam) vs eigen geluid', M, E)
print('  per account', d1)
vergelijk('muziek_album vs eigen', lambda r: r['soort']=='muziek_album', E)
vergelijk('geluid_met_naam vs eigen', lambda r: r['soort']=='geluid_met_naam', E)
d2 = vergelijk('origineel_ander vs eigen', lambda r: r['soort']=='origineel_ander', E)
print('  per account', d2)
vergelijk('rustig vs andere muziek', lambda r: M(r) and r['rustig'], lambda r: M(r) and not r['rustig'])
vergelijk('rustig vs eigen', lambda r: M(r) and r['rustig'], E)
vergelijk('episch vs andere muziek', lambda r: M(r) and r['episch'], lambda r: M(r) and not r['episch'])
vergelijk('geluid ook bij ander account vs alleen hier', lambda r: M(r) and r['zelfde_geluid_andere_accounts'] not in ('', 0),
          lambda r: M(r) and r['zelfde_geluid_andere_accounts'] == 0)
nieuw = [r for r in rijen if r['jaar'] >= 2025]
print('--- sinds 2025')
vergelijk('muziek vs eigen (2025+)', M, E, nieuw)
vergelijk('origineel_ander vs eigen (2025+)', lambda r: r['soort']=='origineel_ander', E, nieuw)
vergelijk('rustig vs andere muziek (2025+)', lambda r: M(r) and r['rustig'], lambda r: M(r) and not r['rustig'], nieuw)
print('--- aandeel per account (eigen / muziek / ander origineel), mediaan views')
for a in accs:
    rr = [r for r in rijen if r['account'] == a]
    c = collections.Counter(r['soort'] for r in rr)
    print(f'{a:22s} n={len(rr):4d} eigen {c["eigen"]/len(rr):4.0%} muziek {(c["muziek_album"]+c["geluid_met_naam"])/len(rr):4.0%} ander {c["origineel_ander"]/len(rr):4.0%} mediaan {st.median(r["views"] for r in rr):.0f}')
