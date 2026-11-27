"""Galerijbeeld Click Cuts 1.1 "Draw your own cut" (Beeldmaker, 27 nov 2026).

python3 tekst_tekenen.py <tekenen-scherm.png> <tekenen.json> <uitmap> <fontmap> <icoon.svg>

Maakt tekenen-2400x1200.jpg (Superhive) en tekenen-1920x1080.jpg (Gumroad). Links: merk, titel en de regel uit de
releasenote 1.1.0 (`producten/blender-splitser/CHANGELOG.md` op tak claude/click-cuts-1.1), met de drie stappen.
Rechts de echte schermafbeelding van Blender 5.3 (uit tekenen.py, niets nagetekend), en het paneel Click Cuts uit
diezelfde schermafbeelding vergroot. Het paneel is pixel voor pixel uit de schermafbeelding.
Omgeving: TK_KADER (x0,y0,x1,y1 van het paneel in px van 2880x1620), TK_RIJ (y van de rij Draw cut en Cut piece),
TK_LIJN_PX (x,y van het begin van de getekende lijn in de schermafbeelding), TK_SX0 (linkerrand van de uitsnede).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

SCHERM, META, UIT, FONTS, ICOON = sys.argv[1:6]
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT, NACHT = (255, 246, 230), (255, 210, 92), (222, 212, 232), (14, 8, 20)
W, H = 2400, 1350


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


def icoon(maat):
    p = os.path.join(UIT, f"_icoon_{maat}.png")
    os.system(f"rsvg-convert -w {maat} '{ICOON}' -o '{p}'")
    im = Image.open(p).convert("RGBA")
    os.remove(p)
    return im


def schaduwtekst(img, xy, tekst, f, kleur, schaduw=10, anchor="la"):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).text(xy, tekst, font=f, fill=(0, 0, 0, 170), anchor=anchor)
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(schaduw)))
    ImageDraw.Draw(img).text(xy, tekst, font=f, fill=kleur, anchor=anchor)


def schaduw(img, box, straal, blur=26, kracht=190, dy=18):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    x0, y0, x1, y1 = box
    ImageDraw.Draw(laag).rounded_rectangle((x0, y0 + dy, x1, y1 + dy), radius=straal, fill=(0, 0, 0, kracht))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(blur)))


def plak_rond(img, beeld, xy, straal, rand=None, dikte=3):
    m = Image.new("L", beeld.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, beeld.size[0] - 1, beeld.size[1] - 1), radius=straal, fill=255)
    img.paste(beeld, xy, m)
    if rand:
        ImageDraw.Draw(img).rounded_rectangle((xy[0], xy[1], xy[0] + beeld.size[0], xy[1] + beeld.size[1]),
                                              radius=straal, outline=rand + (255,), width=dikte)


def bol(img, c, r, tekst, f):
    d = ImageDraw.Draw(img)
    schaduw(img, (c[0] - r, c[1] - r, c[0] + r, c[1] + r), r, blur=10, kracht=160, dy=6)
    d.ellipse((c[0] - r, c[1] - r, c[0] + r, c[1] + r), fill=GOUD + (255,))
    d.text((c[0], c[1] + 2), tekst, font=f, fill=NACHT + (255,), anchor="mm")


def main():
    m = json.load(open(META))
    sch = Image.open(SCHERM).convert("RGBA")
    SW, SH = sch.size
    k = [int(v) for v in os.environ.get("TK_KADER", "2456,120,2840,530").split(",")]
    rij = int(os.environ.get("TK_RIJ", "472"))
    lijn = [int(v) for v in os.environ.get("TK_LIJN_PX", "722,926").split(",")]

    img = Image.new("RGBA", (W, H), NACHT + (255,))
    gloed = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(gloed).ellipse((1050, 150, 2350, 1250), fill=(70, 40, 110, 150))
    img.alpha_composite(gloed.filter(ImageFilter.GaussianBlur(200)))

    # rechts: de echte schermafbeelding, afgerond en met schaduw
    sx0 = int(os.environ.get("TK_SX0", "660"))
    sy0, sx1, sy1 = 100, SW, SH - 40
    uit = sch.crop((sx0, sy0, sx1, sy1))
    sw = int(os.environ.get("TK_BREED", "1440"))
    s = sw / uit.size[0]
    sh = int(uit.size[1] * s)
    uit = uit.resize((sw, sh), Image.LANCZOS)
    bx, by = W - sw - 50, (H - sh) // 2
    schaduw(img, (bx, by, bx + sw, by + sh), 26)
    plak_rond(img, uit, (bx, by), 26, rand=(70, 60, 85), dikte=2)

    # het paneel uit dezelfde schermafbeelding, vergroot
    pan = sch.crop(tuple(k))
    v = float(os.environ.get("TK_VERGROOT", "1.5"))
    pw, ph = int(pan.size[0] * v), int(pan.size[1] * v)
    pan = pan.resize((pw, ph), Image.LANCZOS)
    px = W - pw - 70
    py = int(os.environ.get("TK_PY", "470"))
    kx0, ky0 = bx + (k[0] - sx0) * s, by + (k[1] - sy0) * s
    kx1, ky1 = bx + (k[2] - sx0) * s, by + (k[3] - sy0) * s
    d = ImageDraw.Draw(img)
    for a, b in (((kx0, ky1), (px, py + ph)), ((kx1, ky1), (px + pw, py + ph))):
        d.line([a, b], fill=(150, 140, 160, 150), width=2)
    d.rounded_rectangle((kx0, ky0, kx1, ky1), radius=6, outline=(150, 140, 160, 255), width=2)
    schaduw(img, (px, py, px + pw, py + ph), 22, blur=30, kracht=220, dy=22)
    plak_rond(img, pan, (px, py), 22, rand=GOUD, dikte=4)

    fb = font("Bricolage.ttf", 50, "ExtraBold")
    yr = py + (rij - k[1]) * v
    bol(img, (px - 6, yr), 38, "1", fb)            # Draw cut
    bol(img, (px + pw + 6, yr), 38, "3", fb)       # Cut piece
    bol(img, (bx + (lijn[0] - sx0) * s - 44, by + (lijn[1] - sy0) * s), 38, "2", fb)  # begin van de getekende lijn

    # links: merk, nieuw in 1.1, titel, regel en de drie stappen
    x = 100
    ic = icoon(80)
    img.alpha_composite(ic, (x, 150))
    schaduwtekst(img, (x + 100, 190), "Click Cuts", font("Bricolage.ttf", 60, "Bold"), CREME, anchor="lm")
    fp = font("Inter.ttf", 34, "SemiBold")
    pt = "New in 1.1"
    tb = d.textbbox((0, 0), pt, font=fp)
    pxl = x + 420
    d.rounded_rectangle((pxl, 166, pxl + tb[2] + 44, 214), radius=24, fill=GOUD + (255,))
    d.text((pxl + 22, 190), pt, font=fp, fill=NACHT + (255,), anchor="lm")
    y = 280
    for regel, kl in (("Draw your", CREME), ("own cut.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 116, "ExtraBold"), kl)
        y += 132
    y += 26
    fz = font("Inter.ttf", 40, "Medium")
    for r in ("Keep the face whole: cut under", "the chin or at the shoulder.", "The part that comes off lights up", "white before you cut."):
        schaduwtekst(img, (x, y), r, fz, ZACHT, schaduw=6)
        y += 54
    y += 46
    fs = font("Inter.ttf", 44, "SemiBold")
    fk = font("Inter.ttf", 34, "Medium")
    stappen = (("Press Draw cut", "after Split to fit, on any part"),
               ("Drag a line", "where you want it cut"),
               ("Press Cut piece", "or Flip side for the other part"))
    for i, (kop, onder) in enumerate(stappen):
        bol(img, (x + 36, y + 36), 36, str(i + 1), font("Bricolage.ttf", 46, "ExtraBold"))
        schaduwtekst(img, (x + 100, y + 4), kop, fs, CREME, schaduw=6)
        schaduwtekst(img, (x + 100, y + 60), onder, fk, ZACHT, schaduw=6)
        y += 124

    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, "tekenen-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, "tekenen-1920x1080.jpg"), quality=92)
    print("klaar tekenen", m.get("stuk"), m.get("eraf"))


main()
