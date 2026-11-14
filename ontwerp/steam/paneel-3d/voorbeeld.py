"""Voorbeeld van het paneel in de echte strook (Daan, 14 nov 2026). Ronde 2 (±03:50 UTC), na de frisse kijker (7,5):
warmer pruim en dikkere rand (paneel.py), 4 px lucht rondom, zachtere grotere schaduw naar het hol, knop lichter en warmer
met grotere letter, zachte schaduw onder de titel en het muntje.
    python3 voorbeeld.py <strook-160.png van main> <paneel-bron-384.png> <map voor de uitvoer>
Maten op 160 px: rand 18, titel 18, tekst 15, knop 26 hoog met hoek 13, 4 px vrij van rechterrand, boven en onder.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys, os
HIER = os.path.dirname(os.path.abspath(__file__))
st = Image.open(sys.argv[1]).convert('RGBA').crop((0, 598, 1024, 768))
src = Image.open(sys.argv[2]).convert('RGBA')
UIT = sys.argv[3]


def nine(dst, rect, m, src, b=128):
    x0, y0, x1, y1 = rect; S = src.size[0]
    xs = [x0, x0 + m, x1 - m, x1]; ys = [y0, y0 + m, y1 - m, y1]; bs = [0, b, S - b, S]
    for i in range(3):
        for j in range(3):
            w = xs[i + 1] - xs[i]; h = ys[j + 1] - ys[j]
            part = src.crop((bs[i], bs[j], bs[i + 1], bs[j + 1])).resize((w, h), Image.LANCZOS)
            dst.alpha_composite(part, (xs[i], ys[j]))


def font(sz, w):
    f = ImageFont.truetype(os.path.join(HIER, 'Fredoka.ttf'), sz); f.set_variation_by_axes([w, 100]); return f


def tekst(a, xy, s, f, kleur, anchor='la', schaduw=True):
    if schaduw:
        sh = Image.new('RGBA', a.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((xy[0], xy[1] + 1), s, font=f, fill=(20, 6, 24, 170), anchor=anchor)
        a.alpha_composite(sh.filter(ImageFilter.GaussianBlur(1)))
    ImageDraw.Draw(a).text(xy, s, font=f, fill=kleur, anchor=anchor)


def mock(st):
    a = st.copy()
    # het oude pixelpaneel weg: hol-wand van links ernaast eroverheen (alleen voor dit voorbeeld)
    a.alpha_composite(st.crop((560, 0, 700, 122)), (690, 0)); a.alpha_composite(st.crop((560, 0, 700, 122)), (830, 0))
    a.alpha_composite(st.crop((560, 0, 614, 122)), (970, 0))
    R = (690, 14, 1018, 118)
    sh = Image.new('RGBA', a.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    d.rounded_rectangle((R[0] - 2, R[1] + 3, R[2], R[3] + 5), 14, fill=(24, 8, 28, 150))
    a.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6))); nine(a, R, 18, src)
    tekst(a, (708, 30), "Big Gloop", font(18, 600), (255, 210, 90))
    tekst(a, (708, 55), "Bought.", font(15, 450), (246, 232, 206), schaduw=False)
    S = 4; c = Image.new('RGBA', (20 * S, 20 * S), (0, 0, 0, 0)); cd = ImageDraw.Draw(c)
    cd.ellipse((1 * S, 3 * S, 19 * S, 20 * S), fill=(30, 10, 30, 120))
    cd.ellipse((0, 0, 17 * S, 17 * S), fill=(170, 105, 30)); cd.ellipse((1 * S, 1 * S, 15 * S, 15 * S), fill=(242, 182, 50))
    cd.ellipse((4 * S, 3 * S, 9 * S, 7 * S), fill=(255, 240, 170))
    a.alpha_composite(c.resize((20, 20), Image.LANCZOS), (962, 31))
    tekst(a, (986, 30), "27", font(17, 600), (246, 232, 206))
    bx = (708, 80, 822, 106)
    sh = Image.new('RGBA', a.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((bx[0], bx[1] + 2, bx[2], bx[3] + 2), 13, fill=(20, 6, 24, 150))
    a.alpha_composite(sh.filter(ImageFilter.GaussianBlur(2)))
    d = ImageDraw.Draw(a)
    d.rounded_rectangle(bx, 13, fill=(232, 176, 64))
    d.rounded_rectangle((bx[0] + 2, bx[1] + 2, bx[2] - 2, bx[3] - 2), 11, fill=(122, 66, 108))
    d.rounded_rectangle((bx[0] + 4, bx[1] + 3, bx[2] - 4, bx[1] + 10), 6, fill=(146, 88, 128))   # glans bovenin
    tekst(a, ((bx[0] + bx[2]) // 2, (bx[1] + bx[3]) // 2 + 1), "Undo  +45", font(16, 600), (255, 232, 160), anchor='mm')
    return a


oud = st.copy(); nieuw = mock(st)
both = Image.new('RGBA', (1024, 340), (30, 20, 35, 255)); both.alpha_composite(oud, (0, 0)); both.alpha_composite(nieuw, (0, 170))
both.save(os.path.join(UIT, 'kaartje-voor-na-160-ware-grootte-ronde2.png'))
z = Image.new('RGBA', (1002, 672)); z.alpha_composite(oud.crop((688, 8, 1022, 122)).resize((1002, 342), Image.NEAREST), (0, 0))
z.alpha_composite(nieuw.crop((688, 8, 1022, 122)).resize((1002, 342), Image.LANCZOS), (0, 330))
z.save(os.path.join(UIT, 'kaartje-voor-na-3x-ronde2.png'))
