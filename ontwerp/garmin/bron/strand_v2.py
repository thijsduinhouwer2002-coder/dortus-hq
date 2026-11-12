# Blad strand v2 (Mila, run 53, 12 nov): Today en 8 weeks in dezelfde stijl als de werelden (rond, zacht, witte glans,
# AMOLED zacht verloop, MIP 64 kleuren, dieren met donkere omtrek van 1 px op MIP). Inhoud en regels van strand v1 blijven:
# een schelp per sessie op haar uur, alle even groot, geen inhoudtijd; 8 golven, gehaald = brekende golf, het dier surft.
# Nieuw (de haak): een spoor van pootjes langs de getijdenlijn van schelp naar schelp tot het dier: je dag als strandwandeling.
# Nacht: zelfde scherm door de nachtregel (ebb-nachtregel-v1.json), tekst blijft.
#   python3 strand_v2.py <uitmap>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import krab_keuring2 as K           # zwemband, nachtregel, donkere omtrek
import werelden_v21 as w
import horloge_sim as h
from werelden_v21 import Doek, WIT, ZON
from blad_v13 import kader
from PIL import Image, ImageDraw, ImageChops

K.OMTREK['modus'] = 'wit'
ZAND, NAT, DONKERZAND, INKT = (255, 255, 170), (170, 170, 85), (85, 85, 0), (0, 0, 85)
ROZE, ROZE_D, ROZE_L = (255, 170, 170), (255, 85, 85), (255, 255, 255)
CYAAN = (0, 255, 255)


def X_uur(u): return 36 + u / 24 * 188


def zeilboot(d, hx, hy):
    """Bootje ver op de horizon (zelfde als de strandfamilie in werelden v5): rode romp, wit en geel zeil."""
    d.blob([(hx - 9, hy - 3), (hx + 9, hy - 3), (hx + 6, hy + 1), (hx - 6, hy + 1)], (255, 0, 0), WIT, 1)
    d.blob([(hx - 1, hy - 4), (hx - 1, hy - 20), (hx + 9, hy - 5)], WIT)
    d.blob([(hx - 3, hy - 4), (hx - 3, hy - 15), (hx - 9, hy - 5)], (255, 255, 170))


def lucht_klok(d, uur, kam, zon=True):
    """Overdag (6 tot 18) de krab-lucht met een zon op een boog die de klok volgt; anders nachtblauw met maan."""
    dag = uur is not None and 6 <= uur < 18
    if dag:
        if d.am:
            d.verloop(0, kam * .55, (0, 30, 95), (0, 75, 165)); d.verloop(kam * .55, kam, (0, 75, 165), (0, 165, 250))
        else:
            d.verloop(0, kam, (0, 85, 170), (0, 170, 255), [(kam - 22, (0, 170, 255))])
        if not zon: return dag
        t = (uur - 6) / 12; zx, zy = 40 + t * 180, kam - 14 - 16 * math.sin(math.pi * t)
        if d.am: d.gloed_ellips(zx, zy, 14, 14, (255, 255, 170), .35)
        d.rondje(zx, zy, 9, 9, ZON, WIT, glans=WIT, dikte=1.6)
        zeilboot(d, 214 if zx < 130 else 50, kam - 3)
    else:
        d.verloop(0, kam, (0, 0, 85), (0, 0, 170), [(kam - 22, (0, 0, 170))])
        for x, y in [(60, 22), (204, 30), (30, 52), (226, 56)]:
            d.rondje(x, y, .9, .9, WIT)
        d.rondje(214, kam - 22, 8, 8, (255, 255, 170), (170, 170, 255), dikte=1.2)
        d.rondje(218, kam - 23, 7, 7.5, (0, 0, 170) if not d.am else (0, 25, 120))
    return dag


def zee_en_strand(d, kam, nat, droog, nacht=False):
    ZAND_, NAT_ = ((170, 170, 85), (85, 85, 0)) if nacht else (ZAND, NAT)   # bij nacht een trede donkerder zand, dan pas de nachtregel
    # zee
    if d.am: d.verloop(kam, nat, (0, 105, 160), (0, 60, 130))
    else: d.dr.rectangle([0, kam * d.s, d.N, nat * d.s], fill=(0, 85, 170))
    d.golf(kam, nat, (0, 85, 170) if not d.am else (0, 100, 160), 2.5, 3)
    d.golf(kam + 5, nat, (0, 85, 255) if not d.am else (0, 80, 150), 2, 3, 1.2)
    pts = [d.P(x, kam + 2.5 * math.sin(x / 260 * 2 * math.pi * 3)) for x in range(0, 261, 2)]
    d.dr.line(pts, fill=WIT, width=max(1, round(1.6 * d.s)))
    # nat zand met witte getijdenlijn, droog zand met ronde duintjes
    d.golf(nat, 260, NAT_, 2, 4)
    pts = [d.P(x, nat + 2 * math.sin(x / 260 * 2 * math.pi * 4)) for x in range(0, 261, 2)]
    d.dr.line(pts, fill=WIT, width=max(1, round(1.4 * d.s)))
    d.golf(droog, 260, ZAND_, 1.5, 2)


def schelp(d, x, y, k=1.0):
    """Waaierschelp, punt onder op (x, y). 18 breed, 16 hoog bij k 1. Witte rand en glans zoals de dieren."""
    n = 9; R = 9 * k
    waaier = [(x, y)] + [(x + R * math.cos(math.radians(200 + i * 140 / (n - 1))) * 1.05, y - 4 * k + R * math.sin(math.radians(200 + i * 140 / (n - 1))) * 1.2) for i in range(n)]
    d.blob(waaier, ROZE, WIT, 1.4)
    for a in (-34, -12, 12, 34):
        t = math.radians(-90 + a)
        d.dr.line([d.P(x, y - 1), d.P(x + .82 * R * math.cos(t), y - 4 * k + .9 * R * math.sin(t) * 1.2)], fill=ROZE_D, width=max(1, round(1.3 * d.s)))
    d.blob([(x - 4 * k, y + .5), (x + 4 * k, y + .5), (x + 2 * k, y - 2.5 * k), (x - 2 * k, y - 2.5 * k)], ROZE_D)
    d.rondje(x - 3.5 * k, y - 11 * k, 1.6 * k, 1.2 * k, WIT)


def pootjes(d, x0, x1, y):
    """Spoor van kleine pootafdrukken (paartjes) langs de getijdenlijn."""
    stap = 7
    x = x0
    i = 0
    while x < x1 - 4:
        yy = y + (1.6 if i % 2 else -1.6) + .8 * math.sin(x / 9)
        d.rondje(x, yy, 1.9, 1.4, (85, 85, 0))
        x += stap; i += 1


def dier_gespiegeld(d, nr, cx, cy, maat260):
    wie = w.D[nr]
    m = round(maat260 * d.D / 260)
    _, _, ox, oy = kader(wie, m)
    lag = Image.new('RGB', (d.D, d.D), (1, 2, 3)); ld = ImageDraw.Draw(lag)
    h.teken(ld, wie, round(cx * d.D / 260 - ox), round(cy * d.D / 260 - oy), m)
    mk = ImageChops.difference(lag, Image.new('RGB', (d.D, d.D), (1, 2, 3))).convert('L').point(lambda v: 255 if v else 0)
    c = round(cx * d.D / 260)
    # spiegel rond cx
    lag = lag.transpose(Image.FLIP_LEFT_RIGHT); mk = mk.transpose(Image.FLIP_LEFT_RIGHT)
    dx = 2 * c - d.D
    lag = ImageChops.offset(lag, dx, 0); mk = ImageChops.offset(mk, dx, 0)
    lag = lag.resize((d.N, d.N), Image.NEAREST); mk = mk.resize((d.N, d.N), Image.NEAREST)
    d.im.paste(lag, (0, 0), mk)


def today(D_, am, sessies, nu, nr, eerste, nacht=False):
    d = Doek(D_, am)
    INKT, DONKERZAND = ((255, 255, 170), (255, 255, 170)) if nacht else ((0, 0, 85), (85, 85, 0))
    kam, nat, droog = 78, 128, 152
    lucht_klok(d, nu, kam); zee_en_strand(d, kam, nat, droog, nacht)
    d.tekst(130, 18, 'today', 26, CYAAN)
    for u in (0, 6, 12, 18, 24):
        x = X_uur(u)
        d.dr.rectangle([d.P(x - .6, droog), d.P(x + .6, droog + 3)], fill=DONKERZAND)
        d.tekst(x, droog + 3, str(u), 14, DONKERZAND, False)
    # schelpen op hun uur, tweede rij in het ondiepe water als het te druk wordt
    eind = [-99, -99]; xs = []
    for u in sessies:
        x = X_uur(u)
        if x - eind[0] >= 19: rij = 0
        elif x - eind[1] >= 19: rij = 1
        else: rij = 0; x = eind[0] + 19
        xs.append((x, nat + 13 - rij * 15)); eind[rij] = x
    loper = nr in (3, 4)
    vorige = max([x for x, _ in xs], default=None)
    xd = X_uur(nu) if vorige is None else (vorige + 30 if vorige + 30 <= 212 else vorige - 30)
    xd = min(xd, 212)
    # het spoor: van de eerste schelp tot het dier (alleen lopers laten pootjes na; zwemmers een rij belletjes in het ondiepe)
    if xs:
        a, b = min(xs[0][0], xd), max(xs[-1][0], xd)
        if loper: pootjes(d, a, b, nat + 6)
        else:
            for x in range(int(a), int(b), 11): w.bellen(d, [(x, nat - 9 + 1.5 * math.sin(x), 2)], WIT)
    for x, y in xs: schelp(d, x, y, 1.0)
    # nu: een klein wit golfje op de getijdenlijn
    d.blob([(X_uur(nu) + dx, nat - 1 + dy) for dx, dy in [(-6, 0), (-3, -3), (0, -4), (3, -3), (6, 0), (3, -1), (0, -2), (-3, -1)]], WIT)
    dier_gespiegeld(d, nr, xd, 132 if loper else 112, 26)
    n = len(sessies)
    d.tekst(130, 178, f'{n} shell{"s" if n != 1 else ""} today' if n else 'no shells yet', 22, INKT)
    d.tekst(130, 204, f'first shell {eerste}' if eerste else 'one session leaves one', 16, INKT, False)
    return d.klaar()


def golf(d, x, basis, hoog, vol, kop=True):
    if not vol:
        pts = [(x, basis), (x + 6, basis - hoog * .28), (x + 12, basis - hoog * .34), (x + 18, basis - hoog * .26), (x + 24, basis)]
        d.blob(pts, (0, 170, 255), WIT, 1.2); return
    lijf = [(x, basis), (x + 4, basis - hoog * .45), (x + 10, basis - hoog * .9), (x + 16, basis - hoog), (x + 21, basis - hoog * .85),
            (x + 22, basis - hoog * .6), (x + 18, basis - hoog * .7), (x + 16, basis - hoog * .5), (x + 22, basis)]
    d.blob(lijf, (0, 170, 255), WIT, 1.4)
    if kop:
        krul = [(x + 8, basis - hoog * .82), (x + 12, basis - hoog * .98), (x + 16, basis - hoog - 2), (x + 21, basis - hoog * .9),
                (x + 23, basis - hoog * .62), (x + 20, basis - hoog * .78), (x + 16, basis - hoog * .86), (x + 12, basis - hoog * .84)]
        d.blob(krul, WIT)
        d.rondje(x + 23, basis - hoog * .6, 1.6, 1.6, WIT)


def weken(D_, am, gehaald, voortgang, nr, uur=14.0, nacht=False):
    d = Doek(D_, am)
    INKT, DONKERZAND = ((255, 255, 170), (255, 255, 170)) if nacht else ((0, 0, 85), (85, 85, 0))
    kam, nat, droog = 150, 164, 178
    lucht_klok(d, uur, kam, zon=False); zee_en_strand(d, kam, nat, droog, nacht)
    d.tekst(130, 18, '8 weeks', 26, CYAAN)
    basis, hoog = 154, 36
    for i, g in enumerate(gehaald + [None]):
        x = 28 + i * 25.5
        if g is None:
            hh = max(8, hoog * voortgang); golf(d, x, basis, hh, True, kop=voortgang >= 1)
            d.dier(x + 14, basis - hh - 8, 16, w.D[nr])
        else:
            golf(d, x, basis, hoog, g)
    d.tekst(130, 62, f'{sum(gehaald)} big waves', 22, WIT)
    d.tekst(130, 88, 'one wave a week', 15, (170, 255, 255), False)
    d.tekst(56, 182, '8 wk ago', 14, DONKERZAND, False)
    d.tekst(208, 182, 'now', 14, DONKERZAND, False)
    d.tekst(130, 204, 'this week: 2 of 3', 16, INKT, False)
    return d.klaar()


def met_nacht(fn, D_, am):
    """Nachtregel op alles behalve tekst. Het tekstmasker komt uit een derde beeld met alle tekst in sleutelkleur FF00FF,
    want lichte nachttekst op (overdag) licht zand geeft anders geen verschil."""
    a = fn(); b = K.zonder_tekst(fn)
    oud = w.tekst
    w.tekst = lambda dr, x, y, t, font, c: oud(dr, x, y, t, font, (255, 0, 255))
    try: sleutel = fn()
    finally: w.tekst = oud
    return K.nachtregel_masker(a, b, sleutel, am)


VOORBEELDEN = [
    ('today-3', lambda D_, am: today(D_, am, [7.2, 12.6, 15.1], 15.5, 3, '7:12'), False),
    ('today-0', lambda D_, am: today(D_, am, [], 9.0, 4, None), False),
    ('today-5', lambda D_, am: today(D_, am, [7.0, 7.3, 7.6, 13.0, 16.5], 17.0, 7, '7:00'), False),
    ('today-3-nacht', lambda D_, am: today(D_, am, [7.2, 12.6, 21.1], 21.5, 3, '7:12', nacht=True), True),
    ('weeks-5', lambda D_, am: weken(D_, am, [True, True, False, True, True, True, False], .66, 3), False),
    ('weeks-5-nacht', lambda D_, am: weken(D_, am, [True, True, False, True, True, True, False], .66, 3, uur=22.0, nacht=True), True),
]

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    for D_, am in ((260, False), (454, True)):
        K.OMTREK['modus'] = 'wit' if am else 'donker1'
        rij = []
        for naam, fn, nacht in VOORBEELDEN:
            im = met_nacht(lambda: fn(D_, am), D_, am) if nacht else fn(D_, am)
            im.save(os.path.join(uit, f'{naam}-{D_}.png')); rij.append(im)
        k = 2 if D_ == 260 else 1; W = D_ * k; g = 10
        ov = Image.new('RGB', (len(rij) * (W + g) + g, W + 2 * g), (30, 30, 30))
        for i, im in enumerate(rij): ov.paste(im.resize((W, W), Image.NEAREST), (g + i * (W + g), g))
        ov.save(os.path.join(uit, f'strand-{D_}-rij-{k}x.png'))
