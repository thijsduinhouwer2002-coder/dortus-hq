#!/usr/bin/env python3
"""Contrast van elke tekstregel op de echte beelden van de krabproef (bericht hoofdchat 12 nov 02:30 NL punt 4).

Gebruik: python3 contrast_tekst.py <map met <horloge>-scene<k>.png> <horloge> <schermmaat in px> [eerste scène, standaard 51]

Per regel een band rond de tekst (maten in 1/260 van het scherm). De tekst is de lichtste kleur die minstens
2 procent van de band vult; de achtergrond is elke donkere kleur (helderheid onder 0,3) bij de vijf meest
voorkomende die minstens 8 procent vult. De laagste verhouding telt. Kleuren worden afgerond op stappen van 32,
zodat de randen van letters en de ruis van AMOLED niet als aparte kleur tellen. Norm: 4,5 op 1.
Het scherm wordt gezocht als het vlak met kleur in de foto van de simulator.
Eerlijk: de banden staan vast; schuift een regel, pas dan BANDEN aan. De onderregel van de ademschermen meet dit
script niet (de band viel in run 52 op een golfrand).
"""
import sys
from collections import Counter
from PIL import Image

# (scherm 0 tot 5, naam, y0, y1, x0, x1) in 1/260
BANDEN = [(0, 'woord', 8, 34, 80, 180),
          (3, 'hold', 12, 36, 105, 155), (3, 'press START', 38, 56, 60, 200), (3, 'tijd', 60, 118, 70, 190),
          (3, 'bpm', 122, 142, 70, 190), (4, 'Ebb', 14, 40, 105, 155), (4, 'menuregel', 118, 136, 50, 210),
          (5, 'kop', 26, 48, 50, 210), (5, 'tijden', 50, 70, 60, 200), (5, 'new friend', 160, 174, 95, 165),
          (5, 'naam', 174, 200, 95, 165)]


def helderheid(c):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def verhouding(a, b):
    la, lb = sorted((helderheid(a), helderheid(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def scherm(im, maat):
    """Vierkant van maat x maat rond het midden van het gekleurde vlak (het scherm in de simulatorfoto)."""
    xs, ys = [], []
    px = im.load()
    for y in range(0, im.size[1], 2):
        for x in range(0, im.size[0], 2):
            r, g, b = px[x, y]
            if abs(r - b) > 40 or abs(g - b) > 40:
                xs.append(x); ys.append(y)
    xs.sort(); ys.sort()
    n = len(xs)
    cx = (xs[n // 100] + xs[n - 1 - n // 100]) // 2
    cy = (ys[n // 100] + ys[n - 1 - n // 100]) // 2
    return (cx - maat // 2, cy - maat // 2, cx + maat // 2, cy + maat // 2)


def main():
    map_, horloge, maat = sys.argv[1], sys.argv[2], int(sys.argv[3])
    eerste = int(sys.argv[4]) if len(sys.argv) > 4 else 51
    laagste = None
    for nacht in (0, 1):
        for s, naam, y0, y1, x0, x1 in BANDEN:
            im = Image.open(f'{map_}/{horloge}-scene{eerste + s + 6 * nacht}.png').convert('RGB')
            im = im.crop(scherm(im, maat))
            q = lambda v: v * maat // 260
            band = im.crop((q(x0), q(y0), q(x1), q(y1)))
            pix = [band.getpixel((x, y)) for y in range(band.size[1]) for x in range(band.size[0])]
            tel = Counter(tuple(min(255, (v + 16) // 32 * 32) for v in p) for p in pix)
            n = sum(tel.values())
            tekst = max((k for k, v in tel.items() if v >= n * 0.02), key=helderheid)
            achter = [k for k, v in tel.most_common(5) if v >= n * 0.08 and helderheid(k) < 0.3]
            deel = 'nacht' if nacht else 'dag'
            if not achter:
                print(f'CONTRAST {horloge} {deel} scherm {s} {naam}: geen achtergrond gevonden')
                continue
            a = min(achter, key=lambda k: verhouding(k, tekst))
            v = verhouding(tekst, a)
            laagste = v if laagste is None or v < laagste else laagste
            print(f"CONTRAST {horloge} {deel} scherm {s} {naam}: tekst {'%02X%02X%02X' % tekst} op {'%02X%02X%02X' % a} = {v:.1f}{' TE LAAG' if v < 4.5 else ''}")
    print(f'CONTRAST {horloge} laagste {laagste:.1f}' if laagste else f'CONTRAST {horloge} niets gemeten')


if __name__ == '__main__':
    main()
