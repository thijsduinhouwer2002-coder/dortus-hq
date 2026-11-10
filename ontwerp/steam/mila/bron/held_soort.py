# Mila 10 nov: kleding per heldensoort, een laag over held_lijf_kleuren.png. kunst/held_soort.png.
# 4 loopframes (zelfde als het lijf) x 4 rijen in de volgorde van heldensoort.gd SOORTEN: ridder, dief, magier, bard.
# Tekenen tussen lijf en littekens, zelfde anker, zelfde frame. Alleen pixels die de laag heeft worden overschreven;
# waar hij leeg is zie je het lijf (zo houden ridder, dief en bard hun eigen tuniekkleur, je herkent Kees nog).
# Gemaakt uit het lijf zelf (kleur voor kleur), dus loopt mee met de wip van frame 1 en 3.
import os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
K = os.path.join(R, "producten", "steam-hol", "godot", "kunst")
lijf = Image.open(os.path.join(K, "held_lijf_kleuren.png")).convert("RGBA")

A = (42, 26, 31, 255)          # omtrek
HUID = (243, 196, 155, 255); KIN = (201, 138, 104, 255); WANG = (232, 133, 122, 255)
OOG_W = (255, 255, 255, 255); OOG_Z = (28, 18, 22, 255)
TUNIEK = {(178, 58, 60, 255), (238, 106, 79, 255)}   # rij 0; andere rijen worden per rij gemeten
BROEK = (61, 104, 196, 255)
# ridder: staal
S_L = (214, 222, 232, 255); S_M = (150, 160, 180, 255); S_D = (88, 94, 118, 255)
# dief: masker en buit
MASKER = (34, 30, 44, 255); ZAK_L = (196, 160, 104, 255); ZAK_D = (140, 104, 62, 255); GOUD = (242, 193, 78, 255)
# magier: mantel en baard
M_L = (104, 124, 226, 255); M_M = (62, 76, 176, 255); M_D = (38, 44, 112, 255)
BAARD = (240, 238, 232, 255); BAARD_D = (186, 184, 196, 255)
# bard: luit
HOUT = (206, 134, 62, 255); HOUT_D = (146, 86, 40, 255); GAT = (60, 34, 24, 255); RIEM = (110, 64, 36, 255)

def frame_info(f, rij):
    px = {}
    for y in range(16):
        for x in range(16):
            p = lijf.getpixel((f * 16 + x, rij * 16 + y))
            if p[3]: px[(x, y)] = p
    top = min(y for (x, y) in px)               # bovenkant hoofd: 4 of 5 (wip)
    dy = top - 4
    # tuniek = alle kleuren in de rompregels die geen huid, omtrek, broek of riem zijn
    romp = {}
    for (x, y), p in px.items():
        if 10 + dy <= y <= 12 + dy and p not in (A, HUID, KIN, BROEK, (74, 53, 36, 255), (110, 78, 48, 255)):
            romp[(x, y)] = p
    return px, dy, romp

def ridder(px, dy, romp, o):
    for (x, y), p in px.items():
        if (x, y) in romp:
            if x in (7, 8) and y <= 11 + dy:   # tabbert in eigen kleur blijft zichtbaar
                continue
            o[(x, y)] = S_L if y == 10 + dy else (S_D if x in (4, 11) or y == 12 + dy else S_M)
        elif p == HUID and y >= 10 + dy:        # handschoenen donker, dan lees je armen en geen plank
            o[(x, y)] = S_D
        elif p in ((74, 53, 36, 255), (110, 78, 48, 255)):
            o[(x, y)] = S_D
        elif p == BROEK:
            o[(x, y)] = S_M if y < 15 else S_D
    # schouderstukken: steken een pixel uit boven de schouder
    o[(4, 10 + dy)] = S_L; o[(11, 10 + dy)] = S_L   # schouderstukken glanzen
    o[(6, 10 + dy)] = S_L; o[(9, 10 + dy)] = S_L     # borstplaat rond: licht boven, donker langs de randen
    # vizierstreep: de wang wordt een stalen randje (hoed blijft eroverheen)
    o[(5, 8 + dy)] = S_M

def dief(px, dy, romp, o):
    for (x, y), p in px.items():
        if y in (6 + dy, 7 + dy) and 5 <= x <= 10 and p not in (OOG_W, OOG_Z):
            o[(x, y)] = MASKER
    o[(4, 6 + dy)] = MASKER; o[(3, 6 + dy)] = A; o[(3, 7 + dy)] = MASKER; o[(2, 8 + dy)] = MASKER   # knoop achter het hoofd, slip waait mee
    # buidel op de rug (links, hij kijkt naar rechts), met een munt die eruit piept
    zak = ["..AA..",
           ".ALLA.",
           "ALGLLA",
           "ALLLDA",
           "ALLDDA",
           ".AAAA."]
    for j, r in enumerate(zak):
        for i, c in enumerate(r):
            if c == ".": continue
            x, y = i, 8 + dy + j
            if (x, y) in px and c == "A" and x >= 3: continue
            o[(x, y)] = {"A": A, "L": ZAK_L, "D": ZAK_D, "G": GOUD}[c]
    o[(4, 9 + dy)] = RIEM

def magier(px, dy, romp, o):
    ys = sorted({y for (x, y) in px})
    voet = ys[-1]
    for (x, y), p in px.items():
        if (x, y) in romp or p in ((74, 53, 36, 255), (110, 78, 48, 255)):
            o[(x, y)] = M_L if y == 10 + dy else (M_D if x in (4, 11) else M_M)
        elif p == BROEK and y < voet:
            o[(x, y)] = M_M
    # mantel dicht tussen de benen: van de eerste tot de laatste omtrekpixel per rij
    for y in range(12 + dy, voet):
        xs = [x for (x, yy) in px if yy == y]
        if not xs: continue
        a, b = min(xs), max(xs)
        for x in range(a + 1, b):
            o[(x, y)] = M_D if y == voet - 1 else M_M
    o[(7, 11 + dy)] = GOUD   # sterretje op de borst
    # baard: van de mond over de kin tot op de borst, punt naar beneden
    for x in range(6, 11): o[(x, 8 + dy)] = BAARD
    for x in range(5, 11): o[(x, 9 + dy)] = BAARD if x > 5 else BAARD_D
    for x in range(6, 10): o[(x, 10 + dy)] = BAARD if x != 6 else BAARD_D
    o[(7, 11 + dy)] = BAARD; o[(8, 11 + dy)] = BAARD_D
    o[(9, 11 + dy)] = GOUD
    o[(8, 12 + dy)] = BAARD_D

def bard(px, dy, romp, o):
    # luit op de rug: hals omhoog links van het hoofd, buik achter de heup
    luit = ["AA....",   # kop met stemknoppen
            "AHA...",
            ".AHA..",
            "..AHA.",
            "..AHA.",
            ".AHHHA",
            "AHHHHHA",
            "AHHGHDA",
            "AHHHHDA",
            ".AHDDA.",
            "..AAA.."]
    for j, r in enumerate(luit):
        for i, c in enumerate(r):
            if c == ".": continue
            x, y = i, 4 + dy + j
            if (x, y) in px and px[(x, y)] != A: continue   # niet over het lijf, alleen erachter
            o[(x, y)] = {"A": A, "H": HOUT, "D": HOUT_D, "G": GAT}[c]
    o[(0, 4 + dy)] = GOUD   # stemknop
    # riem schuin over de borst
    for i, (x, y) in enumerate([(5, 10), (6, 10), (7, 11), (8, 11), (9, 12)]):
        if (x, y + dy) in px: o[(x, y + dy)] = RIEM

SOORT = [ridder, dief, magier, bard]
uit = Image.new("RGBA", (64, 64))
for s, fn in enumerate(SOORT):
    for f in range(4):
        px, dy, romp = frame_info(f, 0)
        o = {}
        fn(px, dy, romp, o)
        for (x, y), p in o.items():
            if 0 <= x < 16 and 0 <= y < 16:
                uit.putpixel((f * 16 + x, s * 16 + y), p)
uit.save(os.path.join(K, "held_soort.png"))

# voorbeeld: per soort 4 frames op 10x, en op ware schaal 3 in alle 5 tuniekkleuren, met hoed en wapen
hoeden = Image.open(os.path.join(K, "held_hoeden.png")).convert("RGBA")
wapens = Image.open(os.path.join(K, "held_wapens.png")).convert("RGBA")
WAPEN = [0, 0, 1, 0]
achter = (0x2b, 0x1d, 0x35, 255)
v = Image.new("RGBA", (16 * 5 + 6, 16 * 5), achter)
for kol in range(5):
    soort = kol - 1
    for rij in range(5):
        cel = lijf.crop((0, rij * 16, 16, rij * 16 + 16))
        if soort >= 0: cel.alpha_composite(uit.crop((0, soort * 16, 16, soort * 16 + 16)))
        h = (rij * 3 + kol) % 10
        cel.alpha_composite(hoeden.crop((h * 16, 0, h * 16 + 16, 16)))
        if soort in (-1, 0, 2): cel.alpha_composite(wapens.crop((WAPEN[max(soort, 0)] * 16 if soort >= 0 else 0, 0, (WAPEN[max(soort, 0)] if soort >= 0 else 0) * 16 + 16, 16)))
        v.alpha_composite(cel, (kol * 16 + (2 if kol else 0) + (kol > 0) * 4, rij * 16))
D = os.path.join(R, "ontwerp", "steam", "mila")
v.resize((v.width * 3, v.height * 3), Image.NEAREST).save(os.path.join(D, "held-soorten-3x.png"))
g = Image.new("RGBA", (64, 64), achter); g.alpha_composite(uit)
l4 = Image.new("RGBA", (64, 64), achter)
for s in range(4):
    for f in range(4):
        c = lijf.crop((f * 16, 0, f * 16 + 16, 16)); c.alpha_composite(uit.crop((f * 16, s * 16, f * 16 + 16, s * 16 + 16)))
        l4.alpha_composite(c, (f * 16, s * 16))
l4.resize((640, 640), Image.NEAREST).save(os.path.join(D, "held-soorten-10x.png"))
