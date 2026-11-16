"""Sanne 16 nov ±19:15 UTC: waar zit het ergste gat in de speeltestbuild, en helpen hol 5 / 6 / 7 eerder (op vangsten die niet op een koop vallen)?"""
import prijsladder as P, sim, statistics as S
from collections import Counter
NU = [45, 126, 353]
def loop(dr, prijzen=NU, verbose=False):
    P.DR.clear(); P.DR.update(dr)
    sp = P.spec(prijzen); g = []; plek = Counter(); samen = 0; hol7 = []
    for z in P.ZADEN:
        st = sim.speel(0.6, z, sp)
        ka = [a[0] for a in st["aankopen"]]
        hol = [a for a in st.get("ontgrendeld", []) if a[1] == "hol-niveau"]
        samen += sum(1 for a in hol if any(abs(a[0] - k) < 1e-3 for k in ka) and a[0] <= 1200)
        ev = sorted([(a[0], "hol%d" % a[2]) for a in st.get("ontgrendeld", [])] + [(k, "koop") for k in ka])
        ev = [e for e in ev if 30 < e[0] <= 1200] + [(1200, "eind")]
        prev = (60, "start"); best = (0, None)
        for e in ev:
            if e[0] - prev[0] > best[0]: best = (e[0] - prev[0], prev[1] + ">" + e[1])
            prev = e
        g.append(best[0] / 60); plek[best[1]] += 1
        h7 = [a[0] for a in hol if a[2] == 7]; hol7.append(h7[0] / 60 if h7 else 99)
        if verbose and z <= 3:
            print("   zaad", z, " ".join("%.1f:%s" % (e[0] / 60, e[1]) for e in ev))
    return max(g), S.median(g), samen, plek.most_common(3), S.median(hol7)
if __name__ == "__main__":
    print("Tijdlijn nu (3/5/7/12/17, upgrades 45/126/353, minuten):")
    loop({3: 5, 4: 7, 6: 17}, verbose=True)
    r = loop({3: 5, 4: 7, 6: 17}); print("nu 3/5/7/12/17: ergste %.1f mediaan %.1f samen %d, hol 7 mediaan %.1f min, gat zit meestal: %s" % (r[0], r[1], r[2], r[4], r[3]))
    uit = []
    for d5 in range(8, 15):
        for d6 in range(d5 + 2, 20):
            for d7 in (21, 23, 25):
                if d7 <= d6 + 1: continue
                r = loop({3: 5, 4: 7, 5: d5, 6: d6, 7: d7})
                uit.append((r[0], r[1], r[2], (3, 5, 7, d5, d6, d7), r[4]))
    uit.sort()
    print("Beste reeksen (hol 2 tot 7):")
    for r in uit[:12]:
        print("  ergste %.1f mediaan %.1f samen %d  drempels %s  hol 7 mediaan %.1f min" % r)
