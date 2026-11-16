# Vera 16 nov 2026: analyse volgers bureaublad-apps. Gebruik: python3 -I steam-volgers-analyse-script.py kaart.csv volgers.jsonl
import csv, json, sys, statistics as st
kaart = {r['appid']: r for r in csv.DictReader(open(sys.argv[1]))}
v = {}
for l in open(sys.argv[2]):
    d = json.loads(l)
    if d['volgers'] is not None and d['appid'] in kaart: v[d['appid']] = d['volgers']
    elif d['volgers'] is not None: print('buiten de kaart:', d['appid'], d['volgers'])
def band(xs):
    n = len(xs)
    if not n: return 'leeg'
    p = lambda c: f"{100*sum(1 for x in xs if c(x))/n:.0f}%"
    return f"n={n} mediaan={st.median(xs):g} <10:{p(lambda x:x<10)} 10-99:{p(lambda x:10<=x<100)} 100-999:{p(lambda x:100<=x<1000)} 1000+:{p(lambda x:x>=1000)}"
bk = [a for a in v if kaart[a]['binnenkort'] == 'True']
uit = [a for a in v if kaart[a]['binnenkort'] != 'True']
print('BINNENKORT lijkt 2+ (volledig):', band([v[a] for a in bk if int(kaart[a]['lijkt_op_hats']) >= 2]))
print('BINNENKORT lijkt 0-1 (steekproef):', band([v[a] for a in bk if int(kaart[a]['lijkt_op_hats']) < 2]))
for lab, test in [('datum jan 2027 of Q1 2027', lambda d: 'Q1 2027' in d or d.startswith('2027-01') or 'January 2027' in d), ('datum 2026', lambda d: d.startswith('2026'))]:
    print('BINNENKORT', lab, band([v[a] for a in bk if test(kaart[a]['releasedatum'])]))
print('BINNENKORT met demo:', band([v[a] for a in bk if kaart[a]['demo'] == 'True']), '| zonder:', band([v[a] for a in bk if kaart[a]['demo'] != 'True']))
print('\nTop 15 binnenkort:')
for a in sorted(bk, key=lambda a: -v[a])[:15]:
    r = kaart[a]; print(f"  {r['naam']} ({a}) {v[a]} volgers, datum {r['releasedatum']}, demo {r['demo']}, lijkt {r['lijkt_op_hats']}, maker {r['maker']}")
print('\nUIT 2026, verhouding volgers per review (reviews_totaal>=10):')
rs = [(a, v[a] / int(kaart[a]['reviews_totaal'])) for a in uit if kaart[a]['reviews_totaal'] and int(kaart[a]['reviews_totaal']) >= 10 and kaart[a]['gratis'] != 'True']
q = sorted(x for _, x in rs)
if q: print(f"  n={len(q)} mediaan={st.median(q):.2f} p25={q[len(q)//4]:.2f} p75={q[3*len(q)//4]:.2f}")
print('UIT 2026 betaald lijkt 2+:', band([v[a] for a in uit if int(kaart[a]['lijkt_op_hats']) >= 2 and kaart[a]['gratis'] != 'True']))
print('UIT 2026 betaald steekproef lijkt 0-1:', band([v[a] for a in uit if int(kaart[a]['lijkt_op_hats']) < 2 and kaart[a]['gratis'] != 'True']))
print('\nVergelijkbare spellen:')
for a in ['5376930','5091650','5478110','4262590','4846310','5320500','4623570','3122460','3959890','3733510','3678970']:
    if a in v: r = kaart[a]; print(f"  {r['naam']} ({a}): {v[a]} volgers, reviews {r['reviews_totaal']}, datum {r['releasedatum']}")
