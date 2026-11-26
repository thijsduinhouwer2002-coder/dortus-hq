"""Inzet van de knie op het hoofdbeeld met het mens-figuur (Beeldmaker, 26 nov 2026, issue #38).

python3 inzet.py <beeld-2400x1200.png> <knie-render.png> <hoofdbeeld.json> <uit.jpg> <fontmap>

Ronde 3 (Daan #156 M2): de knie-render is een aparte render van dezelfde scène met de camera precies langs de as van
het rechterkniescharnier (HB_KNIE_CAM, hoofdbeeld.py): pen en oog als rondje, onderbeen gebogen tot de stop van 120°,
alleen boven- en onderbeen in beeld. Een dun goud lijntje loopt van de inzet naar die knie in het hoofdbeeld (punt
uit hoofdbeeld.json, labels). Het bereik 0 tot 120° komt uit de json van de add-on.
Omgeving: IZ_X, IZ_Y, IZ_M (plek en maat in px op 2400x1200), IZ_SNEDE=cx,cy,maat (uitsnede als deel van de render),
IZ_KNIE (welk gewricht het lijntje raakt, standaard Right knee).
Ronde 4 (Daan #170 M2, keuze a): IZ_BOOG=<knie.json> tekent de gradenboog van de add-on zelf (Show bend range,
betaald/scharnier_boog.vorm, in rusthouding gerekend en door hoofdbeeld.py naar pixels van de kniecamera gezet) over de
inzet: wit van 0° (been recht) tot de stop, gouden lijn langs het onderbeen op de stop, getallen 0° en 120°.
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
x0, y0 = cx * kw - c / 2, cy * kh - c / 2
BOOG = os.environ.get("IZ_BOOG")   # ronde 4 (Daan #170 M2 a): knie.json met knie_boog, de gradenboog van de add-on
if BOOG:
    kb = json.load(open(BOOG, encoding="utf-8"))["knie_boog"]
    f4 = 4  # tekenen op 4x en dan verkleinen: gladde lijnen
    groot = k.resize((kw * f4, kh * f4), Image.LANCZOS)
    laag = Image.new("RGBA", groot.size, (0, 0, 0, 0))
    g = ImageDraw.Draw(laag)

    def P(q):
        return (q[0] * f4, q[1] * f4)
    lw = int(c / 1000 * 9 * f4)          # lijndikte in renderpixels, mee met de uitsnede
    WIT = (255, 255, 255, 255)
    # vlak tussen 0 en de grens, heel licht, zodat het bereik als taartpunt leest
    g.polygon([P(kb["centrum"])] + [P(q) for q in kb["boog"]], fill=(255, 255, 255, 46))
    g.line([P(q) for q in kb["boog"]], fill=WIT, width=lw, joint="curve")
    for gr, a1, a2 in kb["streepjes"]:
        if gr % 30 == 0:
            g.line([P(a1), P(a2)], fill=WIT, width=max(2, lw // 2))
    g.line([P(kb["centrum"]), P(kb["as_eind"])], fill=(255, 255, 255, 170), width=max(2, lw // 2))
    g.line([P(kb["centrum"]), P(kb["grens_eind"])], fill=GOUD + (255,), width=lw)
    gx, gy = P(kb["grens_eind"])
    rr = lw * 1.6
    g.ellipse((gx - rr, gy - rr, gx + rr, gy + rr), fill=GOUD + (255,), outline=DONKER + (255,), width=max(2, lw // 3))
    groot.alpha_composite(laag)
    k = groot.resize((kw, kh), Image.LANCZOS)
k = k.crop((int(x0), int(y0), int(x0 + c), int(y0 + c))).resize((M, M), Image.LANCZOS)

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
if BOOG:   # getallen bij de boog, zoals de add-on ze zet (label en label_0), in inzetpixels
    def I(q):
        return (X + (q[0] - x0) * M / c, Y + (q[1] - y0) * M / c)
    for q, t_, fg, maat in ((kb["label"], f"{kb['getal']}°", GOUD, 46), (kb["label_0"], "0°", CREME, 34)):
        fl = font("Inter.ttf", maat, "Bold")
        lx, ly = I(kb["as_eind"]) if t_ == "0°" else I(q)
        bb_ = d.textbbox((0, 0), t_, font=fl)
        tw, th = bb_[2] - bb_[0], bb_[3] - bb_[1]
        if t_ == "0°":   # naast het eind van de 0°-lijn, niet op de boog
            lx, ly = lx + tw / 2 + 26, ly - th / 2 - 4
        lx = min(max(lx, X + tw / 2 + 22), X + M - tw / 2 - 22)
        ly = min(max(ly, Y + th / 2 + 22), Y + M - th / 2 - 60)
        d.rounded_rectangle((lx - tw / 2 - 12, ly - th / 2 - 9, lx + tw / 2 + 12, ly + th / 2 + 9), radius=12, fill=DONKER + (225,))
        d.text((lx - tw / 2 - bb_[0], ly - th / 2 - bb_[1]), t_, font=fl, fill=fg)
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
