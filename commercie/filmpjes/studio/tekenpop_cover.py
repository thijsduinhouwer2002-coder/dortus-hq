"""Tekst op de renders van de tekenpop: cover B met de pop, de dynamische cover (met en zonder label -25%) en het
vergelijkingsblad robot tegen pop (tekenpop-agent, 23 nov 2026). Zelfde letters, kleuren en tekst als cover B van
ontwerp/click-joints-pro-v2 (die functies worden hergebruikt uit bron/maak_beelden.py).

python3 tekenpop_cover.py <rendermap> <uitmap> <fontmap> <icoon.svg> <robot-cover-b-1280x720.png>
Het label "-25%" klopt alleen in de saleweek: kortingscode CYBER25, 25 procent op Click Joints Pro op Gumroad,
27 nov tot en met 1 dec 2026 (berichten/hoofdchat.md). Niet op Superhive gebruiken.
"""
import importlib.util
import os
import sys

from PIL import Image, ImageDraw, ImageFilter

RENDER, UIT, FONTS, ICOON = sys.argv[1:5]
ROBOT = sys.argv[5] if len(sys.argv) > 5 else ""
HIER = os.path.dirname(os.path.abspath(__file__))
_pad = os.path.join(HIER, "..", "..", "..", "ontwerp", "click-joints-pro-v2", "bron", "maak_beelden.py")
sys.argv = [_pad, RENDER, UIT, FONTS, ICOON]
_spec = importlib.util.spec_from_file_location("maak_beelden", _pad)
MB = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(MB)
os.makedirs(UIT, exist_ok=True)
PRUIM = (46, 31, 58)


def tekstblok(img, t):
    """Zelfde tekst en plek als cover B."""
    W, Hh = img.size
    s = Hh / 1200
    x = int(150 * s)
    img.alpha_composite(MB.icoon(int(124 * s)), (x, int(190 * s)))
    ImageDraw.Draw(img).text((x + int(150 * s), int(222 * s)), "Add-on for Blender",
                             font=MB.tekst(int(46 * s), "SemiBold"), fill=t["klein"])
    MB.schaduw(img, (x - int(6 * s), int(350 * s)), "Click Joints\nPro", MB.kop(int(200 * s)), t["kop"], r=18,
               spatie=int(-10 * s))
    MB.schaduw(img, (x, int(790 * s)), "Rig in. Joints out.", MB.kop(int(96 * s)), t["accent"], r=14)
    ImageDraw.Draw(img).text((x, int(930 * s)), "Ball joints and hinges, with the bend\nrange in degrees.",
                             font=MB.tekst(int(44 * s)), fill=t["cover_sub"], spacing=int(10 * s))


def zijlicht(img, breed=0.52, sterkte=150):
    """Donkere zachte rand links, zodat de tekst leesbaar blijft als er een onderdeel achter vliegt."""
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    w = int(img.width * breed)
    for x in range(w):
        d.line([(x, 0), (x, img.height)], fill=(20, 13, 27, int(sterkte * (1 - x / w) ** 1.8)))
    img.alpha_composite(laag)


def label(img, cx, cy, d):
    """Gouden sticker in de stijl van Dortus: rond, iets gekanteld, -25% groot en de code eronder."""
    S = 3 * d   # eerst groot tekenen, dan verkleinen (gladde randen)
    st = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    g = ImageDraw.Draw(st)
    g.ellipse([0, 0, S - 1, S - 1], fill=MB.GOUD + (255,))
    r = int(S * 0.045)
    g.ellipse([r, r, S - 1 - r, S - 1 - r], outline=PRUIM + (255,), width=max(3, int(S * 0.012)))
    f1 = MB.kop(int(S * 0.34))
    f2 = MB.tekst(int(S * 0.085), "Bold")
    f3 = MB.tekst(int(S * 0.07), "SemiBold")
    for s_, f, y in (("-25%", f1, 0.46), ("CYBER25", f2, 0.70), ("until Dec 1", f3, 0.80)):
        bx = g.textbbox((0, 0), s_, font=f)
        g.text(((S - (bx[2] - bx[0])) / 2 - bx[0], S * y - (bx[3] - bx[1]) / 2 - bx[1]), s_, font=f, fill=PRUIM + (255,))
    st = st.rotate(9, resample=Image.BICUBIC).resize((d, d), Image.LANCZOS)
    sch = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).ellipse([cx - d // 2 + 6, cy - d // 2 + 18, cx + d // 2 + 6, cy + d // 2 + 18], fill=(0, 0, 0, 120))
    img.alpha_composite(sch.filter(ImageFilter.GaussianBlur(d // 14)))
    img.alpha_composite(st, (cx - d // 2, cy - d // 2))


def dynamisch(sale):
    img = MB.laad("b", "dyn169", (2560, 1440))
    if img is None:
        return None
    zijlicht(img)
    tekstblok(img, MB.TEKST["b"])
    if sale:
        label(img, int(2560 * 0.40), int(1440 * 0.155), 300)
    naam = "cover-pop-dynamisch-sale.png" if sale else "cover-pop-dynamisch.png"
    p = MB.opslaan(img, naam)
    img.convert("RGB").resize((1280, 720), Image.LANCZOS).save(p.replace(".png", "-1280x720.png"), optimize=True)
    return p


def vergelijk(paren):
    """Groot (1280 x 720) twee aan twee, en klein zoals in een lijst (400 x 225)."""
    beelden = []
    for p, lab in paren:
        if p and os.path.exists(p):
            im = Image.open(p).convert("RGB")
            if abs(im.width / im.height - 16 / 9) > 0.02:
                h = int(im.width * 9 / 16)
                y = (im.height - h) // 2
                im = im.crop((0, y, im.width, y + h))
            beelden.append((im.resize((1280, 720), Image.LANCZOS), lab))
    if not beelden:
        return None
    W = 2 * 1280 + 3 * 40
    rijen = (len(beelden) + 1) // 2
    H = 120 + rijen * 800 + 40 + 70 + 225 + 60 + 80
    img = Image.new("RGB", (W, H), (236, 236, 240))
    d = ImageDraw.Draw(img)
    d.text((40, 40), "Groot (1280 x 720)", font=MB.tekst(40, "SemiBold"), fill=(40, 40, 50))
    for i, (b, lab) in enumerate(beelden):
        r, k = divmod(i, 2)
        x, y = 40 + k * 1320, 120 + r * 800
        img.paste(b, (x, y))
        d.text((x, y + 732), lab, font=MB.tekst(34, "SemiBold"), fill=(40, 40, 50))
    y0 = 120 + rijen * 800 + 40
    d.text((40, y0), "Klein, zoals in een lijst (400 x 225)", font=MB.tekst(40, "SemiBold"), fill=(40, 40, 50))
    for i, (b, lab) in enumerate(beelden):
        x = 40 + i * 440
        img.paste(b.resize((400, 225), Image.LANCZOS), (x, y0 + 70))
        d.text((x, y0 + 70 + 235), lab.split(" (")[0].replace("Tekenpop dynamisch, saleweek", "Dynamisch, sale"), font=MB.tekst(26, "SemiBold"), fill=(40, 40, 50))
    return MB.opslaan(img, "vergelijk-pop.png")


if __name__ == "__main__":
    gemaakt = [MB.cover("b", "pop169", (2560, 1440), "cover-b-pop-2560x1440.png", klein=(1280, 720)),
               dynamisch(False), dynamisch(True)]
    gemaakt.append(vergelijk([
        (ROBOT, "Cover B met robot (nu in click-joints-pro-v2)"),
        (os.path.join(UIT, "cover-b-pop-2560x1440-1280x720.png"), "Cover B met tekenpop"),
        (os.path.join(UIT, "cover-pop-dynamisch-1280x720.png"), "Tekenpop dynamisch"),
        (os.path.join(UIT, "cover-pop-dynamisch-sale-1280x720.png"), "Tekenpop dynamisch, saleweek (-25%)"),
    ]))
    for f in os.listdir(UIT):
        if f.startswith("_icoon"):
            os.remove(os.path.join(UIT, f))
    print("gemaakt:", [os.path.basename(g) for g in gemaakt if g])
