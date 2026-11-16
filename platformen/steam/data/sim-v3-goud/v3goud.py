"""Bram 16 nov ±21:12 UTC, vraag Sanne 21:00: welke goudregel per val gold in de v3-runs, en wat doet elke vorm met versie 3?
Antwoord uit de code: sim.py lagen_run zet SPEL_ECONOMIE aan, dus vast 6 (+3 per bezoek, +1 vanaf Edelman op hol 10).
Dit script draait voortgang-v3-eind-bram.json (graven kost goud, 4 lagen) met drie vormen van het goud per val.
graafbonus: per laag geteld (een nieuwe laag begint met 6 gangen), +1 per 8 zelf gegraven gangen, hooguit +3;
"over alle lagen": wie laag 2 opent heeft de +3 al (34 cellen in laag 1), dus vanaf laag 2 vast +3.
Draai: python3 -I platformen/steam/data/sim-v3-goud/v3goud.py producten/steam-hol/sim 30 100"""
import os, sys, json, time, statistics as S
SIM = sys.argv[1]; ZADEN = int(sys.argv[2]); UREN = float(sys.argv[3])
src = open(os.path.join(SIM, "sim.py")).read()
OUD = 'erbij = ((6 if SPEL_ECONOMIE else'
assert OUD in src
VORM = {"vast 6": "6", "6 + graafbonus (1/8, max 3)": "6 + min(3, max(0, gangen - 6) // 8)", "6 + graafbonus over alle lagen": "6 + (3 if len(laag_info) > 1 else min(3, max(0, gangen - 6) // 8))", "6 x (1 + gangen/40)": "6 * (1 + gangen / 40)"}
spec = json.load(open(os.path.join(SIM, "voortgang-v3-eind-bram.json")))
for naam, f in VORM.items():
    ns = {"__file__": os.path.join(SIM, "sim.py"), "__name__": "simv3"}; sys.path.insert(0, SIM)
    exec(src.replace(OUD, 'erbij = ((%s if SPEL_ECONOMIE else' % f), ns)
    t0 = time.time()
    alle = ns["lagen_run"](spec, ZADEN, UREN)
    lo = []
    for i in range(1, 4):
        r = [st["lagen"][i]["open"] / 3600 for st in alle if len(st["lagen"]) > i and st["lagen"][i].get("open")]
        lo.append("laag %d open %s" % (i + 1, ("%.1f u (%d/%d)" % (S.median(r), len(r), len(alle))) if r else "-"))
    nt = ns["niveau_tijden"](alle, "hol-niveau")
    h = lambda n: ("%.1f u" % (nt[n] / 3600)) if nt.get(n) else "-"
    g = S.median([st.get("goud_totaal", 0) for st in alle])
    print("%-30s | %s | hol 12 %s, 20 %s, 30 %s, 40 %s | goud totaal %.0f | %.0f s" % (naam, " | ".join(lo), h(12), h(20), h(30), h(40), g, time.time() - t0), flush=True)
