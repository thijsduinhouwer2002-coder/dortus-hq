"""Stappen-icoon: sportschoen van opzij in plaats van twee zolen (las bij Gijs als muizenkop). Mila 17 nov.
Draai: python3 voet_schoen.py (schrijft vergelijk-1x.png en -6x.png in de huidige map)."""
import sys
sys.path.insert(0,'/home/claude/dortus-hq/ontwerp/garmin/reeks')
from PIL import Image, ImageDraw
import stijl_proef_v3 as P
# schoen van opzij, punt naar rechts; eenheden van k, midden (0,0), y omlaag
# twee vlakken: bovenkant en zool, met een zwarte naad van 0,1 k (1 px op 12) ertussen: dan is het een sportschoen
BOVEN = [(-0.50, 0.16), (-0.52, 0.0), (-0.44, -0.44), (-0.12, -0.44), (-0.05, -0.2),
         (0.22, -0.1), (0.42, -0.02), (0.54, 0.08), (0.56, 0.16)]
ZOOL = [(-0.56, 0.26), (0.60, 0.26), (0.58, 0.40), (-0.54, 0.40)]
def schoen(d, x, y, k, kl):
    for vlak in (BOVEN, ZOOL):
        d.polygon([(x + k * a, y + k * b) for a, b in vlak], fill=kl)
def strook(k, voetf):
    Z = 8; W = int(k * 6); H = int(k * 1.6)
    im = Image.new('RGB', (W * Z, H * Z), (0, 0, 0)); d = ImageDraw.Draw(im)
    kl = (0xFF, 0xE2, 0xBE)
    for i, f in enumerate((P.hart, P.bliksem, voetf)):
        f(d, (k + i * 2 * k) * Z, H / 2 * Z, k * Z, kl)
    return im.resize((W, H), Image.LANCZOS)
rijen = [strook(k, f) for k in (12, 17, 18) for f in (P.voet, schoen)]
Wt = max(r.width for r in rijen); Ht = sum(r.height + 2 for r in rijen)
o = Image.new('RGB', (Wt, Ht), (40, 40, 40)); y = 0
for r in rijen: o.paste(r, (0, y)); y += r.height + 2
o.save('vergelijk-1x.png'); o.resize((o.width * 6, o.height * 6), Image.NEAREST).save('vergelijk-6x.png')
