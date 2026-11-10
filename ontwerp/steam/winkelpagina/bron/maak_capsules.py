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
HOED_TOP = [0, 0, 2, 3, 2, 0, 0, 0, 2, 0]   # helm 0 sinds de kam (9 nov run 3)
HOED_ONDER = [5, 5, 6, 5, 5, 5, 5, 5, 5, 5]
SCHEEF = [0, 1, -1, 1]
DONKER = (0x12, 0x0b, 0x18, 255)

# ---------- letters: eigen pixelletter, 5 breed, 7 hoog ----------
G = {
 "H": ["X...X", "X...X", "X...X", "XXXXX", "X...X", "X...X", "X...X"],
 "A": [".XXX.", "XX.XX", "X...X", "XXXXX", "X...X", "X...X", "X...X"],   # v4: dicht dak (Daan 1: las als HÄTS)
 "T": ["XXXXX", "..X..", "..X..", "..X..", "..X..", "..X..", "..X.."],
 "S": [".XXX.", "XX..X", "XX...", ".XXX.", "...XX", "X..XX", ".XXX."],   # v5: beide uiteinden krullen om (Daan 3.4: platte bovenkant las als 5)
 "O": [".XXX.", "XX.XX", "X...X", "X...X", "X...X", "XX.XX", ".XXX."],   # v4: dichte hoeken (Daan 10)
 "F": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "X...."],
 "E": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "XXXXX"],
 "L": ["X....", "X....", "X....", "X....", "X....", "X....", "XXXXX"],
 "N": ["X...X", "XX..X", "X.X.X", "X..XX", "X...X", "X...X", "X...X"],
 " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
}
def woord(tekst, blok, kleuren, rand=DONKER, gat=1, binnenrand=None):
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
    # rand: elke lege pixel naast vul wordt donker; schaduw 2 rijen onder.
    # binnenrand (Mila v4): de buitenste rij van de letter zelf wordt een donkerder tint, de bovenste rij een lichtere (reliëf)
    a = vul.split()[3]
    for y in range(im.height):
        for x in range(im.width):
            if a.getpixel((x, y)):
                continue
            buur = any(0 <= x + dx < im.width and 0 <= y + dy < im.height and a.getpixel((x + dx, y + dy))
                       for dx in (-1, 0, 1) for dy in (-1, 0, 1, -2, -3))
            if buur:
                im.putpixel((x, y), rand)
    if blok >= 2 and binnenrand:
        kopie = vul.copy()
        for y in range(vul.height):
            for x in range(vul.width):
                if not a.getpixel((x, y)): continue
                leeg = lambda dx, dy: not (0 <= x + dx < vul.width and 0 <= y + dy < vul.height and a.getpixel((x + dx, y + dy)))
                if leeg(0, -1):
                    kopie.putpixel((x, y), (0xff, 0xf6, 0xd0, 255))
                elif leeg(0, 1) or leeg(1, 0):
                    kopie.putpixel((x, y), binnenrand)
        vul = kopie
    im.alpha_composite(vul)
    return im
GOUD = [(0xff, 0xe9, 0x9a, 255), (0xff, 0xd2, 0x5c, 255), (0xf2, 0xb2, 0x3a, 255), (0xd9, 0x8a, 0x2a, 255)]
MUNT = [(0xb8, 0xf5, 0xd2, 255), (0x7e, 0xe0, 0xae, 255), (0x4f, 0xc0, 0x8f, 255)]

LOGO_HOEDEN = [4, 1, 8, 9]     # kroon op H, puntmuts op A, pan op T, veermuts op S
LOGO_DX = [0, 0, 0, -1]
def logo(blok_groot=2, met_hoeden=True):
    """HATS groot met op elke letter een echte hoed uit het spel; 'OF THE FALLEN' eronder."""
    hats = woord("HATS", blok_groot + 1, GOUD, binnenrand=(0xa8, 0x5a, 0x1e, 255))
    rest = woord("OF THE FALLEN", 1 if blok_groot <= 2 else blok_groot // 2, MUNT)
    w = max(hats.width, rest.width)
    hoog = 10 if met_hoeden else 0
    im = Image.new("RGBA", (w, hoog + hats.height + rest.height - 1), (0, 0, 0, 0))
    hx = (w - hats.width) // 2
    im.alpha_composite(hats, (hx, hoog))
    if met_hoeden:
        # kroon op H, koksmuts op A, pan op T, veermuts op S (de grap: de letters zijn ook opgegeten helden)
        # v5 (Daan keuring 3 punt 4): koksmuts las klein als umlaut, dus de A krijgt de paarse puntmuts (spits op spits,
        # zit vast aan de letter); de veermuts staat midden op de S, niet op het uiteinde (las als 5)
        for n, h in enumerate(LOGO_HOEDEN):
            lx = hx + 2 + n * 6 * (blok_groot + 1) + (5 * (blok_groot + 1)) // 2 - 8 + LOGO_DX[n]
            ly = hoog + 3 - HOED_ONDER[h]   # v4: hoed staat op de letter, zweeft niet (las klein als umlaut)
            im.alpha_composite(cel(HOED, h), (lx, ly))
    im.alpha_composite(rest, ((w - rest.width) // 2, hoog + hats.height - 1))
    return im

def munten(im, x, vloer, zaad=1, n=7):
    """Losse munten naast de kist (Daan 4 en 7): 3 px breed, gouden rand, een glimpixel. Zelfde kleuren als de muntjes in hol.gd."""
    r = random.Random(zaad)
    plekken = [(0, 0), (4, 0), (2, -2), (8, 0), (6, -1), (11, 0), (-4, 0), (14, 0), (9, -3)][:n]
    for dx, dy in plekken:
        cx, cy = x + dx + r.choice([0, 0, 1]), vloer - 2 + dy
        for px, py, kl in ((0, 0, GOUD[3]), (1, 0, GOUD[1]), (2, 0, GOUD[3]), (0, -1, GOUD[2]), (1, -1, GOUD[0]), (2, -1, GOUD[2]), (1, 1, (0x8a, 0x55, 0x22, 255))):
            if 0 <= cx + px < im.width and 0 <= cy + py < im.height:
                im.putpixel((cx + px, cy + py), kl)

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

# ---------- header 920 x 430 v3: close-up op schaal 12 (77 x 36 spelpixels), groot logo op schaal 6 ----------
# v2 verloor naast de toppers (Rusty, Ropuka, Tiny Pasture, Deskrawl): logo en figuren te klein, te donker.
def header():
    W, H, S = 77, 36, 12
    vloer = 34
    im = Image.new("RGBA", (W, H), (0x1d, 0x14, 0x26, 255))
    for kx in range(W // 16 + 1):
        for ry in range(3):
            im.alpha_composite(cel(TEG, 1 if ry == 1 else 0, rij=1), (kx * 16, vloer - 16 * (ry + 1)))
        im.alpha_composite(cel(TEG, (kx * 3) % 8, rij=0), (kx * 16, vloer))
    for gx_, gy_, st in ((62, vloer - 6, 1.0), (50, vloer - 12, .7), (66, vloer - 18, .6), (36, vloer - 8, .35)):
        im = gloed(im, gx_, gy_, st)
    im.alpha_composite(cel(SCHAT, 1, 24, 16), (50, vloer - 16))
    munten(im, 70, vloer, zaad=4, n=2)
    gloop_met_toren(im, 44, vloer, [7, 5, 4, 9])
    held(im, 4, vloer, 0, 3, wapen=0)   # andere hoed dan op de toren (Daan 12)
    im = schaal(im, S)
    lg = schaal(logo(2), 5)
    im.alpha_composite(lg, (4, 0))
    return im.crop((0, 0, 920, 430))

# ---------- klein 462 x 174 (schaal 3: 154 x 58): het logo vult bijna alles, want Steam maakt er 120 x 45 van ----------
def klein():
    W, H, S = 154, 58, 3
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    lucht(im, H)
    for kx in range(W // 16 + 1):
        im.alpha_composite(cel(TEG, (kx * 5) % 8, rij=0), (kx * 16, H - 6))
    im = gloed(im, 136, H - 20, 1.0)
    lg = logo(3, met_hoeden=True)                 # v4: HATS op blok 4, vult ±62% van de breedte (Daan 5)
    im.alpha_composite(lg, (1, (H - lg.height) // 2))
    uit = schaal(im, S)
    g = Image.new("RGBA", (26, 60), (0, 0, 0, 0))
    gloop_met_toren(g, 13, 60, [7, 5, 4, 9])
    g = g.crop(g.getbbox())
    sg = max(1, (174 - 10) // g.height)            # zo groot als de hoogte toelaat (schaal 4 of 5): leest op 120 x 45
    g = schaal(g, sg)
    uit.alpha_composite(g, (462 - g.width - 8, 174 - 6 - g.height))
    return uit

# ---------- schatkamer als losse scene (voor main, staand, library, hero) ----------
def kamer(W, H, vloer, gx, hx, sx, berg_hoeden=(0, 1, 3, 2, 6, 1), toren=(7, 5, 4, 9), wand_rijen=3, held_kleur=0, held_hoed=8, gras_y=None):
    im = Image.new("RGBA", (W, H), (0x1d, 0x14, 0x26, 255))
    for kx in range(W // 16 + 2):
        for ry in range(wand_rijen + 14):
            y = vloer - 16 * (ry + 1)
            if y < -16: break
            im.alpha_composite(cel(TEG, 1 if ry == wand_rijen - 1 else (0 if ry < wand_rijen else (kx * 7 + ry * 3) % 8), rij=1 if ry < wand_rijen else 0), (kx * 16, y))
        for ry in range((H - vloer) // 16 + 1):
            im.alpha_composite(cel(TEG, (kx * 3 + ry * 5) % 8, rij=0), (kx * 16, vloer + ry * 16))
    if gras_y is not None:
        lucht(im, gras_y + 2)
        for kx in range(W // 16 + 1):
            im.alpha_composite(cel(GRAS, kx % 4, 16, 8), (kx * 16, gras_y))
        r = random.Random(3)
        ruimte = (vloer - 16 * wand_rijen) - (gras_y + 8)       # aarde tussen gras en kamer
        for _ in range(W // 30 if ruimte >= 20 else 0):
            x = r.randrange(W - 16); y = r.randrange(gras_y + 9, vloer - 16 * wand_rijen - 17)
            im.alpha_composite(cel(VOND, r.randrange(5)), (x, y))
    im = gloed(im, sx + 10, vloer - 8, .9); im = gloed(im, gx, vloer - 14, .35); im = gloed(im, sx + 16, vloer - 30, .5)
    im.alpha_composite(cel(FAKKEL, 2, 8, 12), (sx + 12, vloer - 34))
    im.alpha_composite(cel(SCHAT, 1, 24, 16), (sx, vloer - 16))
    munten(im, sx + 20, vloer, zaad=sx, n=6)
    berg(im, gx - 1, vloer, list(berg_hoeden))
    gloop_met_toren(im, gx, vloer, list(toren))
    if hx is not None:
        held(im, hx, vloer, held_kleur, held_hoed, wapen=0)
    return im

def main_capsule():   # 1232 x 706: schaal 11 = 112 x 64 (+ rand)
    S = 11; W, H = 113, 65
    im = kamer(W, H, 60, 74, 22, 88, wand_rijen=2, gras_y=14)
    im = schaal(im, S)
    lg = schaal(logo(2), 6)
    im.alpha_composite(lg, ((1232 - lg.width) // 2, 24))
    return im.crop((0, 0, 1232, 706))

def staand():         # 748 x 896: schaal 8 = 94 x 112
    S = 8; W, H = 94, 112
    im = kamer(W, H, 104, 52, 3, 66, wand_rijen=3, gras_y=40)
    im = schaal(im, S)
    lg = schaal(logo(2), 8)
    lg = lg.crop((0, 0, min(lg.width, 748), lg.height)) if lg.width <= 748 else schaal(logo(2), 7)
    im.alpha_composite(lg, ((748 - lg.width) // 2, 24))
    return im.crop((0, 0, 748, 896))

def library():        # 600 x 900: schaal 6 = 100 x 150
    S = 6; W, H = 100, 150
    im = kamer(W, H, 138, 56, 6, 72, wand_rijen=3, gras_y=60)
    im = schaal(im, S)
    lg = schaal(logo(2), 6)
    lg = lg if lg.width <= 600 else schaal(logo(2), 5)
    im.alpha_composite(lg, ((600 - lg.width) // 2, 70))
    return im.crop((0, 0, 600, 900))

def hero():           # 3840 x 1240, geen tekst; Gloops gezicht in het veilige midden (860 x 380 rond het midden)
    # v4: schaal 13 in plaats van 16, want Gloop met toren is 27 spelpixels hoog en past op 16 nooit in 380 px (Daan 6)
    S = 13; W, H = 296, 96; V = 62; G = 148
    im = kamer(W, H, V, G, G - 52, G + 14, berg_hoeden=(0, 1, 3, 2, 6, 1, 0, 3, 2, 1), wand_rijen=2)
    held(im, G - 76, V, 2, 3, wapen=1)
    held(im, G - 112, V, 1, 6, wapen=0)
    im.alpha_composite(cel(VERS, 4), (G - 94, V - 16))
    r = random.Random(5)
    for _ in range(16):
        im.alpha_composite(cel(VOND, r.randrange(5)), (r.randrange(W - 16), r.choice([r.randrange(0, 30), r.randrange(V + 4, H - 14)])))
    return schaal(im, S).crop((0, 0, 3840, 1240))   # v4: 80 px lager dan v3, toren in het veilige vlak (y 430 tot 810)

def logo_los():       # 1280 breed, doorzichtig
    lg = logo(2); s = 1280 // lg.width
    lg = schaal(lg, s)
    uit = Image.new("RGBA", (1280, lg.height + 64), (0, 0, 0, 0)); uit.alpha_composite(lg, ((1280 - lg.width) // 2, 32))
    bb = uit.getbbox()                                  # v5 (Daan kan 7): bijsnijden tot ±16 px lucht boven en onder
    return uit.crop((0, bb[1] - 16, 1280, bb[3] + 16))

# ---------- v5 (Daan keuring 3): close-ups. Gloop met toren is het hoofdbeeld, warm licht van schat en fakkel ----------
import numpy as np
def warm(im, lichten):
    """Zacht warm licht op volle maat (screen), zoals de gloed in het spel maar groter. lichten = [(cx, cy, r, sterkte)]."""
    a = np.asarray(im.convert("RGB")).astype(np.float32) / 255
    yy, xx = np.mgrid[0:im.height, 0:im.width]
    k = np.array((255, 168, 70), np.float32) / 255
    for cx, cy, r, st in lichten:
        m = np.clip(1 - np.hypot(xx - cx, yy - cy) / r, 0, 1) ** 1.6 * st
        a = 1 - (1 - a) * (1 - k * m[..., None])
    uit = Image.fromarray((a * 255).astype(np.uint8)).convert("RGBA")
    uit.putalpha(im.split()[3]); return uit

def dicht(Wp, Hp, vloer, S, licht, dingen, lichten):
    """Kamer van dichtbij: muur tot boven, vloer van aarde. Licht (gloed) op de achtergrond, warm licht sterk op de muur
    en zwak op de figuren, zodat Gloop groen blijft."""
    bg = Image.new("RGBA", (Wp, Hp), (0x1d, 0x14, 0x26, 255))
    for kx in range(Wp // 16 + 2):
        ry = 0
        while vloer - 16 * (ry + 1) > -16:
            bg.alpha_composite(cel(TEG, 1 if ry == 1 else 0, rij=1), (kx * 16, vloer - 16 * (ry + 1))); ry += 1
        for ry in range((Hp - vloer) // 16 + 1):
            bg.alpha_composite(cel(TEG, (kx * 3 + ry * 5) % 8, rij=0), (kx * 16, vloer + ry * 16))
    for cx, cy, st in licht:
        bg = gloed(bg, cx, cy, st)
    fg = Image.new("RGBA", (Wp, Hp), (0, 0, 0, 0))
    for f in dingen:
        f(fg)
    bg = warm(schaal(bg, S), lichten)
    fg = warm(schaal(fg, S), [(cx, cy, r, st * 0.4) for cx, cy, r, st in lichten])
    bg.alpha_composite(fg)
    return bg

def schat(fg, sx, vloer, fakkel=True, n=0):
    if fakkel: fg.alpha_composite(cel(FAKKEL, 2, 8, 12), (sx, vloer - 34))
    fg.alpha_composite(cel(SCHAT, 1, 24, 16), (sx, vloer - 16))
    if n: munten(fg, sx + 22, vloer, zaad=4, n=n)
def schat_licht(sx, vloer, fakkel=True):
    return [(sx + 12, vloer - 6, 1.0), (sx + 10, vloer - 18, .6)] + ([(sx + 4, vloer - 30, .6)] if fakkel else [])

TOREN = [7, 5, 4, 9]
def header_v5():
    # 920 x 430 op schaal 10 (92 x 43): logo links op 24 px marge en ±53% breed, Gloop met toren ±64% hoog
    S, W, H, V, gx, sx = 10, 92, 43, 41, 59, 66
    im = dicht(W, H, V, S, schat_licht(sx, V, False) + [(gx, V - 12, .5)],
               [lambda f: schat(f, sx, V, False, 0), lambda f: gloop_met_toren(f, gx, V, TOREN),
                lambda f: held(f, 35, V, 0, 3, wapen=0)],
               [(780, 380, 640, .8), (560, 300, 300, .35)])
    im.alpha_composite(schaal(logo(2), 6), (24, 0))
    return im.crop((0, 0, 920, 430))

def main_v5():
    # 1232 x 706 op schaal 14 (88 x 51): logo linksboven, Gloop met toren groot (±54% hoog), held komt van links binnen
    S, W, H, V, gx, sx = 14, 88, 51, 48, 53, 62
    im = dicht(W, H, V, S, schat_licht(sx, V) + [(gx, V - 12, .5)],
               [lambda f: schat(f, sx, V, True, 0),
                lambda f: gloop_met_toren(f, gx, V, TOREN), lambda f: held(f, 29, V, 0, 3, wapen=0)],
               [(1000, 620, 860, .8), (720, 500, 380, .35)])
    im.alpha_composite(schaal(logo(2), 7), (40, 24))
    return im.crop((0, 0, 1232, 706))

def staand_v5():
    # 748 x 896 op schaal 13 (58 x 69): logo boven, Gloop met toren groot (±39% hoog) naast zijn schat
    S, W, H, V, gx, sx = 13, 58, 69, 64, 17, 30
    im = dicht(W, H, V, S, schat_licht(sx, V, False) + [(gx, V - 12, .5)],
               [lambda f: schat(f, sx, V, False), lambda f: gloop_met_toren(f, gx, V, TOREN)],
               [(560, 780, 760, .8), (240, 620, 360, .35)])
    lg = schaal(logo(2), 8)
    lg = lg if lg.width <= 700 else schaal(logo(2), 7)
    im.alpha_composite(lg, ((748 - lg.width) // 2, 28))
    return im.crop((0, 0, 748, 896))

def library_v5():
    # 600 x 900 op schaal 20 (30 x 45): een portret. Gloop kijkt je aan met zijn toren (±60% hoog), munten aan zijn voeten,
    # het licht van de schat (buiten beeld rechts) op hem. Naast de toppers is dit het figuur dat je aankijkt (Daan 3.1).
    S, W, H, V, gx = 20, 30, 45, 43, 14
    def voeten(f):
        munten(f, gx + 7, V, zaad=2, n=3)
    im = dicht(W, H, V, S, [(W, V - 6, 1.0), (W - 2, V - 18, .7), (gx, V - 12, .6)],
               [voeten, lambda f: gloop_met_toren(f, gx, V, TOREN)],
               [(600, 800, 760, .85), (300, 640, 380, .35)])
    lg = schaal(logo(2), 6)
    lg = lg if lg.width <= 568 else schaal(logo(2), 5)
    im.alpha_composite(lg, ((600 - lg.width) // 2, 22))
    return im.crop((0, 0, 600, 900))

if __name__ == "__main__":
    os.makedirs(UIT, exist_ok=True)
    h = header_v5(); print("header", h.size); h.convert("RGB").save(os.path.join(UIT, "header-920x430.png"))
    k = klein(); print("klein", k.size); k.convert("RGB").save(os.path.join(UIT, "klein-462x174.png"))
    for naam, f in (("main-1232x706", main_v5), ("staand-748x896", staand_v5), ("library-600x900", library_v5), ("hero-3840x1240", hero)):
        b = f(); print(naam, b.size); b.convert("RGB").save(os.path.join(UIT, naam + ".png"))
    l = logo_los(); print("logo", l.size); l.save(os.path.join(UIT, "logo-1280.png"))
