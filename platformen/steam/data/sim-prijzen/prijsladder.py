"""Sanne 16 nov ±19:05 UTC: het gat tussen minuut 5 en 20 in de speeltestbuild (Bram 18:50: er is daar maar één upgrade te koop).
Vraag: lost een andere prijsladder (45 x f^n per soort, twee soorten) het op, zonder nieuwe feature?
Zelfde opzet als producten/steam-hol/sim/samenval.py deel 3 (graven gratis, drempels hol 3/5/7/12/17, 40 zaden).
Draai: python3 prijsladder.py"""
import sys, os, json, copy, statistics as S
SIM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../producten/steam-hol/sim")
sys.path.insert(0, os.path.abspath(SIM))
import sim
base = json.load(open(os.path.join(SIM, "voortgang-v3-eind-bram.json")))
sim.SPEL_ECONOMIE, sim.SOORTEN, sim.REEKS = True, True, True
ZADEN = range(1, 41)
DR = {3: 5, 4: 7, 6: 17}

def spec(prijzen):
    s = copy.deepcopy(base)
    for n in s["sporen"][0]["niveaus"]:
        if n["niveau"] in DR:
            n["drempel"] = DR[n["niveau"]]
    s["graven"] = False
    s["upg_prijs"] = list(prijzen) + [99999] * (6 - len(prijzen))
    return s

def meet(naam, prijzen, uren=0.6, eind=1200):
    sp = spec(prijzen); gaten = []; kopen20 = []; kooptijd = [[] for _ in range(6)]; op = []
    for z in ZADEN:
        st = sim.speel(uren, z, sp)
        ka = [a[0] for a in st["aankopen"]]
        for i, x in enumerate(ka[:6]):
            kooptijd[i].append(x / 60)
        kopen20.append(sum(1 for x in ka if x <= eind))
        t = sorted([a[0] for a in st.get("ontgrendeld", [])] + ka)
        t = [x for x in t if 30 < x <= eind] + [eind]
        gaten.append(max(b - a for a, b in zip([60] + t, t)) / 60)
        if len(ka) >= 6:
            op.append(ka[5] / 60)
    kt = "  ".join("k%d %.1f" % (i + 1, S.median(v)) if len(v) >= 20 else "k%d -" % (i + 1) for i, v in enumerate(kooptijd))
    print("%-22s gat mediaan %4.1f ergste %4.1f min | kopen in 20 min mediaan %d | %s" % (
        naam, S.median(gaten), max(gaten), S.median(kopen20), kt))

if __name__ == "__main__":
    print("Speeltestbuild, graven gratis, drempels 3/5/7/12/17, 40 zaden, minuut 1 tot 20. k = mediaan minuut van koop n")
    for naam, p in [("nu 45/126/353", [45, 126, 353]),
                    ("45 x 2,2: 45/99/218", [45, 99, 218]),
                    ("45 x 2,0: 45/90/180", [45, 90, 180]),
                    ("45 x 1,8: 45/81/146", [45, 81, 146]),
                    ("40/80/160", [40, 80, 160]),
                    ("45/75/200", [45, 75, 200]),
                    ("45/70/250", [45, 70, 250])]:
        meet(naam, p)
    print()
    print("Zelfde, maar wanneer is de winkel op (koop 6), 3 uur spelen, mediaan minuut:")
    for naam, p in [("nu 45/126/353", [45, 126, 353]), ("45 x 2,0: 45/90/180", [45, 90, 180]), ("45/75/200", [45, 75, 200]), ("45/70/250", [45, 70, 250])]:
        sp = spec(p); v = []
        for z in range(1, 11):
            st = sim.speel(3.0, z, sp)
            ka = [a[0] for a in st["aankopen"]]
            v.append(ka[5] / 60 if len(ka) >= 6 else 999)
        print("  %-22s winkel op na mediaan %.0f min (min %.0f, max %.0f)" % (naam, S.median(v), min(v), max(v)))
