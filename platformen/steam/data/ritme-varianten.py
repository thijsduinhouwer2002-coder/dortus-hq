"""Sanne 10 nov: varianten op graafkosten en eerste upgrade, gerekend met Brams sim (producten/steam-hol/sim/sim.py).
Leest sim.py, vervangt alleen de twee prijsformules, en meet voor de speler die steeds het goedkoopste koopt.
Draaien: python3 platformen/steam/data/ritme-varianten.py
"""
import os, statistics
BRON = os.path.join(os.path.dirname(__file__), "../../../producten/steam-hol/sim/sim.py")
src = open(BRON).read().split('if __name__ == "__main__"')[0]
assert '("graaf", 5 + 1.2 * gangen)' in src and '60 * 2.8 ** upg[s]' in src

VARIANTEN = {
    "nu (5+1,2g, upg 60)":            ("5 + 1.2 * gangen", "60 * 2.8 ** upg[s]"),
    "upg 40":                          ("5 + 1.2 * gangen", "40 * 2.8 ** upg[s]"),
    "graaf +4 per gang boven 12":      ("5 + 1.2 * gangen + 4 * max(0, gangen - 12)", "60 * 2.8 ** upg[s]"),
    "graaf +3 boven 12, upg 45":       ("5 + 1.2 * gangen + 3 * max(0, gangen - 12)", "45 * 2.8 ** upg[s]"),
    "graaf +4 boven 12, upg 45":       ("5 + 1.2 * gangen + 4 * max(0, gangen - 12)", "45 * 2.8 ** upg[s]"),
    "graaf +4 boven 10, upg 45":       ("5 + 1.2 * gangen + 4 * max(0, gangen - 10)", "45 * 2.8 ** upg[s]"),
}
Z = 20
for naam, (g, u) in VARIANTEN.items():
    ns = {}
    exec(src.replace("5 + 1.2 * gangen", g, 1).replace("60 * 2.8 ** upg[s]", u, 1), ns)
    eerste, gat1, n1, alles, gang60, vlucht = [], [], [], [], [], []
    for z in range(1, Z + 1):
        s = ns["speel"](10, z)
        eerste.append(s.get("eerste_upg", 36000) / 60)
        gat1.append(ns["wachttijden"](s["aankopen"], 3600) / 60)
        n1.append(sum(1 for a in s["aankopen"] if a[0] <= 3600))
        alles.append(s["klaar_alles"] / 3600 if s["klaar_alles"] else 99)
        gang60.append(6 + sum(1 for a in s["aankopen"] if a[0] <= 3600 and a[1] == "graaf"))
        vlucht.append(s["gevlucht"] / s["helden"])
    e = sorted(eerste)
    print("%-28s eerste upg %4.1f/%4.1f/%4.1f min | aankopen uur1 %2d-%2d | langste gat uur1 %4.1f-%4.1f min | gangen na 1u %2d-%2d | alles na %.1f-%.1f u | vlucht %2.0f-%2.0f%%" % (
        naam, e[0], statistics.median(e), e[-1], min(n1), max(n1), min(gat1), max(gat1), min(gang60), max(gang60), min(alles), max(alles), 100*min(vlucht), 100*max(vlucht)))
