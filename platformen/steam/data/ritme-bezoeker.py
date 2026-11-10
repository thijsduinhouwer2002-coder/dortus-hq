"""Sanne 10 nov: de speler als bezoeker. Brams sim koopt na elke held meteen het goedkoopste; een echte speler
kijkt eens per zoveel minuten (T1: tussendoor), en ziet dan het muntje boven Gloop als een upgrade kan.
Leest producten/steam-hol/sim/sim.py en verandert alleen het kopen:
- kopen alleen bij een bezoek (elke BEZOEK minuten, eerste 10 minuten elke minuut want dan kijk je);
  een bezoek valt bij de eerste held na dat moment (helden komen elke 25 tot 75 s), dus het schuift tot ±75 s op,
- "muntje eerst": kan een upgrade, dan koopt hij die eerst (het muntje valt op), daarna het goedkoopste.
Draaien: python3 platformen/steam/data/ritme-bezoeker.py
"""
import os, statistics
BRON = os.path.join(os.path.dirname(__file__), "../../../producten/steam-hol/sim/sim.py")
src = open(BRON).read().split('if __name__ == "__main__"')[0]
OUD = "            wat, prijs = min(k, key=lambda x: x[1])\n"
assert OUD in src and "        while True:\n            k = koop_lijst()" in src
NIEUW = ("            upgs = [x for x in k if x[0].startswith('upg_') and x[1] <= goud] if MUNTJE_EERST else []\n"
         "            wat, prijs = min(upgs or k, key=lambda x: x[1])\n")
src = src.replace(OUD, NIEUW, 1)
src = src.replace("        while True:\n            k = koop_lijst()",
                  "        if t >= st.setdefault('bezoek', 0):\n            st['bezoek'] = t + (60 if t < 600 else BEZOEK * 60)\n        else:\n            continue\n        while True:\n            k = koop_lijst()", 1)
# 'continue' slaat alleen het kopen over: het kopen is het laatste deel van de lus (gecontroleerd hieronder)
assert src.index("st['bezoek'] = t") > src.index("goud += 6")
_lus = src[src.index("st['bezoek'] = t"):src.index('    st["helden"] = helden')]
assert "helden += 1" not in _lus and "goud +=" not in _lus   # na het kopen komt niets meer in de lus

def meet(bezoek, muntje, graaf="5 + 1.2 * gangen", upg="60 * 2.8 ** upg[s]", Z=20):
    ns = {"BEZOEK": bezoek, "MUNTJE_EERST": muntje}
    exec(src.replace("5 + 1.2 * gangen", graaf, 1).replace("60 * 2.8 ** upg[s]", upg, 1), ns)
    e, n1, alles, g1 = [], [], [], []
    for z in range(1, Z + 1):
        s = ns["speel"](10, z)
        e.append(s.get("eerste_upg", 36000) / 60)
        n1.append(sum(1 for a in s["aankopen"] if a[0] <= 3600))
        g1.append(6 + sum(1 for a in s["aankopen"] if a[0] <= 3600 and a[1] == "graaf"))
        alles.append(s["klaar_alles"] / 3600 if s["klaar_alles"] else 99)
    e.sort()
    return "eerste upg %5.1f/%5.1f/%5.1f min | aankopen uur1 %2d-%2d | gangen na 1u %2d-%2d | alles na %.1f-%.1f u" % (
        e[0], statistics.median(e), e[-1], min(n1), max(n1), min(g1), max(g1), min(alles), max(alles))

for bezoek in (5, 15, 30):
    for muntje in (False, True):
        print("bezoek elke %2d min, muntje eerst %-5s | %s" % (bezoek, muntje, meet(bezoek, muntje)))
print("-- met upgrade 1 op 45 --")
for bezoek in (5, 15, 30):
    print("bezoek elke %2d min, muntje eerst True  | %s" % (bezoek, meet(bezoek, True, upg="45 * 2.8 ** upg[s]")))
print("-- met upgrade 1 op 45 en graven +3 per gang boven 12 --")
for bezoek in (5, 15, 30):
    print("bezoek elke %2d min, muntje eerst True  | %s" % (bezoek, meet(bezoek, True, graaf="5 + 1.2 * gangen + 3 * max(0, gangen - 12)", upg="45 * 2.8 ** upg[s]")))
