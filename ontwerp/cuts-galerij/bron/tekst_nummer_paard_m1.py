"""M1 van Daan (#129) op 'Numbered for assembly' met het paard (Beeldmaker, 26 nov 2026, issue #105).

python3 tekst_nummer_paard_m1.py <beeldenmap> <fontmap> [nummer-paard.json] [nummer-naad.json]

De zin links beloofde pengaten op elk snijvlak. De add-on zet geen pen waar er geen past ("Glue this joint"),
dus de zin wordt: "Cut faces get pin holes where a pin fits, and an engraved part number, like 5-9 where part 5
meets part 9." De renders zelf zijn niet bewaard, dus dit script haalt de oude zin en de getallenregel uit de
bestaande jpg's (inpainten op het egale donkere verloop links) en zet de nieuwe tekst erin met dezelfde letters,
maten en plek als tekst_nummer_paard.py (die heeft nu ook de nieuwe zin, voor een volgende render).
Beeld, paard en kaart blijven pixel voor pixel gelijk.
"""
import json
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

MAP, FONTS = sys.argv[1:3]
META = sys.argv[3] if len(sys.argv) > 3 else os.path.join(MAP, "nummer-paard.json")
NMETA = sys.argv[4] if len(sys.argv) > 4 else os.path.join(MAP, "nummer-naad.json")
GOUD, ZACHT = (255, 210, 92), (222, 212, 232)
W, H, X = 2400, 1350, 120


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


def regels(tekst, f, breed):
    uit, nu = [], ""
    for w in tekst.split(" "):
        t = (nu + " " + w).strip()
        if f.getlength(t) > breed and nu:
            uit.append(nu)
            nu = w
        else:
            nu = t
    return uit + [nu]


def lagen(zin, m):
    """Schaduw- en tekstlaag op 2400x1350, zoals schaduwtekst() in tekst_nummer_paard.py."""
    schaduw = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    tekst = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fz, fk = font("Inter.ttf", 44, "Medium"), font("Inter.ttf", 38, "SemiBold")
    y = 300 + 2 * 132 + 34
    regs = []
    for r in regels(zin, fz, 740):
        regs.append((r, y, fz, ZACHT))
        y += 62
    y += 40
    regs.append((f"{m['stukken']} parts, {m['pennen']} pins, every part numbered", y, fk, GOUD))
    for r, yy, f, kl in regs:
        s = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(s).text((X, yy), r, font=f, fill=(0, 0, 0, 170))
        schaduw.alpha_composite(s.filter(ImageFilter.GaussianBlur(6)))
        ImageDraw.Draw(tekst).text((X, yy), r, font=f, fill=kl)
    return schaduw, tekst, len(regs) - 1


def naar_doel(laag, maat):
    if maat == (2400, 1200):
        return laag.crop((0, 75, W, 75 + 1200))
    return laag.resize(maat, Image.LANCZOS)


def main():
    m, nm = json.load(open(META)), json.load(open(NMETA))
    a, b, lab = nm["stuk"], nm["buur"], nm["label"]
    oud = f"Cut faces get pin holes and an engraved part number, like {lab} where part {a} meets part {b}."
    nieuw = (f"Cut faces get pin holes where a pin fits, and an engraved part number, like {lab} where part {a} "
             f"meets part {b}.")
    _, oud_t, _ = lagen(oud, m)
    nw_s, nw_t, n = lagen(nieuw, m)
    print("regels nieuw:", n)
    for naam in ("nummer-paard-2400x1200.jpg", "nummer-paard-1920x1080.jpg"):
        p = os.path.join(MAP, naam)
        img = Image.open(p).convert("RGB")
        maat = img.size
        # masker: oude tekst plus de rand van zijn schaduw
        a_oud = np.array(naar_doel(oud_t, maat).split()[3])
        straal = int(26 * maat[0] / W)
        masker = cv2.dilate((a_oud > 8).astype(np.uint8) * 255, np.ones((2 * straal + 1,) * 2, np.uint8))
        bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        schoon = cv2.inpaint(bgr, masker, 25, cv2.INPAINT_TELEA)
        # inpainten laat vlekjes: binnen het masker zacht vervagen, met een zachte overgang
        vaag = cv2.GaussianBlur(schoon, (0, 0), 18)
        zacht = cv2.GaussianBlur(masker.astype(np.float32) / 255, (0, 0), 8)[..., None]
        schoon = (schoon * (1 - zacht) + vaag * zacht).astype(np.uint8)
        uit = Image.fromarray(cv2.cvtColor(schoon, cv2.COLOR_BGR2RGB)).convert("RGBA")
        uit.alpha_composite(naar_doel(nw_s, maat))
        uit.alpha_composite(naar_doel(nw_t, maat))
        uit.convert("RGB").save(p, quality=92)
        print("klaar", p)


main()
