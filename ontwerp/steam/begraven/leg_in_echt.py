"""Proef 2: de begraven stukken in een ECHTE opname van 1920x1080 (Mila, 16 nov 2026, moets Daan 22:45).
Minder demping dan proef 1 (20 procent minder verzadigd in plaats van 35, 15 procent naar de aarde in plaats van 28)
en een lichte rand van 1 schermpixel aan de bovenkant, zodat ze op ware grootte niet in de aarde wegvallen.
Het spel staat op 1920 op 3x: een cel van 16 spelpixels is 48 schermpixels, dus een vak van 64 bladpixels wordt 48.
Gebruik: python3 leg_in_echt.py <strook-10min.png 1920x1080> <stukken-4x.png> <uitmap>
Uit: proef2-echt-1x.png (linkerkant van de strook, ware grootte), proef2-echt-3x.png (zelfde, 3x zonder verzachten),
     proef2-echt-B-1x.png (eerlijke variant: alleen bot en wortel, als graven geen hoed of schat oplevert).
"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
strook, stuk, uit = Image.open(sys.argv[1]).convert('RGBA'), Image.open(sys.argv[2]).convert('RGBA'), sys.argv[3]
Y0, Y1, X1 = 905, 1035, 900          # strook van de aarde, links van het hol
RIJ = (940, 987)                      # bovenkant van de twee aarderijen (gemeten in de opname)
aarde = np.asarray(strook.crop((0, 945, 880, 1025)), dtype=np.float32)[..., :3].reshape(-1, 3).mean(0) / 255

def demp(vak):
    a = np.asarray(vak, dtype=np.float32) / 255
    rgb, al = a[..., :3], a[..., 3:]
    rgb = rgb * 0.80 + rgb.mean(-1, keepdims=True) * 0.20        # 20 procent minder verzadigd
    rgb = rgb * 0.85 + aarde * 0.15                              # 15 procent naar de aarde
    # lichte rand van 1 px bovenaan: de bovenste dekkende pixel per kolom wordt lichter
    dek = al[..., 0] > 0.5
    ys = np.argmax(dek, axis=0); heeft = dek.any(0)
    for x in np.where(heeft)[0]:
        y = ys[x]; rgb[y, x] = rgb[y, x] * 0.45 + np.array([1.0, 0.93, 0.82]) * 0.55
    return Image.fromarray((np.dstack([np.clip(rgb, 0, 1), al]) * 255).astype(np.uint8))

def holletje(vak):
    al = vak.split()[3].filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(2))
    zw = Image.new('RGBA', vak.size, (45, 20, 18, 0)); zw.putalpha(al.point(lambda v: int(v * 0.7)))
    return zw

def leg(plekken):
    im = strook.copy()
    for cx, rij, i in plekken:
        vak = stuk.crop((i * 64, 0, i * 64 + 64, 64)).resize((48, 48), Image.LANCZOS)
        x, y = cx * 48, RIJ[rij]
        im.alpha_composite(holletje(vak), (x, y)); im.alpha_composite(demp(vak), (x, y))
    return im.crop((0, Y0, X1 + 60, Y1))

A = [(2, 0, 0), (7, 1, 1), (11, 0, 2), (16, 1, 3)]   # hoed, bot, kistje, wortel; ver uit elkaar, 5 cellen tussen
B = [(4, 1, 1), (13, 0, 3)]                           # alleen bot en wortel
a = leg(A); a.save(os.path.join(uit, 'proef2-echt-1x.png'))
a.resize((a.width * 3, a.height * 3), Image.NEAREST).save(os.path.join(uit, 'proef2-echt-3x.png'))
leg(B).save(os.path.join(uit, 'proef2-echt-B-1x.png'))
# blad: A en B op 1x boven elkaar, plus de vier stukken los op 3x van de 1x
blad = Image.new('RGBA', (a.width, a.height * 2 + 30), (30, 30, 30, 255))
blad.paste(a, (0, 0)); blad.paste(leg(B), (0, a.height + 30))
blad.save(os.path.join(uit, 'proef2-blad-1x.png')); print('klaar', aarde * 255)
