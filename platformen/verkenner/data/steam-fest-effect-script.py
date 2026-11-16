# Vera 16 nov 2026: wat doet een thema-fest van Steam met het aantal volgers?
# Natuurlijk experiment: het Auto-Battler RPG Fest loopt 16 nov 18:00 UTC tot 23 nov 2026.
# Nulmeting: volgers van 16 nov (vóór de start) in steam-volgers-2026-11-16.jsonl en
# steam-volgers-autobattler-2026-11-16.jsonl. Herhaling na het fest (24 nov) en een week later (1 dec)
# met steam-volgers-curl.sh op dezelfde appids.
# Vergelijk de groei van bureaubladapps met het label Auto Battler (mogen meedoen) met die zonder (controle),
# apart voor "binnenkort" en uitgebracht.
# Gebruik: python3 -I steam-fest-effect-script.py nameting.jsonl
import csv, json, sys, statistics as st, os

hier = os.path.dirname(os.path.abspath(__file__))
kaart = {r['appid']: r for r in csv.DictReader(open(os.path.join(hier, 'steam-desktop-kaart-2026-11-16.csv')))}

def lees(p):
    d = {}
    for l in open(p):
        x = json.loads(l)
        if x.get('volgers') is not None:
            d.setdefault(x['appid'], x['volgers'])  # eerste geldige meting telt
    return d

voor = {}
for f in ['steam-volgers-2026-11-16.jsonl', 'steam-volgers-autobattler-2026-11-16.jsonl']:
    p = os.path.join(hier, f)
    if os.path.exists(p):
        for k, v in lees(p).items():
            voor.setdefault(k, v)
na = lees(sys.argv[1])

groepen = {}
for a, v0 in voor.items():
    if a not in na or a not in kaart:
        continue
    r = kaart[a]
    ab = 'auto battler' in r['labels'].lower()
    bk = r['binnenkort'] in ('1', 'True', 'true', 'ja')
    g = ('auto battler' if ab else 'controle') + (', binnenkort' if bk else ', uit')
    groei = (na[a] - v0) / v0 if v0 >= 10 else None
    groepen.setdefault(g, []).append((a, v0, na[a], groei))

for g, rij in sorted(groepen.items()):
    gr = [x[3] for x in rij if x[3] is not None]
    abs_ = [x[2] - x[1] for x in rij]
    print(f"{g}: n={len(rij)}, mediaan erbij {st.median(abs_)}, mediaan groei (alleen 10+ volgers, n={len(gr)}) "
          f"{(st.median(gr) * 100 if gr else float('nan')):.1f}%")
    for a, v0, v1, _ in sorted(rij, key=lambda x: x[2] - x[1], reverse=True)[:5]:
        print(f"   {a} {kaart[a]['naam'][:40]}: {v0} -> {v1}")
