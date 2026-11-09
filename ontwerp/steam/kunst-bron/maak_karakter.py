# Daan: karakter-laag voor Het Hol (wensen van Sanne 9 nov 19:05 en de keuring van Olafs build).
# Littekens als losse laag, hoeden met een hap, tunieken in kleuren, tekens boven het hoofd,
# slijm met leven-animaties en een plat frame, laars, paneel en naamkaartje (9-slice), trofeebord.
# Draai alleen dit script: het draait maak_kunst.py (basis) en maak_aarde.py (aarde) mee. Uitvoer in producten/steam-hol/godot/kunst/.
import json, os, sys
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import maak_kunst as mk   # tekent ook de basisbladen opnieuw (vast zaad, dus gelijk)

P, sprite, strip, opslaan, UIT = mk.P, mk.sprite, mk.strip, mk.opslaan, mk.UIT
P["P"] = mk.hx("ecd2a8")   # pleister
P["Q"] = mk.hx("b8946c")   # pleister schaduw
P["c"] = mk.hx("c98b4f")   # leer en hout licht (was aarde 5, aarde is nu pruim)

def leeg(w=16, h=16):
    return Image.new("RGBA", (w, h), (0, 0, 0, 0))

def zet(im, punten, c):
    for x, y in punten:
        im.putpixel((x, y), P[c])

# ---------- littekens: 16 x 16, zelfde frame als het lijf, tekenen boven het lijf en onder de hoed ----------
def maak_littekens():
    pleister = leeg(); zet(pleister, [(5, 7), (6, 7), (7, 7), (6, 6)], "j"); zet(pleister, [(6, 8)], "I")
    ooglap = leeg(); zet(ooglap, [(8, 6), (9, 6), (8, 7), (9, 7)], "k"); zet(ooglap, [(5, 6), (6, 6), (7, 6), (10, 6), (11, 6)], "K")
    schram = leeg(); zet(schram, [(9, 5), (10, 6), (10, 8), (9, 9)], "f"); zet(schram, [(9, 8)], "r")
    # verband: arm in een mitella, wit over de borst
    verband = leeg(); zet(verband, [(4, 6), (5, 6), (6, 6), (10, 6), (3, 6), (2, 7), (3, 8)], "j")
    zet(verband, [(7, 6), (2, 8)], "I"); zet(verband, [(5, 6)], "f")
    frames = [pleister, ooglap, schram, verband]
    opslaan(strip(frames), "held_littekens.png")
    return frames

# ---------- hoeden met een hap eruit (terugkomers): zelfde volgorde als held_hoeden.png ----------
def maak_hoeden_hap(hoeden):
    uit = []
    for h in hoeden:
        im = h.copy(); px = im.load(); bb = im.getbbox()
        cx = (bb[0] + bb[2]) // 2 + 2
        top = min(y for y in range(16) if px[cx, y][3])
        weg = set()
        for (dx, dy) in [(-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1), (0, 2), (2, 0)]:
            x, y = cx + dx, top + dy
            if 0 <= x < 16 and px[x, y][3] and y < bb[3] - 1: weg.add((x, y))
        for p in weg: px[p] = (0, 0, 0, 0)
        for (x, y) in weg:   # rand van de hap donker maken
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < 16 and 0 <= ny < 16 and (nx, ny) not in weg and px[nx, ny][3]:
                    px[nx, ny] = P["k"]
        tand = (cx, top + 2)
        if tand in weg: px[tand] = P["k"]; weg.discard(tand)   # tandje in de hap
        uit.append(im)
    opslaan(strip(uit), "held_hoeden_hap.png")
    return uit

# ---------- tunieken in kleuren: rij 0 rood (zoals held_lijf.png), 1 groen, 2 paars, 3 oker, 4 blauw-grijs ----------
KLEUREN = [("r", "R"), ("g", "G"), ("z", "Z"), ("O", "y"), ("m", "M")]
def maak_kleuren(lijven):
    rood, roodl = P["r"], P["R"]
    rijen = []
    for d, l in KLEUREN:
        rij = []
        for f in lijven:
            im = f.copy(); px = im.load()
            for y in range(16):
                for x in range(16):
                    if px[x, y] == rood: px[x, y] = P[d]
                    elif px[x, y] == roodl: px[x, y] = P[l]
            rij.append(im)
        rijen.append(strip(rij))
    blad = Image.new("RGBA", (64, 16 * len(rijen)), (0, 0, 0, 0))
    for i, r in enumerate(rijen): blad.paste(r, (0, i * 16))
    opslaan(blad, "held_lijf_kleuren.png")
    return blad

# ---------- tekens boven het hoofd, 8 x 8 ----------
TEKENS = {
    # Mila 9 nov: onweerswolkje met rode bliksem; het oude rode teken las op ware grootte als een kruisje (Sanne toets 3)
    "boos": ["..kk.kk.", ".k99k98k", "k9988888", "k8888877", ".kkkRkk.", "...kRk..", "..kRRRk.", "..kRk..."],
    "uitroep": ["...kk...", "..kyyk..", "..kYyk..", "..kyyk..", "...kk...", "...kk...", "..kyyk..", "...kk..."],
    "zweet": ["...k....", "..kBk...", "..kBk...", ".kBBBk..", ".kBjBk..", ".kBBBk..", "..kkk...", "........"],
    "zzz": ["BBBB....", "..B.....", ".B......", "BBBB.BBB", "......B.", ".....BBB", "........", "........"],
    "ster": ["...kk...", "..kyyk..", "kkyYYykk", "kyYYYYyk", ".kyYYyk.", ".kykkyk.", "kyk..kyk", "kk....kk"],
}
def maak_tekens():
    frames = [sprite(TEKENS[n]) for n in TEKENS]
    opslaan(strip(frames), "tekens.png")
    return frames

# ---------- slijm: leven-animaties (16 x 16) ----------
def rijen_aan(rows, wat):
    rows = [list(r) for r in rows]
    for (x, y), c in wat.items(): rows[y][x] = c
    return ["".join(r) for r in rows]

def ogen_weg(rows):
    """Mila 9 nov: eenogige Gloop. Haalt oog en grijns weg; de frames hieronder tekenen hun eigen oog en mond."""
    r = list(rows)
    wide = r[13].startswith(".k")   # frame b is breder
    r[9] = r[9][:5] + "n" * (13 - 5) + r[9][13:] if not wide else r[9][:5] + "n" * 8 + r[9][13:]
    for y in (10, 11, 12):
        r[y] = "".join("n" if ch in "kEe" and 5 <= x <= 11 else ch for x, ch in enumerate(r[y]))
    r[13] = "".join("M" if ch in "kE" and 4 <= x <= 11 else ch for x, ch in enumerate(r[13]))
    return r

def maak_slijm_leven():
    a, b = mk.SLIJM_RUST
    lijn = lambda y, x0, x1: {(x, y): "k" for x in range(x0, x1 + 1)}
    slaap1 = rijen_aan(ogen_weg(a), lijn(11, 6, 10))
    slaap2 = rijen_aan(ogen_weg(b), lijn(11, 6, 10))
    blij = rijen_aan(ogen_weg(a), {**lijn(10, 7, 9), (6, 11): "k", (10, 11): "k", **lijn(13, 5, 8), (9, 13): "E", (10, 13): "k"})
    bol = rijen_aan(ogen_weg(b), {**lijn(11, 6, 10), (6, 10): "k", (10, 10): "k", (3, 12): "p", (12, 12): "p"})
    hap = [
        "................", "................", "................", ".....kkkkkk.....",
        "....kNNnnnnk....", "...kNqNnnnnnk...", "...knnkkkkknnk..", "..knnkEEeeeknk..",
        "..knkkkkkkkkk...", "..knkRRRRRRk....", "..knkkkkkkkkk...", "..knnnnnnnnnnk..",
        "..knMnnnnnnnMk..", "..kMMnnnnnnMMk..", "...kMMMMMMMMk...", "....kkkkkkkk....",
    ]
    spuug = rijen_aan(hap, {(11, 6): "k", (12, 6): "k", (13, 6): "k", (11, 7): "L", (12, 7): "L", (13, 7): "k",
                            (11, 8): "L", (12, 8): "L", (13, 8): "k", (14, 8): "k", (15, 8): "k",
                            (11, 9): "L", (12, 9): "L", (13, 9): "L", (14, 9): "L", (15, 9): "k",
                            (11, 10): "l", (12, 10): "l", (13, 10): "l", (14, 10): "l", (15, 10): "k"})
    plat = ["................"] * 10 + [
        "....kkkkkkkk....", "..kkNqnnnnnnkk..", ".knnnnkkkkknnnnk", ".knnnnnnnnnnnnnk",
        "kMnnnnkkEknnnnMk", "kkkkkkkkkkkkkkkk"]
    for _f in (slaap1, slaap2, blij, bol, hap, spuug, plat): assert all(len(r) == 16 for r in _f), _f
    kauw1 = rijen_aan(bol, {**lijn(13, 6, 9), (8, 13): "E"})
    kauw2 = rijen_aan(ogen_weg(a), {**lijn(11, 6, 10), (6, 10): "k", (10, 10): "k", **lijn(13, 5, 8), (6, 13): "E", (4, 12): "p", (12, 12): "p"})
    volgorde = [("slapen", [slaap1, slaap2]), ("spugen", [bol, hap, spuug, blij]),
                ("hap", [hap, kauw1, kauw2, kauw1, blij]), ("plat", [plat]), ("opstaan", [b])]
    frames, index = [], {}
    for naam, fr in volgorde:
        index[naam] = list(range(len(frames), len(frames) + len(fr)))
        frames += [sprite(r) for r in fr]
    opslaan(strip(frames), "slijm_leven.png")
    laars = sprite(["..kkkk..", "..kcck..", "..kUUk..", "..kUUkk.", "..kUUUck", "..kUUUUk", "..kLLLLk", "..kkkkkk"])
    opslaan(laars, "laars.png")
    return frames, index, laars

# ---------- paneel (meldingen in de strook) en naamkaartje (aartsvijand), 9-slice ----------
def maak_paneel():
    im = leeg(12, 12); px = im.load()
    for y in range(12):
        for x in range(12):
            rand = min(x, y, 11 - x, 11 - y)
            # Mila 9 nov: pruim in plaats van bruin hout (Sanne toets 3: "groot en bruin op pruim"); hoort bij de holwand
            c = "k" if rand == 0 else ("V" if rand == 1 else ("k" if rand == 2 else ("v" if (y + (x // 4)) % 4 == 0 else "W")))
            if rand == 1 and (y == 11 - 1 or x == 11 - 1): c = "v"   # schaduw rechtsonder
            px[x, y] = P[c]
    for (x, y) in ((0, 0), (11, 0), (0, 11), (11, 11)): px[x, y] = (0, 0, 0, 0)
    for (x, y) in ((2, 2), (9, 2), (2, 9), (9, 9)): px[x, y] = P["y"]   # gouden spijkertjes
    opslaan(im, "paneel.png")
    kaart = leeg(10, 8); px = kaart.load()
    for y in range(8):
        for x in range(10):
            rand = min(x, y, 9 - x, 7 - y)
            c = "k" if rand == 0 else ("Y" if y == 1 else ("O" if y == 6 else "y"))
            px[x, y] = P[c]
    for (x, y) in ((0, 0), (9, 0), (0, 7), (9, 7)): px[x, y] = (0, 0, 0, 0)
    px[1, 1] = P["*"]; px[2, 4] = P["o"]; px[7, 4] = P["o"]
    opslaan(kaart, "naamkaartje.png")
    return im, kaart

# ---------- trofeebord voor de wand van aartsvijanden: schildje met een haak, de hoed hangt erop ----------
TROFEE = ["................", "................", "................", "................",
          "..kkkkkkkkkkkk..", ".kUccUUUUUUUUUk.", ".kcuuuukkuuuuUk.", ".kUuuuukIkuuuUk.",
          ".kUuuuuukuuuuUk.", ".kUulluuuuuuuUk.", "..kUuuuulluuUk..", "..kUlluuuuuuUk..",
          "...kUuuuuuuUk...", "....kUUUUUUk....", ".....kkkkkk.....", "................"]

# ---------- voorbeeld: alles bij elkaar op schaal 3, om zelf te keuren ----------
def voorbeeld(lijven, hoeden, wapens, littekens, hap_hoeden, kleuren, tekens, slijm, laars, paneel, kaart, trofee):
    W, H = 200, 40
    c = Image.new("RGBA", (W, H), P["w"])
    def plak(im, x, y): c.alpha_composite(im, (x, y))
    # rij helden: elke kleur, met hoed, wapen en een litteken
    for i in range(5):
        lijf = kleuren.crop((0, i * 16, 16, i * 16 + 16))
        plak(lijf, 4 + i * 18, 4)
        if i > 0: plak(littekens[(i - 1) % 4], 4 + i * 18, 4)
        plak(wapens[i % 3], 4 + i * 18, 4)
        plak((hap_hoeden if i > 2 else hoeden)[i % 4], 4 + i * 18, 4)
    plak(tekens[0], 8 + 18, 0); plak(tekens[4], 8 + 4 * 18, 0)
    for i, f in enumerate(slijm): plak(f, 4 + i * 16, 22)
    plak(laars, 4 + 16 * 4 + 12, 30)
    p = Image.new("RGBA", (40, 14));
    # paneel 9-slice opbouwen
    for y in range(14):
        for x in range(40):
            sx = x if x < 4 else (11 - (39 - x) if x > 35 else 4 + (x - 4) % 4)
            sy = y if y < 4 else (11 - (13 - y) if y > 9 else 4 + (y - 4) % 4)
            p.putpixel((x, y), paneel.getpixel((sx, sy)))
    plak(p, 106, 4)
    k = Image.new("RGBA", (30, 8))
    for y in range(8):
        for x in range(30):
            sx = x if x < 3 else (9 - (29 - x) if x > 26 else 3 + (x - 3) % 4)
            k.putpixel((x, y), kaart.getpixel((sx, y)))
    plak(k, 150, 8)
    plak(trofee, 182, 0); plak(hoeden[0], 182, -4)
    c.resize((W * 3, H * 3), Image.NEAREST).save(os.path.join(HIER, "voorbeeld-karakter.png"))

if __name__ == "__main__":
    lijven, hoeden, wapens = mk.lijven, mk.hoeden, mk.wapens
    littekens = maak_littekens(); hap_hoeden = maak_hoeden_hap(hoeden); kleuren = maak_kleuren(lijven)
    tekens = maak_tekens(); slijm, slijm_index, laars = maak_slijm_leven(); paneel, kaart = maak_paneel()
    trofee = sprite(TROFEE); opslaan(trofee, "trofee.png")
    pad = os.path.join(UIT, "kunst.json"); meta = json.load(open(pad))
    meta["held_littekens.png"] = {"frame": [16, 16], "volgorde": ["pleister", "ooglap", "schram", "verband"],
        "tekenen": "boven het lijf, onder hoed en wapen, zelfde frame; 1 px omlaag bij lopen-frames 1 en 3. Bezoek 2: 1 litteken, bezoek 3: 2, aartsvijand: 3; kies vast per held (zaad = naam). Combinaties: ooglap en schram nooit samen (zelfde oog); de rest mag. Vervangt de rode streepjes en het verband-streepje in held.gd: die eruit.", "kleur": "de oude tint-kleuren voor helden en hoeden in strook.gd en held.gd eruit, anders dubbel gekleurd"}
    meta["held_hoeden_hap.png"] = {"frame": [16, 16], "volgorde": mk.HOED_NAMEN,
        "gebruik": "in plaats van held_hoeden.png als de held al eens door de slijm is gebeten (wrok tegen Gloop)"}
    meta["held_lijf_kleuren.png"] = {"frame": [16, 16], "rijen": ["rood", "groen", "paars", "oker", "zeegroen"],
        "gebruik": "zelfde frames als held_lijf.png (4 per rij); kies de rij vast per held, zodat Kees altijd dezelfde tuniek heeft en je hem herkent"}
    meta["tekens.png"] = {"frame": [8, 8], "volgorde": list(TEKENS),
        "plek": "midden boven het hoofd, onderkant van het teken op y = -20 ten opzichte van de voeten (anker midden onder), voor elke hoed gelijk; boos = wrok en ziet zijn vijand, uitroep = ziet de schat, zweet = vlucht, zzz = slijm slaapt, ster = aartsvijand (blijft staan)"}
    meta["slijm_leven.png"] = {"frame": [16, 16], "animaties": slijm_index, "fps": 5,
        "bron": "alle leven-animaties en de hap komen uit dit blad; slijm.png alleen voor rust (frames 0 tot 3)", "gebruik": "slapen: herhalen met zzz uit tekens.png erboven; spugen en hap: eenmalig, daarna terug naar rust van slijm.png; plat: in plaats van uitrekken (nooit schalen, dat breekt de pixels), opstaan: 1 frame voor hij weer rust",
        "zuinig": "een leven-animatie hooguit eens per 20 tot 40 s, alleen als er geen held is"}
    meta["laars.png"] = {"frame": [8, 8], "gebruik": "na het spugen-frame 3 vliegt hij in een boogje 10 tot 14 spelpixels opzij (0,3 s, hele pixels), daarna ligt hij een tijdje naast de slijm op de vloer (buit van een held die vluchtte)"}
    meta["paneel.png"] = {"9slice": 4, "maat": [12, 12], "tekst": "kleur #ffe07a voor de kop, #f3e2c0 voor de regel; tekst begint 5 spelpixels (15 px) binnen de buitenkant, dus 1 spelpixel binnen de 9-slice-rand van 4; lettertype zoals nu in tekst.gd",
        "gebruik": "NinePatchRect (patch_margin 4 aan alle kanten, texture_filter nearest, schaal gelijk aan de strook) in plaats van het zwarte vlak"}
    meta["naamkaartje.png"] = {"9slice": 3, "maat": [10, 8], "tekst": "kleur #2a1a1f, naam van de aartsvijand; binnenkant 6 spelpixels hoog, dus lettergrootte hooguit 15 px op schaal 3, of een kaartje van 8 hoog op schaal 2 boven de strook bij hover",
        "gebruik": "onder de held als hij aartsvijand is (3 keer gevlucht) en onder elk bord op de wand van aartsvijanden"}
    meta["trofee.png"] = {"frame": [16, 16], "gebruik": "wand van aartsvijanden in de schatkamer: bord tegen de wand, de hoed van de held 4 spelpixels hoger erop, naamkaartje eronder"}
    json.dump(meta, open(pad, "w"), indent=1, ensure_ascii=False)
    voorbeeld(lijven, hoeden, wapens, littekens, hap_hoeden, kleuren, tekens, slijm, laars, paneel, kaart, trofee)
    import maak_aarde; maak_aarde.main()
    print("klaar")
