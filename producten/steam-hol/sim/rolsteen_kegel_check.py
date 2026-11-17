"""Nakijken van Sannes kegel.py (17 nov 2026, Bram).
(1) Is de volger van een paar echt nog in de gang? Meet het gat in seconden tussen voorloper en volger
    (6 cellen = 9,6 s). (2) Hoeveel van de 100 zaden zien Two for one binnen 60 min na de koop, gemeten in
    één run van 3 uur (tijdstip van elke Two for one), niet met een kortere run.
Draai: python3 -I producten/steam-hol/sim/rolsteen_kegel_check.py
"""
import os, sys, statistics as S
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "..", "platformen", "steam", "data", "sim-rolsteen-kegel"))
import kegel as K, rolsteen as R
K.KEGEL["aan"] = True
_v = R.vervang

def v2(s, o, n):
    s = _v(s, o, n)
    if "not leider and" in s and "_tt" not in s:
        s = s.replace("            leider = steen_klaar\n",
                      "            leider = steen_klaar\n"
                      "            if leider: st['steen']['_lt'] = t\n"
                      "            else: st['steen'].setdefault('_gat', []).append((t - st['steen']['_lt'], st['steen']['_raak'], hs_))\n")
        s = s.replace("                    st['steen']['twee'] += 1\n",
                      "                    st['steen']['twee'] += 1; st['steen'].setdefault('_tt', []).append(t)\n")
    return s
R.vervang = v2
ns = R.bron(steen_basis=0.50, edel_goud=2, mis_klap="ridder")
gat, hit, n, eerste = [], 0, 0, []
for z in range(1, 101):
    st = ns["speel"](3.0, z, R.spec(True))
    gat += st["steen"].get("_gat", [])
    ks = [x[0] for x in st["aankopen"] if x[1] == "tegen_rolsteen"]
    if not ks:
        continue
    n += 1
    tt = [x for x in st["steen"].get("_tt", []) if x >= ks[0]]
    hit += bool(tt and tt[0] - ks[0] <= 3600)
    eerste.append((tt[0] - ks[0]) / 60 if tt else 999)
na = [g for g in gat if g[1] >= 1]
print("volgerbeurten %d, gat boven 9,6 s: %d (langste %.1f s), na raak voorloper %d waarvan ridder %d"
      % (len(gat), sum(g[0] > 9.6 for g in gat), max(g[0] for g in gat), len(na), sum(g[2] == "ridder" for g in na)))
print("%d zaden met steen, Two for one binnen 60 min na koop: %d | eerste na koop mediaan %.1f min, langste %.1f min"
      % (n, hit, S.median(eerste), max(eerste)))
