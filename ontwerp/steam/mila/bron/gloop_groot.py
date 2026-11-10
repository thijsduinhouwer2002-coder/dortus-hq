# Mila 10 nov: Big Gloop, getekend en niet geschaald. Elk frame van slijm.png en slijm_leven.png krijgt een lijf dat
# 1 spelpixel breder is aan elke kant en 1 hoger (de oude omtreklijn wordt slijm, eromheen een nieuwe donkere lijn).
# Oog, tand en mond blijven precies waar ze waren, dus alle animaties werken gelijk. Zelfde bladindeling (16 x 16 per frame).
# Uit: kunst/slijm_groot.png en kunst/slijm_leven_groot.png. Bovenkant per frame is 1 hoger: RUST_TOP en LEVEN_TOP min 1.
import os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
K = os.path.abspath(os.path.join(H, "..", "..", "..", "..", "producten", "steam-hol", "godot", "kunst"))
D = (28, 18, 22, 255)
LICHT = {(87, 196, 156, 255), (166, 240, 204, 255), (230, 255, 244, 255)}
def groot(bron):
    b = bron.convert("RGBA"); w, h = b.size; u = b.copy()
    vol = lambda x, y: 0 <= x < w and 0 <= y < h and b.getpixel((x, y))[3] > 0
    for cx in range(0, w, 16):
        for y in range(16):
            for x in range(cx, cx + 16):
                if vol(x, y):
                    rand = any(not vol(x + dx, y + dy) or not (cx <= x + dx < cx + 16) for dx, dy in ((1, 0), (-1, 0), (0, -1)))
                    if rand and y < 15 and b.getpixel((x, y))[:3] in (D[:3], (42, 26, 31)):
                        # oude rand wordt slijm: kleur van de buur naar binnen (niet donker), anders het donkere groen
                        kl = None
                        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1)):
                            if vol(x + dx, y + dy) and cx <= x + dx < cx + 16:
                                c = b.getpixel((x + dx, y + dy))
                                if c[:3] not in (D[:3], (42, 26, 31)): kl = c; break
                        u.putpixel((x, y), kl or (47, 143, 122, 255))
                else:
                    if any(vol(x + dx, y + dy) and cx <= x + dx < cx + 16 for dx, dy in ((1, 0), (-1, 0), (0, 1))):
                        if cx <= x < cx + 16: u.putpixel((x, y), D)
    return u
for n in ("slijm", "slijm_leven"):
    groot(Image.open(os.path.join(K, n + ".png"))).save(os.path.join(K, n + "_groot.png"))
