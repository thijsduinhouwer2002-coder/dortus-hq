# Zet de dieren van ebb_dieren_v7.py om naar data in hetzelfde formaat als Gijs' maak_dieren_data.py
# (per dier: [aantal delen, per deel: rol, aantal punten, x, y, ...; aantal ogen, per oog: x, y], int8 in 1/90 van de diermaat,
# al op het zwaartepunt, hoogstens 60 punten per veelhoek). Nieuw t.o.v. v6: rol 6 = 'zz' (wit, zonder stickerrand).
# Controleert ook: dier opnieuw tekenen uit de data en vergelijken met dier_beeld (pixels die verschillen).
# Gebruik: python3 exporteer_dieren_v7.py <uit.json>
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
import ebb_dieren_v7 as dv7
from PIL import Image, ImageDraw
import numpy as np
SCHAAL = 90; MAX = 60

def rdp(pts, eps):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]; dx, dy = b[0]-a[0], b[1]-a[1]; n = math.hypot(dx, dy)
    best, j = -1, 0
    for i in range(1, len(pts)-1):
        p = pts[i]; d = abs(dy*(p[0]-a[0]) - dx*(p[1]-a[1]))/n if n else math.hypot(p[0]-a[0], p[1]-a[1])
        if d > best: best, j = d, i
    return rdp(pts[:j+1], eps)[:-1] + rdp(pts[j:], eps) if best > eps else [a, b]

def vereenvoudig(pts):
    p = [pts[0]]
    for q in pts[1:]:
        if round(q[0]*100) != round(p[-1][0]*100) or round(q[1]*100) != round(p[-1][1]*100): p.append(q)
    eps = 0.004; uit = rdp(p + [p[0]], eps)[:-1] if len(p) > 3 else p
    while len(uit) > MAX: eps *= 1.5; uit = rdp(p + [p[0]], eps)[:-1]
    return uit

def kleur(c): return '0x%02X%02X%02X' % c
dieren = []; rap = []
for nr, (soort, naam) in enumerate(dv7.ALLE, 1):
    delen, ogen = dv7.delen_v7(soort)
    im, (zx, zy), _ = dv7.dier_beeld(soort, 100)
    c = im.width/2; ox, oy = (zx - c)/100, (zy - c)/100
    b = [len(delen)]; poly = []
    for pts, rol in delen:
        v = [(round((x-ox)*SCHAAL), round((y-oy)*SCHAAL)) for x, y in vereenvoudig([(x, y) for x, y in pts])]
        assert all(-127 <= q <= 127 for xy in v for q in xy), (soort, rol)
        b += [dv7.ROL_V7[rol], len(v)] + [q for xy in v for q in xy]; poly.append((rol, v))
    b += [len(ogen)] + [round((x-ox)*SCHAAL) if i == 0 else round((y-oy)*SCHAAL) for x, y in ogen for i in (0, 1)]
    l, li, d = v3.TINT[soort]
    dieren.append({'nr': nr if nr < 25 else 'bonus', 'soort': soort, 'naam': naam, 'tint': [kleur(l), kleur(li), kleur(d)],
                   'rand': kleur(dv7.RAND[soort]), 'slaperig': soort in dv7.dv5.SLAPERIG, 'bytes': b})
    # controle: teken uit de data (alleen de vorm) en vergelijk met de vorm van dier_beeld op s=100
    W = im.width; t = Image.new('L', (W, W), 0); td = ImageDraw.Draw(t)
    for rol, v in poly:
        if rol != 'zz': td.polygon([(zx + x*100/SCHAAL, zy + y*100/SCHAAL) for x, y in v], fill=255)
    echt = Image.new('L', (W, W), 0); ed = ImageDraw.Draw(echt)
    for pts, rol in delen:
        if rol != 'zz': ed.polygon([(c + x*100, c + y*100) for x, y in pts], fill=255)
    a1, a2 = np.array(t) > 0, np.array(echt) > 0
    rap.append(f'{nr:>2} {naam:13s} {len(b):4d} bytes, {max(len(v) for _, v in poly):2d} punten max, vorm wijkt af: {100*(a1 ^ a2).sum()/a2.sum():.1f}%')
uit = {'bron': 'ontwerp/garmin/bron/ebb_dieren_v7.py', 'schaal': SCHAAL,
       'rollen': dv7.ROL_V7, 'silhouet': {'vlak': kleur(dv7.SIL), 'rand': kleur(dv7.SIL_RAND)},
       'stickerrand_px': {'260': 2, '390-416': 2, '454': 3}, 'dieren': dieren}
json.dump(uit, open(sys.argv[1], 'w'), indent=0)
rap.append(f'totaal {sum(len(x["bytes"]) for x in dieren)} bytes')
print('\n'.join(rap))
