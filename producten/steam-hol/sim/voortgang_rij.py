"""Bram 16 nov ±16:30 UTC, vraag Sanne 16:00 (voortgang.md "Versie 3 definitief" punt 5): de rij bij de ingang in de sim.
Regel (spec "rij" in sim.py): per keer weg hooguit 4 hol-niveaus meteen, de rest wacht en komt er één per 3 minuten open
spelen bij; eigen faam die de rij inhaalt geeft het niveau meteen.
Neemt voortgang-v3-eind-bram.json (versie 3 definitief, de bouwgetallen) en meet:
1. X = 0, 1, 5, 15, 60 minuten spelen, dan één nacht weg (12 u x 0,25): hol meteen na de nacht, hoeveel niveaus in de rij,
   en hoeveel open minuten na de nacht tot hol 12 (met en zonder rij);
2. de hele voortgang (165 open uur, werkdagen van 6 uur) met en zonder rij: hol 12/20/30/40/50, langste gat per week en
   de langste rij na een nacht per week.
Draaien: python3 voortgang_rij.py > voortgang-rij-uitkomst.txt"""
import copy, json, os
import sim

hier = os.path.dirname(os.path.abspath(__file__))
spec0 = json.load(open(os.path.join(hier, "voortgang-v3-eind-bram.json")))
RIJ = {"meteen": 4, "elke_s": 180}
Z = 8
w = spec0["weg"]
print("Bram 16 nov, de rij bij de ingang (Sanne 16:00). Gemaakt met: python3 voortgang_rij.py   (%d zaden, spec voortgang-v3-eind-bram.json, rij %s)" % (Z, RIJ))
d12 = [nv["drempel"] for nv in spec0["sporen"][0]["niveaus"] if nv["niveau"] == 12][0]

# 1. eerste keer kort spelen, dan één nacht
print("\n1. X minuten spelen, dan één nacht weg (12 u x 0,25 = 3 u tempo; bij 0 min het tempo van het spel: 1 held per 47,5 s, 60% gevangen).")
print("   hol 12 = %d gevangen helden. Mediaan van %d zaden (min tot max tussen haakjes)." % (d12, Z))
print("   %-6s | %-22s | %-18s | %-26s | %-24s | %-22s" % ("X", "hol meteen na de nacht", "niveaus in de rij", "open min na nacht tot hol 12", "open min tot de rij leeg", "zonder rij: hol 12 na"))
for X in (0, 1, 5, 15, 60):
    rijen = []
    for met in (True, False):
        s2 = copy.deepcopy(spec0)
        s2["weg"] = dict(w, open_u=X / 60.0, keer=1)
        s2["uren"] = X / 60.0 + 3.0
        if met:
            s2["rij"] = RIJ
        r = []
        for st in sim.lagen_run(s2, Z):
            tw = st["terug_t"][0] if st.get("terug_t") else st["weg"][0][0]
            hol = [x for x in st.get("ontgrendeld", []) if x[1] == "hol-niveau"]
            meteen = max([x[2] for x in hol if x[0] <= tw] + [1])
            t12 = next((x[0] for x in hol if x[2] == 12), None)
            wacht = st["rij_na_weg"][0][1] if st.get("rij_na_weg") else 0
            tl = next((x[0] for x in hol if x[2] == meteen + wacht), tw)
            r.append((meteen, wacht, None if t12 is None else max(0.0, t12 - tw) / 60, max(0.0, tl - tw) / 60))
        rijen.append(r)
    m, z = rijen

    def mm(v):
        v = [x for x in v if x is not None]
        return "%g (%g tot %g)" % (round(sim.mediaan(v), 1), round(min(v), 1), round(max(v), 1)) if v else "-"
    print("   %-6s | %-22s | %-18s | %-26s | %-24s | %-22s" % ("%g min" % X, mm([x[0] for x in m]), mm([x[1] for x in m]),
                                                            mm([x[2] for x in m]), mm([x[3] for x in m]), mm([x[2] for x in z])))

# 2. de hele voortgang met en zonder rij
wk_s = w["open_u"] * 5 * 3600


def gaten(alle):
    uit = []
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
        uit.append("%.1f / %.1f" % (sim.mediaan(gs) / 3600, max(gs) / 3600))
    return uit


print("\n2. De hele voortgang (165 open uur, 6 uur open per werkdag, weekend dicht), %d zaden:" % Z)
res = {}
for naam, met in (("zonder rij", False), ("met rij", True)):
    s2 = copy.deepcopy(spec0)
    if met:
        s2["rij"] = RIJ
    alle = sim.lagen_run(s2, Z)
    hol = sim.niveau_tijden(alle, "hol-niveau")
    res[naam] = (alle, hol)
    print("   %-10s: hol 12 / 20 / 30 / 40 / 50 op %s open uur" % (naam, " / ".join("%.1f" % (hol[n] / 3600) for n in (12, 20, 30, 40, 50))))
    print("   %-10s  langste gat per week 1 tot 5 (mediaan / ergste, open uren): %s" % ("", "; ".join(gaten(alle))))
    if met:
        per_wk = {}
        for st in alle:
            for t, n in st.get("rij_na_weg", []):
                per_wk.setdefault(int(t // wk_s) + 1, []).append(n)
        print("   %-10s  niveaus in de rij na een nacht, per week (hoogste van alle nachten en zaden; nachten met iets in de rij / alle nachten): %s" % (
            "", "; ".join("week %d: %d (%d/%d)" % (k, max(v), sum(1 for x in v if x), len(v)) for k, v in sorted(per_wk.items()) if k <= 5)))
a, b = res["zonder rij"][1], res["met rij"][1]
verschil = max(abs(a[n] - b[n]) for n in a if n in b and n > 1)
print("   grootste verschil in de mediane tijd van een hol-niveau (2 tot 50): %.1f open minuten" % (verschil / 60))
