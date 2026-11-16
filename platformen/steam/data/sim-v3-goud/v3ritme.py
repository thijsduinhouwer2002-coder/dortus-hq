"""Bram 16 nov ±21:30 UTC: versie 3 (voortgang-v3-eind-bram.json, 4 lagen, graven kost goud) met het nieuwe ritme van
Sanne (op main sinds 16 nov 20:50: 28 tot 38 s, 15% paar van 6 tot 10 s, Gloop 30 s plat, geen 40 tot 60 meer).
De v3-tijden in voortgang.md zijn met het oude ritme (35 tot 45, daarna 40 tot 60, plat 60) gemaakt.
Zelfde vervanging in de bron als Sannes sim-graafbonus/graafbonus.py. Goud: vast 6, of met graafbonus.
Laatste regel: alle drempels boven hol 12 (en van Gloop, laagsterren, bewoners) x 1,7, de verhouding helden per uur nieuw/oud.
Draai: python3 -I platformen/steam/data/sim-v3-goud/v3ritme.py producten/steam-hol/sim 30 150"""
import os, sys, json, statistics as S
SIM = sys.argv[1]; ZADEN = int(sys.argv[2]); UREN = float(sys.argv[3])
src = open(os.path.join(SIM, "sim.py")).read()
OUD_GAT = 'gat = (5, 7) if begin_i == 1 else (18, 22) if begin_i == 2 else (35, 45)\n            else:\n                gat = (40, 60)'
OUD_VOLGENDE = 'volgende = t + (rng.uniform(8, 20) if lied_extra > 0 else rng.uniform(*gat) * (1.0 if stap else eff["gat"]))'
OUD_GOUD = 'erbij = ((6 if SPEL_ECONOMIE else'
for x in (OUD_GAT, OUD_VOLGENDE, OUD_GOUD, "PLAT_S = 60"):
    assert x in src, x
def maak(nieuw, bonus):
    s = src
    if nieuw:
        s = s.replace(OUD_GAT, 'gat = (5, 7) if begin_i == 1 else (18, 22) if begin_i == 2 else (28, 38)\n            else:\n                gat = (28, 38)')
        s = s.replace(OUD_VOLGENDE, 'volgende = t + (rng.uniform(8, 20) if lied_extra > 0 else (rng.uniform(6, 10) if (not stap and rng.random() < 0.15) else rng.uniform(*gat) * (1.0 if stap else eff["gat"])))')
        s = s.replace("PLAT_S = 60", "PLAT_S = 30")
    if bonus:
        s = s.replace(OUD_GOUD, 'erbij = ((6 + min(3, max(0, gangen - 6) // 8) if SPEL_ECONOMIE else')
    ns = {"__file__": os.path.join(SIM, "sim.py"), "__name__": "simv3"}
    sys.path.insert(0, SIM); exec(s, ns)
    return ns
spec = json.load(open(os.path.join(SIM, "voortgang-v3-eind-bram.json")))
spec["uren"] = UREN
print("%d zaden, %g open uur, mediaan open uur tot hol-niveau (alleen als meer dan de helft het haalt)" % (ZADEN, UREN))
import copy
def rek(spec, f):
    # alle drempels x f, behalve hol-niveau 2 tot 12 (de demo, drempels van Olaf); prijzen blijven gelijk
    s = copy.deepcopy(spec)
    for sp in s["sporen"]:
        for nv in sp["niveaus"]:
            if not (sp["naam"] == "hol-niveau" and nv["niveau"] <= 12):
                nv["drempel"] = round(nv["drempel"] * f)
    return s
for naam, nieuw, bonus, f in (("oud ritme, vast 6", False, False, 1), ("nieuw ritme, vast 6", True, False, 1), ("nieuw ritme, graafbonus", True, True, 1),
                              ("nieuw, graafbonus, drempels x1,7", True, True, 1.7)):
    ns = maak(nieuw, bonus)
    alle = ns["lagen_run"](rek(spec, f), ZADEN, UREN)
    nt = ns["niveau_tijden"](alle, "hol-niveau")
    h = lambda n: ("%.1f" % (nt[n] / 3600)) if nt.get(n) else "-"
    print("%-26s | hol 12 %s u | 20 %s | 30 %s | 40 %s | 50 %s | helden per open uur %.0f" % (naam, h(12), h(20), h(30), h(40), h(50),
          S.median([st.get("helden", 0) for st in alle]) / UREN if "helden" in alle[0] else -1), flush=True)
