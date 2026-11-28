"""itch-omslag 630x500 als een hoek van een bureaublad (Sanne 28 nov 2026, #314).
Waarom: omslag v1 tot v3 (spelbeeld met 3D-logo) NIET GESLAAGD, de rechter zag "geen teken dat het een
pc-maatje is" en "cheap mobile-game". Echte bureaubladschermen halen wel plek 2. Dus hier: een werkvenster,
het echte hol eronder en een taakbalk, met een vlakke titel in plaats van het 3D-logo.
Het spelbeeld is een beeld uit een eigen film van het spel (hoogte=160); niets aan de figuren nagetekend.
Gebruik: python3 maak_omslag_bureau.py <spelbeeld.png> <x0> <notes|titel|bord> <uit.png>
v6 en v7 (28 nov, Daan #348 M1): bron op hoogte=240 uit main 46ca6e9 (na de fijne korrel ca6f928 en de knoppen
52507cc). Het hol staat dan op ware maat op de omslag (240 px hoog, 630 breed), niet meer 1,5x opgeschaald.
"bord" (v7, Daan K1): dezelfde titel met de gouden rand van het houten bord uit het spel.
"""
import sys, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BRON, X0, SOORT, UIT = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
S = 2                       # we tekenen op 2x en verkleinen aan het eind
W, H = 630 * S, 500 * S
TB = 40 * S                 # taakbalk
F_I = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
F_P = "/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf"
fi = lambda w, s: ImageFont.truetype(F_I % w, s)
fp = lambda w, s: ImageFont.truetype(F_P % w, s)
random.seed(3)
ICOON = __file__.rsplit("/", 1)[0] + "/../../../ontwerp/steam/icoon/icoon-tegel-256.png" if "/" in __file__ else "../../../ontwerp/steam/icoon/icoon-tegel-256.png"

def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

bron = Image.open(BRON).convert("RGB")
BH = bron.height                       # 160 (v1 tot v5) of 240 (v6 en later)
F = 240 / BH                           # op de omslag is het hol 240 px hoog
GB = round(630 / F)                    # 420 bij 160, 630 bij 240 (ware maat)
spel = bron.crop((X0, 0, X0 + GB, BH))
if BH == 240:
    spel = spel.resize((W, BH * S), Image.NEAREST)   # precies 2x, aan het eind weer /2: ware maat, geen zachte rand
else:
    spel = spel.resize((GB * 3, BH * 3), Image.NEAREST).resize((W, int(BH * 3 * W / (GB * 3))), Image.NEAREST)
SH = spel.height
TOP = H - TB - SH

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
for y in range(TOP + 20):
    d.line((0, y, W, y), fill=mix((84, 150, 224), (190, 220, 246), y / (TOP + 20)))
wl = Image.new("L", (W, H), 0); dw = ImageDraw.Draw(wl)
for (cx, cy) in [(220, 120), (1020, 300)]:
    for k in range(7):
        r = random.uniform(40, 80)
        x = cx + random.uniform(-150, 150); y = cy + random.uniform(-20, 20)
        dw.ellipse((x - r * 1.7, y - r, x + r * 1.7, y + r * 0.7), fill=255)
img.paste((255, 255, 255), (0, 0), wl.filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.8)))
hl = Image.new("L", (W, H), 0)
ImageDraw.Draw(hl).ellipse((-300, TOP - 90, W + 300, TOP + 400), fill=255)
img.paste((104, 172, 110), (0, 0), hl.filter(ImageFilter.GaussianBlur(2)))

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

if SOORT == "notes":
    x0, y0, x1 = 70, 56, 1190
    venster(x0, y0, x1, TOP + 40, "Notes.txt")
    tx = x0 + 52
    d.text((tx, y0 + 96), "Hats of the Fallen", font=fp("Bold", 84), fill=(36, 30, 52))
    d.text((tx + 4, y0 + 212), "A tiny dungeon above your taskbar.", font=fi("Medium", 38), fill=(92, 88, 110))
    for i, (klaar, t) in enumerate([(True, "answer emails"), (False, "check on Gloop")]):
        y = y0 + 290 + i * 56
        d.rounded_rectangle((tx + 4, y + 4, tx + 36, y + 36), 6, outline=(120, 124, 140), width=3)
        if klaar:
            d.line((tx + 11, y + 20, tx + 18, y + 28), fill=(70, 150, 90), width=5)
            d.line((tx + 18, y + 28, tx + 31, y + 11), fill=(70, 150, 90), width=5)
        d.text((tx + 54, y), t, font=fi("Regular", 34), fill=(120, 124, 140) if klaar else (40, 44, 56))
        if klaar:
            tw = d.textlength(t, font=fi("Regular", 34))
            d.line((tx + 54, y + 21, tx + 54 + tw, y + 21), fill=(120, 124, 140), width=3)
else:
    # klein mailvenster rechts achter, titel vlak in de lucht
    venster(700, 250, W + 40, TOP + 40, "Inbox (3)")
    for i, (v, o) in enumerate([("Team", "Notes from Monday")]):
        y = 340 + i * 84
        d.text((740, y), v, font=fi("Medium", 28), fill=(30, 34, 46))
        d.text((740, y + 36), o, font=fi("Regular", 24), fill=(96, 100, 112))
    t1 = "Hats of the Fallen"
    f1 = fp("Bold", 96)
    if SOORT == "bord":
        # gouden rand zoals het houten bord in het spel: donkere buitenlijn, gouden binnenlijn, room vlak
        for dx, dy in [(-7, 0), (7, 0), (0, -7), (0, 10), (-6, -6), (6, 6), (6, -6), (-6, 6), (0, 12), (-5, 10), (5, 10)]:
            d.text((60 + dx, 50 + dy), t1, font=f1, fill=(46, 30, 22))
        for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (-2, -2), (2, 2), (2, -2), (-2, 2)]:
            d.text((60 + dx, 50 + dy), t1, font=f1, fill=(232, 168, 52))
        lg = Image.new("L", (W, H), 0)
        ImageDraw.Draw(lg).text((60, 50), t1, font=f1, fill=255)
        verloop = Image.new("RGB", (W, H))
        dv = ImageDraw.Draw(verloop)
        for y in range(40, 190):
            dv.line((0, y, W, y), fill=mix((255, 248, 222), (250, 214, 130), (y - 40) / 150))
        img.paste(verloop, (0, 0), lg)
    else:
        for dx, dy in [(-5, 0), (5, 0), (0, -5), (0, 7), (-4, -4), (4, 4), (4, -4), (-4, 4), (0, 9)]:
            d.text((60 + dx, 50 + dy), t1, font=f1, fill=(34, 28, 50))
        d.text((60, 50), t1, font=f1, fill=(255, 246, 214))
    pill = "Lives above your taskbar"
    f2 = fi("SemiBold", 34)
    pw = d.textlength(pill, font=f2)
    d.rounded_rectangle((64, 196, 64 + pw + 48, 252), 28, fill=(34, 28, 50))
    d.text((88, 204), pill, font=f2, fill=(255, 246, 214))

img.paste(spel, (0, TOP))
d.rectangle((0, H - TB, W, H), fill=(32, 36, 48))
kl = [(80, 140, 230), (240, 196, 80), (100, 190, 130), (226, 104, 90), (200, 202, 210)]
n = len(kl) + 1
bx = W // 2 - n * 34
for i, c in enumerate(kl):
    d.rounded_rectangle((bx + i * 68, H - TB + 18, bx + i * 68 + 44, H - TB + 62), 10, fill=c)
# het echte icoon van het spel (ontwerp/steam/icoon) in de taakbalk
gx = bx + len(kl) * 68
ico = Image.open(ICOON).convert("RGBA").resize((44, 44), Image.LANCZOS)
img.paste(ico, (gx, H - TB + 18), ico)
d = ImageDraw.Draw(img)
d.line((gx + 12, H - 6, gx + 32, H - 6), fill=(200, 210, 230), width=3)
d.text((W - 150, H - TB + 14), "11:21 AM", font=fi("Regular", 22), fill=(230, 232, 240))
d.text((W - 150, H - TB + 44), "Sat 28 Nov", font=fi("Regular", 20), fill=(170, 176, 190))

img.resize((630, 500), Image.LANCZOS).save(UIT)
print(UIT, "spelhoogte", SH // S, "px op de omslag")
