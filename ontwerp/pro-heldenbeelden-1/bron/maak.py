"""Heldenbeelden afmaken: titel op beeld 1 en 2, voor en na samen met een lichtstreep, en elk beeld in 2400 x 1200
(Superhive) en 1920 x 1080 (Gumroad). Tekenpop-agent, 24 nov 2026.

python3 maak.py <rendermap> <uitmap> <fontmap> <icoon.svg>
"""
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

RENDER, UIT, FONTS, ICOON = sys.argv[1:5]
os.makedirs(UIT, exist_ok=True)
CREME = (255, 244, 224)
GOUD = (255, 210, 92)


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


def icoon(maat):
    p = os.path.join(UIT, f"_icoon_{maat}.png")
    if not os.path.exists(p):
        os.system(f"rsvg-convert -w {maat} '{ICOON}' -o '{p}'")
    return Image.open(p).convert("RGBA")


def laad(naam):
    p = os.path.join(RENDER, f"b-{naam}.png")
    return Image.open(p).convert("RGBA").resize((2400, 1200), Image.LANCZOS) if os.path.exists(p) else None


def titel(img, x, y, s=1.0):
    """Icoon en 'Click Joints Pro', zoals op cover B, met een zachte schaduw."""
    f = font("Bricolage.ttf", int(150 * s), "ExtraBold")
    ic = icoon(int(118 * s))
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    tx = x + int(150 * s)
    d.text((tx, y + 4), "Click Joints Pro", font=f, fill=(0, 0, 0, 110))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(16)))
    bx = ImageDraw.Draw(img).textbbox((tx, y), "Click Joints Pro", font=f)
    img.alpha_composite(ic, (x, int((bx[1] + bx[3]) / 2 - ic.height / 2)))
    ImageDraw.Draw(img).text((tx, y), "Click Joints Pro", font=f, fill=CREME)


def opslaan(img, naam, midden=0.5):
    """2400 x 1200 zoals hij is, 1920 x 1080 uit het midden (midden = fractie waar het 16:9-vak zit)."""
    img = img.convert("RGB")
    p = os.path.join(UIT, f"{naam}-2400x1200.png")
    img.save(p, optimize=True)
    w = int(1200 * 16 / 9)
    x0 = int((2400 - w) * midden)
    img.crop((x0, 0, x0 + w, 1200)).resize((1920, 1080), Image.LANCZOS).save(
        os.path.join(UIT, f"{naam}-1920x1080.png"), optimize=True)
    return p


def voor_na():
    a, b = laad("voor"), laad("na")
    if a is None or b is None:
        return None
    W, H = a.size
    # schuine grens: van (x0, 0) naar (x1, H)
    x0, x1 = int(W * 0.545), int(W * 0.455)
    masker = Image.new("L", (W, H), 0)
    ImageDraw.Draw(masker).polygon([(x0, 0), (W, 0), (W, H), (x1, H)], fill=255)
    masker = masker.filter(ImageFilter.GaussianBlur(3))
    img = Image.composite(b, a, masker)
    # lichtstreep: smalle witgouden lijn met een brede gloed
    streep = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(streep)
    for breed, kleur in ((90, (255, 196, 90, 60)), (36, (255, 214, 130, 120)), (10, (255, 236, 190, 220)),
                         (3, (255, 255, 245, 255))):
        laag = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(laag).line([(x0, -20), (x1, H + 20)], fill=kleur, width=breed)
        if breed > 5:
            laag = laag.filter(ImageFilter.GaussianBlur(breed / 2.2))
        streep = Image.alpha_composite(streep, laag)
    img = Image.alpha_composite(img, streep)
    return opslaan(img, "held-3-voor-na")


if __name__ == "__main__":
    gemaakt = []
    im = laad("knie")
    if im is not None:
        titel(im, 230, 110, 0.80)
        gemaakt.append(opslaan(im, "held-1-knie", midden=0.5))
    im = laad("spiraal")
    if im is not None:
        titel(im, 230, 110, 0.80)
        gemaakt.append(opslaan(im, "held-2-spiraal", midden=0.5))
    gemaakt.append(voor_na())
    im = laad("strip")
    if im is not None:
        gemaakt.append(opslaan(im, "held-4-fit-test-strip"))
    # overzicht voor de keurder: alle vier groot (1200 x 600) en klein zoals in een lijst (400 x 200 en 16:9 384 x 216)
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
