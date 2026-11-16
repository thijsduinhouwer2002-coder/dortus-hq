"""Ritme van het gewone spel uit een spel-log (Olaf 16 nov 2026, vraag Iris keuring 6).

Leest de regels 'HOL zicht <t> <helden>' (strook.gd: als de eerste held in beeld komt of de laatste weg is)
en 'HOL kroniek <t> (wacht ...)' en geeft:
  - deel van de tijd met minstens een held in beeld
  - langste stuk zonder held in beeld
  - langste stuk zonder kroniekregel
  - langste stuk zonder held EN zonder nieuwe kroniekregel
Gebruik: python3 ritme_meting.py <log> [eind_s]   (eind_s: standaard de 'HOL einde na N s' uit de log)
"""
import re
import sys


def meet(pad, eind=None):
    zicht, kroniek = [], []
    for r in open(pad, encoding="utf-8", errors="replace"):
        m = re.match(r"HOL zicht ([0-9.]+) (\d+)", r)
        if m:
            zicht.append((float(m.group(1)), int(m.group(2)) > 0))
        m = re.match(r"HOL kroniek ([0-9.]+) \(wacht", r)
        if m:
            kroniek.append(float(m.group(1)))
        m = re.match(r"HOL einde na (\d+) s", r)
        if m and eind is None:
            eind = float(m.group(1))
    if eind is None:
        eind = max([t for t, _ in zicht] + kroniek + [0.0])
    # stukken met een held in beeld
    aan, stukken, start = False, [], None
    for t, z in zicht:
        if z and not aan:
            aan, start = True, t
        elif not z and aan:
            aan = False
            stukken.append((start, t))
    if aan:
        stukken.append((start, eind))
    in_beeld = sum(b - a for a, b in stukken)
    # gaten zonder held
    leeg, vorige = [], 0.0
    for a, b in stukken:
        leeg.append((vorige, a))
        vorige = b
    leeg.append((vorige, eind))
    langst_leeg = max(leeg, key=lambda x: x[1] - x[0])
    # gaten zonder kroniekregel
    kt = [0.0] + sorted(k for k in kroniek if k <= eind) + [eind]
    stil = max(zip(kt, kt[1:]), key=lambda x: x[1] - x[0])
    # zonder held en zonder regel: een leeg stuk opgeknipt door kroniekregels
    beide = (0.0, 0.0)
    for a, b in leeg:
        pts = [a] + [k for k in kroniek if a < k < b] + [b]
        for x, y in zip(pts, pts[1:]):
            if y - x > beide[1] - beide[0]:
                beide = (x, y)
    return {
        "eind": eind,
        "deel_held": in_beeld / eind if eind else 0.0,
        "langst_zonder_held": langst_leeg,
        "langst_zonder_regel": stil,
        "langst_zonder_beide": beide,
        "regels": len([k for k in kroniek if k <= eind]),
        "keer_held": len(stukken),
    }


if __name__ == "__main__":
    u = meet(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else None)
    f = lambda p: "%.0f s (van %.0f tot %.0f)" % (p[1] - p[0], p[0], p[1])
    print("gemeten %.0f s, %d kroniekregels, %d keer een held in beeld" % (u["eind"], u["regels"], u["keer_held"]))
    print("deel van de tijd met minstens een held in beeld: %.0f%%" % (100 * u["deel_held"]))
    print("langste stuk zonder held: " + f(u["langst_zonder_held"]))
    print("langste stuk zonder kroniekregel: " + f(u["langst_zonder_regel"]))
    print("langste stuk zonder held en zonder regel: " + f(u["langst_zonder_beide"]))
