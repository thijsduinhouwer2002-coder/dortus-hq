"""Maakt van de renders (kunst/render.sh) de plaatjes voor het spel: schaduw eraf, bijsnijden, op maat.

Gebruik: python3 kunst/knip.py <rendermap> <app/public/kunst>
Maten in spel-eenheden (de speelstrook is 454 breed). De plaatjes zijn 2,6 keer zo groot, zodat ze op een
telefoon met een scherp scherm (3x) niet wazig worden. De ankers (kruin, mond) gaan naar kunst.json.
"""
import json
import sys
from pathlib import Path

from PIL import Image

BRON = Path(sys.argv[1])
UIT = Path(sys.argv[2])
# --alleen-helden: alleen de soorten held bijwerken (ridder uit de bestaande plaatjes in UIT).
ALLEEN_HELDEN = "--alleen-helden" in sys.argv
UIT.mkdir(parents=True, exist_ok=True)
PX = 2.6  # pixels per eenheid
GLOOP_B = 176  # breedte van Gloop in eenheden (horloge: 154)
HELD_H = 128  # hoogte van een staande held
HELM_B = 86  # breedte van de helm; de andere hoeden houden hun maat ten opzichte daarvan


def zonder_schaduw(im):
    """De vloer van de render vangt schaduw: zwart met een beetje alfa. Die halen we weg."""
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a < 252 and max(r, g, b) < 40:
                px[x, y] = (0, 0, 0, 0)
    return im


def vak(im, drempel=10):
    return im.split()[3].point(lambda v: 255 if v > drempel else 0).getbbox()


def op_maat(im, breedte_eenheden):
    f = breedte_eenheden * PX / im.width
    return im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS), f


if ALLEEN_HELDEN:
    uit_json = json.loads((UIT / "kunst.json").read_text())
else:
    uit_json = {"px": PX}

def alles():
    global uit_json
    uit_json = {"px": PX}

    # ---------- Gloop: alle standen met hetzelfde kader, zodat ze precies op elkaar vallen ----------
    standen = ["rust", "hap", "blij", "knipper", "kneep"]
    gl = {s: zonder_schaduw(Image.open(BRON / f"gloop-{s}.png")) for s in standen}
    kaders = [vak(im) for im in gl.values()]
    kader = (min(k[0] for k in kaders), min(k[1] for k in kaders), max(k[2] for k in kaders), max(k[3] for k in kaders))
    for s, im in gl.items():
        gl[s] = im.crop(kader)
    rust = gl["rust"]
    # Kruin: het hoogste punt van het lijf in het middelste derde.
    a = rust.split()[3]
    kruin = None
    for y in range(rust.height):
        for x in range(rust.width // 3, rust.width * 2 // 3):
            if a.getpixel((x, y)) > 128:
                kruin = (x, y)
                break
        if kruin:
            break
    # Mond in de hap: het donkere rood-bruine vlak.
    hap = gl["hap"]
    mx = []
    my = []
    hp = hap.load()
    for y in range(int(hap.height * 0.55), hap.height):
        for x in range(hap.width):
            r, g, b, al = hp[x, y]
            if al > 250 and 50 < r < 140 and g < 60 and b < 80 and r > g + 20:
                mx.append(x)
                my.append(y)
    mond = ((min(mx) + max(mx)) / 2, (min(my) + max(my)) / 2, (max(mx) - min(mx)) / 2, (max(my) - min(my)) / 2)
    f = GLOOP_B * PX / rust.width
    for s, im in gl.items():
        im2 = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
        im2.save(UIT / f"gloop-{s}.png", optimize=True)
    uit_json["gloop"] = {
        "b": GLOOP_B,
        "h": round(rust.height * f / PX, 1),
        "kruin": [round(kruin[0] * f / PX, 1), round(kruin[1] * f / PX, 1)],
        "mond": [round(v * f / PX, 1) for v in mond],
    }

    # ---------- held (zonder hoed; het spel zet de hoed erop) ----------
    uit_json["held"] = {}
    for s in ["schrik", "vallen", "stap1", "stap2"]:
        im = zonder_schaduw(Image.open(BRON / f"held-{s}.png"))
        im = im.crop(vak(im))
        f = HELD_H * PX / im.height if s != "vallen" else None
        if s == "vallen":
            f = uit_json["held"]["schrik"]["f"]
        im2 = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
        im2.save(UIT / f"held-{s}.png", optimize=True)
        # Kruin van het hoofd (voor de hoed): hoogste punt.
        al = im2.split()[3]
        top = None
        for y in range(im2.height):
            for x in range(im2.width):
                if al.getpixel((x, y)) > 128:
                    top = (x, y)
                    break
            if top:
                break
        uit_json["held"][s] = {
            "b": round(im2.width / PX, 1),
            "h": round(im2.height / PX, 1),
            "kruin": [round(top[0] / PX, 1), round(top[1] / PX, 1)],
            "f": f,
        }
    for s in uit_json["held"].values():
        s.pop("f")

    # ---------- hoeden ----------
    hoeden = [zonder_schaduw(Image.open(BRON / f"hoed-{n}.png")) for n in range(10)]
    hoeden = [im.crop(vak(im)) for im in hoeden]
    f = HELM_B * PX / hoeden[0].width
    uit_json["hoed"] = []
    for n, im in enumerate(hoeden):
        im2 = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
        im2.save(UIT / f"hoed-{n}.png", optimize=True)
        uit_json["hoed"].append({"b": round(im2.width / PX, 1), "h": round(im2.height / PX, 1)})



if not ALLEEN_HELDEN:
    alles()

# ---------- alle soorten held (ridder en de extra renders held-<soort>-<stand>.png), zelfde maat ----------
uit_json["helden"] = []
for soort in ["ridder", "heks0", "held0", "held2", "dief0", "bard0"]:
    maten = {}
    for s in ["schrik", "stap1", "stap2"]:
        if soort == "ridder":
            bron = (UIT / f"held-{s}.png") if ALLEEN_HELDEN else (BRON / f"held-{s}.png")
        else:
            bron = BRON / f"held-{soort}-{s}.png"
        im = zonder_schaduw(Image.open(bron))
        im = im.crop(vak(im))
        f = HELD_H * PX / im.height
        im2 = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
        im2.save(UIT / f"held-{soort}-{s}.png", optimize=True)
        al = im2.split()[3]
        top = next((x, y) for y in range(im2.height) for x in range(im2.width) if al.getpixel((x, y)) > 128)
        maten[s] = {"b": round(im2.width / PX, 1), "h": round(im2.height / PX, 1), "kruin": [round(top[0] / PX, 1), round(top[1] / PX, 1)]}
    uit_json["helden"].append(maten)

(UIT / "kunst.json").write_text(json.dumps(uit_json, indent=1))
print(json.dumps(uit_json))
