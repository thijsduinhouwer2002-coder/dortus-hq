# Winkelicoon Ebb, 500x500 (Connect IQ: icoon en cover 500x500, hoogstens 300 KB).
# Stijl Mila (ontwerp/garmin/tij-stijl.md): zwart rond scherm als patrijspoort, turquoise water met schuimrand,
# alleen MIP-kleuren, geen verloop. Gijs, 10 nov 2026.
import math, sys
from PIL import Image, ImageDraw
N, S = 500, 4                      # tekenen op 4x en verkleinen voor zachte randen
W = N * S
img = Image.new("RGBA", (W, W), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
c, r = W / 2, W * 0.48
d.ellipse([c - r, c - r, c + r, c + r], fill=(0, 0, 0, 255))
water = Image.new("RGBA", (W, W), (0, 0, 0, 0))
dw = ImageDraw.Draw(water)
def golf(y0, amp, fase):
    return [(x, y0 + amp * math.sin(2 * math.pi * 1.6 * x / W + fase)) for x in range(0, W + 1, 4)]
lijn = golf(W * 0.50, W * 0.035, 0.6)
dw.polygon(lijn + [(W, W), (0, W)], fill=(0x00, 0xAA, 0xAA, 255))
dw.line(lijn, fill=(0x55, 0xFF, 0xFF, 255), width=int(W * 0.018))
for (bx, by, br) in [(0.36, 0.70, 0.030), (0.40, 0.80, 0.018), (0.62, 0.64, 0.022)]:
    dw.ellipse([bx * W - br * W, by * W - br * W, bx * W + br * W, by * W + br * W],
               outline=(0x55, 0xAA, 0xFF, 255), width=int(W * 0.008))
masker = Image.new("L", (W, W), 0)
ImageDraw.Draw(masker).ellipse([c - r, c - r, c + r, c + r], fill=255)
img.paste(water, (0, 0), Image.composite(water, Image.new("RGBA", (W, W)), masker).split()[3])
d = ImageDraw.Draw(img)
d.ellipse([c - r, c - r, c + r, c + r], outline=(0x55, 0xAA, 0xAA, 255), width=int(W * 0.012))
img = img.resize((N, N), Image.LANCZOS)
img.save(sys.argv[1], optimize=True)
