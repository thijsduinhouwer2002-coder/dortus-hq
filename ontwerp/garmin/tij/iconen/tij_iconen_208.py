"""Proef op 208 px (Forerunner 55/245 maat): drie velden met de nieuwe pictogrammen boven de getallen, in twee rijen
van drie zoals de drager ze kan kiezen. Alleen om te keuren, geen spelbeeld. Draai: python3 tij_iconen_208.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont
import tij_iconen as T
HIER = os.path.dirname(os.path.abspath(__file__))
F = ImageFont.truetype(os.path.join(HIER, '../../reeks/BigShouldersDisplay.ttf'), 15)
def wijzer(trio, waarden):
    im = Image.new('RGB', (208, 208), (40, 40, 40)); d = ImageDraw.Draw(im)
    d.ellipse([0, 0, 207, 207], fill=(0, 0, 0))
    d.text((104, 60), '07:17', font=ImageFont.truetype(os.path.join(HIER, '../../reeks/BigShouldersDisplay.ttf'), 46), fill=(230, 250, 255), anchor='mm')
    T.KL = (0x2E, 0xD4, 0xE0)
    for i, (naam, w) in enumerate(zip(trio, waarden)):
        cx = 104 + (i - 1) * 44; cy = 104
        if naam == 'hart': T.hart(d, cx, cy, 9)
        elif naam == 'bliksem': T.bliksem(d, cx, cy, 9)
        elif naam == 'schoen': T.vlakken(d, [T.SCHOEN_BOVEN, T.SCHOEN_ZOOL], cx, cy, 9)
        else: T.vlakken(d, T.ICONEN[naam], cx, cy, 9)
        d.text((cx, cy + 15), w, font=F, fill=(230, 250, 255), anchor='mm')
    return im
a = wijzer(['VLAM', 'TRAP', 'KLOK'], ['412', '9', '34'])
b = wijzer(['SPELD', 'ACCU', 'THERMO'], ['6.2', '71', '-3'])
c = wijzer(['hart', 'bliksem', 'schoen'], ['80', '35', '4210'])
o = Image.new('RGB', (208 * 3 + 8, 208), (40, 40, 40))
for i, x in enumerate((c, a, b)): o.paste(x, (i * 212, 0))
o.save(os.path.join(HIER, 'tij-iconen-208-1x.png')); o.resize((o.width * 3, o.height * 3), Image.NEAREST).save(os.path.join(HIER, 'tij-iconen-208-3x.png'))
