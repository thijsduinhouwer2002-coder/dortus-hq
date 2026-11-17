"""Proef 3: de begraven stukken half IN de aarde (Mila, 16 nov 2026, moet Daan 23:30).
Proef 2 lag op de aarde. Nu: het onderste derde van elk stuk zit onder een rand aarde met een grillige bovenkant en
losse kruimels erboven, met een lichte lip op de rand (zoals de bovenrand van de gegraven gang). Het donkere holletje
bijna weg (70 naar 15 procent), want juist die schaduwrand liet ze geplakt lijken. Het bot 12 procent minder wit.
Variant A blijft (Olaf en Sanne 23:40). Demping zoals proef 2.
Gebruik: python3 leg_in_echt3.py <strook-10min.png 1920x1080> <stukken2-4x.png> <uitmap>
Uit: proef3-echt-1x.png, proef3-echt-3x.png, proef3-stukken-1x-4x.png, proef3-voor-na-4x.png (proef 2 boven, 3 onder)
"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
strook, stuk, uit = Image.open(sys.argv[1]).convert('RGBA'), Image.open(sys.argv[2]).convert('RGBA'), sys.argv[3]
Y0, Y1, X1 = 905, 1035, 900
RIJ = (940, 987)
aarde = np.asarray(strook.crop((0, 945, 880, 1025)), dtype=np.float32)[..., :3].reshape(-1, 3).mean(0) / 255
rng = np.random.default_rng(11)
LIP = np.array([1.0, 0.86, 0.66])          # warm licht, zoals de bovenrand van de gang

def demp(vak, i):
    a = np.asarray(vak, dtype=np.float32) / 255
    rgb, al = a[..., :3].copy(), a[..., 3:].copy()
    rgb = rgb * 0.80 + rgb.mean(-1, keepdims=True) * 0.20
    rgb = rgb * 0.85 + aarde * 0.15
    if i == 1: rgb *= 0.88                                        # bot: minder wit, was het felste in de rij
    dek = al[..., 0] > 0.5
    ys = np.argmax(dek, axis=0); heeft = dek.any(0)
    for x in np.where(heeft)[0]:
        y = ys[x]; rgb[y, x] = rgb[y, x] * 0.45 + np.array([1.0, 0.93, 0.82]) * 0.55
    return rgb, al

def begraaf(rgb, al, grond):
    """onderste derde onder de aarde. De aarde ervoor is de ECHTE grond van die plek (geen eigen vlak, dat las
    als een blok), met een bultige rand, een zachte lichte lip waar de aarde voor het stuk ligt, een
    schaduwrandje van 1 px op het stuk vlak boven de aarde, en een paar kluitjes van 2 px op het stuk."""
    dek = al[..., 0] > 0.5
    rij = np.where(dek.any(1))[0]; kol = np.where(dek.any(0))[0]
    top, bod = rij[0], rij[-1]; h = bod - top + 1
    snij = top + h * 0.64
    n = len(kol)
    bult = np.convolve(rng.normal(0, 2.0, n + 8), np.ones(5) / 5, 'same')[4:n + 4] * 1.5
    rand = {}
    for k, x in enumerate(kol):
        y = int(round(snij + bult[k])); rand[x] = y
        if not dek[y:, x].any(): continue
        rgb[y:, x] = grond[y:, x]; al[y:, x] = np.where(dek[y:, x], 1, 0)[:, None] * 1.0
        if dek[y, x] or dek[min(y + 1, rgb.shape[0] - 1), x]:
            rgb[y, x] = np.clip(grond[y, x] * 0.62 + LIP * 0.40, 0, 1); al[y, x] = 1      # lip
        if y - 1 >= 0 and dek[y - 1, x]: rgb[y - 1, x] = rgb[y - 1, x] * 0.68               # schaduw op het stuk
    ks = [x for x in kol if dek[:rand[x], x].any()]
    for _ in range(3):
        x = ks[rng.integers(len(ks))]; y = rand[x] - 3 - rng.integers(0, 3)
        if y < 1 or x + 1 >= rgb.shape[1] or not (dek[y, x] and dek[y, x + 1]): continue
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)): rgb[y + dy, x + dx] = grond[y + dy, x + dx]; al[y + dy, x + dx] = 1
        rgb[y, x] = np.clip(grond[y, x] * 0.72 + LIP * 0.30, 0, 1)
    return rgb, al

def holletje(vak):
    al = vak.split()[3].filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2))
    zw = Image.new('RGBA', vak.size, (45, 20, 18, 0)); zw.putalpha(al.point(lambda v: int(v * 0.15)))
    return zw

def leg(plekken):
    im = strook.copy()
    for cx, rij, i in plekken:
        vak = stuk.crop((i * 64, 0, i * 64 + 64, 64)).resize((48, 48), Image.LANCZOS)
        x, y = cx * 48, RIJ[rij]
        grond = np.asarray(strook.crop((x, y, x + 48, y + 48)), dtype=np.float32)[..., :3] / 255
        rgb, al = demp(vak, i); rgb, al = begraaf(rgb, al, grond)
        zicht = Image.fromarray((np.dstack([np.clip(rgb, 0, 1), al]) * 255).astype(np.uint8))
        stukmask = np.asarray(vak)[..., 3] > 127
        boven = (al[..., 0] > 0.5) & stukmask & ~np.all(np.isclose(rgb, grond, atol=1e-4), axis=-1)
        schaduw = Image.fromarray((boven * 255).astype(np.uint8)); hz = Image.new('RGBA', (48, 48)); hz.putalpha(schaduw)
        im.alpha_composite(holletje(hz), (x, y))      # alleen om het zichtbare deel, geen spook van het begraven deel
        im.alpha_composite(zicht, (x, y))
    return im.crop((0, Y0, X1 + 60, Y1))

A = [(2, 0, 0), (7, 1, 1), (11, 0, 2), (16, 1, 3)]
a = leg(A); a.save(os.path.join(uit, 'proef3-echt-1x.png'))
a.resize((a.width * 3, a.height * 3), Image.NEAREST).save(os.path.join(uit, 'proef3-echt-3x.png'))
rijen = Image.new('RGBA', (4 * 300 + 50, 300), (30, 30, 30, 255))
for k, (cx, r, i) in enumerate(A):
    y = RIJ[r] - Y0
    rijen.paste(a.crop((cx * 48 - 13, y - 13, cx * 48 + 62, y + 62)).resize((300, 300), Image.NEAREST), (10 + k * 310, 0))
rijen.save(os.path.join(uit, 'proef3-stukken-1x-4x.png'))
oud = Image.open(os.path.join(uit, 'proef2-echt-1x.png')).convert('RGBA')
vn = Image.new('RGBA', (4 * 300 + 50, 610), (30, 30, 30, 255))
for k, (cx, r, i) in enumerate(A):
    y = RIJ[r] - Y0
    for j, bron in enumerate((oud, a)):
        vn.paste(bron.crop((cx * 48 - 13, y - 13, cx * 48 + 62, y + 62)).resize((300, 300), Image.NEAREST), (10 + k * 310, j * 310))
vn.save(os.path.join(uit, 'proef3-voor-na-4x.png')); print('klaar')
