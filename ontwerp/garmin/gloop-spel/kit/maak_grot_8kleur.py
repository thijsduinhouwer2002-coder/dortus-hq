# Mila, 16 nov 2026: grot voor schermen met maar 8 kleuren (Forerunner 55, 208 px).
# Alleen zwart, rood en geel, met een dambord van 1 pixel om tussentinten te maken:
#   rood/zwart dambord = donker bruinrood (rand van de grot), vol rood = spotlicht achter Gloop,
#   geel/rood dambord = oranje (lichtbaan), vloer = zwart met elke 4e pixel rood.
# Zelfde vormen als maak_grot_donker.py en SpelView.mc. Op ware grootte (0,17 mm per pixel) mengt het dambord.
# Gebruik: python3 maak_grot_8kleur.py  -> 208-mip/grot-8kleur.png
import math, os
from PIL import Image, ImageDraw

HIER = os.path.dirname(os.path.abspath(__file__))
K, R, Y = (0, 0, 0), (255, 0, 0), (255, 255, 0)

def maak(w, h):
    cx, cy = w * 0.5, h * 0.78
    rmax = math.hypot(w * 0.62, h * 0.80)
    m = Image.new("L", (w, h), 0)
    d = int(w * 0.11)
    ax, ay = int(w * -0.03), int(h * -0.10)
    bx, by = int(w * 0.38), int(h * 0.74)
    ImageDraw.Draw(m).polygon([(ax - d, ay), (ax + d, ay), (bx + d, by), (bx - d, by)], fill=255)
    v = Image.new("L", (w, h), 0)
    ew, eh = int(w * 0.80), int(h * 0.16)
    ImageDraw.Draw(v).ellipse((w // 2 - ew, h - eh, w // 2 + ew, h + eh), fill=255)
    img = Image.new("RGB", (w, h)); px = img.load(); mp = m.load(); vp = v.load()
    for y in range(h):
        for x in range(w):
            dam = (x + y) % 2 == 0
            r = math.hypot(x - cx, (y - cy) * 1.05) / rmax
            if vp[x, y]:
                c = R if (x % 2 == 0 and y % 2 == 0) else K
            elif mp[x, y]:
                c = Y if dam else R
            elif r < 0.42:
                c = R
            elif r < 0.60:
                c = R if (x % 2 or y % 2) else K      # 3 op 4 rood
            else:
                c = R if dam else K
            px[x, y] = c
    assert len(img.getcolors()) <= 3
    return img

if __name__ == "__main__":
    out = os.path.join(HIER, "208-mip", "grot-8kleur.png")
    maak(208, 208).save(out, optimize=True)
    print(out, os.path.getsize(out))
