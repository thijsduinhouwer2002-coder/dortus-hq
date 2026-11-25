"""Tekst op een galerijbeeld van Click Cuts (Beeldmaker, 25 nov 2026, issue #39).

python3 tekst.py <render 2400x1350.png> <render.json> <uitmap> <fontmap> <icoon.svg> <naam>

Maakt <naam>-2400x1200.jpg (Superhive) en <naam>-1920x1080.jpg (Gumroad) uit één render van 2400x1350.
Links: klein merk, de titel en één regel uit `producten/blender-splitser/galerij.md` (onderschrift 4), met de
nummers van het snijvlak in beeld in plaats van het voorbeeld 3-5. In het beeld: een lijn naar het gegraveerde
nummer, met de maten die de add-on gaf (render.json), niet verzonnen.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON, NAAM = sys.argv[1:7]
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT = (255, 246, 230), (255, 210, 92), (222, 212, 232)
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
    laag = laag.filter(ImageFilter.GaussianBlur(schaduw))
    img.alpha_composite(laag)
    ImageDraw.Draw(img).text(xy, tekst, font=f, fill=kleur, anchor=anchor)


def regels(tekst, f, breed):
    uit, nu = [], ""
    for w in tekst.split():
        t = (nu + " " + w).strip()
        if f.getlength(t) > breed and nu:
            uit.append(nu)
            nu = w
        else:
            nu = t
    return uit + [nu]


def main():
    m = json.load(open(META))
    img = Image.open(RENDER).convert("RGBA").resize((W, H), Image.LANCZOS)
    verloop = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(verloop)
    for x in range(1200):
        dv.line([(x, 0), (x, H)], fill=int(165 * (1 - x / 1200) ** 1.5))
    img = Image.composite(Image.new("RGBA", (W, H), (14, 8, 20, 255)), img, verloop)

    x = 120
    ic = icoon(84)
    img.alpha_composite(ic, (x, 190))
    schaduwtekst(img, (x + 104, 232), "Click Cuts", font("Bricolage.ttf", 64, "Bold"), CREME, anchor="lm")
    y = 360
    for regel, kl in (("Numbered", CREME), ("for assembly.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 132, "ExtraBold"), kl)
        y += 150
    y += 40
    a, b = m["label"].split("-")
    zin = (f"Cut faces get pin holes and an engraved part number, like {a}-{b} where part {a} "
           f"meets part {b}.")
    fz = font("Inter.ttf", 46, "Medium")
    for r in regels(zin, fz, 900):
        schaduwtekst(img, (x, y), r, fz, ZACHT, schaduw=6)
        y += 64

    # lijn naar het gegraveerde nummer
    lx, ly = m["label_beeld"][0] * W, m["label_beeld"][1] * H
    dx, dy = float(os.environ.get("TK_DX", "-330")), float(os.environ.get("TK_DY", "-250"))
    ex, ey = lx + dx, ly + dy
    d = ImageDraw.Draw(img)
    import math
    ey0 = ey + 34  # de lijn begint onder de tekst
    lengte = math.hypot(lx - ex, ly - ey0)
    stop = float(os.environ.get("TK_STOP", "70"))  # de lijn stopt vóór het nummer, zodat het leesbaar blijft
    tx, ty = lx - (lx - ex) / lengte * stop, ly - (ly - ey0) / lengte * stop
    d.line([(ex, ey0), (tx, ty)], fill=GOUD, width=5)
    d.ellipse((tx - 9, ty - 9, tx + 9, ty + 9), fill=GOUD)
    fl = font("Inter.ttf", 38, "SemiBold")
    fk = font("Inter.ttf", 32, "Medium")
    schaduwtekst(img, (ex, ey - 54), f"part {a} meets part {b}", fl, CREME, schaduw=6, anchor="ma")
    schaduwtekst(img, (ex, ey - 12), f"{m['pen_d_mm']:g} mm pins, {m['speling_mm']:g} mm clearance", fk, GOUD,
                 schaduw=6, anchor="ma")

    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, f"{NAAM}-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, f"{NAAM}-1920x1080.jpg"), quality=92)
    print("klaar", NAAM)


main()
