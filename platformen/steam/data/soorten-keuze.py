"""Sanne 10 nov: maken de heldensoorten de keuze tussen Gloop en de put zinvol?
Telt per soort wie hem vangt (slijm, put) en hoeveel vluchten, met Brams getallen en met mijn voorstel.
Leest producten/steam-hol/sim/sim.py en voegt alleen een teller toe; de regels blijven gelijk.
Draaien: python3 platformen/steam/data/soorten-keuze.py
"""
import os
BRON = os.path.join(os.path.dirname(__file__), "../../../producten/steam-hol/sim/sim.py")
src = open(BRON).read().split('if __name__ == "__main__"')[0]
OUD = '                uit = "gevallen"\n'
assert src.count(OUD) == 1
src = src.replace(OUD, OUD + '                VANG.setdefault(h.get("soort", ""), {}).setdefault(v["soort"], 0); VANG[h.get("soort", "")][v["soort"]] += 1\n')
OUD2 = '            st["gevlucht"] += 1\n'
assert src.count(OUD2) == 1
src = src.replace(OUD2, OUD2 + '            VANG.setdefault(h.get("soort", ""), {}).setdefault("vlucht", 0); VANG[h.get("soort", "")]["vlucht"] += 1\n')

BRAM = {"ridder": ({"slijm": 0.85, "put": 1.0}, True), "dief": ({"slijm": 1.15, "put": 0.5}, False),
        "magier": ({"slijm": 1.25, "put": 0.3}, False), "bard": ({"slijm": 1.15, "put": 1.15}, False)}
SANNE = {"ridder": ({"slijm": 0.7, "put": 1.4}, True), "dief": ({"slijm": 1.15, "put": 0.5}, False),
         "magier": ({"slijm": 1.25, "put": 0.3}, False), "bard": ({"slijm": 1.1, "put": 1.1}, False)}

def meet(data, Z=8):
    ns = {"VANG": {}}
    exec(src, ns)
    ns["SOORTEN"], ns["SOORT_DATA"] = True, data
    vl, h = 0, 0
    for z in range(1, Z + 1):
        s = ns["speel"](10, z)
        vl += s["gevlucht"]; h += s["helden"]
    print("  vluchten totaal %.1f%%" % (100 * vl / h))
    for soort in ["", "ridder", "dief", "magier", "bard"]:
        d = ns["VANG"].get(soort, {})
        n = sum(d.values()) or 1
        print("  %-7s n=%5d | slijm %4.1f%% | put %4.1f%% | vlucht %4.1f%%" % (soort or "gewoon", n,
              100 * d.get("slijm", 0) / n, 100 * d.get("put", 0) / n, 100 * d.get("vlucht", 0) / n))

print("Bram (nu in heldensoort.gd):"); meet(BRAM)
print("Sanne (voorstel):"); meet(SANNE)
