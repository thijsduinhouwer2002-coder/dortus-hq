"""Eigen cijferletter voor het grote getal van Ebb (eis 11), als BMFont (tekstvorm + PNG) voor Connect IQ.

Waarom: de grootste systeemletter van de epix2pro47mm is 123 van 416 px (29,6%), eis 11 vraagt 30%.
Letter: Barlow Condensed Medium (SIL Open Font License, zie OFL-barlow-condensed.txt), alleen 0-9 en de dubbele punt.
Smal genoeg dat "0:00" binnen 72% van het scherm past bij cijfers van 33% hoog.
Gebruik: python3 maak_cijfers.py <cijferhoogte px> <uitmap> <naam>
"""
import sys
from PIL import Image, ImageDraw, ImageFont

import os
LETTER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "barlow-condensed-latin-500-normal.woff")
TEKENS = "0123456789:"


def maak(cijferhoogte, uitmap, naam):
    # Lettergrootte zo kiezen dat de hoogte van "0" precies cijferhoogte is.
    grootte = cijferhoogte
    for _ in range(40):
        f = ImageFont.truetype(LETTER, grootte)
        b = f.getbbox("0")
        h = b[3] - b[1]
        if abs(h - cijferhoogte) <= 0:
            break
        grootte = max(8, round(grootte * cijferhoogte / h))
    f = ImageFont.truetype(LETTER, grootte)
    stijg, daal = f.getmetrics()
    top = f.getbbox("0")[1]          # lege ruimte boven de cijfers binnen de regel
    rand = 2
    vakken = []
    x = rand
    for t in TEKENS:
        bb = f.getbbox(t)
        w = bb[2] - bb[0]
        vakken.append((t, x, bb, w))
        x += w + 2 * rand
    breedte = x
    hoogte = cijferhoogte + 2 * rand
    beeld = Image.new("RGBA", (breedte, hoogte), (0, 0, 0, 0))
    teken = ImageDraw.Draw(beeld)
    regels = []
    for t, vx, bb, w in vakken:
        teken.text((vx - bb[0], rand - top), t, font=f, fill=(255, 255, 255, 255))
        adv = round(f.getlength(t)) + max(1, round(cijferhoogte * 0.03))
        yoff = bb[1] - top
        h = bb[3] - bb[1]
        regels.append(f"char id={ord(t)} x={vx} y={rand + yoff} width={w} height={h} xoffset={bb[0]} yoffset={yoff} xadvance={adv} page=0 chnl=15")
    beeld.save(f"{uitmap}/{naam}.png")
    with open(f"{uitmap}/{naam}.fnt", "w") as uit:
        uit.write(f'info face="EbbCijfers" size={grootte} bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=0,0\n')
        uit.write(f"common lineHeight={cijferhoogte} base={cijferhoogte} scaleW={breedte} scaleH={hoogte} pages=1 packed=0\n")
        uit.write(f'page id=0 file="{naam}.png"\n')
        uit.write(f"chars count={len(TEKENS)}\n")
        uit.write("\n".join(regels) + "\n")
    print(naam, "grootte", grootte, "cijferhoogte", cijferhoogte, "beeld", breedte, "x", hoogte)


if __name__ == "__main__":
    maak(int(sys.argv[1]), sys.argv[2], sys.argv[3])
