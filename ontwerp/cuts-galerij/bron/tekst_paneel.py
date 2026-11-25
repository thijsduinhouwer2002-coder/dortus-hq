"""Galerijbeeld Click Cuts "Three steps in one tab" (Beeldmaker, 25 nov 2026, issue #39).

python3 tekst_paneel.py <paneel-scherm.png> <paneel.json> <uitmap> <fontmap> <icoon.svg>

Maakt paneel-2400x1200.jpg (Superhive) en paneel-1920x1080.jpg (Gumroad). Links: merk, titel en de regel uit
onderschrift 7 van `producten/blender-splitser/galerij.md`, met de drie stappen. Rechts de echte schermafbeelding
van Blender 5.3 (uit paneel.py, niets nagetekend), en het paneel Click Cuts uit diezelfde schermafbeelding vergroot,
met de nummers 1, 2 en 3 bij printer, Split to fit en Export. Het paneel is pixel voor pixel uit de schermafbeelding.
Omgeving: PN_KADER (x0,y0,x1,y1 van het paneel in de schermafbeelding, in px van 2880x1620),
PN_RIJEN (y van printer, Split to fit, Export in diezelfde px).
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
    k = [int(v) for v in os.environ.get("PN_KADER", "2452,118,2842,548").split(",")]
    rijen = [int(v) for v in os.environ.get("PN_RIJEN", "220,310,477").split(",")]

    # achtergrond: nacht met een zachte gloed achter het beeld
    img = Image.new("RGBA", (W, H), NACHT + (255,))
    gloed = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(gloed).ellipse((1150, 150, 2350, 1250), fill=(70, 40, 110, 150))
    img.alpha_composite(gloed.filter(ImageFilter.GaussianBlur(200)))

    # rechts: de echte schermafbeelding (3D-venster met zijbalk), afgerond en met schaduw
    sx0, sy0, sx1, sy1 = 700, 0, SW, SH - 30
    uit = sch.crop((sx0, sy0, sx1, sy1))
    sh = 1040
    s = sh / uit.size[1]
    sw = int(uit.size[0] * s)
    uit = uit.resize((sw, sh), Image.LANCZOS)
    bx, by = W - sw - 60, (H - sh) // 2
    schaduw(img, (bx, by, bx + sw, by + sh), 26)
    plak_rond(img, uit, (bx, by), 26, rand=(70, 60, 85), dikte=2)

    # het paneel uit dezelfde schermafbeelding, vergroot
    pan = sch.crop(tuple(k))
    v = float(os.environ.get("PN_VERGROOT", "1.62"))
    pw, ph = int(pan.size[0] * v), int(pan.size[1] * v)
    pan = pan.resize((pw, ph), Image.LANCZOS)
    px = W - pw - 110
    py = int(os.environ.get("PN_PY", "330"))
    # waar het paneel klein in de schermafbeelding staat: dun gouden kader en twee lijnen naar de vergroting
    kx0, ky0 = bx + (k[0] - sx0) * s, by + (k[1] - sy0) * s
    kx1, ky1 = bx + (k[2] - sx0) * s, by + (k[3] - sy0) * s
    d = ImageDraw.Draw(img)
    for a, b in (((kx0, ky1), (px, py + ph)), ((kx1, ky1), (px + pw, py + ph))):
        d.line([a, b], fill=GOUD + (150,), width=3)
    d.rounded_rectangle((kx0, ky0, kx1, ky1), radius=8, outline=GOUD + (255,), width=3)
    schaduw(img, (px, py, px + pw, py + ph), 22, blur=30, kracht=220, dy=22)
    plak_rond(img, pan, (px, py), 22, rand=GOUD, dikte=4)

    # nummers 1, 2, 3 links naast de rijen van het vergrote paneel
    fb = font("Bricolage.ttf", 50, "ExtraBold")
    for i, y in enumerate(rijen):
        bol(img, (px - 6, py + (y - k[1]) * v), 38, str(i + 1), fb)

    # links: merk, titel, regel en de drie stappen
    x = 110
    ic = icoon(80)
    img.alpha_composite(ic, (x, 150))
    schaduwtekst(img, (x + 100, 190), "Click Cuts", font("Bricolage.ttf", 60, "Bold"), CREME, anchor="lm")
    y = 285
    for regel, kl in (("Three steps", CREME), ("in one tab.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 124, "ExtraBold"), kl)
        y += 140
    y += 26
    fz = font("Inter.ttf", 42, "Medium")
    for r in ("Press N in the 3D viewport and", "open the Click Cuts tab."):
        schaduwtekst(img, (x, y), r, fz, ZACHT, schaduw=6)
        y += 58
    y += 54
    fs = font("Inter.ttf", 44, "SemiBold")
    fk = font("Inter.ttf", 34, "Medium")
    stappen = (("Pick your printer", "Bambu, Prusa, Creality or your own size"),
               ("Split to fit", f"{m['stukken']} parts, all fit the bed"),
               ("Export", "STL or 3MF, in millimeters"))
    for i, (kop, onder) in enumerate(stappen):
        bol(img, (x + 36, y + 36), 36, str(i + 1), font("Bricolage.ttf", 46, "ExtraBold"))
        schaduwtekst(img, (x + 100, y + 4), kop, fs, CREME, schaduw=6)
        schaduwtekst(img, (x + 100, y + 60), onder, fk, ZACHT, schaduw=6)
        y += 132

    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, "paneel-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, "paneel-1920x1080.jpg"), quality=92)
    print("klaar paneel")


main()
