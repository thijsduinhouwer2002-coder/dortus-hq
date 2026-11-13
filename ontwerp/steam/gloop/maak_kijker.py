# Plaatjes voor de frisse kijker: links de strook op ware grootte, rechts het figuur 8x (kaal en met toren).
import os, sys
from PIL import Image
HIER = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HIER)
import maak_blad as mb
o = Image.open(os.path.join(HIER, 'strook-ware-grootte.png')).convert('RGB'); W, H = 340, 120
crops = {'nu': o.crop((0, 0, W, H)), 'A': o.crop((W + 10, 126, 2 * W + 10, 126 + H)), 'B': o.crop((W + 10, 252, 2 * W + 10, 252 + H)), 'C': o.crop((W + 10, 378, 2 * W + 10, 378 + H))}
hats = mb.hoeden(); keuze = [hats[0], hats[4], hats[1]]
oud = Image.open(os.path.join(HIER, '../../../producten/steam-hol/godot/kunst/slijm_groot2.png')).convert('RGBA').crop((0, 0, 20, 16))
os.makedirs(os.path.join(HIER, 'kijker'), exist_ok=True)
for k, c in crops.items():
    g = oud if k == 'nu' else Image.open(os.path.join(HIER, f'gloop_{k}.png')).crop((0, 0, 20, 16))
    t = mb.met_toren(g, keuze, 3)
    big = [x.resize((x.width * 8, x.height * 8), Image.NEAREST) for x in (g, t)]
    out = Image.new('RGB', (W + 40 + sum(b.width for b in big) + 40, max(H, max(b.height for b in big)) + 20), (63, 40, 70))
    out.paste(c, (10, 10)); x = W + 30
    for b in big: out.paste(b, (x, out.height - 10 - b.height), b); x += b.width + 20
    out.save(os.path.join(HIER, 'kijker', f'{k}.png'))
