"""Graafrand in de 3D-stijl (Daan, 14 nov 2026): vervangt de gele 1x1-stippels "hier kun je graven".

Een scheur in de aarde langs de rand van de gang, met een lichte lip en drie losse kiezels die er half uit steken,
alsof de aarde daar al los zit. Blad graafrand_3d.png: 2 vakken van 16 x 64 bladpixels (4 x 16 spelpixels):
vak 0 voor een cel rechts van de gang (scheur aan de linkerkant van de cel), vak 1 gespiegeld.
Doorzichtig, je legt het over het 3D-stuk `aarde`.

Gebruik: python3 maak_graafrand.py <hol_proef.png> <uitmap>
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from maak_graaf import bol, plak  # noqa: E402

W, H = 16, 64


def maak(aarde):
    pix = aarde[..., :3].reshape(-1, 3).astype(np.float32) / 255.0
    hel = pix.sum(1)
    kiezel = pix[hel >= np.quantile(hel, 0.97)].mean(0)
    donker = pix[hel <= np.quantile(hel, 0.05)].mean(0) * 0.55
    rng = np.random.default_rng(7)
    doek = np.zeros((H, W, 4), np.float32)
    # scheur: kronkellijn van boven naar onder, 3 tot 7 bladpixels van de rand, smaller aan de uiteinden
    x = 4.5
    for y in range(8, H - 6):
        x = float(np.clip(x + rng.normal(0, 0.7), 4, 8))
        dik = 3.0 * np.sin(np.pi * (y - 8) / (H - 14)) ** 0.6 + 0.4
        for xx in range(W):
            d = abs(xx - x)
            a = np.clip(dik - d + 0.5, 0, 1)
            if a > doek[y, xx, 3]:
                doek[y, xx, :3] = donker
                doek[y, xx, 3] = a
            # lichte lip rechts van de scheur (licht van linksboven valt op de rechterwand van de scheur)
            l = np.clip(2.0 - abs(xx - (x + dik + 1.5)), 0, 1) * 1.0 * np.sin(np.pi * (y - 8) / (H - 14))
            if l > 0 and doek[y, xx, 3] < 0.3:
                doek[y, xx, :3] = np.clip(kiezel * 1.35, 0, 1)
                doek[y, xx, 3] = max(doek[y, xx, 3], l)
    # drie losse kiezels die uit de scheur steken
    zand = np.array([0xc9, 0xa2, 0x7a], np.float32)   # zelfde warme kleur als de oude stippels: het teken blijft gelijk
    for (kx, ky, r) in [(7.5, 17, 3.2), (9.5, 33, 3.8), (7.0, 49, 3.0)]:
        sch = bol(r * 1.1, (20, 8, 24)); sch[..., 3] *= 0.5
        plak_s(doek, sch, kx + 1.0, ky + 1.2)
        plak_s(doek, bol(r, zand), kx, ky)
    return doek


def plak_s(doek, stuk, x, y):
    # zelfde als plak, maar op een doek van W x H
    h, w = stuk.shape[:2]
    x0, y0 = int(round(x - w / 2)), int(round(y - h / 2))
    for yy in range(h):
        for xx in range(w):
            ty, tx = y0 + yy, x0 + xx
            if 0 <= ty < H and 0 <= tx < W and stuk[yy, xx, 3] > 0:
                a = stuk[yy, xx, 3]; da = doek[ty, tx, 3]; oa = a + da * (1 - a)
                doek[ty, tx, :3] = (stuk[yy, xx, :3] * a + doek[ty, tx, :3] * da * (1 - a)) / max(oa, 1e-6)
                doek[ty, tx, 3] = oa


if __name__ == "__main__":
    bron = Image.open(sys.argv[1]).convert("RGBA")
    aarde = np.asarray(bron.crop((76, 4, 140, 68)))
    v0 = maak(aarde)
    v1 = v0[:, ::-1]
    blad = np.concatenate([v0, v1], 1)
    Image.fromarray((np.clip(blad, 0, 1) * 255).astype(np.uint8), "RGBA").save(sys.argv[2] + "/graafrand_3d.png")
    print("klaar")
