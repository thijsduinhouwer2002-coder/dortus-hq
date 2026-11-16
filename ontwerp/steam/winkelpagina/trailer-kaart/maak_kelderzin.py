# Mila 16 nov: proefkaart trailer 3 tot 6 s, "Your taskbar has a basement now." op het echte bureaublad (scherm 2).
# Zelfde letter als de capsule (Lilita One), geel met donkere rand, linksboven. A zonder pijl, B met een pijl naar de strook.
# Gebruik: python3 maak_kelderzin.py  (vanuit deze map)
from PIL import Image, ImageDraw, ImageFont
import math
BRON = "../schermen-3d/scherm-2-bureaublad.png"
LETTER = "../../capsule-3d/LilitaOne-Regular.ttf"
GEEL, RAND = (255, 214, 64), (42, 18, 12)

def kaart(pijl):
    im = Image.open(BRON).convert("RGB"); d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype(LETTER, 104); f2 = ImageFont.truetype(LETTER, 132)
    x, y = 820, 110
    d.text((x, y), "Your taskbar has", font=f1, fill=GEEL, stroke_width=10, stroke_fill=RAND)
    d.text((x - 6, y + 112), "a basement now.", font=f2, fill=GEEL, stroke_width=12, stroke_fill=RAND)
    if pijl:   # gebogen pijl van "basement" omlaag naar de strook boven de taakbalk
        pts = [(1180 + 120 * math.sin(t / 40 * math.pi * 0.9), 400 + t * 8.2) for t in range(41)]
        for w, c in [(30, RAND), (16, GEEL)]:
            d.line(pts, fill=c, width=w, joint="curve")
        ex, ey = pts[-1]; a = math.atan2(pts[-1][1] - pts[-3][1], pts[-1][0] - pts[-3][0])
        kop = [(ex + 46 * math.cos(a), ey + 46 * math.sin(a)), (ex + 34 * math.cos(a + 2.3), ey + 34 * math.sin(a + 2.3)), (ex + 34 * math.cos(a - 2.3), ey + 34 * math.sin(a - 2.3))]
        d.polygon(kop, fill=GEEL, outline=RAND, width=7)
    return im

for naam, p in [("A", False), ("B", True)]:
    kaart(p).save(f"kelderzin-{naam}-1920.png")
a, b = Image.open("kelderzin-A-1920.png"), Image.open("kelderzin-B-1920.png")
blad = Image.new("RGB", (1210, 340), "white")
blad.paste(a.resize((600, 338), Image.LANCZOS), (0, 0)); blad.paste(b.resize((600, 338), Image.LANCZOS), (610, 0))
blad.save("vergelijk-kelderzin-A-B-600.png")
