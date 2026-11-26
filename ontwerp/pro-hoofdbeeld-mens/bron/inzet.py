"""Inzet van de knie op het hoofdbeeld met het mens-figuur (Beeldmaker, 26 nov 2026, issue #38).

python3 inzet.py <beeld-2400x1200.png> <knie-render.png> <hoofdbeeld.json> <uit.jpg> <fontmap>

Ronde 3 (Daan #156 M2): de knie-render is een aparte render van dezelfde scène met de camera precies langs de as van
het rechterkniescharnier (HB_KNIE_CAM, hoofdbeeld.py): pen en oog als rondje, onderbeen gebogen tot de stop van 120°,
alleen boven- en onderbeen in beeld. Een dun goud lijntje loopt van de inzet naar die knie in het hoofdbeeld (punt
uit hoofdbeeld.json, labels). Het bereik 0 tot 120° komt uit de json van de add-on.
Omgeving: IZ_X, IZ_Y, IZ_M (plek en maat in px op 2400x1200), IZ_SNEDE=cx,cy,maat (uitsnede als deel van de render),
IZ_KNIE (welk gewricht het lijntje raakt, standaard Right knee).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BEELD, KNIE, META, UIT, FONTS = sys.argv[1:6]
X, Y, M = int(os.environ.get("IZ_X", "1060")), int(os.environ.get("IZ_Y", "700")), int(os.environ.get("IZ_M", "400"))
GOUD, CREME, DONKER = (255, 196, 84), (255, 246, 230), (24, 16, 30)


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


img = Image.open(BEELD).convert("RGBA")
W, H = img.size
meta = json.load(open(META, encoding="utf-8"))
q = meta["labels"][os.environ.get("IZ_KNIE", "Right knee")]
kx, ky = q["x"] * 2400 * W / 2400, q["y"] * 1350 - 75   # zelfde omrekening als tekst.py (render 2400x1350, rand 75)

k = Image.open(KNIE).convert("RGBA")
kw, kh = k.size
cx, cy, c = (float(v) for v in os.environ.get("IZ_SNEDE", "0.5,0.5,1.0").split(","))
c *= min(kw, kh)
k = k.crop((int(cx * kw - c / 2), int(cy * kh - c / 2), int(cx * kw + c / 2), int(cy * kh + c / 2))).resize((M, M), Image.LANCZOS)

d = ImageDraw.Draw(img)
# lijntje van de rechterbovenhoek van de inzet naar de knie, met een stip op de knie
sx, sy = X + M - 40, Y + 40
d.line((sx, sy, kx, ky), fill=GOUD + (255,), width=4)
r = 11
d.ellipse((kx - r, ky - r, kx + r, ky + r), fill=GOUD + (255,), outline=DONKER + (255,), width=3)

masker = Image.new("L", (M, M), 0)
ImageDraw.Draw(masker).rounded_rectangle((0, 0, M - 1, M - 1), radius=30, fill=255)
schaduw = Image.new("RGBA", img.size, (0, 0, 0, 0))
ImageDraw.Draw(schaduw).rounded_rectangle((X, Y + 12, X + M, Y + M + 12), radius=30, fill=(0, 0, 0, 180))
img.alpha_composite(schaduw.filter(ImageFilter.GaussianBlur(18)))
img.paste(k, (X, Y), masker)
d = ImageDraw.Draw(img)
d.rounded_rectangle((X, Y, X + M, Y + M), radius=30, outline=GOUD + (255,), width=4)
f = font("Inter.ttf", 31, "SemiBold")
t = os.environ.get("IZ_TEKST", "Knee hinge, stops at 120°")
bb = d.textbbox((0, 0), t, font=f)
w, h = bb[2] - bb[0], bb[3] - bb[1]
bw, bh = w + 36, h + 26
bx, by = X + (M - bw) // 2, Y + M - bh // 2
d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=bh // 2, fill=DONKER + (240,), outline=GOUD + (255,), width=3)
d.text((bx + 18, by + 13 - bb[1]), t, font=f, fill=CREME)
img.convert("RGB").save(UIT, quality=93)
print("klaar", UIT, "knie op", round(kx), round(ky))
