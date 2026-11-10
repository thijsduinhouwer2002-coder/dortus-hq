# Mila 10 nov run 9: Big Gloop 2 spelpixels groter rondom (Sanne toets 9: 1 px was op ware maat niet te zien).
# Getekend, niet geschaald: twee keer "oude omtreklijn wordt slijm, eromheen een nieuwe donkere lijn".
# Omdat hij nu breder is dan 16 krijgt elk frame 20 x 16 (2 lucht links en rechts), Gloop staat op x + 2.
# Oog, tand en mond blijven waar ze waren (2 naar rechts in het bredere frame), alle animaties gelijk.
# Uit (nieuwe namen, zodat de build niet breekt tot Bram de code omzet):
#   kunst/slijm_groot2.png, kunst/slijm_leven_groot2.png   frames 20 x 16, zelfde volgorde
#   kunst/slijm_upgrades2.png  cel 0 (x 0, 20 x 16) glansster, cel 1 (x 20, 28 x 16) cape met gouden gesp
# Bovenkant per frame is 2 hoger dan in slijm.png: RUST_TOP en LEVEN_TOP min 2.
import os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
K = os.path.join(R, "producten", "steam-hol", "godot", "kunst")
D = (28, 18, 22, 255)
RAND = {(28, 18, 22), (42, 26, 31)}
FW = 20

def groei(b, cx, w):
    """Eén keer 1 px groter rondom binnen het frame [cx, cx+w)."""
    u = b.copy(); W, Hh = b.size
    vol = lambda x, y: cx <= x < cx + w and 0 <= y < Hh and b.getpixel((x, y))[3] > 0
    for y in range(Hh):
        for x in range(cx, cx + w):
            if vol(x, y):
                rand = any(not vol(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, -1)))
                if rand and y < Hh - 1 and b.getpixel((x, y))[:3] in RAND:
                    kl = None
                    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1)):
                        if vol(x + dx, y + dy):
                            c = b.getpixel((x + dx, y + dy))
                            if c[:3] not in RAND: kl = c; break
                    u.putpixel((x, y), kl or (47, 143, 122, 255))
            elif any(vol(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1))):
                u.putpixel((x, y), D)
    return u

def groot2(bron):
    b = bron.convert("RGBA"); n = b.width // 16
    u = Image.new("RGBA", (n * FW, 16), (0, 0, 0, 0))
    for i in range(n):
        u.alpha_composite(b.crop((i * 16, 0, i * 16 + 16, 16)), (i * FW + 2, 0))
    for _ in range(2):
        u = Image.merge("RGBA", u.split())  # kopie
        for i in range(n):
            u = groei(u, i * FW, FW)
    return u

for n in ("slijm", "slijm_leven"):
    groot2(Image.open(os.path.join(K, n + ".png"))).save(os.path.join(K, n + "_groot2.png"))

# glansster en cape voor het grotere lijf
G3, W = (230, 255, 244, 255), (255, 255, 255, 255)
P0, P1, P2 = (0x3a, 0x1d, 0x4e, 255), (0x6e, 0x3c, 0x8f, 255), (0x9b, 0x62, 0xbe, 255)
GD, GL = (0xd9, 0x8a, 0x2a, 255), (0xff, 0xd2, 0x5c, 255)
blad = Image.new("RGBA", (68, 16), (0, 0, 0, 0))
def zet(ox, w, pts, kl):
    for x, y in pts:
        if 0 <= x < w and 0 <= y < 16: blad.putpixel((ox + x, y), kl)
# cel 0 (20 breed): ster vrij rechtsboven, los van de omtrek (Daan kan 2). Lijf in rust: x 2..17, top 4.
# Wit hart, lichte armen, groene punten: een glinster en geen plusteken.
G1 = (87, 196, 156, 255)
sx, sy = 17, 2
zet(0, FW, [(sx, sy)], W)
zet(0, FW, [(sx, sy - 1), (sx - 1, sy), (sx + 1, sy), (sx, sy + 1)], G3)
zet(0, FW, [(sx, sy - 2), (sx - 2, sy), (sx + 2, sy), (sx, sy + 2)], G1)
zet(0, FW, [(sx - 3, sy)], G1)
# cel 1 (28 breed): koningsmantel als één stuk (Daan kan 1). Achter hem, vanaf de schouders 2 px breder, onderaan
# uitwaaierend tot de rand van de cel, met een staande kraag van hermelijn (wit met zwarte stipjes) die links en rechts
# boven zijn schouders uitsteekt, en een gouden zoom. Hermelijn is het teken van een koning dat iedereen kent.
lijf = Image.open(os.path.join(K, "slijm_groot2.png")).convert("RGBA").crop((0, 0, FW, 16))
vol = lambda x, y: 0 <= x < FW and 0 <= y < 16 and lijf.getpixel((x, y))[3] > 0
OX = 4
HW, HS = (246, 240, 230, 255), (40, 26, 34, 255)
cape = set()
for y in range(6, 16):
    xs = [x for x in range(FW) if vol(x, y)]
    if not xs: continue
    uit = [2, 2, 2, 2, 2, 3, 3, 4, 4, 5][y - 6]
    for x in range(xs[0] - uit, xs[-1] + uit + 1): cape.add((x + OX, y))
for (x, y) in cape:
    rand = any((x + dx, y + dy) not in cape for dx, dy in ((1, 0), (-1, 0), (0, -1)))
    kl = P0 if rand else (P2 if (x - 1, y) not in cape else P1)
    zet(20, 28, [(x, y)], kl)
for x in range(28):
    if (x, 15) in cape:
        zet(20, 28, [(x, 15)], P0 if ((x - 1, 15) not in cape or (x + 1, 15) not in cape) else (GL if x % 3 == 0 else GD))
# cel 2 (x 48, 20 breed): VOOR Gloop: de bovenzoom van de mantel loopt over zijn schouders en is in het midden
# vastgemaakt met een gouden gesp. Zo zijn de twee flappen links en rechts één mantel (Daan kan 1).
C2 = 48
xs7 = [x for x in range(FW) if vol(x, 7)]
l7, r7 = xs7[0], xs7[-1]
mid = (l7 + r7) // 2
for x in range(l7, r7 + 1):
    zak = 1 if abs(x - mid) <= 3 else 0
    zet(C2, FW, [(x, 6 + zak)], P2 if abs(x - mid) > 1 else P1)
    zet(C2, FW, [(x, 7 + zak)], P0)
zet(C2, FW, [(mid, 6), (mid + 1, 6), (mid, 7), (mid + 1, 7)], GL)
zet(C2, FW, [(mid, 8), (mid + 1, 8)], GD)
zet(C2, FW, [(mid - 1, 7), (mid + 2, 7)], GD)
blad.save(os.path.join(K, "slijm_upgrades2.png"))

# proef: niveau 0 (oud klein), 1, 2, 3 op pruim, 10x en ware maat x3
klein = Image.open(os.path.join(K, "slijm.png")).convert("RGBA").crop((0, 0, 16, 16))
oud1 = Image.open(os.path.join(K, "slijm_groot.png")).convert("RGBA").crop((0, 0, 16, 16))
groot = Image.open(os.path.join(K, "slijm_groot2.png")).convert("RGBA").crop((0, 0, FW, 16))
p = Image.new("RGBA", (5 * 30, 20), (0x3f, 0x28, 0x46, 255))
for n in range(5):
    x0 = n * 30 + 1
    if n == 0: p.alpha_composite(klein, (x0 + 6, 3))
    elif n == 1: p.alpha_composite(oud1, (x0 + 6, 3))
    else:
        if n >= 4: p.alpha_composite(blad.crop((20, 0, 48, 16)), (x0, 3))
        p.alpha_composite(groot, (x0 + 4, 3))
        if n >= 4: p.alpha_composite(blad.crop((48, 0, 68, 16)), (x0 + 4, 3))
        if n >= 3: p.alpha_composite(blad.crop((0, 0, FW, 16)), (x0 + 4, 3))
for s, naam in ((10, "gloop-groot2-10x.png"), (3, "gloop-groot2-3x.png")):
    p.resize((p.width * s, p.height * s), Image.NEAREST).save(os.path.join(R, "ontwerp", "steam", "mila", naam))
