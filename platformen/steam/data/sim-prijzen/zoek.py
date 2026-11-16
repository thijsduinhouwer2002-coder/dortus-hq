"""Sanne 16 nov: zoek een ladder (stap 1, 2, 3 per soort) met het kleinste ergste gat in minuut 1 tot 20 (speeltestbuild)."""
import prijsladder as P, statistics as S, sim, itertools
uit = []
for p1 in (25, 30, 35, 40, 45):
    for p2 in (50, 60, 70, 80, 90, 100, 126):
        if p2 <= p1: continue
        for p3 in (200, 250, 353):
            sp = P.spec([p1, p2, p3]); g = []; k = []
            for z in P.ZADEN:
                st = sim.speel(0.6, z, sp)
                ka = [a[0] for a in st["aankopen"]]
                t = sorted([a[0] for a in st.get("ontgrendeld", [])] + ka)
                t = [x for x in t if 30 < x <= 1200] + [1200]
                g.append(max(b - a for a, b in zip([60] + t, t)) / 60)
                k.append(sum(1 for x in ka if x <= 1200))
            uit.append((max(g), S.median(g), S.median(k), (p1, p2, p3)))
uit.sort()
for r in uit[:15]:
    print("ergste %.1f mediaan %.1f kopen20 %d  ladder %s" % r)
