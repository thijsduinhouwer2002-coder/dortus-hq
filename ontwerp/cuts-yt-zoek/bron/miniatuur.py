"""YouTube-miniatuur zoekvideo Click Cuts (#382 voor #332).
Bron: de Blender-render van het hoofdbeeld (ontwerp/cuts-hoofdbeeld/beelden/paard-render.jpg): het paard
(Poly Haven Horse Statue 01, CC0) heel in het gouden bouwvolume van 256 mm, en de 12 stukken die de echte knop
Split to fit van Click Cuts maakte (paard.json). Twee uitsneden uit die ene render, dichter bij elkaar gezet,
met een pijl en een grote kop. Geen AI-beeld, geen foto van een print.
    python3 miniatuur.py <paard-render.jpg> <uit.jpg> [variant]
variant a: kop "TOO BIG / TO PRINT?" plus "SPLIT IT IN BLENDER"; variant b: "SPLIT ANY / MODEL" plus "FOR 3D PRINTING".
variant c (r2, kan-punten Daan #391): als a, bouwvolume nagetrokken in goud 3 px, stukken 30 px van de randen, minder verscherpt.
Letters: Poppins ExtraBold (OFL 1.1, commercie/filmpjes/regisseur-31/fonts)."""
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HIER = __file__.rsplit("/", 1)[0]
FONT = HIER + "/../../../commercie/filmpjes/regisseur-31/fonts/Poppins-ExtraBold.ttf"
bron, uit = sys.argv[1], sys.argv[2]
variant = sys.argv[3] if len(sys.argv) > 3 else "a"
W, H = 1280, 720
GOUD = (255, 201, 74)

r = Image.open(bron).convert("RGB")
r = ImageEnhance.Brightness(r).enhance(1.35)
r = ImageEnhance.Contrast(r).enhance(1.12)
r = ImageEnhance.Color(r).enhance(1.15)

# achtergrond: verloop in de kleur van de render (donker paars)
bg = Image.new("RGB", (W, H))
dg = ImageDraw.Draw(bg)
for y in range(H):
    t = y / H
    dg.line([(0, y), (W, y)], fill=(int(22 + 14 * t), int(14 + 8 * t), int(34 + 20 * t)))
# zacht licht achter het model
gloed = Image.new("L", (W, H), 0)
ImageDraw.Draw(gloed).ellipse((560, 40, 1300, 760), fill=120)
gloed = gloed.filter(ImageFilter.GaussianBlur(140))
bg = Image.composite(Image.new("RGB", (W, H), (70, 48, 96)), bg, gloed)


def plak(vak, hoogte, x, y):
    stuk = r.crop(vak)
    s = hoogte / stuk.height
    stuk = stuk.resize((int(stuk.width * s), hoogte), Image.LANCZOS)
    m = Image.new("L", stuk.size, 255)
    rand = 40
    dm = ImageDraw.Draw(m)
    for i in range(rand):
        a = int(255 * i / rand)
        dm.rectangle((i, i, stuk.width - 1 - i, stuk.height - 1 - i), outline=a)
    # alleen waar de render lichter is dan de achtergrond telt hij echt mee: houdt de vlakken rustig
    grijs = stuk.convert("L").point(lambda v: max(0, min(255, (v - 36) * 9)))
    m = Image.fromarray(__import__("numpy").minimum(__import__("numpy").array(m), __import__("numpy").array(grijs)))
    m = m.filter(ImageFilter.GaussianBlur(2))
    bg.paste(stuk, (x, y), m)
    return stuk.size


# vakken in pixels van de render 2400x1350
heel = (1080, 300, 1530, 1000)   # paard in het gouden bouwvolume
delen = (1770, 120, 2330, 1010)  # de 12 stukken met pennen
wh = plak(heel, 440, 540, 250)
if variant == "c":
    wd = plak(delen, 590, 1280 - 48 - int(560 * 590 / 890), 50)
    rechts = 1280 - 48
else:
    wd = plak(delen, 620, 1280 - 18 - int(560 * 620 / 890), 60)
    rechts = 1280 - 18

d = ImageDraw.Draw(bg, "RGBA")
# pijl tussen heel en delen
ax0, ax1, ay = 540 + wh[0] - 6, rechts - wd[0] + 14, 470
if variant == "c":
    # het bouwvolume van 256 mm uit de render nagetrokken in goud, zodat "te groot" ook op 168x94 leest
    A, B, C, Dk = (551, 470), (736, 482), (809, 447), (636, 442)
    E, F, G, Hk = (554, 663), (737, 679), (810, 633), (636, 603)
    for p0, p1, w in [(Dk, Hk, 2), (A, Dk, 3), (Dk, C, 3), (A, B, 4), (B, C, 4), (A, E, 4), (B, F, 4),
                      (C, G, 4), (E, F, 4), (F, G, 4)]:
        d.line([p0, p1], fill=GOUD + (255,), width=w)
d.polygon([(ax0, ay - 16), (ax1 - 34, ay - 16), (ax1 - 34, ay - 38), (ax1, ay), (ax1 - 34, ay + 38),
           (ax1 - 34, ay + 16), (ax0, ay + 16)], fill=(255, 255, 255, 240))

f = lambda n: ImageFont.truetype(FONT, n)
if variant in ("a", "c"):
    regels = [("TOO BIG", 100, (255, 255, 255)), ("TO PRINT?", 100, GOUD)]
    onder = "SPLIT IT IN"
else:
    regels = [("SPLIT ANY", 100, (255, 255, 255)), ("MODEL", 100, GOUD)]
    onder = "FOR 3D PRINTING IN"
y = 70
for tekst, n, kleur in regels:
    d.text((44, y), tekst, font=f(n), fill=kleur, stroke_width=5, stroke_fill=(10, 8, 14))
    y += int(n * 1.05)
y += 16
d.text((48, y), onder, font=f(50), fill=(255, 255, 255), stroke_width=3, stroke_fill=(10, 8, 14))
y += 70
# pil "BLENDER": het woord dat de rechters groter wilden
fb = f(78)
bb = d.textbbox((0, 0), "BLENDER", font=fb)
pw, ph = bb[2] - bb[0] + 48, bb[3] - bb[1] + 34
d.rounded_rectangle((44, y, 44 + pw, y + ph), radius=18, fill=(234, 118, 0, 255))
d.text((44 + 24 - bb[0], y + 17 - bb[1]), "BLENDER", font=fb, fill=(255, 255, 255))
bg = bg.filter(ImageFilter.UnsharpMask(radius=2, percent=25 if variant == "c" else 50, threshold=2))
bg.save(uit, quality=93)
bg.resize((168, 94), Image.LANCZOS).save(uit.replace(".jpg", "-168.jpg"), quality=93)
print(uit, bg.size)
