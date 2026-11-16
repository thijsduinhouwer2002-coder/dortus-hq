"""Sanne 16 nov ±19:20 UTC: dezelfde reeksen over minuut 1 tot 40 (wordt het gat na minuut 20 niet groter?)."""
import prijsladder as P, sim, statistics as S
def gat(dr, eind):
    P.DR.clear(); P.DR.update(dr); sp = P.spec([45, 126, 353]); g = []; samen = 0
    for z in P.ZADEN:
        st = sim.speel(eind / 3600 + 0.1, z, sp)
        ka = [a[0] for a in st["aankopen"]]
        samen += sum(1 for a in st.get("ontgrendeld", []) if a[1] == "hol-niveau" and a[0] <= eind and any(abs(a[0] - k) < 1e-3 for k in ka))
        t = sorted([a[0] for a in st.get("ontgrendeld", [])] + ka)
        t = [x for x in t if 30 < x <= eind] + [eind]
        g.append(max(b - a for a, b in zip([60] + t, t)) / 60)
    return max(g), S.median(g), samen
for naam, dr in [("nu 3/5/7/12/17/25", {3: 5, 4: 7, 6: 17}), ("3/5/7/9/14/25", {3: 5, 4: 7, 5: 9, 6: 14}),
                 ("3/5/7/9/14/21", {3: 5, 4: 7, 5: 9, 6: 14, 7: 21}), ("3/5/7/8/14/21", {3: 5, 4: 7, 5: 8, 6: 14, 7: 21})]:
    a = gat(dr, 1200); b = gat(dr, 2400); c = gat(dr, 3600)
    print("%-20s min 1-20 ergste %.1f med %.1f samen %d | 1-40 ergste %.1f med %.1f samen %d | 1-60 ergste %.1f med %.1f samen %d" % ((naam,) + a + b + c))
