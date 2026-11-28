"""Tekst op de cover van het gratis testblok (Beeldmaker, 28 nov 2026, issue #423).

python3 tekst.py <render.png> <render.json> <uit.jpg> <fontmap> <icoon.svg> [variant]

Cover 1600x1200 (4:3). Printables toont ±3:2, dus alle tekst en het blok staan binnen y 66..1134.
Boven: badge, titel en één regel wat het doet; de spelingen en de pen komen uit render.json (de echte knop
Make fit test), niet verzonnen. Linksboven: merk Click Cuts, rechtsboven de badge. Lettertype Poppins (OFL 1.1).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON = sys.argv[1:6]
VARIANT = sys.argv[6] if len(sys.argv) > 6 else "a"
CREME, GOUD, ZACHT, BLAUW = (255, 246, 230), (255, 210, 92), (222, 212, 232), (120, 156, 255)
W, H = 1600, 1200
m = json.load(open(META))


def font(naam, maat):
    for d in (FONTS, "/usr/share/fonts/truetype/google-fonts"):
        p = os.path.join(d, naam)
        if os.path.exists(p):
            return ImageFont.truetype(p, maat)
    raise SystemExit(f"lettertype {naam} niet gevonden")


def icoon(maat):
    p = UIT + f"._icoon_{maat}.png"
    os.system(f"rsvg-convert -w {maat} '{ICOON}' -o '{p}'")
    im = Image.open(p).convert("RGBA")
    os.remove(p)
    return im


def schaduwtekst(img, xy, tekst, f, kleur, schaduw=10, anchor="la"):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).text(xy, tekst, font=f, fill=(0, 0, 0, 190), anchor=anchor)
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(schaduw)))
    ImageDraw.Draw(img).text(xy, tekst, font=f, fill=kleur, anchor=anchor)


img = Image.open(RENDER).convert("RGBA").resize((W, H), Image.LANCZOS)
# zachte donkere band boven, zodat de tekst leest
band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(band)
for y in range(520):
    bd.line([(0, y), (W, y)], fill=(16, 10, 22, int(150 * (1 - y / 520) ** 1.6)))
img.alpha_composite(band)

d = ImageDraw.Draw(img)
spel = m["spelingen_mm"]
pen = m["pen_d_mm"]
# badge
fb = font("Poppins-Bold.ttf", 34)
badge = "FREE  STL + 3MF"
bw = fb.getlength(badge) + 56
bx, by = W - 70 - bw, 92
d.rounded_rectangle((bx, by, bx + bw, by + 58), radius=29, fill=GOUD + (255,))
d.text((bx + bw / 2, by + 30), badge, font=fb, fill=(28, 18, 36), anchor="mm")
# titel
ft = font("Poppins-ExtraBold.ttf", 118)
y = 178
if VARIANT == "b":
    schaduwtekst(img, (W / 2, y), "Split Test Block", ft, CREME, anchor="ma")
else:
    t1, t2 = "Pin Fit ", "Test Block"
    tw = ft.getlength(t1 + t2)
    x = (W - tw) / 2
    schaduwtekst(img, (x, y), t1, ft, CREME)
    schaduwtekst(img, (x + ft.getlength(t1), y), t2, ft, GOUD)
# één regel wat het doet
fr = font("Poppins-Medium.ttf", 42)
r1 = f"Find the clearance for pins in split prints"
r2 = f"{pen:g} mm pin, 4 holes: " + "  ".join(f"{s:.2f}" for s in spel) + " mm"
schaduwtekst(img, (W / 2, 330), r1, fr, ZACHT, schaduw=8, anchor="ma")
schaduwtekst(img, (W / 2, 386), r2, font("Poppins-Bold.ttf", 42), GOUD, schaduw=8, anchor="ma")
# merk linksboven, op de hoogte van de badge
ic = icoon(58)
fm = font("Poppins-Bold.ttf", 38)
img.alpha_composite(ic, (70, 92))
ImageDraw.Draw(img).text((70 + 58 + 18, 92 + 29), "Click Cuts", font=fm, fill=CREME, anchor="lm")
fk = font("Poppins-Medium.ttf", 26)
ImageDraw.Draw(img).text((70 + 58 + 18, 92 + 29 + 34), "for Blender", font=fk, fill=ZACHT, anchor="lm")
img.convert("RGB").save(UIT, quality=92)
print("klaar", UIT)
