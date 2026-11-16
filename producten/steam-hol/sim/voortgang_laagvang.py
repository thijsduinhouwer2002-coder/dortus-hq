"""Bram 16 nov ±16:45 UTC: hoeveel mogen de eigen helden per laag kosten? (voortgang.md "Wat nog niet klopt" punt 2)
De mijnwerker (laag 2, graaft om je eerste val heen) en de archeoloog (laag 3, onthoudt elke val) zitten nog niet in de sim.
Hoe vaak ze komen en hoe goed hun tegenzet (valluik, nep-schat) werkt, is nog niet ontworpen. Daarom geen GOK-model,
maar een gevoeligheid: de vangkans in laag 2, 3 en 4 x een factor ("laag_vang" in sim.py), en kijken wat er met de
bouwgetallen van versie 3 definitief gebeurt (hol 20/30/40/50, werkdag van hol 50, langste gat per week).
Draaien: python3 voortgang_laagvang.py > voortgang-laagvang-uitkomst.txt"""
import copy, json, os
import sim

hier = os.path.dirname(os.path.abspath(__file__))
spec0 = json.load(open(os.path.join(hier, "voortgang-v3-eind-bram.json")))
Z = 8
w = spec0["weg"]
wk_s = w["open_u"] * 5 * 3600
GEVALLEN = [
    ("versie 3 definitief (alles x 1)", None),
    ("laag 2 tot 4 x 0,9", [1, 0.9, 0.9, 0.9]),
    ("laag 2 tot 4 x 0,8", [1, 0.8, 0.8, 0.8]),
    ("laag 2 x 0,9, laag 3 en 4 x 0,8", [1, 0.9, 0.8, 0.8]),
    ("laag 2 tot 4 x 0,7", [1, 0.7, 0.7, 0.7]),
    ("laag 2 tot 4 x 1,1 (tegenzet wint)", [1, 1.1, 1.1, 1.1]),
]
print("Bram 16 nov, gevoeligheid vangkans per laag. Gemaakt met: python3 voortgang_laagvang.py   (%d zaden, spec voortgang-v3-eind-bram.json, 165 open uur, 6 uur open per werkdag)" % Z)
print("Kolommen: hol 20 / 30 / 40 / 50 in open uren (mediaan), werkdag van hol 50,")
print("langste gat per week 1 tot 5 (mediaan / ergste, open uren).\n")
for naam, lv in GEVALLEN:
    s2 = copy.deepcopy(spec0)
    if lv:
        s2["laag_vang"] = lv
    alle = sim.lagen_run(s2, Z)
    hol = sim.niveau_tijden(alle, "hol-niveau")
    tijd = lambda n: "%.1f" % (hol[n] / 3600) if n in hol else "niet"
    d50 = "werkdag %d" % (int(hol[50] // (w["open_u"] * 3600)) + 1) if 50 in hol else "niet binnen 165 u"
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
    print("%-36s hol %s / %s / %s / %s u, hol 50 %s" % (naam, tijd(20), tijd(30), tijd(40), tijd(50), d50))
    print("%-36s gaten %s" % ("", "; ".join(gs_w)))
