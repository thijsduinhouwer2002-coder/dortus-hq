"""itch-schermen 3 tot 5 in 16:9 (Sanne 28 nov 2026, #314, keuring Daan #324 M2 en K3).
Een hoek van een bureaublad, zoals op een scherm met schaal 200%: bovenin een stuk van een werkvenster
(per scherm een ander: spreadsheet, mail, browser), daaronder het echte spelbeeld en de taakbalk.
Het spelbeeld is een beeld uit een eigen film van het spel (hoogte=160, 1920 breed); we nemen er 960 px
van en verdubbelen elke pixel (NEAREST, geen Lanczos), dus scherp en zonder verzonnen rand.
Venster en taakbalk tekenen we direct op 2x, zodat de letters scherp zijn.
Gebruik: python3 maak_schermen.py <spelbeeld.png> <x0> <venster: blad|mail|web|notes> <uit.png>
28 nov (Daan #348 M2, M3, K2): bron nu op hoogte=240 (main 46ca6e9, fijne korrel). 960 x 240 uit de film, elke
pixel 2x, dus het spel is 480 hoog: een groot spelmoment. x0 = -1: de hele strook op ware maat (1920 x 240),
zoals hij op een scherm van 1920 x 1080 staat ("zo zit het op je scherm"). Het echte icoon staat altijd in de taakbalk.
"""
import sys, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BRON, X0, VENSTER, UIT = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
W, H, TB = 1920, 1080, 96
BRONBEELD = Image.open(BRON).convert("RGB")
BH = BRONBEELD.height
HEEL = X0 < 0
SH = BH if HEEL else BH * 2
if HEEL:
    TB = 48            # taakbalk op 100%, net als de strook
ICOON = __file__.rsplit("/", 1)[0] + "/../../../ontwerp/steam/icoon/icoon-tegel-256.png" if "/" in __file__ else "../../../ontwerp/steam/icoon/icoon-tegel-256.png"
F = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
f_r = lambda s: ImageFont.truetype(F % "Regular", s)
f_m = lambda s: ImageFont.truetype(F % "Medium", s)
random.seed(X0)

def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

img = Image.new("RGB", (W, H))
px = img.load()
TOP = H - TB - SH
for y in range(TOP):
    c = mix((92, 156, 226), (196, 222, 246), y / TOP)
    for x in range(W):
        px[x, y] = c
# twee zachte wolken
wl = Image.new("L", (W, H), 0); d = ImageDraw.Draw(wl)
for (cx, cy) in [(300 + X0 % 500, 120), (1500 - X0 % 400, 260)]:
    for k in range(8):
        r = random.uniform(50, 100)
        x = cx + random.uniform(-200, 200); y = cy + random.uniform(-30, 30)
        d.ellipse((x - r * 1.7, y - r, x + r * 1.7, y + r * 0.7), fill=255)
img.paste((255, 255, 255), (0, 0), wl.filter(ImageFilter.GaussianBlur(18)).point(lambda v: int(v * 0.8)))
# heuvel net boven het hol
hl = Image.new("L", (W, H), 0); dh = ImageDraw.Draw(hl)
pts = [(x, TOP - 60 - 40 * math.sin(x * 0.003 + X0) - 14 * math.sin(x * 0.009)) for x in range(0, W + 8, 8)]
dh.polygon(pts + [(W, TOP), (0, TOP)], fill=255)
img.paste((104, 172, 110), (0, 0), hl.filter(ImageFilter.GaussianBlur(2)))

# werkvenster: loopt van links of rechts buiten beeld, zoals bij een uitsnede van een groter scherm
d = ImageDraw.Draw(img)
links = VENSTER != "mail"
wx0, wx1 = (-40, 1500) if links else (420, W + 40)
wy0, wy1 = 70, TOP + 40   # onderkant valt achter het hol
sch = Image.new("L", (W, H), 0); ds = ImageDraw.Draw(sch)
ds.rounded_rectangle((wx0 + 10, wy0 + 18, wx1 + 10, wy1 + 18), 18, fill=120)
img.paste((30, 40, 60), (0, 0), sch.filter(ImageFilter.GaussianBlur(22)))
d.rounded_rectangle((wx0, wy0, wx1, wy1), 16, fill=(250, 250, 252))
d.rounded_rectangle((wx0, wy0, wx1, wy0 + 80), 16, fill=(234, 236, 241))
d.rectangle((wx0, wy0 + 60, wx1, wy0 + 80), fill=(234, 236, 241))
titel = {"blad": "Budget 2027.xlsx", "mail": "Inbox (3)", "web": "Recipes: easy pasta", "notes": "Notes.txt"}[VENSTER]
d.text((wx0 + 76 if links else wx0 + 36, wy0 + 24), titel, font=f_r(30), fill=(40, 44, 56))
bx = wx1 - 60 if wx1 < W else W - 60
for i, s in enumerate(["x", "o", "-"]):
    cx = bx - i * 80
    if s == "x":
        d.line((cx - 12, wy0 + 28, cx + 12, wy0 + 52), fill=(60, 60, 70), width=3); d.line((cx - 12, wy0 + 52, cx + 12, wy0 + 28), fill=(60, 60, 70), width=3)
    elif s == "o":
        d.rectangle((cx - 12, wy0 + 28, cx + 12, wy0 + 52), outline=(60, 60, 70), width=3)
    else:
        d.line((cx - 12, wy0 + 40, cx + 12, wy0 + 40), fill=(60, 60, 70), width=3)
cy0 = wy0 + 80
if VENSTER == "blad":
    kols = ["", "A", "B", "C", "D", "E", "F"]
    rijen = [["Month", "Rent", "Food", "Travel", "Fun", "Total"], ["Jan", "950", "310", "85", "60", "1405"], ["Feb", "950", "295", "120", "45", "1410"],
             ["Mar", "950", "330", "70", "90", "1440"], ["Apr", "950", "305", "", "", ""]]
    cw, rh = 230, 62
    for r in range(len(rijen) + 2):
        for c in range(len(kols)):
            x = wx0 + 40 + (90 if c > 0 else 0) + max(0, c - 1) * cw
            w = 90 if c == 0 else cw
            y = cy0 + r * rh
            kop = r == 0 or c == 0
            d.rectangle((x, y, x + w, y + rh), fill=(240, 242, 246) if kop else (255, 255, 255), outline=(214, 218, 226))
            t = kols[c] if r == 0 else (str(r) if c == 0 else (rijen[r - 1][c - 1] if r - 1 < len(rijen) else ""))
            if t:
                d.text((x + 16, y + 16), t, font=(f_m(28) if (r == 1 or kop) else f_r(28)), fill=(40, 44, 56))
    d.rectangle((wx0 + 130 + 4 * cw, cy0 + 5 * rh, wx0 + 130 + 5 * cw, cy0 + 6 * rh), outline=(38, 120, 70), width=4)
elif VENSTER == "mail":
    mails = [("Team", "Notes from Monday", "9:12"), ("Mum", "Sunday dinner?", "8:47"), ("Library", "Your book is due Friday", "Yesterday"),
             ("Anna", "Photos from the trip", "Yesterday")]
    for i, (van, onderwerp, t) in enumerate(mails):
        y = cy0 + 20 + i * 96
        if i < 2:
            d.ellipse((wx0 + 36, y + 30, wx0 + 50, y + 44), fill=(52, 120, 220))
        d.text((wx0 + 76, y + 10), van, font=f_m(30), fill=(30, 34, 46))
        d.text((wx0 + 76, y + 50), onderwerp, font=f_r(28), fill=(96, 100, 112))
        d.text((W - 220, y + 10), t, font=f_r(26), fill=(120, 124, 136))
        d.line((wx0 + 36, y + 94, W, y + 94), fill=(228, 230, 236), width=2)
elif VENSTER == "notes":
    d.text((wx0 + 120, cy0 + 60), "Monday", font=f_m(56), fill=(30, 34, 46))
    for i, (klaar, t) in enumerate([(True, "answer emails"), (True, "call the dentist"), (False, "finish the report"), (False, "check on Gloop")]):
        y = cy0 + 170 + i * 70
        d.rounded_rectangle((wx0 + 124, y + 4, wx0 + 162, y + 42), 7, outline=(120, 124, 140), width=3)
        if klaar:
            d.line((wx0 + 132, y + 24, wx0 + 141, y + 34), fill=(70, 150, 90), width=5)
            d.line((wx0 + 141, y + 34, wx0 + 156, y + 13), fill=(70, 150, 90), width=5)
        d.text((wx0 + 186, y), t, font=f_r(36), fill=(120, 124, 140) if klaar else (40, 44, 56))
else:
    d.rounded_rectangle((wx0 + 76, cy0 + 16, wx0 + 1100, cy0 + 72), 28, fill=(238, 240, 245))
    d.text((wx0 + 110, cy0 + 28), "recipes.example/easy-pasta", font=f_r(26), fill=(90, 94, 106))
    d.text((wx0 + 120, cy0 + 110), "Easy pasta in 20 minutes", font=f_m(48), fill=(30, 34, 46))
    for i, regel in enumerate(["1. Boil a big pot of salted water.", "2. Fry the garlic gently in olive oil.", "3. Add the tomatoes and let it simmer."]):
        d.text((wx0 + 120, cy0 + 200 + i * 54), regel, font=f_r(30), fill=(70, 74, 86))

# het echte spelbeeld: 960 x 160 uit de film, elke pixel 2x (NEAREST)
if HEEL:
    spel = BRONBEELD                                         # ware maat
else:
    spel = BRONBEELD.crop((X0, 0, X0 + 960, BH)).resize((1920, SH), Image.NEAREST)
img.paste(spel, (0, TOP))
# taakbalk (2x, of 1x bij de hele strook), altijd met het echte icoon van het spel
k = TB / 96
d.rectangle((0, H - TB, W, H), fill=(32, 36, 46))
iconen = [(70, 140, 230), (240, 196, 70), (100, 190, 120), (226, 100, 90), (200, 202, 210)]
stap, maat, boven = int(96 * k), int(52 * k), int(22 * k)
start = W // 2 - 3 * stap
for i, c in enumerate(iconen):
    x = start + i * stap
    d.rounded_rectangle((x, H - TB + boven, x + maat, H - TB + boven + maat), int(12 * k), fill=c)
gx = start + len(iconen) * stap
ico = Image.open(ICOON).convert("RGBA").resize((maat, maat), Image.LANCZOS)
img.paste(ico, (gx, H - TB + boven), ico)
d = ImageDraw.Draw(img)
d.line((gx + maat // 4, H - int(8 * k), gx + maat * 3 // 4, H - int(8 * k)), fill=(200, 210, 230), width=max(2, int(4 * k)))
d.text((W - int(190 * k), H - TB + int(14 * k)), "11:21 AM", font=f_r(int(26 * k)), fill=(230, 232, 238))
d.text((W - int(190 * k), H - TB + int(50 * k)), "Sat 28 Nov", font=f_r(int(24 * k)), fill=(190, 194, 204))
img.save(UIT, optimize=True)
print(UIT, img.size)
