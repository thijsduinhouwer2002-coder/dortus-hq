"""Maakt de proefbeelden voor de reeksproef (Gijs, run 124): een schermvullend kleurverloop per
schermmaat en de vier letters van Tij (tijd, BB-getal, veldgetal, datum) op de maten van Mila voor 208, 260 en 454 px. Alleen om geheugen te
meten, geen ontwerp. Draaien: python3 maak_proefbeelden.py"""
import os
from PIL import Image, ImageDraw, ImageFont

HIER = os.path.dirname(os.path.abspath(__file__))
# Letter van Mila (Big Shoulders Display, OFL), kopie uit ontwerp/garmin/reeks/.
TTF = os.path.join(HIER, "BigShouldersDisplay.ttf")


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


def letter(resmap, naam, px, gewicht, tekens):
    font = ImageFont.truetype(TTF, px)
    font.set_variation_by_axes([gewicht])
    asc, desc = font.getmetrics()
    hoog = asc + desc
    breedtes = [max(1, int(font.getlength(c) + 0.999)) for c in tekens]
    cel = max(breedtes) + 2
    # zo vierkant mogelijk, zijden een macht van twee
    W = 32
    while True:
        per_rij = max(1, W // cel)
        rijen = (len(tekens) + per_rij - 1) // per_rij
        if rijen * (hoog + 2) <= W:
            break
        W *= 2
    H = 32
    while H < rijen * (hoog + 2):
        H *= 2
    im = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(im)
    regels = []
    for i, c in enumerate(tekens):
        x = (i % per_rij) * cel
        y = (i // per_rij) * (hoog + 2)
        d.text((x, y), c, fill=255, font=font)
        regels.append("char id=%d x=%d y=%d width=%d height=%d xoffset=0 yoffset=0 xadvance=%d page=0 chnl=15"
                      % (ord(c), x, y, breedtes[i], hoog, breedtes[i]))
    map_ = os.path.join(HIER, resmap, "fonts")
    os.makedirs(map_, exist_ok=True)
    im.save(os.path.join(map_, naam + ".png"), optimize=True)
    with open(os.path.join(map_, naam + ".fnt"), "w") as f:
        f.write('info face="proef" size=%d bold=1 italic=0 charset="" unicode=1 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=1,1 outline=0\n' % px)
        f.write("common lineHeight=%d base=%d scaleW=%d scaleH=%d pages=1 packed=0 alphaChnl=0 redChnl=4 greenChnl=4 blueChnl=4\n" % (hoog, asc, W, H))
        f.write('page id=0 file="%s.png"\n' % naam)
        f.write("chars count=%d\n" % len(tekens))
        f.write("\n".join(regels) + "\n")
    return "%s/%s %dpx: blad %dx%d" % (resmap, naam, px, W, H)


FONTS_XML = """<fonts>
    <font id="Tijd" filename="tijd.fnt" filter="0123456789:" antialias="true"/>
    <font id="Bb" filename="bb.fnt" filter="0123456789" antialias="true"/>
    <font id="Veld" filename="veld.fnt" filter="0123456789.K" antialias="true"/>
    <font id="Datum" filename="datum.fnt" filter="0123456789 ADEFHIMNORSTUW" antialias="true"/>
</fonts>
"""
# maat van het scherm: (tijd, BB-getal, veldgetal, datum) in px, uit maten-tij-tabel.md van Mila.
# 208 staat niet in haar tabel: 260 maal 0,8.
MATEN = {"resources": (78, 29, 17, 17), "resources-round-208x208": (62, 23, 14, 14),
         "resources-round-260x260": (78, 29, 17, 17), "resources-round-454x454": (136, 50, 30, 30)}
verloop(260, os.path.join(HIER, "resources", "drawables", "achtergrond.png"))
for m in (208, 260, 454):
    verloop(m, os.path.join(HIER, "resources-round-%dx%d" % (m, m), "drawables", "achtergrond.png"))
for resmap, (t, b, v, dt) in MATEN.items():
    print(letter(resmap, "tijd", t, 900, "0123456789:"))
    print(letter(resmap, "bb", b, 900, "0123456789"))
    print(letter(resmap, "veld", v, 800, "0123456789.K"))
    print(letter(resmap, "datum", dt, 700, "0123456789 ADEFHIMNORSTUW"))
    open(os.path.join(HIER, resmap, "fonts", "fonts.xml"), "w").write(FONTS_XML)
