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


def lucht_klok(d, uur, kam, zon=True, tekst_tot=None):
    """Overdag (6 tot 18) de krab-lucht met een zon op een boog die de klok volgt; anders nachtblauw met maan."""
    dag = uur is not None and 6 <= uur < 18
    if dag:
        if d.am:
            kn = .8 if tekst_tot else .55     # met tekst in de lucht: het lichte blauw pas vlak boven de horizon
            d.verloop(0, kam * kn, (0, 30, 95), (0, 75, 165)); d.verloop(kam * kn, kam, (0, 75, 165), (0, 165, 250))
        else:
            d.verloop(0, kam, (0, 85, 170), (0, 170, 255), [(kam - (5 if tekst_tot else 22), (0, 170, 255))])
        if not zon: return dag
        t = (uur - 6) / 12; zx, zy = 40 + t * 180, kam - 14 - 16 * math.sin(math.pi * t)
        if tekst_tot and 56 < zx < 204:     # de zon staat achter de tekst: dan zie je hem als schittering op het water
            for i, (dy, L) in enumerate([(6, 14), (11, 10), (16, 7), (21, 4)]):
                d.dr.line([d.P(zx - L / 2, kam + dy), d.P(zx + L / 2, kam + dy)], fill=(255, 255, 170), width=max(1, round(1.6 * d.s)))
        else:
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
    ZAND_, NAT_ = ((85, 85, 170), (0, 0, 85)) if nacht else ((ZAND, NAT) if not d.am else ((255, 235, 170), (215, 195, 125)))   # bij nacht koel blauwgrijs zand (keuring: olijfgeel was te fel), dan de nachtregel
    # zee
    z1, z2 = ((0, 0, 170), (0, 0, 170)) if nacht else ((0, 85, 170), (0, 85, 255))     # nacht: zee een trede donkerder, dan de nachtregel
    if d.am: d.verloop(kam, nat, (0, 105, 160) if not nacht else (0, 30, 120), (0, 60, 130) if not nacht else (0, 15, 80))
    else: d.dr.rectangle([0, kam * d.s, d.N, nat * d.s], fill=z1)
    d.golf(kam, nat, z1 if not d.am else ((0, 100, 160) if not nacht else (0, 30, 120)), 2.5, 3)
    d.golf(kam + 5, nat, z2 if not d.am else ((0, 80, 150) if not nacht else (0, 20, 100)), 2, 3, 1.2)
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
        d.rondje(x, yy, 2.4, 1.7, (85, 85, 0))
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
    """v2.1 (keuring 2 van run 53): tekst bovenin de lucht, het strand groter en voller, schelpen twee keer zo groot."""
    d = Doek(D_, am)
    INKT, LABEL = ((170, 170, 170), (170, 170, 170)) if nacht else ((0, 0, 85), (85, 85, 0))
    kam, nat, droog = 64, 112, 160
    lucht_klok(d, nu, kam, tekst_tot=50); zee_en_strand(d, kam, nat, droog, nacht)
    n = len(sessies)
    d.tekst(130, 8, 'today', 22, (85, 170, 255) if nacht else CYAAN)
    d.tekst(130, 28, f'{n} shell{"s" if n != 1 else ""}' if n else 'no shells yet', 22, (170, 170, 255) if nacht else WIT)
    korrels(d, droog, nacht)
    for u in (0, 6, 12, 18, 24):       # kleine streepjes, alleen 0, 12 en 24 met een cijfer
        x = X_uur(u)
        d.dr.rectangle([d.P(x - .6, droog + 2), d.P(x + .6, droog + 5)], fill=LABEL)
        if u % 12 == 0: d.tekst(x, droog + 5, str(u), 13, LABEL, False)
    # schelpen op hun uur (groot), tweede rij in het ondiepe water als het te druk wordt
    eind = [-99, -99]; xs = []
    for u in sessies:
        x = X_uur(u)
        if x - eind[0] >= 30: rij = 0
        elif x - eind[1] >= 30: rij = 1
        else: rij = 0; x = eind[0] + 30
        xs.append((x, nat + 34 - rij * 20)); eind[rij] = x
    loper = nr in (3, 4)
    vorige = max([x for x, _ in xs], default=None)
    xd = X_uur(nu) if vorige is None else (vorige + 36 if vorige + 36 <= 208 else vorige - 36)
    xd = min(max(xd, 52), 208)
    if xs:
        a, b = min(xs[0][0], xd), max(xs[-1][0], xd)
        if loper: pootjes(d, a, b, nat + 12)
        else:
            for x in range(int(a), int(b), 12): w.bellen(d, [(x, nat - 10 + 1.5 * math.sin(x), 2.4)], WIT)
    for x, y in xs: schelp(d, x, y, 2.0)
    d.blob([(X_uur(nu) + dx, nat - 1 + dy) for dx, dy in [(-7, 0), (-3.5, -3.5), (0, -4.5), (3.5, -3.5), (7, 0), (3.5, -1), (0, -2), (-3.5, -1)]], WIT)
    if loper:
        dier_gespiegeld(d, nr, xd, nat + 22, 36)
    else:     # zwemmers springen uit de branding: boogje schuim en druppels onder hen
        dier_gespiegeld(d, nr, xd, nat - 22, 36)
        d.dr.arc([d.P(xd - 20, nat - 26), d.P(xd + 20, nat + 4)], 200, 340, fill=WIT, width=max(1, round(1.8 * d.s)))
        for dx, dy in [(-17, -7), (-12, -14), (14, -10), (18, -4)]: d.rondje(xd + dx, nat + dy, 1.7, 1.7, WIT)
    d.tekst(130, 198, f'first shell {eerste}' if eerste else 'one session leaves one', 16, INKT, False)
    return d.klaar()


def korrels(d, droog, nacht):
    """Droog zand met korrels, een zeestertje en een gaatje: het strand leeft (keuring 2 van run 53)."""
    c = (85, 85, 170) if nacht else (170, 170, 85)
    for x, y in [(44, 182), (62, 196), (84, 186), (178, 184), (196, 196), (214, 182), (120, 228), (150, 232), (100, 220), (170, 222), (70, 214), (196, 214)]:
        d.rondje(x, y, 1.1, 1.1, c)
    zx, zy, R = 210, 206, 7      # zeestertje
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rr = R if i % 2 == 0 else R * .45
        pts.append((zx + rr * math.cos(a), zy + rr * math.sin(a)))
    d.blob(pts, (255, 170, 0), WIT, 1.2)
    d.rondje(zx - 1.5, zy - 2, 1, 1, (255, 255, 170))
    d.rondje(52, 208, 3.2, 1.8, c)   # gaatje van een krab


def golf(d, x, basis, hoog, vol, kop=True, b=22):
    k = b / 22
    X = lambda v: x + v * k
    if not vol:
        pts = [(X(0), basis), (X(6), basis - 5), (X(12), basis - 6), (X(18), basis - 5), (X(22), basis)]   # gemiste week: plat en kalm, met witte rand
        d.blob(pts, (0, 170, 255), WIT, 1.6); return
    lijf = [(X(0), basis), (X(4), basis - hoog * .45), (X(10), basis - hoog * .9), (X(16), basis - hoog), (X(21), basis - hoog * .85),
            (X(22), basis - hoog * .6), (X(18), basis - hoog * .7), (X(16), basis - hoog * .5), (X(22), basis)]
    d.blob(lijf, (0, 170, 255), WIT, 1.4)
    d.blob([(X(2), basis), (X(6), basis - hoog * .5), (X(11), basis - hoog * .72), (X(14), basis - hoog * .5), (X(17), basis)], (0, 85, 255))   # diepte in de golf
    if kop:
        krul = [(X(8), basis - hoog * .82), (X(12), basis - hoog * .98), (X(16), basis - hoog - 2), (X(21), basis - hoog * .9),
                (X(23), basis - hoog * .62), (X(20), basis - hoog * .78), (X(16), basis - hoog * .86), (X(12), basis - hoog * .84)]
        d.blob(krul, WIT)
        d.rondje(X(23), basis - hoog * .6, 1.6 * k, 1.6 * k, WIT)


def weken(D_, am, gehaald, voortgang, nr, uur=14.0, nacht=False):
    d = Doek(D_, am)
    INKT, DONKERZAND = ((255, 255, 170), (255, 255, 170)) if nacht else ((0, 0, 85), (85, 85, 0))
    kam, nat, droog = 150, 164, 178
    lucht_klok(d, uur, kam, zon=False); zee_en_strand(d, kam, nat, droog, nacht)
    d.tekst(130, 12, '8 weeks', 24, (85, 170, 255) if nacht else CYAAN)
    basis, hoog = 156, 44
    for i, g in enumerate(gehaald):          # zeven weken: gehaald = brekende golf, gemist = plat en kalm
        golf(d, 12 + i * 21.5, basis, hoog, g, b=24)
    # deze week: een grote golf (groeit met de voortgang) en het dier groot op een surfplank erop: de haak
    hh = 40 + 30 * min(1, voortgang); xg = 170
    golf(d, xg, basis, hh, True, kop=True, b=58)
    tx, ty = xg + 58 * 16 / 22, basis - hh
    d.blob([(tx - 17, ty - 1), (tx + 15, ty - 5), (tx + 18, ty - 3), (tx - 15, ty + 3)], (255, 255, 85), WIT, 1.2)   # plank
    d.dr.line([d.P(tx - 14, ty + 1), d.P(tx + 15, ty - 3.5)], fill=(255, 0, 0), width=max(1, round(1.4 * d.s)))
    d.dier(tx, ty - 16, 34, w.D[nr])
    d.tekst(104, 40, f'{sum(gehaald)} big waves', 22, (170, 170, 255) if nacht else WIT)
    d.tekst(104, 64, 'one wave a week', 15, (170, 255, 255), False)
    d.tekst(52, 182, '8 wk ago', 14, DONKERZAND, False)
    d.tekst(200, 182, 'now', 14, DONKERZAND, False)
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
