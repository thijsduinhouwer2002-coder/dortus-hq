# Mila 10 nov: stekelput per upgrade-stap. Uit: kunst/stekelput_upgrades.png, 48 x 24: rij n-1 = niveau n, elke rij
# precies dezelfde indeling als stekelput.png (3 beelden van 16 x 8: dicht, half, open). Stappen stapelen.
#   1 Rusty Spikes: stekels roestig (oranjebruin met een lichte punt), om en om een grijze ertussen.
#   2 Deep Pit:     ook roestig; als hij opengaat is de plank weg en zie je een zwart gat met een paars randje.
#   3 Trick Lid:    ook roestig en diep; dicht ziet hij eruit als de aarde van de vloer, met één haarscheurtje.
import os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
K = os.path.join(R, "producten", "steam-hol", "godot", "kunst")
bron = Image.open(os.path.join(K, "stekelput.png")).convert("RGBA")
L5, L6, D2 = (169, 182, 191, 255), (228, 236, 239, 255), (108, 120, 132, 255)
ROEST, ROEST_D, ROEST_P = (0xc0, 0x6a, 0x34, 255), (0x7a, 0x3e, 0x24, 255), (0xf0, 0xc0, 0x8a, 255)
GAT, RAND = (0x08, 0x04, 0x0b, 255), (0x55, 0x33, 0x63, 255)
NACHT, AARDE, AARDE_L, AARDE_D = (29, 20, 38, 255), (63, 40, 70, 255), (82, 54, 90, 255), (43, 29, 53, 255)
def roestig(im):
    u = im.copy()
    for x in range(48):
        grijs = (x // 4) % 2 == 1 and x >= 32   # in het open beeld blijft om en om een grijze stekel
        if grijs: continue
        for y in range(8):
            c = im.getpixel((x, y))
            if c == L5: u.putpixel((x, y), ROEST)
            elif c == D2: u.putpixel((x, y), ROEST_D)
            elif c == L6: u.putpixel((x, y), ROEST_P)
    return u
def diep(im):
    u = im.copy()
    for f in (1, 2):
        for x in range(f * 16 + 1, f * 16 + 15):
            u.putpixel((x, 6), RAND if x in (f * 16 + 1, f * 16 + 14) else GAT)
    return u
def truc(im):
    u = im.copy()
    for x in range(16):
        u.putpixel((x, 5), NACHT); u.putpixel((x, 7), AARDE_D)
        u.putpixel((x, 6), AARDE_L if x in (3, 11) else AARDE)
    u.putpixel((8, 6), NACHT)   # haarscheurtje: wie goed kijkt, ziet hem
    return u
r1 = roestig(bron); r2 = diep(r1); r3 = truc(r2)
blad = Image.new("RGBA", (48, 24), (0, 0, 0, 0))
for i, r in enumerate((r1, r2, r3)): blad.alpha_composite(r, (0, i * 8))
blad.save(os.path.join(K, "stekelput_upgrades.png"))
# proef: 4 rijen (niveau 0 tot 3), op de vloer van het hol, 10x en 3x
p = Image.new("RGBA", (52, 4 * 11), (0x1d, 0x14, 0x26, 255))
for i, r in enumerate((bron, r1, r2, r3)):
    y = i * 11 + 2
    for x in range(52): p.putpixel((x, y + 7), AARDE_D); p.putpixel((x, y + 6), AARDE); p.putpixel((x, y + 5), NACHT)
    p.alpha_composite(r, (2, y))
for s, naam in ((10, "put-upgrades-10x.png"), (3, "put-upgrades-3x.png")):
    p.resize((p.width * s, p.height * s), Image.NEAREST).save(os.path.join(R, "ontwerp", "steam", "mila", naam))
