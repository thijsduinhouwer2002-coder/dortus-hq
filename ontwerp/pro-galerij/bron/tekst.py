"""Tekst en uitleg op de galerijbeelden van Click Joints Pro (Beeldmaker, 25 nov 2026, issue #49).

python3 tekst.py <modus knie|klik|strip> <render.png> <json> <uitmap> <fontmap> <icoon.svg>

Maakt <modus>-2400x1200.png (Superhive) en <modus>-1920x1080.png (Gumroad) uit één render van 2400x1350.
Elk beeld: icoon en naam, een kop en één regel wat het doet. Getallen (graden, spelingen, aantal gewrichten) komen uit
de json die galerij.py schreef, dus uit wat de add-on maakte, niet verzonnen.
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

MODUS, RENDER, META, UIT, FONTS, ICOON = sys.argv[1:7]
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT, DONKER = (255, 246, 230), (255, 196, 84), (226, 216, 232), (24, 16, 30)


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


def schaduw_tekst(img, stukken, blur):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for (x, y), t, f, _k in stukken:
        d.text((x, y + blur // 3), t, font=f, fill=(0, 0, 0, 200))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(img)
    for (x, y), t, f, k in stukken:
        d.text((x, y), t, font=f, fill=k)


def donker(img, breed, kant="links", sterk=170):
    W, H = img.size
    if kant == "links":
        m = Image.new("L", (W, 1), 0)
        for x in range(W):
            m.putpixel((x, 0), int(sterk * max(0.0, 1 - x / breed) ** 1.6))
        m = m.resize((W, H))
    else:  # boven
        m = Image.new("L", (1, H), 0)
        for y in range(H):
            m.putpixel((0, y), int(sterk * max(0.0, 1 - y / breed) ** 1.6))
        m = m.resize((W, H))
    img.paste(Image.new("RGBA", (W, H), (10, 6, 14, 255)), (0, 0), m)


def pil(img, s, xy, tekst, maat=30, midden=True, rand=GOUD, vul=DONKER, kleur=CREME):
    d = ImageDraw.Draw(img)
    f = font("Inter.ttf", int(maat * s), "SemiBold")
    bb = d.textbbox((0, 0), tekst, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    bw, bh = w + int(36 * s), h + int(28 * s)
    x, y = xy
    bx, by = (x - bw // 2, y - bh // 2) if midden else (x, y - bh // 2)
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((bx, by + 6, bx + bw, by + bh + 6), radius=bh // 2, fill=(0, 0, 0, 150))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=bh // 2, fill=vul + (235,), outline=rand + (255,),
                        width=max(2, int(2 * s)))
    d.text((bx + int(18 * s), by + int(14 * s) - bb[1]), tekst, font=f, fill=kleur)
    return (bx, by, bx + bw, by + bh)


def kop(img, s, x0, y, titel, regel, breed_px):
    ic = icoon(int(72 * s))
    img.alpha_composite(ic, (x0, y))
    f_klein = font("Inter.ttf", int(32 * s), "SemiBold")
    schaduw_tekst(img, [((x0 + ic.width + int(22 * s), y + ic.height // 2 - int(20 * s)), "Click Joints Pro",
                         f_klein, ZACHT)], 8)
    y += ic.height + int(30 * s)
    f_titel = font("Bricolage.ttf", int(104 * s), "ExtraBold")
    stukken = []
    for t in titel:
        stukken.append(((x0 - int(4 * s), y), t, f_titel, CREME))
        y += int(112 * s)
    schaduw_tekst(img, stukken, 14)
    y += int(18 * s)
    f_regel = font("Inter.ttf", int(40 * s), "Medium")
    d = ImageDraw.Draw(img)
    for t in passend(d, regel, f_regel, breed_px):
        schaduw_tekst(img, [((x0, y), t, f_regel, GOUD)], 8)
        y += int(56 * s)
    return y


def passend(d, tekst, f, breed):
    regels, nu = [], ""
    for w in tekst.split(" "):  # alleen gewone spaties: "0.20\u00a0mm" blijft bij elkaar
        proef = (nu + " " + w).strip()
        if d.textlength(proef, font=f) > breed and nu:
            regels.append(nu)
            nu = w
        else:
            nu = proef
    return regels + [nu]


def boog(img, s, meta, P):
    """Gradenboog om de knie: van de scheen recht (0°) tot de stop die de add-on meldt."""
    b = meta["boog"]
    k, s0, s1 = P(b["knie"]), P(b["scheen0"]), P(b["scheen"])
    a0 = math.atan2(s0[1] - k[1], s0[0] - k[0])
    a1 = math.atan2(s1[1] - k[1], s1[0] - k[0])
    # korte kant op (de knie buigt minder dan 180° in beeld)
    d_a = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    stop = round(float(meta["stop_graden"]))
    R = int(210 * s)
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    stappen = 90
    # gevulde waaier, zacht
    pts = [k] + [(k[0] + R * math.cos(a0 + d_a * i / stappen), k[1] + R * math.sin(a0 + d_a * i / stappen))
                 for i in range(stappen + 1)]
    d.polygon(pts, fill=GOUD + (46,))
    img.alpha_composite(laag)
    d = ImageDraw.Draw(img)
    rand = pts[1:]
    d.line(rand, fill=GOUD + (255,), width=max(3, int(6 * s)), joint="curve")
    for p in (rand[0], rand[-1]):
        d.line((k, p), fill=GOUD + (255,), width=max(2, int(4 * s)))
    f = font("Inter.ttf", int(24 * s), "SemiBold")
    for g in range(0, stop + 1, 30):
        a = a0 + d_a * g / stop
        p1 = (k[0] + R * math.cos(a), k[1] + R * math.sin(a))
        p2 = (k[0] + (R + 18 * s) * math.cos(a), k[1] + (R + 18 * s) * math.sin(a))
        d.line((p1, p2), fill=GOUD + (255,), width=max(2, int(4 * s)))
        if g in (0, 60):
            pt = (k[0] + (R + 50 * s) * math.cos(a), k[1] + (R + 50 * s) * math.sin(a))
            tw = d.textlength(f"{g}°", font=f)
            schaduw_tekst(img, [((pt[0] - tw / 2, pt[1] - 14 * s), f"{g}°", f, CREME)], 6)
            d = ImageDraw.Draw(img)
    r = int(12 * s)
    d.ellipse((k[0] - r, k[1] - r, k[0] + r, k[1] + r), fill=GOUD + (255,), outline=(20, 12, 24, 255), width=3)
    a = a0 + d_a
    pt = (k[0] + (R + 110 * s) * math.cos(a), k[1] + (R + 110 * s) * math.sin(a))
    pil(img, s, (int(pt[0]), int(pt[1])), f"Stop {stop}°", maat=40)


def klik(img, s, meta, P):
    kr, kd = meta["kaders"]["rig"], meta["kaders"]["delen"]
    links = P(kr[1])
    rechts = P(kd[0])
    y = int(img.size[1] * 0.56)
    x1, x2 = links[0] + int(40 * s), rechts[0] - int(40 * s)
    d = ImageDraw.Draw(img)
    d.line((x1, y, x2 - int(30 * s), y), fill=GOUD + (255,), width=max(4, int(8 * s)))
    d.polygon([(x2, y), (x2 - int(40 * s), y - int(24 * s)), (x2 - int(40 * s), y + int(24 * s))], fill=GOUD + (255,))
    pil(img, s, ((x1 + x2) // 2, y - int(62 * s)), "1 click", maat=40)
    onder_r = P(kr[0])
    onder_d = P(kd[0])
    n_s = sum(1 for g in meta["gewrichten"] if " Hinge " in g)
    n_k = sum(1 for g in meta["gewrichten"] if " Ball " in g)
    yb = int(img.size[1] * 0.93)
    pil(img, s, (int((P(kr[0])[0] + P(kr[1])[0]) / 2), yb), "Your rigged model", maat=30, rand=(79, 179, 255))
    pil(img, s, (int((P(kd[0])[0] + P(kd[1])[0]) / 2), yb), f"{n_s} hinges, {n_k} ball joints", maat=30)
    return onder_r, onder_d


def strip(img, s, meta, P):
    for getal, q in sorted(meta["labels"].items()):
        x, y = P(q["voet"])
        pil(img, s, (int(x), int(y + 70 * s)), f"{getal} mm", maat=30)


def inzet(img, s, x0, y0):
    """Kaartje met de robot uit dezelfde render als 'Rig in. Parts out.' (klik): daarna krijgt elk gewricht die speling."""
    pad = os.environ.get("GB_INZET")
    if not pad:
        return
    r = Image.open(pad).convert("RGBA")
    W0, H0 = r.size
    robot = r.crop((int(W0 * 0.53), int(H0 * 0.10), int(W0 * 0.82), int(H0 * 0.92)))
    h = int(330 * s)
    robot = robot.resize((int(robot.width * h / robot.height), h), Image.LANCZOS)
    bw = robot.width + int(430 * s)
    bh = h + int(30 * s)
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((x0, y0 + 8, x0 + bw, y0 + bh + 8), radius=int(28 * s), fill=(0, 0, 0, 160))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(14)))
    kaart = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    m = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, bw - 1, bh - 1), radius=int(28 * s), fill=255)
    kaart.paste(robot, (int(10 * s), int(15 * s)))
    img.paste(Image.new("RGBA", (bw, bh), (20, 12, 28, 255)), (x0, y0), m)
    img.alpha_composite(kaart, (x0, y0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), radius=int(28 * s), outline=GOUD + (255,), width=max(2, int(2 * s)))
    tx = x0 + robot.width + int(30 * s)
    f1 = font("Bricolage.ttf", int(44 * s), "Bold")
    f2 = font("Inter.ttf", int(30 * s), "Medium")
    ty = y0 + int(70 * s)
    schaduw_tekst(img, [((tx, ty), "Then one click", f1, CREME)], 6)
    ty += int(64 * s)
    for t in passend(d, "and every joint on your figure gets that clearance.", f2, int(370 * s)):
        schaduw_tekst(img, [((tx, ty), t, f2, ZACHT)], 6)
        ty += int(42 * s)


BEREIK = [  # gewricht, tekst, richting van het kaartje (dx, dy in px bij 2400 breed)
    ("Neck", "Neck · ball · ±{g}°", (-300, -40)),
    ("Right shoulder", "Shoulder · ball · ±{g}°", (-330, 10)),
    ("Left elbow", "Elbow · hinge · 0–{g}°", (300, -150)),
    ("Left knee", "Knee · hinge · 0–{g}°", (340, 40)),
]


def bereik(img, s, meta, P):
    """Kaartjes bij vier gewrichten, met het bereik dat de add-on op dat gewricht zette (json, uit de records)."""
    d = ImageDraw.Draw(img)
    for naam, tekst, (dx, dy) in BEREIK:
        q = meta["punten"].get(naam)
        if not q:
            continue
        g = q["graden"]
        g = int(round(float(g)))
        x, y = P(q["beeld"])
        tx, ty = x + dx * s, y + dy * s
        d = ImageDraw.Draw(img)
        half = (d.textlength(tekst.format(g=g), font=font("Inter.ttf", int(30 * s), "SemiBold")) + 36 * s) / 2
        tx = max(half + 40 * s, min(tx, img.size[0] - half - 40 * s))   # kaartje binnen het beeld
        eind = (tx - half if tx > x else tx + half, ty)
        d.line(((x, y), eind), fill=GOUD + (255,), width=max(3, int(4 * s)))
        r = int(9 * s)
        d.ellipse((x - r, y - r, x + r, y + r), fill=GOUD + (255,), outline=(20, 12, 24, 255), width=max(2, int(3 * s)))
        bb = pil(img, s, (int(tx), int(ty)), tekst.format(g=g), maat=30)


def zoomkaart(img, s, x0, y0, meta):
    """Kaartje met de render van dichtbij: het scharnier van de linkerknie bij de stop (render-bereik-knie.png)."""
    pad = os.environ.get("GB_ZOOM")
    if not pad:
        return
    z = Image.open(pad).convert("RGBA")
    W0, H0 = z.size
    k = [float(v) for v in os.environ.get("GB_ZOOM_KADER", "0,0,1,1").split(",")]   # uitsnede, 0..1
    z = z.crop((int(W0 * k[0]), int(H0 * k[1]), int(W0 * k[2]), int(H0 * k[3])))
    h = int(400 * s)
    z = z.resize((h, h), Image.LANCZOS)
    tw = int(400 * s)
    bw, bh = h + tw, h
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((x0, y0 + 8, x0 + bw, y0 + bh + 8), radius=int(28 * s), fill=(0, 0, 0, 170))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(14)))
    m = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, bw - 1, bh - 1), radius=int(28 * s), fill=255)
    kaart = Image.new("RGBA", (bw, bh), (20, 12, 28, 255))
    kaart.paste(z, (0, 0))
    img.paste(kaart, (x0, y0), m)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), radius=int(28 * s), outline=GOUD + (255,), width=max(2, int(2 * s)))
    tx = x0 + h + int(30 * s)
    f1 = font("Bricolage.ttf", int(44 * s), "Bold")
    f2 = font("Inter.ttf", int(30 * s), "Medium")
    ty = y0 + int(70 * s)
    stop = int(round(float(meta["stop_graden"])))
    for t in ("Built-in", f"end stop at {stop}°"):
        schaduw_tekst(img, [((tx, ty), t, f1, CREME)], 6)
        ty += int(58 * s)
    ty += int(14 * s)
    for t in passend(d, "The knee hinge, up close: it can't bend past the limit of your rig. 0.20\u00a0mm clearance.", f2,
                     tw - int(56 * s)):
        schaduw_tekst(img, [((tx, ty), t, f2, ZACHT)], 6)
        ty += int(42 * s)


def maak(basis, W, H, meta, dy, schaal):
    img = basis.copy()
    s = H / 1200.0 if W / H > 1.9 else H / 1080.0 * 0.92

    def P(q):
        return (q[0] * schaal[0], q[1] * schaal[1] - dy)
    x0 = int(W * 0.05)
    if MODUS == "knie":
        donker(img, int(W * 0.55))
        kop(img, s, x0, int(H * 0.12), ["Knees stop", "where your", "rig stops"],
            "Generated hinge with a real end stop, bend range in degrees, 0.20\u00a0mm clearance.", int(W * 0.36))
        boog(img, s, meta, P)
    elif MODUS == "klik":
        donker(img, int(H * 0.42), kant="boven", sterk=150)
        kop(img, s, x0, int(H * 0.06), ["Rig in. Parts out."],
            "One click turns your rigged model into printable parts with joints.", int(W * 0.21))
        klik(img, s, meta, P)
    elif MODUS == "bereik":
        donker(img, int(W * 0.55))
        kop(img, s, x0, int(H * 0.08), ["Every joint", "knows its limit"],
            "Hinges stop where your rig stops. Ball joints get their own swing.", int(W * 0.36))
        bereik(img, s, meta, P)
        zoomkaart(img, s, x0, int(H * 0.56), meta)
    else:
        donker(img, int(W * 0.55))
        kop(img, s, x0, int(H * 0.12), ["Find the fit", "for your", "printer"],
            "Five test joints, 0.10 to 0.30 mm. Keep the one that turns without wobble.", int(W * 0.37))
        strip(img, s, meta, P)
        inzet(img, s, x0, int(H * 0.62))
    return img.convert("RGB")


def main():
    meta = json.load(open(META, encoding="utf-8"))
    r = Image.open(RENDER).convert("RGBA")
    if r.size != (2400, 1350):
        r = r.resize((2400, 1350), Image.LANCZOS)
    a = r.crop((0, 75, 2400, 1275))
    maak(a, 2400, 1200, meta, 75, (2400, 1350)).save(os.path.join(UIT, f"{MODUS}-2400x1200.jpg"), quality=92)
    b = r.resize((1920, 1080), Image.LANCZOS)
    maak(b, 1920, 1080, meta, 0, (1920, 1080)).save(os.path.join(UIT, f"{MODUS}-1920x1080.jpg"), quality=92)
    print("klaar", MODUS)


main()
