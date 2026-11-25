"""Sale-versie van het Gumroad-hoofdbeeld met de robot (Beeldmaker, 25 nov 2026, issue #56).

python3 sale.py <robot-uit-labels-1920x1080.jpg> <uit.jpg> <fontmap>

Zet rechtsboven, in de lege hoek naast het hoofd, dezelfde gouden sticker als de tekenpop-sale
(commercie/filmpjes/studio/tekenpop_cover.py): rond, iets gekanteld, "-25%" groot, "CYBER25" en "until Dec 1" eronder.
Het beeld zelf blijft gelijk (GESLAAGD, sets click-joints-pro-robot-gumroad).
Klopt alleen in de saleweek op Gumroad: code CYBER25, 25 procent, 27 nov t/m 1 dec 2026
(platformen/blender/pro-sale-27nov.md). Niet op Superhive gebruiken (daar 35%, zonder code). Na 1 dec terug naar
robot-uit-labels-1920x1080.jpg.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BRON, UIT, FONTS = sys.argv[1:4]
GOUD, PRUIM = (255, 196, 84), (46, 31, 58)


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


def sticker(img, cx, cy, d):
    S = 3 * d  # groot tekenen, dan verkleinen voor gladde randen
    st = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    g = ImageDraw.Draw(st)
    g.ellipse([0, 0, S - 1, S - 1], fill=GOUD + (255,))
    r = int(S * 0.045)
    g.ellipse([r, r, S - 1 - r, S - 1 - r], outline=PRUIM + (255,), width=max(3, int(S * 0.012)))
    regels = (
        ("-25%", font("Bricolage.ttf", int(S * 0.27), "ExtraBold"), 0.45),
        ("CYBER25", font("Inter.ttf", int(S * 0.095), "Bold"), 0.68),
        ("until Dec 1", font("Inter.ttf", int(S * 0.08), "SemiBold"), 0.81),
    )
    for s_, f, y in regels:
        bx = g.textbbox((0, 0), s_, font=f)
        g.text(((S - (bx[2] - bx[0])) / 2 - bx[0], S * y - (bx[3] - bx[1]) / 2 - bx[1]), s_, font=f,
               fill=PRUIM + (255,))
    st = st.rotate(9, resample=Image.BICUBIC).resize((d, d), Image.LANCZOS)
    sch = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).ellipse([cx - d // 2 + 5, cy - d // 2 + 14, cx + d // 2 + 5, cy + d // 2 + 14],
                                fill=(0, 0, 0, 130))
    img.alpha_composite(sch.filter(ImageFilter.GaussianBlur(d // 14)))
    img.alpha_composite(st, (cx - d // 2, cy - d // 2))


img = Image.open(BRON).convert("RGBA")
s = img.width / 1920
sticker(img, int(1735 * s), int(140 * s), int(244 * s))
img.convert("RGB").save(UIT, quality=95, subsampling=0)
print("gemaakt", UIT, img.size)
