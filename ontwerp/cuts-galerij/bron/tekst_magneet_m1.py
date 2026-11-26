"""Magneetbeeld zegt wat de add-on doet (Beeldmaker, 26 nov 2026, issue #200).

python3 tekst_magneet_m1.py <beeldenmap> <fontmap> [magneet-paard.json]

Het beeld beloofde "Magnet holes in every cut" en "Both sides of every cut get a hole". De add-on slaat een gat
over waar de magneet niet past ("glue this joint"); de gekeurde winkeltekst zegt "each cut where it fits"
(Daan M1 #189). Titel wordt "Magnet holes / or pins.", de zin noemt "where a disc magnet fits".
De renders zijn niet bewaard, dus dit script haalt het hele linker tekstblok (titel, zin, getallen) uit de
bestaande jpg's (inpainten op het egale donkere verloop) en zet de nieuwe tekst erin met dezelfde letters, maten
en plek als tekst_magneet.py (die heeft nu ook de nieuwe tekst, voor een volgende render). Merk, paard en kaart
blijven pixel voor pixel gelijk. Zelfde aanpak als tekst_nummer_paard_m1.py (M1 #129).
"""
import json
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

MAP, FONTS = sys.argv[1:3]
META = sys.argv[3] if len(sys.argv) > 3 else os.path.join(MAP, "magneet-paard.json")
CREME, GOUD, ZACHT = (255, 246, 230), (255, 210, 92), (222, 212, 232)
W, H, X = 2400, 1350, 120

OUD_TITEL = (("Magnet holes", CREME), ("in every cut.", GOUD))
OUD_ZIN = "Pick Magnets instead of pins. Both sides of every cut get a hole for a disc magnet, sized with your clearance."
NW_TITEL = (("Magnet holes", CREME), ("or pins.", GOUD))
NW_ZIN = "Pick Magnets instead of pins: each cut gets a hole on both sides where a disc magnet fits, sized with your clearance."


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


def lagen(titel, zin, m):
    """Schaduw- en tekstlaag op 2400x1350, zoals main() en schaduwtekst() in tekst_magneet.py."""
    ft = font("Bricolage.ttf", 112, "ExtraBold")
    fz = font("Inter.ttf", 44, "Medium")
    regs = []
    y = 300
    for r, kl in titel:
        regs.append((r, y, ft, kl, 10))
        y += 132
    y += 34
    for r in regels(zin, fz, 740):
        regs.append((r, y, fz, ZACHT, 6))
        y += 62
    y += 40
    regs.append((f"{m['stukken']} parts, {m['pennen']} magnet holes", y, font("Inter.ttf", 38, "SemiBold"), GOUD, 6))
    regs.append(("5 sizes, 5x2 to 10x3 mm. Magnets not included.", y + 58, font("Inter.ttf", 32, "Medium"), ZACHT, 5))
    schaduw = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    tekst = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for r, yy, f, kl, s in regs:
        laag = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(laag).text((X, yy), r, font=f, fill=(0, 0, 0, 170))
        schaduw.alpha_composite(laag.filter(ImageFilter.GaussianBlur(s)))
        ImageDraw.Draw(tekst).text((X, yy), r, font=f, fill=kl)
    return schaduw, tekst


def naar_doel(laag, maat):
    if maat == (2400, 1200):
        return laag.crop((0, 75, W, 75 + 1200))
    return laag.resize(maat, Image.LANCZOS)


def main():
    m = json.load(open(META))
    _, oud_t = lagen(OUD_TITEL, OUD_ZIN, m)
    nw_s, nw_t = lagen(NW_TITEL, NW_ZIN, m)
    for naam in ("magneet-2400x1200.jpg", "magneet-1920x1080.jpg"):
        p = os.path.join(MAP, naam)
        img = Image.open(p).convert("RGB")
        maat = img.size
        a_oud = np.array(naar_doel(oud_t, maat).split()[3])
        straal = int(30 * maat[0] / W)
        masker = cv2.dilate((a_oud > 8).astype(np.uint8) * 255, np.ones((2 * straal + 1,) * 2, np.uint8))
        bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        schoon = cv2.inpaint(bgr, masker, 25, cv2.INPAINT_TELEA)
        vaag = cv2.GaussianBlur(schoon, (0, 0), 18)
        zacht = cv2.GaussianBlur(masker.astype(np.float32) / 255, (0, 0), 8)[..., None]
        schoon = (schoon * (1 - zacht) + vaag * zacht).astype(np.uint8)
        uit = Image.fromarray(cv2.cvtColor(schoon, cv2.COLOR_BGR2RGB)).convert("RGBA")
        uit.alpha_composite(naar_doel(nw_s, maat))
        uit.alpha_composite(naar_doel(nw_t, maat))
        uit.convert("RGB").save(p, quality=92)
        print("klaar", p)


main()
