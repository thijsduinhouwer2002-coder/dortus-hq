"""Bram 16 nov ±17:30 UTC: een echte speler koopt niet meteen (voortgang.md "Wat nog niet klopt" punt 5: "de sim koopt alles
meteen; een echte speler klikt minder, dus het gaat eerder langzamer"). Hoeveel langzamer?
Nieuwe sleutel "koop_elke_s" in sim.py: de speler kijkt hooguit elke X open seconden in de winkel en koopt dan alles wat kan
(goedkoopste eerst), en kijkt altijd meteen als hij het spel weer opent na weg zijn. Spec versie 3 definitief, met de eigen
helden per laag en hun tegenzet (Sanne 17:00, getallen ongewijzigd).
Draaien: python3 voortgang_kijken.py > voortgang-kijken-uitkomst.txt"""
import copy, json, os
import sim
import contextlib, io, sys
with contextlib.redirect_stdout(io.StringIO()):   # voortgang_laaghelden rekent bij import zijn eigen tabel; die tonen we niet
    _argv, sys.argv = sys.argv, sys.argv[:1]
    import voortgang_laaghelden as V
    sys.argv = _argv

hier = os.path.dirname(os.path.abspath(__file__))
spec0 = json.load(open(os.path.join(hier, "voortgang-v3-eind-bram.json")))
spec0["laag_helden"] = {"helden": V.HELDEN, "tegen": V.tegen()}
Z = 8


def gaten(alle, wk_s, weken):
    uit = []
    for k in range(weken):
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
        uit.append("%.1f/%.1f" % (sim.mediaan(gs) / 3600, max(gs) / 3600))
    return "; ".join(uit)


def bank(alle):
    # mediaan van het goud dat op de bank ligt aan het eind van elk open uur, uur 20 tot 120 (wat de speler laat liggen)
    v = [g for st in alle for g in st.get("bank", [])[20:120]]
    return sim.mediaan(v) if v else 0.0


print("Bram 16 nov, de speler die niet meteen koopt. Gemaakt met: python3 voortgang_kijken.py   (%d zaden, spec voortgang-v3-eind-bram.json + eigen helden met tegenzet)" % Z)
print("Deel 1: werkdagen van 6 uur open (weg x 0,25, plafond 12 u). Hol in open uren (mediaan), werkdag van hol 50,")
print("langste gat per week 1 tot 5 (mediaan / ergste, open uren; een aankoop telt als iets nieuws), goud op de bank (mediaan uur 20 tot 120).\n")
w = spec0["weg"]
for naam, ks in [("koopt meteen (zoals tot nu)", None), ("kijkt elke 10 min", 600), ("kijkt elke 30 min", 1800),
                 ("kijkt elk uur", 3600), ("kijkt elke 2 uur", 7200), ("kijkt alleen bij het openen (1 x per dag)", 10 ** 7)]:
    s2 = copy.deepcopy(spec0)
    if ks:
        s2["koop_elke_s"] = ks
    alle = sim.lagen_run(s2, Z)
    hol = sim.niveau_tijden(alle, "hol-niveau")
    tijd = lambda n: "%.1f" % (hol[n] / 3600) if hol.get(n) else "niet"
    d50 = "werkdag %d" % (int(hol[50] // (w["open_u"] * 3600)) + 1) if hol.get(50) else "niet binnen 165 u"
    print("%-42s hol 12 / 20 / 30 / 40 / 50: %s / %s / %s / %s / %s u, hol 50 %s, bank %d" % (
        naam, tijd(12), tijd(20), tijd(30), tijd(40), tijd(50), d50, bank(alle)))
    print("%-42s gaten %s" % ("", gaten(alle, w["open_u"] * 5 * 3600, 5)))

print("\nDeel 2: de tussendoor-speler, elke dag M minuten open, rest dicht (ook weekend). Dag van hol 20 / 30 / 40 / 50.\n")
for M in (15, 30, 60):
    for naam, ks in [("koopt meteen", None), ("kijkt alleen bij het openen", 10 ** 7)]:
        s2 = copy.deepcopy(spec0)
        s2["weg"] = dict(spec0["weg"], open_u=M / 60.0)
        s2["uren"] = 90 * M / 60.0
        if ks:
            s2["koop_elke_s"] = ks
        alle = sim.lagen_run(s2, Z)
        hol = sim.niveau_tijden(alle, "hol-niveau")
        dag = lambda n: "dag %d" % (int(hol[n] // (M * 60)) + 1) if hol.get(n) else "na dag 90"
        print("%2d min per dag, %-28s hol 20 %s, hol 30 %s, hol 40 %s, hol 50 %s" % (M, naam, dag(20), dag(30), dag(40), dag(50)))
