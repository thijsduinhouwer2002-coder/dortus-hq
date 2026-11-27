#!/usr/bin/env python3
# Maakt godot/hol/kamerwand_masker.gd: per kamerstuk welke spelpixels kale buiswand zijn (Olaf 27 nov, #252).
# De korrel van hol/kamerwand.gd komt alleen op die pixels, dus nooit over stut, houweel, ton, fakkel of kistje die in
# het kamerstuk zelf zitten. Een pixel is wand als hij glad is (weinig verschil binnen zijn 4 x 4 bladpixels) en de
# zalmkleur van de buis heeft, en geen van zijn buren een ding is (dus altijd 1 spelpx afstand tot decor). Rij 4 (de
# zachte overgang van aarde naar buis) telt als rand als hij die overgang echt heeft en er wand onder zit. Draai opnieuw als Mila het hol-blad opnieuw rendert:
#   python3 pijplijn/kamerwand_masker.py
import json
import os
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
GODOT = os.path.join(HIER, "..", "godot")
STUKKEN = ["kamer_begin", "kamer_eind", "kamer_links", "kamer_rechts", "kamer_los",
           "kamer_midden_a", "kamer_midden_b", "kamer_midden_c"]
RIJ_BOVEN = 4      # bovenrand van de buis (rij in het stuk); 5 tot 11 wand, 12 rand van de vloer
RIJ_ONDER = 12
# per rij: (r/g van, tot, g/b van, tot, spreiding van, tot); gemeten in de kamerstukken van 27 nov
WAND = (1.72, 1.95, 1.28, 1.45, 0, 6)
RAND = (1.74, 1.84, 1.21, 1.30, 15, 60)
VLOER = (1.64, 1.76, 1.27, 1.34, 0, 12)


def main():
    info = json.load(open(os.path.join(GODOT, "kunst/3d/sprites.json")))["hol_proef"]
    im = Image.open(os.path.join(GODOT, info["blad"].replace("res://", ""))).convert("RGB")
    st = info["stukken"]

    def gelijk(naam, x, y):
        vx, vy = st[naam]["vak_px"][0], st[naam]["vak_px"][1]
        p = [im.getpixel((vx + x * 4 + i, vy + y * 4 + j)) for i in range(4) for j in range(4)]
        m = [sum(q[c] for q in p) / 16.0 for c in range(3)]
        sd = max((sum((q[c] - m[c]) ** 2 for q in p) / 16.0) ** 0.5 for c in range(3))
        regel = RAND if y == RIJ_BOVEN else (VLOER if y == RIJ_ONDER else WAND)
        rg, gb = m[0] / max(m[1], 1.0), m[1] / max(m[2], 1.0)
        return regel[0] <= rg <= regel[1] and regel[2] <= gb <= regel[3] and regel[4] <= sd <= regel[5]

    uit = {}
    for naam in STUKKEN:
        if naam not in st:
            continue
        g = [[gelijk(naam, x, y) for x in range(16)] for y in range(16)]
        rijen = []
        for y in range(16):
            r = ""
            for x in range(16):
                ok = RIJ_BOVEN <= y <= RIJ_ONDER and g[y][x]
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        yy, xx = y + dy, x + dx
                        if 0 <= xx < 16 and RIJ_BOVEN <= yy <= RIJ_ONDER and not g[yy][xx]:
                            ok = False
                if y == RIJ_BOVEN and not g[y + 1][x]:
                    ok = False
                r += "1" if ok else "."
            rijen.append(r)
        uit[naam] = rijen

    regels = ["extends RefCounted",
              "# Gemaakt door pijplijn/kamerwand_masker.py (niet met de hand wijzigen). 1 = kale buiswand of rand, . = niet.",
              "# Rij 4 is de bovenrand van de buis, 5 tot 11 de wand, 12 de rand van de vloer.",
              "const MASKER := {"]
    for naam, rijen in uit.items():
        regels.append('\t"%s": [' % naam)
        for r in rijen:
            regels.append('\t\t"%s",' % r)
        regels.append("\t],")
    regels.append("}")
    open(os.path.join(GODOT, "hol/kamerwand_masker.gd"), "w").write("\n".join(regels) + "\n")
    for naam, rijen in uit.items():
        print(naam, sum(r.count("1") for r in rijen))


if __name__ == "__main__":
    main()
