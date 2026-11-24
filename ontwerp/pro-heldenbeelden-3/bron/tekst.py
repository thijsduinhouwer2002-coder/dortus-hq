"""Heldenbeelden ronde 3 (Bram, 24 nov 2026, opdracht hoofdchat 21:05): titel en een regel wat het doet op held-1 tot
en met held-4, zodat elk beeld los te snappen is. De blinde test zei over held-3: "geen tekst, niemand snapt wat het
doet". De renders zelf blijven die van ronde 2 (release pro-heldenbeelden-2), hier komt alleen tekst bij.

python3 tekst.py <map met held-*-2400x1200.png en held-*-1920x1080.png> <uitmap> <fontmap> <icoon.svg>

Held-3 en held-4 hebben bovenaan geen plek voor tekst: het beeld wordt kleiner (KRIMP) naar rechtsonder gezet op
een kale achtergrond in de kleuren van zijn eigen randen, zodat de achtergrond doorloopt.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter

BRON, UIT, FONTS, ICOON = sys.argv[1:5]
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "..", "pro-heldenbeelden-1", "bron"))
sys.argv = [sys.argv[0], BRON, UIT, FONTS, ICOON]
import maak as M1  # noqa: E402  (titel, font, icoon; leest sys.argv[1:5])

CREME, GOUD = M1.CREME, M1.GOUD
ZACHT = (232, 222, 210)

REGELS = {
    "held-1-knie": ["Hinge joints with real end stops,", "ready to print."],
    "held-2-spiraal": ["One click turns your rigged figure", "into 10 printable, jointed parts."],
    "held-3-voor-na": ["Rig in. Joints out.", "Turns a rigged character into printable, jointed parts."],
    "held-4-fit-test-strip": ["Fit test strip", "One small print shows which clearance clicks on your printer."],
}


def schrijf(img, xy, regels, maat, eerste_goud=False, gewicht="Medium"):
    """Regels tekst met een zachte schaduw; de eerste regel eventueel goud en vet."""
    x, y = xy
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    plekken = []
    for i, r in enumerate(regels):
        groot = eerste_goud and i == 0
        f = M1.font("Bricolage.ttf" if groot else "Inter.ttf", int(maat * (1.25 if groot else 1)),
                    "Bold" if groot else gewicht)
        plekken.append((x, y, r, f, GOUD if groot else ZACHT))
        d.text((x, y + 3), r, font=f, fill=(0, 0, 0, 160))
        bb = d.textbbox((x, y), r, font=f)
        y = bb[3] + int(maat * 0.45)
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(img)
    for x_, y_, r, f, k in plekken:
        d.text((x_, y_), r, font=f, fill=k)
    return y


def label(img, midden_x, y, woord, maat):
    f = M1.font("Inter.ttf", maat, "Bold")
    d = ImageDraw.Draw(img)
    bb = d.textbbox((0, 0), woord, font=f)
    w = bb[2] - bb[0]
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).text((midden_x - w / 2, y + 3), woord, font=f, fill=(0, 0, 0, 170))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(8)))
    d.text((midden_x - w / 2, y), woord, font=f, fill=GOUD)


def krimp(img, f, rechts=0.03, onder=0.0):
    W, H = img.size
    # achtergrond zonder figuren: per rij de kleur van de linker- en rechterrand, daartussen een overgang
    rgb = img.convert("RGB")
    kl = rgb.crop((0, 0, max(8, W // 60), H)).resize((1, H), Image.BOX)
    kr = rgb.crop((W - max(8, W // 60), 0, W, H)).resize((1, H), Image.BOX)
    twee = Image.new("RGB", (2, H))
    twee.paste(kl, (0, 0))
    twee.paste(kr, (1, 0))
    achter = twee.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(20)).convert("RGBA")
    k = img.resize((int(W * f), int(H * f)), Image.LANCZOS)
    rand = int(min(k.size) * 0.12)
    m = Image.new("L", k.size, 0)
    ImageDraw.Draw(m).rectangle((rand, rand, k.width - rand, k.height - rand), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(rand / 2.2))
    x, y = int(W - k.width - W * rechts), int(H - k.height - H * onder)
    achter.paste(k, (x, y), m)
    return achter, (x, y, k.width, k.height)


def laad(naam, fmt):
    return Image.open(os.path.join(BRON, f"{naam}-{fmt}.png")).convert("RGBA")


def bewaar(img, naam, fmt):
    p = os.path.join(UIT, f"{naam}-{fmt}.png")
    img.convert("RGB").save(p, optimize=True)
    return p


def maak():
    os.makedirs(UIT, exist_ok=True)
    gemaakt = []
    # held-1 en held-2: titel staat er al (x 230, y 110, schaal 0,80 op 2400; 16:9 zie maak2.py)
    for naam in ("held-1-knie", "held-2-spiraal"):
        im = laad(naam, "2400x1200")
        schrijf(im, (350, 262), REGELS[naam], 50)
        gemaakt.append(bewaar(im, naam, "2400x1200"))
    im = laad("held-1-knie", "1920x1080")   # 16:9 is het midden van 2400: x0 = 133, schaal 0,9
    schrijf(im, (int((350 - 133) * 0.9), int(262 * 0.9)), REGELS["held-1-knie"], 45)
    gemaakt.append(bewaar(im, "held-1-knie", "1920x1080"))
    im = laad("held-2-spiraal", "1920x1080")  # titel x 190, schaal 0,74 op het vak van 2133 breed
    schrijf(im, (int((190 + 111) * 0.9), int(242 * 0.9)), REGELS["held-2-spiraal"], 37)
    gemaakt.append(bewaar(im, "held-2-spiraal", "1920x1080"))

    # held-3 en held-4: kleiner naar rechtsonder, titel en regels linksboven
    for naam in ("held-3-voor-na", "held-4-fit-test-strip"):
        for fmt, (W, H) in (("2400x1200", (2400, 1200)), ("1920x1080", (1920, 1080))):
            s = H / 1200
            im = laad(naam, fmt)
            f = float(os.environ.get("KRIMP", "0.70"))
            im, (bx, by, bw, bh) = krimp(im, f, rechts=0.02 if naam.startswith("held-3") else 0.0)
            M1.titel(im, int(110 * s), int(70 * s), 0.72 * s)
            schrijf(im, (int(110 * s), int(250 * s)), REGELS[naam], int(50 * s), eerste_goud=True)
            if naam.startswith("held-3"):
                # de twee figuren staan op 27 en 75 procent van de breedte van het oude beeld
                label(im, bx + 0.27 * bw, by + bh - int(70 * s), "YOUR RIG", int(40 * s))
                label(im, bx + 0.745 * bw, by + bh - int(70 * s), "PRINTABLE PARTS", int(40 * s))
            gemaakt.append(bewaar(im, naam, fmt))
    for f in os.listdir(UIT):
        if f.startswith("_icoon"):
            os.remove(os.path.join(UIT, f))
    print("gemaakt:", [os.path.basename(g) for g in gemaakt])


if __name__ == "__main__":
    maak()
