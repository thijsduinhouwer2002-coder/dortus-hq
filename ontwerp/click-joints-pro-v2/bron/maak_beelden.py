"""Tekst op de renders van Click Joints Pro v2, plus voor/na, close-up, paneelbeeld en vergelijkingsblad.
(Dortus, merk-agent, 23 nov 2026.)

python3 maak_beelden.py <rendermap> <uitmap> <fontmap> <icoon.svg> [paneel-scherm.png] [vergelijkmap]
Fonts: Bricolage.ttf en Inter.ttf (OFL). Elke bewering komt uit platformen/blender/pro-1.2.0.md en de Gumroad-tekst
(platformen/blender-2/gumroad-1.1.md): Figure from rig, hinge met eindstop voor ellebogen en knieen, kogel voor
schouders, heupen en nek, buigbereik in graden naast elk gewricht, speling die je zelf kiest. Geen "holds a pose",
geen beloftes over printen.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, UIT, FONTS, ICOON = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
PANEEL = sys.argv[5] if len(sys.argv) > 5 else ""
VERGELIJK = sys.argv[6] if len(sys.argv) > 6 else ""
os.makedirs(UIT, exist_ok=True)
NAAM = "Click Joints Pro"
GOUD = (255, 210, 92)
TEKST = {
    "a": {"kop": (255, 255, 255), "accent": (255, 255, 255), "sub": (225, 232, 255), "klein": (215, 224, 255),
          "cover_sub": (22, 28, 92), "bg": (36, 67, 230)},
    "b": {"kop": (255, 244, 224), "accent": GOUD, "sub": (226, 214, 240), "klein": (185, 170, 210),
          "cover_sub": (226, 214, 240), "bg": (29, 20, 38)},
}


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


def kop(m):
    return font("Bricolage.ttf", m, "ExtraBold")


def tekst(m, g="Medium"):
    return font("Inter.ttf", m, g)


def schaduw(img, xy, s, f, kleur, r=12, spatie=0):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).multiline_text((xy[0], xy[1] + 4), s, font=f, fill=(0, 0, 0, 90), spacing=spatie)
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(r)))
    ImageDraw.Draw(img).multiline_text(xy, s, font=f, fill=kleur, spacing=spatie)


def icoon(maat):
    p = os.path.join(UIT, f"_icoon_{maat}.png")
    if not os.path.exists(p):
        os.system(f"rsvg-convert -w {maat} '{ICOON}' -o '{p}'")
    return Image.open(p).convert("RGBA")


def laad(st, shot, maat):
    p = os.path.join(RENDER, f"{st}-{shot}.png")
    if not os.path.exists(p):
        return None
    return Image.open(p).convert("RGBA").resize(maat, Image.LANCZOS)


def strook(img, hoogte=360, sterkte=110):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for y in range(hoogte):
        d.line([(0, y), (img.width, y)], fill=(10, 8, 30, int(sterkte * (1 - y / hoogte) ** 1.6)))
    img.alpha_composite(laag)


def opslaan(img, naam):
    p = os.path.join(UIT, naam)
    img.convert("RGB").save(p, optimize=True)
    return p


def cover(st, shot, maat, naam_uit, klein=None):
    img = laad(st, shot, maat)
    if img is None:
        return None
    t = TEKST[st]
    W, Hh = maat
    s = Hh / 1200
    x = int(150 * s)
    img.alpha_composite(icoon(int(124 * s)), (x, int(190 * s)))
    ImageDraw.Draw(img).text((x + int(150 * s), int(222 * s)), "Add-on for Blender", font=tekst(int(46 * s), "SemiBold"),
                             fill=t["klein"])
    schaduw(img, (x - int(6 * s), int(350 * s)), "Click Joints\nPro", kop(int(200 * s)), t["kop"], r=18, spatie=int(-10 * s))
    schaduw(img, (x, int(790 * s)), "Rig in. Joints out.", kop(int(96 * s)), t["accent"], r=14)
    ImageDraw.Draw(img).text((x, int(930 * s)), "Ball joints and hinges, with the bend\nrange in degrees.",
                             font=tekst(int(44 * s)), fill=t["cover_sub"], spacing=int(10 * s))
    p = opslaan(img, naam_uit)
    if klein:
        img.convert("RGB").resize(klein, Image.LANCZOS).save(p.replace(".png", f"-{klein[0]}x{klein[1]}.png"), optimize=True)
    return p


GALERIJ = {
    "pose": ("Built from your rig.", "Figure from rig places every joint it can."),
    "uit": ("Ball joints and hinges.", "Shoulders, hips and neck turn. Elbows and knees bend."),
    "paneel": ("See how far each joint bends.", "Measured in Blender, before you print."),
}


def galerij(st, shot, nr, img=None):
    img = img or laad(st, shot, (1600, 1600))
    if img is None:
        return None
    t = TEKST[st]
    strook(img)
    k, s = GALERIJ[shot]
    schaduw(img, (90, 86), k, kop(92), t["kop"])
    ImageDraw.Draw(img).text((92, 206), s, font=tekst(42), fill=t["sub"])
    img.alpha_composite(icoon(72), (1600 - 72 - 70, 1600 - 72 - 64))
    return opslaan(img, f"galerij-{st}-{nr}-{shot}.png")


def closeup(st):
    a, b = laad(st, "kogel", (796, 1600)), laad(st, "knie", (796, 1600))
    if a is None or b is None:
        return None
    t = TEKST[st]
    img = Image.new("RGBA", (1600, 1600), t["bg"] + (255,))
    img.paste(a, (0, 0))
    img.paste(b, (804, 0))
    strook(img)
    schaduw(img, (90, 86), "Ball in socket. Hinge with a stop.", kop(80), t["kop"])
    ImageDraw.Draw(img).text((92, 196), "With the clearance you set (0.2 mm here).", font=tekst(42), fill=t["sub"])
    for x, s in ((60, "Shoulder: ball joint"), (868, "Knee: hinge")):
        ImageDraw.Draw(img).text((x, 1500), s, font=tekst(40, "SemiBold"), fill=t["kop"])
    img.alpha_composite(icoon(72), (1600 - 72 - 70, 1600 - 72 - 64 - 60))
    return opslaan(img, f"galerij-{st}-3-closeup.png")


def laad_bijsnijden(st, shot):
    p = os.path.join(RENDER, f"{st}-{shot}.png")
    if not os.path.exists(p):
        return None
    im = Image.open(p).convert("RGBA").resize((1600, 1600), Image.LANCZOS)
    return im.crop((400, 0, 1192, 1600))


def paneel(st):
    if not PANEEL or not os.path.exists(PANEEL):
        return None
    t = TEKST[st]
    sch = Image.open(PANEEL).convert("RGBA")
    # het echte scherm uit de studio-2-opname (Blender 5.3.0, Pro 1.2.0): figuur met graden plus het paneel
    sch = sch.crop((470, 0, 1920, 1080))
    w = 1440
    sch = sch.resize((w, int(sch.height * w / sch.width)), Image.LANCZOS)
    achter = laad(st, "pose", (1600, 1600))
    img = achter if achter is not None else Image.new("RGBA", (1600, 1600), t["bg"] + (255,))
    img = img.filter(ImageFilter.GaussianBlur(24)) if achter is not None else img
    x, y = 80, 420
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x, y + 20, x + sch.width, y + sch.height + 30], 26, fill=(0, 0, 0, 150))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    m = Image.new("L", sch.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, sch.width, sch.height], 26, fill=255)
    img.paste(sch, (x, y), m)
    ImageDraw.Draw(img).text((x, y + sch.height + 40), "Real screenshot: Click Joints Pro 1.2.0 in Blender 5.3",
                             font=tekst(32), fill=t["klein"])
    return galerij(st, "paneel", 4, img)


def voor_na(st):
    a, b = laad(st, "voor", (796, 1600)), laad(st, "uitp", (796, 1600))
    if a is None or b is None:
        return None
    t = TEKST[st]
    img = Image.new("RGBA", (1600, 1600), t["bg"] + (255,))
    img.paste(a, (0, 0))
    img.paste(b, (804, 0))
    strook(img)
    schaduw(img, (90, 86), "From rig to printable parts.", kop(88), t["kop"])
    ImageDraw.Draw(img).text((92, 202), "One button: Figure from rig.", font=tekst(42), fill=t["sub"])
    d = ImageDraw.Draw(img)
    for x, s in ((60, "Before: your rigged figure"), (868, "After: parts with joints")):
        d.text((x, 1500), s, font=tekst(40, "SemiBold"), fill=t["kop"])
    # pijl in het midden
    cx, cy = 800, 820
    d.ellipse([cx - 56, cy - 56, cx + 56, cy + 56], fill=GOUD)
    d.polygon([(cx - 18, cy - 26), (cx + 26, cy), (cx - 18, cy + 26)], fill=(29, 20, 38))
    img.alpha_composite(icoon(72), (1600 - 72 - 70, 1600 - 72 - 64 - 60))
    return opslaan(img, f"galerij-{st}-5-voor-na.png")


def vierkant(st):
    img = laad(st, "pose", (1200, 1200))
    if img is None:
        return None
    t = TEKST[st]
    strook(img, 300, 110)
    img.alpha_composite(icoon(110), (64, 60))
    schaduw(img, (200, 66), NAAM, kop(96), t["kop"])
    return opslaan(img, f"vierkant-{st}-1200.png")


def vergelijk():
    rij = [("oud", "Oud (nu op Gumroad)"), ("cover-a", "Nieuw A: Pop"), ("cover-b", "Nieuw B: Nacht"), ("catpin", "CatPin")]
    beelden = []
    for k, lab in rij:
        p = None
        if k.startswith("cover"):
            p = os.path.join(UIT, f"{k}-2400x1200-1200x600.png")
        elif VERGELIJK:
            for ext in ("png", "jpeg", "jpg"):
                q = os.path.join(VERGELIJK, f"{k}.{ext}")
                if os.path.exists(q):
                    p = q
        if p and os.path.exists(p):
            im = Image.open(p).convert("RGB")
            # alles als 2:1, zoals op Superhive (het oude beeld van Gumroad is 16:9: midden uitgesneden)
            r = im.width / im.height
            if r < 2:
                h = int(im.width / 2)
                y = (im.height - h) // 2
                im = im.crop((0, y, im.width, y + h))
            beelden.append((im.resize((1200, 600), Image.LANCZOS), lab))
    if not beelden:
        return None
    W = 2 * 1200 + 3 * 40
    rijen = (len(beelden) + 1) // 2
    H = 120 + rijen * 670 + 40 + 70 + 200 + 80
    img = Image.new("RGB", (W, H), (236, 236, 240))
    d = ImageDraw.Draw(img)
    d.text((40, 40), "Groot (1200 x 600)", font=tekst(40, "SemiBold"), fill=(40, 40, 50))
    for i, (b, lab) in enumerate(beelden):
        r, k = divmod(i, 2)
        x, y = 40 + k * 1240, 120 + r * 670
        img.paste(b, (x, y))
        d.text((x, y + 610), lab, font=tekst(34, "SemiBold"), fill=(40, 40, 50))
    y0 = 120 + rijen * 670 + 40
    d.text((40, y0), "Klein, zoals in een lijst (400 x 200)", font=tekst(40, "SemiBold"), fill=(40, 40, 50))
    for i, (b, lab) in enumerate(beelden):
        img.paste(b.resize((400, 200), Image.LANCZOS), (40 + i * 440, y0 + 70))
    return opslaan(img, "vergelijk.png")


if __name__ == "__main__":
    gemaakt = []
    for st in ("a", "b"):
        gemaakt.append(cover(st, "cover169", (2560, 1440), f"cover-{st}-2560x1440.png", klein=(1280, 720)))
        gemaakt.append(cover(st, "cover21", (2400, 1200), f"cover-{st}-2400x1200.png", klein=(1200, 600)))
        gemaakt.append(vierkant(st))
        gemaakt.append(galerij(st, "pose", 1))
        gemaakt.append(galerij(st, "uit", 2))
        gemaakt.append(closeup(st))
        gemaakt.append(paneel(st))
        gemaakt.append(voor_na(st))
    gemaakt.append(vergelijk())
    for f in os.listdir(UIT):
        if f.startswith("_icoon"):
            os.remove(os.path.join(UIT, f))
    print("gemaakt:", [os.path.basename(g) for g in gemaakt if g])
