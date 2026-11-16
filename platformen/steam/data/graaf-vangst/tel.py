# Telt de DIAG-uitvoer van de headless runs (zie LEESMIJ.md). Gebruik: python3 tel.py <map> gewoon koop graaf beide
import re, glob, sys
map_ = sys.argv[1]
for m in sys.argv[2:]:
    R = []
    for f in glob.glob(f"{map_}/{m}-*.out"):
        t = open(f).read()
        g = t.count("DIAG uit "); v = len(re.findall(r"DIAG uit .* gevallen", t))
        R.append((g, v, g - v, t.count("DIAG aangekomen"),
                  len(re.findall(r"kol=24 .*valt=true", t)), len(re.findall(r"kol=24 .*valt=", t)),
                  len(re.findall(r"kol=27 .*valt=true", t)), len(re.findall(r"kol=27 .*valt=", t))))
    n = len(R); S = lambda i: sum(r[i] for r in R) / n
    print(f"{m}: n={n} helden {S(0):.1f} gevangen {S(1):.1f} weg {S(2):.1f} schat {S(3):.1f} put {S(4):.1f}/{S(5):.1f} Gloop {S(6):.1f}/{S(7):.1f}")
