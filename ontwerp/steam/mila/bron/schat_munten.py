"""Mila: voorstel schat.png v2. De goudhoop leest als brood of croissant (Daan, keuring 1 en 3, kan 7).
Zelfde kist, zelfde omtrek van de hoop, maar binnenin losse munten: elke munt een lichte bovenkant en een donkere
rand, in rijen om en om (zoals stenen in een muur), plus twee munten op hun kant. Glinster per beeld zoals nu.
Gebruik: python3 schat_munten.py <schat.png> <uit.png>"""
import sys
from PIL import Image
import numpy as np
L, M, D, R, W = (0xff, 0xe9, 0x9a, 255), (0xf2, 0xb2, 0x3a, 255), (0xd9, 0x8a, 0x2a, 255), (0x8a, 0x4f, 0x1c, 255), (0xff, 0xff, 0xf0, 255)
src = Image.open(sys.argv[1]).convert("RGBA"); a = np.array(src)
def goud(p): return p[3] and p[0] > 200 and p[1] > 120 and p[2] < 140
uit = a.copy()
for f in range(a.shape[1] // 24):
    x0 = f * 24
    for y in range(7, 13):
        for x in range(24):
            if not goud(a[y, x0 + x]): continue
            # munten van 4 breed (3 goud + 1 donkere naad), elke rij een halve munt verschoven; per munt 2 rijen hoog
            rij = (y - 7) // 2; boven = (y - 7) % 2 == 0
            kx = (x + (2 if rij % 2 else 0)) % 4
            if kx == 3: c = R
            elif boven: c = M if kx == 0 else L
            else: c = D
            uit[y, x0 + x] = c
    # twee munten op hun kant tegen de hoop (links en rechts), 1 breed 3 hoog met donkere rand
    for (x, y) in ((4, 8), (20, 8)):
        if goud(a[y + 1, x0 + x]) or goud(a[y, x0 + x]):
            uit[y, x0 + x] = L; uit[y + 1, x0 + x] = M; uit[y + 2, x0 + x] = D
    # glinster van het origineel terugzetten (witte pixels)
    for y in range(16):
        for x in range(24):
            p = a[y, x0 + x]
            if p[3] and p[0] > 245 and p[1] > 235 and p[2] > 180: uit[y, x0 + x] = W
Image.fromarray(uit).save(sys.argv[2])
