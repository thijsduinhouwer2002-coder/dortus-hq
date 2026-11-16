"""Spelblad van de begraven stukken voor Olaf (Mila, 16 nov 2026, vraag Olaf 23:40). Zelfde look als proef 3.
Uit: producten/steam-hol/godot/kunst/3d/begraven.png (+ .import) en begraven.json, en een proef in deze map.
Blad: 5 cellen van 64 x 64 bladpixels naast elkaar = 16 x 16 spelpixels per cel bij px 4 (zoals holbord).
  hoed, bot, kist, wortel: gedempt (20 procent minder verzadigd, 15 procent naar de aarde, bot 12 procent minder wit),
    lichte rand van 1 px bovenaan, het onderste derde WEGGESNEDEN met een bultige rand: daar is de cel doorzichtig,
    zodat de echte aarde van het spel er doorheen komt. Op de rand een zachte lichte lip en een schaduwrandje op het
    stuk, en drie kluitjes aarde op het stuk. Holletje 15 procent alleen om het zichtbare deel.
  kist_open: dezelfde kist na het doorgraven, deksel naar achteren open, leeg (donker van binnen). Niet begraven,
    want die cel is dan gang; wel dezelfde demping, en een zachte schaduw eronder.
Bron: stukken3-blad-4x.png = BLAD=1 <bpy-python> begraven.py stukken3-blad-4x.png
Gebruik: python3 maak_blad.py <strook-10min.png 1920x1080 van tak schermen>   (strook alleen voor de proef)
"""
import sys, os, json
import numpy as np
from PIL import Image, ImageFilter
HIER = os.path.dirname(os.path.abspath(__file__))
DOEL = os.path.join(HIER, '../../../producten/steam-hol/godot/kunst/3d')
NAMEN = ['hoed', 'bot', 'kist', 'wortel', 'kist_open']
AARDE = np.array([137, 72, 60]) / 255     # gemiddelde dichte aarde, gemeten in de opname (proef 2)
LIP = np.array([1.0, 0.86, 0.66])
rng = np.random.default_rng(11)
bron = np.asarray(Image.open(os.path.join(HIER, 'stukken3-blad-4x.png')).convert('RGBA'), dtype=np.float32) / 255

def demp(rgb, al, i):
    rgb = rgb * 0.80 + rgb.mean(-1, keepdims=True) * 0.20
    rgb = rgb * 0.85 + AARDE * 0.15
    if i == 1: rgb = rgb * 0.88
    dek = al[..., 0] > 0.5; ys = np.argmax(dek, axis=0)
    for x in np.where(dek.any(0))[0]:
        y = ys[x]; rgb[y, x] = rgb[y, x] * 0.45 + np.array([1.0, 0.93, 0.82]) * 0.55
    return rgb, al

def begraaf(rgb, al):
    dek = al[..., 0] > 0.5
    rij = np.where(dek.any(1))[0]; kol = np.where(dek.any(0))[0]
    top, bod = rij[0], rij[-1]; snij = top + (bod - top + 1) * 0.64; n = len(kol)
    bult = np.convolve(rng.normal(0, 1.8, n + 8), np.ones(7) / 7, 'same')[4:n + 4] * 1.7
    rand = {}
    for k, x in enumerate(kol):
        y = int(round(snij + bult[k])); rand[x] = y
        al[y:, x] = 0                                                   # weg: hier komt de echte aarde door
        if dek[y:y + 2, x].any():
            rgb[y, x] = AARDE * 0.62 + LIP * 0.40; al[y, x] = 1           # lip (1 px bij px 4 is een kwart spelpixel,
            if y + 1 < 64: rgb[y + 1, x] = AARDE * 0.8 + LIP * 0.2; al[y + 1, x] = 1   # dus 2 rijen: lip en overgang)
        for d in (1, 2):
            if y - d >= 0 and dek[y - d, x]: rgb[y - d, x] *= 0.68 if d == 1 else 0.82   # schaduw op het stuk
    ks = [x for x in kol if dek[:rand[x] - 4, x].any()]
    for _ in range(2):                                                  # kluitjes van 3 x 3 bladpixels
        x = ks[rng.integers(len(ks))]; y = rand[x] - 4 - rng.integers(0, 4)
        if y < 1 or x + 2 >= 64 or not dek[y:y + 3, x:x + 3].all(): continue
        rgb[y:y + 3, x:x + 3] = np.clip(AARDE * 1.18, 0, 1); al[y:y + 3, x:x + 3] = 1
        rgb[y, x:x + 2] = AARDE * 0.62 + LIP * 0.40
    return rgb, al

def holletje(al, sterk):
    m = Image.fromarray(((al[..., 0] > 0.5) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2.5))
    return np.asarray(m, dtype=np.float32)[..., None] / 255 * sterk

blad = np.zeros((64, 64 * 5, 4), dtype=np.float32)
for i, naam in enumerate(NAMEN):
    c = bron[:, i * 64:(i + 1) * 64]
    rgb, al = demp(c[..., :3].copy(), c[..., 3:].copy(), i)
    if naam != 'kist_open':
        rgb, al = begraaf(rgb, al); h = holletje(al, 0.15)
    else:
        sch = np.zeros_like(al); dek = al[..., 0] > 0.5; bod = np.where(dek.any(1))[0][-1]
        sch[bod - 3:bod + 3] = dek.any(0)[None, :, None]                # schaduw onder de kist
        h = np.asarray(Image.fromarray((sch[..., 0] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3)), dtype=np.float32)[..., None] / 255 * 0.5
    zw = np.array([45, 20, 18]) / 255
    a_out = al + h * (1 - al)
    rgb_out = (rgb * al + zw * h * (1 - al)) / np.maximum(a_out, 1e-6)
    blad[:, i * 64:(i + 1) * 64] = np.dstack([rgb_out, a_out])
img = Image.fromarray((np.clip(blad, 0, 1) * 255).astype(np.uint8))
img.save(os.path.join(DOEL, 'begraven.png'))
imp = open(os.path.join(DOEL, 'holbord.png.import')).read().replace('holbord', 'begraven')
imp = '\n'.join(l for l in imp.split('\n') if not l.startswith('uid='))
open(os.path.join(DOEL, 'begraven.png.import'), 'w').write(imp)
json.dump({'_uitleg': 'Mila 16 nov (Olaf 23:40): begraven stukken, zie ontwerp/steam/begraven/LEESMIJ.md. '
           'Cel 64 x 64 bladpixels = 16 x 16 spelpixels (px 4), cel linksboven = linksboven van de spelcel. '
           'hoed en kist in de bovenste rij, bot en wortel in de gangrij; kist_open na het doorgraven (dan is het gang).',
           'blad': 'res://kunst/3d/begraven.png', 'cel_px': [64, 64], 'px': 4, 'frames': NAMEN},
          open(os.path.join(DOEL, 'begraven.json'), 'w'), indent=1, ensure_ascii=False)
# proef: in de echte opname, 64 -> 48 (spel op 3x), voor en na het doorgraven van de kist
if len(sys.argv) > 1:
    strook = Image.open(sys.argv[1]).convert('RGBA'); RIJ = (940, 987)
    def leg(plek):
        im = strook.copy()
        for cx, r, i in plek:
            im.alpha_composite(img.crop((i * 64, 0, i * 64 + 64, 64)).resize((48, 48), Image.LANCZOS), (cx * 48, RIJ[r]))
        return im.crop((0, 905, 960, 1035))
    voor = leg([(2, 0, 0), (7, 1, 1), (11, 0, 2), (16, 1, 3)])
    na = leg([(2, 0, 0), (7, 1, 1), (11, 0, 4), (16, 1, 3)])
    voor.save(os.path.join(HIER, 'blad-echt-1x.png'))
    p = Image.new('RGBA', (5 * 230 + 20, 470), (30, 30, 30, 255))
    for k, (cx, r, bronbeeld) in enumerate([(2, 0, voor), (7, 1, voor), (11, 0, voor), (16, 1, voor), (11, 0, na)]):
        y = RIJ[r] - 905
        p.paste(bronbeeld.crop((cx * 48 - 10, y - 10, cx * 48 + 58, y + 58)).resize((224, 224), Image.NEAREST), (10 + k * 230, 0))
    p.paste(img.resize((1280, 256), Image.NEAREST).crop((0, 0, 1150, 230)), (10, 236))
    p.save(os.path.join(HIER, 'blad-proef.png'))
print('klaar', img.size)
