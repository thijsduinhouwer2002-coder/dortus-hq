"""Galerijbeeld Click Joints Pro "From your rig in one click" (Beeldmaker, 27 nov 2026, issue #259).

python3 tekst_paneel_rig.py <rig-voor.png> <rig-na.png> <paneel-rig.json> <uitmap> <fontmap> <icoon.svg>

Maakt paneel-rig-2400x1200.jpg (Superhive) en paneel-rig-1920x1080.jpg (Gumroad). Links: merk, titel, één regel en
drie stappen. Rechts de echte schermafbeelding van Blender 5.3 met de Pro-add-on uit main (paneel_rig.py): figuur
met rig, paneel met "Rig found" en Figure from rig bovenaan. Dat stuk paneel komt vergroot uit dezelfde
schermafbeelding (pixel voor pixel, niets nagetekend). Onderaan een kaartje uit de tweede schermafbeelding: dezelfde
figuur na één druk op die knop. Getallen (aantal gewrichten, buigbereik) komen uit paneel-rig.json.
Omgeving: PR_KADER (x0,y0,x1,y1 van het stuk paneel in px van 2880x1620), PR_NA (uitsnede van het kaartje).
"""
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

VOOR, NA, META, UIT, FONTS, ICOON = sys.argv[1:7]
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT, NACHT, GROEN = (255, 246, 230), (255, 196, 84), (222, 212, 232), (16, 10, 22), (69, 235, 182)
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
    voor = Image.open(VOOR).convert("RGBA")
    na = Image.open(NA).convert("RGBA")
    SW, SH = voor.size
    aantal = int(re.match(r"(\d+) joints", m["samenvatting"]).group(1))
    knie = next(r for r in m["regels"] if r.startswith("Left knee"))
    knie_graden = re.search(r"(\d+)–(\d+)°", knie).groups()
    k = [int(v) for v in os.environ.get("PR_KADER", "2452,118,2842,316").split(",")]

    img = Image.new("RGBA", (W, H), NACHT + (255,))
    gloed = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(gloed).ellipse((1100, 150, 2350, 1250), fill=(40, 90, 80, 120))
    img.alpha_composite(gloed.filter(ImageFilter.GaussianBlur(220)))

    # rechts: de echte schermafbeelding (figuur met rig en de zijbalk)
    sx0, sy0, sx1, sy1 = int(os.environ.get("PR_SX0", "860")), 60, SW, SH - 30
    uit = voor.crop((sx0, sy0, sx1, sy1))
    sh = 1040
    s = sh / uit.size[1]
    sw = int(uit.size[0] * s)
    uit = uit.resize((sw, sh), Image.LANCZOS)
    bx, by = W - sw - 60, (H - sh) // 2
    schaduw(img, (bx, by, bx + sw, by + sh), 26)
    plak_rond(img, uit, (bx, by), 26, rand=(70, 60, 85), dikte=2)

    # het stuk paneel met Rig found en Figure from rig, vergroot uit dezelfde schermafbeelding
    pan = voor.crop(tuple(k))
    v = float(os.environ.get("PR_VERGROOT", "1.75"))
    pw, ph = int(pan.size[0] * v), int(pan.size[1] * v)
    pan = pan.resize((pw, ph), Image.LANCZOS)
    px, py = W - pw - 100, int(os.environ.get("PR_PY", "440"))
    kx0, ky0 = bx + (k[0] - sx0) * s, by + (k[1] - sy0) * s
    kx1, ky1 = bx + (k[2] - sx0) * s, by + (k[3] - sy0) * s
    d = ImageDraw.Draw(img)
    for a, b in (((kx0, ky1), (px, py)), ((kx1, ky1), (px + pw, py))):
        d.line([a, b], fill=GOUD + (150,), width=3)
    d.rounded_rectangle((kx0, ky0, kx1, ky1), radius=8, outline=GOUD + (255,), width=3)
    schaduw(img, (px, py, px + pw, py + ph), 22, blur=30, kracht=220, dy=22)
    plak_rond(img, pan, (px, py), 22, rand=GOUD, dikte=4)
    # rij "Figure from rig" in het vergrote paneel: bol 1 ervoor
    rij = int(os.environ.get("PR_RIJ", "241"))
    bol(img, (px - 6, py + (rij - k[1]) * v), 38, "1", font("Bricolage.ttf", 50, "ExtraBold"))

    # kaartje: dezelfde figuur na één klik (tweede schermafbeelding)
    nk = [int(v) for v in os.environ.get("PR_NA", "1000,200,1840,1380").split(",")]
    kaart = na.crop(tuple(nk))
    kh = int(os.environ.get("PR_KH", "560"))
    kw = int(kaart.size[0] * kh / kaart.size[1])
    kaart = kaart.resize((kw, kh), Image.LANCZOS)
    kx, ky = W - kw - int(os.environ.get("PR_KX", "130")), by + sh - kh - 40
    schaduw(img, (kx, ky, kx + kw, ky + kh), 22, blur=30, kracht=220, dy=22)
    plak_rond(img, kaart, (kx, ky), 22, rand=GROEN, dikte=4)
    lab = f"After one click: {aantal} joints"
    fl = font("Inter.ttf", 30, "SemiBold")
    tw = d.textlength(lab, font=fl)
    d.rounded_rectangle((kx + 16, ky + 16, kx + 16 + tw + 36, ky + 64), radius=24, fill=(16, 10, 22, 235))
    d.text((kx + 34, ky + 40), lab, font=fl, fill=GROEN + (255,), anchor="lm")

    # links: merk, titel, regel en de drie stappen
    x = 110
    img.alpha_composite(icoon(80), (x, 150))
    schaduwtekst(img, (x + 100, 190), "Click Joints Pro", font("Bricolage.ttf", 60, "Bold"), CREME, anchor="lm")
    y = 285
    for regel, kl in (("From your rig", CREME), ("in one click.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 116, "ExtraBold"), kl)
        y += 132
    y += 26
    fz = font("Inter.ttf", 40, "Medium")
    for r in ("Rig found? Figure from rig sits at", "the top of the Click Joints tab."):
        schaduwtekst(img, (x, y), r, fz, ZACHT, schaduw=6)
        y += 56
    y += 50
    fs = font("Inter.ttf", 44, "SemiBold")
    fk = font("Inter.ttf", 32, "Medium")
    stappen = (("Select your rigged figure", "Mixamo or Rigify bones, or your own"),
               ("Figure from rig", f"{aantal} joints: hinges on knees and elbows,"),
               ("Bend range from the rig", f"knee {knie_graden[0]} to {knie_graden[1]}°, then export STL or 3MF"))
    extra = {1: "balls on hips, shoulders and neck"}
    for i, (kop, onder) in enumerate(stappen):
        bol(img, (x + 36, y + 36), 36, str(i + 1), font("Bricolage.ttf", 46, "ExtraBold"))
        schaduwtekst(img, (x + 100, y + 4), kop, fs, CREME, schaduw=6)
        schaduwtekst(img, (x + 100, y + 60), onder, fk, ZACHT, schaduw=6)
        if i in extra:
            schaduwtekst(img, (x + 100, y + 102), extra[i], fk, ZACHT, schaduw=6)
            y += 42
        y += 128

    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, "paneel-rig-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, "paneel-rig-1920x1080.jpg"), quality=92)
    print("klaar paneel-rig")


main()
