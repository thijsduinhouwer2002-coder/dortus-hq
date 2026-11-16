"""Bram 16 nov ±22:30 UTC (Sanne 22:00): versie 3 nog een keer, nu met de nieuwe weg-regel (balans.md bovenaan, Iris keuring 9):
SNELHEID weg 0,25 naar 0,12, en faam uit een keer weg telt hooguit tot de drempel van huidig hol-niveau + 2.
Basis zoals v3ritme.py (nieuw ritme 28 tot 38 s, 15% paar, Gloop 30 s plat, graafbonus +1 per 8 cellen, hooguit +3).
Drempels boven hol 12 (en Gloop, laagsterren, bewoners) x f; hol 2 tot 12 blijven (demo). Prijzen gelijk.
De sim-tijd is open tijd; na elke 6 open uur is het spel dicht (12 uur plafond, x factor van het tempo van het laatste uur).
Draai: python3 -I platformen/steam/data/sim-v3-weg/v3weg.py producten/steam-hol/sim 30 170 1.7 1.5 1.4"""
import os, sys, json, copy, statistics as S
SIM = sys.argv[1]; ZADEN = int(sys.argv[2]); UREN = float(sys.argv[3]); FS = [float(x) for x in sys.argv[4:]] or [1.7]
# Sinds 22:30 rekent sim.py het nieuwe ritme, de graafbonus en het weg-plafond zelf (sleutels "ritme", "graafbonus",
# weg "faam_niveaus"); dit script zet die sleutels op de oude v3-spec (voortgang-v3-eind-bram.json) en rekt de drempels.
sys.path.insert(0, SIM)
import sim as ns_mod
ns = vars(ns_mod)
spec0 = json.load(open(os.path.join(SIM, "voortgang-v3-eind-bram.json")))
spec0["uren"] = UREN
spec0["ritme"] = "nieuw"
spec0["graafbonus"] = {"per": 8, "max": 3}
def rek(spec, f, weg):
    s_ = copy.deepcopy(spec)
    for sp in s_["sporen"]:
        for nv in sp["niveaus"]:
            if not (sp["naam"] == "hol-niveau" and nv["niveau"] <= 12):
                nv["drempel"] = round(nv["drempel"] * f)
    s_["weg"].update(weg)
    return s_
print("%d zaden, %g open uur; mediaan open uur tot hol-niveau (- = minder dan de helft haalt het)" % (ZADEN, UREN))
print("werkdag = 6 open uur; hol 50 op open uur u valt op werkdag u/6 + 1")
gevallen = [("weg 0,25 zonder plafond (zoals 21:17)", {"factor": 0.25}, 1.7)]
for f in FS:
    gevallen.append(("weg 0,12, faam hooguit +2 niveaus", {"factor": 0.12, "faam_niveaus": 2}, f))
for naam, weg, f in gevallen:
    alle = ns["lagen_run"](rek(spec0, f, weg), ZADEN, UREN)
    nt = ns["niveau_tijden"](alle, "hol-niveau")
    h = lambda n: ("%.1f" % (nt[n] / 3600)) if nt.get(n) else "-"
    wg = [g for st in alle for (t, g) in st.get("weg", []) if t < 7 * 3600]
    af = S.median([st.get("weg_faam_af", 0.0) for st in alle])
    print("%-38s x%.2f | hol 12 %s u | 20 %s | 30 %s | 40 %s | 50 %s | goud 1e nacht %.0f | weg-faam afgekapt (mediaan, totaal) %.0f"
          % (naam, f, h(12), h(20), h(30), h(40), h(50), S.median(wg) if wg else 0, af), flush=True)

# Verslag voor de gekozen factor (laatste getal van de regel als KEUS=..), plus een toets of het plafond werkt:
# vroeg in het spel (30 of 60 min spelen, één nacht weg) moet de nacht hooguit 2 hol-niveaus geven.
KEUS = float(os.environ.get("KEUS", "0") or 0)
if KEUS:
    print("\n== verslag x%.2f, weg 0,12, faam hooguit +2 niveaus ==" % KEUS)
    # VERGELIJK=1: zelfde verslag met de oude weg (0,25, geen plafond) en x1,7, zoals 21:17
    ns["lagen"](None, zaden=ZADEN, spec=rek(spec0, KEUS, {"factor": 0.25} if os.environ.get("VERGELIJK") else {"factor": 0.12, "faam_niveaus": 2}))
    print("\n== toets plafond: X min spelen, één nacht (12 u plafond) weg, daarna 1 open uur ==")
    for minuten in (30, 60):
        for plafond in (False, True):
            w = {"factor": 0.12, "open_u": minuten / 60.0, "keer": 1}
            if plafond:
                w["faam_niveaus"] = 2
            alle = ns["lagen_run"](rek(spec0, KEUS, w), ZADEN, minuten / 60.0 + 0.02)
            voor, na = [], []
            for st in alle:
                tw = st["weg"][0][0]
                hv = max([1] + [n for (t, sp, n, _) in st.get("ontgrendeld", []) if sp == "hol-niveau" and t < tw])
                hn = max([1] + [n for (t, sp, n, _) in st.get("ontgrendeld", []) if sp == "hol-niveau"])
                voor.append(hv); na.append(hn)
            print("  %d min, %-12s hol voor de nacht %s, na de nacht %s, erbij hooguit %d" % (
                minuten, "met plafond" if plafond else "zonder", S.median(voor), S.median(na), max(b - a for a, b in zip(voor, na))))
