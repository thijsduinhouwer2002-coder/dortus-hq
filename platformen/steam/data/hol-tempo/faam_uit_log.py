"""Sanne 17 nov ±09:10 UTC (Iris keuring 20 punt 3): wanneer hol 10 tot 12 komen met de oude en de nieuwe drempels,
gemeten in plaats van gemodelleerd. Faam = gevangen helden (kern/afloop.gd: +1 per val); elke vangst geeft een
kroniekregel die eindigt op " +<goud>", dus tijd van vangst k = tijd van die regel min zijn wachttijd.
Nagerekend: telling klopt precies met alle "HOL hol-niveau ... (faam n, t ...)"-regels in beide logs.
Draai: python3 -I faam_uit_log.py <hol.log> [<hol.log> ...]"""
import re, sys
OUD = [3, 5, 7, 12, 17, 25, 31, 39, 53, 69, 88]
NIEUW = [3, 5, 7, 12, 17, 25, 31, 39, 49, 60, 72]
for pad in sys.argv[1:]:
    vang = sorted(float(m.group(1)) - float(m.group(2)) for l in open(pad).read().splitlines()
                  for m in [re.match(r"HOL kroniek ([\d.]+) \(wacht ([\d.]+)\): .* \+\d+$", l)] if m)
    print("%s: %d vangsten" % (pad, len(vang)))
    for naam, dr in (("oud", OUD), ("nieuw", NIEUW)):
        t = [0.0] + [vang[d - 1] / 60 if d <= len(vang) else None for d in dr]
        rij = " ".join("h%d %s" % (i + 2, "%.1f" % x if x is not None else "-") for i, x in enumerate(t[1:]))
        gaten = [(t[i + 1] - t[i], i + 2) for i in range(len(t) - 1) if t[i + 1] is not None]
        g = max(gaten)
        print("  %-5s %s | grootste gat %.1f min (naar hol %d)" % (naam, rij, g[0], g[1]))
    print("  vangsten per 10 min:", [sum(1 for v in vang if a * 600 <= v < (a + 1) * 600) for a in range(int(vang[-1] // 600) + 1)])
