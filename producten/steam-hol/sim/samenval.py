"""Bram 16 nov ±18:30 UTC: vallen een hol-niveau en een aankoop op dezelfde vangst? (vraag Sanne 18:10)
Goud komt bijna alleen van vangsten en een graaf kost ±2 vangsten goud, dus koop n valt bijna altijd op een vaste vangst.
De drempels van hol-niveau tellen ook vangsten (bron "gevallen"). Draai: python3 samenval.py  (40 zaden, minuut 0 tot 25)"""
import sys, os, json, copy, collections, statistics as S
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim
HIER = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(HIER, "voortgang-v3-eind-bram.json")))
sim.SPEL_ECONOMIE, sim.SOORTEN, sim.REEKS = True, True, True
ZADEN = range(1, 41)

def spec_met(dr):
    spec = copy.deepcopy(base)
    for n in spec["sporen"][0]["niveaus"]:
        if n["niveau"] in dr:
            n["drempel"] = dr[n["niveau"]]
    return spec

# 1. op welke vangst valt koop n (huidige drempels; aankopen hangen niet van de drempels af)
tel = [collections.Counter() for _ in range(8)]
for z in ZADEN:
    st = sim.speel(0.6, z, base)
    for i, a in enumerate(st["aankopen"][:8]):
        tel[i][max([r[2] for r in st["reeks"] if r[0] <= a[0] + 1e-6] or [0])] += 1
print("1. aantal gevangen helden op het moment van koop n (40 zaden)")
for i, c in enumerate(tel):
    print("   koop %d: %s" % (i + 1, dict(sorted(c.items()))))

# 2. per drempelreeks: hoe vaak valt hol n op dezelfde vangst als een koop, en het langste gat (zoals eerste20-gat.py)
print("2. hol n samen met een koop (x van de keren dat hol n binnen 25 min kwam) en langste gat minuut 1 tot 20")
for naam, dr in [("nu 3/6/10/12/20", {}), ("Sanne 3/4/8/12/17", {3: 4, 4: 8, 6: 17}),
                 ("3/4/7/12/16", {3: 4, 4: 7, 6: 16}), ("3/4/7/12/17", {3: 4, 4: 7, 6: 17})]:
    spec = spec_met(dr); per = {}; gaten = []
    for z in ZADEN:
        st = sim.speel(0.6, z, spec)
        kt = set(round(a[0], 3) for a in st["aankopen"])
        for a in st.get("ontgrendeld", []):
            if a[1] == "hol-niveau" and a[0] <= 1500:
                p = per.setdefault(a[2], [0, 0]); p[0] += 1; p[1] += round(a[0], 3) in kt
        t = sorted([a[0] for a in st.get("ontgrendeld", [])] + [a[0] for a in st["aankopen"]])
        t = [x for x in t if 30 < x <= 1200] + [1200]
        gaten.append(max(b - a for a, b in zip([60] + t, t)) / 60)
    print("   %-18s %s | gat mediaan %.1f ergste %.1f min" % (naam, "  ".join("hol%d %d/%d" % (k, v[1], v[0]) for k, v in sorted(per.items()) if k <= 6),
                                                         S.median(gaten), max(gaten)))
