# Overzicht dieren v8: alle 25 in hetzelfde vak van 40 x 32 px (sea log op 260), boven gevonden op 0000AA, onder niet gevonden op zwart.
# Gebruik: python3 overzicht_dieren_v8.py <uit.png> [vergroting]
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_dieren_v8 as dv8
from PIL import Image, ImageDraw, ImageFont
import numpy as np
VW, VH = 40, 32; CEL = 72
uit = sys.argv[1]; z = int(sys.argv[2]) if len(sys.argv) > 2 else 1
n = len(dv8.ALLE); W = CEL*n; H = CEL*2 + 16
im = Image.new('RGB', (W, H), (0,0,0)); d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, CEL], fill=(0,0,170))
try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 8)
except Exception: f = None
rap = []
for i, (soort, naam) in enumerate(dv8.ALLE):
    s = dv8.maat_voor_vak(soort, VW, VH)
    for rij, mode in enumerate((None, 'silhouet')):
        b, (zx, zy), _ = dv8.dier_beeld(soort, s, mode, oog_s=VH)
        im.paste(b, (round(i*CEL + CEL/2 - zx), round(rij*CEL + CEL/2 - zy)), b)
        if rij == 0:
            a = np.array(b)[:, :, 3] > 0; ys, xs = np.nonzero(a)
            rap.append(f'{naam:13s} {xs.max()-xs.min()+1:3d} x {ys.max()-ys.min()+1:3d} px (met rand)')
    w = d.textlength(naam, font=f); d.text((i*CEL + (CEL - w)/2, CEL*2 + 2), naam, fill=(170,170,170), font=f)   # naam heel, gecentreerd
if z > 1: im = im.resize((W*z, H*z), Image.NEAREST)
im.save(uit); print('\n'.join(rap))
