# Gloop met een eigen trek (Daan, 13 nov 2026, run na ronde 6). Basis: B groot (kijker 8 van 10, "generiek slime-achtig").
# Drie versies voor het blad van Thijs:
#   1 "groot"  : B groot zoals in ronde 6
#   2 "munt"   : een gouden muntje dat in zijn buik zweeft en glimt (hij eet de schat van de helden mee)
#   3 "glas"   : doorzichtige buik met munt, sleuteltje en belletjes (de druppel-versie las niet: zag eruit als een breder lijf)
# Alles pixel voor pixel uit code. Frame 32 x 22 (B groot is 28 x 22, 2 px rand links en rechts voor de druppel).
import os, sys
from PIL import Image
HIER = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HIER)
import maak_gloop as mg
P = mg.P

def basis(staat="rust", wiebel=0):
    g = mg.frame_groot(staat, wiebel)
    im = Image.new("RGBA", (34, 22), (0, 0, 0, 0)); im.paste(g, (2, 0), g)
    return im

def zet(im, punten):
    for x, y, c in punten:
        im.putpixel((x, y), P[c] + (255,))

MUNT = [".ggg.",
        "gwgGg",
        "ggGgg",
        "gGggG",
        ".GGG."]  # met een streepje in het midden (muntteken), zodat hij als munt leest
SLEUTEL = ["III....",  # klein sleuteltje, ring links, baard rechts
           "I.IIIII",
           "III.I.I"]

def stempel_met_gloed(im, patroon, x0, y0):
    # kijker ronde 7: met een lichte ring las de munt als "gat" of "gele vlek". Nu een donkerbruine rand: een voorwerp.
    vol = {(x0 + i, y0 + j) for j, r in enumerate(patroon) for i, c in enumerate(r) if c != "."}
    ring = {(x + dx, y + dy) for x, y in vol for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))} - vol
    for x, y in ring:
        if im.getpixel((x, y))[3] > 0:
            im.putpixel((x, y), (110, 62, 22, 255))
    for j, r in enumerate(patroon):
        for i, c in enumerate(r):
            if c != ".": im.putpixel((x0 + i, y0 + j), P[c] + (255,))

def munt(im):
    # linksonder in de buik, onder het linkerblosje: zijn muntje (hij eet de schat van de helden mee)
    stempel_met_gloed(im, MUNT, 7, 15)
    return im

def glas(im):
    # doorzichtige buik: lichter slijm onder de mond, met een munt, een sleuteltje en twee belletjes erin
    w, h = im.size
    for y in range(15, h - 2):
        for x in range(w):
            if im.getpixel((x, y))[:3] == P["m"]:
                im.putpixel((x, y), P["l"] + (255,))
    stempel_met_gloed(im, MUNT, 7, 15)
    stempel_met_gloed(im, MUNT, 21, 16)  # tweede munt rechts (sleuteltje viel op ware grootte weg tegen de voet)
    for x, y in ((16, 19), (13, 18), (19, 19)):
        if im.getpixel((x, y))[:3] in (P["l"], P["m"]):
            im.putpixel((x, y), P["h"] + (255,))
    return im

def rechterrand(im, y):
    rij = [x for x in range(im.width) if im.getpixel((x, y))[3] > 0]
    return max(rij) if rij else None

def drup(im):
    # een dikke druppel die langs de rechterzij naar beneden loopt en onderaan een plasje maakt
    h = im.height
    # bult naar buiten van rij 9 tot de vloer, 1 px bij 9-10, 2 px vanaf 11
    for y in range(9, h):
        b = rechterrand(im, y)
        if b is None: continue
        uit = 1 if y < 11 else 2
        if y >= h - 2: uit = 4  # plasje
        for x in range(b, b + uit):
            im.putpixel((x, y), P["s" if y < h - 2 else "d"] + (255,))
        im.putpixel((b + uit, y), P["o"] + (255,))
    # glimstip op de druppel en ronde top
    b = rechterrand(im, 13); im.putpixel((b - 2, 13), P["l"] + (255,)); im.putpixel((b - 2, 14), P["l"] + (255,))
    b = rechterrand(im, h - 1); im.putpixel((b, h - 1), (0, 0, 0, 0))
    return im

MAKERS = {"groot": lambda i: i, "munt": munt, "glas": glas}

def strip(naam):
    frames = [MAKERS[naam](basis("rust", w)) for w in range(4)] + [MAKERS[naam](basis("hap")), MAKERS[naam](basis("kauw"))]
    s = Image.new("RGBA", (34 * 6, 22), (0, 0, 0, 0))
    for i, f in enumerate(frames): s.paste(f, (i * 34, 0), f)
    return s

if __name__ == "__main__":
    for n in MAKERS:
        strip(n).save(os.path.join(HIER, f"gloop_{n}.png"))
    print("ok")
