"""Hol 2.0 proef (Olaf, #388): kleine kunst voor de proeftak.

Geen nieuwe tekeningen van figuren: de bestaande renders van Mila (kunst/3d) verkleind naar de doelmaat
(Gloop 20 spelpx, helden 16, hoeden 5) en per figuur op een klein palet gezet, zoals ontwerp-hol2/maak_schets.py.
Tegels (aarde, wand, ladder, gras, vallen, fakkel, troon) zijn eenvoudige pixeltegels uit een vast palet van 32
kleuren; ze worden vervangen door de tegels van Mila zodra die er zijn (issue Hol 2.0 kleine figuren).

Maak opnieuw:  python3 producten/steam-hol/godot/hol2/maak_kunst.py
"""
from PIL import Image, ImageDraw
import json, os, random

R = os.path.dirname(os.path.abspath(__file__))
K3 = os.path.join(os.path.dirname(R), "kunst", "3d")
UIT = os.path.join(R, "kunst")
os.makedirs(UIT, exist_ok=True)
SP = json.load(open(os.path.join(K3, "sprites.json")))
random.seed(7)


def figuur(naam, h, kleuren):
    d = SP[naam]
    cw, ch = d["cel_px"]
    blad = Image.open(os.path.join(K3, naam + ".png")).convert("RGBA")
    n = len(d["frames"])
    vak = None
    for i in range(n):
        b = blad.crop((i * cw, 0, i * cw + cw, ch)).getbbox()
        if b:
            vak = b if vak is None else (min(vak[0], b[0]), min(vak[1], b[1]), max(vak[2], b[2]), max(vak[3], b[3]))
    f = h / (vak[3] - vak[1])
    w = max(1, round((vak[2] - vak[0]) * f))
    uit = Image.new("RGBA", (w * n, h))
    for i in range(n):
        c = blad.crop((i * cw + vak[0], vak[1], i * cw + vak[2], vak[3])).resize((w, h), Image.LANCZOS)
        al = c.split()[3].point(lambda v: 255 if v > 100 else 0)
        q = c.convert("RGB").quantize(kleuren, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGBA")
        q.putalpha(al)
        uit.alpha_composite(q, (i * w, 0))
    uit.save(os.path.join(UIT, naam + ".png"))
    return {"w": w, "h": h, "frames": d["frames"], "anker_x": round((d.get("anker_x", cw // 2) - vak[0]) * f)}


info = {}
info["gloop"] = figuur("gloop", 20, 8)
for n in ("held0", "held1", "held2", "dief", "bard", "heks", "ridder"):
    info[n] = figuur(n, 16, 7)
info["hoeden"] = figuur("hoeden", 5, 5)

# ---- tegels (vast palet) ----
P = {
    "lucht": (0, 0, 0, 0),
    "gras1": (70, 132, 58), "gras2": (98, 162, 70), "gras3": (52, 100, 48), "gras4": (138, 190, 90),
    "aarde1": (74, 52, 38), "aarde2": (90, 64, 46), "aarde3": (58, 40, 30), "aarde4": (108, 78, 54),
    "wand1": (66, 60, 66), "wand2": (82, 74, 80), "wand3": (50, 46, 52), "voeg": (38, 34, 40),
    "vloer1": (104, 76, 52), "vloer2": (128, 94, 62), "vloer3": (78, 56, 40),
    "hout1": (140, 98, 58), "hout2": (104, 70, 42), "staal1": (176, 180, 188), "staal2": (118, 122, 132),
    "goud1": (246, 204, 76), "goud2": (214, 158, 46), "goud3": (150, 100, 30),
    "vuur1": (255, 214, 96), "vuur2": (240, 128, 44), "rood": (170, 52, 52), "paars": (120, 70, 140),
    "bloem1": (232, 96, 120), "bloem2": (240, 220, 110), "bloem3": (150, 160, 240), "zwart": (20, 16, 20),
}


def nieuw(w, h):
    return Image.new("RGBA", (w, h), (0, 0, 0, 0))


def ruis(img, box, kleuren, kans):
    x0, y0, x1, y1 = box
    for y in range(y0, y1):
        for x in range(x0, x1):
            if random.random() < kans:
                img.putpixel((x, y), P[random.choice(kleuren)] + (255,))


tegels = {}
# aarde 16x16
t = nieuw(16, 16); ImageDraw.Draw(t).rectangle((0, 0, 15, 15), fill=P["aarde1"])
ruis(t, (0, 0, 16, 16), ["aarde2", "aarde3", "aarde4"], 0.28); tegels["aarde"] = t
# wand van een kamer 16x8 (stenen)
t = nieuw(16, 8); d = ImageDraw.Draw(t); d.rectangle((0, 0, 15, 7), fill=P["wand1"])
for y in (3, 7): d.line((0, y, 15, y), fill=P["voeg"])
for x, y0 in ((5, 0), (13, 0), (1, 4), (9, 4)): d.line((x, y0, x, y0 + 2), fill=P["voeg"])
ruis(t, (0, 0, 16, 8), ["wand2", "wand3"], 0.18); tegels["wand"] = t
# vloer 8x4
t = nieuw(8, 4); d = ImageDraw.Draw(t); d.rectangle((0, 0, 7, 3), fill=P["vloer1"]); d.line((0, 0, 7, 0), fill=P["vloer2"])
d.line((0, 3, 7, 3), fill=P["vloer3"]); d.point((3, 1), fill=P["vloer3"]); tegels["vloer"] = t
# gras strook 16x6 (bovenkant tuin-grond)
t = nieuw(16, 6); d = ImageDraw.Draw(t); d.rectangle((0, 2, 15, 5), fill=P["gras1"])
for x in range(16):
    hh = random.choice((0, 1, 1, 2)); d.line((x, 2 - hh, x, 2), fill=P[random.choice(("gras2", "gras4", "gras1"))])
ruis(t, (0, 3, 16, 6), ["gras3", "gras2"], 0.3); tegels["gras"] = t
# ladder 7 breed, 4 hoog (herhaalt)
t = nieuw(7, 4); d = ImageDraw.Draw(t); d.line((0, 0, 0, 3), fill=P["hout2"]); d.line((6, 0, 6, 3), fill=P["hout2"])
d.line((1, 1, 5, 1), fill=P["hout1"]); tegels["ladder"] = t
# fakkel 2 beelden, 5x8
for i in range(2):
    t = nieuw(5, 9); d = ImageDraw.Draw(t); d.line((2, 5, 2, 8), fill=P["hout2"]); d.line((1, 5, 3, 5), fill=P["hout1"])
    d.rectangle((1, 2, 3, 4), fill=P["vuur2"]); d.point((2, 3), fill=P["vuur1"]); d.point((1 + 2 * i, 1), fill=P["vuur2"]); d.point((2, 1 - i if i == 0 else 2), fill=P["vuur1"]); d.point((2, 0 + i), fill=P["vuur1"])
    tegels["fakkel%d" % i] = t
# luik dicht en open, 12x4
t = nieuw(12, 4); d = ImageDraw.Draw(t); d.rectangle((0, 0, 11, 3), fill=P["zwart"]); d.rectangle((1, 0, 10, 2), fill=P["hout1"])
d.line((4, 0, 4, 2), fill=P["hout2"]); d.line((7, 0, 7, 2), fill=P["hout2"]); d.point((5, 1), fill=P["staal1"]); d.point((6, 1), fill=P["staal1"]); tegels["luik"] = t
t = nieuw(12, 4); d = ImageDraw.Draw(t); d.rectangle((0, 0, 11, 3), fill=P["zwart"]); d.line((0, 0, 0, 3), fill=P["hout1"]); d.line((11, 0, 11, 3), fill=P["hout1"])
tegels["luik_open"] = t
# stekelput 12x6
t = nieuw(12, 6); d = ImageDraw.Draw(t); d.rectangle((0, 2, 11, 5), fill=P["zwart"])
for x in range(1, 12, 2): d.line((x, 1, x, 4), fill=P["staal2"]); d.point((x, 0), fill=P["staal1"])
tegels["stekels"] = t
# troon met schat, 26x16
t = nieuw(26, 16); d = ImageDraw.Draw(t)
d.rectangle((2, 2, 11, 15), fill=P["paars"]); d.rectangle((0, 0, 13, 2), fill=P["goud2"]); d.rectangle((0, 12, 13, 15), fill=P["goud3"])
d.point((6, 0), fill=P["rood"]); d.point((7, 0), fill=P["rood"])
for i, (x, y) in enumerate(((15, 15), (17, 15), (19, 15), (21, 15), (23, 15), (16, 14), (18, 14), (20, 14), (22, 14), (17, 13), (19, 13), (21, 13), (18, 12), (20, 12), (19, 11))):
    d.point((x, y), fill=P["goud1" if i % 3 else "goud2"]); d.point((x + 1, y), fill=P["goud2"])
d.rectangle((14, 13, 16, 15), fill=P["hout2"]); tegels["troon"] = t
# bloemen en struik
for i, k in enumerate(("bloem1", "bloem2", "bloem3")):
    t = nieuw(5, 6); d = ImageDraw.Draw(t); d.line((2, 2, 2, 5), fill=P["gras3"]); d.point((1, 4), fill=P["gras2"])
    d.point((2, 1), fill=P[k]); d.point((1, 1), fill=P[k]); d.point((3, 1), fill=P[k]); d.point((2, 0), fill=P[k]); d.point((2, 1), fill=P["bloem2"] if k != "bloem2" else P["goud2"])
    tegels["bloem%d" % i] = t
t = nieuw(12, 8); d = ImageDraw.Draw(t); d.ellipse((0, 1, 11, 9), fill=P["gras3"]); d.ellipse((2, 0, 9, 6), fill=P["gras1"])
ruis(t, (1, 1, 11, 7), ["gras2", "gras4"], 0.12)
for x in range(12):
    for y in range(8):
        if t.getpixel((x, y))[3] and not (0 < x < 11): pass
tegels["struik"] = t
# kool (tuin, iets om te eten), 6x5
t = nieuw(6, 5); d = ImageDraw.Draw(t); d.ellipse((0, 0, 5, 4), fill=P["gras2"]); d.point((2, 1), fill=P["gras4"]); d.point((3, 2), fill=P["gras3"]); tegels["kool"] = t
# zzz en munt (2x2)
t = nieuw(3, 3); d = ImageDraw.Draw(t); d.line((0, 0, 2, 0), fill=(230, 230, 240)); d.point((1, 1), fill=(230, 230, 240)); d.line((0, 2, 2, 2), fill=(230, 230, 240)); tegels["z"] = t
t = nieuw(2, 2); d = ImageDraw.Draw(t); d.rectangle((0, 0, 1, 1), fill=P["goud1"]); d.point((1, 1), fill=P["goud3"]); tegels["munt"] = t

# alle tegels op één blad, posities in de json
x = 0; blad_h = max(t.height for t in tegels.values()); vakken = {}
blad = nieuw(sum(t.width + 1 for t in tegels.values()), blad_h)
for n, t in tegels.items():
    blad.alpha_composite(t, (x, 0)); vakken[n] = [x, 0, t.width, t.height]; x += t.width + 1
blad.save(os.path.join(UIT, "tegels.png"))
info["tegels"] = vakken
json.dump(info, open(os.path.join(UIT, "kunst.json"), "w"), indent=1)
print("klaar:", {k: (v["w"], v["h"]) for k, v in info.items() if k != "tegels"}, len(vakken), "tegels")
