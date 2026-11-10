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
VLOER, KIER = (92, 55, 88, 255), (42, 26, 31, 255)   # bovenste vloerrij in het echte spel (GEZIEN, film main 04:25)
def diep(im):
    # run 9 (Daan kan 4: Deep Pit las niet als diep): als hij opengaat snijdt een zwart gat van 3 rijen door de vloer,
    # met paarse wanden; de stekels staan IN het gat (hun voet verdwijnt in het zwart), dus je kijkt erin.
    u = im.copy()
    for f in (1, 2):
        for y in (5, 6, 7):
            for x in range(f * 16, f * 16 + 16):
                wand = x in (f * 16, f * 16 + 15)
                c = u.getpixel((x, y))
                if wand: u.putpixel((x, y), RAND)
                elif y >= 6 or c in (KIER, (42, 26, 31, 255)): u.putpixel((x, y), GAT)
    return u
def truc(im):
    # run 9 (Daan kan 4: het deksel lag als strook naast de put): dicht is hij echt vloer. Rij 5 en 6 doorzichtig
    # (je ziet de muur van de gang erachter), rij 7 in de kleur van de vloer, met alleen twee naden en één haarscheurtje.
    u = im.copy()
    for x in range(16):
        u.putpixel((x, 5), (0, 0, 0, 0)); u.putpixel((x, 6), (0, 0, 0, 0))
        u.putpixel((x, 7), KIER if x in (1, 14) else VLOER)
    u.putpixel((8, 6), (0, 0, 0, 0)); u.putpixel((9, 7), KIER)
    return u
r1 = roestig(bron); r2 = diep(r1); r3 = truc(r2)
blad = Image.new("RGBA", (48, 24), (0, 0, 0, 0))
for i, r in enumerate((r1, r2, r3)): blad.alpha_composite(r, (0, i * 8))
blad.save(os.path.join(K, "stekelput_upgrades.png"))
# proef op de echte gang (uitsnede van de film van main, spelpixels: elke 3 schermpixels 1), 4 rijen: niveau 0 tot 3,
# telkens dicht en open naast elkaar op de plek van de put. 10x en 3x.
film = os.path.join(R, "ontwerp", "steam", "mila", "bron", "gang-uit-film.png")
gang = Image.open(film).convert("RGBA")   # 40 x 12 spelpixels, vloer bovenrand op rij 8
p = Image.new("RGBA", (2 * 42, 4 * 13), (255, 255, 255, 255))
for i, r in enumerate((bron, r1, r2, r3)):
    for j, f in enumerate((0, 2)):
        g = gang.copy(); g.alpha_composite(r.crop((f * 16, 0, f * 16 + 16, 8)), (12, 1))
        p.alpha_composite(g, (j * 42 + 1, i * 13 + 1))
for s_, naam in ((10, "put-upgrades-10x.png"), (3, "put-upgrades-3x.png")):
    p.resize((p.width * s_, p.height * s_), Image.NEAREST).save(os.path.join(R, "ontwerp", "steam", "mila", naam))
