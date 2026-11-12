# Blad werelden v3 (Mila, run 47, 12 nov): schildpad en clownvis in de opzet van de krab v2.2 (besluit hoofdchat 12 nov 03:10 NL),
# met de punten uit keuring 13 en de echte beelden van Gijs (run 51):
#  - boven water maar twee golfrijen onder de kam (Gijs: vier rijen is ±240 punten per beurt, te veel)
#  - AMOLED-lucht overdag bovenin donkerder, fel blauw alleen als band boven de horizon
#  - geen baan van licht onder de zon, alleen losse vonkjes zonder vlak (Gijs: de trapezium was hard)
#  - een eigen detail onderin het water op de ademschermen (schaduw van de volgende vriend)
#  - de held kantelt mee met de adem (neus omhoog bij inademen, plat bij uitademen)
#  - "press START to breathe" blijft altijd staan tijdens inhouden; bpm-regel een maat groter
# Per dier een eigen plek en een eigen grap:
#  - schildpad: zeegrasweide met ruimte; boven water is hij een eiland en er LIFT EEN MEEUW MEE op zijn schild;
#    onder water graast hij, er hangt een spriet met een hap eruit voor zijn bek
#  - clownvis: rif met zijn anemoon als huis; boven water SPRINGT hij uit de golf en JONGLEERT drie belletjes (hij is een clown);
#    onder water jongleert hij door vanuit zijn anemoon
# Coordinaten in 1/260 D.   python3 werelden_v3.py <uitmap>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL, ZON, ROZE, PAARS, ZAND, ZAND_DONKER, D, bellen, fonkel, stofjes, kring
from blad_v9 import stippen
from blad_v13 import kader
import horloge_sim as h
from PIL import Image, ImageDraw, ImageChops

SCHILD, CLOWN, KWAL, PAARD = D[3], D[7], D[2], D[5]
GRAS, GRAS_L, GRAS_D = (0, 170, 85), (85, 255, 85), (0, 85, 0)
RIF, RIF_L = (85, 0, 170), (170, 85, 255)
ORANJE = (255, 170, 0)


# ---------------- hulpjes ----------------
def dier_kantel(d, cx, cy, maat, wie, hoek):
    """Het dier zoals in de app (niet aangepast), alleen als geheel gekanteld. hoek in graden, + = neus omhoog (dier kijkt naar links)."""
    m = round(maat * d.D / 260)
    _, _, ox, oy = kader(wie, m)
    lag = Image.new('RGB', (d.D, d.D), (1, 2, 3)); ld = ImageDraw.Draw(lag)
    h.teken(ld, wie, round(cx * d.D / 260 - ox), round(cy * d.D / 260 - oy), m)
    mk = ImageChops.difference(lag, Image.new('RGB', (d.D, d.D), (1, 2, 3))).convert('L').point(lambda v: 255 if v else 0)
    if hoek:
        c = (cx * d.D / 260, cy * d.D / 260)
        lag = lag.rotate(-hoek, Image.NEAREST, center=c); mk = mk.rotate(-hoek, Image.NEAREST, center=c)
    lag = lag.resize((d.N, d.N), Image.NEAREST); mk = mk.resize((d.N, d.N), Image.NEAREST)
    d.im.paste(lag, (0, 0), mk)


def lucht(d, dd, nacht, top):
    """AMOLED overdag: bovenin donker, fel blauw alleen als band boven de horizon (keuring 13 punt 4)."""
    if d.am and not nacht:
        d.verloop(0, top * .55, (0, 30, 95), (0, 75, 165)); d.verloop(top * .55, top, (0, 75, 165), (0, 165, 250))
    else:
        d.verloop(0, top, dd['lucht'][0], dd['lucht'][1], [(top - 28, dd['lucht'][1] if not nacht else (0, 0, 85))])
    if nacht:
        for x, y in [(56, 50), (204, 44), (222, 82), (34, 100), (184, 24), (96, 20), (238, 110)]:
            d.rondje(x, y, .9, .9, WIT)
        d.rondje(40, 84, 13, 13, (255, 255, 170), (170, 170, 255), dikte=1.6)
        d.rondje(47, 82, 11, 12, dd['lucht'][1] if not d.am else (0, 25, 120))
    else:
        if d.am: d.gloed_ellips(40, 86, 20, 20, (255, 255, 170), .35)
        d.rondje(40, 86, 14, 14, ZON, WIT, glans=WIT, dikte=2)


def zee(d, nacht, top):
    """Kam met schuim en maar twee golfrijen eronder (Gijs: ±120 punten per beurt past)."""
    am_k = [(0, 85, 175), (0, 55, 140), (0, 30, 100)] if not nacht else [(0, 75, 150), (0, 45, 115), (0, 15, 75)]
    mip_k = [(0, 85, 170), (0, 0, 170), (0, 0, 85)] if not nacht else [(0, 0, 170), (0, 0, 85), (0, 0, 85)]
    d.golf(top - 3, 262, WIT, 4, 2, 1.2)
    for k, (y, a, n, fa) in enumerate([(top, 4, 2, 1.2), (top + 34, 3, 4, .3), (top + 66, 3.5, 3, 2.0)]):
        if k: d.golf(y - 1.6, 262, (85, 170, 255) if not nacht else (85, 85, 255), a, n, fa)
        d.golf(y, 262, am_k[k] if d.am else mip_k[k], a, n, fa)
    # vonkjes op het water onder zon of maan: losse puntjes, geen vlak (Gijs run 51 punt 5)
    for x, y, k in [(34, top + 9, 3.2), (48, top + 17, 2.4), (30, top + 26, 1.8)]:
        if y < 238: fonkel(d, x, y, k) if not nacht else d.rondje(x, y, k * .45, k * .45, (255, 255, 170))


def volgende_vriend(d, nacht, top, x=196):
    """Eigen detail onderin het water: de schaduw van de volgende vriend (een vis), een vaste donkere tint."""
    y = top + 84
    if y > 234: return
    c = (0, 20, 70) if (d.am and not nacht) else ((0, 5, 45) if d.am else (0, 0, 85 if not nacht else 0))
    d.rondje(x, y, 13, 6, c)
    d.blob([(x + 11, y), (x + 21, y - 6), (x + 19, y), (x + 21, y + 6)], c)


def tekst_adem(d, top, woord, getal, onder):
    d.tekst(130, 14 if top < 140 else 22, woord, 25, WIT)
    d.tekst(130, 32 if top < 140 else 42, getal, 56, WIT)
    d.tekst(130, top + 40, onder, 16, WIT, False)


def meeuw(d, x, y, k=1.0, nacht=False):
    """Een meeuw die staat (op het schild). Kijkt naar rechts: de andere kant op dan de schildpad, dat is de grap."""
    lijf = WIT      # ook bij nacht wit, anders verdwijnt hij tegen de lucht (keuring 14)
    d.dr.line([d.P(x - 2 * k, y + 3 * k), d.P(x - 2.6 * k, y + 8 * k)], fill=ORANJE, width=max(1, round(1.5 * k * d.s)))
    d.dr.line([d.P(x + 2 * k, y + 3 * k), d.P(x + 2.6 * k, y + 8 * k)], fill=ORANJE, width=max(1, round(1.5 * k * d.s)))
    d.blob([(x - 10 * k, y - 1 * k), (x - 4 * k, y - 4.5 * k), (x + 5 * k, y - 4 * k), (x + 7 * k, y + 1 * k), (x + 1 * k, y + 4.5 * k), (x - 6 * k, y + 3 * k)], lijf, (0, 0, 85), 1.2)
    d.blob([(x - 9 * k, y - 1.4 * k), (x - 3 * k, y - 3 * k), (x + 3 * k, y - 1 * k), (x - 4 * k, y + 1.2 * k)], (170, 170, 170))   # vleugel
    d.rondje(x + 6 * k, y - 6 * k, 3.6 * k, 3.4 * k, lijf, (0, 0, 85), dikte=1.1)
    d.blob([(x + 9 * k, y - 7 * k), (x + 14 * k, y - 5.6 * k), (x + 9 * k, y - 4.6 * k)], ORANJE)    # snavel
    d.rondje(x + 7 * k, y - 6.6 * k, .9 * k, .9 * k, (0, 0, 0))


def jongleer(d, cx, cy, r_, k=1.0, nacht=False):
    """Drie belletjes in een boog boven de clownvis, met een stippellijn van de worp: hij jongleert."""
    for i in range(9):
        a = math.pi * (1.05 + i * .9 / 8)
        d.rondje(cx + r_ * math.cos(a) * 1.15, cy + r_ * math.sin(a), .8 * k, .8 * k, (170, 255, 255))
    for t, c in ((.12, (255, 255, 0)), (.5, (255, 85, 170)), (.88, (85, 255, 85))):     # drie felle ballen: jongleren, geen luchtbellen
        a = math.pi * (1.0 + t)
        x, y = cx + r_ * math.cos(a) * 1.15, cy + r_ * math.sin(a)
        d.rondje(x, y, 4.4 * k, 4.4 * k, c, WIT, glans=WIT, dikte=1.5)


def spat(d, x, y, k=1.0):
    """Spatwater waar de clownvis uit de golf springt: een kroontje van druppels."""
    for dx, dy, r_ in [(-16, -6, 2.4), (-10, -14, 2.2), (-2, -19, 2.4), (8, -16, 2), (16, -8, 2.4), (21, -2, 1.8)]:
        d.rondje(x + dx * k, y + dy * k, r_ * k, r_ * k, WIT, (0, 85, 170), dikte=.9)
    for i in range(7):        # spatkroon: puntjes omhoog vanuit de golf
        a = math.pi * (1.1 + i * .8 / 6); x0, y0 = x + 2 * k + 14 * k * math.cos(a) * 1.2, y + 2 * k
        d.blob([(x0 - 2 * k, y0), (x0 + 6 * k * math.cos(a) * .6, y0 - 7 * k), (x0 + 2 * k, y0)], WIT)


# ---------------- boven water ----------------
def adem(D_, am, dd, nacht, wereld, top=134, woord='breathe in', getal='12', onder='round 2 · 18 left', fase='in'):
    d = Doek(D_, am)
    lucht(d, dd, nacht, top)
    # wolkje links laag bij de clownvis (rechts boven is zijn jongleerboog), anders rechts
    wx = 60 if wereld == 'clown' else 222
    wk = (255, 255, 255) if not nacht else (85, 85, 170); wr = (170, 255, 255) if not nacht else (0, 0, 170)
    if not (wereld == 'clown'):
        for cx, cy, rx, ry in [(wx - 8, 70, 14, 8), (wx + 4, 64, 12, 10), (wx + 14, 72, 11, 7)]: d.rondje(cx, cy, rx, ry, wr)
        for cx, cy, rx, ry in [(wx - 8, 69, 12, 6.5), (wx + 4, 63, 10, 8.5), (wx + 14, 71, 9, 5.5)]: d.rondje(cx, cy, rx, ry, wk)
    zee(d, nacht, top)
    volgende_vriend(d, nacht, top)
    hoek = {'in': 8, 'calm': 3, 'uit': 0}[fase]          # held kantelt mee: neus omhoog bij inademen
    if wereld == 'schild':
        hx = 128 if top > 160 else 166; dy = 0 if top < 140 else -4
        m = 44
        # schildpad als eilandje: hij ligt in de golf, kop en schild boven, onderkant in het water
        dier_kantel(d, hx, top + dy - 4, m, SCHILD, hoek)
        # golfje voor zijn buik: hij drijft IN het water, niet erop
        zk = ((0, 85, 175) if not nacht else (0, 75, 150)) if am else ((0, 85, 170) if not nacht else (0, 0, 170))
        y0 = top + dy + 10
        pts = [(x, y0 + 1.8 * math.sin((x - hx) / 7)) for x in range(int(hx - m * 1.0), int(hx + m * 1.0) + 1, 2)]
        d.blob(pts + [(hx + m * .9, y0 + 7), (hx - m * .9, y0 + 7)], zk)          # golfje voor zijn buik: hij drijft IN het water
        d.dr.line([d.P(*q) for q in pts], fill=WIT, width=max(1, round(1.6 * d.s)))
        # de meeuw liftet mee boven op het schild (schildtop op +0,13 m, -0,58 m; gekanteld)
        a = math.radians(hoek); sx, sy = .16 * m, -.6 * m
        mx, my = hx + sx * math.cos(a) + sy * math.sin(a), top + dy - 4 - sx * math.sin(a) + sy * math.cos(a)
        meeuw(d, mx, my - 11, 1.4, nacht)
    elif wereld == 'clown':
        hx = 188 if top < 160 else 176
        sprong = {'in': 26, 'calm': 18, 'uit': 12}[fase]         # bij inademen springt hij het hoogst
        spat(d, hx + 6, top - 1, 1.0 if fase == 'in' else .8)
        dier_kantel(d, hx, top - sprong, 32, CLOWN, hoek + 10)
        jongleer(d, hx + 2, top - sprong - 16, 24, 1.0, nacht)
    tekst_adem(d, top, woord, getal, onder)
    return d.klaar()


# ---------------- onder water ----------------
def spriet(d, x0, y0, lengte, buig, breed, c, rand, hap=False):
    """Zeegrasspriet: smalle gebogen strook, ronde top. hap = er is een hap uit (de schildpad eet zeegras)."""
    n = 12; links, rechts = [], []
    for i in range(n + 1):
        t = i / n; x = x0 + buig * t * t; y = y0 - lengte * t; b = breed * (1 - .35 * t)
        links.append((x - b / 2, y)); rechts.append((x + b / 2, y))
    pts = links + list(reversed(rechts))
    d.blob(pts, c, rand, 1.3)
    if hap:   # halve maan uit de rand, in de kleur van het water erachter: zet hij er pas overheen
        t = .62; x = x0 + buig * t * t; y = y0 - lengte * t
        return (x + breed * .5, y)
    return None


def wereld_schild(d, dd, hx=124, hy=186, m=40, spiegel=False, held=True, zak=0):
    """Zeegrasweide: lichte zandvlakte met ruimte in het midden, hoge sprieten aan beide randen, laag gras vooraan."""
    s = d.s
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in [(60, 196, 90, 18), (210, 192, 80, 22)]:
        d.rondje(cx, cy + zak, rx, ry, verder)
    d.dr.ellipse([-60 * s, (206 + zak) * s, 320 * s, 340 * s], fill=ZAND_DONKER)
    d.dr.ellipse([-50 * s, (210 + zak) * s, 310 * s, 340 * s], fill=ZAND if not d.am else (235, 225, 150))
    if d.am: d.gloed_ellips(hx, 230 + zak, 52, 10, WIT, .4)
    X = (lambda x: 260 - x) if spiegel else (lambda x: x)
    g, gl, gd = GRAS, GRAS_L, GRAS_D
    # hoge sprieten links (achter) en rechts
    for x0, L, b in [(14, 86, 8), (28, 104, 9), (42, 74, 8), (56, 54, 7)]:
        spriet(d, X(x0), 222 + zak, L, (10 if x0 % 3 else -8) * (-1 if spiegel else 1), b, gd if x0 < 30 else g, gl)
    for x0, L, b in [(204, 60, 7), (218, 92, 9), (234, 78, 8), (248, 98, 8)]:
        spriet(d, X(x0), 224 + zak, L, (-12 if x0 % 4 else 9) * (-1 if spiegel else 1), b, g if x0 > 210 else gd, gl)
    # een zeeschelp en een steentje op het zand: de weide is een plek, geen behang
    d.rondje(X(176), 236 + zak, 6, 4, (255, 170, 170), WIT, dikte=1.2)
    d.rondje(X(86), 240 + zak, 5, 3, (170, 170, 255), WIT, dikte=1.2)
    if held:
        # schaduw, dan de schildpad, dan de spriet met de hap voor zijn bek (hij graast)
        if d.am: d.gloed_ellips(hx + 4, hy + m * .72, m * .95, 4.5, (90, 80, 40), .45, groei=.25)
        else: d.rondje(hx + 4, hy + m * .72, m * .9, 4, ZAND_DONKER)
        # de spriet waar hij van eet: komt uit het zand en eindigt IN zijn bek (achter de kop getekend), met twee kruimels
        sg = 1      # het dier kijkt altijd naar links, ook als de weide gespiegeld is
        bek_x, bek_y = hx - .80 * m * sg, hy + .04 * m
        voet_x = bek_x - 14 * sg
        spriet(d, voet_x, hy + m * .78, (hy + m * .78) - bek_y, (bek_x - voet_x) + 2 * sg, 7, GRAS_L, WIT)
        dier_kantel(d, hx, hy, m, SCHILD, 0)
        for dx, dy, r_ in [(-9, -6, 2.0), (-14, 2, 1.5)]:
            d.blob([(bek_x + dx * sg - r_, bek_y + dy), (bek_x + dx * sg, bek_y + dy - r_ * 1.4), (bek_x + dx * sg + r_, bek_y + dy), (bek_x + dx * sg, bek_y + dy + r_ * .8)], GRAS_L, WIT, .9)


def wereld_clown(d, dd, hx=150, hy=178, m=34, held=True, zak=0, jong=True, nacht=False, adx=0):
    """Rif: donkerpaarse koraalbult rechts met de grote anemoon (zijn huis), paarse waaier en geel takje links."""
    s = d.s
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in [(30, 190, 56, 30), (130, 200, 70, 16), (236, 180, 50, 36)]:
        d.rondje(cx, cy + zak, rx, ry, verder)
    d.dr.ellipse([-40 * s, (226 + zak) * s, 300 * s, 340 * s], fill=ZAND_DONKER)
    d.dr.ellipse([-30 * s, (230 + zak) * s, 290 * s, 340 * s], fill=ZAND if not d.am else (235, 225, 150))
    if d.am: d.gloed_ellips(hx - 6, 236 + zak, 46, 9, WIT, .4)
    # links: paarse waaier (lijnen vanuit een voet) en een geel takje
    vx, vy = 34, 214 + zak
    for i in range(7):
        a = math.radians(-150 + i * 20); L = 40 + 6 * math.sin(i * 1.7)
        d.dr.line([d.P(vx, vy), d.P(vx + L * math.cos(a), vy + L * math.sin(a))], fill=RIF_L, width=max(2, round(3.4 * s)))
    d.dr.line([d.P(vx - 34, vy - 26), d.P(vx - 4, vy - 46), d.P(vx + 30, vy - 30)], fill=RIF_L, width=max(2, round(2.4 * s)), joint='curve')
    d.rondje(vx, vy + 6, 24, 12, RIF, RIF_L, glans=RIF_L)
    for (x0, y0), (x1, y1) in [((70, 230), (70, 204)), ((70, 214), (60, 200)), ((70, 218), (82, 202)), ((82, 202), (88, 194))]:
        d.dr.line([d.P(x0, y0 + zak), d.P(x1, y1 + zak)], fill=WIT, width=round(6.4 * s))
    for (x0, y0), (x1, y1) in [((70, 230), (70, 204)), ((70, 214), (60, 200)), ((70, 218), (82, 202)), ((82, 202), (88, 194))]:
        d.dr.line([d.P(x0, y0 + zak), d.P(x1, y1 + zak)], fill=ZON, width=round(4 * s))
        d.rondje(x1, y1 + zak, 2.4, 2.4, ZON)
    # rechts: rifbult met de anemoon als huis; de vis zit erin, twee vingers liggen voor hem
    d.rondje(214 + adx, 222 + zak, 52, 30, RIF, RIF_L, glans=RIF_L)
    vingers = [(-34, -34), (-24, -46), (-12, -54), (0, -58), (12, -54), (24, -46), (34, -34), (40, -20)]
    ax, ay = 206 + adx, 200 + zak
    def vinger(i, vx_, vy_, c_rand=True):
        x1, y1 = ax + vx_, ay + vy_
        if c_rand:
            d.dr.line([d.P(ax + vx_ * .3, ay), d.P(x1, y1)], fill=WIT, width=round(9 * s)); d.rondje(x1, y1, 4.5, 4.5, WIT)
        else:
            d.dr.line([d.P(ax + vx_ * .3, ay), d.P(x1, y1)], fill=(255, 85, 170), width=round(6 * s)); d.rondje(x1, y1, 3.8, 3.8, (255, 170, 255))
    for i, (a, b) in enumerate(vingers): vinger(i, a, b)
    for i, (a, b) in enumerate(vingers): vinger(i, a, b, False)
    d.rondje(ax, ay, 30, 9, (255, 85, 170), WIT, dikte=1.6)
    if held:
        dier_kantel(d, hx, hy, m, CLOWN, 0)
        # twee vingers vooraan liggen over zijn staart: hij woont erin (oog en banden blijven vrij)
        for a, b in [(-40, -4), (-30, -16)]:
            x0, y0, x1, y1 = ax - 10, ay + 4, ax + a, ay + b
            d.dr.line([d.P(x0, y0), d.P(x1, y1)], fill=WIT, width=round(9 * s)); d.rondje(x1, y1, 4.5, 4.5, WIT)
            d.dr.line([d.P(x0, y0), d.P(x1, y1)], fill=(255, 85, 170), width=round(6 * s)); d.rondje(x1, y1, 3.8, 3.8, (255, 170, 255))
        if jong:
            jongleer(d, hx - m * .55, hy - m * .55, m * .7, .9, nacht)


def onder(d, dd, nacht, raster_y=None, stralen=3, xo=118, xh=112, yh=236):
    w.water_onder(d, dd, nacht, stralen=0, raster_y=raster_y)
    if stralen: w.bundel(d, dd, nacht, xo=xo, xh=xh, yh=yh)


def hold(D_, am, dd, nacht, wereld):
    d = Doek(D_, am)
    if wereld == 'schild':
        onder(d, dd, nacht, xo=126, xh=128); wereld_schild(d, dd, hx=136, hy=182, m=46)
    else:
        onder(d, dd, nacht, xo=150, xh=152); wereld_clown(d, dd, hx=150, hy=184, m=33, nacht=nacht)
    stofjes(d, dd)
    d.tekst(130, 24, 'hold', 24, GEEL)
    d.tekst(130, 48, 'press START to breathe', 14, WIT, False)     # blijft altijd staan (veiligheid, besluit 12 nov 03:10)
    d.tekst(130, 58, '1:45', 58, WIT)
    d.tekst(130, 117, '61 bpm · round 2', 18, WIT, False)          # een maat groter (keuring 13)
    return d.klaar()


def menu(D_, am, dd, nacht, wereld):
    d = Doek(D_, am)
    if wereld == 'schild':
        onder(d, dd, nacht, xo=120, xh=124); wereld_schild(d, dd, hx=132, hy=188, m=42, spiegel=True, zak=4)
    else:
        onder(d, dd, nacht, xo=142, xh=144); wereld_clown(d, dd, hx=142, hy=188, m=30, zak=4, nacht=nacht)
    stofjes(d, dd); s = d.s
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for y, t in [(52, 'Rounds'), (86, 'Calm 4-7-8')]:
        fill = ((0, 30, 60) if dd is DAG else (0, 0, 50)) if am else (0, 0, 85)
        d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=fill,
                               outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        d.tekst(130, y + 2, t, 20, WIT)
    d.tekst(130, 118, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    return d.klaar()


def eind(D_, am, dd, nacht, wereld):
    """Eindscherm: de held links in zijn plek, de nieuwe vriend in een belletje rechts (zoals bij de krab)."""
    d = Doek(D_, am); w.water_onder(d, dd, nacht, stralen=0, raster_y=146)
    w.bundel(d, dd, nacht, xo=184, xh=186, yh=164)
    if wereld == 'schild':
        wereld_schild(d, dd, held=False, zak=10); vriend, naam = KWAL, 'Jellyfish'
    else:
        wereld_clown(d, dd, held=False, zak=30, adx=26); vriend, naam = PAARD, 'Seahorse'
    stofjes(d, dd)
    for x, y, k in [(226, 82, 8), (146, 86, 5), (236, 146, 5)]: fonkel(d, x, y, k)
    bx, by, brx, bry = 184, 122, 40, 35
    kring(d, dd, bx, by, 44)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 4, 4, WIT)
    d.dier(bx, by + 1, 28 if vriend is PAARD else 30, vriend)
    hart = [(128 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 104 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)
    d.tekst(130, 30, '3 rounds done', 25, GEEL)
    d.tekst(130, 56, '1:20   1:45   1:58', 19, WIT)
    if wereld == 'schild':
        dier_kantel(d, 76, 134, 36, SCHILD, 6)
    else:
        dier_kantel(d, 74, 128, 29, CLOWN, 0)
        jongleer(d, 62, 116, 20, .8, nacht)
    d.tekst(130, 163, 'new friend', 15, WIT, False)
    d.tekst(130, 171, naam, 30 if len(naam) < 9 else 27, GEEL)
    stippen(d.dr, 130 * d.s, 209 * d.s, 3, 1, max(2, round(3.5 * d.s)), round(13 * d.s))
    return d.klaar()


def scherm(naam, wereld):
    if naam == 'in': return lambda D_, am, dd, n: adem(D_, am, dd, n, wereld)
    if naam == 'uit': return lambda D_, am, dd, n: adem(D_, am, dd, n, wereld, top=170, woord='breathe out', getal='9', fase='uit')
    if naam == 'calm': return lambda D_, am, dd, n: adem(D_, am, dd, n, wereld, top=146, woord='breathe out', getal='5', onder='4-7-8 · 2 of 4', fase='calm')
    return lambda D_, am, dd, n: {'hold': hold, 'menu': menu, 'eind': eind}[naam](D_, am, dd, n, wereld)


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    welke = sys.argv[2:] or ['schild', 'clown']
    for wereld in welke:
        rij = {}
        for nacht in (False, True):
            dd = NACHT if nacht else DAG
            for D_, am in ((454, True), (260, False)):
                for naam in NAMEN:
                    im = scherm(naam, wereld)(D_, am, dd, nacht)
                    im.save(os.path.join(uit, f'{wereld}-{naam}-{"nacht" if nacht else "dag"}-{D_}.png')); rij[(naam, nacht, D_)] = im
        for D_, k in ((454, 1), (260, 2), (260, 1)):
            g = 12 * k; W = D_ * k; n = len(NAMEN)
            ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
            for j, nacht in enumerate((False, True)):
                for i, naam in enumerate(NAMEN):
                    ov.paste(rij[(naam, nacht, D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
            ov.save(os.path.join(uit, f'overzicht-{wereld}-{D_}-{k}x.png'))
