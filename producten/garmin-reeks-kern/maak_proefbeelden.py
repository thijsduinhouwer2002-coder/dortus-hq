"""Maakt de letters van Tij per schermmaat (tijd, dunne tijd voor de slaapstand, BB-getal, veldgetal, datum)
op de maten uit maten-tij-tabel.md van Mila, voor alle acht ronde schermmaten. Maakt ook nog het kleurverloop
van de eerste proef (run 124) voor 208, 260 en 454 px. Draaien: python3 maak_proefbeelden.py"""
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
    # De inkt van een teken kan rechts voorbij zijn opschuifmaat steken (de T van de datum, 2 px): de cel wordt zo
    # breed als de inkt, het opschuiven blijft de maat van de letter. Zo snijdt het horloge niets af.
    inkt = [max(b, font.getbbox(c)[2]) for b, c in zip(breedtes, tekens)]
    cel = max(inkt) + 2
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
                      % (ord(c), x, y, inkt[i], hoog, breedtes[i]))
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
    <font id="TijdSlaap" filename="tijdslaap.fnt" filter="0123456789:" antialias="true"/>
    <font id="Bb" filename="bb.fnt" filter="0123456789" antialias="true"/>
    <font id="Veld" filename="veld.fnt" filter="0123456789.K" antialias="true"/>
    <font id="Datum" filename="datum.fnt" filter="0123456789 ADEFHIMNORSTUW" antialias="true"/>
</fonts>
"""
# Gewicht van de tijd in de slaapstand: dun, zodat er op een scherm dat kan inbranden minder dan 8% aan staat
# (de dikke tijd, gewicht 900, kwam op de fenix 8 op 7,9 en 9,1%; run 43993153363). De vorm is nog een keuze van Mila.
SLAAP_GEWICHT = 300
# maat van het scherm: (tijd, BB-getal, veldgetal, datum) in px, uit maten-tij-tabel.md van Mila.
MATEN = {208: (62, 23, 14, 14), 218: (65, 24, 14, 14), 240: (72, 26, 16, 16), 260: (78, 29, 17, 17),
         280: (84, 31, 18, 18), 390: (117, 43, 25, 25), 416: (125, 46, 27, 27), 454: (136, 50, 30, 30)}


def toets_tegen_blad():
    """Stopt als de lettermaten hierboven niet meer bij het blad van Mila passen."""
    import maak_maten
    blad = maak_maten.lees_blad(os.path.join(HIER, "maten-tij-tabel.md"))
    if set(blad) != set(MATEN):
        raise SystemExit("het blad heeft de schermmaten %r, dit script maakt letters voor %r" % (sorted(blad), sorted(MATEN)))
    for S, (t, b, v, dt) in MATEN.items():
        rij = dict(zip(maak_maten.NAMEN, blad[S]))
        if (rij["TIJD_PX"], rij["BB_PX"], rij["VELD_PX"], rij["DATUM_PX"]) != (t, b, v, dt):
            raise SystemExit("lettermaten voor %d px passen niet bij het blad: %r" % (S, rij))


if __name__ == "__main__":
    toets_tegen_blad()
    verloop(260, os.path.join(HIER, "resources", "drawables", "achtergrond.png"))
    for m in (208, 260, 454):
        verloop(m, os.path.join(HIER, "resources-round-%dx%d" % (m, m), "drawables", "achtergrond.png"))
    mappen = [("resources", MATEN[260])] + [("resources-round-%dx%d" % (S, S), MATEN[S]) for S in sorted(MATEN)]
    for resmap, (t, b, v, dt) in mappen:
        print(letter(resmap, "tijd", t, 900, "0123456789:"))
        print(letter(resmap, "tijdslaap", t, SLAAP_GEWICHT, "0123456789:"))
        print(letter(resmap, "bb", b, 900, "0123456789"))
        print(letter(resmap, "veld", v, 800, "0123456789.K"))
        print(letter(resmap, "datum", dt, 700, "0123456789 ADEFHIMNORSTUW"))
        open(os.path.join(HIER, resmap, "fonts", "fonts.xml"), "w").write(FONTS_XML)
