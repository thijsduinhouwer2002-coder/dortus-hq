# Mila, 16 nov 2026: donkere grot voor AMOLED als vast achtergrondplaatje per maat.
# Zelfde vormen als in SpelView.mc (lichtbaan van linksboven naar de bek, vloer-ellips),
# maar de grot is warm in het midden achter Gloop en bijna zwart aan de rand.
# Precies 16 kleuren (5 ringen, lichtbaan in 2 lagen over elke ring, vloer), zodat het plaatje klein blijft.
# Gebruik: python3 maak_grot_donker.py  -> <maat>/grot-donker.png
import math, os
from PIL import Image, ImageDraw

MATEN = {"320": (320, 360), "390": (390, 390), "416": (416, 416), "454": (454, 454)}
HIER = os.path.dirname(os.path.abspath(__file__))

# warm midden -> bijna zwart (kleur H, zoals de randen van het spelscherm en het icoon)
MIDDEN = (176, 90, 14)
RAND = (22, 10, 4)
TINTEN = [(176, 90, 14), (134, 64, 12), (96, 44, 10), (62, 28, 8), (34, 15, 5)]

def mix(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))

def maak(w, h):
    cx, cy = w * 0.5, h * 0.78          # licht achter Gloop
    rmax = math.hypot(w * 0.62, h * 0.80)
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            r = math.hypot(x - cx, (y - cy) * 1.05) / rmax
            t = min(1.0, max(0.0, (r - 0.12) / 0.78))
            # vijf harde ringen, als een spotlicht in een strip (bewust zichtbaar, geen verloop)
            k = min(4, int(t * 5))
            px[x, y] = TINTEN[k]
    grot = img.copy()

    # lichtbaan: zelfde maten als in het spel; als licht over de grot gelegd
    d = int(w * 0.11)
    ax, ay = int(w * -0.03), int(h * -0.10)
    bx, by = int(w * 0.38), int(h * 0.74)
    def baan(r):
        return [(ax - r, ay), (ax + r, ay), (bx + r, by), (bx - r, by)]
    for r, kracht in ((int(d * 1.18), 0.24), (d, 0.55)):
        m = Image.new("L", (w, h), 0)
        ImageDraw.Draw(m).polygon(baan(r), fill=255)
        licht = Image.new("RGB", (w, h), (255, 184, 96))
        img = Image.composite(Image.blend(grot, licht, kracht), img, m)
    # vloer: donkerrood, in het midden warmer
    m = Image.new("L", (w, h), 0)
    ew, eh = int(w * 0.80), int(h * 0.16)
    ImageDraw.Draw(m).ellipse((w // 2 - ew, h - eh, w // 2 + ew, h + eh), fill=255)
    vloer = Image.new("RGB", (w, h), (74, 10, 4))
    img = Image.composite(vloer, img, m)
    n = len(img.getcolors(1 << 16))
    assert n <= 16, n
    return img.quantize(colors=16, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)

if __name__ == "__main__":
    for naam, (w, h) in MATEN.items():
        out = os.path.join(HIER, naam, "grot-donker.png")
        maak(w, h).save(out, optimize=True)
        print(out, os.path.getsize(out))
