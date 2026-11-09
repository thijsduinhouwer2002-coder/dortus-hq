# Daan: tekent de pixelkunst van Het Hol in code (geen beeldgenerator).
# Uitvoer: producten/steam-hol/godot/kunst/*.png en kunst.json, plus voorbeeldbeelden in ontwerp/steam/kunst-bron/.
# Maat: cellen van 16 x 16 spelpixels, schaal 3 op 100% Windows (strook 120 px = 40 spelpixels: maaiveld 8 + twee rijen).
import json, os, random
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
UIT = os.path.join(REPO, "producten", "steam-hol", "godot", "kunst")
os.makedirs(UIT, exist_ok=True)

def hx(s):
    s = s.lstrip("#"); return tuple(int(s[i:i+2], 16) for i in (0, 2, 4)) + (255,)

# Vast palet: warm, aards, met goud en mos als accent. Omlijning is donker bruinpaars, nooit zwart.
P = {
    ".": (0, 0, 0, 0),
    "k": hx("2a1a1f"),   # omlijning
    "K": hx("432a2c"),   # zachte omlijning
    # aarde
    "1": hx("261a30"), "2": hx("3f2846"), "3": hx("5c3758"), "4": hx("7d4a68"), "5": hx("a46577"),
    # holwand (achter de gang)
    "w": hx("1d1426"), "W": hx("2b1d35"), "v": hx("3e2a47"), "V": hx("503856"),
    # steen
    "7": hx("5d5552"), "8": hx("847a72"), "9": hx("aca196"),
    # gras en mos
    "g": hx("2f5e34"), "G": hx("4c8a3c"), "h": hx("7cb84a"), "H": hx("b4dc6a"),
    # goud
    "o": hx("8a4f17"), "O": hx("c27f1f"), "y": hx("f0b43c"), "Y": hx("ffe07a"), "*": hx("fffbe0"),
    # slijm
    "m": hx("1f5c56"), "M": hx("2f8f7a"), "n": hx("57c49c"), "N": hx("a6f0cc"), "q": hx("e6fff4"),
    # huid
    "s": hx("f3c49b"), "S": hx("c98a68"), "p": hx("e8857a"),
    # kleren
    "r": hx("b23a3c"), "R": hx("ee6a4f"), "b": hx("3d68c4"), "B": hx("6f9ff0"),
    "l": hx("4a3524"), "L": hx("6e4e30"),
    # metaal en hout
    "i": hx("6c7884"), "I": hx("a9b6bf"), "j": hx("e4ecef"),
    "u": hx("5c3a22"), "U": hx("8a5b33"),
    # vuur
    "f": hx("d2522b"), "F": hx("ff9a3c"), "x": hx("ffd65e"),
    # oog
    "e": hx("1c1216"), "E": hx("ffffff"),
    # paars (tovenaar)
    "z": hx("4b2f6e"), "Z": hx("7a52b0"),
}

def sprite(rows):
    h = len(rows); w = max(len(r) for r in rows)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            if c != ".": im.putpixel((x, y), P[c])
    return im

def strip(frames):
    w, h = frames[0].size
    im = Image.new("RGBA", (w * len(frames), h), (0, 0, 0, 0))
    for i, f in enumerate(frames): im.paste(f, (i * w, 0), f)
    return im

def opslaan(im, naam):
    im.save(os.path.join(UIT, naam))

CEL = 16
OPP = 8    # hoogte van het maaiveld (gras) boven de eerste aardelaag

# ---------- aarde en gangen (autotegel, 16 varianten op 4 buren) ----------
def aarde_cel(rnd, im, ox, oy):
    for y in range(CEL):
        for x in range(CEL):
            im.putpixel((ox + x, oy + y), P["3"])
    # kluiten: blobje met licht linksboven en schaduw rechtsonder
    for _ in range(rnd.randint(3, 5)):
        x, y = rnd.randint(0, 12), rnd.randint(0, 12); w, h = rnd.randint(2, 4), rnd.randint(2, 3)
        for yy in range(h):
            for xx in range(w):
                c = "4" if (yy == 0 or xx == 0) else "3"
                im.putpixel((ox + (x + xx) % CEL, oy + (y + yy) % CEL), P[c])
        for xx in range(w): im.putpixel((ox + (x + xx) % CEL, oy + (y + h) % CEL), P["2"])
        im.putpixel((ox + (x + w) % CEL, oy + (y + h) % CEL), P["2"])
    for _ in range(rnd.randint(2, 4)):
        im.putpixel((ox + rnd.randint(0, 15), oy + rnd.randint(0, 15)), P["2"])
    k = rnd.random()
    if k < 0.40:
        x, y = rnd.randint(2, 10), rnd.randint(2, 10)
        steen = [".kkk.", "k898k", "k8887k", ".k77k", "..kk."] if rnd.random() < 0.5 else [".kk.", "k98k", "k87k", ".kk."]
        for yy, r in enumerate(steen):
            for xx, c in enumerate(r):
                if c != "." and x + xx < 16 and y + yy < 16: im.putpixel((ox + x + xx, oy + y + yy), P[c if c != "k" else "1"])
    elif k < 0.44:   # botje (zeldzaam)
        x, y = rnd.randint(2, 9), rnd.randint(3, 11)
        for xx, c in enumerate("jIIIIj"): im.putpixel((ox + x + xx, oy + y), P[c])
        for dx in (0, 5):
            im.putpixel((ox + x + dx, oy + y - 1), P["j"]); im.putpixel((ox + x + dx, oy + y + 1), P["I"])
    elif k < 0.47:   # kristalletje
        x, y = rnd.randint(3, 11), rnd.randint(3, 10)
        for yy, r in enumerate([".N.", "NqM", "nNM", ".m."]):
            for xx, c in enumerate(r):
                if c != ".": im.putpixel((ox + x + xx, oy + y + yy), P[c])
    if rnd.random() < 0.3:   # worteltje
        x = rnd.randint(2, 13); y = rnd.randint(0, 6)
        for i in range(rnd.randint(3, 6)):
            im.putpixel((ox + x, oy + y + i), P["u"])
            if rnd.random() < 0.4: x = max(1, min(14, x + rnd.choice((-1, 1))))

def gang_cel(rnd, im, ox, oy, n, e, s, w):
    """n,e,s,w = True als de buur aarde is (dan komt er een rand)."""
    for y in range(CEL):
        for x in range(CEL):
            im.putpixel((ox + x, oy + y), P["W"])
    # gestapelde stenen in de achterwand (metselwerk, rij van 5 hoog)
    for ry, y0 in enumerate((0, 5, 10)):
        off = (ry * 4) % 8
        for x in range(CEL):
            if (x + off) % 8 == 0:
                for y in range(y0, min(y0 + 5, CEL)): im.putpixel((ox + x, oy + y), P["w"])
            else:
                im.putpixel((ox + x, oy + min(y0 + 4, 15)), P["w"])
                if (x + off) % 8 in (1, 2, 3): im.putpixel((ox + x, oy + y0), P["v"])
    for _ in range(rnd.randint(0, 2)):   # mosplekje
        x, y = rnd.randint(1, 12), rnd.randint(2, 11)
        for dx, dy, c in ((0, 0, "g"), (1, 0, "G"), (2, 0, "g"), (1, -1, "G"), (1, 1, "g")):
            im.putpixel((ox + x + dx, oy + y + dy), P[c])
    if rnd.random() < 0.4:                # scheurtje
        x, y = rnd.randint(2, 13), rnd.randint(2, 6)
        for i in range(rnd.randint(3, 6)):
            im.putpixel((ox + x, oy + y + i), P["w"]); x += rnd.choice((-1, 0, 1)); x = max(1, min(14, x))
    if n:   # plafond: aarderand, schaduw, hangende worteltjes
        for x in range(CEL):
            im.putpixel((ox + x, oy), P["2"]); im.putpixel((ox + x, oy + 1), P["1"])
            if rnd.random() < 0.5: im.putpixel((ox + x, oy + 2), P["k"])
        for _ in range(rnd.randint(1, 2)):
            x = rnd.randint(1, 14)
            for i in range(rnd.randint(2, 4)): im.putpixel((ox + x, oy + 1 + i), P["u"])
    if s:   # vloer: aangestampte aarde met mos
        for x in range(CEL):
            im.putpixel((ox + x, oy + 15), P["2"]); im.putpixel((ox + x, oy + 14), P["4"])
            im.putpixel((ox + x, oy + 13), P["3"] if rnd.random() < 0.8 else P["4"])
            if rnd.random() < 0.18: im.putpixel((ox + x, oy + 12), P["G"])
    if w:
        for y in range(CEL):
            im.putpixel((ox, oy + y), P["2"]); im.putpixel((ox + 1, oy + y), P["1"])
    if e:
        for y in range(CEL):
            im.putpixel((ox + 15, oy + y), P["2"]); im.putpixel((ox + 14, oy + y), P["1"])

def maak_tegels():
    # rij 0: 8 aardevarianten; rij 1: 16 gangvarianten (index = n*1 + e*2 + s*4 + w*8)
    im = Image.new("RGBA", (CEL * 16, CEL * 2), (0, 0, 0, 0))
    for i in range(8): aarde_cel(random.Random(10 + i), im, i * CEL, 0)
    for m in range(16):
        gang_cel(random.Random(100 + m), im, m * CEL, CEL, bool(m & 1), bool(m & 2), bool(m & 4), bool(m & 8))
    opslaan(im, "tegels.png")
    return im

# ---------- maaiveld ----------
def maak_gras():
    # 4 varianten van 16 x 8: lucht doorzichtig, dichte grasrand met sprieten, bovenste aarde
    im = Image.new("RGBA", (CEL * 4, OPP), (0, 0, 0, 0))
    for v in range(4):
        rnd = random.Random(200 + v); ox = v * CEL
        for x in range(CEL):
            top = 4
            for y in range(top, OPP):
                c = "G" if y < top + 2 else ("g" if y < top + 3 else ("2" if y < top + 4 else "3"))
                im.putpixel((ox + x, y), P[c])
            if rnd.random() < 0.5: im.putpixel((ox + x, top + 2), P["G"])
            hgt = rnd.choice((1, 1, 2, 2, 3, 4))
            for i in range(1, hgt + 1): im.putpixel((ox + x, top - i + 1), P["h" if i == hgt else "G"])
            if rnd.random() < 0.3: im.putpixel((ox + x, top - hgt), P["H"])
    opslaan(im, "gras.png")
    return im

BOVEN = {   # versiering op het maaiveld; getekend op 16 x 12, opgeslagen als 16 x 8 (rij 2 tot 10)
    "bloemen": ["................", "...*......p.....", "..*Y*....pRp....", "...*......p.....", "...G...Y..G..*..", "...G..YxY.G.*Y*.", "..hG...G..G..G..", "..GG...G.GG..G..", "................", "................", "................", "................"],
    "struik": ["................", "................", "......kkkk......", "....kkhhGGkk....", "...khHhGGGGGk...", "..khhGGGGgGGGk..", "..kGGGRGGGgRGk..", "..kgGGGGgGGGgk..", "...kkgggggggk...", "................", "................", "................"],
    "steen": ["................"]*4 + [".....kkkk.......", "....k9988k......", "...k998887k.....", "...k888777k.....", "....kkkkkk......", "................", "................", "................"],
    "bordje": ["................", "..kkkkkkkkkkk...", "..kUUUUUUUUUk...", "..kUkUkUkkUUk...", "..kUkkkUkUkUk...", "..kUkUkUkkUUk...", "..kuuuuuuuuuk...", "..kkkkkukkkkk...", "......kuk.......", "......kuk.......", "................", "................"],
    "paddo": ["................"]*3 + ["....kkkk........", "...kRjRRk.......", "..kRRRRjRk......", "..kkkkkkkk......", "....kssk........", "....kssk........", "................", "................", "................"],
}
def maak_boven():
    # 16 x 8: de grasrand valt op rij 5 en 6, net als in gras.png
    frames = [sprite(BOVEN[n][2:10]) for n in BOVEN]
    opslaan(strip(frames), "maaiveld.png"); return dict(zip(BOVEN, frames))

# ---------- ingang: houten poortje met bordje ----------
INGANG = [
    "......kkkkkkkk......",
    ".....kUUUUUUUUk.....",
    "....kUuUUUUUUuUk....",
    "....kukkkkkkkkuk....",
    "....kuk......kuk....",
    "....kUk......kUk....",
    ".kkkkUk......kUk....",
    "kUUUUUUk.....kUk....",
    "kUyyyUUk.....kUk....",
    "kUyUyUUk.....kUk....",
    "kUUUUUUk.....kUk....",
    ".kkkuk.k.....kuk....",
    "....kuk......kuk....",
    "....kuk......kuk....",
]

# ---------- fakkel, 4 frames, 8 x 12 ----------
def maak_fakkel():
    vlam = [
        ["...x....", "..xFx...", "..FxF...", ".fFxFf..", "..fFf..."],
        ["....x...", "...xF...", "..FxFf..", ".fFxxf..", "..fFf..."],
        ["...x....", "..Fx....", "..FxF...", ".fFxFf..", "..fff..."],
        ["..x.....", "..xF....", ".fFxF...", ".fFxFf..", "..fFf..."],
    ]
    stok = ["..kUk...", "..kuk...", ".kiIik..", "..kuk...", "..kuk...", "..kuk...", "...k...."]
    frames = [sprite(v + stok) for v in vlam]
    im = strip(frames); opslaan(im, "fakkel.png"); return frames

# ---------- schat: berg munten met kist, 24 x 16, 4 frames glinstering ----------
SCHAT = [
    "........................",
    "........................",
    "........kkkkkkkk........",
    ".......kUUUUUUUUk.......",
    "......kUuuuuuuuuUk......",
    "......kkkkkkkkkkkk......",
    "......kUUUkyykUUUk......",
    "...kk.kuuukYykuuuk.kk...",
    "..kYyk.kkkkkkkkkk.kyYk..",
    ".kyYyykkYyyYyyyYkkyyYyk.",
    "kyYyyOyYyyOyyYyyOyyyYyyk",
    "kOyyYyyyOyyYyOyyyyYyyOyk",
    "kooOyyOyyyOyyyyOyyOyOook",
    ".kkooOooOooOooOooOoookk.",
    "...kkkkkkkkkkkkkkkkkk...",
    "........................",
]

def maak_schat():
    basis = sprite(SCHAT)
    glans = [(3, 9), (11, 9), (19, 10), (8, 11)]
    frames = []
    for i in range(4):
        f = basis.copy()
        x, y = glans[i]
        for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
            f.putpixel((x + dx, y + dy), P["*"])
        frames.append(f)
    opslaan(strip(frames), "schat.png"); return frames

# ---------- slijm, 16 x 16: 4 frames rust (zachte wiebel), 2 frames hap ----------
SLIJM_RUST = [
    [
        "................", "................", "................", "................",
        "................", "................", ".....kkkkkk.....", "....kNNnnnnk....",
        "...kNqNnnnnnk...", "...knnEenEennk..", "..knnneenneenk..", "..knnnnnnnnnnk..",
        "..knMnnppnnnMk..", "..kMMnnnnnnMMk..", "...kMMMMMMMMk...", "....kkkkkkkk....",
    ],
    [
        "................", "................", "................", "................",
        "................", "................", "................", ".....kkkkkk.....",
        "...kkNNnnnnkk...", "..kNqnEennEenk..", "..knnneenneennk.", ".knnnnnnnnnnnnk.",
        ".knMnnnppnnnMnk.", ".kMMnnnnnnnnMMk.", "..kMMMMMMMMMMk..", "...kkkkkkkkkk...",
    ],
]

def maak_slijm():
    a, b = sprite(SLIJM_RUST[0]), sprite(SLIJM_RUST[1])
    # knipper: ogen dicht in frame 4
    c = sprite([r.replace("E", "n").replace("ee", "kk") if i in (9, 10) else r for i, r in enumerate(SLIJM_RUST[0])])
    hap = sprite([
        "................", "................", "................", ".....kkkkkk.....",
        "....kNNnnnnk....", "...kNqNnnnnnk...", "...knEennEennk..", "..knneenneennk..",
        "..knkkkkkkkkk...", "..knkRRRRRRk....", "..knkkkkkkkkk...", "..knnnnnnnnnnk..",
        "..knMnnnnnnnMk..", "..kMMnnnnnnMMk..", "...kMMMMMMMMk...", "....kkkkkkkk....",
    ])
    frames = [a, b, a, c, hap, b]
    opslaan(strip(frames), "slijm.png"); return frames

# ---------- stekelput, 16 x 8 vloerval: frame 0 dicht, 1 half, 2 open ----------
def maak_val():
    dicht = ["................", "................", "................", "................",
             "................", "kkkkkkkkkkkkkkkk", "ULuULuULuULuULuU", "kkkkkkkkkkkkkkkk"]
    half = ["................", "................", "................", "...j...j...j....",
            "..kIk.kIk.kIk.k.", "kkiIikiIikiIikkk", "ULuULuULuULuULuU", "kkkkkkkkkkkkkkkk"]
    open_ = ["..j...j...j...j.", ".kIk.kIk.kIk.kI.", ".kIk.kIk.kIk.kI.", "kiIkkiIkkiIkkiIk",
             "kiIikiIikiIikiIk", "kkiikkiikkiikkik", "ULuULuULuULuULuU", "kkkkkkkkkkkkkkkk"]
    frames = [sprite(dicht), sprite(half), sprite(open_)]
    opslaan(strip(frames), "stekelput.png"); return frames

# ---------- held: los lijf, hoed en wapen (16 x 16, voeten op y 15, kijkt naar rechts) ----------
LIJF_BOVEN = [
    "................", "................", "................", "................",
    ".....kkkkkk.....", "....ksssssSk....", "....ksssEesk....", "....ksssEEsk....",
    "....kpsssssk....", ".....kSSSSk.....",
]
LIJF_ROMP = [
    "....krRRRRrk....", "...ksrRRRRrsk...", "....klLLLLlk....",
]
BENEN = [
    ["....kbk..kbk....", "....kbk..kbk....", "....kkk..kkk...."],
    ["...kbk....kbk...", "...kbk....kbk...", "..kkk......kkk.."],
    ["....kbk..kbk....", "....kbk..kbk....", "....kkk..kkk...."],
    [".....kbkkbk.....", ".....kbkkbk.....", ".....kkk.kkk...."],
]

def lijf(fr, bob):
    rows = LIJF_BOVEN + LIJF_ROMP + BENEN[fr]
    im = sprite(rows)
    if bob:   # op en neer bij het lopen
        n = Image.new("RGBA", im.size, (0, 0, 0, 0)); n.paste(im.crop((0, 0, 16, 13)), (0, 1)); n.paste(im.crop((0, 13, 16, 16)), (0, 13))
        im = n
    return im

HOEDEN = {
    "helm": ["................", "................", "......kkkk......", "....kkIjjIkk....", "...kiIIIIIIIk...", "...kkkkkkkkkk...", "................"],
    "puntmuts": ["........kk......", ".......kZZk.....", "......kZzZk.....", ".....kZZzZZk....", "....kZZZZzZZk...", "...kkYkkkkkkkk..", "................"],
    "kap": ["................", "................", "......kkkkk.....", ".....kGGGGGk....", "....kgGGGGGGk...", "...kgk.....kk...", "...kgk.........."],
    "pet": ["................", "................", "................", ".....kkkkkk.....", "....kRRRRRRk....", "....kkkkkkkkkk..", "................"],
}
WAPENS = {
    "zwaard": ["............kk..", "...........kjk..", "...........kjk..", "...........kjk..", "...........kIk..", "..........kyyyk.", "...........kok..", "...........kok.."],
    "staf":   [".........kkk....", "........kYxYk...", "........kx*xk...", ".........kYk....", "..........kUk...", "..........kUk...", "..........kuk...", "..........kuk...", "..........kuk..."],
    "fakkel": ["...........x....", "..........kxk...", ".........kFxFk..", ".........kfFfk..", "..........kik...", "..........kuk...", "..........kuk...", "..........kuk..."],
}

def maak_held():
    lijven = [lijf(i, i in (1, 3)) for i in range(4)]
    opslaan(strip(lijven), "held_lijf.png")
    hoeden = []
    for naam in ("helm", "puntmuts", "kap", "pet"):
        im = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); im.paste(sprite(HOEDEN[naam]), (0, 0)); hoeden.append(im)
    opslaan(strip(hoeden), "held_hoeden.png")
    wapens = []
    for naam in ("zwaard", "staf", "fakkel"):
        im = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); sp = sprite(WAPENS[naam]); im.paste(sp, (1, 15 - sp.height - 1)); wapens.append(im)
    opslaan(strip(wapens), "held_wapens.png")
    return lijven, hoeden, wapens

def held(lijven, hoeden, wapens, fr, hoed, wapen):
    im = lijven[fr].copy()
    bob = 1 if fr in (1, 3) else 0
    if wapen is not None:
        w = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); w.paste(wapens[wapen], (0, bob)); im = Image.alpha_composite(im, w)
    if hoed is not None:
        h = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); h.paste(hoeden[hoed], (0, bob)); im = Image.alpha_composite(im, h)
    return im


# ---------- versiering, 16 x 16 per stuk ----------
DECO = {
    "paddenstoel": ["................"]*7 + ["....kkk.........", "...kRjRk..kk....", "..kRRRjRkkRjk...", "..kkkkkkkkkkk...", "....ksk...kk....", "....ksk...kk....", "...kSSSk.kSk....", "...kkkkk.kkk...."],
    "lichtzwam": ["................"]*6 + ["...kkkk.........", "..kNqqNk........", ".kNNqNNNk.......", ".kkMMMMkk..kkk..", "...kqqk...kNqNk.", "...kqNk...kkMkk.", "...kqNk....kqk..", "...kNNk.kk.kNk..", "..kkNMkkNqkkMk..", ".kkkkkkkkkkkkkk."],
    "ton":  ["................"]*4 + ["....kkkkkkk.....", "...kUUUUUUUk....", "...kiiiiiiik....", "..kUuUUUUUuUk...", "..kUuUUUUUuUk...", "..kiiiiiiiiik...", "..kUuUUUUUuUk...", "..kUuUUUUUuUk...", "...kiiiiiiik....", "...kUUUUUUUk....", "....kkkkkkk.....", "................"],
    "kist": ["................"]*6 + ["..kkkkkkkkkk....", "..kUUUUUUUUk....", "..kuUkkkkUuk....", "..kUkUUUUkUk....", "..kUUkUUkUUk....", "..kUUUkkUUUk....", "..kUkUUUUkUk....", "..kuUkkkkUuk....", "..kUUUUUUUUk....", "..kkkkkkkkkk...."],
    "schedel": ["................"]*7 + ["....kkkkk.......", "...kjjjjjk......", "..kjjjjjjjk.....", "..kjeejeejk.....", "..kjeejeejk.....", "..kIjjkjjIk.....", "...kIjjjIk..kk..", "...kjkjkjk.kjIk.", "....kkkkk.kkkkk."],
    "kristal": ["................"]*5 + ["......k.........", ".....kqk...k....", ".....kNk..kqk...", "..k..knMk.kNk...", ".kqk.knMk.kNMk..", ".kNk.kNMkknMk...", ".kNMkknMkknMk...", "..kMkknMkkMk....", "...kmkMkmkk.....", "...kkkkkkk......", "................"],
    "spinrag": ["9...........9...", ".9.......9.9....", "..9...9.9..9....", "..9.9..9...9....", "...9...9..9.....", "....9..9.9......", ".....9.99.......", "......9.........", "................", "................", "................", "................", "................", "................", "................", "................"],
    "stut": ["kkkkkkkkkkkkkkkk", "kUUUUUUUUUUUUUUk", "kuuuuuuuuuuuuuuk", "kkkkkkkkkkkkkkkk", ".kUk........kUk.", ".kUk........kUk.", ".kuk........kuk.", ".kUk........kUk.", ".kUk........kUk.", ".kuk........kuk.", ".kUk........kUk.", ".kUk........kUk.", ".kuk........kuk.", ".kUk........kUk.", ".kUk........kUk.", ".kkk........kkk."],
    "vaandel": ["kkkkkkkkkkkkkkkk", "UUUUUUUUUUUUUUUU", "kkk..........kkk", "..krrrrrrrrrrk..", "..krRRRRRRRRrk..", "..krRRyyRRRRrk..", "..krRyYyRRRRrk..", "..krRRyyRRRRrk..", "..krRRRRRRRRrk..", "..krRRRRRRRRrk..", "..krrrrrrrrrrk..", "...krrkkkkrrk...", "....kk....kk....", "................", "................", "................"],
}
def maak_deco():
    frames = []
    for n in DECO:
        sp = sprite(DECO[n]); f = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); f.paste(sp, (0, 16 - sp.height), sp); frames.append(f)
    opslaan(strip(frames), "versiering.png"); return dict(zip(DECO, frames))

def maak_gloed(r=26):
    # warm licht rond fakkels en lichtzwammen; in Godot als sprite met optellen (blend add) of als PointLight2D-textuur
    im = Image.new("RGBA", (r * 2, r * 2), (0, 0, 0, 0))
    for y in range(r * 2):
        for x in range(r * 2):
            d = ((x - r + 0.5) ** 2 + (y - r + 0.5) ** 2) ** 0.5 / r
            if d < 1:
                # in treden (pixel art, geen zachte waas): 3 ringen
                a = 70 if d < 0.4 else (42 if d < 0.7 else 20)
                im.putpixel((x, y), (255, 170, 80, a))
    opslaan(im, "gloed.png"); return im

# ---------- alles maken ----------
tegels = maak_tegels(); gras = maak_gras(); fakkel = maak_fakkel(); schat = maak_schat()
slijm = maak_slijm(); val = maak_val(); lijven, hoeden, wapens = maak_held()
ingang = sprite(INGANG); opslaan(ingang, "ingang.png")
deco = maak_deco(); gloed = maak_gloed(); boven = maak_boven()

json.dump({
    "spelpixel": "schaal 3 bij strook 120 tot 160 px (100% Windows), schaal 2 onder 120 px; bij 150% en 200% Windows schaal 4 en 6. Altijd hele schaal, filter nearest. Strook 120 px = 40 spelpixels = maaiveld 8 + 2 rijen cellen; extra hoogte toont meer aarde eronder", "maaiveld.png": {"frame": [16, 8], "volgorde": ["bloemen", "struik", "steen", "bordje", "paddo"]},
    "cel": 16, "maaiveld_hoogte": OPP,
    "tegels.png": {"rij0": "aarde, 8 varianten (kies willekeurig per cel, vast zaad)", "rij1": "gang, 16 varianten, index = n*1 + e*2 + s*4 + w*8 waarbij een bit 1 is als die buur AARDE is"},
    "gras.png": {"frame": [16, 8], "varianten": 4, "plek": "boven de bovenste aardelaag"},
    "ingang.png": {"frame": [20, 14], "anker": "onderkant op de grasrand, poortje boven de ingang-cel"},
    "fakkel.png": {"frame": [8, 12], "frames": 4, "fps": 6, "plek": "aan de wand van een gang, alleen bij de ingang en de schatkamer"},
    "schat.png": {"frame": [24, 16], "frames": 4, "fps": 4, "anker": "midden onder"},
    "slijm.png": {"frame": [16, 16], "rust": [0, 1, 2, 3], "rust_fps": 3, "hap": [4, 5], "anker": "midden onder"},
    "stekelput.png": {"frame": [16, 8], "dicht": 0, "half": 1, "open": 2, "anker": "op de vloer van de gang"},
    "held_lijf.png": {"frame": [16, 16], "lopen": [0, 1, 2, 3], "fps": 8, "anker": "midden onder (voeten op y 15)", "kijkt": "rechts; spiegel voor links"},
    "held_hoeden.png": {"frame": [16, 16], "volgorde": ["helm", "puntmuts", "kap", "pet"], "tekenen": "boven het lijf, zelfde frame, 1 px omlaag bij lopen-frames 1 en 3"},
    "versiering.png": {"frame": [16, 16], "volgorde": ["paddenstoel", "lichtzwam", "ton", "kist", "schedel", "kristal", "spinrag", "stut", "vaandel"], "anker": "midden onder op de vloer; spinrag, stut en vaandel tegen het plafond (bovenkant); stut is een houten gangsteun, achter de figuren tekenen"},
    "gloed.png": {"frame": [52, 52], "gebruik": "warm licht rond fakkels (en groen getint rond lichtzwammen); tekenen met optellen (CanvasItemMaterial blend add) of als PointLight2D-textuur, alleen in de gangen"},
    "held_wapens.png": {"frame": [16, 16], "volgorde": ["zwaard", "staf", "fakkel"], "tekenen": "boven het lijf, in de rechterhand; 1 px omlaag bij frames 1 en 3"},
}, open(os.path.join(UIT, "kunst.json"), "w"), ensure_ascii=False, indent=1)

# ---------- voorbeeld: een stuk hol op ware maat (schaal 3, strook 120 px) ----------
def voorbeeld(breedte_cellen=40, schaal=3, naam="voorbeeld-strook.png"):
    rnd = random.Random(7)
    RIJ = 2
    H = OPP + RIJ * CEL   # 40 spelpixels
    W = breedte_cellen * CEL
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gang = [[False] * breedte_cellen for _ in range(RIJ)]
    ing = 3
    gang[0][ing] = True
    for x in range(ing, 33): gang[1][x] = True              # hoofdgang
    for x in range(12, 16): gang[0][x] = True               # kamer van de slijmen (2 hoog)
    for x in range(26, 31): gang[0][x] = True               # schatkamer (2 hoog)
    for x in range(33, 36): gang[1][x] = True               # wordt gegraven
    for x in range(19, 22): gang[0][x] = True               # voorraadkamer
    gang[0][7] = True                                       # schacht
    for cx in range(breedte_cellen):
        g = gras.crop(((cx % 4) * CEL, 0, (cx % 4) * CEL + CEL, OPP)); im.paste(g, (cx * CEL, 0), g)
    def is_g(r, c):
        return 0 <= r < RIJ and 0 <= c < breedte_cellen and gang[r][c]
    for r in range(RIJ):
        for c in range(breedte_cellen):
            x, y = c * CEL, OPP + r * CEL
            if gang[r][c]:
                n = not is_g(r - 1, c) and not (r == 0 and c == ing)
                e = not is_g(r, c + 1); s_ = not is_g(r + 1, c) or r == RIJ - 1; w = not is_g(r, c - 1)
                m = int(n) | int(e) << 1 | int(s_) << 2 | int(w) << 3
                t = tegels.crop((m * CEL, CEL, m * CEL + CEL, 2 * CEL))
            else:
                v = rnd.randint(0, 7); t = tegels.crop((v * CEL, 0, v * CEL + CEL, CEL))
            im.paste(t, (x, y))
    for xx in range(ing * CEL, ing * CEL + CEL):
        for yy in range(3, OPP): im.putpixel((xx, yy), P["W"] if yy > 4 else (0, 0, 0, 0))
    im.paste(ingang, (ing * CEL - 2, OPP - 14 + 4), ingang)
    def zet(sp, x, y): im.paste(sp, (int(x), int(y)), sp)
    for cx, n in ((1, "bloemen"), (6, "bordje"), (8, "struik"), (11, "steen"), (17, "bloemen"), (20, "paddo"), (23, "struik"), (32, "bloemen"), (34, "steen"), (37, "struik")):
        zet(boven[n], cx * CEL, 0)
    vloer = OPP + 2 * CEL - 3
    plaf = OPP + CEL
    for cx, n in ((5, "ton"), (9, "paddenstoel"), (12, "lichtzwam"), (17, "schedel"), (21, "kist"), (25, "kristal"), (31, "lichtzwam")):
        zet(deco[n], cx * CEL, vloer - 16 + 1)
    for cx in (6, 17, 24, 32): zet(deco["stut"], cx * CEL, plaf)
    for cx in (9, 32): zet(deco["spinrag"], cx * CEL, plaf)
    zet(deco["ton"], 19 * CEL + 2, plaf - 16 + 13); zet(deco["kist"], 20 * CEL + 4, plaf - 16 + 13)
    zet(deco["vaandel"], 28 * CEL, OPP + 1)
    zet(fakkel[1], 4 * CEL + 4, plaf + 1)
    zet(fakkel[2], 25 * CEL + 4, plaf + 1)
    zet(schat[0], 28 * CEL - 4, vloer - 16 + 1)
    zet(slijm[0], 13 * CEL, vloer - 16 + 1)
    zet(slijm[1], 14 * CEL + 6, vloer - 16 + 1)
    zet(val[2], 18 * CEL + 4, vloer - 8 + 1)
    zet(val[0], 23 * CEL, vloer - 8 + 1)
    zet(held(lijven, hoeden, wapens, 0, 0, 0), 7 * CEL, vloer - 16 + 1)
    zet(held(lijven, hoeden, wapens, 1, 1, 1), 10 * CEL + 2, vloer - 16 + 1)
    zet(held(lijven, hoeden, wapens, 2, 2, 2), 16 * CEL + 4, vloer - 16 + 1)
    zet(held(lijven, hoeden, wapens, 3, 3, None).transpose(Image.FLIP_LEFT_RIGHT), 22 * CEL, vloer - 16 + 1)
    licht = Image.new("RGBA", im.size, (0, 0, 0, 0))
    for (lx, ly) in ((4 * CEL + 8, plaf + 4), (25 * CEL + 8, plaf + 4), (28 * CEL + 8, vloer - 6)):
        licht.alpha_composite(gloed, (lx - gloed.width // 2, ly - gloed.height // 2))
    for (lx, ly) in ((12 * CEL + 8, vloer - 4), (31 * CEL + 8, vloer - 4)):
        g2 = gloed.resize((32, 32), Image.NEAREST); px = g2.load()
        for yy in range(32):
            for xx in range(32):
                a_ = px[xx, yy][3]; px[xx, yy] = (110, 255, 200, a_)
        licht.alpha_composite(g2, (lx - 16, ly - 16))
    import numpy as np
    a = np.asarray(im).astype(np.int32); l = np.asarray(licht).astype(np.int32)
    gm = np.zeros((H, W, 1), dtype=bool)
    for r in range(RIJ):
        for c in range(breedte_cellen):
            if gang[r][c]: gm[OPP + r * CEL:OPP + (r + 1) * CEL, c * CEL:(c + 1) * CEL] = True
    a[..., :3] = np.where(gm, np.clip(a[..., :3] + (l[..., :3] * l[..., 3:4]) // 255, 0, 255), a[..., :3])
    im = Image.fromarray(a.astype(np.uint8), "RGBA")
    groot = im.resize((W * schaal, H * schaal), Image.NEAREST)
    groot.save(os.path.join(HIER, naam))
    return groot

strookbeeld = voorbeeld()
# atlasoverzicht op schaal 6 om te keuren
def overzicht():
    delen = [Image.open(os.path.join(UIT, n)) for n in ("held_lijf.png", "held_hoeden.png", "held_wapens.png", "slijm.png", "schat.png", "stekelput.png", "fakkel.png", "ingang.png", "gras.png", "tegels.png")]
    W = max(d.width for d in delen) + 8; H = sum(d.height + 4 for d in delen) + 4
    im = Image.new("RGBA", (W, H), hx("1a1418")); y = 4
    for d in delen: im.paste(d, (4, y), d); y += d.height + 4
    combos = [held(lijven, hoeden, wapens, 0, h, w) for h, w in ((0, 0), (1, 1), (2, 2), (3, None), (0, 2), (1, 0))]
    c = strip(combos); im2 = Image.new("RGBA", (max(W, c.width + 8), H + 24), hx("1a1418")); im2.paste(im, (0, 0)); im2.paste(c, (4, H + 4), c)
    im2.resize((im2.width * 5, im2.height * 5), Image.NEAREST).save(os.path.join(HIER, "atlas-groot.png"))
overzicht()
print("klaar", UIT)
