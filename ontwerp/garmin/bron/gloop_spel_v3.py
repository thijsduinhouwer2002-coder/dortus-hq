# Gloop op je pols, voorstel v3 (Mila, 16 nov 2026), bovenop v2 (gloop_spel_v2.py).
# Nieuw na Daans keuring van v2 (16 nov 02:55, twee kan-punten):
#  - beeld 3: de helm zat over Gloops blije oogboog, klein las dat als een frons. Nu staat de toren
#    hoger op zijn kruin en is de boog dikker overgetrokken.
#  - beeld 2 nieuw: de grap in één beeld. De held duikt ondersteboven in Gloops mond, alleen zijn
#    benen en blauwe lijf steken er nog uit, de helm schiet omhoog naar de toren.
#   python3 gloop_spel_v3.py <rendermap> <uitmap>
import sys, os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.argv = sys.argv[:3]
import gloop_spel_v2 as v2

R, UIT = sys.argv[1], sys.argv[2]


def held_benen():
    # held-vallen ligt al ondersteboven (benen boven, hoofd met helm onder). Schild eruit, knippen
    # boven het hoofd: wat overblijft steekt straks uit de mond.
    h = Image.open(os.path.join(R, "held-vallen.png")).convert("RGBA")
    px = h.load()
    for y in range(0, 70):
        for x in range(262, 400):
            px[x, y] = (0, 0, 0, 0)
    for y in range(h.height):   # vloerschaduw van de render weg (halfdoorzichtig), anders klopt de bbox niet
        for x in range(h.width):
            if px[x, y][3] < 200:
                px[x, y] = (0, 0, 0, 0)
    return v2.bijsnijden(h.crop((0, 0, 400, KNIP)))


KNIP = 125   # net onder de riem: benen, riem en halve buik
HELD_B = 1.25
HOEK = 22
GLOOP_B = 0.42


def mond(g):
    # mondvlek in de hap-render (na zonder_schaduw): paarsbruin, rond (115, 64, 85)
    px = g.load(); xs = []; ys = []
    for y in range(int(g.height * 0.62), g.height):
        for x in range(g.width):
            r, gg, b, a = px[x, y]
            if a > 240 and 90 < r < 150 and gg < 90 and b > 60 and r > gg + 25:
                xs.append(x); ys.append(y)
    return min(xs), min(ys), max(xs), max(ys)


def slok(N):
    H = v2.hoeden()
    im = v2.achtergrond(N)
    d = ImageDraw.Draw(im)
    cx, voet = N / 2, N * 0.90
    gb = N * GLOOP_B   # groter dan in beeld 1 en 2: dit is de grap
    hap = v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-hap-h0.png")).convert("RGBA"))
    top_y, top_x = v2.toren(im, hap, [H[4], H[1]], N, cx, voet, gb, 1)
    g = v2.schaal(hap, gb)
    gx, gy = int(cx - g.width / 2), int(voet - g.height)
    m0x, m0y, m1x, m1y = mond(g)
    mcx, mcy = (m0x + m1x) / 2, (m0y + m1y) / 2
    ruw = held_benen()   # buikbal is ±90 px breed in de render; even breed als de mond
    f = (m1x - m0x) * HELD_B / 90
    hb = ruw.resize((round(ruw.width * f), round(ruw.height * f)), Image.LANCZOS).rotate(HOEK, expand=True, resample=Image.BICUBIC)
    hb = v2.bijsnijden(hb)
    # de knip (onderkant) valt in de bovenste helft van de mond
    hx = int(gx + mcx - hb.width * 0.5)
    hy = int(gy + m0y + (m1y - m0y) * 0.60 - hb.height)
    im.alpha_composite(hb, (hx, hy))
    # onderlip en tong van Gloop eroverheen: de held zit echt IN de mond
    lip = Image.new("L", g.size, 0)
    ImageDraw.Draw(lip).rectangle([0, int(m0y + (m1y - m0y) * 0.50), g.width, g.height], fill=255)
    laag = Image.new("RGBA", g.size, (0, 0, 0, 0)); laag.paste(g, (0, 0), lip)
    im.alpha_composite(laag, (gx, gy))
    # helm vliegt naar de toren
    pan = v2.schaal(H[0], N * 0.15).rotate(-24, expand=True, resample=Image.BICUBIC)
    px_, py_ = int(top_x - pan.width / 2 + N * 0.10), int(top_y - pan.height - N * 0.03)
    for k in range(3):
        xx = px_ + pan.width * (0.25 + 0.25 * k)
        d.line([(xx, py_ + pan.height + N * 0.005), (xx, py_ + pan.height + N * 0.045)], fill=(255, 245, 220), width=max(2, int(N * 0.01)))
    im.alpha_composite(pan, (px_, py_))
    v2.tekst(d, (N * 0.22, N * 0.50), "GULP!", 0.09, N, (255, 255, 255))
    v2.tekst(d, (px_ + pan.width + N * 0.06, py_ + pan.height * 0.5), "+1", 0.07, N, (255, 214, 90))
    v2.teller(im, 3, N, H[0])
    return v2.rond(im, N)


KRUIN = 0.13   # v2 had 0.30: de eerste hoed zakte over Gloops oog (Daan, beeld 3)


def toren_v3(im, gloop, hoedlijst, N, cx, voet_y, gloop_breed, kantelzaad=1, extra=None):
    g = v2.schaal(gloop, gloop_breed)
    gx, gy = int(cx - g.width / 2), int(voet_y - g.height)
    ImageDraw.Draw(im).ellipse([gx + g.width * 0.08, voet_y - N * 0.025, gx + g.width * 0.95, voet_y + N * 0.02],
                               fill=(85, 0, 0, 255) if v2.MIP else (70, 34, 20, 255))
    im.alpha_composite(g, (gx, gy))
    rnd = random.Random(kantelzaad)
    y = gy + g.height * KRUIN
    x = cx + g.width * 0.03
    stuk = []
    for i, h in enumerate(hoedlijst):
        hb = v2.schaal(h, gloop_breed * rnd.uniform(0.40, 0.48)).rotate(rnd.uniform(-12, 12), expand=True, resample=Image.BICUBIC)
        y_top = y - hb.height * 0.78
        stuk.append((hb, int(x - hb.width / 2), int(y_top)))
        y = y_top + hb.height * 0.22
        x += rnd.uniform(-0.06, 0.06) * gloop_breed
    for hb, hx, hy in stuk:
        im.alpha_composite(hb, (hx, hy))
    return y, x


def dikke_boog(src, uit):
    # blije oogboog van Gloop dikker: donkere pixels in de bovenste 70% oprekken met een MaxFilter
    g = Image.open(src).convert("RGBA")
    px = g.load()
    m = Image.new("L", g.size, 0); pm = m.load()
    for y in range(int(g.height * 0.15), int(g.height * 0.60)):
        for x in range(g.width):
            r, gg, b, a = px[x, y]
            if a > 240 and r < 90 and gg < 80 and b < 110:
                pm[x, y] = 255
    m = m.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(0.8))
    g.paste(Image.new("RGBA", g.size, (40, 32, 58, 255)), (0, 0), m)
    g.save(uit)


if __name__ == "__main__":
    import shutil, tempfile
    tmp = tempfile.mkdtemp()
    for f in os.listdir(R):
        shutil.copy(os.path.join(R, f), tmp)
    dikke_boog(os.path.join(R, "gloop-blij-h0.png"), os.path.join(tmp, "gloop-blij-h0.png"))
    R = tmp; v2.R = tmp
    v2.toren = toren_v3
    os.makedirs(UIT, exist_ok=True)
    for nr in (1, 3):
        v2.MIP = False; v2.beeld(nr, 454).convert("RGB").save(os.path.join(UIT, f"v3-amoled-454-beeld{nr}.png"))
        v2.MIP = True; v2.rond(v2.mip(v2.beeld(nr, 260)).convert("RGBA"), 260).convert("RGB").save(os.path.join(UIT, f"v3-mip-260-beeld{nr}.png"))
    v2.MIP = False; a = slok(454); a.convert("RGB").save(os.path.join(UIT, "v3-amoled-454-slok.png"))
    v2.MIP = True; m = v2.rond(v2.mip(slok(260)).convert("RGBA"), 260); m.convert("RGB").save(os.path.join(UIT, "v3-mip-260-slok.png"))
    print("klaar")
