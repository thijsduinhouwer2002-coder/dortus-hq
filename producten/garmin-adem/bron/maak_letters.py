"""Barlow Condensed Medium (OFL) voor alle tekst in Ebb (keuring bouw 4 punt 4), als BMFont voor Connect IQ.

Drie letters per schermmaat: EbbXtiny, EbbSmall, EbbMedium, met dezelfde regelhoogte als de systeemletters
FONT_XTINY, FONT_SMALL en FONT_MEDIUM op dat horloge (gemeten in de plaatjesbouw, logboek run 32), zodat de
opmaak niet verschuift. De hoofdletters zijn 52 procent van de regelhoogte (Roboto op Garmin: ±46 procent);
Barlow Condensed is smaller, zodat een regel per saldo smaller wordt.
Gebruik: python3 -I maak_letters.py <map producten/garmin-adem>
Schrijft in elke resources*/fonts naast ebb_cijfers: ebb_xtiny, ebb_small, ebb_medium (.fnt en .png) en fonts.xml.
"""
import os
import re
import sys
from PIL import Image, ImageDraw, ImageFont

LETTER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "barlow-condensed-latin-500-normal.woff")
TEKENS = "".join(chr(c) for c in range(32, 127)) + "·"
# Schermmaat uit de hoogte van de cijferletter (±31,5 procent van D).
MAAT = {82: 260, 88: 280, 123: 390, 130: 416, 143: 454}
# Regelhoogte xtiny, small, medium per schermmaat (systeemletters, plaatjesrun c304861).
REGEL = {260: (19, 32, 37), 280: (19, 34, 40), 390: (31, 46, 53), 416: (32, 48, 56), 454: (36, 51, 60)}
NAMEN = ("ebb_xtiny", "ebb_small", "ebb_medium")
IDS = ("EbbXtiny", "EbbSmall", "EbbMedium")
CAP = 0.52


def lettergrootte(regel):
    doel = round(regel * CAP)
    g = regel
    for _ in range(30):
        f = ImageFont.truetype(LETTER, g)
        bb = f.getbbox("H", anchor="ls")
        h = bb[3] - bb[1]
        if h == doel:
            break
        g = max(6, round(g * doel / max(1, h)))
    return ImageFont.truetype(LETTER, g), g


def maak(regel, uitmap, naam, fid):
    f, g = lettergrootte(regel)
    cap = -f.getbbox("H", anchor="ls")[1]
    base = (regel + cap) // 2          # hoofdletters in het midden van de regel (VCENTER zoals de systeemletters)
    rand = 1
    breed_max = 512
    x, y, rij_h = rand, rand, 0
    plek = []
    for t in TEKENS:
        bb = f.getbbox(t, anchor="ls")
        w = max(0, bb[2] - bb[0])
        h = max(0, bb[3] - bb[1])
        if x + w + rand > breed_max:
            x, y, rij_h = rand, y + rij_h + 2 * rand, 0
        plek.append((t, x, y, bb, w, h))
        x += w + 2 * rand
        rij_h = max(rij_h, h)
    hoog = y + rij_h + rand
    beeld = Image.new("RGBA", (breed_max, hoog), (0, 0, 0, 0))
    teken = ImageDraw.Draw(beeld)
    regels = []
    for t, px, py, bb, w, h in plek:
        if w > 0 and h > 0:
            teken.text((px - bb[0], py - bb[1]), t, font=f, fill=(255, 255, 255, 255), anchor="ls")
        adv = round(f.getlength(t))
        regels.append(f"char id={ord(t)} x={px} y={py} width={w} height={h} xoffset={bb[0]} yoffset={base + bb[1]} xadvance={adv} page=0 chnl=15")
    beeld.save(f"{uitmap}/{naam}.png")
    with open(f"{uitmap}/{naam}.fnt", "w") as uit:
        uit.write(f'info face="{fid}" size={g} bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=0,0\n')
        uit.write(f"common lineHeight={regel} base={base} scaleW={breed_max} scaleH={hoog} pages=1 packed=0\n")
        uit.write(f'page id=0 file="{naam}.png"\n')
        uit.write(f"chars count={len(TEKENS)}\n")
        uit.write("\n".join(regels) + "\n")
    return g


def main(app):
    for d in sorted(os.listdir(app)):
        fm = os.path.join(app, d, "fonts")
        cij = os.path.join(fm, "ebb_cijfers.fnt")
        if not d.startswith("resources") or not os.path.exists(cij):
            continue
        lh = int(re.search(r"lineHeight=(\d+)", open(cij).read()).group(1))
        maat = MAAT[lh]
        groottes = [maak(r, fm, n, i) for r, n, i in zip(REGEL[maat], NAMEN, IDS)]
        with open(os.path.join(fm, "fonts.xml"), "w") as uit:
            uit.write("<fonts>\n")
            uit.write("    <!-- Eigen cijferletter voor het grote getal (eis 11), gemaakt met bron/maak_cijfers.py. -->\n")
            uit.write('    <font id="EbbCijfers" filename="ebb_cijfers.fnt" filter="0123456789:" antialias="true"/>\n')
            uit.write("    <!-- Keuring bouw 4 punt 4: Barlow Condensed voor alle tekst, gemaakt met bron/maak_letters.py. -->\n")
            for n, i in zip(NAMEN, IDS):
                uit.write(f'    <font id="{i}" filename="{n}.fnt" antialias="true"/>\n')
            uit.write("</fonts>\n")
        print(d, maat, REGEL[maat], "lettergrootte", groottes)


if __name__ == "__main__":
    main(sys.argv[1])
