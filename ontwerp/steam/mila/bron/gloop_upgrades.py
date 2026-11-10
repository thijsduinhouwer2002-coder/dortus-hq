# Mila 10 nov: tekening per upgrade-stap van Gloop. Geen schalen. Stappen stapelen (Royal heeft ook Big en Bouncy).
#   1 Big Gloop:    eigen bladen kunst/slijm_groot.png en slijm_leven_groot.png (bron: gloop_groot.py), lijf 1 px groter rondom.
#   2 Bouncy Gloop: kunst/slijm_upgrades.png cel 0 (x 0, 16 x 16), VOOR Gloop, net als het frame op (-8, -16),
#                   maar met y + (top_nu() - 5): een glansster rechtsboven tegen zijn kruin. Niet tekenen als hij plat ligt.
#   3 Royal Gloop:  kunst/slijm_upgrades.png cel 1 (x 16, 24 x 16), ACHTER Gloop op (-12, -16): een paarse cape met
#                   gouden zoom die links en rechts onder hem uitwaait. Staat vast op de vloer. Niet tekenen als hij plat ligt.
import os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
K = os.path.join(R, "producten", "steam-hol", "godot", "kunst")
D = (28, 18, 22, 255)
G3, W = (230, 255, 244, 255), (255, 255, 255, 255)
P0, P1, P2 = (0x3a, 0x1d, 0x4e, 255), (0x6e, 0x3c, 0x8f, 255), (0x9b, 0x62, 0xbe, 255)
GD, GL = (0xd9, 0x8a, 0x2a, 255), (0xff, 0xd2, 0x5c, 255)
blad = Image.new("RGBA", (40, 16), (0, 0, 0, 0))
def zet(ox, w, pts, kl):
    for x, y in pts:
        if 0 <= x < w and 0 <= y < 16: blad.putpixel((ox + x, y), kl)
# cel 0: glansster, midden op (13, 6) bij top 5 (bovenkant van Big Gloop in rust)
zet(0, 16, [(13, 3), (13, 4), (11, 6), (12, 6), (14, 6), (15, 6), (13, 8), (13, 9)], G3)
zet(0, 16, [(13, 5), (12, 6), (14, 6), (13, 7)], W)
zet(0, 16, [(13, 6)], W)
# cel 1: cape, 24 breed; Big Gloop beslaat x 5 tot 18 van deze cel (1 tot 14 in zijn eigen frame + 4)
for y in range(7, 16):
    uit = 0 if y < 10 else 1 if y < 12 else 2 if y < 14 else 3
    l, r = 4 - uit, 19 + uit
    for x in range(l, r + 1):
        kl = P0 if x in (l, r) else (P2 if x == l + 1 else P1)
        zet(16, 24, [(x, y)], kl)
for x in range(1, 23):
    zet(16, 24, [(x, 15)], GL if x % 3 == 0 else GD)
zet(16, 24, [(1, 14), (22, 14)], P0)
blad.save(os.path.join(K, "slijm_upgrades.png"))

# proef: rust-frame op niveau 0 tot 3, op pruim, op 10x en op ware maat x3 (strook 120 px = schaal 3)
klein = Image.open(os.path.join(K, "slijm.png")).convert("RGBA").crop((0, 0, 16, 16))
groot = Image.open(os.path.join(K, "slijm_groot.png")).convert("RGBA").crop((0, 0, 16, 16))
p = Image.new("RGBA", (4 * 26, 20), (0x3f, 0x28, 0x46, 255))
for n in range(4):
    x0 = n * 26 + 1
    if n >= 3: p.alpha_composite(blad.crop((16, 0, 40, 16)), (x0, 3))
    p.alpha_composite(groot if n >= 1 else klein, (x0 + 4, 3))
    if n >= 2: p.alpha_composite(blad.crop((0, 0, 16, 16)), (x0 + 4, 3))
for s, naam in ((10, "gloop-upgrades-10x.png"), (3, "gloop-upgrades-3x.png")):
    p.resize((p.width * s, p.height * s), Image.NEAREST).save(os.path.join(R, "ontwerp", "steam", "mila", naam))
