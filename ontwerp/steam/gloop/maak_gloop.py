# Gloop, drie versies voor Thijs (Daan, 13 nov 2026). Alles pixel voor pixel uit code, geen beeldgenerator.
# Frame 20 x 16 spelpixels, anker midden onder (zelfde als slijm_groot2.png), dus later een vervanging zonder codewerk.
# Draai: python3 maak_gloop.py  ->  schrijft gloop_<versie>.png (strip: rust 0-3, hap 4, kauw 5) in deze map.
import math, os
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
FW, FH = 20, 16

# palet: munt op pruim (stijl Mila), omlijning donker groenblauw in plaats van zwart: zachter en schattiger
P = {
    "o": (22, 58, 62), "d": (36, 112, 104), "s": (52, 160, 132), "m": (92, 211, 166),
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
MOND_33 = ["k..k", ".kt."]      # kleine lach met één tandje
MOND_LACH = ["k..k", ".kt."]
MOND_OPEN = [".kkk.", "kkkkk", "krrrk", ".kkk."]
MOND_KAUW = [".kk.", "k..k"]

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
    if versie == "A":    # Druppel: rond en iets hoger, puntje bovenop
        B, H, punt, glas = 14, 13, True, False
    elif versie == "B":  # Mochi: breed en zacht
        B, H, punt, glas = 18, 12, False, False
    else:                # C Gelei: doorzichtig, je ziet wat hij at
        B, H, punt, glas = 16, 13, False, True
    mask = lichaam(B + dw, H + dh, punt)
    pix = kleur_lijf(mask, glas)
    bodem = FH - 1; top = bodem - (H + dh) + 1
    cx = FW // 2
    oy = top + 2
    ox = cx - 3 + 1
    if versie == "C":
        # spullen in de buik, achter het oog getekend
        munt = [(-6, -4, "g"), (-5, -4, "g"), (-7, -3, "g"), (-6, -3, "G"), (-5, -3, "g"), (-4, -3, "g"), (-6, -2, "G"), (-5, -2, "G")]
        zwaard = [(3, -2, "I"), (4, -3, "i"), (5, -4, "i"), (6, -5, "i"), (3, -4, "I"), (4, -2, "I")]
        bel = [(-4, -(H - 4), "u"), (-6, -(H - 7), "u"), (5, -(H - 9), "u")]
        for (dx, dy, c) in munt + zwaard + bel:
            x, y = cx + dx, bodem + dy
            if pix.get((x, y)) in ("m", "l", "s"):
                pix[(x, y)] = c
    if staat in ("rust", "hap"):
        if versie == "B":
            stempel(pix, OOG_WIT, ox - 1, oy)
        else:
            stempel(pix, OOG, ox, oy)
    else:
        stempel(pix, OOG_BLIJ, ox, oy)
    my = oy + 7
    if staat == "hap":
        stempel(pix, MOND_OPEN, cx - 1, my)
    elif staat == "kauw":
        stempel(pix, MOND_KAUW, cx - 1, my)
    else:
        stempel(pix, MOND_33 if versie != "B" else MOND_LACH, cx - 1, my)
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

def strip(versie):
    frames = [frame(versie, "rust", w) for w in range(4)] + [frame(versie, "hap", 0), frame(versie, "kauw", 0)]
    s = Image.new("RGBA", (FW * len(frames), FH), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        s.paste(f, (i * FW, 0))
    return s

if __name__ == "__main__":
    for v in "ABC":
        strip(v).save(os.path.join(HIER, f"gloop_{v}.png"))
    print("klaar")
