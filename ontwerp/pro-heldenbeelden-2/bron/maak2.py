"""Heldenbeelden ronde 2 afmaken (heldenbeelden-maker, 24 nov 2026): titel op beeld 1 en 2, de inzet (scherpe
close-up van het kniescharnier) op beeld 1, elk beeld in 2400 x 1200 (Superhive) en 1920 x 1080 (Gumroad), en
overzicht.png met alle vier (beeld 3 en 4 uit ronde 1, die blijven).

python3 maak2.py <rendermap> <uitmap> <fontmap> <icoon.svg> <map met held-3 en held-4 uit ronde 1>

Hergebruikt titel() en opslaan() uit ontwerp/pro-heldenbeelden-1/bron/maak.py (zelfde letters, icoon en uitsnede).
"""
import json
import os
import shutil
import sys

from PIL import Image, ImageDraw, ImageFilter

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "pro-heldenbeelden-1", "bron"))
import maak as M1  # noqa: E402  (leest zelf sys.argv[1:5]: rendermap, uitmap, fontmap, icoon)

RENDER, UIT, FONTS, ICOON, RONDE1 = sys.argv[1:6]
GOUD = (255, 196, 92)


def laad(naam, maat=(2400, 1200)):
    p = os.path.join(RENDER, f"b-{naam}.png")
    return Image.open(p).convert("RGBA").resize(maat, Image.LANCZOS) if os.path.exists(p) else None


def gloed_lijn(img, punten, breed, kleur, gloed=True):
    W, H = img.size
    laag = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lagen = ((breed * 6, kleur + (50,)), (breed * 2.5, kleur + (110,)), (breed, kleur + (255,))) if gloed else \
        ((breed, kleur + (255,)),)
    for b, k in lagen:
        l2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(l2).line(punten, fill=k, width=int(round(b)))
        if b > breed:
            l2 = l2.filter(ImageFilter.GaussianBlur(b / 2.5))
        laag = Image.alpha_composite(laag, l2)
    img.alpha_composite(laag)


def inzet(img, close, midden, straal, doel):
    """Rond venster met de close-up, dunne gouden rand met gloed, een lijn naar het kniescharnier en een ringetje
    om het scharnier."""
    cx, cy = midden
    d = 2 * straal
    c = close.resize((d, d), Image.LANCZOS)
    masker = Image.new("L", (d * 4, d * 4), 0)
    ImageDraw.Draw(masker).ellipse((0, 0, d * 4 - 1, d * 4 - 1), fill=255)
    masker = masker.resize((d, d), Image.LANCZOS)
    # schaduw onder het venster
    sch = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).ellipse((cx - straal + 6, cy - straal + 14, cx + straal + 6, cy + straal + 14),
                                fill=(0, 0, 0, 170))
    img.alpha_composite(sch.filter(ImageFilter.GaussianBlur(22)))
    # lijn van de rand van het venster naar het scharnier (achter het venster langs)
    dx, dy = doel[0] - cx, doel[1] - cy
    L = (dx * dx + dy * dy) ** 0.5
    ring_r = 34
    start = (cx + dx / L * straal, cy + dy / L * straal)
    eind = (doel[0] - dx / L * ring_r, doel[1] - dy / L * ring_r)
    gloed_lijn(img, [start, eind], 3, GOUD)
    img.paste(c, (cx - straal, cy - straal), masker)
    rand = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(rand).ellipse((cx - straal, cy - straal, cx + straal, cy + straal), outline=GOUD + (255,), width=5)
    gl = rand.filter(ImageFilter.GaussianBlur(9))
    img.alpha_composite(gl)
    img.alpha_composite(rand)
    ring = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((doel[0] - ring_r, doel[1] - ring_r, doel[0] + ring_r, doel[1] + ring_r),
                                 outline=GOUD + (255,), width=4)
    img.alpha_composite(ring.filter(ImageFilter.GaussianBlur(6)))
    img.alpha_composite(ring)


if __name__ == "__main__":
    os.makedirs(UIT, exist_ok=True)
    gemaakt = []
    im = laad("knie")
    if im is not None:
        M1.titel(im, 230, 110, 0.80)
        close = laad("knie-inzet", (1000, 1000))
        meta = json.load(open(os.path.join(RENDER, "b-knie.json"))) if os.path.exists(
            os.path.join(RENDER, "b-knie.json")) else {}
        kx, ky = meta.get("knie_in_beeld", [0.61, 0.33])
        if close is not None:
            inzet(im, close, (int(os.environ.get("INZET_CX", "600")), int(os.environ.get("INZET_CY", "790"))),
                  int(os.environ.get("INZET_STRAAL", "290")), (kx * 2400, ky * 1200))
        gemaakt.append(M1.opslaan(im, "held-1-knie", midden=0.5))
    im = laad("spiraal")
    if im is not None:
        M1.titel(im, 230, 110, 0.80)
        gemaakt.append(M1.opslaan(im, "held-2-spiraal", midden=0.5))
        # 16:9 apart: de delen lopen tot x 0,97, dus het vak rechts tegen de rand en de titel er daarna op, zodat de
        # voet rechts niet wegvalt
        kaal = laad("spiraal")
        w = int(1200 * 16 / 9)
        vak = kaal.crop((2400 - w, 0, 2400, 1200))
        M1.titel(vak, int(os.environ.get("TITEL169_X", "190")), 110, float(os.environ.get("TITEL169_S", "0.74")))
        vak.convert("RGB").resize((1920, 1080), Image.LANCZOS).save(
            os.path.join(UIT, "held-2-spiraal-1920x1080.png"), optimize=True)
    for n in ("held-3-voor-na", "held-4-fit-test-strip"):
        for f in ("2400x1200", "1920x1080"):
            bron = os.path.join(RONDE1, f"{n}-{f}.png")
            if os.path.exists(bron):
                shutil.copy(bron, os.path.join(UIT, f"{n}-{f}.png"))
    # overzicht voor de keurder: alle vier groot (1200 x 600) en klein zoals in een lijst (384 x 216, 16:9)
    namen = ["held-1-knie", "held-2-spiraal", "held-3-voor-na", "held-4-fit-test-strip"]
    groot = [Image.open(os.path.join(UIT, f"{n}-2400x1200.png")).resize((1200, 600), Image.LANCZOS)
             for n in namen if os.path.exists(os.path.join(UIT, f"{n}-2400x1200.png"))]
    if groot:
        ov = Image.new("RGB", (2 * 1200 + 60, 2 * 620 + 20 + 260), (236, 236, 240))
        for i, g in enumerate(groot):
            ov.paste(g, (20 + (i % 2) * 1220, 20 + (i // 2) * 620))
        for i, n in enumerate(namen[:len(groot)]):
            k = Image.open(os.path.join(UIT, f"{n}-1920x1080.png")).resize((384, 216), Image.LANCZOS)
            ov.paste(k, (20 + i * 404, 2 * 620 + 30))
        ov.save(os.path.join(UIT, "overzicht.png"), optimize=True)
        gemaakt.append(os.path.join(UIT, "overzicht.png"))
    for f in os.listdir(UIT):
        if f.startswith("_icoon"):
            os.remove(os.path.join(UIT, f))
    print("gemaakt:", [os.path.basename(g) for g in gemaakt if g])
