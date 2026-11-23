"""Zet tekst op de renders en maakt paneelschets, winkelbeelden en vergelijkingsblad (Dortus, merk-agent, 23 nov 2026).

python3 maak_beelden.py <rendermap> <uitmap> <fontmap> [naam] [concurrentiemap]
Fonts in fontmap: Bricolage.ttf (naam en koppen, OFL) en Inter.ttf (kleine tekst, OFL).
Tekst in het product is Engels. Elke render komt uit Blender (splits_scene.py), niets is AI-beeld.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, UIT, FONTS = sys.argv[1], sys.argv[2], sys.argv[3]
NAAM = sys.argv[4] if len(sys.argv) > 4 else "Click Cuts"
CONC = sys.argv[5] if len(sys.argv) > 5 else ""
HIER = os.path.dirname(os.path.abspath(__file__))
os.makedirs(UIT, exist_ok=True)

KLEUR = {
    "nacht": (29, 20, 38), "creme": (255, 244, 224), "goud": (255, 210, 92), "koraal": (255, 91, 58),
    "kobalt": (61, 91, 255), "lila": (165, 140, 255), "wit": (255, 255, 255), "inkt": (20, 22, 48),
}
STIJL_TEKST = {
    "a": {"kop": KLEUR["wit"], "sub": (225, 232, 255), "klein": (215, 224, 255), "cover_sub": (22, 28, 92)},
    "b": {"kop": KLEUR["creme"], "sub": (226, 214, 240), "klein": (185, 170, 210)},
}


def font(naam, maat, gewicht=None):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    if gewicht:
        try:
            f.set_variation_by_name(gewicht)
        except Exception:  # noqa: BLE001
            try:
                f.set_variation_by_axes([gewicht_as(gewicht)])
            except Exception:  # noqa: BLE001
                pass
    return f


def gewicht_as(g):
    return {"ExtraBold": 800, "Bold": 700, "SemiBold": 600, "Medium": 500, "Regular": 400}.get(g, 700)


def kop(maat):
    return font("Bricolage.ttf", maat, "ExtraBold")


def tekst(maat, g="Medium"):
    return font("Inter.ttf", maat, g)


def schaduwtekst(img, xy, s, f, kleur, schaduw=(0, 0, 0, 90), r=10, spatie=0):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    d.multiline_text((xy[0], xy[1] + 4), s, font=f, fill=schaduw, spacing=spatie)
    laag = laag.filter(ImageFilter.GaussianBlur(r))
    img.alpha_composite(laag)
    ImageDraw.Draw(img).multiline_text(xy, s, font=f, fill=kleur, spacing=spatie)


def icoon(maat):
    p = os.path.join(UIT, f"_icoon_{maat}.png")
    if not os.path.exists(p):
        os.system(f"rsvg-convert -w {maat} '{os.path.join(HIER, 'icoon.svg')}' -o '{p}'")
    return Image.open(p).convert("RGBA")


def cover(stijl):
    src = os.path.join(RENDER, f"{stijl}-cover.png")
    if not os.path.exists(src):
        return None
    img = Image.open(src).convert("RGBA").resize((2400, 1200), Image.LANCZOS)
    t = STIJL_TEKST[stijl]
    x = 150
    ic = icoon(132)
    img.alpha_composite(ic, (x, 170))
    ImageDraw.Draw(img).text((x + 160, 205), "Add-on for Blender", font=tekst(46, "SemiBold"), fill=t["klein"])
    schaduwtekst(img, (x - 8, 340), NAAM, kop(225), t["kop"], r=18)
    schaduwtekst(img, (x, 650), "Print bigger than\nyour printer.", kop(112), KLEUR["goud"] if stijl == "b" else KLEUR["wit"],
                 r=14, spatie=10)
    ImageDraw.Draw(img).text((x, 960), "Parts that fit your bed, with pins that line up.", font=tekst(46),
                                fill=t.get("cover_sub", t["sub"]))
    uit = os.path.join(UIT, f"cover-{stijl}.png")
    img.convert("RGB").save(uit, optimize=True)
    img.convert("RGB").resize((1200, 600), Image.LANCZOS).save(os.path.join(UIT, f"cover-{stijl}-1200x600.png"))
    return uit


KOPPEN = {
    "heel": ("Bigger than your build plate?", "One model, way past what your printer can do."),
    "delen": ("Split it into parts that fit.", "Clean cuts where you want them."),
    "pen": ("Pins and holes that line up.", "Clearance built in, so parts press together."),
    "bed": ("Every part fits the bed.", "Each part sized to your printer."),
    "samen": ("One piece again.", "Press the pins in and the parts line up."),
}


def winkelbeeld(stijl, shot, nr):
    src = os.path.join(RENDER, f"{stijl}-{shot}.png")
    if not os.path.exists(src):
        return None
    img = Image.open(src).convert("RGBA").resize((1600, 1600), Image.LANCZOS)
    t = STIJL_TEKST[stijl]
    # zachte strook bovenaan voor leesbaarheid, geen kader
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for y in range(360):
        a = int(110 * (1 - y / 360) ** 1.6)
        d.line([(0, y), (1600, y)], fill=(10, 8, 30, a))
    img.alpha_composite(laag)
    k, s = KOPPEN[shot]
    schaduwtekst(img, (90, 86), k, kop(92), t["kop"], r=12)
    ImageDraw.Draw(img).text((92, 206), s, font=tekst(42), fill=t["sub"])
    ic = icoon(72)
    img.alpha_composite(ic, (1600 - 72 - 70, 1600 - 72 - 64))
    uit = os.path.join(UIT, f"winkel-{stijl}-{nr}-{shot}.png")
    img.convert("RGB").save(uit, optimize=True)
    return uit


def paneel():
    """Schets van het paneel in Blender (N-paneel): weinig knoppen, één grote eerste stap. 2x schaal."""
    S = 2
    W, H = 420 * S, 640 * S
    img = Image.new("RGBA", (W, H), (48, 48, 48, 255))
    d = ImageDraw.Draw(img)
    f = lambda m, g="Medium": tekst(m * S, g)  # noqa: E731
    # kop van het paneel
    d.rectangle([0, 0, W, 44 * S], fill=(40, 40, 40))
    ic = icoon(26 * S)
    img.alpha_composite(ic, (12 * S, 9 * S))
    d.text((46 * S, 12 * S), NAAM, font=f(15, "SemiBold"), fill=(235, 235, 235))
    y = 62 * S

    def label(s, y):
        d.text((16 * S, y), s, font=f(12), fill=(170, 170, 170))

    # stap 1: printer
    label("Your printer", y)
    y += 20 * S
    d.rounded_rectangle([16 * S, y, W - 16 * S, y + 34 * S], 6 * S, fill=(34, 34, 34), outline=(70, 70, 70), width=S)
    d.text((28 * S, y + 9 * S), "Bambu Lab X1 / P1   256 mm", font=f(13), fill=(230, 230, 230))
    d.polygon([(W - 36 * S, y + 14 * S), (W - 26 * S, y + 14 * S), (W - 31 * S, y + 20 * S)], fill=(200, 200, 200))
    y += 52 * S
    # stap 2: verbinders als drie grote keuzes met icoon
    label("Connectors", y)
    y += 20 * S
    bw = (W - 32 * S - 2 * 8 * S) // 3
    keuzes = [("Pins", True), ("Click", False), ("None", False)]
    for i, (k, aan) in enumerate(keuzes):
        x0 = 16 * S + i * (bw + 8 * S)
        d.rounded_rectangle([x0, y, x0 + bw, y + 64 * S], 8 * S, fill=(61, 91, 255) if aan else (34, 34, 34),
                            outline=(110, 135, 255) if aan else (70, 70, 70), width=S)
        cx, cy = x0 + bw // 2, y + 24 * S
        kl = (255, 255, 255) if aan else (190, 190, 190)
        if k == "Pins":
            d.rounded_rectangle([cx - 4 * S, cy - 12 * S, cx + 4 * S, cy + 12 * S], 4 * S, fill=(255, 210, 92))
        elif k == "Click":
            d.polygon([(cx - 10 * S, cy + 10 * S), (cx - 10 * S, cy - 2 * S), (cx - 4 * S, cy - 10 * S),
                       (cx + 4 * S, cy - 10 * S), (cx + 10 * S, cy - 2 * S), (cx + 10 * S, cy + 10 * S)], outline=kl,
                      width=2 * S)
        else:
            d.line([(cx - 10 * S, cy), (cx + 10 * S, cy)], fill=kl, width=2 * S)
        tw = d.textlength(k, font=f(12, "SemiBold"))
        d.text((cx - tw / 2, y + 42 * S), k, font=f(12, "SemiBold"), fill=kl)
    y += 84 * S
    # de grote eerste stap
    d.rounded_rectangle([16 * S, y, W - 16 * S, y + 56 * S], 10 * S, fill=(255, 210, 92))
    s = "Split to fit"
    tw = d.textlength(s, font=f(18, "Bold"))
    d.text(((W - tw) / 2, y + 16 * S), s, font=f(18, "Bold"), fill=(29, 20, 38))
    y += 74 * S
    # uitkomst
    d.rounded_rectangle([16 * S, y, W - 16 * S, y + 92 * S], 8 * S, fill=(38, 38, 38))
    d.ellipse([28 * S, y + 14 * S, 48 * S, y + 34 * S], fill=(46, 211, 168))
    d.line([(33 * S, y + 24 * S), (37 * S, y + 29 * S), (44 * S, y + 19 * S)], fill=(20, 40, 30), width=2 * S)
    d.text((58 * S, y + 14 * S), "7 parts, all fit the bed", font=f(14, "SemiBold"), fill=(235, 235, 235))
    d.text((58 * S, y + 38 * S), "19 pins, 0.2 mm clearance", font=f(12), fill=(170, 170, 170))
    d.text((58 * S, y + 60 * S), "Drag a cut to move it", font=f(12), fill=(170, 170, 170))
    y += 110 * S
    d.rounded_rectangle([16 * S, y, W - 16 * S, y + 40 * S], 8 * S, fill=(70, 70, 70))
    s = "Export parts (3MF)"
    tw = d.textlength(s, font=f(14, "SemiBold"))
    d.text(((W - tw) / 2, y + 11 * S), s, font=f(14, "SemiBold"), fill=(240, 240, 240))
    y += 58 * S
    d.polygon([(18 * S, y + 4 * S), (26 * S, y + 8 * S), (18 * S, y + 12 * S)], fill=(150, 150, 150))
    d.text((32 * S, y), "More settings", font=f(12), fill=(150, 150, 150))
    img = img.crop((0, 0, W, y + 30 * S))
    uit = os.path.join(UIT, "paneel-schets.png")
    img.convert("RGB").save(uit)
    return uit, img


def winkel_paneel(stijl, pimg, nr):
    """Winkelbeeld 4: het paneel naast de uiteengevallen leeuw."""
    src = os.path.join(RENDER, f"{stijl}-delen.png")
    if not os.path.exists(src):
        return None
    img = Image.open(src).convert("RGBA").resize((1600, 1600), Image.LANCZOS)
    t = STIJL_TEKST[stijl]
    p = pimg.copy()
    sch = 1040 / p.height
    p = p.resize((int(p.width * sch), 1040), Image.LANCZOS)
    masker = Image.new("L", p.size, 0)
    ImageDraw.Draw(masker).rounded_rectangle([0, 0, p.width, p.height], 28, fill=255)
    schaduw = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(schaduw).rounded_rectangle([80, 400, 80 + p.width, 400 + p.height + 20], 28, fill=(0, 0, 0, 120))
    img.alpha_composite(schaduw.filter(ImageFilter.GaussianBlur(30)))
    img.paste(p, (80, 390), masker)
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for y in range(360):
        d.line([(0, y), (1600, y)], fill=(10, 8, 30, int(110 * (1 - y / 360) ** 1.6)))
    img.alpha_composite(laag)
    schaduwtekst(img, (90, 86), "One button to start.", kop(92), t["kop"], r=12)
    ImageDraw.Draw(img).text((92, 206), "Pick your printer, pick a connector, split.", font=tekst(42), fill=t["sub"])
    uit = os.path.join(UIT, f"winkel-{stijl}-4-paneel.png")
    img.convert("RGB").save(uit, optimize=True)
    return uit


def vergelijk(covers):
    """Ons coverbeeld naast CatPin en Cleave, zoals in een raster op Superhive (klein) en groot."""
    namen = [("cover-a", "Ons A: Pop"), ("cover-b", "Ons B: Nacht"), ("catpin", "CatPin"), ("cleave", "Cleave")]
    beelden = []
    for k, lab in namen:
        p = None
        if k.startswith("cover"):
            p = os.path.join(UIT, f"{k}-1200x600.png")
        elif CONC:
            for ext in ("png", "jpeg", "jpg", "webp"):
                q = os.path.join(CONC, f"{k}.{ext}")
                if os.path.exists(q):
                    p = q
        if p and os.path.exists(p):
            beelden.append((Image.open(p).convert("RGB").resize((1200, 600), Image.LANCZOS), lab))
    if not beelden:
        return None
    W = 2 * 1200 + 3 * 40
    rijen = (len(beelden) + 1) // 2
    klein_h = 200 + 60
    H = 120 + rijen * (600 + 70) + 120 + klein_h + 60
    img = Image.new("RGB", (W, H), (236, 236, 240))
    d = ImageDraw.Draw(img)
    d.text((40, 40), "Groot (1200 x 600)", font=tekst(40, "SemiBold"), fill=(40, 40, 50))
    for i, (b, lab) in enumerate(beelden):
        r, k = divmod(i, 2)
        x, y = 40 + k * 1240, 120 + r * 670
        img.paste(b, (x, y))
        d.text((x, y + 610), lab, font=tekst(34, "SemiBold"), fill=(40, 40, 50))
    y0 = 120 + rijen * 670 + 40
    d.text((40, y0), "Klein, zoals in een raster op Superhive (400 x 200)", font=tekst(40, "SemiBold"), fill=(40, 40, 50))
    for i, (b, lab) in enumerate(beelden):
        x = 40 + i * 440
        img.paste(b.resize((400, 200), Image.LANCZOS), (x, y0 + 70))
    uit = os.path.join(UIT, "vergelijk.png")
    img.save(uit, optimize=True)
    return uit


def gumroad_vierkant(stijl):
    """Vierkant voor Gumroad: de uiteengevallen leeuw, naam en icoon bovenaan (daar laat de camera ruimte)."""
    src = os.path.join(RENDER, f"{stijl}-delen.png")
    if not os.path.exists(src):
        return None
    img = Image.open(src).convert("RGBA").resize((1200, 1200), Image.LANCZOS)
    t = STIJL_TEKST[stijl]
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for y in range(300):
        d.line([(0, y), (1200, y)], fill=(10, 8, 30, int(110 * (1 - y / 300) ** 1.6)))
    img.alpha_composite(laag)
    img.alpha_composite(icoon(118), (70, 64))
    schaduwtekst(img, (214, 66), NAAM, kop(112), t["kop"], r=12)
    uit = os.path.join(UIT, f"gumroad-{stijl}-1200.png")
    img.convert("RGB").save(uit, optimize=True)
    return uit


if __name__ == "__main__":
    gemaakt = []
    for st in ("a", "b"):
        gemaakt.append(cover(st))
        for nr, sh in ((1, "heel"), (2, "bed"), (3, "pen"), (5, "samen")):
            gemaakt.append(winkelbeeld(st, sh, nr))
        gemaakt.append(gumroad_vierkant(st))
    pp, pimg = paneel()
    gemaakt.append(pp)
    for st in ("a", "b"):
        gemaakt.append(winkel_paneel(st, pimg, 4))
    gemaakt.append(vergelijk(None))
    for f in os.listdir(UIT):
        if f.startswith("_icoon"):
            os.remove(os.path.join(UIT, f))
    print("gemaakt:", [os.path.basename(g) for g in gemaakt if g])
