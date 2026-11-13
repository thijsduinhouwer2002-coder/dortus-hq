# Gloop, drie versies voor Thijs (Daan, 13 nov 2026). Alles pixel voor pixel uit code, geen beeldgenerator.
# Frame 20 x 16 spelpixels, anker midden onder (zelfde als slijm_groot2.png), dus later een vervanging zonder codewerk.
# Draai: python3 maak_gloop.py  ->  schrijft gloop_<versie>.png (strip: rust 0-3, hap 4, kauw 5) in deze map.
import math, os
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
FW, FH = 20, 16

# palet: munt op pruim (stijl Mila), omlijning donker groenblauw in plaats van zwart: zachter en schattiger
P = {
    "o": (18, 52, 58), "d": (36, 112, 104), "s": (52, 160, 132), "m": (92, 211, 166),
    "l": (150, 238, 196), "h": (232, 255, 244), "w": (250, 247, 238), "p": (34, 22, 44),
    "e": (255, 255, 255), "k": (34, 22, 44), "t": (255, 255, 255), "b": (255, 132, 150),
    "r": (232, 86, 110),  # tong
    "g": (255, 205, 80), "G": (196, 130, 40),  # munt in de buik (versie C)
    "i": (170, 176, 196), "I": (110, 114, 136),  # zwaardje in de buik (versie C)
    "u": (196, 250, 224),  # belletje
}

def lichaam(breed, hoog, punt=False):
    """Masker van het lijf: koepel boven, platte voet die iets uitloopt. Geeft set (x, y) in het frame."""
    cx = FW / 2
    bodem = FH - 1
    top = bodem - hoog + 1
    rx = breed / 2
    cy = top + hoog * 0.62
    ry = cy - top
    mask = set()
    for y in range(top, bodem + 1):
        yc = y + 0.5
        if yc < cy:
            f = 1 - ((cy - yc) / ry) ** 2
            hw = rx * math.sqrt(max(f, 0)) if f > 0 else 0
        else:
            hw = rx
        if y == bodem:
            hw = rx - 0.6  # ronde onderhoek
        for x in range(FW):
            if abs(x + 0.5 - cx) <= hw:
                mask.add((x, y))
    if punt:  # druppelpuntje bovenop, iets naar links gebogen
        tx = int(cx) - 1
        for (x, y) in [(tx, top - 1), (tx, top - 2), (tx - 1, top - 3)]:
            mask.add((x, y))
    return mask

def kleur_lijf(mask, glas=False):
    pix = {}
    xs = [x for x, y in mask]; ys = [y for x, y in mask]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    for (x, y) in mask:
        rand = any((x + dx, y + dy) not in mask for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        if rand:
            pix[(x, y)] = "o"; continue
        fy = (y - y0) / max(1, y1 - y0); fx = (x - x0) / max(1, x1 - x0)
        if y >= y1 - 1:
            c = "d"
        elif y >= y1 - 2 or fx > 0.86:
            c = "s"
        else:
            c = "m"
        if glas and c == "m" and fy > 0.35:
            c = "l"  # glazig: licht binnenin, rand donkerder
        pix[(x, y)] = c
    # glans linksboven: een boogje van drie en een stip
    top = min(y for x, y in mask if x == x0 + 3) if any(x == x0 + 3 for x, y in mask) else y0
    for (x, y, c) in [(x0 + 2, top + 2, "l"), (x0 + 3, top + 1, "h"), (x0 + 4, top + 1, "l"), (x0 + 2, top + 3, "h")]:
        if pix.get((x, y)) in ("m", "l"):
            pix[(x, y)] = c
    return pix

OOG = [  # kraaloog: groot donker ovaal met twee glimlichtjes (groot linksboven, klein rechtsonder), zoals een knuffel
    ".kkkk.",
    "kkkkkk",
    "keekkk",
    "keekkk",
    "kkkkek",
    "kkkkkk",
    ".kkkk.",
]
OOG_WIT = [  # groot wit oog, pupil naar rechts met één glimlicht (Gloop kijkt naar rechts)
    "........",
    ".wwwwww.",
    "wwwkkkkw",
    "wwkekkkw",
    "wwkkkkkw",
    "wwwkkkkw",
    ".wwwwww.",
]
OOG_BLIJ = [  # dichtgeknepen van plezier ^
    "......",
    "......",
    "..kk..",
    ".k..k.",
    "k....k",
    "......",
    "......",
]
# Ronde 2 (na de frisse kijkers): elk oog krijgt een donkere rand en wit, en elke versie een duidelijke open lach.
OOG_PIXAR = [  # A: wit oog met hoge pupil iets naar rechts, glimlicht linksboven
    "..kkk..",
    ".kwwwk.",
    "kwwekwk",
    "kwwkkwk",
    ".kwwwk.",
    "..kkk..",
]
OOG_LOOM = [  # B: tevreden half dicht, het ooglid in lijfkleur
    "..kkk..",
    "kkkkkkk",
    "kwwekwk",
    "kwwkkwk",
    ".kwwwk.",
    "..kkk..",
]
OOG_KRAAL = [  # C: kraaloog met groot glimlicht en een witte onderrand
    "..kkk..",
    ".kkkkk.",
    "kkeekkk",
    "kkkkkek",
    ".kwwwk.",
    "..kkk..",
]
OOG_GROOT = [  # B groot: zelfde oog als A, maar 9 breed, pupil 3 breed met glimlicht van 1 x 2
    "..kkkkk..",
    ".kwwwwwk.",
    "kwwwekkwk",
    "kwwwekkwk",
    "kwwwkkkwk",
    "kwwwkkkwk",
    ".kwwwwwk.",
    "..kkkkk..",
]
OOG_BLIJ_GROOT = [
    ".........",
    ".........",
    "...kkk...",
    "..k...k..",
    ".k.....k.",
    "k.......k",
    ".........",
    ".........",
]
MOND_GROOT = ["kktkkk", ".krrk.", "..kk.."]
MOND_OPEN_GROOT = [".kkkk.", "kkkkkk", "krrrrk", "krrrrk", ".kkkk."]
MOND_KAUW_GROOT = ["k.kk.k", ".k..k."]
MOND_LACH = ["ktkkk", ".krk."]   # open lach met tong en één tandje
MOND_KLEIN = ["k...k", ".kkk."]
MOND_OPEN = ["kkkkk", "krrrk", "krrrk", ".kkk."]
MOND_KAUW = ["k.k.k", ".k.k."]

def stempel(pix, patroon, x0, y0, mask=None):
    for j, rij in enumerate(patroon):
        for i, c in enumerate(rij):
            if c != ".":
                pix[(x0 + i, y0 + j)] = c

def frame(versie, staat, wiebel):
    # wiebel 0..3: 0 rust, 1 iets platter en breder, 2 rust, 3 iets hoger
    dw, dh = [(0, 0), (1, -1), (0, 0), (-1, 1)][wiebel]
    if staat == "hap":
        dw, dh = -1, 1
    if staat == "kauw":
        dw, dh = 2, -1
    if versie == "B":
        return frame_groot(staat, wiebel)
    if versie == "A":    # Druppel: hoog en rond, open blik
        B, H, glas, oog, mond = 14, 14, False, OOG_PIXAR, MOND_LACH
    elif versie == "B":  # Mochi: breed en zacht, tevreden half dicht
        B, H, glas, oog, mond = 18, 13, False, OOG_LOOM, MOND_KLEIN
    else:                # C Gelei: glazig, zelfde oog als A (kraaloog las als "twee ogen")
        B, H, glas, oog, mond = 16, 14, True, OOG_PIXAR, MOND_LACH
    H2 = min(H + dh, 15)
    mask = lichaam(B + dw, H2, False)
    pix = kleur_lijf(mask, glas)
    bodem = FH - 1; top = bodem - H2 + 1
    cx = FW // 2
    oy = top + 2
    ox = cx - 3 + 1
    if versie == "C":
        for (dx, dy, c) in [(-5, 4, "u"), (-4, 4, "u"), (-5, 5, "u"), (5, 9, "u")]:
            x, y = cx + dx, top + dy
            if pix.get((x, y)) in ("m", "l", "s"):
                pix[(x, y)] = c
    if staat in ("rust", "hap"):
        stempel(pix, oog, ox, oy)
    else:
        stempel(pix, OOG_BLIJ, ox, oy)
    my = oy + 7
    if staat == "hap":
        stempel(pix, MOND_OPEN, cx - 1, my - 1)
    elif staat == "kauw":
        stempel(pix, MOND_KAUW, cx - 1, my)
    else:
        stempel(pix, mond, cx - 1, my)
    # blosjes: twee pixels breed, links en rechts van het oog, op de onderste ooghoogte
    by = oy + 6
    for bx in (ox - 3, ox + 7):
        for x in (bx, bx + 1):
            if pix.get((x, by)) in ("m", "l", "s"):
                pix[(x, by)] = "b"
    im = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
    for (x, y), c in pix.items():
        if 0 <= x < FW and 0 <= y < FH:
            im.putpixel((x, y), P[c] + (255,))
    return im

def frame_groot(staat, wiebel):
    """B groot: frame 28 x 22, lijf 24 x 19 (ronde 2: op ware grootte las het gezicht niet, Ropuka is daar ±100 px hoog)."""
    global FW, FH
    oud = (FW, FH); FW, FH = 28, 22
    try:
        dw, dh = [(0, 0), (1, -1), (0, 0), (-1, 1)][wiebel]
        if staat == "hap": dw, dh = -1, 1
        if staat == "kauw": dw, dh = 2, -1
        H2 = 19 + dh
        mask = lichaam(24 + dw, H2, False)
        pix = kleur_lijf(mask, False)
        bodem = FH - 1; top = bodem - H2 + 1; cx = FW // 2
        oy = top + 3; ox = cx - 4 + 1
        stempel(pix, OOG_GROOT if staat != "kauw" else OOG_BLIJ_GROOT, ox, oy)
        my = oy + 9
        if staat == "hap": stempel(pix, MOND_OPEN_GROOT, cx - 2, my - 1)
        elif staat == "kauw": stempel(pix, MOND_KAUW_GROOT, cx - 2, my)
        else: stempel(pix, MOND_GROOT, cx - 2, my)
        by = oy + 7
        for bx in (ox - 4, ox + 10):
            for x in (bx, bx + 1, bx + 2):
                if pix.get((x, by)) in ("m", "l", "s"):
                    pix[(x, by)] = "b"
        im = Image.new("RGBA", (FW, FH), (0, 0, 0, 0))
        for (x, y), c in pix.items():
            if 0 <= x < FW and 0 <= y < FH:
                im.putpixel((x, y), P[c] + (255,))
        return im
    finally:
        FW, FH = oud

def strip(versie):
    frames = [frame(versie, "rust", w) for w in range(4)] + [frame(versie, "hap", 0), frame(versie, "kauw", 0)]
    fw, fh = frames[0].size
    s = Image.new("RGBA", (fw * len(frames), fh), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        s.paste(f, (i * fw, 0))
    return s

if __name__ == "__main__":
    for v in "ABC":
        strip(v).save(os.path.join(HIER, f"gloop_{v}.png"))
    print("klaar")
