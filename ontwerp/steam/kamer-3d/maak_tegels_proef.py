"""Daan 13 nov: snijdt kamertegels uit een render (960x160, 1 spelpixel = 4 px, kolom = 64 px) en legt
rijen zoals het spel ze zou leggen: oud (kamer_links/rechts om en om) tegen nieuw (los, begin, midden, eind)."""
import sys
from PIL import Image
oud, nieuw, uit = Image.open(sys.argv[1]), Image.open(sys.argv[2]), sys.argv[3]
nieuw_b = Image.open(sys.argv[4]) if len(sys.argv) > 4 else nieuw   # ronde 2: tweede middenstuk
K, Y0, Y1 = 64, 32, 96            # bovenste rij: spelpixel 8 tot 24
def tegel(im, k): return im.crop((k * K, Y0, (k + 1) * K, Y1))
aarde = tegel(nieuw, 13)
oude = {"L": tegel(oud, 3), "R": tegel(oud, 11)}
nieuwe = {"b": tegel(nieuw, 2), "m": tegel(nieuw, 3), "e": tegel(nieuw, 4), "l": tegel(nieuw, 11), "n": tegel(nieuw_b, 3)}
rijen = [
    ("oud, 3 cellen gegraven", ["a", "L", "R", "L", "a", "a", "R", "a"], oude),
    ("nieuw, 3 cellen", ["a", "b", "m", "e", "a", "a", "l", "a"], nieuwe),
    ("nieuw, 5 cellen en 1 los", ["a", "b", "m", "n", "m", "e", "a", "l"], nieuwe),
]
W = 8 * K
doek = Image.new("RGBA", (W, len(rijen) * (Y1 - Y0 + 8)), (30, 22, 40, 255))
for i, (_, cel, set_) in enumerate(rijen):
    for k, c in enumerate(cel):
        t = aarde if c == "a" else set_[c]
        doek.alpha_composite(t, (k * K, i * (Y1 - Y0 + 8)))
doek.save(uit.replace(".png", "-groot.png"))
klein = doek.resize((W * 3 // 4, doek.height * 3 // 4), Image.LANCZOS)   # ware grootte: strook 120 px = 3 px per spelpixel
klein.save(uit.replace(".png", "-ware-grootte.png"))
klein.resize((klein.width * 3, klein.height * 3), Image.NEAREST).save(uit.replace(".png", "-ware-grootte-3x.png"))
print("klaar")
