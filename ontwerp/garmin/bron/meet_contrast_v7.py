# Contrast nameten op blad v7 (260 MIP): tekst tegen zijn directe achtergrond (eis 4,5:1),
# dieren met hun buitenrand tegen 0000AA en 000055 (eis 3:1). Gebruik: python3 meet_contrast_v7.py <map blad7> <font>
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image
from collections import Counter
import ebb_blad_v3 as v3, ebb_blad_v7 as b6, ebb_dieren_v7 as dv7
def lum(c):
    def k(v):
        v = v/255; return v/12.92 if v <= 0.03928 else ((v+0.055)/1.055)**2.4
    r, g, b = c; return 0.2126*k(r) + 0.7152*k(g) + 0.0722*k(b)
def cr(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la+0.05)/(lb+0.05)
TEKST = [v3.WIT, b6.LICHTCYAAN, v3.SCHUIM, v3.GEEL]
uit = []
for p in sorted(glob.glob(os.path.join(sys.argv[1], 'ebb-v7-*-260.png'))):
    a = np.array(Image.open(p).convert('RGB')); D = a.shape[0]
    istekst = np.zeros(a.shape[:2], bool)
    for c in TEKST: istekst |= (a == c).all(axis=2)
    paren = Counter()
    ys, xs = np.nonzero(istekst)
    for y, x in zip(ys[::3], xs[::3]):
        if np.hypot(x - D/2, y - D/2) > D*0.40: continue
        blok = a[max(0, y-2):y+3, max(0, x-2):x+3].reshape(-1, 3)
        for c in blok:
            t = tuple(int(v) for v in c)
            if t not in [tuple(z) for z in TEKST]:
                paren[(tuple(int(v) for v in a[y, x]), t)] += 1; break
    # alleen paren die echt vaak voorkomen (geen randpixels van dieren of golf)
    ACHTER = [v3.ZWART, v3.W0, v3.W1, v3.W2, v3.W3]   # alleen tekst op zwart, water of knop (W1); randen van dieren en schuim tellen niet
    echt = [(cr(f, b), f, b, n) for (f, b), n in paren.items() if n >= 15 and b in ACHTER]
    if echt:
        m = min(echt); uit.append(f'{os.path.basename(p):28s} laagste tekstcontrast {m[0]:5.1f}:1  ({m[1]} op {m[2]}, {m[3]} px)')
uit.append('')
v3.FONT = sys.argv[2]; dv7.D_NU = 260
def rand_deel(laag, bg):
    al = np.array(laag)[:, :, 3] > 0; rgb = np.array(laag)[:, :, :3]
    rand_ = al & ~(np.roll(al, 1, 0) & np.roll(al, -1, 0) & np.roll(al, 1, 1) & np.roll(al, -1, 1))
    kl = Counter(tuple(int(v) for v in rgb[y, x]) for y, x in zip(*np.nonzero(rand_)))
    return sum(n for c, n in kl.items() if cr(c, bg) >= 3) / sum(kl.values())
uit.append('Dieren op 260 (s=20, stickerrand 2 px). Gevonden: buitenrand tegen 0000AA en 000055. Niet gevonden (silhouet): tegen zwart en 0000AA.')
for soort, naam in dv7.ALLE:
    g = v3.dier_beeld(soort, 20)[0]; z = v3.dier_beeld(soort, 20, 'silhouet')[0]
    uit.append(f'{naam:13s} gevonden 3:1+: op 0000AA {rand_deel(g, v3.W2)*100:4.0f} %  op 000055 {rand_deel(g, v3.W3)*100:4.0f} %   '
               f'silhouet 3:1+: op zwart {rand_deel(z, v3.ZWART)*100:4.0f} %  op 0000AA {rand_deel(z, v3.W2)*100:4.0f} %')
uit.append(f'Losse paren: wit op 0000AA {cr(v3.WIT, v3.W2):.1f}:1, 00AAFF op zwart {cr(v3.W0, v3.ZWART):.1f}:1, 00AAFF op 0000AA {cr(v3.W0, v3.W2):.1f}:1, '
           f'00AAFF (staaf) op zwart {cr(v3.W0, v3.ZWART):.1f}:1, 0055AA (oude staaf) op zwart {cr(v3.W1, v3.ZWART):.1f}:1')
print('\n'.join(uit))
open(os.path.join(sys.argv[1], 'contrast-v7.txt'), 'w').write('\n'.join(uit) + '\n')
raise SystemExit
for soort, naam in []:
    laag = None
    al = np.array(laag)[:, :, 3] > 0; rgb = np.array(laag)[:, :, :3]
    rand_ = al & ~(np.roll(al, 1, 0) & np.roll(al, -1, 0) & np.roll(al, 1, 1) & np.roll(al, -1, 1))
    kl = Counter(tuple(int(v) for v in rgb[y, x]) for y, x in zip(*np.nonzero(rand_)))
    for bg, bn in ((v3.W2, '0000AA'), (v3.W3, '000055')):
        # deel van de buitenrand dat minstens 3:1 haalt
        ok = sum(n for c, n in kl.items() if cr(c, bg) >= 3) / sum(kl.values())
        if bn == '0000AA': r1 = ok
        else: r2 = ok
    uit.append(f'{naam:13s} buitenrand met 3:1 of meer: op 0000AA {r1*100:4.0f} %   op 000055 {r2*100:4.0f} %')
print('\n'.join(uit))
open(os.path.join(sys.argv[1], 'contrast-v7.txt'), 'w').write('\n'.join(uit) + '\n')
