"""Tekst op het hoofdbeeld van Click Cuts (Beeldmaker, 25 nov 2026, issue #13).

python3 tekst.py <render 2400x1350.png> <render.json> <uitmap> <fontmap> <icoon.svg> <naam> [kort]

Maakt <naam>-2400x1200.jpg (Superhive) en <naam>-1920x1080.jpg (Gumroad) uit één render van 2400x1350.
Links: icoon, naam, de haak die blind won ("Pick your printer. Click once. Every part fits.") en drie regels.
In het beeld: wat het voor-model meet en hoeveel stukken de add-on maakte; die getallen komen uit render.json
(wat de add-on meldde), niet verzonnen.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON, NAAM = sys.argv[1:7]
KORT = len(sys.argv) > 7 and sys.argv[7] == "kort"  # zonder de drie regels
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT = (255, 246, 230), (255, 210, 92), (222, 212, 232)
W, H = 2400, 1350

PUNTEN = [
    "Cuts your model to fit your printer bed",
    "Pins, holes and part numbers on every cut",
    "Fit test block, so pins fit your printer",
]


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


def pil(img, x0, y0, x1, y1, kleur, dik=6):
    """Gebogen pijl van (x0,y0) naar (x1,y1)."""
    d = ImageDraw.Draw(img)
    pts = []
    for i in range(41):
        t = i / 40
        mx, my = (x0 + x1) / 2, min(y0, y1) - 90
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t ** 2 * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t ** 2 * y1
        pts.append((x, y))
    d.line(pts[:-3], fill=kleur, width=dik, joint="curve")
    (ax, ay), (bx, by) = pts[-6], pts[-1]
    import math
    hoek = math.atan2(by - ay, bx - ax)
    L = 30
    p1 = (bx - L * math.cos(hoek - 0.45), by - L * math.sin(hoek - 0.45))
    p2 = (bx - L * math.cos(hoek + 0.45), by - L * math.sin(hoek + 0.45))
    d.polygon([(bx, by), p1, p2], fill=kleur)


def main():
    meta = json.load(open(META))
    img = Image.open(RENDER).convert("RGBA").resize((W, H), Image.LANCZOS)
    # zachte donkere gloed links achter de tekst
    verloop = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(verloop)
    for x in range(1100):
        dv.line([(x, 0), (x, H)], fill=int(150 * (1 - x / 1100) ** 1.6))
    zwart = Image.new("RGBA", (W, H), (14, 8, 20, 255))
    img = Image.composite(zwart, img, verloop)

    x = 120
    ic = icoon(150)
    img.alpha_composite(ic, (x, 175))
    schaduwtekst(img, (x + 182, 238), "Click Cuts", font("Bricolage.ttf", 168, "ExtraBold"), CREME, anchor="lm")
    y = 400
    for regel, kl in (("Pick your printer.", CREME), ("Click once.", CREME), ("Every part fits.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 92, "Bold"), kl)
        y += 108
    y += 50
    fp = font("Inter.ttf", 40, "Medium")
    d = ImageDraw.Draw(img)
    for p in ([] if KORT else PUNTEN):
        d.ellipse((x, y + 14, x + 18, y + 32), fill=GOUD)
        schaduwtekst(img, (x + 40, y), p, fp, ZACHT, schaduw=6)
        y += 66

    # labels in de scène
    fl = font("Inter.ttf", 34, "SemiBold")
    fk = font("Inter.ttf", 30, "Medium")
    v = meta["vak_voor"]
    n = meta["vak_na"]
    b = meta["vak_bed"]
    bx_mid = (b[0] + b[1]) / 2 * W
    onder = max(v[3], n[3]) * H + 40
    schaduwtekst(img, (bx_mid, onder), f"Too big: {meta['hoogte_mm']:.0f} mm tall", fl, CREME, anchor="ma")
    schaduwtekst(img, (bx_mid, onder + 46), f"gold box: {meta['bed_mm']:.0f} mm printer bed", fk, GOUD, anchor="ma")
    nx = (n[0] + n[1]) / 2 * W
    schaduwtekst(img, (nx, onder), f"{meta['stukken']} parts, {meta['pennen']} pins", fl, CREME, anchor="ma")
    schaduwtekst(img, (nx, onder + 46), "every part fits the bed", fk, GOUD, anchor="ma")
    # pijl met "1 click" tussen voor en na, op de hoogte van het bovenste deel van het bouwvolume
    px0 = v[1] * W + 18
    px1 = n[0] * W - 12
    py = (b[2] + 0.25 * (b[3] - b[2])) * H
    pil(img, px0, py, px1, py, GOUD)
    schaduwtekst(img, ((px0 + px1) / 2, py - 105), "1 click", font("Bricolage.ttf", 54, "Bold"), GOUD, anchor="ma")

    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, f"{NAAM}-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, f"{NAAM}-1920x1080.jpg"), quality=92)
    print("klaar", NAAM)


main()
