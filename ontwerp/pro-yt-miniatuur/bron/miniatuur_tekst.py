"""Tekst en inzet op de YouTube-miniatuur (issue #346, Beeldmaker). Pillow, Bricolage Grotesque Bold (OFL).

    python3 miniatuur_tekst.py <miniatuur-render.png> <kom-kogel-render.png> <uit.jpg> <Bricolage-Bold.ttf>
Variabelen: MT_KOGEL=x,y (hipkogel in de render, 0..1, voor de lijn naar de inzet), MT_INZET=x,y,r (midden en straal
van de uitsnede in kom-kogel-render, px), MT_PLEK=x,y,r (waar de inzet komt, 0..1 van breedte/hoogte, r als deel van
de hoogte), MT_WOORD1, MT_WOORD2, MT_PIL.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

render, kk, uit, font = sys.argv[1:5]
W, H = 2560, 1440
im = Image.open(render).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")
CREME, GOUD, DONKER = (255, 248, 234), (255, 185, 56), (24, 14, 34)

# links donkerder voor de tekst
schaduw = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(schaduw)
for x in range(W):
    t = max(0.0, 1 - x / (0.55 * W))
    d.line([(x, 0), (x, H)], fill=int(205 * t ** 1.4))
zwart = Image.new("RGBA", (W, H), (10, 4, 18, 255))
im = Image.composite(zwart, im, schaduw)

# inzet: echte kogel en kom (kom-kogel.py), rond, met gouden rand
kx, ky, kr = (int(v) for v in os.environ.get("MT_INZET", "490,470,235").split(","))
px, py, pr = (float(v) for v in os.environ.get("MT_PLEK", "0.835,0.30,0.235").split(","))
R = int(pr * H)
cx, cy = int(px * W), int(py * H)
bron = Image.open(kk).convert("RGBA")
achter = Image.new("RGBA", bron.size, (58, 28, 92, 255))
achter.alpha_composite(bron)
uitsnede = achter.crop((kx - kr, ky - kr, kx + kr, ky + kr)).resize((2 * R, 2 * R), Image.LANCZOS)
masker = Image.new("L", (2 * R, 2 * R), 0)
ImageDraw.Draw(masker).ellipse([0, 0, 2 * R - 1, 2 * R - 1], fill=255)
# lijn van de inzet naar de kogel in het figuur
gx, gy = (float(v) for v in os.environ.get("MT_KOGEL", "0.66,0.80").split(","))
lijn = ImageDraw.Draw(im)
import math
hoek = math.atan2(gy * H - cy, gx * W - cx)
lijn.line([(cx + R * math.cos(hoek), cy + R * math.sin(hoek)), (gx * W, gy * H)], fill=GOUD + (255,), width=8)
lijn.ellipse([gx * W - 18, gy * H - 18, gx * W + 18, gy * H + 18], outline=GOUD + (255,), width=8)
# schaduw onder de inzet
sl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sl).ellipse([cx - R - 10, cy - R + 20, cx + R + 10, cy + R + 40], fill=(0, 0, 0, 170))
im.alpha_composite(sl.filter(ImageFilter.GaussianBlur(30)))
im.paste(uitsnede, (cx - R, cy - R), masker)
ImageDraw.Draw(im).ellipse([cx - R - 6, cy - R - 6, cx + R + 6, cy + R + 6], outline=GOUD + (255,), width=16)

# woorden
d = ImageDraw.Draw(im)
w1 = os.environ.get("MT_WOORD1", "BALL")
w2 = os.environ.get("MT_WOORD2", "JOINTS")
pil = os.environ.get("MT_PIL", "1-CLICK")
X = 112
breed = int(0.43 * W)
maat = 400
while ImageFont.truetype(font, maat).getbbox(w2)[2] > breed:
    maat -= 4
f = ImageFont.truetype(font, maat)
asc = f.getbbox("J")[1]
hoogte = f.getbbox("J")[3] - asc
y1 = int(os.environ.get("MT_Y", "250"))
for i, w in enumerate((w1, w2)):
    y = y1 + i * int(hoogte * 1.16) - asc
    for dx, dy in ((0, 10), (0, 6)):
        d.text((X + dx, y + dy), w, font=f, fill=(0, 0, 0, 160))
    d.text((X, y), w, font=f, fill=CREME + (255,))
# gouden pil
fp = ImageFont.truetype(font, int(maat * 0.52))
bb = fp.getbbox(pil)
pw, ph = bb[2] - bb[0], fp.getbbox("C")[3] - fp.getbbox("C")[1]
py0 = y1 + 2 * int(hoogte * 1.16) + 30
pad_x, pad_y = 44, 34
d.rounded_rectangle([X, py0, X + pw + 2 * pad_x, py0 + ph + 2 * pad_y], radius=34, fill=GOUD + (255,))
d.text((X + pad_x - bb[0], py0 + pad_y - fp.getbbox("C")[1]), pil, font=fp, fill=DONKER + (255,))

# r2 (Gemini in beide rondes van de kop-aan-kop-test: "show the addon interface"): het echte paneel uit Blender 5.3.0
# (schermbeeld paneel-rig-scherm-voor.jpg), uitsnede met de knop Figure from rig, gouden rand om de knop
if os.environ.get("MT_PANEEL"):
    pad, *bx = os.environ["MT_PANEEL"].split(",")
    x0, y0, x1, y1 = (int(v) for v in bx)
    pn = Image.open(pad).convert("RGBA").crop((x0, y0, x1, y1))
    breedte = int(os.environ.get("MT_PANEEL_B", "860"))
    k = breedte / pn.width
    pn = pn.resize((breedte, int(pn.height * k)), Image.LANCZOS)
    top = py0 + ph + 2 * pad_y + 46
    sl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sl).rounded_rectangle([X - 6, top + 14, X + pn.width + 6, top + pn.height + 30], radius=24, fill=(0, 0, 0, 200))
    im.alpha_composite(sl.filter(ImageFilter.GaussianBlur(22)))
    m = Image.new("L", pn.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, pn.width - 1, pn.height - 1], radius=20, fill=255)
    im.paste(pn, (X, top), m)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([X, top, X + pn.width - 1, top + pn.height - 1], radius=20, outline=(90, 80, 110, 255), width=3)
    if os.environ.get("MT_KNOP"):
        bx0, by0, bx1, by1 = (int(v) for v in os.environ["MT_KNOP"].split(","))
        r = [X + (bx0 - x0) * k, top + (by0 - y0) * k, X + (bx1 - x0) * k, top + (by1 - y0) * k]
        d.rounded_rectangle([r[0] - 8, r[1] - 8, r[2] + 8, r[3] + 8], radius=16, outline=GOUD + (255,), width=10)
        # muispijl (eenvoudige pijl, eigen tekening) rechtsonder op de knop
        ax, ay = r[0] + (r[2] - r[0]) * 0.86, r[1] + (r[3] - r[1]) * 0.40
        s_ = 2.2
        pijl = [(0, 0), (0, 40), (10, 31), (17, 47), (24, 44), (17, 29), (30, 29)]
        pts = [(ax + x * s_, ay + y * s_) for x, y in pijl]
        d.polygon(pts, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=4)

out = im.convert("RGB").resize((1280, 720), Image.LANCZOS)
out.save(uit, quality=92)
out.resize((320, 180), Image.LANCZOS).save(uit.replace(".jpg", "-320.jpg"), quality=92)
print("klaar", uit, "lettermaat", maat)
