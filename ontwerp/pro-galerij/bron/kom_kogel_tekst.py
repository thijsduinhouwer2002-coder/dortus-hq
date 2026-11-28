"""Tekst en achtergrond op het galerijbeeld kom en kogel (issue #331, Beeldmaker, 28 nov 2026).

    python3 kom_kogel_tekst.py <kom-kogel-render.png (RGBA)> <kom-kogel.json> <uit.jpg> <fontmap> <icoon.svg>
Elk getal komt uit kom-kogel.json (de add-on zelf): kogel, gemeten speling, aantal delen en open randen.
Plek van de labels: KT_KOGEL=x,y en KT_KOM=x,y (pixels, op het oog in de render gemeten).
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON = sys.argv[1:6]
m = json.load(open(META))
W, H = 1920, 1080
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
d.ellipse((900, -250, 2150, 900), fill=255)
gl = gl.filter(ImageFilter.GaussianBlur(260))
bg = Image.composite(Image.new("RGB", (W, H), (88, 40, 128)), bg, gl.point(lambda v: int(v * 0.85)))
bg = bg.convert("RGBA")
ren = Image.open(RENDER).convert("RGBA")
schaduw = Image.new("RGBA", (W, H), (0, 0, 0, 0))
schaduw.putalpha(ren.getchannel("A").filter(ImageFilter.GaussianBlur(40)).point(lambda v: int(v * 0.55)))
bg.alpha_composite(schaduw, (0, 18))
bg.alpha_composite(ren)
img = bg
d = ImageDraw.Draw(img)

# links zachte donkere overgang achter de tekst
mk = Image.new("L", (W, 1), 0)
for x in range(W):
    mk.putpixel((x, 0), int(170 * max(0.0, 1 - x / 900) ** 1.5))
img.alpha_composite(Image.composite(Image.new("RGBA", (W, H), (14, 8, 20, 255)), Image.new("RGBA", (W, H), (0, 0, 0, 0)), mk.resize((W, H))))
d = ImageDraw.Draw(img)

X = 96
# kop: icoon en productnaam
os.system(f"rsvg-convert -w 76 '{ICOON}' -o /tmp/_kk_icoon.png")
ic = Image.open("/tmp/_kk_icoon.png").convert("RGBA")
img.alpha_composite(ic, (X, 84))
d.text((X + 100, 122), "Click Joints Pro", font=font("Inter.ttf", 34, "Medium"), fill=CREME, anchor="lm")

# titel en één regel
ft = font("Bricolage.ttf", 104, "Bold")
d.text((X, 230), "Clean cuts.", font=ft, fill=CREME)
d.text((X, 350), "Closed parts.", font=ft, fill=CREME)
fs = font("Bricolage.ttf", 44, "SemiBold")
d.text((X, 492), "The real mesh of a hip joint", font=fs, fill=GOUD)
d.text((X, 546), "from Figure from rig.", font=fs, fill=GOUD)

# drie feiten uit de add-on
fb = font("Inter.ttf", 34, "Regular")
dl = sum(1 for _ in m["open_randen"])
open_tot = sum(m["open_randen"].values())
feiten = [f"Ball {m['kogel_d_mm']:.1f} mm, swings ±{m['graden']:.0f}°",
          f"Clearance {m['speling_gemeten_mm']:.2f} mm, measured",
          f"{dl} parts, {open_tot} open edges"]
y = 668
for t in feiten:
    d.ellipse((X, y + 12, X + 16, y + 28), fill=GOUD)
    d.text((X + 36, y), t, font=fb, fill=CREME)
    y += 62

# voetregel: wat je ziet
fv = font("Inter.ttf", 22, "Regular")
d.text((X, 1010), "Render of the add-on's own output in Blender, wireframe on. Figure CC0.", font=fv, fill=GRIJS)


def pil(tekst, punt, kant, dx, maat=30, plek=None):
    """Label als pil met gouden rand, lijn naar het punt (zoals de labels op het hoofdbeeld)."""
    f = font("Inter.ttf", maat, "SemiBold")
    bw = d.textlength(tekst, font=f) + 40
    bh = 54
    px_, py_ = punt
    lx = px_ + dx if kant > 0 else px_ - dx - bw
    ly = py_ - bh / 2
    lx = min(lx, W - bw - 24)
    eind = lx if kant > 0 else lx + bw
    if plek:   # pil op een vaste plek (midden x,y), schuine lijn naar de onderrand
        lx, ly = plek[0] - bw / 2, plek[1] - bh / 2
        d.line((px_, py_, plek[0] - bw * 0.25, ly + bh), fill=GOUD, width=3)
        py_l = plek[1]
    else:
        d.line((px_, py_, eind, py_), fill=GOUD, width=3)
        py_l = py_
    d.ellipse((px_ - 9, py_ - 9, px_ + 9, py_ + 9), fill=GOUD, outline=(20, 12, 26), width=3)
    d.rounded_rectangle((lx, ly, lx + bw, ly + bh), radius=bh / 2, fill=(26, 16, 34, 235), outline=GOUD, width=3)
    d.text((lx + bw / 2, py_l), tekst, font=f, fill=CREME, anchor="mm")


kx, ky = (float(v) for v in os.environ.get("KT_KOGEL", "1600,330").split(","))
ox, oy = (float(v) for v in os.environ.get("KT_KOM", "1790,640").split(","))
pil(f"Ball {m['kogel_d_mm']:.1f} mm", (kx, ky), 1, float(os.environ.get("KT_KOGEL_DX", "60")))
plek = tuple(float(v) for v in os.environ["KT_KOM_PIL"].split(",")) if os.environ.get("KT_KOM_PIL") else None
pil(f"Socket, {m['speling_gemeten_mm']:.2f} mm gap", (ox, oy), 1, float(os.environ.get("KT_KOM_DX", "50")), plek=plek)

img.convert("RGB").save(UIT, quality=92)
print("klaar", UIT)
