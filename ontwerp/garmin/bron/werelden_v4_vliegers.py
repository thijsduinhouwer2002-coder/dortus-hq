# Werelden v4, familie vliegers (run 50, 12 nov): Ray, Manta, Dolphin, Swordfish in de opzet van krab, schildpad en clownvis (v3.2).
# Hergebruikt werelden_v21 (Doek, water, tekst), werelden_v3 (lucht, zee, kantelen) en werelden_v32 (bundel, indeling).
# Per dier een eigen plek onder water en een eigen grapvoorwerp (de sticker zelf blijft zoals hij is):
#  - ray: wit zand met rimpels / toets 22: hij IS een vlieger: lattenkruis over zijn ruit, lange staart met drie strikjes
#    (rood, geel, groen) en een touwtje naar de golfkam; onder water houdt hij touwtje en staart (ufo vervallen)
#  - manta: open water met een zandbank ver weg / reclamevliegtuigje met een spandoekje met een hartje;
#    onder water ligt het spandoekje opgerold op de zandbank; toets 22: manta donker van boven, witte schoudervlekken, hoornlobben
#  - dolphin: open water met lichtvlekken / duikbril met snorkel die uit de golf steekt; onder water staat de bril op zijn voorhoofd
#  - swordfish (ronde 3): open blauw met lichtstreepjes / zijn zwaard steekt door een grote roze donut met spikkels (boven, onder, eind);
#    (eerdere krullijn en zandhartje lazen niet, keuring blad 7)
# Coordinaten in 1/260 D.   python3 werelden_v4_vliegers.py <uitmap> [ray manta dolphin swordfish]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w
import werelden_v3 as v3
import werelden_v32 as v
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL, ROZE, ZAND, ZAND_DONKER, D, fonkel, stofjes, kring
from blad_v9 import stippen
from blad_v13 import kader
import horloge_sim as h
from PIL import Image, ImageDraw, ImageChops

N = {d_['naam']: d_ for d_ in D}
WIE = {'ray': N['Ray'], 'manta': N['Manta'], 'dolphin': N['Dolphin'], 'swordfish': N['Swordfish']}
VRIEND = {'ray': 'Seal', 'manta': 'Shark', 'dolphin': 'Orca', 'swordfish': 'Sunfish'}
HELD_AAN = True          # de meetscripts zetten dit uit: dan valt held plus grapvoorwerp weg
DONKER = (0, 0, 85)
GEEL_D = (255, 170, 0)

_merk = {}
def merk(wie):
    """Oog (zwarte pixels) en neuspunt (meest linkse pixel) van de sticker, in eenheden van de maat t.o.v. het midden."""
    if wie['naam'] in _merk: return _merk[wie['naam']]
    m, S = 100, 400
    _, _, ox, oy = kader(wie, m)
    lag = Image.new('RGB', (S, S), (1, 2, 3)); h.teken(ImageDraw.Draw(lag), wie, round(200 - ox), round(200 - oy), m)
    px = lag.load(); zw = []; links = (S, 0); boven = (0, S); onder = (0, 0)
    for y in range(S):
        for x in range(S):
            c = px[x, y]
            if c == (1, 2, 3): continue
            if max(c) < 30: zw.append((x, y))
            if x < links[0]: links = (x, y)
            if y < boven[1]: boven = (x, y)
            if y > onder[1]: onder = (x, y)
    if zw:
        # het oog: het zwarte groepje dat het meest links ligt (dolfijn/zwaardvis kijken naar links)
        x0 = min(p[0] for p in zw); oog = [p for p in zw if p[0] < x0 + 12]
        e = (sum(p[0] for p in oog) / len(oog), sum(p[1] for p in oog) / len(oog))
    else: e = (200, 200)
    f = lambda p: ((p[0] - 200) / m, (p[1] - 200) / m)
    _merk[wie['naam']] = dict(oog=f(e), neus=f(links), top=f(boven), staart=f(onder))
    return _merk[wie['naam']]


def rot(cx, cy, m, hoek):
    a = math.radians(hoek)
    def r(dx, dy):
        x, y = dx * m, dy * m
        return (cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a))
    return r


def lijn(d, pts, c, b):
    d.dr.line([d.P(*p) for p in pts], fill=c, width=max(1, round(b * d.s)), joint='curve')
    for p in (pts[0], pts[-1]): d.rondje(p[0], p[1], b / 2.2, b / 2.2, c)


def hartje(d, cx, cy, k, c, rand=WIT, rd=1.4):
    pts = [(cx + k * math.sin(t / 24 * 2 * math.pi) ** 3, cy - k / 16 * 13 * (13 * math.cos(t / 24 * 2 * math.pi) - 5 * math.cos(2 * t / 24 * 2 * math.pi) - 2 * math.cos(3 * t / 24 * 2 * math.pi) - math.cos(4 * t / 24 * 2 * math.pi)) / 13) for t in range(24)]
    d.blob(pts, c, rand, rd)
    return pts


# ---------------- grapvoorwerpen ----------------
# toets 22: de manta donker van boven (vaste MIP-tinten), witte schoudervlekken (de V op zijn rug) en
# twee duidelijke hoornlobben bij de bek. Grijs en zwart, dus nooit te verwarren met de olijfgroene rog-vlieger.
MANTA = dict(N['Manta']); MANTA['tint'] = ['0x555555', '0xFFFFFF', '0x000000']
def manta(d, cx, cy, m, hoek):
    v3.dier_kantel(d, cx, cy, m, MANTA, hoek)
    r = rot(cx, cy, m, hoek)
    for s_ in (-1, 1):
        x = lambda q: q * s_ - .04
        # witte schoudervlek (de V op de rug van een manta)
        d.blob([r(x(.30), -.24), r(x(.86), -.08), r(x(.50), -.06)], WIT)
        # hoornlob: korte dikke krul naar voren aan elke kant van de bek, donker met witte rand
        hart_ = [(.17 + .05 * math.sin(math.pi * t) - .05 * t ** 3, -.34 - .50 * math.sin(t * 1.35)) for t in [i / 14 for i in range(15)]]
        bl, br_ = [], []
        for i in range(len(hart_)):
            a_, b_ = hart_[max(0, i - 1)], hart_[min(len(hart_) - 1, i + 1)]
            tx, ty = b_[0] - a_[0], b_[1] - a_[1]; L_ = math.hypot(tx, ty) or 1
            wd = .085 * (1 - .30 * i / 14)
            bl.append((hart_[i][0] - ty / L_ * wd, hart_[i][1] + tx / L_ * wd)); br_.append((hart_[i][0] + ty / L_ * wd, hart_[i][1] - tx / L_ * wd))
        lob = [r(x(px_), py_) for px_, py_ in bl + list(reversed(br_))]
        d.blob(lob, (0, 0, 0), WIT, 1.4)


# toets 22: de rog IS een vlieger. Lattenkruis over zijn ruit, een lange staart met drie strikjes en een touwtje.
STRIK_KL = [(255, 0, 0), (255, 255, 0), (0, 255, 85)]
def strikje(d, x, y, k, c):
    for s_ in (-1, 1):
        d.blob([(x, y), (x + 6 * k * s_, y - 4.2 * k), (x + 7 * k * s_, y), (x + 6 * k * s_, y + 4.2 * k)], c, DONKER, 1.2)
    d.rondje(x, y, 1.8 * k, 1.8 * k, c, DONKER, dikte=1.0)


def vlieger(d, cx, cy, m, hoek, touw_naar=None, staart=None, lat=True):
    """De rog als vlieger. touw_naar: eindpunt van het touwtje (of None); staart: lijst richtingspunten t.o.v. de
    staartpunt in eenheden van m (de staart golft daarlangs)."""
    r = rot(cx, cy, m, hoek); k = max(.7, m / 38)
    if touw_naar is not None:      # touwtje eerst: het komt onder zijn buik vandaan
        a = r(0, .12); b = touw_naar
        mid = ((a[0] + b[0]) / 2 + 4, (a[1] + b[1]) / 2 + 6)        # licht doorhangend
        pts = [(a[0] * (1 - t) ** 2 + 2 * mid[0] * t * (1 - t) + b[0] * t * t, a[1] * (1 - t) ** 2 + 2 * mid[1] * t * (1 - t) + b[1] * t * t) for t in [i / 20 for i in range(21)]]
        d.dr.line([d.P(*q) for q in pts], fill=DONKER, width=max(2, round(2.8 * d.s)), joint='curve')
        d.dr.line([d.P(*q) for q in pts], fill=WIT, width=max(1, round(1.3 * d.s)), joint='curve')
    v3.dier_kantel(d, cx, cy, m, WIE['ray'], hoek)
    if lat:      # lattenkruis van een vlieger, dun bruin over de ruit
        bruin = (170, 85, 0)
        for p0, p1 in (((-.02, -.80), (-.04, .80)), ((-1.0, -.20), (1.0, -.20))):
            d.dr.line([d.P(*r(*p0)), d.P(*r(*p1))], fill=bruin, width=max(1, round(1.5 * d.s)))
    st = staart or [(.5, .5), (1.1, .7), (1.6, .6)]
    x0, y0 = r(-.04, .84)
    ankers = [(x0, y0)] + [(x0 + dx * m, y0 + dy * m) for dx, dy in st]
    pts = []
    for i in range(len(ankers) - 1):
        (ax, ay), (bx, by) = ankers[i], ankers[i + 1]
        for j in range(10):
            t = j / 10; nx_, ny_ = -(by - ay), (bx - ax); L = math.hypot(nx_, ny_) or 1
            g = 3.2 * k * math.sin(t * math.pi) * (1 if i % 2 else -1)
            pts.append((ax + (bx - ax) * t + nx_ / L * g, ay + (by - ay) * t + ny_ / L * g))
    pts.append(ankers[-1])
    d.dr.line([d.P(*q) for q in pts], fill=DONKER, width=max(2, round(3.4 * d.s)), joint='curve')
    d.dr.line([d.P(*q) for q in pts], fill=WIT, width=max(1, round(1.6 * d.s)), joint='curve')
    n = len(pts)
    for c, f in zip(STRIK_KL, (.30, .62, .96)):
        q = pts[min(n - 1, round(f * (n - 1)))]; strikje(d, q[0], q[1], k * 1.35, c)



RAY_IN, RAY_CALM = 28, 26     # hoogte van de rog boven de golf bij in en Calm (was 34 en 30)
def ufo_koepel(d, cx, cy, m, hoek):
    """Ronde 4: glazen koepel bovenop zijn rug, zoals op een vliegende schotel: lichtblauw glas, donkere omtrek,
    witte glimstreep en een grijze voetring. Alleen vaste kleuren, dus ook op MIP goed."""
    r = rot(cx, cy, m, hoek)
    R = .42; by = .00          # voet van de koepel midden op de rug
    boog = [r(R * math.cos(t), by - R * 1.05 * math.sin(t)) for t in [i / 16 * math.pi for i in range(17)]]
    d.blob(boog, (170, 255, 255), DONKER, 1.6)
    # glimstreep: dikke witte boog linksboven in het glas
    gl = [r(R * .70 * math.cos(t), by - R * .75 * math.sin(t)) for t in [i / 10 * math.pi for i in range(5, 9)]]
    d.dr.line([d.P(*q) for q in gl], fill=WIT, width=max(2, round(2.4 * d.s)), joint='curve')
    x, y = r(-R * .22, by - R * .72); d.rondje(x, y, 1.6, 1.6, WIT)
    # voetring
    pts = [r(R * 1.25 * math.cos(t), by + .10 * math.sin(t)) for t in [i / 16 * 2 * math.pi for i in range(16)]]
    d.blob(pts, (170, 170, 170), DONKER, 1.4)


def ufo_lichtjes(d, cx, cy, m, hoek, aan=True):
    """Ronde 4: drie grote gele lampen onder de rog, zoals onder een vliegende schotel."""
    r = rot(cx, cy, m, hoek)
    for dx, dy in [(-.52, .50), (0, .66), (.52, .50)]:
        x, y = r(dx, dy)
        k = .15 * m
        d.rondje(x, y, k, k, (255, 255, 0) if aan else (85, 85, 170), DONKER, dikte=1.4)
        if aan: d.rondje(x - k * .35, y - k * .35, k * .3, k * .3, WIT)


def ufo(d, cx, cy, m, hoek, aan=True):
    v3.dier_kantel(d, cx, cy, m, WIE['ray'], hoek)
    ufo_koepel(d, cx, cy, m, hoek)
    ufo_lichtjes(d, cx, cy, m, hoek, aan)


def ufo_bundel(d, cx, cy, m, yg, nacht):
    """Ronde 4: een duidelijke gele trapezium van onder de lampen tot op de golf, smal boven en breed onder,
    met een witte kern; drie vaste tinten, geen vlek."""
    y0 = cy + .55 * m
    tinten = [(255, 255, 85), (255, 255, 170), WIT]
    for (bo, on), c in zip([(.40 * m, 30), (.28 * m, 21), (.14 * m, 10)], tinten):
        d.blob([(cx - bo, y0), (cx + bo, y0), (cx + on, yg), (cx - on, yg)], c)


def donut(d, cx, cy, R=12):
    """Ronde 3 (swordfish): grote roze donut met spikkels; tekenen NA de vis, zodat het zwaard door het gat steekt."""
    ring = R * .62
    def ovaal(r_, c, dik):
        d.dr.ellipse([(cx - r_) * d.s, (cy - r_) * d.s, (cx + r_) * d.s, (cy + r_) * d.s], outline=c, width=max(1, round(dik * d.s)))
    ovaal(R + 1.4, WIT, ring + 2.8)
    ovaal(R, (170, 85, 0), ring)
    ovaal(R - .8, (255, 85, 170), ring * .78)
    kl = [(255, 255, 0), (85, 255, 255), WIT, (85, 255, 85), (255, 255, 0), WIT, (85, 255, 255), (85, 255, 85)]
    rm = R - ring / 2 - .4
    for i, c in enumerate(kl):
        t = i / len(kl) * 2 * math.pi + .3
        x, y = cx + rm * math.cos(t), cy + rm * math.sin(t)
        d.dr.line([d.P(x - 1.2 * math.sin(t + 1), y - 1.2 * math.cos(t + 1)), d.P(x + 1.2 * math.sin(t + 1), y + 1.2 * math.cos(t + 1))], fill=c, width=max(1, round(1.4 * d.s)))


def spandoek(d, x0, y0, b=62, hg=20, opgerold=False):
    """Spandoekje van een reclamevliegtuigje: wit doek met golvende onderrand en een groot roze hart."""
    if opgerold:
        # rol met een stuk doek dat er nog uit hangt, met het hart erop: zo herken je het spandoek
        d.blob([(x0 + b - 4, y0 - 7), (x0 + b + 26, y0 - 4), (x0 + b + 28, y0 + 14), (x0 + b - 4, y0 + 10)], WIT, DONKER, 1.4)
        hartje(d, x0 + b + 12, y0 + 3, 7, ROZE, None)
        d.rondje(x0 + b / 2, y0, b / 2, 7.5, WIT, DONKER, dikte=1.4)
        for i in range(1, 6): d.rondje(x0 + i * b / 6, y0, 1.2, 6, (170, 170, 170))
        d.rondje(x0, y0, 3, 7.5, (170, 170, 170), DONKER, dikte=1.0)
        return
    golf = lambda x, t: 2.6 * math.sin((x - x0) / b * 2 * math.pi + t)
    boven = [(x0 + i * b / 12, y0 + golf(x0 + i * b / 12, 0)) for i in range(13)]
    onder = [(x, y + hg) for x, y in reversed(boven)]
    d.blob(boven + onder, WIT, DONKER, 1.6)
    hartje(d, x0 + b / 2, y0 + hg / 2 + golf(x0 + b / 2, 0), 8, ROZE, None)
    return boven[0], onder[-1]


def duikbril(d, cx, cy, m, hoek, wie, op_voorhoofd=False, snorkel=True, snorkel_l=1.0):
    """Duikbril om het oog (alleen een dikke gele rand met donkere omtrek, het oog blijft zichtbaar), bandje naar achter,
    en een gele snorkel met een oranje mondstuk die recht omhoog steekt."""
    mk = merk(wie); ex, ey = mk['oog']
    if op_voorhoofd: ey -= .30; ex += .06
    r = rot(cx, cy, m, hoek)
    ox, oy = r(ex, ey); rx, ry = .31 * m, .23 * m
    a = math.radians(hoek)
    # bandje naar achter over de kop
    b0, b1 = r(ex + .20, ey - .03), r(ex + .62, ey - .12)
    lijn(d, [b0, b1], DONKER, 3.4); lijn(d, [b0, b1], (0, 85, 170), 2.0)
    # glas licht, dik geel montuur met donkere omtrek; het oog blijft erdoor zichtbaar
    d.rondje(ox, oy, rx, ry, (170, 255, 255), DONKER, dikte=4.2)
    d.dr.ellipse([(ox - rx) * d.s, (oy - ry) * d.s, (ox + rx) * d.s, (oy + ry) * d.s], outline=GEEL, width=max(2, round(2.6 * d.s)))
    d.rondje(ox - rx * .38, oy - ry * .36, 1.6, 1.6, WIT)
    if not op_voorhoofd:
        e = r(*merk(wie)['oog']); d.rondje(e[0], e[1], .06 * m, .06 * m, (0, 0, 0))
    if snorkel:
        sx, sy = r(ex + .46, ey - .11)
        L = .95 * m * snorkel_l
        pts = [(sx, sy), (sx, sy - L)]
        lijn(d, pts, DONKER, 7.6); lijn(d, pts, GEEL, 5.2)
        d.rondje(sx, sy - L - 2, 5.2, 3.6, (255, 85, 0), DONKER, dikte=1.3)
        return (sx, sy - L)


def krullijn(d, x_tip, y_tip, x_eind, y_lijn, nacht):
    """De witte lijn die de zwaardvis met zijn punt trekt: een lijn met lusjes, zoals schrijven, die eindigt bij de punt."""
    pts = []; n = 90
    for i in range(n + 1):
        t = i / n; x = x_eind + (x_tip - x_eind) * t
        lus = 5.0 * math.sin(t * 2 * math.pi * 4)
        pts.append((x - 4.5 * math.cos(t * 2 * math.pi * 4) + 4.5, y_lijn + lus * .9 + (y_tip - y_lijn) * t ** 6))
    lijn(d, pts, DONKER, 4.4); lijn(d, pts, WIT, 2.6)
    fonkel(d, x_tip, y_tip, 5)


def zand_hart(d, cx, cy, k):
    """Hartje in het zand getekend: een groef (donker zand) met een witte rand."""
    pts = hartje(d, cx, cy, k, ZAND_DONKER, None)
    pts = pts + [pts[0]]
    d.dr.line([d.P(*p) for p in pts], fill=WIT, width=max(1, round(3.2 * d.s)), joint='curve')
    d.dr.line([d.P(*p) for p in pts], fill=(170, 85, 85) if not d.am else (190, 120, 90), width=max(1, round(1.6 * d.s)), joint='curve')
    d.rondje(cx, cy, k * .55, k * .45, ZAND if not d.am else (235, 225, 150))


# ---------------- plekken onder water ----------------
def zandbodem(d, dd, zak=0, y=210, licht=True):
    s = d.s
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in [(50, 200, 80, 16), (220, 196, 70, 18)]: d.rondje(cx, cy + zak, rx, ry, verder)
    d.dr.ellipse([-60 * s, (y - 4 + zak) * s, 320 * s, 340 * s], fill=ZAND_DONKER)
    d.dr.ellipse([-50 * s, (y + zak) * s, 310 * s, 340 * s], fill=ZAND if not d.am else (235, 225, 150))


def kiezel(d, x, y, rx, ry, c): d.rondje(x, y, rx, ry, c, WIT, glans=WIT, dikte=1.4)


def bodem(d, y, c, rand=WIT, golf=2.0, n=2):
    """Bodem over de hele breedte met een golvende bovenrand (geen schijf)."""
    pts = [(x, y + golf * math.sin(x / 260 * 2 * math.pi * n)) for x in range(-4, 266, 2)]
    if rand: d.blob([(x, q - 1.6) for x, q in pts] + [(266, 270), (-4, 270)], rand)
    d.blob(pts + [(266, 270), (-4, 270)], c)


def bel_ring(d, x, y, r_):
    d.dr.ellipse([(x - r_) * d.s, (y - r_) * d.s, (x + r_) * d.s, (y + r_) * d.s], outline=WIT, width=max(1, round(1.6 * d.s)))
    d.rondje(x - r_ * .4, y - r_ * .4, max(.8, r_ * .18), max(.8, r_ * .18), WIT)


def plek(d, dd, dier, zak=0, held_x=130, held_y=186, m=44, spiegel=False):
    """Ronde 2: elke plek een eigen bodem die je meteen herkent, geen gele zandschijf met verre bollen meer."""
    X = (lambda x: 260 - x) if spiegel else (lambda x: x)
    if dier == 'ray':
        # wit rimpelzand over de hele breedte, met veel rimpels
        bodem(d, 206 + zak, WIT if not d.am else (238, 238, 228), (170, 170, 170) if not d.am else (190, 190, 180))
        rimpel = (170, 170, 85) if not d.am else (196, 186, 140)
        for i, y0 in enumerate([214, 224, 236, 250]):
            pts = [(x, y0 + zak + 2.4 * math.sin(x / 26 * 2 * math.pi + i)) for x in range(0, 261, 2)]
            d.dr.line([d.P(*q) for q in pts], fill=rimpel, width=max(1, round(2.2 * d.s)), joint='curve')
        d.rondje(X(30), 212 + zak, 6, 4, (255, 170, 170), (170, 85, 85), dikte=1.2)
    elif dier == 'manta':
        # open water, ver weg een lage zandbank (heuvel met witte rand) en daarvoor het opgerolde spandoek, groot
        d.rondje(X(196), 238 + zak, 92, 34, WIT)
        d.rondje(X(196), 240 + zak, 90, 32, ZAND if not d.am else (235, 225, 150))
        d.rondje(X(150), 230 + zak, 4, 2.6, (170, 85, 85) if not d.am else (170, 120, 80))
        d.rondje(X(238), 226 + zak, 4, 2.6, (170, 85, 85) if not d.am else (170, 120, 80))
    elif dier == 'dolphin':
        # glad bodempje (vlak, lichtgrijs-blauw met witte rand) met ronde lichtvlekken, bellenringen opzij
        bodem(d, 218 + zak, (85, 170, 170) if not d.am else (70, 150, 160), WIT, golf=1.2, n=1)
        vlek = (170, 255, 255) if not d.am else (170, 240, 235)
        for x0, y0, rx, ry in [(40, 230, 16, 4.5), (96, 246, 12, 3.6), (190, 236, 18, 5), (236, 226, 9, 3)]:
            d.rondje(X(x0), y0 + zak, rx, ry, vlek)
        for x0, y0, r_ in [(30, 196, 5), (38, 176, 3.6), (32, 160, 2.6), (232, 192, 4.4), (226, 174, 3.2)]:
            bel_ring(d, X(x0), y0 + zak, r_)
    else:   # swordfish
        # open blauw met lichtstreepjes; alleen een smalle zandstrook onderin voor het hartje
        streep = (0, 170, 255) if not d.am else (60, 160, 220)
        for x0, y0, b in [(28, 150, 30), (206, 160, 34), (40, 176, 22), (222, 184, 22)]:
            lijn(d, [(X(x0), y0 + zak), (X(x0 + b), y0 + zak)], streep, 2.4)
        bodem(d, 194 + zak, ZAND if not d.am else (235, 225, 150), WIT, golf=2.4, n=1)


def spoor(d, gx, gy, gr):
    """Landingsspoor: een brede ronde groef in het witte zand met drie putjes van de pootjes."""
    zd = (170, 170, 85) if not d.am else (170, 160, 110)
    d.rondje(gx, gy, gr, gr * .22, zd)
    d.rondje(gx, gy - .8, gr * .80, gr * .16, WIT if not d.am else (238, 238, 228))
    for dx, dy in ((-.9, 0), (0, .2), (.9, 0)):
        d.rondje(gx + dx * gr * .9, gy + dy * gr + 1, 4, 2.6, (85, 85, 85) if not d.am else (110, 100, 70))


def schaduw(d, x, y, b):
    if d.am: d.gloed_ellips(x, y, b, 4.5, (90, 80, 40), .45, groei=.25)
    else: d.rondje(x, y, b, 4, ZAND_DONKER)


def held_onder(d, dier, hx, hy, m, nacht, scherm='hold'):
    """Held met zijn grap onder water."""
    wie = WIE[dier]
    if dier == 'ray':
        # het landingsspoor: een ronde ring met drie putjes, de rog zweeft erboven met de lampjes uit
        # hij nam de vlieger mee naar beneden: touwtje hangt slap naar het zand, staart met strikjes golft achter hem
        if HELD_AAN:
            vlieger(d, hx, hy, m, 0, touw_naar=(hx - 34, 226), staart=[(.55, .30), (1.15, .25), (1.70, .05)])
    elif dier == 'manta':
        if HELD_AAN:
            manta(d, hx, hy, m, 0)
    elif dier == 'dolphin':
        schaduw(d, hx + 4, hy + m * .78, m * .9)
        if HELD_AAN:
            v3.dier_kantel(d, hx, hy, m, wie, 4); duikbril(d, hx, hy, m, 4, wie, op_voorhoofd=True, snorkel=False)
    else:
        mk = merk(wie)
        hoek = 0
        r = rot(hx, hy, m, hoek); tx, ty = r(*mk['neus'])
        if HELD_AAN:
            v3.dier_kantel(d, hx, hy, m, wie, hoek)
            dx_, dy_ = r(-.86, -.02); donut(d, dx_, dy_, 18)
        return (tx, ty)


# ---------------- schermen ----------------
def adem(D_, am, dd, nacht, dier, top=134, woord='breathe in', getal='12', onder='round 2 · 18 left', fase='in'):
    d = Doek(D_, am); v._KAP['y'] = 140
    v3.lucht(d, dd, nacht, top)
    wie = WIE[dier]; hoek = {'in': 8, 'calm': 3, 'uit': 0}[fase]
    if dier in ('dolphin', 'swordfish'):     # wolkje rechts boven, zoals bij de schildpad
        wx = 222; wk = WIT if not nacht else (85, 85, 170); wr = (170, 255, 255) if not nacht else (0, 0, 170)
        for cx, cy, rx, ry in [(wx - 8, 70, 14, 8), (wx + 4, 64, 12, 10), (wx + 14, 72, 11, 7)]: d.rondje(cx, cy, rx, ry, wr)
        for cx, cy, rx, ry in [(wx - 8, 69, 12, 6.5), (wx + 4, 63, 10, 8.5), (wx + 14, 71, 9, 5.5)]: d.rondje(cx, cy, rx, ry, wk)
    v3.zee(d, nacht, top)
    if dier != 'swordfish': v3.volgende_vriend(d, nacht, top, x=70 if dier == 'manta' else 196)
    if dier == 'ray':
        m = 38; hx = {'in': 196, 'calm': 194, 'uit': 150}[fase]
        hy = top - {'in': RAY_IN, 'calm': RAY_CALM, 'uit': 32}[fase]     # ronde 4: lager, de punt raakte de 12
        if HELD_AAN:
            vlieger(d, hx, hy, m, hoek, touw_naar=(hx - 58, top + 7), staart=[(.45, .35), (.95, .45), (1.35, .30)])
    elif dier == 'manta':
        m = 34; hx = {'in': 206, 'calm': 204, 'uit': 196}[fase]; hy = top - 22   # rechts, het doek waait achter hem naar links
        if HELD_AAN:
            mk = merk(wie); r = rot(hx, hy, m, hoek)
            sx, sy = r(mk['staart'][0], mk['staart'][1] - .05)
            bx, by = hx - 46 - 66, hy + 4
            lijn(d, [(sx, sy), (bx + 66, by + 10)], DONKER, 2.4); lijn(d, [(sx, sy), (bx + 66, by + 10)], WIT, 1.2)
            manta(d, hx, hy, m, hoek)
            spandoek(d, bx, by, 66, 20)
    elif dier == 'dolphin':
        m = 44; hx = 128 if top > 160 else 176; dy = 0 if top < 140 else -4
        hy = top + dy - 2
        if HELD_AAN:
            v3.dier_kantel(d, hx, hy, m, wie, hoek)
            duikbril(d, hx, hy, m, hoek, wie, snorkel_l=.85 if top < 140 else .95)
        zk = ((0, 85, 175) if not nacht else (0, 75, 150)) if am else ((0, 85, 170) if not nacht else (0, 0, 170))
        y0 = top + dy + 12
        pts = [(x, y0 + 1.8 * math.sin((x - hx) / 7)) for x in range(int(hx - m * 1.1), int(hx + m * 1.1) + 1, 2)]
        d.blob(pts + [(hx + m, y0 + 9), (hx - m, y0 + 9)], zk)
        d.dr.line([d.P(*q) for q in pts], fill=WIT, width=max(1, round(1.6 * d.s)))
    else:   # swordfish
        m = 42; hx = 196 if top < 160 else 170; dy = -2
        hy = top + dy - 4
        mk = merk(wie); r = rot(hx, hy, m, hoek); tx, ty = r(*mk['neus'])
        if HELD_AAN:
            v3.dier_kantel(d, hx, hy, m, wie, hoek)
            dx_, dy_ = r(-.86, -.02); donut(d, dx_, dy_, 17)
        zk = ((0, 85, 175) if not nacht else (0, 75, 150)) if am else ((0, 85, 170) if not nacht else (0, 0, 170))
        y0 = top + dy + 10
        pts = [(x, y0 + 1.8 * math.sin((x - hx) / 7)) for x in range(int(hx - m * .7), int(hx + m * 1.2) + 1, 2)]
        d.blob(pts + [(hx + m * 1.1, y0 + 9), (hx - m * .6, y0 + 9)], zk)
        d.dr.line([d.P(*q) for q in pts], fill=WIT, width=max(1, round(1.6 * d.s)))
    v3.tekst_adem(d, top, woord, getal, onder)
    return d.klaar()


# held op hold en menu (x, y, maat), plus waar de bundel valt
HOLD = {'ray': (112, 184, 46), 'manta': (130, 189, 46), 'dolphin': (140, 186, 48), 'swordfish': (150, 190, 46)}
MENU = {'ray': (110, 178, 40), 'manta': (130, 186, 42), 'dolphin': (138, 194, 42), 'swordfish': (150, 197, 40)}


def hold(D_, am, dd, nacht, dier):
    d = Doek(D_, am); v._KAP['y'] = 139
    hx, hy, m = HOLD[dier]
    v3.onder(d, dd, nacht, xo=hx - 6, xh=hx - 2)
    plek(d, dd, dier)
    if dier == 'manta':
        spandoek(d, 96, 230, 62, opgerold=True)
    held_onder(d, dier, hx, hy, m, nacht)
    stofjes(d, dd)
    d.tekst(130, 24, 'hold', 24, GEEL)
    d.tekst(130, 48, 'press START to breathe', 14, WIT, False)
    d.tekst(130, 58, '1:45', 58, WIT)
    d.tekst(130, 117, '61 bpm · round 2', 18, WIT, False)
    return d.klaar()


def menu(D_, am, dd, nacht, dier):
    d = Doek(D_, am); v._KAP['y'] = 140
    hx, hy, m = MENU[dier]
    v3.onder(d, dd, nacht, xo=hx - 8, xh=hx - 4)
    plek(d, dd, dier, zak=4)
    if dier == 'manta':
        spandoek(d, 96, 234, 62, opgerold=True)
    held_onder(d, dier, hx, hy, m, nacht, 'menu')
    stofjes(d, dd); s = d.s
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for y, t in [(52, 'Rounds'), (86, 'Calm 4-7-8')]:
        fill = ((0, 30, 60) if dd is DAG else (0, 0, 50)) if am else (0, 0, 85)
        d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=fill,
                               outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        d.tekst(130, y + 2, t, 20, WIT)
    d.tekst(130, 118, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    return d.klaar()


def eind(D_, am, dd, nacht, dier):
    """Indeling van v3.2: kop en tijden tot y 70, held links en vriend in het belletje rechts, naam van 150 tot 196."""
    v._KAP['y'] = 72
    d = Doek(D_, am); w.water_onder(d, dd, nacht, stralen=0, raster_y=146)
    v.bundel(d, dd, nacht, xo=184, xh=184, yh=136)
    plek(d, dd, dier, zak=14)
    if dier == 'manta': spandoek(d, 120, 240, 50, opgerold=True)
    stofjes(d, dd)
    for x, y, k in [(228, 76, 7), (236, 140, 5)]: fonkel(d, x, y, k)
    bx, by, brx, bry = 186, 108, 36, 32
    kring(d, dd, bx, by, 40)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 3.6, 3.6, WIT)
    d.dier(bx, by + 1, 26, N[VRIEND[dier]])
    hart = [(132 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 94 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)
    d.tekst(130, 18, '3 rounds done', 27, GEEL)
    d.tekst(130, 46, '1:20   1:45   1:58', 22, WIT)
    wie = WIE[dier]
    if HELD_AAN:
        if dier == 'ray':
            vlieger(d, 72, 104, 30, 0, touw_naar=(40, 140), staart=[(.5, .25), (1.0, .35), (1.45, .2)])
        elif dier == 'manta':
            manta(d, 66, 106, 28, 0)
            mk = merk(wie); sx, sy = 66 + mk['staart'][0] * 28, 106 + mk['staart'][1] * 28 - 1
            lijn(d, [(sx, sy), (sx + 6, sy + 10)], DONKER, 2.4); lijn(d, [(sx, sy), (sx + 6, sy + 10)], WIT, 1.2)
            spandoek(d, sx + 4, sy + 6, 40, 14)
        elif dier == 'dolphin':
            v3.dier_kantel(d, 76, 116, 32, wie, 6); duikbril(d, 76, 116, 32, 6, wie, op_voorhoofd=True, snorkel=False)
        else:
            v3.dier_kantel(d, 82, 118, 30, wie, 4)
            r = rot(82, 118, 30, 4); dx_, dy_ = r(-.86, -.02); donut(d, dx_, dy_, 12)
    d.tekst(130, 150, 'new friend', 18, WIT, False)
    naam = VRIEND[dier]
    d.tekst(130, 166, naam, 32 if len(naam) < 9 else 29, GEEL)
    stippen(d.dr, 130 * d.s, 212 * d.s, 3, 1, max(2, round(3.5 * d.s)), round(13 * d.s))
    return d.klaar()


def scherm(naam, dier):
    if naam == 'in': return lambda D_, am, dd, n: adem(D_, am, dd, n, dier)
    if naam == 'uit': return lambda D_, am, dd, n: adem(D_, am, dd, n, dier, top=170, woord='breathe out', getal='9', fase='uit')
    if naam == 'calm': return lambda D_, am, dd, n: adem(D_, am, dd, n, dier, top=146, woord='breathe out', getal='5', onder='4-7-8 · 2 of 4', fase='calm')
    return lambda D_, am, dd, n: {'hold': hold, 'menu': menu, 'eind': eind}[naam](D_, am, dd, n, dier)


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']
DIEREN = ['ray', 'manta', 'dolphin', 'swordfish']

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    for dier in sys.argv[2:] or DIEREN:
        rij = {}
        for nacht in (False, True):
            dd = NACHT if nacht else DAG
            for D_, am in ((454, True), (260, False)):
                for naam in NAMEN:
                    im = scherm(naam, dier)(D_, am, dd, nacht)
                    im.save(os.path.join(uit, f'{dier}-{naam}-{"nacht" if nacht else "dag"}-{D_}.png')); rij[(naam, nacht, D_)] = im
        for D_, k in ((454, 1), (260, 2)):
            g = 12 * k; W = D_ * k; n = len(NAMEN)
            ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
            for j, nacht in enumerate((False, True)):
                for i, naam in enumerate(NAMEN):
                    ov.paste(rij[(naam, nacht, D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
            ov.save(os.path.join(uit, f'overzicht-{dier}-{D_}-{k}x.png'))
