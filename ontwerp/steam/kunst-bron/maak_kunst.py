# Daan: tekent de pixelkunst van Het Hol in code (geen beeldgenerator).
# Uitvoer: producten/steam-hol/godot/kunst/*.png en kunst.json, plus voorbeeldbeelden in ontwerp/steam/kunst-bron/.
# Maat: spelpixels van 16 x 16 per cel, schaal 2 op 100% Windows (strook 120 px = 60 spelpixels).
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
    "1": hx("3d2621"), "2": hx("5a3a2c"), "3": hx("774c34"), "4": hx("96633f"), "5": hx("b5804f"),
    # holwand (achter de gang)
    "w": hx("231719"), "W": hx("2f2023"), "v": hx("3c2b2b"),
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
    "r": hx("8e2f36"), "R": hx("c9493f"), "b": hx("2f4f8f"), "B": hx("4f7fd0"),
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
OPP = 12   # hoogte van het maaiveld (gras) boven de eerste aardelaag

# ---------- aarde en gangen (autotegel, 16 varianten op 4 buren) ----------
def aarde_cel(rnd, im, ox, oy):
    for y in range(CEL):
        for x in range(CEL):
            v = rnd.random()
            c = "3" if v < 0.62 else ("2" if v < 0.86 else "4")
            im.putpixel((ox + x, oy + y), P[c])
    # klonten en steentjes
    for _ in range(rnd.randint(1, 3)):
        x, y = rnd.randint(1, 13), rnd.randint(1, 13)
        for dx, dy, c in ((0, 0, "4"), (1, 0, "4"), (0, 1, "2"), (1, 1, "2")):
            im.putpixel((ox + x + dx, oy + y + dy), P[c])
    if rnd.random() < 0.45:
        x, y = rnd.randint(2, 11), rnd.randint(2, 11)
        steen = [".88.", "8997", "7887", ".77."]
        for yy, r in enumerate(steen):
            for xx, c in enumerate(r):
                if c != ".": im.putpixel((ox + x + xx, oy + y + yy), P[c])
        im.putpixel((ox + x + 1, oy + y + 4), P["1"]); im.putpixel((ox + x + 2, oy + y + 4), P["1"])
    if rnd.random() < 0.25:   # worteltje
        x = rnd.randint(2, 13); y = rnd.randint(0, 6)
        for i in range(rnd.randint(3, 6)):
            im.putpixel((ox + x, oy + y + i), P["u"])
            if rnd.random() < 0.4: x = max(1, min(14, x + rnd.choice((-1, 1))))

def gang_cel(rnd, im, ox, oy, n, e, s, w):
    """n,e,s,w = True als de buur aarde is (dan komt er een rand)."""
    for y in range(CEL):
        for x in range(CEL):
            v = rnd.random()
            c = "W" if v < 0.7 else ("w" if v < 0.9 else "v")
            im.putpixel((ox + x, oy + y), P[c])
    # stenen in de achterwand, heel zacht
    for _ in range(2):
        x, y = rnd.randint(2, 12), rnd.randint(4, 10)
        for dx in range(3): im.putpixel((ox + x + dx, oy + y), P["v"])
        im.putpixel((ox + x + 1, oy + y - 1), P["v"])
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
    # rij 0: 4 aardevarianten; rij 1: 16 gangvarianten (index = n*1 + e*2 + s*4 + w*8)
    im = Image.new("RGBA", (CEL * 16, CEL * 2), (0, 0, 0, 0))
    for i in range(4): aarde_cel(random.Random(10 + i), im, i * CEL, 0)
    for m in range(16):
        gang_cel(random.Random(100 + m), im, m * CEL, CEL, bool(m & 1), bool(m & 2), bool(m & 4), bool(m & 8))
    opslaan(im, "tegels.png")
    return im

# ---------- maaiveld ----------
def maak_gras():
    # 4 varianten van 16 x 12: lucht doorzichtig, grasrand, bovenste aarde
    im = Image.new("RGBA", (CEL * 4, OPP), (0, 0, 0, 0))
    for v in range(4):
        rnd = random.Random(200 + v); ox = v * CEL
        for x in range(CEL):
            top = 6 + (1 if rnd.random() < 0.3 else 0)
            for y in range(top, OPP):
                c = "G" if y < top + 2 else ("g" if y < top + 3 else ("2" if y < top + 4 else "3"))
                im.putpixel((ox + x, y), P[c])
            im.putpixel((ox + x, top), P["h"])
            if rnd.random() < 0.35:          # sprietjes
                hgt = rnd.randint(1, 3)
                for i in range(1, hgt + 1): im.putpixel((ox + x, top - i), P["G" if i < hgt else "h"])
        if v in (1, 3):                       # bloempje
            x = rnd.randint(3, 12)
            im.putpixel((ox + x, 3), P["Y"]); im.putpixel((ox + x - 1, 3), P["*"]); im.putpixel((ox + x + 1, 3), P["*"])
            im.putpixel((ox + x, 2), P["*"]); im.putpixel((ox + x, 4), P["*"])
            for y in (5, 6): im.putpixel((ox + x, y), P["G"])
    opslaan(im, "gras.png")
    return im

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
    ".....kkkkkk.....", "....ksssssSk....", "....ksssEesk....", "....ksssEesk....",
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
    "zwaard": ["..........kj....", ".........kjI....", "........kjIk....", ".......kjIk.....", "......kyk.......", "......kok.......", "................"],
    "staf":   ["..........kYk...", "..........kxk...", "..........kUk...", "..........kuk...", "..........kuk...", "..........kuk...", "..........kuk..."],
    "fakkel": ["..........kx....", ".........kFxk...", "..........fk....", "..........kuk...", "..........kuk...", "................", "................"],
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
        im = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); im.paste(sprite(WAPENS[naam]), (1, 6)); wapens.append(im)
    opslaan(strip(wapens), "held_wapens.png")
    return lijven, hoeden, wapens

def held(lijven, hoeden, wapens, fr, hoed, wapen):
    im = lijven[fr].copy()
    bob = 1 if fr in (1, 3) else 0
    if wapen is not None:
        w = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); w.paste(wapens[wapen], (0, bob)); im = Image.alpha_composite(w, im) if wapen == 1 else Image.alpha_composite(im, w)
    if hoed is not None:
        h = Image.new("RGBA", (16, 16), (0, 0, 0, 0)); h.paste(hoeden[hoed], (0, bob)); im = Image.alpha_composite(im, h)
    return im

# ---------- alles maken ----------
tegels = maak_tegels(); gras = maak_gras(); fakkel = maak_fakkel(); schat = maak_schat()
slijm = maak_slijm(); val = maak_val(); lijven, hoeden, wapens = maak_held()
ingang = sprite(INGANG); opslaan(ingang, "ingang.png")

json.dump({
    "spelpixel": "1 spelpixel = 2 schermpixels bij 100% Windows, 3 bij 150%, 4 bij 200% (altijd hele schaal, filter nearest)",
    "cel": 16, "maaiveld_hoogte": OPP,
    "tegels.png": {"rij0": "aarde, 4 varianten (kies willekeurig per cel, vast zaad)", "rij1": "gang, 16 varianten, index = n*1 + e*2 + s*4 + w*8 waarbij een bit 1 is als die buur AARDE is"},
    "gras.png": {"frame": [16, 12], "varianten": 4, "plek": "boven de bovenste aardelaag"},
    "ingang.png": {"frame": [20, 14], "anker": "onderkant op de grasrand, poortje boven de ingang-cel"},
    "fakkel.png": {"frame": [8, 12], "frames": 4, "fps": 6, "plek": "aan de wand van een gang, alleen bij de ingang en de schatkamer"},
    "schat.png": {"frame": [24, 16], "frames": 4, "fps": 4, "anker": "midden onder"},
    "slijm.png": {"frame": [16, 16], "rust": [0, 1, 2, 3], "rust_fps": 3, "hap": [4, 5], "anker": "midden onder"},
    "stekelput.png": {"frame": [16, 8], "dicht": 0, "half": 1, "open": 2, "anker": "op de vloer van de gang"},
    "held_lijf.png": {"frame": [16, 16], "lopen": [0, 1, 2, 3], "fps": 8, "anker": "midden onder (voeten op y 15)", "kijkt": "rechts; spiegel voor links"},
    "held_hoeden.png": {"frame": [16, 16], "volgorde": ["helm", "puntmuts", "kap", "pet"], "tekenen": "boven het lijf, zelfde frame, 1 px omlaag bij lopen-frames 1 en 3"},
    "held_wapens.png": {"frame": [16, 16], "volgorde": ["zwaard", "staf", "fakkel"], "tekenen": "zwaard en fakkel boven het lijf, staf achter het lijf; 1 px omlaag bij frames 1 en 3"},
}, open(os.path.join(UIT, "kunst.json"), "w"), ensure_ascii=False, indent=1)

# ---------- voorbeeld: een stuk hol op ware maat (schaal 2, strook 120 px) ----------
def voorbeeld(breedte_cellen=60, schaal=2, naam="voorbeeld-strook.png"):
    rnd = random.Random(7)
    H = OPP + 3 * CEL   # 60 spelpixels
    W = breedte_cellen * CEL
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # raster: rij 0..2; True = gang
    gang = [[False] * breedte_cellen for _ in range(3)]
    ing = 6
    gang[0][ing] = True
    for x in range(ing, 40): gang[1][x] = True
    for x in range(18, 23): gang[2][x] = True   # kamer van de slijm (2 hoog)
    gang[2][14] = True
    for x in range(34, 40): gang[2][x] = True   # schatkamer
    gang[0][36] = True; gang[0][37] = True
    for x in range(40, 44): gang[1][x] = True    # wordt gegraven
    # gras
    for cx in range(breedte_cellen):
        g = gras.crop(((cx % 4) * CEL, 0, (cx % 4) * CEL + CEL, OPP)); im.paste(g, (cx * CEL, 0), g)
    def is_g(r, c):
        return 0 <= r < 3 and 0 <= c < breedte_cellen and gang[r][c]
    for r in range(3):
        for c in range(breedte_cellen):
            x, y = c * CEL, OPP + r * CEL
            if gang[r][c]:
                n = not is_g(r - 1, c) and not (r == 0 and c == ing)
                e = not is_g(r, c + 1); s = not is_g(r + 1, c); w = not is_g(r, c - 1)
                m = int(n) | int(e) << 1 | int(s) << 2 | int(w) << 3
                t = tegels.crop((m * CEL, CEL, m * CEL + CEL, 2 * CEL))
            else:
                v = rnd.randint(0, 3); t = tegels.crop((v * CEL, 0, v * CEL + CEL, CEL))
            im.paste(t, (x, y))
    # gras ingang weg (gat), poortje
    for xx in range(ing * CEL, ing * CEL + CEL):
        for yy in range(5, OPP): im.putpixel((xx, yy), P["W"] if yy > 8 else (0, 0, 0, 0))
    im.paste(ingang, (ing * CEL - 4, OPP - 14 + 2), ingang)
    def zet(sp, x, y): im.paste(sp, (int(x), int(y)), sp)
    vloer1 = OPP + 2 * CEL - 3   # onderkant van rij 1, op de vloer
    vloer2 = OPP + 3 * CEL - 3
    zet(fakkel[1], 8 * CEL + 4, OPP + CEL + 1)
    zet(fakkel[2], 33 * CEL + 4, OPP + CEL + 1)
    zet(schat[0], 36 * CEL - 4, vloer2 - 16 + 1)
    zet(slijm[0], 20 * CEL, vloer2 - 16 + 1)
    zet(slijm[1], 21 * CEL + 4, vloer2 - 16 + 1)
    zet(val[2], 26 * CEL, vloer1 - 8 + 1)
    zet(val[0], 30 * CEL, vloer1 - 8 + 1)
    zet(held(lijven, hoeden, wapens, 0, 0, 0), 11 * CEL, vloer1 - 16 + 1)
    zet(held(lijven, hoeden, wapens, 1, 1, 1), 15 * CEL - 4, vloer1 - 16 + 1)
    zet(held(lijven, hoeden, wapens, 2, 2, 2), 24 * CEL + 2, vloer1 - 16 + 1)
    h4 = held(lijven, hoeden, wapens, 3, 3, None).transpose(Image.FLIP_LEFT_RIGHT); zet(h4, 32 * CEL, vloer1 - 16 + 1)
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
