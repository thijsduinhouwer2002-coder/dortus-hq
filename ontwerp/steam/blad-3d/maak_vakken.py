"""Vak 3 en 4 van het blad: figuren los uitgesneden uit doorzichtige renders, op de kaartkleur,
groot en eronder op ware grootte (Daan, 14 nov). python3 maak_vakken.py <map met renders>"""
import sys
from PIL import Image
import numpy as np
R = sys.argv[1]; BG = (58, 36, 64, 255); W = 1660

def stukken(pad, drempel=60):
    a = Image.open(pad).convert("RGBA"); al = np.array(a)[:, :, 3]
    kol = (al > drempel).any(axis=0); uit = []; x = 0
    while x < len(kol):
        if kol[x]:
            b = x
            while x < len(kol) and kol[x]: x += 1
            if x - b > 8: uit.append((b, x))
        x += 1
    rij = (al > drempel).any(axis=1); y0 = int(np.argmax(rij)); y1 = len(rij) - int(np.argmax(rij[::-1]))
    res = []
    for b, e in uit:
        m = 14; res.append(a.crop((max(0, b - m), max(0, y0 - m), min(a.width, e + m), min(a.height, y1 + 22))))
    return res, y1 - y0

def zacht(im, rand=12):
    im = im.copy(); al = np.array(im.split()[3]).astype(float); h, w = al.shape
    al = np.clip((al - 32) * 255 / (255 - 32), 0, 255)  # de vage brede schaduw van de schaduwvanger weg, de schaduw onder de voeten blijft
    rx = np.minimum(np.arange(w), np.arange(w)[::-1]) / rand; ry = np.minimum(np.arange(h), np.arange(h)[::-1]) / rand
    m = np.clip(np.minimum.outer(ry, rx), 0, 1); im.putalpha(Image.fromarray((al * m).astype("uint8"))); return im

def hoofddeel(im):
    """Alleen het figuur zelf: losse stukjes van de buren (bezempunt) weg."""
    from scipy import ndimage
    al = np.array(im.split()[3]); lab, n = ndimage.label(al > 20)
    if n < 2: return im
    groot = 1 + int(np.argmax(ndimage.sum(np.ones_like(al), lab, range(1, n + 1))))
    houd = ndimage.binary_dilation(lab == groot, iterations=3)
    im = im.copy(); im.putalpha(Image.fromarray((al * houd).astype("uint8"))); return im

def vak(figs, groot_h, klein_h, uit, extra=None):
    figs = [hoofddeel(f) for f in figs]
    n = len(figs); vakw = W // n
    gs = [f.resize((max(1, round(f.width * groot_h / f.height)), groot_h), Image.LANCZOS) for f in figs]
    ks = [f.resize((max(1, round(f.width * klein_h / f.height)), klein_h), Image.LANCZOS) for f in figs]
    H = groot_h + klein_h + 40
    doek = Image.new("RGBA", (W, H), BG)
    for i in range(n):
        cx = vakw * i + vakw // 2
        g = zacht(gs[i]); doek.alpha_composite(g, (cx - g.width // 2, 0))
        k = zacht(ks[i], 3); doek.alpha_composite(k, (cx - k.width // 2, groot_h + 22))
    doek.convert("RGB").save(uit)

# Gloop: vier standen, ware grootte 42 px lijf
gl = [stukken(f"{R}/g-{s}.png")[0][0] for s in ("rust", "knipper", "blij", "hap")]
vak(gl, 300, 50, "vak3-gloop.png")
# helden met hoed (10) en de zeven helden: zelfde maat per figuur
def plakken(pad, n, stap_px, drempel=40):
    a = Image.open(pad).convert("RGBA"); al = np.array(a)[:, :, 3]
    rij = (al > drempel).any(axis=1); y0 = int(np.argmax(rij)); y1 = len(rij) - int(np.argmax(rij[::-1]))
    mid = a.width / 2; half = stap_px * 0.44
    return [a.crop((round(mid + (i - (n - 1) / 2) * stap_px - half), max(0, y0 - 10),
                    round(mid + (i - (n - 1) / 2) * stap_px + half), min(a.height, y1 + 18))) for i in range(n)]
h10 = plakken(f"{R}/hoed10.png", 10, 1.5 * 1600 / 15.5); h7 = plakken(f"{R}/helden7.png", 7, 1.5 * 1540 / 11.0)
vak(h10, 250, 60, "vak4-hoeden.png")
vak(h7, 230, 50, "vak4-helden.png")
