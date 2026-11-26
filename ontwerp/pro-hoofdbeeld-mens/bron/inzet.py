"""Inzet van de knie op het hoofdbeeld met het mens-figuur (Beeldmaker, 26 nov 2026, issue #38).

python3 inzet.py <beeld-2400x1200.png> <knie-render.png> <uit.jpg> <fontmap> [x y maat]

Daan (#17) en ChatGPT (blinde test 26 nov) vroegen een uitsnede van een knie. De knie-render is dezelfde scène en
dezelfde camera als het hoofdbeeld, alleen een uitsnede rond de linkerknie op 300% (HB_RAND, HB_NAAM=knie): het
scharnier dat de echte knop Figure from rig maakte. Het bereik 0 tot 120° komt uit mens-uit.json.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BEELD, KNIE, UIT, FONTS = sys.argv[1:5]
X, Y, M = (int(v) for v in sys.argv[5:8]) if len(sys.argv) > 7 else (1150, 760, 340)
GOUD, CREME, DONKER = (255, 196, 84), (255, 246, 230), (24, 16, 30)


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


img = Image.open(BEELD).convert("RGBA")
k = Image.open(KNIE).convert("RGBA")
kw, kh = k.size
c = min(kw, kh) * 0.58   # vierkant rond het scharnier: onderkant bovenbeen boven, knokkel midden
cx, cy = kw * 0.455, kh * 0.40
k = k.crop((int(cx - c / 2), int(cy - c / 2), int(cx + c / 2), int(cy + c / 2))).resize((M, M), Image.LANCZOS)
masker = Image.new("L", (M, M), 0)
ImageDraw.Draw(masker).rounded_rectangle((0, 0, M - 1, M - 1), radius=28, fill=255)
schaduw = Image.new("RGBA", img.size, (0, 0, 0, 0))
ImageDraw.Draw(schaduw).rounded_rectangle((X, Y + 10, X + M, Y + M + 10), radius=28, fill=(0, 0, 0, 170))
img.alpha_composite(schaduw.filter(ImageFilter.GaussianBlur(16)))
img.paste(k, (X, Y), masker)
d = ImageDraw.Draw(img)
d.rounded_rectangle((X, Y, X + M, Y + M), radius=28, outline=GOUD + (255,), width=4)
f = font("Inter.ttf", 30, "SemiBold")
t = "Knee hinge, stops at 120°"
bb = d.textbbox((0, 0), t, font=f)
w, h = bb[2] - bb[0], bb[3] - bb[1]
bw, bh = w + 36, h + 26
bx, by = X + (M - bw) // 2, Y + M - bh // 2
d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=bh // 2, fill=DONKER + (240,), outline=GOUD + (255,), width=3)
d.text((bx + 18, by + 13 - bb[1]), t, font=f, fill=CREME)
img.convert("RGB").save(UIT, quality=93)
print("klaar", UIT)
