"""Bram 16 nov ±16:25 UTC: de tussendoor-speler met de rij bij de ingang (T1 van voortgang.md).
Wie het spel elke dag maar kort open heeft (15, 30 of 60 minuten) en de rest van de dag dicht (12 uur plafond x 0,25 =
elke dag 3 uur tempo erbij): hoeveel dagen tot hol 12, 20, 30, 40, en hoe lang wordt de rij (stapelt hij op, of loopt hij
leeg in de open minuten)? Met en zonder rij, spec versie 3 definitief.
Draaien: python3 voortgang_tussendoor.py > voortgang-tussendoor-uitkomst.txt"""
import copy, json, os
import sim

hier = os.path.dirname(os.path.abspath(__file__))
spec0 = json.load(open(os.path.join(hier, "voortgang-v3-eind-bram.json")))
RIJ = {"meteen": 4, "elke_s": 180}
Z = 8
DAGEN = 80
print("Bram 16 nov, de tussendoor-speler. Gemaakt met: python3 voortgang_tussendoor.py   (%d zaden, %d dagen, spec voortgang-v3-eind-bram.json, rij %s)" % (Z, DAGEN, RIJ))
print("Elke dag M minuten open, daarna dicht (12 u x 0,25 = 3 u tempo van het laatste open uur, of minder als je minder dan een uur speelde).")
print("Dag n = de n-de keer open; hol aan het eind van die open tijd. Mediaan van %d zaden.\n" % Z)
for M in (15, 30, 60):
    for met in (False, True):
        s2 = copy.deepcopy(spec0)
        s2["weg"] = dict(spec0["weg"], open_u=M / 60.0)
        s2["uren"] = DAGEN * M / 60.0
        if met:
            s2["rij"] = RIJ
        alle = sim.lagen_run(s2, Z)
        hol = sim.niveau_tijden(alle, "hol-niveau")
        dag = lambda n: "dag %d" % (int(hol[n] // (M * 60)) + 1) if n in hol else "na dag %d" % DAGEN
        rij_max = max([n for st in alle for _, n in st.get("rij_na_weg", [])] + [0])
        rij_dag = {}
        for st in alle:
            for t, n in st.get("rij_na_weg", []):
                rij_dag.setdefault(int(t // (M * 60)) + 1, []).append(n)
        print("%2d min per dag, %-10s: hol 12 %s, hol 20 %s, hol 30 %s, hol 40 %s, hol 50 %s" % (M, "met rij" if met else "zonder rij", dag(12), dag(20), dag(30), dag(40), dag(50)))
        if met:
            print("   %-24s rij bij het openen (mediaan per dag): %s; langste rij %d" % ("", ", ".join(
                "dag %d: %g" % (d, sim.mediaan(v)) for d, v in sorted(rij_dag.items()) if d <= 10 and sim.mediaan(v) > 0) or "nooit iets", rij_max))
