# Mila: capsules voor de winkelpagina, opgebouwd uit de ECHTE spelplaatjes (godot/kunst), hele schaal, nearest.
# Gebruik: python3 maak_capsules.py [uitmap]
import os, sys, random
from PIL import Image, ImageDraw
HIER = os.path.dirname(os.path.abspath(__file__))
K = os.path.abspath(os.path.join(HIER, "..", "..", "..", "..", "producten", "steam-hol", "godot", "kunst"))
UIT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HIER, "..")
def o(n): return Image.open(os.path.join(K, n)).convert("RGBA")
TEG, GRAS, MAAI, SLIJM, HOED, LIJF, SCHAT, FAKKEL, GLOED, TEK, VERS, VOND, ING, WAP, LIT = [o(n) for n in (
    "tegels.png", "gras.png", "maaiveld.png", "slijm.png", "held_hoeden.png", "held_lijf_kleuren.png", "schat.png",
    "fakkel.png", "gloed.png", "tekens.png", "versiering.png", "vondsten.png", "ingang.png", "held_wapens.png", "held_littekens.png")]
def cel(im, i, w=16, h=16, rij=0): return im.crop((i * w, rij * h, i * w + w, rij * h + h))
HOED_TOP = [2, 0, 2, 3, 1, 0, 0, 0, 2, 0]
HOED_ONDER = [5, 5, 6, 5, 5, 5, 5, 5, 5, 5]
SCHEEF = [0, 1, -1, 1]
DONKER = (0x12, 0x0b, 0x18, 255)

# ---------- letters: eigen pixelletter, 5 breed, 7 hoog ----------
G = {
 "H": ["X...X", "X...X", "X...X", "XXXXX", "X...X", "X...X", "X...X"],
 "A": ["..X..", ".X.X.", "X...X", "X...X", "XXXXX", "X...X", "X...X"],
 "T": ["XXXXX", "..X..", "..X..", "..X..", "..X..", "..X..", "..X.."],
 "S": [".XXXX", "X....", "X....", ".XXX.", "....X", "....X", "XXXX."],
 "O": [".XXX.", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
 "F": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "X...."],
 "E": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "XXXXX"],
 "L": ["X....", "X....", "X....", "X....", "X....", "X....", "XXXXX"],
 "N": ["X...X", "XX..X", "X.X.X", "X..XX", "X...X", "X...X", "X...X"],
 " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
}
def woord(tekst, blok, kleuren, rand=DONKER, gat=1):
    """Pixeltekst met dikke donkere rand en een schaduw eronder. blok = pixels per letterpixel (in spelpixels)."""
    w = sum(5 * blok + gat * blok for _ in tekst) - gat * blok
    h = 7 * blok
    im = Image.new("RGBA", (w + 4, h + 5), (0, 0, 0, 0))
    vul = Image.new("RGBA", im.size, (0, 0, 0, 0))
    x0 = 2
    for ch in tekst:
        g = G[ch]
        for gy, rij in enumerate(g):
            for gx, c in enumerate(rij):
                if c == "X":
                    for by in range(blok):
                        y = gy * blok + by
                        kl = kleuren[min(len(kleuren) - 1, y * len(kleuren) // h)]
                        for bx in range(blok):
                            vul.putpixel((x0 + gx * blok + bx, 2 + y), kl)
        x0 += 6 * blok if gat else 5 * blok
    # rand: elke lege pixel naast vul wordt donker; schaduw 2 rijen onder
    a = vul.split()[3]
    for y in range(im.height):
        for x in range(im.width):
            if a.getpixel((x, y)):
                continue
            buur = any(0 <= x + dx < im.width and 0 <= y + dy < im.height and a.getpixel((x + dx, y + dy))
                       for dx in (-1, 0, 1) for dy in (-1, 0, 1, -2, -3))
            if buur:
                im.putpixel((x, y), rand)
    im.alpha_composite(vul)
    return im
GOUD = [(0xff, 0xe9, 0x9a, 255), (0xff, 0xd2, 0x5c, 255), (0xf2, 0xb2, 0x3a, 255), (0xd9, 0x8a, 0x2a, 255)]
MUNT = [(0xb8, 0xf5, 0xd2, 255), (0x7e, 0xe0, 0xae, 255), (0x4f, 0xc0, 0x8f, 255)]

def logo(blok_groot=2, met_hoeden=True):
    """HATS groot met op elke letter een echte hoed uit het spel; 'OF THE FALLEN' eronder."""
    hats = woord("HATS", blok_groot, GOUD)
    rest = woord("OF THE FALLEN", 1 if blok_groot <= 2 else blok_groot // 2, MUNT)
    w = max(hats.width, rest.width)
    hoog = 9 if met_hoeden else 0
    im = Image.new("RGBA", (w, hoog + hats.height + rest.height - 1), (0, 0, 0, 0))
    hx = (w - hats.width) // 2
    im.alpha_composite(hats, (hx, hoog))
    if met_hoeden:
        # kroon op H, koksmuts op A, pan op T, veermuts op S (de grap: de letters zijn ook opgegeten helden)
        for n, h in enumerate([4, 5, 8, 9]):
            lx = hx + 2 + n * 6 * blok_groot + (5 * blok_groot) // 2 - 8 + [0, 0, 0, 1][n]
            ly = hoog + 2 - HOED_ONDER[h] - 1 + 1 + (1 if n == 1 else 0)
            im.alpha_composite(cel(HOED, h), (lx, ly))
    im.alpha_composite(rest, ((w - rest.width) // 2, hoog + hats.height - 1))
    return im

# ---------- hol ----------
def tegel(open_, x, y, kol, rij):
    def aarde(cx, cy): return not ((cx, cy) in open_)
    if aarde(x, y):
        return cel(TEG, (x * 7 + y * 3) % 8, rij=0)
    i = (aarde(x, y - 1) * 1) + (aarde(x + 1, y) * 2) + (aarde(x, y + 1) * 4) + (aarde(x - 1, y) * 8)
    return cel(TEG, i, rij=1)

def gloop_met_toren(im, gx, vloer, hoeden, frame=0):
    """gx = midden van Gloop, vloer = y van de vloer. Zelfde regels als slijm.gd (toren, 1 px erin, scheef)."""
    im.alpha_composite(cel(SLIJM, frame), (gx - 8, vloer - 16))
    boven = vloer - 16 + 6
    for n, h in enumerate(hoeden[:4]):
        y = boven - HOED_ONDER[h]
        im.alpha_composite(cel(HOED, h), (gx - 8 + SCHEEF[n], y))
        boven = y + HOED_TOP[h]
    return boven

def berg(im, gx, vloer, hoeden):
    """Hoedenberg links van Gloop, zelfde formule als slijm.gd berg()."""
    n = len(hoeden); in_rij = 1
    def past(onder): return sum(onder - r for r in range(min(onder, 6)))
    while past(in_rij) < n: in_rij += 1
    k, rij, br = 0, 0, in_rij
    while k < n and br > 0 and rij < 6:
        for j in range(br):
            if k >= n: break
            h = hoeden[k]; x = -12 - 6 * (in_rij - 1) + 6 * j + 3 * rij
            im.alpha_composite(cel(HOED, h), (gx + x - 8, vloer - 1 - HOED_ONDER[h] - 3 * rij))
            k += 1
        rij += 1; br -= 1

def held(im, x, vloer, kleur, hoed, wapen=None, teken=None, litteken=False, spiegel=False, frame=0):
    l = cel(LIJF, frame, rij=kleur)
    if litteken: l.alpha_composite(cel(LIT, 0))
    l.alpha_composite(cel(HOED, hoed))
    if wapen is not None: l.alpha_composite(cel(WAP, wapen))
    if spiegel: l = l.transpose(Image.FLIP_LEFT_RIGHT)
    im.alpha_composite(l, (x, vloer - 16))
    if teken is not None:
        im.alpha_composite(cel(TEK, teken, 8, 8), (x + 4, vloer - 16 + HOED_TOP[hoed] - 9))

def gloed(im, cx, cy, sterkte=0.55):
    g = GLOED.copy(); a = g.split()[3].point(lambda v: int(v * sterkte)); g.putalpha(a)
    laag = Image.new("RGBA", im.size, (0, 0, 0, 0)); laag.alpha_composite(g, (cx - 26, cy - 26))
    return Image.alpha_composite(im, laag)

def lucht(im, tot):
    d = ImageDraw.Draw(im)
    boven, onder = (0x14, 0x0f, 0x2a), (0x3a, 0x22, 0x4a)
    for y in range(tot):
        t = y / max(1, tot - 1)
        d.line([(0, y), (im.width, y)], fill=tuple(int(boven[i] + (onder[i] - boven[i]) * t) for i in range(3)) + (255,))
    r = random.Random(7)
    for _ in range(im.width * tot // 90):
        x, y = r.randrange(im.width), r.randrange(max(1, tot - 6))
        im.putpixel((x, y), (0xe8, 0xd8, 0xff, 255) if r.random() < .3 else (0x8a, 0x76, 0xb0, 255))

def scene(W, H, grond_y, kamer, items):
    """grond_y: y van het gras. kamer: lijst van open cellen (kolom, rij) in het rooster vanaf grond_y+8."""
    im = Image.new("RGBA", (W, H), (0x1d, 0x14, 0x26, 255))
    lucht(im, grond_y + 8)
    open_ = set(kamer)
    y0 = grond_y + 8
    for ry in range((H - y0) // 16 + 1):
        for kx in range(W // 16 + 1):
            im.alpha_composite(tegel(open_, kx, ry, 0, 0), (kx * 16, y0 + ry * 16))
    for kx in range(W // 16 + 1):
        im.alpha_composite(cel(GRAS, kx % 4, 16, 8), (kx * 16, grond_y))
    for f in items:
        im = f(im) or im
    return im

def schaal(im, s): return im.resize((im.width * s, im.height * s), Image.NEAREST)

# ---------- header 920 x 430 (schaal 6: 154 x 76 spelpixels, boven 20 px weg) ----------
def header():
    W, H, S = 154, 76, 6
    gy = 34
    y0 = gy + 8
    vloer = y0 + 32
    kamer = [(kx, r) for kx in range(0, 10) for r in (0, 1)]
    def dingen(im):
        im = gloed(im, 18, y0 + 10, .45); im.alpha_composite(cel(FAKKEL, 1, 8, 12), (14, y0 + 4))
        im = gloed(im, 140, vloer - 8, .8); im = gloed(im, 120, y0 + 8, .4)
        im.alpha_composite(cel(FAKKEL, 2, 8, 12), (116, y0 + 3))
        im.alpha_composite(cel(SCHAT, 1, 24, 16), (128, vloer - 16))
        berg(im, 104, vloer, [0, 1, 3, 2, 6, 1, 0, 3, 2, 1])            # maat 3: 10 zichtbaar
        gloop_met_toren(im, 110, vloer, [7, 5, 4, 9])                    # hoge hoed, koksmuts, kroon, veermuts
        held(im, 50, vloer, 0, 8, wapen=0, teken=1)                       # held met een pan op, "!"
        held(im, 30, vloer, 2, 3, wapen=1, teken=0, litteken=True)        # terugkomer met wrok
        return im
    im = scene(W, H, gy, kamer, [dingen])
    lg = logo(2)
    im.alpha_composite(lg, (4, 4))
    im.alpha_composite(ING, (100, gy - 6))
    return schaal(im, S).crop((2, 26, 922, 456))

# ---------- klein 462 x 174 (schaal 4: 116 x 44, rand weg) ----------
def klein():
    W, H, S = 116, 44, 4
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    lucht(im, H)
    for kx in range(W // 16 + 1):
        im.alpha_composite(cel(TEG, (kx * 5) % 8, rij=0), (kx * 16, H - 5))
    im = gloed(im, 100, H - 10, .7)
    gloop_met_toren(im, 101, H - 4, [7, 5, 4])
    lg = logo(2, met_hoeden=True)
    im.alpha_composite(lg, (1, (H - lg.height) // 2))
    return schaal(im, S).crop((1, 1, 463, 175))

if __name__ == "__main__":
    os.makedirs(UIT, exist_ok=True)
    h = header(); print("header", h.size); h.convert("RGB").save(os.path.join(UIT, "header-920x430.png"))
    k = klein(); print("klein", k.size); k.convert("RGB").save(os.path.join(UIT, "klein-462x174.png"))
