#!/usr/bin/env python3
"""Vergelijk testbeelden pixel voor pixel (REGELS.md punt 6: opruimen verandert niets aan wat de app doet).

Gebruik: python3 vergelijk_plaatjes.py <map vóór> <map na> [--negeer y0-y1 ...]
--negeer: rijen die niet meetellen, zoals de statusbalk van de simulator onder het horloge (die toont het
geheugen, en dat verandert bij opruimen wel). Op fr255 is dat y 598-620, op fenix847mm zie de uitvoer.
Per beeld met dezelfde naam: aantal pixels dat verschilt. Exit 1 als er een verschil of een ontbrekend beeld is.
"""
import sys, os
from PIL import Image, ImageChops

voor, na = sys.argv[1], sys.argv[2]
negeer = []
for i, a in enumerate(sys.argv):
    if a == '--negeer':
        y0, y1 = sys.argv[i + 1].split('-'); negeer.append((int(y0), int(y1)))
namen = sorted(set(f for f in os.listdir(voor) if f.endswith('.png')) | set(f for f in os.listdir(na) if f.endswith('.png')))
fout = 0
for n in namen:
    a, b = os.path.join(voor, n), os.path.join(na, n)
    if not (os.path.exists(a) and os.path.exists(b)):
        print(f"ONTBREEKT {n} (voor: {os.path.exists(a)}, na: {os.path.exists(b)})"); fout += 1; continue
    ia, ib = Image.open(a).convert('RGB'), Image.open(b).convert('RGB')
    if ia.size != ib.size:
        print(f"MAAT {n} {ia.size} {ib.size}"); fout += 1; continue
    diff = ImageChops.difference(ia, ib)
    for y0, y1 in negeer:
        diff.paste((0, 0, 0), (0, y0, diff.size[0], y1 + 1))
    box = diff.getbbox()
    if box is None:
        print(f"GELIJK {n}")
    else:
        aantal = diff.convert('L').point(lambda p: 255 if p else 0).histogram()[255]
        print(f"VERSCHIL {n} {aantal} pixels in {box}"); fout += 1
print(f"{len(namen)} beelden, {fout} met verschil of ontbrekend")
sys.exit(1 if fout else 0)
