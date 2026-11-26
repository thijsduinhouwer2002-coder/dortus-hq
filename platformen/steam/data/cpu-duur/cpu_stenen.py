"""CPU binnen één run: gouden stenen (#162) aan tegen uit. Olaf 26 nov 2026.
Ook voor worm en mot (#190): wissel=leven of wissel=nep geeft "HOL wissel leven aan|uit ..." met dezelfde blokken.

Gebruik: python3 cpu_stenen.py <map> [...]
De map heeft cpu.txt (per seconde "<unix-tijd> <utime+stime in ticks>" van het Godot-proces), uit.txt (uitvoer van
het spel) en hol.log. Startargument wissel=stenen zet de stenen aan in even blokken van 20 s (int(unix/20) even) en uit
in oneven; wissel=nep schrijft dezelfde regels maar laat ze aan (placebo: dat verschil is de ruis).
Een held die loopt kost veel meer dan de stenen, dus alleen seconden zonder held in beeld tellen (HOL zicht in hol.log,
speltijd omgezet naar unix-tijd met de wisselregels), en niet de 3 s rond een held die komt of gaat.
Per blok tellen seconde 3 tot 18. Uitkomst in CPU-s per 10 s, en per buurpaar (elk uit-blok tegen het gemiddelde van
de aan-blokken ervoor en erna), zodat langzame drift wegvalt.
"""
import os, re, sys, statistics as S

ALLES = os.environ.get('ALLES') == '1'   # ALLES=1: ook seconden met een held (ter vergelijking, veel ruis)

TCK = 100.0
BLOK = 20
for d in sys.argv[1:]:
    uit = open(d + '/uit.txt').read()
    paren_tu = [(float(u), float(t)) for u, t in re.findall(r'HOL wissel (?:stenen|leven) \w+ unix=([\d.]+) t=([\d.]+) pad=Hol', uit)]
    paren_tu = [p for p in paren_tu if p[1] > 1.0]
    off = S.median(u - t for u, t in paren_tu)
    zicht = [(float(t) + off, int(n)) for t, n in re.findall(r'HOL zicht ([\d.]+) (\d+)', open(d + '/hol.log').read())]

    def stil(m):
        held = 0
        for u, n in zicht:
            if abs(u - m) < 3:
                return False
            if u <= m:
                held = n
        return held == 0

    rijen = [tuple(map(float, r.split())) for r in open(d + '/cpu.txt') if len(r.split()) == 2]
    blok = {}
    for (t0, c0), (t1, c1) in zip(rijen, rijen[1:]):
        m = (t0 + t1) / 2
        if m - rijen[0][0] < 30 or t1 <= t0:   # eerste halve minuut: laden
            continue
        b = int(m // BLOK)
        if 3 <= m - b * BLOK <= BLOK - 2 and (ALLES or stil(m)):
            blok.setdefault(b, []).append((c1 - c0) / TCK / (t1 - t0) * 10)
    gem = {b: S.mean(v) for b, v in blok.items() if len(v) >= 6}
    aan = [v for b, v in gem.items() if b % 2 == 0]
    weg = [v for b, v in gem.items() if b % 2 == 1]
    rel = [((gem[b - 1] + gem[b + 1]) / 2 / gem[b] - 1) * 100 for b in gem if b % 2 == 1 and b - 1 in gem and b + 1 in gem]
    print(f"{d.rstrip('/').split('/')[-1]}: {len(aan)} blokken aan, {len(weg)} uit (" + ("alle seconden" if ALLES else "alleen stille seconden") + ")")
    print(f"  aan {S.mean(aan):.3f}  uit {S.mean(weg):.3f} CPU-s per 10 s, verschil {(S.mean(aan) / S.mean(weg) - 1) * 100:+.2f} procent")
    if len(rel) > 1:
        print(f"  buurparen ({len(rel)}): gemiddeld {S.mean(rel):+.2f} procent, spreiding {S.stdev(rel):.2f}, "
              f"fout van het gemiddelde {S.stdev(rel) / len(rel) ** 0.5:.2f}")
