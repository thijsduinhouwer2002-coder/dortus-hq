# Mila: voorbeeld van alle hoeden op een held en op Gloops toren, op de pruimen holwand. Leest alleen de pngs.
import os, sys
from PIL import Image
HIER = os.path.dirname(os.path.abspath(__file__))
K = os.path.abspath(os.path.join(HIER, "..", "..", "..", "..", "producten", "steam-hol", "godot", "kunst"))
def o(n): return Image.open(os.path.join(K, n)).convert("RGBA")
lijf, hoed, hap, tek, slijm = o("held_lijf_kleuren.png"), o("held_hoeden.png"), o("held_hoeden_hap.png"), o("tekens.png"), o("slijm.png")
N = hoed.width // 16
def cel(im, i, w=16, h=16, rij=0): return im.crop((i * w, rij * h, i * w + w, rij * h + h))
def top_onder(i):
    c = cel(hoed, i); ys = [y for y in range(16) for x in range(16) if c.getpixel((x, y))[3]]
    return min(ys), max(ys)
W, H = 16 * (N + 1) + 40, 72
im = Image.new("RGBA", (W, H), (0x1d, 0x14, 0x26, 255))
for x in range(W):
    for y in range(H - 8, H): im.putpixel((x, y), (0x3f, 0x28, 0x46, 255))
vloer = H - 8
for i in range(N):
    kl = i % max(1, lijf.height // 16)
    im.alpha_composite(cel(lijf, 0, rij=kl), (4 + i * 17, vloer - 16))
    im.alpha_composite(cel(hoed, i), (4 + i * 17, vloer - 16))
    im.alpha_composite(cel(hap, i), (4 + i * 17, vloer - 40))
    im.alpha_composite(cel(lijf, 0, rij=kl), (4 + i * 17, vloer - 40 + 0))
    im.alpha_composite(cel(hap, i), (4 + i * 17, vloer - 40))
# tekens boven een paar helden (onderkant 1 lege rij boven de hoed, zoals held.gd)
for i, t in ((0, 0), (5, 0), (7, 2), (9, 1)):
    tp, _ = top_onder(i); im.alpha_composite(cel(tek, t, 8, 8), (4 + i * 17 + 4, vloer - 16 + tp - 1 - 8))
# Gloop met een toren van 4 verschillende hoeden (zelfde regels als slijm.gd: 1 px erin, x 0 +1 -1 +1)
def toren(hs, gx):
    im.alpha_composite(cel(slijm, 0), (gx, vloer - 16))
    boven = vloer - 16 + 6
    for n, h in enumerate(hs):
        t, b = top_onder(h); y = boven - b
        im.alpha_composite(cel(hoed, h), (gx + [0, 1, -1, 1][n], y)); boven = y + t
toren([5, 7, 4, 9], 4 + N * 17 + 2)
for t in range(tek.width // 8): im.alpha_composite(cel(tek, t, 8, 8), (W - 10, 2 + t * 9)) if 2 + t * 9 + 8 <= vloer else None
uit = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HIER, "..", "hoeden-6x.png")
im.resize((W * 6, H * 6), Image.NEAREST).save(uit)
im.resize((W * 3, H * 3), Image.NEAREST).save(uit.replace("6x", "3x"))
print(N, "hoeden", [top_onder(i) for i in range(N)])
