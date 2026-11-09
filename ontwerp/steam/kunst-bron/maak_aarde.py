# Daan: aarde met lagen en vondsten voor Het Hol (keuring build 408d67b, punt 5: aarde was één bruin vlak).
# Uitvoer: producten/steam-hol/godot/kunst/aarde_lagen.png, vondsten.png, en kunst-bron/voorbeeld-aarde.png.
# Wordt gedraaid door maak_karakter.py (draai alleen dat: maak_kunst.py schrijft kunst.json opnieuw). Naadloos in de breedte: de lagen lopen over de celgrens door.
import json, math, os, random, sys
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import maak_kunst as mk

P, sprite, strip, opslaan, UIT, CEL = mk.P, mk.sprite, mk.strip, mk.opslaan, mk.UIT, mk.CEL
P["A"] = mk.hx("6c4262")   # aarde tussentoon (tussen 3 en 4)
P["a"] = mk.hx("4d3050")   # aarde tussentoon (tussen 2 en 3)
P["d"] = mk.hx("2e1f3b")   # diepe aarde
P["D"] = mk.hx("372644")   # diepe aarde licht

# per diepte: grondkleur, licht, donker
LAGEN = [("A", "4", "3"), ("3", "A", "a"), ("a", "3", "d")]

def golf(x, fase, hoogte):
    # laaglijn die naadloos over 16 pixels loopt
    return int(round(hoogte * math.sin(2 * math.pi * (x + fase) / 16)))

def cel(rij, var):
    rnd = random.Random(1000 + rij * 37 + var)
    grond, licht, donker = LAGEN[min(rij, 2)]
    im = Image.new("RGBA", (CEL, CEL), P[grond])
    px = im.load()
    # korrel: kleine gedithterde vlekjes, geen herkenbare vormen
    for _ in range(26):
        x, y = rnd.randrange(16), rnd.randrange(16)
        px[x, y] = P[licht if rnd.random() < 0.5 else donker]
        if rnd.random() < 0.35 and x < 15: px[x + 1, y] = px[x, y]
    # sedimentlaag: dunne golvende streep op vaste hoogte (naadloos), per diepte anders
    yl = (5, 10, 7)[min(rij, 2)]
    for x in range(16):
        y = yl + golf(x, 3 * rij, 1)
        if (x + 2 * rij) % 7 not in (0, 1): px[x, y] = P[donker]
        if (x + rij) % 3 == 0: px[x, y - 1] = P[licht]
    # overgang naar de laag erboven: gedithterd, zodat de celgrens geen harde lijn is
    if rij >= 1:
        boven = LAGEN[min(rij, 2) - 1][0]
        for x in range(16):
            if (x + var) % 2 == 0: px[x, 0] = P[boven]
            if (x + var) % 4 == 1: px[x, 1] = P[boven]
    # rij 0: wortels van het gras naar beneden
    if rij == 0:
        for _ in range(rnd.randint(2, 3)):
            x = rnd.randint(1, 14); y = 0
            for i in range(rnd.randint(4, 9)):
                px[x, y] = P["u" if i < 3 else "U"] if i % 3 else P["u"]
                y += 1
                if rnd.random() < 0.35: x = max(0, min(15, x + rnd.choice((-1, 1))))
                if y > 15: break
    # steentjes: meer naar beneden
    for _ in range(1 if rnd.random() < 0.25 + 0.15 * min(rij, 2) else 0):
        x, y = rnd.randint(1, 12), rnd.randint(1, 12)
        st = [".77.", "7898", "7787", ".77."] if rnd.random() < 0.5 else ["79.", "787"]
        for yy, r in enumerate(st):
            for xx, c in enumerate(r):
                if c != ".": px[x + xx, y + yy] = P[c]
    # diepe rij: kristaladertje af en toe
    if rij >= 2 and var % 3 == 0:
        x, y = rnd.randint(3, 11), rnd.randint(3, 10)
        for yy, r in enumerate([".q.", "NnM", ".m."]):
            for xx, c in enumerate(r):
                if c != ".": px[x + xx, y + yy] = P[c]
    return im

def maak_lagen():
    blad = Image.new("RGBA", (CEL * 8, CEL * 3), (0, 0, 0, 0))
    for rij in range(3):
        for v in range(8): blad.paste(cel(rij, v), (v * CEL, rij * CEL))
    opslaan(blad, "aarde_lagen.png")
    return blad

# vondsten: begraven in de aarde, zeldzaam (ongeveer 1 op 10 aardecellen), zelfde 16 x 16
VONDSTEN = {
    "helm": ["................", "................", "................", "................",
             "................", "................", ".....kkkkk......", "....kiIjIik.....",
             "...kiIIIIIik....", "...kkkkkkkkk....", "................", "................",
             "................", "................", "................", "................"],
    "zwaard": ["................", "................", "..........kk....", ".........kjk....",
               "........kjk.....", ".......kjk......", "......kIk.......", "...kkkIk........",
               "....kyk.........", "...koyk.........", "..kok.kk........", "...k............",
               "................", "................", "................", "................"],
    "botten": ["................", "................", "................", "................",
               "................", "................", "................", "..kk.......kk...",
               ".kjjIIIIIIIjjk..", "..kk...kk..kk...", "......kjjk......", ".....kjeejk.....",
               ".....kjjjjk.....", "......kjk.......", "................", "................"],
    "fossiel": ["................", "................", "................", "................",
                "................", ".....kkkk.......", "....k9888k......", "...k98kk78k.....",
                "...k8k97k8k.....", "...k8kk78k......", "...k988kk.......", "....k9888kk.....",
                ".....kkkk.......", "................", "................", "................"],
    "pot": ["................", "................", "................", "................",
            "................", "................", "......kkkk......", ".....kOyYOk.....",
            "....kUUUUUUk....", "....kU5UUUuk....", "....kUUUUUuk....", ".....kuuuuk.....",
            "......kkkk......", "................", "................", "................"],
}

def maak_vondsten():
    frames = [sprite(VONDSTEN[n]) for n in VONDSTEN]
    opslaan(strip(frames), "vondsten.png")
    return frames

def voorbeeld(lagen, vondsten, schaal=3, breedte=40, rijen=3):
    tegels = Image.open(os.path.join(UIT, "tegels.png")).convert("RGBA")
    gras = Image.open(os.path.join(UIT, "gras.png")).convert("RGBA")
    W, H = breedte * CEL, mk.OPP + rijen * CEL
    c = Image.new("RGBA", (W, H), (120, 170, 220, 255))
    rnd = random.Random(7)
    gang = {(1, k) for k in range(4, 22)} | {(0, 4)} | {(0, k) for k in range(17, 21)}
    for r in range(rijen):
        for k in range(breedte):
            x, y = k * CEL, mk.OPP + r * CEL
            if (r, k) in gang:
                n = (r - 1, k) not in gang; s = (r + 1, k) not in gang
                w = (r, k - 1) not in gang; e = (r, k + 1) not in gang
                idx = n * 1 + e * 2 + s * 4 + w * 8
                c.alpha_composite(tegels.crop((idx * CEL, CEL, idx * CEL + CEL, 2 * CEL)), (x, y))
            else:
                v = rnd.randrange(8)
                c.alpha_composite(lagen.crop((v * CEL, min(r, 2) * CEL, v * CEL + CEL, min(r, 2) * CEL + CEL)), (x, y))
                if rnd.random() < 0.09:
                    c.alpha_composite(vondsten[rnd.randrange(len(vondsten))], (x, y))
    for k in range(breedte):
        c.alpha_composite(gras.crop(((k % 4) * 16, 0, (k % 4) * 16 + 16, 8)), (k * CEL, 0))
    c.resize((W * schaal, H * schaal), Image.NEAREST).save(os.path.join(HIER, "voorbeeld-aarde.png"))

def main():
    lagen = maak_lagen(); vondsten = maak_vondsten()
    pad = os.path.join(UIT, "kunst.json"); meta = json.load(open(pad))
    meta["aarde_lagen.png"] = {"frame": [16, 16], "rijen": ["rij 0: bovenste rij cellen (wortels)", "rij 1: tweede rij", "rij 2: alles dieper (bij een hogere strook)"],
        "varianten": 8, "gebruik": "vervangt rij 0 van tegels.png: kies de rij op diepte en de variant willekeurig (vast zaad). De laaglijn loopt naadloos over de celgrens."}
    meta["vondsten.png"] = {"frame": [16, 16], "volgorde": list(VONDSTEN),
        "gebruik": "over een aardecel tekenen, ongeveer 1 op 10 (niet vaker, anders wordt het rommelig), vast zaad; verdwijnt als de cel gegraven wordt. Later kan graven een vondst opleveren (Sanne beslist)."}
    json.dump(meta, open(pad, "w"), indent=1, ensure_ascii=False)
    voorbeeld(lagen, vondsten)
    print("klaar")

if __name__ == "__main__":
    main()
