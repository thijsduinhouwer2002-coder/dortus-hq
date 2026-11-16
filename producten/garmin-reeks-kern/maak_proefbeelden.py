"""Maakt de proefbeelden voor de reeksproef (Gijs, run 124): een schermvullend kleurverloop per
schermmaat en een eigen cijferletter (0-9 en dubbele punt) op twee maten. Alleen om geheugen te
meten, geen ontwerp. Draaien: python3 maak_proefbeelden.py"""
import os
from PIL import Image, ImageDraw, ImageFont

HIER = os.path.dirname(os.path.abspath(__file__))
TTF = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"


def verloop(maat, pad):
    im = Image.new("RGB", (maat, maat))
    px = im.load()
    for y in range(maat):
        for x in range(maat):
            t = y / (maat - 1)
            u = x / (maat - 1)
            px[x, y] = (int(10 + 60 * t + 30 * u), int(20 + 90 * (1 - t)), int(60 + 150 * (1 - t) * (0.6 + 0.4 * u)))
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    im.save(pad, optimize=True)


def letter(naam, px_hoog):
    font = ImageFont.truetype(TTF, px_hoog)
    tekens = "0123456789:"
    asc, desc = font.getmetrics()
    hoog = asc + desc
    breedtes = [int(font.getlength(c)) + 2 for c in tekens]
    per_rij = 4
    cel = max(breedtes) + 2
    rijen = (len(tekens) + per_rij - 1) // per_rij
    W = 1
    while W < cel * per_rij:
        W *= 2
    H = 1
    while H < (hoog + 2) * rijen:
        H *= 2
    im = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(im)
    regels = []
    for i, c in enumerate(tekens):
        x = (i % per_rij) * cel
        y = (i // per_rij) * (hoog + 2)
        d.text((x + 1, y), c, fill=255, font=font)
        regels.append("char id=%d x=%d y=%d width=%d height=%d xoffset=0 yoffset=0 xadvance=%d page=0 chnl=15"
                      % (ord(c), x, y, breedtes[i], hoog, breedtes[i]))
    map_ = os.path.join(HIER, "resources", "fonts")
    os.makedirs(map_, exist_ok=True)
    im.save(os.path.join(map_, naam + ".png"), optimize=True)
    with open(os.path.join(map_, naam + ".fnt"), "w") as f:
        f.write('info face="proef" size=%d bold=1 italic=0 charset="" unicode=1 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=1,1 outline=0\n' % px_hoog)
        f.write("common lineHeight=%d base=%d scaleW=%d scaleH=%d pages=1 packed=0 alphaChnl=0 redChnl=4 greenChnl=4 blueChnl=4\n" % (hoog, asc, W, H))
        f.write('page id=0 file="%s.png"\n' % naam)
        f.write("chars count=%d\n" % len(tekens))
        f.write("\n".join(regels) + "\n")
    return W, H, hoog


verloop(260, os.path.join(HIER, "resources", "drawables", "achtergrond.png"))
for m in (208, 260, 454):
    verloop(m, os.path.join(HIER, "resources-round-%dx%d" % (m, m), "drawables", "achtergrond.png"))
print("klein", letter("cijfers_klein", 56))
print("groot", letter("cijfers_groot", 110))
