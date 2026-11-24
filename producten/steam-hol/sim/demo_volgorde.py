"""Demovolgorde van inhoud-100.md nagerekend (Bram, 24 nov 2026, opdracht Sanne 19:30).
Wanneer (open tijd, minuten) vallen de vangsten 2, 4, 6 ... 33 in 20 zaden, en hoe lang is het langste stuk
zonder iets nieuws in de eerste 30 minuten (alleen vrijspelen; en vrijspelen plus aankopen uit de sim).
Economie zoals het spel nu (reeksen(): heldensoorten aan, goud 6 + 3 per bezoek, start 20 goud).
Draaien: python3 demo_volgorde.py [zaden]
"""
import sys
import sim

DREMPELS = [2, 4, 6, 8, 9, 12, 13, 15, 18, 20, 21, 24, 27, 30, 33]
ZADEN = int(sys.argv[1]) if len(sys.argv) > 1 else 20
GRENS = 30 * 60

alle = sim.reeksen(ZADEN, uren=2)

def tijd(st, kolom, d):
    for rij in st["reeks"]:
        if rij[kolom] >= d:
            return rij[0]
    return None

def gat(ts):
    ts = sorted([0.0] + [t for t in ts if t <= GRENS] + [GRENS])
    return max(b - a for a, b in zip(ts, ts[1:]))

for naam, kolom in (("gevangen helden (st['gevallen'])", 2),):
    print("== Vrijspelen op %s, %d zaden, minuten open tijd ==" % (naam, ZADEN))
    print("vangst   min  mediaan  max")
    for d in DREMPELS:
        v = sorted(tijd(st, kolom, d) or 99999 for st in alle)
        print("%5d  %5.1f  %6.1f  %5.1f" % (d, v[0] / 60, v[len(v) // 2] / 60, v[-1] / 60))
    g1 = sorted(gat([tijd(st, kolom, d) or 99999 for d in DREMPELS]) for st in alle)
    g2 = sorted(gat([tijd(st, kolom, d) or 99999 for d in DREMPELS] + [a[0] for a in st["aankopen"]]) for st in alle)
    print("langste stuk zonder vrijspelen, eerste 30 min:        min %.1f, mediaan %.1f, max %.1f" % (g1[0] / 60, g1[len(g1) // 2] / 60, g1[-1] / 60))
    print("langste stuk zonder vrijspelen of aankoop, eerste 30: min %.1f, mediaan %.1f, max %.1f" % (g2[0] / 60, g2[len(g2) // 2] / 60, g2[-1] / 60))
    print("zaden met een stuk boven 3 min (alleen vrijspelen): %d van %d" % (sum(1 for x in g1 if x > 180), ZADEN))
    print()
v = sorted(len([x for x in st["reeks"] if x[0] <= GRENS]) for st in alle)
print("helden binnen in 30 min: min %d, mediaan %d, max %d" % (v[0], v[len(v) // 2], v[-1]))

# Voorstel Bram: vrijspelen op binnengekomen helden (helden_nr in de save van strook.gd), Banana Peel op 2.
VOORSTEL = [2, 6, 8, 10, 13, 15, 18, 21, 23, 26, 29, 31, 34, 37, 40]
for titel, groep in (("zaden 1-%d" % ZADEN, alle), ("zaden 21-40 (controle, niet gebruikt bij het kiezen)", sim.reeksen(40, uren=1)[20:])):
    print("== Voorstel op binnengekomen helden, %s ==" % titel)
    if groep is alle:
        print("helden   min  mediaan  max")
        for d in VOORSTEL:
            v = sorted(tijd(st, 1, d) or 99999 for st in groep)
            print("%5d  %5.1f  %6.1f  %5.1f" % (d, v[0] / 60, v[len(v) // 2] / 60, v[-1] / 60))
    g = sorted(gat([tijd(st, 1, d) or 99999 for d in VOORSTEL]) for st in groep)
    print("langste stuk zonder vrijspelen, eerste 30 min: min %.1f, mediaan %.1f, max %.1f; boven 3 min: %d van %d" % (g[0] / 60, g[len(g) // 2] / 60, g[-1] / 60, sum(1 for x in g if x > 180), len(g)))
    print()
