"""Bram 16 nov ±15:40 UTC, vraag Sanne 14:50: laatste run van voortgang versie 3.
Neemt voortgang-v3-bram.json (versie 3 vastgesteld) en zet erin:
1. kamertje 4 en 5 van laag 4 pas vrij op hol 47 en 49 (decor "laatste_op_hol"); geen stap 7;
2. de kamertjes van laag 3 vrij zodra laag 3 gebouwd is in plaats van bij het luik naar laag 4 (decor "vrij_gebouwd"),
   want zonder iets te kopen tussen ±55 en 75 u blijft er een gat van een heel hol-niveau (±4 u), wat de drempels ook doen;
3. upgrade stap 4 tot 6 in laag 3 x 1,85 in plaats van x 2,0 (stap 6 was de duurste aankoop van het spel, 3,2 u sparen);
4. drempels hol 36 tot 40 opnieuw geijkt op gelijke afstand tussen hol 35 en 76 open uur (hol 40 iets later, was 75,8).
Schrijft voortgang-v3-eind-bram.json en het rapport (python3 voortgang_v3_eind.py > voortgang-v3-eind-uitkomst.txt).
Daarna: het langste gat per week, hol 40 en 50 in werkdagen, en na hoeveel minuten spelen de eerste nacht weg het hol
tot 12 tilt."""
import copy, json, os
import sim

hier = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(hier, "voortgang-v3-bram.json")))
EIND40 = float(os.environ.get("EIND40", "76"))
spec["decor"]["laatste_op_hol"] = [47, 49]
spec["decor"]["vrij_gebouwd"] = [3]
spec["laag_factor_hoog"][2] = float(os.environ.get("HOOG3", "1.85"))
voor = {nv["niveau"]: nv["drempel"] for nv in spec["sporen"][0]["niveaus"]}
hol = sim.niveau_tijden(sim.lagen_run(spec, 8), "hol-niveau")
t35 = hol[35] / 3600
doel = {"hol-niveau": {n: t35 + (EIND40 - t35) * (n - 35) / 5 for n in range(36, 41)}, "laagsterren": {}, "bewoners": {}}
spec = sim.ijken(spec, doel, sporen=("hol-niveau",))
spec["_uitleg"] = spec["_uitleg"] + (" Versie 3 eind (Bram 16 nov, vraag Sanne 14:50): kamertje 4 en 5 van laag 4 op hol 47 en 49, kamertjes laag 3 vrij "
                                     "als laag 3 gebouwd is, stap 4 tot 6 in laag 3 x %g, hol 36 tot 40 gelijk verdeeld tot %g u. Gemaakt met voortgang_v3_eind.py."
                                     % (spec["laag_factor_hoog"][2], EIND40))
uit = os.path.join(hier, "voortgang-v3-eind-bram.json")
json.dump(spec, open(uit, "w"), indent=1, ensure_ascii=False)
print("Bram 16 nov, voortgang versie 3 eind. Gemaakt met: python3 voortgang_v3_eind.py (EIND40=%g HOOG3=%g)\n" % (EIND40, spec["laag_factor_hoog"][2]))
alle = sim.lagen(uit, (750, 1650, 3000), [45, 126, 353, 600, 1000, 1600], False, factor=spec["laag_factor"], gloop_oud=False, spec=spec)
na = {nv["niveau"]: nv["drempel"] for nv in spec["sporen"][0]["niveaus"]}
print("  drempels hol 35 tot 41 (gevangen helden), versie 3 -> eind: " + "  ".join("%d: %d->%d" % (n, voor[n], na[n]) for n in range(35, 42)))

w = spec["weg"]
wk_s = w["open_u"] * 5 * 3600
print("\n  langste gat per week (open uren, van ontgrendeling of aankoop tot de volgende; mediaan / ergste van 8 zaden), en waar:")
for k in range(6):
    a, b = k * wk_s, (k + 1) * wk_s
    gs = []
    for st in alle:
        ev = sorted([(x[0], "hol %s" % x[2] if x[1] == "hol-niveau" else "%s %s" % (x[1], x[2])) for x in st.get("ontgrendeld", [])] +
                    [(x[0], x[1]) for x in st["aankopen"]])
        prev = (0.0, "start")
        best = (0.0, "")
        for t, wat in ev:
            if a < t <= b and t - prev[0] > best[0]:
                best = (t - prev[0], "%.0f-%.0f u, na %s tot %s" % (prev[0] / 3600, t / 3600, prev[1], wat))
            prev = (t, wat)
        gs.append(best)
    gs.sort()
    if gs[-1][0] == 0:
        print("    week %d: niets meer" % (k + 1))
        break
    print("    week %d: %.1f u / %.1f u  (ergste: %s)" % (k + 1, sim.mediaan([g[0] for g in gs]) / 3600, gs[-1][0] / 3600, gs[-1][1]))
hol = sim.niveau_tijden(alle, "hol-niveau")
for n in (40, 50):
    s = hol[n]
    d = int(s // (w["open_u"] * 3600)) + 1
    print("  hol %d: %.1f open uur = werkdag %d (week %d dag %d)" % (n, s / 3600, d, (d - 1) // 5 + 1, (d - 1) % 5 + 1))

# extra: na hoeveel minuten spelen tilt een eerste nacht weg (12 uur dicht, x 0,25) het hol tot 12?
print("\n  extra: eerste keer X minuten spelen, dan een nacht weg (plafond 12 u x 0,25 = 3 u tempo van het laatste uur):")
drempel12 = na[12]
rij = []
for X in (1, 1.5, 2, 3, 4, 5, 7, 10, 15, 20, 30, 45, 60):
    s2 = copy.deepcopy(spec)
    s2["weg"] = dict(w, open_u=X / 60)
    s2["uren"] = X / 60 + 0.02
    ok, lv = 0, []
    for st in sim.lagen_run(s2, 8):
        h = max([x[2] for x in st.get("ontgrendeld", []) if x[1] == "hol-niveau"] + [1])
        lv.append(h)
        ok += h >= 12
    rij.append((X, sim.mediaan(lv), ok))
print("    hol 12 = %d gevangen helden. minuten spelen: hol na de nacht (mediaan), zaden met hol 12 of hoger van 8" % drempel12)
print("    " + "  ".join("%g min: hol %g (%d/8)" % r for r in rij))
eerste = next((r[0] for r in rij if r[2] >= 4), None)
print("    eerste keer bij de helft van de zaden: %s minuten" % eerste)
