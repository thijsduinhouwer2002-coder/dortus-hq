# Blad dieren v8.3: het echte FR255-beeld (sea log, plaatjesrun 42956563037) naast dezelfde dieren in v8.3,
# getekend met horloge_sim.py (nabootsing van DierenData.mc). Daaronder alle 25 op 260 (ware grootte en 3x) en op 454.
# Gebruik: python3 blad_v83.py <fr255-scene4.png> <uitmap>
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from PIL import Image, ImageDraw, ImageFont
G = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
echt = Image.open(sys.argv[1]).convert('RGB'); uit = sys.argv[2]; os.makedirs(uit, exist_ok=True)
V82 = h.laad(os.path.join(G, 'ebb-dieren-v82-data.json')); V83 = h.laad(os.path.join(G, 'ebb-dieren-v83-data.json'))
F = ImageFont.load_default()

def sealog(D, oog):
    """De 9 dieren van sea log blad 1 zoals in scène 4 (8 gevonden, kogelvis als silhouet), maat 20 (d * 0,078 op 260)."""
    im = Image.new('RGB', (156, 120)); dr = ImageDraw.Draw(im)
    for j in range(9):
        cx = 28 + (j % 3)*50; cy = 20 + (j // 3)*40
        if j == 8: h.silhouet(dr, D[8], cx, cy, 20)
        else: h.teken(dr, D[j], cx, cy, 20, oog)
    return im

def groot(im, k): return im.resize((im.width*k, im.height*k), Image.NEAREST)
# 1. echt (uitsnede rond de dieren) | v8.2 nagebootst | v8.3 nagebootst, alle drie 3x
e = groot(echt.crop((133, 255, 289, 375)), 3)
a = groot(sealog(V82, 'oud'), 3); b = groot(sealog(V83, 'v83'), 3)
a.save(os.path.join(uit, 'sealog-v82-sim-3x.png')); b.save(os.path.join(uit, 'sealog-v83-sim-3x.png'))
r260 = h.raster(V83, 20, 'v83'); r454 = h.raster(V83, 35, 'v83', kolommen=9)
r260.save(os.path.join(uit, 'alle25-260.png')); groot(r260, 3).save(os.path.join(uit, 'alle25-260-3x.png')); r454.save(os.path.join(uit, 'alle25-454.png'))
W = max(e.width + a.width + b.width + 40, groot(r260, 2).width + r454.width + 30)
H = 30 + e.height + 30 + max(groot(r260, 2).height, r454.height) + 20
blad = Image.new('RGB', (W, H), (16, 16, 24)); d = ImageDraw.Draw(blad)
x = 10
for im, t in ((e, 'echt FR255 (bouw 3), 3x'), (a, 'v8.2 nagebootst, 3x'), (b, 'v8.3 nagebootst, 3x')):
    d.text((x, 10), t, fill=(255, 255, 255), font=F); blad.paste(im, (x, 26)); x += im.width + 10
y = 26 + e.height + 14
d.text((10, y), 'alle 25 op 260 (sea log, maat 20), 2x; gevonden boven, silhouet eronder', fill=(255, 255, 255), font=F)
blad.paste(groot(r260, 2), (10, y + 16))
d.text((20 + groot(r260, 2).width, y), 'op 454 (maat 35), ware grootte', fill=(255, 255, 255), font=F)
blad.paste(r454, (20 + groot(r260, 2).width, y + 16))
blad.save(os.path.join(G, 'ebb-blad-v83.png')); print(blad.size)
