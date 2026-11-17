"""Tij: zes nieuwe veld-pictogrammen (Mila 17 nov, vraag Gijs 07:25).
Alles als rijen x, y in honderdsten van h, midden (0,0), y omlaag, zoals SCHOEN_BOVEN in Teken.mc.
Getekend zoals het horloge het doet: elk punt afgerond met round(h*v/100), vlak zonder gladde rand.
Draai: python3 tij_iconen.py  (schrijft tij-iconen-echt.png en tij-iconen-8x.png en iconen.mc.txt hier)."""
import math, os
from PIL import Image, ImageDraw
HIER = os.path.dirname(os.path.abspath(__file__))

def boog(cx, cy, r, a0, a1, n):
    # punten op een cirkel, hoek in graden, 0 = rechts, 90 = onder (y omlaag)
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def ring_helft(cx, cy, ro, ri, a0, a1, n=6):
    # halve ring als één vlak zonder gat: buitenboog heen, binnenboog terug
    return boog(cx, cy, ro, a0, a1, n) + boog(cx, cy, ri, a1, a0, n)

def rij(p):
    return [int(round(v)) for xy in p for v in xy]

ICONEN = {}
# bestaande, ter vergelijking (uit Teken.mc)
SCHOEN_BOVEN = [-50, 16, -52, 0, -44, -44, -12, -44, -5, -20, 22, -10, 42, -2, 54, 8, 56, 16]
SCHOEN_ZOOL = [-56, 26, 60, 26, 58, 40, -54, 40]

# 3 calorieen: vlam met punt omhoog en een tweede tong links, zodat hij nooit een druppel of speld wordt
ICONEN['VLAM'] = [[10, -50, 30, -22, 38, 6, 34, 30, 18, 46, -12, 48, -30, 38, -38, 18, -38, -4,
                   -34, -22, -20, -4, -10, -24]]
# 4 trappen: drie treden omhoog naar rechts
ICONEN['TRAP'] = [[-50, 48, -50, 18, -18, 18, -18, -14, 14, -14, 14, -46, 48, -46, 48, 48]]
# 5 intensiteitsminuten: stopwatch, ring met een kwart gevuld (de tijd die loopt) en een knop boven
cx, cy, ro, ri = 0, 8, 42, 26
ICONEN['KLOK'] = [rij(ring_helft(cx, cy, ro, ri, 90, 270)),            # linker helft ring
                  rij(ring_helft(cx, cy, ro, ri, -90, 90)),            # rechter helft ring
                  rij([(cx, cy)] + boog(cx, cy, ri + 1, -90, 0, 4)),   # gevuld kwart, 12 tot 3 uur
                  [-10, -50, 10, -50, 10, -38, -10, -38]]              # knop
# 6 afstand: speld, ring met gat en punt omlaag
cx, cy, ro, ri = 0, -16, 34, 14
ICONEN['SPELD'] = [rij(ring_helft(cx, cy, ro, ri, 90, 270)),
                   rij(ring_helft(cx, cy, ro, ri, -90, 90)),
                   [-28, 4, 28, 4, 0, 50]]
# 7 accu: liggende batterij met rand, knop rechts en een vulblok
ICONEN['ACCU'] = [[-62, -34, 46, -34, 46, -20, -62, -20],   # boven
                  [-62, 20, 46, 20, 46, 34, -62, 34],       # onder
                  [-62, -34, -48, -34, -48, 34, -62, 34],   # links
                  [32, -34, 46, -34, 46, 34, 32, 34],       # rechts
                  [46, -14, 60, -14, 60, 14, 46, 14],       # knop
                  [-48, -20, -4, -20, -4, 20, -48, 20]]     # vulling tegen de linkerrand: half vol, rechts leeg
# 8 temperatuur: thermometer, steel en bol, twee streepjes rechts
b = boog(0, 24, 26, 0, 360, 12)[:-1]
ICONEN['THERMO'] = [[-10, -44, -6, -50, 6, -50, 10, -44, 10, 10, -10, 10], rij(b)]

def hart(d, cx, cy, h):
    r = h // 4; top = cy - h // 2
    d.ellipse([cx - 2 * r, top, cx, top + 2 * r], fill=KL)
    d.ellipse([cx, top, cx + 2 * r, top + 2 * r], fill=KL)
    d.polygon([(cx - 2 * r, top + r + 1), (cx + 2 * r, top + r + 1), (cx, top + h)], fill=KL)

def bliksem(d, cx, cy, h):
    r = h // 4; top = cy - h // 2; mid = top + h // 2
    d.polygon([(cx + r, top), (cx - 2 * r, mid + 1), (cx + 1, mid + 1)], fill=KL)
    d.polygon([(cx - r, top + h), (cx + 2 * r, mid - 1), (cx - 1, mid - 1)], fill=KL)

def vlakken(d, rijen, cx, cy, h):
    for r in rijen:
        pts = [(cx + round(h * r[i] / 100.0), cy + round(h * r[i + 1] / 100.0)) for i in range(0, len(r), 2)]
        d.polygon(pts, fill=KL)

KL = (0x2E, 0xD4, 0xE0)
VOLG = [('hart', None), ('bliksem', None), ('schoen', [SCHOEN_BOVEN, SCHOEN_ZOOL])] + [(k, v) for k, v in ICONEN.items()]

def strook(h, kl=(0x2E, 0xD4, 0xE0)):
    global KL; KL = kl
    stap = int(h * 2.2); W = stap * len(VOLG) + 4; H = int(h * 1.8)
    im = Image.new('RGB', (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    for i, (naam, rijen) in enumerate(VOLG):
        cx = 2 + stap // 2 + i * stap; cy = H // 2
        if naam == 'hart': hart(d, cx, cy, h)
        elif naam == 'bliksem': bliksem(d, cx, cy, h)
        else: vlakken(d, rijen, cx, cy, h)
    return im

if __name__ == '__main__':
    stroken = [strook(h) for h in (9, 10, 12, 17)] + [strook(9, (255, 255, 255)), strook(12, (0xFF, 0xE2, 0xBE))]
    W = max(s.width for s in stroken); H = sum(s.height + 2 for s in stroken)
    o = Image.new('RGB', (W, H), (60, 60, 60)); y = 0
    for s in stroken: o.paste(s, (0, y)); y += s.height + 2
    o.save(os.path.join(HIER, 'tij-iconen-echt.png'))
    o.resize((W * 8, H * 8), Image.NEAREST).save(os.path.join(HIER, 'tij-iconen-8x.png'))
    with open(os.path.join(HIER, 'iconen.mc.txt'), 'w') as f:
        for k, rijen in ICONEN.items():
            for j, r in enumerate(rijen):
                f.write('    const %s_%d = [%s];\n' % (k, j, ', '.join(map(str, r))))
    print(open(os.path.join(HIER, 'iconen.mc.txt')).read())
