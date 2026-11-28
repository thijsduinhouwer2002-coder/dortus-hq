"""Tekst, gradenboog en paneel op de YouTube-miniatuur van de scharniervideo (issue #352, Beeldmaker).
Pillow, Bricolage Grotesque Bold (OFL). Stijl gelijk aan de geslaagde miniatuur yt-pro-r2 (#346).

    python3 scharnier_tekst.py <knie-render.png (vierkant)> <paneel-schermbeeld.jpg> <uit.jpg> <Bricolage-Bold.ttf>
Variabelen:
  ST_KNIE=x,y      draaipunt van de knie in de render (0..1), op het oog (GOK)
  ST_SCHEEN=graden richting van de scheen op de stop in beeldgraden (0 = rechts, 90 = omlaag), op het oog (GOK)
  ST_GRADEN=115    getal van de add-on (cj_bereik_graden, knie.json)
  ST_STRAAL=0.2    straal van de boog als deel van de hoogte
  ST_PANEEL=x0,y0,x1,y1  uitsnede uit het schermbeeld (rij 'Or a hinge that bends up to:' met 90°, 115°, 135°)
  ST_KNOP=x0,y0,x1,y1    de knop 115° in het schermbeeld (gouden rand)
"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

render, paneel, uit, font = sys.argv[1:5]
W, H = 2560, 1440
CREME, GOUD, DONKER = (255, 248, 234), (255, 185, 56), (24, 14, 34)

# achtergrond: de render vierkant rechts, links overvloeien naar de donkere studio
r = Image.open(render).convert("RGBA").resize((H, H), Image.LANCZOS)
X0 = W - H + int(os.environ.get("ST_SCHUIF", "0"))
im = Image.new("RGBA", (W, H), (10, 4, 18, 255))
im.alpha_composite(r, (X0, 0))
schaduw = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(schaduw)
for x in range(W):
    t = 1.0 if x < X0 else max(0.0, 1 - (x - X0) / 520)
    t2 = max(0.0, 1 - x / (0.56 * W))
    d.line([(x, 0), (x, H)], fill=int(255 * max(t ** 1.3, t2 ** 1.4 * 0.8)))
im = Image.composite(Image.new("RGBA", (W, H), (10, 4, 18, 255)), im, schaduw)

# gradenboog op de knie: 0° langs de dij omlaag, tot de stop van de add-on langs de scheen
kx, ky = (float(v) for v in os.environ.get("ST_KNIE", "0.43,0.55").split(","))
cx, cy = X0 + kx * H, ky * H
g = float(os.environ.get("ST_GRADEN", "115"))
eind = float(os.environ.get("ST_SCHEEN", str(90 - g)))
R = float(os.environ.get("ST_STRAAL", "0.2")) * H
laag = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ld = ImageDraw.Draw(laag)
# vlak van de boog, licht goud
ld.pieslice([cx - R, cy - R, cx + R, cy + R], start=eind, end=90, fill=GOUD + (60,))
ld.arc([cx - R, cy - R, cx + R, cy + R], start=eind, end=90, fill=GOUD + (255,), width=14)
for i in range(0, int(g) + 1, 15):   # streepjes elke 15 graden
    a = math.radians(90 - i * (90 - eind) / g)
    ld.line([(cx + (R - 30) * math.cos(a), cy + (R - 30) * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))],
            fill=GOUD + (255,), width=6)
for a_ in (90, eind):   # benen van de hoek
    a = math.radians(a_)
    ld.line([(cx, cy), (cx + (R + 40) * math.cos(a), cy + (R + 40) * math.sin(a))], fill=GOUD + (255,), width=8)
ld.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=GOUD + (255,))
im.alpha_composite(laag)
d = ImageDraw.Draw(im)
fl = ImageFont.truetype(font, 76)
def kaart(tekst, x, y, f, vul, inkt):
    bb = f.getbbox(tekst)
    w, h = bb[2] - bb[0], f.getbbox("0")[3] - f.getbbox("0")[1]
    d.rounded_rectangle([x - w / 2 - 26, y - h / 2 - 20, x + w / 2 + 26, y + h / 2 + 20], radius=26, fill=vul)
    d.text((x - w / 2 - bb[0], y - h / 2 - f.getbbox("0")[1]), tekst, font=f, fill=inkt)
a = math.radians(eind)
kaart(f"{int(g)}°", cx + (R + 130) * math.cos(a), cy + (R + 130) * math.sin(a), ImageFont.truetype(font, 104), GOUD + (255,), DONKER + (255,))
kaart("0°", cx, cy + R + 100, fl, (24, 14, 34, 230), CREME + (255,))

# woorden links
X = 112
w1 = os.environ.get("ST_WOORD", "HINGES")
pil = os.environ.get("ST_PIL", "STOP AT 115°")
breed = int(0.40 * W)
maat = 440
while ImageFont.truetype(font, maat).getbbox(w1)[2] > breed:
    maat -= 4
f = ImageFont.truetype(font, maat)
asc = f.getbbox("H")[1]
hoogte = f.getbbox("H")[3] - asc
y1 = int(os.environ.get("ST_Y", "190"))
for dx, dy in ((0, 10), (0, 6)):
    d.text((X + dx, y1 - asc + dy), w1, font=f, fill=(0, 0, 0, 160))
d.text((X, y1 - asc), w1, font=f, fill=CREME + (255,))
fp = ImageFont.truetype(font, int(os.environ.get("ST_PILMAAT", "150")))
bb = fp.getbbox(pil)
pw, ph = bb[2] - bb[0], fp.getbbox("S")[3] - fp.getbbox("S")[1]
py0 = y1 + hoogte + 60
pad_x, pad_y = 44, 34
d.rounded_rectangle([X, py0, X + pw + 2 * pad_x, py0 + ph + 2 * pad_y], radius=34, fill=GOUD + (255,))
d.text((X + pad_x - bb[0], py0 + pad_y - fp.getbbox("S")[1]), pil, font=fp, fill=DONKER + (255,))

# het echte paneel van Pro 1.2.9 (Blender 5.3.0): kop 'Click Joints' en de rij met 90°, 115°, 135°
if os.environ.get("ST_PANEEL"):
    x0, y0, x1, y1_ = (int(v) for v in os.environ["ST_PANEEL"].split(","))
    bron = Image.open(paneel).convert("RGBA")
    kop = bron.crop((x0, int(os.environ.get("ST_KOP_Y", "112")), x1, int(os.environ.get("ST_KOP_Y2", "165"))))
    rij = bron.crop((x0, y0, x1, y1_))
    pn = Image.new("RGBA", (x1 - x0, kop.height + rij.height), (40, 40, 40, 255))
    pn.paste(kop, (0, 0)); pn.paste(rij, (0, kop.height))
    breedte = int(os.environ.get("ST_PANEEL_B", "900"))
    k = breedte / pn.width
    pn = pn.resize((breedte, int(pn.height * k)), Image.LANCZOS)
    top = py0 + ph + 2 * pad_y + 70
    sl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sl).rounded_rectangle([X - 6, top + 14, X + pn.width + 6, top + pn.height + 30], radius=24, fill=(0, 0, 0, 200))
    im.alpha_composite(sl.filter(ImageFilter.GaussianBlur(22)))
    m = Image.new("L", pn.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, pn.width - 1, pn.height - 1], radius=20, fill=255)
    im.paste(pn, (X, top), m)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([X, top, X + pn.width - 1, top + pn.height - 1], radius=20, outline=(90, 80, 110, 255), width=3)
    if os.environ.get("ST_KNOP"):
        bx0, by0, bx1, by1 = (int(v) for v in os.environ["ST_KNOP"].split(","))
        oy = top + kop.height * k
        q = [X + (bx0 - x0) * k, oy + (by0 - y0) * k, X + (bx1 - x0) * k, oy + (by1 - y0) * k]
        d.rounded_rectangle([q[0] - 8, q[1] - 8, q[2] + 8, q[3] + 8], radius=16, outline=GOUD + (255,), width=10)
        ax, ay = q[0] + (q[2] - q[0]) * 0.80, q[1] + (q[3] - q[1]) * 0.45   # muispijl, eigen tekening
        s_ = 2.2
        pijl = [(0, 0), (0, 40), (10, 31), (17, 47), (24, 44), (17, 29), (30, 29)]
        d.polygon([(ax + x * s_, ay + y * s_) for x, y in pijl], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=4)

out = im.convert("RGB").resize((1280, 720), Image.LANCZOS)
out.save(uit, quality=92)
out.resize((320, 180), Image.LANCZOS).save(uit.replace(".jpg", "-320.jpg"), quality=92)
print("klaar", uit, "lettermaat", maat)
