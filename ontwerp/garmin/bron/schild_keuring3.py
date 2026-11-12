# Schildpad na frisse keuring 3 (Mila, run 55, 12 nov): drie punten van de hoofdchat (07:35 NL).
#  1. Kop met donkere omlijning (000055, 1 px) en duidelijk oog; het blad in de bek wordt een los, licht slablad
#     (bleekgeel FFFFAA met groene nerven en gekrulde rand: de schildpad met een slablaadje leest in een blik).
#     Regel voor alle werelden: achter de held staat nooit iets in dezelfde kleurfamilie als de held.
#     Daarom: geen spriet met hap meer achter zijn kop, en een open plek in de weide rond de held (ook op het eindscherm).
#  2. Nachtregel v1.3: de held valt bij nacht niet weg. Groene en bruine kleuren van de held houden hun dagkleur
#     (een tint lichter dan de regel), en zijn donkere omtrek wordt bij nacht een smalle lichte rand (5555AA).
#  3. Nachtwater op MIP: een dieper gedempt blauw (000055) met dunne golflijnen in 0000AA, geen felle blokken.
#  Na twee frisse kijkers (keuring 3b en 3c): ook het slablad werd niet herkend en plakte aan de kop. Besluit: geen voedsel
#  in de bek; zijn grap is de meeuw die meeliftet. Onder water: open plek, groot oog met lichtpuntje, donkere omtrek.
#  slablad() blijft in dit bestand staan (bek=True) voor wie het later opnieuw wil proberen.
# Bouwt op krab_keuring2.py en werelden_v32.py; verandert daar niets.   python3 schild_keuring3.py <uitmap>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import krab_keuring2 as k2          # zet ook de donkere omtrek-functie op h.teken
import werelden_v21 as w
import werelden_v32 as v32
v3 = sys.modules['werelden_v3']
import horloge_sim as h
from blad_v13 import kader
from PIL import Image, ImageDraw, ImageChops, ImageFilter
import numpy as np

WIT = (255, 255, 255)
SLA, SLA_NERF = (255, 255, 170), (0, 170, 85)
OMTREK_DAG, OMTREK_NACHT = (0, 0, 85), (85, 85, 170)
HELD = {'mk': None}          # masker van de held op eindmaat (D), voor de nachtregel van de held


def _held_masker(D_, mk):
    HELD['mk'] = mk if HELD['mk'] is None or HELD['mk'].size != mk.size else ImageChops.lighter(HELD['mk'], mk)


# ---------- 1. held: omtrek, slablad, open plek ----------
def dier_kantel(d, cx, cy, maat, wie, hoek):
    """Als v3.dier_kantel, met donkere omtrek van 1 px en het masker van de held voor de nachtregel."""
    m = round(maat * d.D / 260)
    _, _, ox, oy = kader(wie, m)
    lag = Image.new('RGB', (d.D, d.D), (1, 2, 3)); ld = ImageDraw.Draw(lag)
    X, Y = round(cx * d.D / 260 - ox), round(cy * d.D / 260 - oy)
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)):
        h.delen(ld, wie, X + dx, Y + dy, m, h.hx('000055'), 2)
    o = h.delen(ld, wie, X, Y, m, None, 0)
    h.ogen(ld, wie, o, X, Y, m, 'v83')
    if wie is v3.SCHILD: groot_oog(lag)
    mk = ImageChops.difference(lag, Image.new('RGB', (d.D, d.D), (1, 2, 3))).convert('L').point(lambda v: 255 if v else 0)
    if hoek:
        c = (cx * d.D / 260, cy * d.D / 260)
        lag = lag.rotate(-hoek, Image.NEAREST, center=c); mk = mk.rotate(-hoek, Image.NEAREST, center=c)
    _held_masker(d.D, mk)
    d.im.paste(lag.resize((d.N, d.N), Image.NEAREST), (0, 0), mk.resize((d.N, d.N), Image.NEAREST))


def groot_oog(lag):
    """Keuring 3b: het oog groter, wit met een zwarte pupil en een wit lichtpuntje, zodat het gezicht in een blik leest."""
    a = np.asarray(lag)
    ys, xs = np.where((a[..., 0] == 0) & (a[..., 1] == 0) & (a[..., 2] == 0))   # achtergrond van de laag is (1, 2, 3)
    if not len(xs): return
    # de pupil is het zwarte groepje dat het meest links ligt (de schildpad kijkt naar links)
    x0 = xs.min(); sel = xs <= x0 + 4
    ex, ey = xs[sel].mean(), ys[sel].mean()
    r = max(3.0, lag.width / 260 * 3.2)
    dr = ImageDraw.Draw(lag)
    dr.ellipse([ex - r - 1, ey - r - 1, ex + r + 1, ey + r + 1], fill=(0, 0, 85))
    dr.ellipse([ex - r, ey - r, ex + r, ey + r], fill=(255, 255, 255))
    pr = r * .62
    dr.ellipse([ex - pr - .6, ey - pr + .4, ex + pr - .6, ey + pr + .4], fill=(0, 0, 0))
    dr.point([(round(ex - pr * .6), round(ey - pr * .5))], fill=(255, 255, 255))


def slablad(d, bx, by, k=1.0):
    """Los slablad dat uit zijn bek hangt: bleekgeel met groene nerven en een gekrulde rand; een hap uit de punt."""
    # keuring 3b: het blad raakt het gezicht niet meer; een steeltje in de bek, het blad hangt eronder en ervoor
    lw0 = max(1, round(1.6 * d.s))
    d.dr.line([d.P(bx - 3 * k, by + 1 * k), d.P(bx - 9 * k, by + 5 * k)], fill=SLA_NERF, width=lw0)
    bx, by = bx - 9 * k, by + 5 * k
    pts = []
    n = 28
    for i in range(n):
        t = i / n * 2 * math.pi
        rx, ry = 15 * k, 9 * k
        krul = 1 + .13 * math.sin(7 * t)            # gekrulde rand: sla, geen gras
        x = -rx * (1 + math.cos(t)) * krul * .95
        y = ry * math.sin(t) * krul
        # hap uit de punt (links), rond
        if math.cos(t) < -.85 and abs(math.sin(t)) < .35: x *= .86
        a = math.radians(-30)                      # hangt schuin naar beneden-links uit de bek
        pts.append((bx + x * math.cos(a) - y * math.sin(a), by + 2 * k + x * math.sin(a) + y * math.cos(a)))
    d.blob(pts, SLA, SLA_NERF, 1.4)
    a = math.radians(-30)
    p = lambda x, y: d.P(bx + x * math.cos(a) - y * math.sin(a), by + 2 * k + x * math.sin(a) + y * math.cos(a))
    lw = max(1, round(1.2 * d.s))
    d.dr.line([p(0, 0), p(-26 * k, 0)], fill=SLA_NERF, width=lw)
    for xx in (-8, -15, -21):
        d.dr.line([p(xx * k, 0), p((xx - 4) * k, -5 * k)], fill=SLA_NERF, width=lw)
        d.dr.line([p(xx * k, 0), p((xx - 4) * k, 5 * k)], fill=SLA_NERF, width=lw)
    # masker voor de nachtregel van de held (het blad hoort bij hem)
    mk = Image.new('L', (d.D, d.D), 0)
    ImageDraw.Draw(mk).polygon([(x * d.D / 260, y * d.D / 260) for x, y in pts], fill=255)
    _held_masker(d.D, mk.filter(ImageFilter.MaxFilter(3)))


def wereld_schild(d, dd, hx=124, hy=186, m=40, spiegel=False, held=True, zak=0, vrij=None, bek=False):
    """Zeegrasweide zoals v3, maar met een open plek rond de held: geen groen achter hem (regel hoofdchat 07:35)."""
    s = d.s
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in [(60, 196, 90, 18), (210, 192, 80, 22)]:
        d.rondje(cx, cy + zak, rx, ry, verder)
    d.dr.ellipse([-60 * s, (206 + zak) * s, 320 * s, 340 * s], fill=w.ZAND_DONKER)
    d.dr.ellipse([-50 * s, (210 + zak) * s, 310 * s, 340 * s], fill=w.ZAND if not d.am else (235, 225, 150))
    if d.am: d.gloed_ellips(hx, 230 + zak, 52, 10, WIT, .4)
    X = (lambda x: 260 - x) if spiegel else (lambda x: x)
    if vrij is None and held: vrij = (hx - 1.45 * m, hx + 1.2 * m)
    def mag(x0, buig=0):            # spriet (voet en top) helemaal buiten de open plek
        if not vrij: return True
        xs = (X(x0), X(x0) + buig)
        return all(x < vrij[0] or x > vrij[1] for x in xs)
    g, gl, gd = v3.GRAS, v3.GRAS_L, v3.GRAS_D
    for x0, L, b in [(14, 86, 8), (28, 104, 9), (42, 74, 8), (56, 54, 7)]:
        bg = (10 if x0 % 3 else -8) * (-1 if spiegel else 1)
        if mag(x0, bg): v3.spriet(d, X(x0), 222 + zak, L, bg, b, gd if x0 < 30 else g, gl)
    for x0, L, b in [(204, 60, 7), (218, 92, 9), (234, 78, 8), (248, 98, 8)]:
        bg = (-12 if x0 % 4 else 9) * (-1 if spiegel else 1)
        if mag(x0, bg): v3.spriet(d, X(x0), 224 + zak, L, bg, b, g if x0 > 210 else gd, gl)
    d.rondje(X(176), 240 + zak, 6, 4, (255, 170, 170), WIT, dikte=1.2)
    d.rondje(X(96), 244 + zak, 5, 3, (170, 170, 255), WIT, dikte=1.2)
    for x0, y0, n, L, c in [(34, 232, 5, 30, gd), (52, 240, 4, 20, g), (226, 232, 5, 32, g), (206, 242, 4, 18, gd)]:
        if mag(x0 - 8) and mag(x0 + 8): v3.pluk(d, X(x0), y0 + zak, n, L, c, gl)
    v3.zeester(d, X(190), 230 + zak, 7.5)
    if held:
        if d.am: d.gloed_ellips(hx + 4, hy + m * .72, m * .95, 4.5, (90, 80, 40), .45, groei=.25)
        else: d.rondje(hx + 4, hy + m * .72, m * .9, 4, w.ZAND_DONKER)
        dier_kantel(d, hx, hy, m, v3.SCHILD, 7)
        if bek: slablad(d, hx - .86 * m, hy + .06 * m - 5, m / 40)


def eind_schild(D_, am, dd, nacht):
    """Eindscherm v3.2 d, met een open plek achter de schildpad: links geen sprieten en plukken (x 20 tot 132)."""
    oud = v3.wereld_schild
    v3.wereld_schild = lambda d, dd_, **kw: wereld_schild(d, dd_, vrij=(20, 132), **kw)
    oud_dk, oud_bb = v3.dier_kantel, v3.blad_in_bek
    v3.dier_kantel = dier_kantel
    v3.blad_in_bek = lambda d, bx, by, k=1.0: None     # keuring 3c: geen blad, het gezicht is vrij
    try:
        return v32.eind(D_, am, dd, nacht, 'schild')
    finally:
        v3.wereld_schild, v3.dier_kantel, v3.blad_in_bek = oud, oud_dk, oud_bb


def zet_schild():
    v3.wereld_schild = wereld_schild
    v3.dier_kantel = dier_kantel
    v3.blad_in_bek = lambda d, bx, by, k=1.0: None     # keuring 3c: geen blad


# ---------- 2. nachtregel v1.3 voor de held ----------
def groen_of_bruin(c):
    r, g, b = c
    if g >= r and g > b: return True                       # groen (00AA55, AAFF55, 005500, 55AA00 ...)
    if r >= g > b and r <= 170: return True                # bruin en olijf (AA5500, 555500, AAAA55 ...)
    return False


def held_nacht(im_dag, am):
    """Kleuren van de held bij nacht: groen en bruin houden hun dagkleur (AMOLED: 80 procent), de donkere omtrek wordt 5555AA,
    alle andere kleuren gaan gewoon door de nachtregel."""
    a = np.asarray(im_dag).astype(np.int16).copy()
    uit = np.asarray(k2.nachtregel(im_dag, im_dag, am, masker_van=im_dag)).astype(np.int16).copy()   # gewone regel op alles
    H, W_, _ = a.shape
    plat = a.reshape(-1, 3); u = uit.reshape(-1, 3)
    for i in range(plat.shape[0]):
        c = tuple(int(v) for v in plat[i])
        if c == OMTREK_DAG or (am and max(c) <= 40 and c[2] >= c[0]):
            u[i] = OMTREK_NACHT
        elif groen_of_bruin(c) and max(c) > 0:
            u[i] = [round(v * (.8 if am else 1.0)) for v in c]
    return Image.fromarray(u.reshape(H, W_, 3).clip(0, 255).astype(np.uint8), 'RGB')


# ---------- 3. nachtwater MIP ----------
def mip_nachtwater(im, tekstmasker):
    """Elke felle blauwe vlak (0000AA en 0000FF) in het water wordt 000055; om de 18 px een dunne golflijn 0000AA."""
    a = np.asarray(im).copy()
    blauw = ((a[..., 0] == 0) & (a[..., 1] == 0) & (a[..., 2] >= 170))
    vrij = np.asarray(tekstmasker) == 0
    a[blauw & vrij] = (0, 0, 85)
    D_ = a.shape[0]
    for y0 in range(D_ // 2 - 30, D_, 18):
        for x in range(D_):
            y = int(y0 + 2 * math.sin(x / D_ * 2 * math.pi * 3 + y0))
            if 0 <= y < D_ and tuple(a[y, x]) == (0, 0, 85) and vrij[y, x]:
                a[y, x] = (0, 0, 170)
    return Image.fromarray(a, 'RGB')


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']


def scherm(naam):
    if naam == 'eind': return eind_schild
    return v32.scherm(naam, 'schild')


def maak(naam, D_, am, nacht):
    f = scherm(naam)
    dd = w.NACHT if nacht else w.DAG
    HELD['mk'] = None
    im = f(D_, am, dd, nacht)
    mk = HELD['mk']
    if not nacht:
        return im
    leeg = k2.zonder_tekst(lambda: f(D_, am, dd, nacht))
    tmk = ImageChops.difference(im, leeg).convert('L').point(lambda v: 255 if v > 8 else 0).filter(ImageFilter.MaxFilter(3))
    uit = k2.nachtregel(im, leeg, am)
    if not am:
        uit = mip_nachtwater(uit, ImageChops.lighter(tmk, mk if mk is not None else Image.new('L', im.size, 0)))
    if mk is not None:
        mk = ImageChops.darker(mk, ImageChops.invert(tmk))          # tekst gaat voor
        uit = Image.composite(held_nacht(im, am), uit, mk)
    return uit


def overzicht(b, D_, k, pad):
    g = 12 * k; W = D_ * k; n = len(NAMEN)
    ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
    for j, nacht in enumerate((False, True)):
        for i, naam in enumerate(NAMEN):
            ov.paste(b[(naam, nacht)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
    ov.save(pad)


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    zet_schild()
    for D_, am in ((454, True), (260, False)):
        b = {}
        for nacht in (False, True):
            for naam in NAMEN:
                im = maak(naam, D_, am, nacht); b[(naam, nacht)] = im
                im.save(os.path.join(uit, f'schild-{naam}-{"nacht" if nacht else "dag"}-{D_}.png'))
        for k in ((1, 2) if D_ == 260 else (1,)):
            overzicht(b, D_, k, os.path.join(uit, f'overzicht-schild-{D_}-{k}x.png'))
