"""Rolsteen als kegelbaan (Sanne 17 nov 2026, na keuring 12 van Iris punt 2).

Brams rolsteen.py blijft zoals hij is; dit script leent zijn bron() en voegt in het geheugen een regel toe:
- KEGEL: wordt de voorloper geraakt, dan is de held achter hem in de gang ook raak (de steen neemt hem mee),
  behalve een ridder: die krijgt zijn eigen kans (x 0,6, "Clang.").
Brams model telt de volgende held al als "in de gang" als zijn gat korter is dan 6 cellen lopen. In het echte spel
klopt dat alleen als de steen pas rolt als de voorloper aan het eind van de gang is (mijn regel "de steen kraakt").
Draai: python3 -I platformen/steam/data/sim-rolsteen-kegel/kegel.py   (ZADEN=100 standaard)
"""
import os, sys, statistics as S
HIER = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.join(HIER, "..", "..", "..", "..", "producten", "steam-hol", "sim")
sys.path.insert(0, os.path.abspath(SIM))
import rolsteen as R

KEGEL = {"aan": False}
_oud = R.vervang

def vervang(s, oud, nieuw):
    s = _oud(s, oud, nieuw)
    if KEGEL["aan"] and "            if rng.random() < kans_s:\n" in s:
        s = s.replace("            if steen_klaar:\n                steen_klaar = False\n",
                      "            leider = steen_klaar\n            if steen_klaar:\n                steen_klaar = False\n")
        s = s.replace("            if rng.random() < kans_s:\n",
                      "            if rng.random() < kans_s or (not leider and st['steen']['_raak'] >= 1 and hs_ != 'ridder'):\n")
    return s
R.vervang = vervang

def per20(r, uren=3.0):
    steentijd = sum(max(0.0, uren * 60 - t) for t in r["steen_t"] if t < 900)
    return 20.0 * r["paar_twee"] / max(1e-9, steentijd), 20.0 * r["worp"] / max(1e-9, steentijd)

if __name__ == "__main__":
    Z = int(os.environ.get("ZADEN", "100"))
    print("Rolsteen, %d zaden, 3 uur, mis = klap alleen voor de ridder" % Z)
    for basis in (0.40, 0.50):
        for kegel in (False, True):
            KEGEL["aan"] = kegel
            r = R.meet(R.bron(steen_basis=basis, edel_goud=2, mis_klap="ridder"), True, Z)
            p20, w20 = per20(r)
            print("%s  | Two for one per 20 min steentijd %.2f, worpen per 20 min %.2f" % (
                R.regel("steen %.2f%s" % (basis, ", kegel" if kegel else ""), r), p20, w20))
    KEGEL["aan"] = False
    r = R.meet(R.bron(steen_basis=0.35, edel_goud=2, edel_aan=True), False, Z)
    print(R.regel("zonder steen", r))
