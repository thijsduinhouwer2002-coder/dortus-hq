"""Bram 16 nov ±18:00 UTC: de eigen helden per laag met hun tegenzet nagerekend (vraag Sanne 17:00, voortgang.md
"Eigen helden per laag en hun tegenzet"). Spec versie 3 definitief (voortgang-v3-eind-bram.json) plus "laag_helden" in sim.py.
Doel van Sanne: per laag met tegenzet gemiddelde vangkans x 1,0 tot 1,05 van versie 3; in het ene niveau tussen held en
tegenzet mag het zakken tot ±x 0,95. Wat de held doet blijft; alleen de getallen van de tegenzet mogen anders.
Aannames (staan niet in de tekst van Sanne): een tegenzet koop je één keer voor ±1 uur goud (prijs_u 1,0 x goud per uur op
het moment dat hij vrijkomt) en hij zit daarna in elke nieuwe laag; het valluik vangt alleen de mijnwerker (die graaft erin),
gewone helden lopen eroverheen; de lokker hangt voor de eerste val; de Gekroonde zit er niet in (telt niet mee, zegt Sanne).
Draaien: python3 voortgang_laaghelden.py > voortgang-laaghelden-uitkomst.txt"""
import copy, json, os
import sim

hier = os.path.dirname(os.path.abspath(__file__))
spec0 = json.load(open(os.path.join(hier, "voortgang-v3-eind-bram.json")))
Z = 8
w = spec0["weg"]
wk_s = w["open_u"] * 5 * 3600

HELDEN = {"mijnwerker": {"hol": 21, "laag": 2, "gewicht": 20}, "ontdekker": {"hol": 31, "laag": 3, "gewicht": 15},
          "heks": {"hol": 36, "laag": 3, "gewicht": 10}, "hoedenjager": {"hol": 41, "laag": 4, "gewicht": 15}}


def tegen(valluik=0.8, nep=(0.75, 0.5, 0.3), lokker=True, prijs_u=1.0):
    t = {"valluik": {"hol": 22, "prijs_u": prijs_u, "kans": valluik},
         "nephoard": {"hol": 32, "prijs_u": prijs_u, "kans": nep[0], "hebzuchtig": nep[1], "schijterig": nep[2]}}
    if lokker:
        t["lokker"] = {"hol": 41, "prijs_u": prijs_u}
    return t


GEVALLEN = [
    ("versie 3 (geen eigen helden)", {"helden": {}, "tegen": {}}),
    ("helden zonder tegenzet", {"helden": HELDEN, "tegen": {}}),
    ("Sanne: valluik 0,8, nep 0,75/0,5/0,3, lokker x 2", {"helden": HELDEN, "tegen": tegen()}),
]
import sys
if len(sys.argv) > 1 and sys.argv[1] == "ijk":
    GEVALLEN = GEVALLEN[:1] + [
        ("Sanne, tegenzet voor 0,5 uur goud", {"helden": HELDEN, "tegen": tegen(prijs_u=0.5)}),
        ("Sanne, tegenzet voor 0,25 uur goud", {"helden": HELDEN, "tegen": tegen(prijs_u=0.25)}),
        ("Sanne, tegenzet voor 2 uur goud", {"helden": HELDEN, "tegen": tegen(prijs_u=2.0)}),
        ("Sanne zonder lokker", {"helden": HELDEN, "tegen": tegen(lokker=False)}),
        ("valluik 0,9, nep 0,75/0,4/0,25", {"helden": HELDEN, "tegen": tegen(0.9, (0.75, 0.4, 0.25))}),
    ]


def vang(alle, test):
    g = n = 0
    for st in alle:
        for t, laag, hol, soort, ja in st.get("vang_log", []):
            if test(laag, hol, soort):
                n += 1
                g += ja
    return g / n if n else float("nan"), n


VAKKEN = [("laag 2, hol 21", lambda L, h, s: L == 2 and h == 21), ("laag 2, hol 22+", lambda L, h, s: L == 2 and h >= 22),
          ("laag 3, hol 31", lambda L, h, s: L == 3 and h == 31), ("laag 3, hol 32+", lambda L, h, s: L == 3 and h >= 32),
          ("laag 4, hol 41+", lambda L, h, s: L == 4 and h >= 41), ("laag 2 heel", lambda L, h, s: L == 2),
          ("laag 3 heel", lambda L, h, s: L == 3), ("laag 4 heel", lambda L, h, s: L == 4)]

print("Bram 16 nov, eigen helden per laag met tegenzet. Gemaakt met: python3 voortgang_laaghelden.py %s  (%d zaden, spec voortgang-v3-eind-bram.json, 165 open uur, 6 uur open per werkdag)"
      % (" ".join(sys.argv[1:]), Z))
print("Vangkans = gevangen / helden in de laag die je ziet (alle helden, ook gewone). Tussen haakjes: x tegen versie 3.")
print("Daaronder: hol 20 / 30 / 40 / 50 in open uren (mediaan), werkdag van hol 50, langste gat per week 1 tot 5 (mediaan / ergste).\n")
basis = None
for naam, lh in GEVALLEN:
    s2 = copy.deepcopy(spec0)
    s2["laag_helden"] = lh
    alle = sim.lagen_run(s2, Z)
    vk = [vang(alle, f) for _, f in VAKKEN]
    if basis is None:
        basis = vk
    hol = sim.niveau_tijden(alle, "hol-niveau")
    tijd = lambda n: "%.1f" % (hol[n] / 3600) if n in hol and hol[n] is not None else "niet"
    d50 = "werkdag %d" % (int(hol[50] // (w["open_u"] * 3600)) + 1) if hol.get(50) else "niet binnen 165 u"
    gs_w = []
    for k in range(5):
        a, b = k * wk_s, (k + 1) * wk_s
        gs = []
        for st in alle:
            ev = sorted([x[0] for x in st.get("ontgrendeld", [])] + [x[0] for x in st["aankopen"]])
            prev, best = 0.0, 0.0
            for t in ev:
                if a < t <= b:
                    best = max(best, t - prev)
                prev = t
            gs.append(best)
        gs_w.append("%.1f/%.1f" % (sim.mediaan(gs) / 3600, max(gs) / 3600))
    print(naam)
    print("  " + "; ".join("%s %.3f (x %.2f)" % (VAKKEN[i][0], v[0], v[0] / basis[i][0]) for i, v in enumerate(vk)))
    tk = [sorted(t for t, wat in st["aankopen"] if wat.startswith("tegen_")) for st in alle]
    tk_t = ", ".join("%s" % "/".join("%.1f" % (x / 3600) for x in r) for r in tk[:3])
    soorten = {}
    for st in alle:
        for t, L, h, s, ja in st.get("vang_log", []):
            if s in HELDEN:
                d = soorten.setdefault(s, [0, 0])
                d[0] += 1
                d[1] += ja
    print("  eigen helden (bezoeken, gevangen): " + ", ".join("%s %d %.0f%%" % (s, d[0] / Z, 100 * d[1] / d[0]) for s, d in soorten.items())
          + ("; tegenzet gekocht op (open uur, zaad 1 tot 3): " + tk_t if any(tk) else ""))
    print("  hol %s / %s / %s / %s u, hol 50 %s" % (tijd(20), tijd(30), tijd(40), tijd(50), d50))
    print("  gaten " + "; ".join(gs_w))
    print()
