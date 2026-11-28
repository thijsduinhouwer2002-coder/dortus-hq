"""Steam-header 920x430 in de lijn van itch-omslag v5 (GESLAAGD plek 1,0, Sanne 28 nov 2026, #30).
Lucht van een bureaublad met een vlakke titel en het label "Lives above your taskbar", een mailvenster
rechts achter, het echte hol uit een eigen film van het spel eronder, taakbalk met het echte icoon.
Niets aan de figuren nagetekend: de strook is spelbeeld (NEAREST vergroot).
Gebruik: python3 header_bureau.py <spelbeeld.png> <x0> <schaal> <uit.png>
Bron v12: producten/steam-hol/itch/bron-scherm5-1305s.png (main e72baf9, 1305 s, zie de LEESMIJ daar).
"""
import sys, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BRON, X0, SCH, UIT = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
S = 2
W, H = 920 * S, 430 * S
TB = 36 * S
F_I = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
F_P = "/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf"
fi = lambda w, s: ImageFont.truetype(F_I % w, s)
fp = lambda w, s: ImageFont.truetype(F_P % w, s)
random.seed(3)
HIER = __file__.rsplit("/", 1)[0] if "/" in __file__ else "."
ICOON = HIER + "/../icoon/icoon-tegel-256.png"

def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

GB = int(round(920 / SCH))
spel = Image.open(BRON).convert("RGB").crop((X0, 0, X0 + GB, 160))
SW = int(round(GB * SCH * S)); SH = int(round(160 * SCH * S))
spel = spel.resize((GB * 4, 160 * 4), Image.NEAREST).resize((SW, SH), Image.LANCZOS).crop((0, 0, W, SH))
TOP = H - TB - SH

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
for y in range(TOP + 20):
    d.line((0, y, W, y), fill=mix((84, 150, 224), (190, 220, 246), y / (TOP + 20)))
wl = Image.new("L", (W, H), 0); dw = ImageDraw.Draw(wl)
for (cx, cy) in [(260, TOP - 30), (1500, 70)]:
    for k in range(7):
        r = random.uniform(36, 70)
        x = cx + random.uniform(-160, 160); y = cy + random.uniform(-16, 16)
        dw.ellipse((x - r * 1.7, y - r, x + r * 1.7, y + r * 0.7), fill=255)
img.paste((255, 255, 255), (0, 0), wl.filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.8)))

def venster(x0, y0, x1, y1, titel):
    sch = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sch).rounded_rectangle((x0 + 8, y0 + 16, x1 + 8, y1 + 16), 18, fill=110)
    img.paste((30, 40, 60), (0, 0), sch.filter(ImageFilter.GaussianBlur(20)))
    d.rounded_rectangle((x0, y0, x1, y1), 16, fill=(250, 250, 252))
    d.rounded_rectangle((x0, y0, x1, y0 + 64), 16, fill=(234, 236, 241))
    d.rectangle((x0, y0 + 44, x1, y0 + 64), fill=(234, 236, 241))
    d.text((x0 + 30, y0 + 18), titel, font=fi("Regular", 26), fill=(40, 44, 56))
    for i in range(3):
        cx = min(x1, W) - 50 - i * 64; cy = y0 + 32
        if i == 0:
            d.line((cx - 10, cy - 10, cx + 10, cy + 10), fill=(60, 60, 70), width=3)
            d.line((cx - 10, cy + 10, cx + 10, cy - 10), fill=(60, 60, 70), width=3)
        elif i == 1:
            d.rectangle((cx - 9, cy - 9, cx + 9, cy + 9), outline=(60, 60, 70), width=3)
        else:
            d.line((cx - 10, cy, cx + 10, cy), fill=(60, 60, 70), width=3)

# mailvenster rechts achter
vx = 1290
venster(vx, 64, W + 40, TOP + 40, "Inbox (3)")
mails = [("Team", "Notes from Monday"), ("Calendar", "Standup at 10:00")]
for i, (v, o) in enumerate(mails):
    y = 64 + 92 + i * 92
    if y + 70 > TOP: break
    d.text((vx + 40, y), v, font=fi("Medium", 28), fill=(30, 34, 46))
    d.text((vx + 40, y + 36), o, font=fi("Regular", 24), fill=(96, 100, 112))

# titel vlak in de lucht, grootte past zich aan de hoogte van de lucht aan
t1 = "Hats of the Fallen"
gr = 112 if TOP > 330 else 96
f1 = fp("Bold", gr)
ty = 22 if TOP > 330 else 14
tx = 56
for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 7), (-4, -4), (4, 4), (4, -4), (-4, 4), (0, 9)]:
    d.text((tx + dx, ty + dy), t1, font=f1, fill=(34, 28, 50))
d.text((tx, ty), t1, font=f1, fill=(255, 246, 214))
pill = "Lives above your taskbar"
f2 = fi("SemiBold", 34 if gr == 96 else 38)
pw = d.textlength(pill, font=f2)
py = ty + int(gr * 1.42)
ph = 56 if gr == 96 else 62
d.rounded_rectangle((tx + 4, py, tx + 4 + pw + 48, py + ph), ph // 2, fill=(34, 28, 50))
d.text((tx + 28, py + (ph - 42) // 2), pill, font=f2, fill=(255, 246, 214))

img.paste(spel, (0, TOP))
d.rectangle((0, H - TB, W, H), fill=(32, 36, 48))
kl = [(80, 140, 230), (240, 196, 80), (100, 190, 130), (226, 104, 90), (200, 202, 210)]
n = len(kl) + 1
bx = W // 2 - n * 34
for i, c in enumerate(kl):
    d.rounded_rectangle((bx + i * 68, H - TB + 14, bx + i * 68 + 44, H - TB + 58), 10, fill=c)
gx = bx + len(kl) * 68
ico = Image.open(ICOON).convert("RGBA").resize((44, 44), Image.LANCZOS)
img.paste(ico, (gx, H - TB + 14), ico)
d = ImageDraw.Draw(img)
d.line((gx + 12, H - 5, gx + 32, H - 5), fill=(200, 210, 230), width=3)
d.text((W - 150, H - TB + 8), "11:21 AM", font=fi("Regular", 22), fill=(230, 232, 240))
d.text((W - 150, H - TB + 38), "Sat 28 Nov", font=fi("Regular", 20), fill=(170, 176, 190))

img.resize((920, 430), Image.LANCZOS).save(UIT)
img.resize((460, 215), Image.LANCZOS).save(UIT.replace(".png", "-460.png"))
print(UIT, "strook", SH // S, "px, lucht", TOP // S, "px, uitsnede", X0, X0 + GB)
