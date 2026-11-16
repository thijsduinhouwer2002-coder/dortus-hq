"""Sanne 16 nov ±21:10 UTC: graafbonus (balans.md, stand 21:00). Goud per val 6 + 3 per bezoek + bonus,
bonus = +1 per STAP zelf gegraven cellen, hooguit MAX. Graver graaft 41 cellen per 20 min (Olafs koper=1), tot 34 cellen.
Speeltestbuild met het nieuwe ritme (28-38 s, 15% paar, plat 30), Brams sim via ../sim-ritme/ritme.py, 40 zaden.
Meet per variant (mediaan, max): koopmomenten 2 tot 6 in min, winkel leeg, goud verdiend na 20 min.
Draai: python3 -I platformen/steam/data/sim-graafbonus/graafbonus.py"""
import os, sys, statistics as S
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "../sim-ritme"))
import ritme as R
OUD = 'erbij = ((6 if SPEL_ECONOMIE else'
def maak(stap, mx, graaft):
    s = R.src.replace(R.OUD_GAT, ('gat = (5, 7) if begin_i == 1 else (18, 22) if begin_i == 2 else (28, 38)\n            else:\n'
                                   '                gat = (28, 38) if t < 1e9 else (40, 60)')).replace("PLAT_S = 60", "PLAT_S = 30")
    s = s.replace(R.OUD_VOLGENDE, 'volgende = t + (rng.uniform(8, 20) if lied_extra > 0 else (rng.uniform(6, 10) if (not stap and rng.random() < 0.15) else rng.uniform(*gat) * (1.0 if stap else eff["gat"])))')
    gb = "min(%d, int(min(34, t * 41 / 1200) // %d))" % (mx, stap) if graaft and stap else "0"
    assert OUD in s
    s = s.replace(OUD, 'erbij = ((6 + %s if SPEL_ECONOMIE else' % gb)
    ns = {"__file__": os.path.join(R.SIM, "sim.py")}
    sys.path.insert(0, R.SIM); exec(s, ns)
    ns["SPEL_ECONOMIE"] = ns["SOORTEN"] = ns["REEKS"] = True
    return ns
def meet(ns):
    k = [[] for _ in range(6)]; leeg = []; g20 = []
    for z in range(1, 41):
        st = ns["speel"](3.0, z, R.spec_build())
        a = [x[0] / 60 for x in st["aankopen"]]
        for i in range(6): k[i].append(a[i] if i < len(a) else 999)
        leeg.append(a[5] if len(a) >= 6 else 999)
    return k
VAR = [("niet graven", 0, 0, False), ("graver, geen bonus", 0, 0, True), ("graver +1/8 tot +3 (KEUS)", 8, 3, True),
       ("graver +1/8 tot +2", 8, 2, True), ("graver +1/4 tot +6", 4, 6, True)]
if __name__ == "__main__":
    print("40 zaden, speeltestbuild nieuw ritme; koop 1..6 in min, mediaan (ergste)")
    for naam, st_, mx, gr in VAR:
        k = meet(maak(st_, mx, gr))
        print("%-28s " % naam + "  ".join("k%d %5.1f (%5.1f)" % (i + 1, S.median(k[i]), max(k[i])) for i in range(6)))
