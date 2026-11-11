# Meet op een simulatorbeeld: het ronde scherm (zwart vlak) en of de tekst in het midden en binnen 80% van de diameter staat.
import sys
from PIL import Image
from collections import deque
MAAT = {'fenix7': 260, 'fr255': 260, 'vivoactive5': 390, 'fr265': 416, 'venu2': 416, 'venu3': 454, 'fenix847mm': 454, 'epix2pro47mm': 416, 'fr965': 454}
def meet(pad):
    im = Image.open(pad).convert('RGB'); W, H = im.size; px = im.load()
    zwart = lambda x, y: max(px[x, y]) < 4
    # start: zwarte pixel het dichtst bij het midden van het beeld (scherm ligt rond het midden)
    cx0, cy0 = W // 2, H // 2
    start = None
    for r in range(0, min(W, H) // 2):
        for (x, y) in ((cx0 + r, cy0), (cx0 - r, cy0), (cx0, cy0 + r), (cx0, cy0 - r)):
            if 0 <= x < W and 0 <= y < H and zwart(x, y):
                start = (x, y); break
        if start: break
    # zwart vlak vullen, met tekst als gaten: neem bbox van het gevulde vlak
    gezien = bytearray(W * H); q = deque([start]); gezien[start[1] * W + start[0]] = 1
    x0 = x1 = start[0]; y0 = y1 = start[1]
    while q:
        x, y = q.popleft()
        x0, x1, y0, y1 = min(x0, x), max(x1, x), min(y0, y), max(y1, y)
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < W and 0 <= ny < H and not gezien[ny * W + nx] and zwart(nx, ny):
                gezien[ny * W + nx] = 1; q.append((nx, ny))
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2; R = (x1 - x0) / 2
    import os
    naam = os.path.basename(pad).split('-')[0]
    if naam in MAAT: R = MAAT[naam] / 2
    # getekende pixels: niet zwart, binnen de cirkel van het scherm (R - 2)
    tx0 = ty0 = 10 ** 9; tx1 = ty1 = -1; uiterst = 0.0
    for y in range(int(cy - R), int(cy + R) + 1):
        for x in range(int(cx - R), int(cx + R) + 1):
            d2 = (x - cx) ** 2 + (y - cy) ** 2
            if d2 < (R - 2) ** 2 and max(px[x, y]) > 60:
                tx0, tx1, ty0, ty1 = min(tx0, x), max(tx1, x), min(ty0, y), max(ty1, y)
                uiterst = max(uiterst, d2 ** 0.5 / R)
    if tx1 < 0:
        return dict(beeld=pad, scherm=2 * R, leeg=True)
    return dict(beeld=pad, scherm=round(2 * R), dx=round((tx0 + tx1) / 2 - cx, 1), dy=round((ty0 + ty1) / 2 - cy, 1),
                uiterst=round(uiterst, 3))
for p in sys.argv[1:]:
    m = meet(p)
    ok = (not m.get('leeg')) and abs(m['dx']) <= 2 and m['uiterst'] <= 0.80
    print(('GOED ' if ok else 'LET OP ') + str(m))
