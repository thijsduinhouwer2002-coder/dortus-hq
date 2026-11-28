"""Steam-header 920x430, ronde 13 (Mila, 28 nov 2026, #30, keuring Daan #351).
Zelfde lijn als v12a (GESLAAGD plek 1,5), met de drie moet-punten van Daan:
  M1  geen losse tekst: geen label, mailvenster met grijze balkjes zonder woorden, geen klok of datum
      (regels Steam: alleen spelbeeld, spelnaam en officiele ondertitel op een capsule).
  M2  titel met iets eigens: tweede kleur op "Fallen", dieptekant, en de hoge hoed uit het spelmodel
      (modellen/hoeden.py, nr 7, gerenderd in Blender) scheef op de H.
  M3  pixelkunst met hele factor NEAREST op een tekendoek van 4x (1,25x wordt 5x, 1,5x wordt 6x), pas het
      hele beeld gaat in een keer terug naar 920; en een uitsnede waar links iets gebeurt.
Gebruik: python3 header_v13.py <spelbeeld.png> <x0> <schaal> <hoed.png> <uit.png>
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

BRON, X0, SCH, HOED, UIT = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4], sys.argv[5]
S = 4
W, H = 920 * S, 430 * S
TB = 36 * S
F_P = "/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf"
fp = lambda w, s: ImageFont.truetype(F_P % w, s)
random.seed(3)
HIER = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
ICOON = HIER + "/../icoon/icoon-tegel-256.png"
u = lambda v: int(round(v * S))  # maat in 920-pixels naar het doek


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


k = int(round(SCH * S))  # hele factor op het doek
assert abs(k - SCH * S) < 1e-6, "schaal x 4 moet heel zijn"
GB = -(-W // k)
bron_img = Image.open(BRON).convert("RGB")
HB = bron_img.height  # 160 (v13) of 240 (v14, film op hoogte=240)
spel = bron_img.crop((X0, 0, X0 + GB, HB))
spel = spel.resize((GB * k, HB * k), Image.NEAREST).crop((0, 0, W, HB * k))
SH = HB * k
TOP = H - TB - SH

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
for y in range(TOP + u(10)):
    d.line((0, y, W, y), fill=mix((78, 146, 224), (192, 222, 247), y / (TOP + u(10))))
wl = Image.new("L", (W, H), 0); dw = ImageDraw.Draw(wl)
for (cx, cy) in [(u(560), TOP - u(18)), (u(380), u(30))]:
    for _ in range(7):
        r = random.uniform(u(18), u(35))
        x = cx + random.uniform(-u(80), u(80)); y = cy + random.uniform(-u(8), u(8))
        dw.ellipse((x - r * 1.7, y - r, x + r * 1.7, y + r * 0.7), fill=255)
img.paste((255, 255, 255), (0, 0), wl.filter(ImageFilter.GaussianBlur(u(8))).point(lambda v: int(v * 0.75)))

import os
if os.environ.get("HV_RAAM") == "groot":
    # v15: venster zoals v12a (GESLAAGD), groot en rechtsboven tot op het hol, maar zonder woorden (Daan #351 M1)
    vx0, vy0, vx1, vy1 = u(645), u(32), W - u(0), TOP
    sch = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sch).rectangle((vx0 + u(3), vy0 + u(6), vx1 + u(3), vy1), fill=110)
    img.paste((30, 40, 60), (0, 0), sch.filter(ImageFilter.GaussianBlur(u(9))))
    d.rectangle((vx0, vy0, vx1, vy1), fill=(250, 250, 252))
    d.rectangle((vx0, vy0, vx1, vy0 + u(30)), fill=(240, 242, 246))
    d.rounded_rectangle((vx0 + u(14), vy0 + u(11), vx0 + u(74), vy0 + u(19)), u(4), fill=(150, 156, 170))
    g = u(1.6); c = (60, 64, 76); my = vy0 + u(15)
    x = vx1 - u(26); d.line((x - u(6), my - u(6), x + u(6), my + u(6)), fill=c, width=g); d.line((x - u(6), my + u(6), x + u(6), my - u(6)), fill=c, width=g)
    x = vx1 - u(62); d.rectangle((x - u(6), my - u(6), x + u(6), my + u(6)), outline=c, width=g)
    x = vx1 - u(98); d.line((x - u(6), my, x + u(6), my), fill=c, width=g)
    for i in range(3):
        y = vy0 + u(46) + i * u(36)
        if y + u(22) > TOP: break
        d.ellipse((vx0 + u(16), y, vx0 + u(36), y + u(20)), fill=[(120, 160, 230), (240, 170, 90), (130, 200, 150)][i])
        d.rounded_rectangle((vx0 + u(46), y + u(2), vx0 + u(120), y + u(9)), u(3), fill=(60, 66, 82))
        d.rounded_rectangle((vx0 + u(46), y + u(13), vx0 + u(180), y + u(19)), u(3), fill=(184, 188, 200))
else:
    # mailvenster rechts, half over de rand (Daan kan-punt: kleiner), zonder woorden
    vx0, vy0, vx1, vy1 = u(712), u(40), W + u(30), TOP + u(20)
    sch = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sch).rounded_rectangle((vx0 + u(4), vy0 + u(8), vx1 + u(4), vy1 + u(8)), u(9), fill=110)
    img.paste((30, 40, 60), (0, 0), sch.filter(ImageFilter.GaussianBlur(u(10))))
    d.rounded_rectangle((vx0, vy0, vx1, vy1), u(8), fill=(250, 250, 252))
    d.rounded_rectangle((vx0, vy0, vx1, vy0 + u(30)), u(8), fill=(232, 235, 241))
    d.rectangle((vx0, vy0 + u(20), vx1, vy0 + u(30)), fill=(232, 235, 241))
    d.rounded_rectangle((vx0 + u(14), vy0 + u(11), vx0 + u(64), vy0 + u(19)), u(4), fill=(176, 182, 196))
    for i, c in enumerate([(226, 104, 90), (240, 196, 80), (100, 190, 130)]):
        cx = vx0 + u(118) + i * u(20); cy = vy0 + u(15)
        d.ellipse((cx - u(5), cy - u(5), cx + u(5), cy + u(5)), fill=c)
    d.line((vx0 + u(70), vy0 + u(30), vx0 + u(70), vy1), fill=(232, 235, 241), width=u(1))
    for i in range(4):
        y = vy0 + u(42) + i * u(22)
        if y + u(14) > TOP: break
        d.rounded_rectangle((vx0 + u(12), y, vx0 + u(58), y + u(7)), u(3), fill=(214, 218, 228))
    for i in range(3):
        y = vy0 + u(44) + i * u(34)
        if y + u(20) > TOP: break
        d.ellipse((vx0 + u(82), y, vx0 + u(98), y + u(16)), fill=[(120, 160, 230), (240, 170, 90), (130, 200, 150)][i])
        d.rounded_rectangle((vx0 + u(106), y + u(1), vx0 + u(170), y + u(7)), u(3), fill=(70, 76, 92))
        d.rounded_rectangle((vx0 + u(106), y + u(11), vx0 + u(196), y + u(16)), u(3), fill=(188, 192, 204))

# titel: twee kleuren, donkere rand en een dieptekant, hoge hoed op de H
gr = u(68) if TOP > u(185) else u(58)
f1 = fp("Bold", gr)
tx, ty = u(28), u(46) if TOP > u(185) else u(38)
delen = [("Hats of the ", (255, 246, 214)), ("Fallen", (255, 196, 72))]
laag = Image.new("L", (W, H), 0); dl = ImageDraw.Draw(laag)
x = tx
for t, _ in delen:
    dl.text((x, ty), t, font=f1, fill=255)
    x += dl.textlength(t, font=f1)
rand = laag.filter(ImageFilter.MaxFilter(2 * u(2.5) + 1))
diep = Image.new("L", (W, H), 0)
for s in range(1, u(4) + 1):
    diep.paste(255, (0, 0), rand.transform(rand.size, Image.AFFINE, (1, 0, -s * 0.4, 0, 1, -s)))
schaduw = rand.filter(ImageFilter.GaussianBlur(u(5))).point(lambda v: int(v * 0.35))
img.paste((20, 30, 60), (u(3), u(6)), schaduw)
img.paste((22, 16, 38), (0, 0), diep)
img.paste((46, 34, 70), (0, 0), rand)
d = ImageDraw.Draw(img)
x = tx
for t, c in delen:
    d.text((x, ty), t, font=f1, fill=c)
    # lichte bovenkant van elke letter: een tint lichter in de bovenste 40 procent
    x += d.textlength(t, font=f1)
glans = Image.new("L", (W, H), 0)
bb = laag.getbbox()
gm = Image.new("L", (W, H), 0); ImageDraw.Draw(gm).rectangle((0, 0, W, bb[1] + int((bb[3] - bb[1]) * 0.38)), fill=70)
glans.paste(gm, (0, 0), laag)
img.paste((255, 255, 255), (0, 0), glans)

hoed = Image.open(HOED).convert("RGBA")
hoed = hoed.crop(hoed.getbbox())
hb = int(gr * 0.95)
hoed = hoed.resize((hb, int(hoed.height * hb / hoed.width)), Image.LANCZOS).rotate(16, Image.BICUBIC, expand=True)
hx = tx - int(gr * 0.22); hy = bb[1] - int(hoed.height * 0.84)
hr = Image.new("L", hoed.size, 0); hr.paste(hoed.split()[3].filter(ImageFilter.MaxFilter(2 * u(2) + 1)))
img.paste((46, 34, 70), (hx, hy), hr)
img.paste(hoed, (hx, hy), hoed)

img.paste(spel, (0, TOP))
d = ImageDraw.Draw(img)
d.rectangle((0, H - TB, W, H), fill=(32, 36, 48))
kl = [(80, 140, 230), (240, 196, 80), (100, 190, 130), (226, 104, 90), (200, 202, 210)]
n = len(kl) + 1
bx = W // 2 - n * u(17)
for i, c in enumerate(kl):
    d.rounded_rectangle((bx + i * u(34), H - TB + u(7), bx + i * u(34) + u(22), H - TB + u(29)), u(5), fill=c)
gx = bx + len(kl) * u(34)
ico = Image.open(ICOON).convert("RGBA").resize((u(22), u(22)), Image.LANCZOS)
img.paste(ico, (gx, H - TB + u(7)), ico)
d = ImageDraw.Draw(img)
d.line((gx + u(6), H - u(2.5), gx + u(16), H - u(2.5)), fill=(200, 210, 230), width=u(1.5))
for i in range(3):  # systeemvak zonder tekst
    cx = W - u(30) - i * u(20)
    d.rounded_rectangle((cx - u(6), H - TB + u(13), cx + u(6), H - TB + u(23)), u(2), fill=(150, 156, 172))

img.resize((920, 430), Image.LANCZOS).save(UIT)
img.resize((460, 215), Image.LANCZOS).save(UIT.replace(".png", "-460.png"))
print(UIT, "strook", SH // S, "px, lucht", TOP // S, "px, uitsnede", X0, X0 + GB // 1)
