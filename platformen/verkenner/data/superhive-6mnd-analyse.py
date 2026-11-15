# Vera 15 nov 2026: analyse van superhive-addons-6mnd.csv (uit superhive-6mnd-script.py).
# Gebruik: python3 -I superhive-6mnd-analyse.py addons-6mnd.csv
import csv, sys, re, statistics as st, collections as co

rijen = [r for r in csv.DictReader(open(sys.argv[1])) if r['code'] == '200']
# dubbele (zelfde slug) eruit
gezien = set(); R = []
for r in rijen:
    if r['slug'] in gezien: continue
    gezien.add(r['slug']); R.append(r)

def verkoop(s):
    """Ondergrens van het verkoopblok. Leeg = Superhive toont niets = 0 tot 9."""
    m = re.match(r'(\d+)\+?', (s or '').replace(',', ''))
    return int(m.group(1)) if m else 0

def emmer(v):
    return '1000+' if v >= 1000 else '100-999' if v >= 100 else '10-99' if v >= 10 else '0-9'

SOORTEN = [
    ('3D-printen', r'3d.?print|\bstl\b|\b3mf\b|slicer|resin|\bfdm\b|printable|print.?ready|miniature|dovetail|lithophane'),
    ('generator', r'generat|procedural|scatter|builder|creator'),
    ('materialen', r'material|shader|texture|\bpbr\b|surface|decal'),
    ('animatie en rig', r'animat|\brig|bone|pose|keyframe|motion|mocap|walk cycle|lip.?sync'),
    ('render, licht, camera', r'render|light|camera|hdri|lighting|compositor|post.?process|denois'),
    ('AI', r'\bai\b|a\.i\.|neural|llm|gpt|diffusion|machine learning'),
    ('modelleren', r'model|mesh|topolog|retopo|remesh|bevel|boolean|sculpt|uv\b|unwrap|cad\b'),
    ('werkstroom en interface', r'workflow|interface|\bui\b|menu|shortcut|hotkey|batch|organi[sz]|manager|rename|export|import|pipeline|asset'),
]
def soort(r):
    tekst = (r['titel'] + ' ' + r['beschrijving'] + ' ' + r['cat']).lower()
    for naam, pat in SOORTEN:
        if re.search(pat, tekst): return naam
    return 'overig'

for r in R:
    r['v'] = verkoop(r['sales']); r['soort'] = soort(r)
    r['p'] = float(r['prijs']) if r['prijs'] not in ('', None) else None
    r['l'] = float(r['leeftijd_mnd']) if r['leeftijd_mnd'] not in ('', None) else None

ZES = [r for r in R if r['l'] is not None and r['l'] <= 6]
betaald = [r for r in ZES if r['p'] and r['p'] > 0]
gratis = [r for r in ZES if not r['p']]
print(f'rijen {len(rijen)}, uniek {len(R)}, 0 tot 6 maanden {len(ZES)} (betaald {len(betaald)}, gratis {len(gratis)})')
print('makers (betaald):', len({r["maker"] for r in betaald}))

def verdeling(groep, kop):
    n = len(groep) or 1
    c = co.Counter(emmer(r['v']) for r in groep)
    print(f'{kop} n={len(groep)}: ' + ', '.join(f'{k} {c[k]} ({100*c[k]/n:.1f}%)' for k in ['0-9', '10-99', '100-999', '1000+']))

verdeling(betaald, 'Betaald, 0 tot 6 maanden')
verdeling(gratis, 'Gratis, 0 tot 6 maanden')
print('\nPer leeftijd (betaald):')
for lo, hi, naam in [(0, 0.99, '<1 mnd'), (1, 1, '1 mnd'), (2, 2, '2 mnd'), (3, 3, '3 mnd'), (4, 4, '4 mnd'), (5, 5, '5 mnd'), (6, 6, '6 mnd')]:
    verdeling([r for r in betaald if lo <= r['l'] <= hi], '  ' + naam)
print('\nPrijs betaald: mediaan', st.median(r['p'] for r in betaald), ' kwartielen', st.quantiles([r['p'] for r in betaald], n=4))
print('Per maand instroom (betaald+gratis):', sorted(co.Counter(int(r['l']) for r in ZES).items()))

print('\nPer soort (betaald, 2 tot 6 maanden oud, zodat jonge add-ons de cijfers niet drukken):')
oud = [r for r in betaald if r['l'] >= 2]
per = co.defaultdict(list)
for r in oud: per[r['soort']].append(r)
for naam, g in sorted(per.items(), key=lambda x: -len(x[1])):
    n = len(g); t10 = sum(r['v'] >= 10 for r in g); t100 = sum(r['v'] >= 100 for r in g)
    som = sum(r['v'] * r['p'] for r in g)
    print(f'  {naam:26} n={n:4}  10+ {100*t10/n:5.1f}%  100+ {100*t100/n:5.1f}%  prijs med {st.median(r["p"] for r in g):5.2f}  omzet-ondergrens ${som:,.0f}')

print('\nSuperhive-categorie (betaald, 2 tot 6 mnd):')
per = co.defaultdict(list)
for r in oud:
    for c in (r['cat'] or 'geen').split(';'): per[c].append(r)
for naam, g in sorted(per.items(), key=lambda x: -len(x[1]))[:15]:
    n = len(g); t10 = sum(r['v'] >= 10 for r in g); t100 = sum(r['v'] >= 100 for r in g)
    print(f'  {naam:22} n={n:4}  10+ {100*t10/n:5.1f}%  100+ {100*t100/n:5.1f}%')

print('\nPrijsklassen (betaald, 2 tot 6 mnd):')
# controleur 15 nov: ondergrens inclusief, bovengrens exclusief (een prijs van precies $15 hoort bij $15-20)
for lo, hi in [(0, 5), (5, 10), (10, 15), (15, 20), (20, 30), (30, 100000)]:
    g = [r for r in oud if lo <= r['p'] < hi]
    if g: print(f'  ${lo:.0f}-{hi:.0f}: n={len(g)}  10+ {100*sum(r["v"]>=10 for r in g)/len(g):.1f}%  100+ {100*sum(r["v"]>=100 for r in g)/len(g):.1f}%')

print('\nMakers: aandeel van alle verkopen (ondergrens) bij de top 10 makers, betaald 0 tot 6 mnd:')
mk = co.Counter()
for r in betaald: mk[r['maker']] += r['v'] * r['p']
tot = sum(mk.values()) or 1
for m, v in mk.most_common(10): print(f'  {m:28} ${v:,.0f} ({100*v/tot:.0f}%)')
nmk = co.Counter(r['maker'] for r in betaald)
print('Makers met 1 add-on in deze 6 maanden:', sum(1 for m, c in nmk.items() if c == 1), 'van', len(nmk))
een = [r for r in betaald if nmk[r['maker']] == 1 and r['l'] >= 2]
verdeling(een, 'Betaald, maker met 1 add-on in 6 mnd, 2 tot 6 mnd oud')

print('\nTop 40 betaald op verkopen per maand:')
for r in sorted(betaald, key=lambda r: -r['v'] / max(r['l'], 1))[:40]:
    print(f"  {r['sales']:>6} {r['published']:>20} ${r['p']:>6} {r['ratings']:>3}r  {r['soort']:22} {r['maker'][:20]:20} {r['titel'][:60]}")

print('\n3D-printen, alles 0 tot 6 maanden (betaald en gratis):')
for r in sorted([r for r in ZES if r['soort'] == '3D-printen'], key=lambda r: -r['v']):
    print(f"  {r['sales'] or '<10':>6} {r['published']:>20} ${r['p']} {r['ratings']}r  {r['maker'][:20]:20} {r['titel'][:70]}")
