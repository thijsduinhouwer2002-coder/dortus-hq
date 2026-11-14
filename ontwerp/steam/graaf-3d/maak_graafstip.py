"""Graafstippels in de 3D-stijl (Bram, 14 nov 2026, proef voor Daan).

Daan 13:42: links van de ladder staan nog vier lichte pixelvierkantjes op de muur. Dat zijn de stippels "hier kun je
graven" uit `hol_vast.gd` (1 x 1 spelpixel, #c9a27a, elke 3 spelpixels). Daans scheur (`maak_graafrand.py`) paste
beter bij de stijl maar was op ware grootte minder duidelijk (5 van 10). Deze proef houdt wat de stippels duidelijk
maakt (vier lichte punten op een rij, op dezelfde plek, in dezelfde zandkleur) en maakt er kiezeltjes van: rond,
licht van linksboven zoals Gloop en de kluitjes, met een klein donker kuiltje rechtsonder, alsof ze los in de wand
zitten en je ze er zo uit kunt wrikken.

Blad graafstip_3d.png: 2 vakken van 12 x 64 bladpixels (3 x 16 spelpixels, 4 bladpixels per spelpixel):
vak 0 voor een cel rechts van de gang (kiezels aan de linkerkant van de cel), vak 1 gespiegeld.

Gebruik: python3 maak_graafstip.py <uitmap>
"""
import sys
import numpy as np
from PIL import Image

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from maak_graaf import bol, klein, plak, S  # noqa: E402,F401

W, H = 12, 64
ZAND = (224, 186, 142)          # iets lichter dan #c9a27a (oude stippels): de schaduwkant van de bol maakt hem anders donkerder
F = 4                           # op 4 keer maken, dan rond verkleinen (zoals de kluitjes)


def maak(spiegel=False):
    doek = np.zeros((H, W, 4), np.float32)
    # dezelfde hoogtes als de oude stippels: spelpixel 3, 6, 9 en 12 van de gang (midden van de spelpixel)
    for i, sy in enumerate([3, 6, 9, 12]):
        y = sy * 4 + 2
        x = 6 + (0.6 if i % 2 else -0.6)          # klein zigzagje, geen liniaal
        if spiegel:
            x = W - x                             # plek gespiegeld, licht en kuiltje niet (licht blijft linksboven)
        r = 2.6 if i % 2 else 3.0                 # om en om iets kleiner
        kuil = klein(bol(r * 1.25 * F, (24, 10, 30)))
        kuil[..., 3] *= 0.55
        _plak(doek, kuil, x + 0.9, y + 1.0)
        _plak(doek, klein(bol(r * F, ZAND)), x, y)
    return doek


def _plak(doek, stuk, x, y):
    """plak() uit maak_graaf werkt op een doek van S x S; hier is het doek smaller."""
    h, w = stuk.shape[:2]
    x0, y0 = int(round(x - w / 2)), int(round(y - h / 2))
    for yy in range(h):
        for xx in range(w):
            ty, tx = y0 + yy, x0 + xx
            if not (0 <= ty < H and 0 <= tx < W):
                continue
            a = stuk[yy, xx, 3]
            if a <= 0:
                continue
            da = doek[ty, tx, 3]
            oa = a + da * (1 - a)
            doek[ty, tx, :3] = (stuk[yy, xx, :3] * a + doek[ty, tx, :3] * da * (1 - a)) / max(oa, 1e-6)
            doek[ty, tx, 3] = oa


if __name__ == "__main__":
    vak = maak()
    blad = np.concatenate([vak, maak(True)], 1)
    im = Image.fromarray((np.clip(blad, 0, 1) * 255).astype(np.uint8), "RGBA")
    im.save(sys.argv[1] + "/graafstip_3d.png")
    print("klaar", im.size)
