"""Tekst en achtergrond op het galerijbeeld kom en kogel (issue #331, Beeldmaker, 28 nov 2026).

    python3 kom_kogel_tekst.py <kom-kogel-render.png (RGBA)> <kom-kogel.json> <uit.jpg> <fontmap> <icoon.svg>
Elk getal komt uit kom-kogel.json (de add-on zelf): kogel, gemeten speling, aantal delen en open randen.
Plek van de labels: KT_KOGEL=x,y en KT_KOM=x,y (pixels, op het oog in de render gemeten). De maat volgt de render
(1920x1080 of 2400x1200); letters en marges schalen mee met de hoogte.
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON = sys.argv[1:6]
m = json.load(open(META))
ren0 = Image.open(RENDER)
W, H = ren0.size   # 1920x1080 (Gumroad) of 2400x1200 (Superhive, #338 M2)
S = H / 1080       # tekst en marges schalen mee met de hoogte
SX = W / 1920


def s_(v):
    return int(round(v * S))

CREME, GOUD, GRIJS = (255, 246, 230), (255, 185, 56), (190, 178, 205)


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


# achtergrond: donker pruim met een paarse gloed achter het figuur en een fijn raster onderin, als het hoofdbeeld
bg = Image.new("RGB", (W, H), (20, 12, 26))
gl = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(gl)
d.ellipse((900 * SX, -250 * S, 2150 * SX, 900 * S), fill=255)
gl = gl.filter(ImageFilter.GaussianBlur(s_(260)))
bg = Image.composite(Image.new("RGB", (W, H), (88, 40, 128)), bg, gl.point(lambda v: int(v * 0.85)))
bg = bg.convert("RGBA")
ren = Image.open(RENDER).convert("RGBA")
schaduw = Image.new("RGBA", (W, H), (0, 0, 0, 0))
schaduw.putalpha(ren.getchannel("A").filter(ImageFilter.GaussianBlur(s_(40))).point(lambda v: int(v * 0.55)))
bg.alpha_composite(schaduw, (0, s_(18)))
bg.alpha_composite(ren)
img = bg
d = ImageDraw.Draw(img)

# links zachte donkere overgang achter de tekst
mk = Image.new("L", (W, 1), 0)
for x in range(W):
    mk.putpixel((x, 0), int(170 * max(0.0, 1 - x / (900 * S)) ** 1.5))
img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), (14, 8, 20, 255)), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mk.resize((W, H))))
d = ImageDraw.Draw(img)

X = s_(96)
# kop: icoon en productnaam
os.system(f"rsvg-convert -w {s_(76)} '{ICOON}' -o /tmp/_kk_icoon.png")
ic = Image.open("/tmp/_kk_icoon.png").convert("RGBA")
img.alpha_composite(ic, (X, s_(84)))
d.text((X + s_(100), s_(122)), "Click Joints Pro", font=font("Inter.ttf", s_(34), "Medium"), fill=CREME, anchor="lm")

# titel en één regel
ft = font("Bricolage.ttf", s_(104), "Bold")
d.text((X, s_(230)), "Clean cuts.", font=ft, fill=CREME)
d.text((X, s_(350)), "Closed parts.", font=ft, fill=CREME)
fs = font("Bricolage.ttf", s_(44), "SemiBold")
d.text((X, s_(492)), "The real mesh of a hip joint", font=fs, fill=GOUD)
d.text((X, s_(546)), "from Figure from rig.", font=fs, fill=GOUD)

# drie feiten uit de add-on
fb = font("Inter.ttf", s_(34), "Regular")
dl = sum(1 for _ in m["open_randen"])
open_tot = sum(m["open_randen"].values())
feiten = [f"Ball {m['kogel_d_mm']:.1f} mm, swings ±{m['graden']:.0f}°",
          f"Clearance {m['speling_gemeten_mm']:.2f} mm, measured",
          f"{dl} parts, {open_tot} open edges"]
y = s_(668)
for t in feiten:
    d.ellipse((X, y + s_(12), X + s_(16), y + s_(28)), fill=GOUD)
    d.text((X + s_(36), y), t, font=fb, fill=CREME)
    y += s_(62)

# voetregel: wat je ziet
fv = font("Inter.ttf", s_(22), "Regular")
d.text((X, H - s_(70)), "Render of the add-on's own output in Blender, wireframe on. Figure CC0.", font=fv, fill=GRIJS)


def pil(tekst, punt, kant, dx, maat=None, plek=None):
    """Label als pil met gouden rand, lijn naar het punt (zoals de labels op het hoofdbeeld)."""
    f = font("Inter.ttf", maat or s_(30), "SemiBold")
    bw = d.textlength(tekst, font=f) + s_(40)
    bh = s_(54)
    px_, py_ = punt
    lx = px_ + dx if kant > 0 else px_ - dx - bw
    ly = py_ - bh / 2
    lx = min(lx, W - bw - s_(24))
    eind = lx if kant > 0 else lx + bw
    if plek:   # pil op een vaste plek (midden x,y), schuine lijn naar de onderrand
        lx, ly = plek[0] - bw / 2, plek[1] - bh / 2
        d.line((px_, py_, plek[0] - bw * 0.25, ly + bh), fill=GOUD, width=s_(3))
        py_l = plek[1]
    else:
        d.line((px_, py_, eind, py_), fill=GOUD, width=s_(3))
        py_l = py_
    r9 = s_(9)
    d.ellipse((px_ - r9, py_ - r9, px_ + r9, py_ + r9), fill=GOUD, outline=(20, 12, 26), width=s_(3))
    d.rounded_rectangle((lx, ly, lx + bw, ly + bh), radius=bh / 2, fill=(26, 16, 34, 235), outline=GOUD, width=s_(3))
    d.text((lx + bw / 2, py_l), tekst, font=f, fill=CREME, anchor="mm")


kx, ky = (float(v) for v in os.environ.get("KT_KOGEL", "1600,330").split(","))
ox, oy = (float(v) for v in os.environ.get("KT_KOM", "1790,640").split(","))
pil(f"Ball {m['kogel_d_mm']:.1f} mm", (kx, ky), 1, float(os.environ.get("KT_KOGEL_DX", "60")))
plek = tuple(float(v) for v in os.environ["KT_KOM_PIL"].split(",")) if os.environ.get("KT_KOM_PIL") else None
pil(f"Socket, {m['speling_gemeten_mm']:.2f} mm gap", (ox, oy), 1, float(os.environ.get("KT_KOM_DX", "50")), plek=plek)

img.convert("RGB").save(UIT, quality=92)
print("klaar", UIT)
