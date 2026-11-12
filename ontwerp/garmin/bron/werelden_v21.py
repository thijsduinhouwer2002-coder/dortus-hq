# Blad werelden v2.1 (Mila, run 45, 12 nov): punten hoofdchat 02:30 NL en keuring 8. Bouwbaar: geen vervaging,
# licht en gloed als 3 tinten per vlak; slipper 70 procent; held binnen de cirkel; MIP drie banden; uitademen en Calm erbij.
# (Basis: werelden_v2.py) Blad werelden v2 (Mila, run 43, 12 nov): nieuwe richting van de hoofdchat (12 nov 01:45 NL), eerst alleen de krab.
# Twee beelden in plaats van een doorsnede:
#   boven water = ademen (lucht per dagdeel, zon of maan, grote zee, geen bodem; de krab dobbert in zijn slipper als bootje)
#   onder water = inhouden, menu, eindscherm (heel scherm water, licht van boven, wereld met diepte onderin en opzij, held groot)
# Een stijl: alles rond en zacht met dezelfde lichte rand en een glansvlek als de dieren. Weinig en groot (vier dingen).
# 454 = AMOLED: zachte verlopen en randen zonder trapjes. 260 = MIP: dezelfde compositie in vlakken uit de 64 kleuren.
# Coordinaten in 1/260 D.   python3 werelden_v2.py <uitmap>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from blad_v9 import rond, tekst, f, FM, FS, D, stippen
from blad_v13 import kader
from PIL import Image, ImageDraw, ImageFilter

KRAB = D[4]
SLIP = .8      # slipper 70 procent van v2: de krab blijft de held
WIT, GEEL = (255, 255, 255), (255, 255, 170)
DAG = dict(lucht=[(0, 85, 170), (0, 170, 255)], zee_top=(0, 105, 140), zee_bodem=(0, 22, 60), licht=(85, 255, 255),
           ver=(0, 30, 70), mip_water=[(0, 85, 85), (0, 0, 85)], mip_boven=(0, 85, 170), mip_licht=(0, 85, 255), mip_zee=(0, 85, 170), mip_ver=(0, 0, 85), mip_verder=(0, 85, 170), mip_bundel=(0, 85, 170))
NACHT = dict(lucht=[(0, 0, 85), (0, 0, 170)], zee_top=(0, 0, 105), zee_bodem=(0, 0, 22), licht=(170, 170, 255),
             ver=(0, 0, 60), mip_water=[(0, 0, 85), (0, 0, 0)], mip_licht=(0, 0, 170), mip_zee=(0, 0, 170), mip_ver=(0, 0, 170), mip_verder=(0, 0, 85), mip_bundel=(0, 0, 170))
ROTS, ROTS_R, ROTS_DONKER = (85, 85, 170), (170, 170, 255), (0, 0, 85)
ZAND, ZAND_DONKER = (255, 255, 170), (170, 170, 85)
ROZE, PAARS, ZON = (255, 85, 170), (170, 85, 255), (255, 255, 85)


class Doek:
    """Tekent in 1/260-maat. AMOLED: 4x groot en verkleind (zacht). MIP: 1x, harde randen, alleen MIP-kleuren."""
    def __init__(self, D_, amoled):
        self.D, self.am = D_, amoled
        self.k = 4 if amoled else 1
        self.N = D_ * self.k; self.s = self.N / 260
        self.im = Image.new('RGB', (self.N, self.N)); self.dr = ImageDraw.Draw(self.im)

    def P(self, x, y): return (x * self.s, y * self.s)

    def verloop(self, y0, y1, c0, c1, banden=None):
        """Verloop van c0 (y0) naar c1 (y1). Op MIP: harde banden met een golvende rand."""
        if self.am:
            for Y in range(int(y0 * self.s), int(y1 * self.s) + 1):
                t = min(1, max(0, (Y / self.s - y0) / max(1, y1 - y0)))
                self.dr.line([(0, Y), (self.N, Y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(c0, c1)))
        else:
            self.dr.rectangle([0, y0 * self.s, self.N, y1 * self.s], fill=c0)
            if banden:
                for yb, c in banden: self.golf(yb, y1, c, 2.5, 2)

    def golf(self, y, y_onder, c, a=3, n=3, fase=0.0):
        pts = [self.P(x, y + a * math.sin(x / 260 * 2 * math.pi * n + fase)) for x in range(0, 261, 2)]
        self.dr.polygon(pts + [self.P(260, y_onder), self.P(0, y_onder)], fill=c)

    def rondje(self, cx, cy, rx, ry, c, rand=None, glans=None, dikte=2.2):
        if rand:
            self.dr.ellipse([(cx - rx - dikte) * self.s, (cy - ry - dikte) * self.s,
                             (cx + rx + dikte) * self.s, (cy + ry + dikte) * self.s], fill=rand)
        self.dr.ellipse([(cx - rx) * self.s, (cy - ry) * self.s, (cx + rx) * self.s, (cy + ry) * self.s], fill=c)
        if glans:
            self.dr.ellipse([(cx - rx * .62 - rx * .22) * self.s, (cy - ry * .55 - ry * .16) * self.s,
                             (cx - rx * .62 + rx * .22) * self.s, (cy - ry * .55 + ry * .16) * self.s], fill=glans)

    def blob(self, pts, c, rand=None, dikte=2.2):
        """Zachte veelhoek: rand eerst (iets groter), dan het vlak."""
        if rand:
            mx = sum(p[0] for p in pts) / len(pts); my = sum(p[1] for p in pts) / len(pts)
            gr = [(x + (x - mx) / max(1, math.hypot(x - mx, y - my)) * dikte, y + (y - my) / max(1, math.hypot(x - mx, y - my)) * dikte) for x, y in pts]
            self.dr.polygon([self.P(*p) for p in gr], fill=rand)
        self.dr.polygon([self.P(*p) for p in pts], fill=c)

    def stralen(self, kleur, achter, n_vak):
        """Lichtstralen van het oppervlak. AMOLED: doorzichtig en zacht. MIP: smalle wiggen in een kleur."""
        wiggen = [((70, 0), (96, 0), (60, 150), (34, 150)), ((150, 0), (166, 0), (176, 120), (154, 120)),
                  ((196, 0), (214, 0), (248, 140), (226, 140))][:n_vak]
        if self.am:
            laag = Image.new('L', (self.N, self.N), 0); ld = ImageDraw.Draw(laag)
            for w in wiggen: ld.polygon([self.P(*p) for p in w], fill=70)
            laag = laag.filter(ImageFilter.GaussianBlur(6 * self.s))
            # straal vervaagt naar beneden
            vaag = Image.linear_gradient('L').resize((self.N, self.N)).point(lambda v: 255 - v)
            from PIL import ImageChops
            laag = ImageChops.multiply(laag, vaag)
            self.im.paste(Image.new('RGB', (self.N, self.N), kleur), (0, 0), laag)
        else:
            for w in wiggen[:2]:
                mx = (w[2][0] + w[3][0]) / 2
                self.dr.polygon([self.P(*w[0]), self.P(*w[1]), self.P(w[1][0] * .55 + mx * .45, 62)], fill=kleur)

    def tint(self, vorm, kleur, alfa):
        """Een vlak in een vaste mengtint (alfa 0..1 over wat er ligt). Bouwbaar: Gijs tekent dit als een vlak met een vaste kleur."""
        laag = Image.new('L', (self.N, self.N), 0); vorm(ImageDraw.Draw(laag))
        laag = laag.point(lambda v: round(alfa * 255) if v else 0)
        self.im.paste(Image.new('RGB', (self.N, self.N), kleur), (0, 0), laag)

    def gloed_ellips(self, cx, cy, rx, ry, kleur, totaal, stappen=3, groei=.35):
        """Zachte gloed zonder vervaging: 3 ellipsen, buiten groot en zwak, binnen klein; samen 'totaal'."""
        a = 1 - (1 - totaal) ** (1 / stappen)
        for i in range(stappen):
            k = 1 + groei * (stappen - 1 - i) / max(1, stappen - 1)
            self.tint(lambda ld: ld.ellipse([(cx - rx * k) * self.s, (cy - ry * k) * self.s, (cx + rx * k) * self.s, (cy + ry * k) * self.s], fill=255), kleur, a)

    def tekst(self, x, y, s, maat, c, dik=True):
        tekst(self.dr, x * self.s, y * self.s, s, f(FS if dik else FM, round(maat * self.s)), c)

    def dier(self, cx, cy, maat260, wie=None):
        wie = KRAB if wie is None else wie
        m = round(maat260 * self.D / 260)
        lag = Image.new('RGB', (self.D, self.D)); ld = ImageDraw.Draw(lag)
        _, _, ox, oy = kader(wie, m)
        lag = Image.new('RGB', (self.D, self.D), (1, 2, 3)); ld = ImageDraw.Draw(lag)
        h.teken(ld, wie, round(cx * self.D / 260 - ox), round(cy * self.D / 260 - oy), m)
        from PIL import ImageChops
        mk = ImageChops.difference(lag, Image.new('RGB', (self.D, self.D), (1, 2, 3))).convert('L').point(lambda v: 255 if v else 0)
        lag = lag.resize((self.N, self.N), Image.NEAREST); mk = mk.resize((self.N, self.N), Image.NEAREST)
        self.im.paste(lag, (0, 0), mk)

    def klaar(self):
        im = self.im.resize((self.D, self.D), Image.LANCZOS) if self.am else self.im
        if self.am:   # zacht donkerder naar de rand: de ronde kast voelt als een raampje in de zee
            # bouwbaar: drie ringen met een vaste tint (geen vervaging)
            v = Image.new('L', (self.D, self.D), 255); vd = ImageDraw.Draw(v)
            for k, a in [(0, 200), (.03, 225), (.06, 255)]:
                vd.ellipse([self.D * k, self.D * k, self.D * (1 - k), self.D * (1 - k)], fill=a)
            im = Image.composite(im, Image.new('RGB', im.size, (0, 0, 20)), v)
        return rond(im)


# ---------------- de krab en zijn wereld ----------------
def slipper(d, cx, cy, sch=1.0, hoek=-8):
    """Grote roze teenslipper (de haak), schuin van boven: hak (waar de krab zit) op cx, smalle taille, brede neus rechts.
    Witte rand en glans zoals de dieren. Lokale maat: hak op x 0, neus op x 62, platgedrukt (perspectief)."""
    def r(x, y):
        a = math.radians(hoek); return (cx + (x * math.cos(a) - y * math.sin(a)) * sch, cy + (x * math.sin(a) + y * math.cos(a)) * sch)
    def w(x):    # halve breedte langs de zool: hak rond, taille smal, neus breed en rond
        hak = math.sqrt(max(0, 13 ** 2 - x ** 2)) if x < 0 else 13 - 4.2 * min(1, x / 26)
        neus = math.sqrt(max(0, 15 ** 2 - (x - 50) ** 2)) if x > 50 else 8.8 + 6.2 * min(1, max(0, (x - 26) / 24))
        return hak if x < 26 else neus
    xs = [-13 + i * 78 / 40 for i in range(41)]
    boven = [r(x, -w(x) * .8) for x in xs]; onder = [r(x, w(x) * .8) for x in reversed(xs)]
    d.blob([(x + .8 * sch, y + 3.2 * sch) for x, y in boven + onder], (170, 0, 85), WIT, 2.2)   # dikke zool: donkerroze rand eronder
    d.blob(boven + onder, ROZE, None)
    d.blob([r(30, -4.5), r(46, -6), r(58, -4), r(46, -3)], (255, 170, 255))          # glans op de neus
    d.blob([r(52, -1), r(57, -3.5), r(61, -1), r(57, 1.5)], (170, 0, 85))            # teenafdruk
    return r


def bandje(d, r, sch=1.0):
    """V-bandje: van het teenpaaltje in de neus naar beide kanten van de taille, wit en dik."""
    paal = r(55, 0)
    for kant in (r(31, -10.5), r(31, 10.5)):     # beide poten van de V vrij naast de krab
        d.dr.line([d.P(*kant), d.P(paal[0], paal[1] - 2 * sch)], fill=WIT, width=max(2, round(5 * sch * d.s)))
        d.rondje(kant[0], kant[1], 2.1 * sch, 2.1 * sch, WIT)
    d.rondje(paal[0], paal[1] - 2 * sch, 3.2 * sch, 3.2 * sch, WIT)


def bellen(d, lijst, c):
    for x, y, r_ in lijst:
        d.dr.ellipse([(x - r_) * d.s, (y - r_) * d.s, (x + r_) * d.s, (y + r_) * d.s], outline=c, width=max(1, round(1.3 * d.s)))
        d.dr.ellipse([(x - r_ * .45) * d.s, (y - r_ * .55) * d.s, (x - r_ * .05) * d.s, (y - r_ * .15) * d.s], fill=c)


def wereld_onder(d, dd, held_y=200, held_maat=30, held=True, slipper_y=None, zak=0, met_slipper=True, spiegel=False, anem_dy=0, anem_dx=0, held_x=118):
    """Krab onder water: ver de donkere ruggen, dan zand, twee ronde rotsen (anemoon, zeester), vooraan de held in zijn slipper."""
    s = d.s
    # ver: donkere ronde ruggen over de hele breedte (silhouet)
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in [(40, 176, 60, 26), (150, 186, 70, 20), (240, 168, 46, 30)]:
        d.rondje(cx, cy, rx, ry, verder)
    for cx, cy, rx, ry in [(10, 192, 52, 36), (78, 208, 46, 20), (186, 206, 50, 20), (252, 186, 50, 40)]:
        d.rondje(cx, cy, rx, ry, dd['ver'] if d.am else dd['mip_ver'])
    # zand: een lage ronde heuvel
    d.dr.ellipse([-40 * s, 222 * s, 300 * s, 330 * s], fill=ZAND_DONKER)
    d.dr.ellipse([-30 * s, 226 * s, 290 * s, 330 * s], fill=ZAND if not d.am else (235, 225, 150))
    if d.am:      # lichtvlek van de bundel op het zand
        d.gloed_ellips(124, 234, 48, 11, WIT, .45)
    X = (lambda x: 260 - x) if spiegel else (lambda x: x)
    # rots links met anemoon (paarse bolletjes die meeademen); bij spiegel rechts
    d.rondje(X(36), 202 + zak, 34, 26, ROTS, ROTS_R, glans=ROTS_R)
    # anemoon: vijf dikke tentakels met ronde roze toppen op de rots (geen druiven)
    for bx, tx, ty in [(18, 12, 158), (26, 22, 150), (36, 36, 146), (46, 50, 150), (54, 60, 160)]:
        x0, y0, x1, y1 = X(bx + anem_dx), 180 + zak, X(tx + anem_dx), ty + zak + anem_dy
        d.dr.line([d.P(x0, y0), d.P(x1, y1)], fill=WIT, width=round(8.6 * d.s))
        d.rondje(x1, y1, 4.3, 4.3, WIT)
    for bx, tx, ty in [(18, 12, 158), (26, 22, 150), (36, 36, 146), (46, 50, 150), (54, 60, 160)]:
        x0, y0, x1, y1 = X(bx + anem_dx), 180 + zak, X(tx + anem_dx), ty + zak + anem_dy
        d.dr.line([d.P(x0, y0), d.P(x1, y1)], fill=PAARS, width=round(5.6 * d.s))
        d.rondje(x1, y1, 3.6, 3.6, ROZE)
    d.rondje(X(36 + anem_dx), 180 + zak, 22, 7, PAARS, WIT, dikte=1.6)
    # rots rechts met zeester
    d.rondje(X(222 - zak / 3), 210 + zak, 30, 22, ROTS, ROTS_R, glans=ROTS_R)
    ster = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rr = 11 if i % 2 == 0 else 4.6
        ster.append((X(218 - zak / 3) + rr * math.cos(a), 197 + zak + rr * math.sin(a)))
    d.blob(ster, ZON, WIT, 1.8)
    # held: krab in zijn slipper
    sy = slipper_y if slipper_y is not None else held_y + held_maat * .55
    hx = held_x
    if met_slipper:   # schaduw van de slipper op het zand
        if d.am:
            d.gloed_ellips(hx + 30, sy + 15, 44, 5, (90, 80, 40), .5, groei=.25)
        else:
            d.rondje(hx + 30, sy + 15, 42, 5, ZAND_DONKER)
    if met_slipper:
        r = slipper(d, hx + 2, sy, held_maat / 30 * 1.3 * SLIP, hoek=-4)
    if held:
        d.dier(hx, held_y, held_maat)
    if met_slipper:
        bandje(d, r, held_maat / 30 * 1.3 * SLIP)


def water_onder(d, dd, maan=False, stralen=3, raster_y=None):
    if d.am:
        d.verloop(0, 260, dd['zee_top'], dd['zee_bodem'])
    else:
        # MIP: drie banden van licht naar donker met golvende randen; de middelste is een raster van de twee buren
        # (op 260 leest dat als een tussentint; Gijs zet het als plaatje). Geen harde horizon meer.
        c0, c2 = dd['mip_water']
        def raster(a, b):
            im = Image.new('RGB', (d.N, d.N), a); px = im.load()
            for yy in range(d.N):
                for xx in range(yy % 2, d.N, 2): px[xx, yy] = b
            return im
        def onder_golf(y):
            mk = Image.new('L', (d.N, d.N), 0)
            ImageDraw.Draw(mk).polygon([d.P(x, y + 3 * math.sin(x / 260 * 2 * math.pi * 2)) for x in range(0, 261, 2)] + [d.P(260, 260), d.P(0, 260)], fill=255)
            return mk
        boven = dd.get('mip_boven')
        if boven:   # v2.2: bovenin een raster van 0055AA en 005555: leest als het teal van AMOLED, niet als modderig groen
            d.im.paste(raster(c0, boven), (0, 0))
        else:
            d.verloop(0, 260, c0, None)
        d.golf(raster_y or (142 if boven else 150), 262, c2, 3, 2, 1.0)   # daaronder vlak: geen raster achter tekst of held
    # oppervlak: lichte golvende rand bovenin
    d.dr.polygon([d.P(x, 7 + 2.5 * math.sin(x / 260 * 2 * math.pi * 5)) for x in range(0, 261, 2)] + [d.P(260, 0), d.P(0, 0)],
                 fill=(dd['mip_licht'] if dd['mip_licht'] != (0, 0, 170) else (85, 85, 255)) if not d.am else tuple((a + b) // 2 for a, b in zip(dd['licht'], dd['zee_top'])))
    if maan:      # maanvlek op het oppervlak, in de stand van de maan (hier: links boven)
        if d.am:
            d.gloed_ellips(88, 5, 22, 17, (200, 200, 255), .55)
        else:
            d.rondje(88, 6, 24, 12, (85, 85, 255)); d.rondje(88, 5, 14, 7, (170, 170, 255))
    if stralen: bundel(d, dd, maan)


def bundel(d, dd, nacht, xo=118, xh=112, yh=236):
    """Een brede lichtbundel van het oppervlak (bij nacht van de maanvlek) die schuin op de held valt.
    AMOLED: zacht en vervagend. MIP: een vlak een stap lichter dan het water (wit haalt er nog 5:1 op)."""
    top_b, onder_b = (26, 96) if d.am else (16, 74)
    vlak = [d.P(xo - top_b, 0), d.P(xo + top_b, 0), d.P(xh + onder_b / 2, yh), d.P(xh - onder_b / 2, yh)]
    if d.am:
        totaal = .34 if not nacht else .22; a = 1 - (1 - totaal) ** (1 / 3)
        for k in (1.45, 1.2, .95):      # drie tinten: buiten breed en zwak, binnen smal (bouwbaar, geen vervaging)
            v = [d.P(xo - top_b * k, 0), d.P(xo + top_b * k, 0), d.P(xh + onder_b / 2 * k, yh), d.P(xh - onder_b / 2 * k, yh)]
            d.tint(lambda ld, v=v: ld.polygon(v, fill=255), dd['licht'], a)
    else:
        pass      # MIP: geen bundel (harde vlakken lazen als palen); het licht zit in de golfrand bovenin


def kring(d, dd, cx, cy, r_):
    """Zachte lichtkring achter de nieuwe vriend (alleen op het eindscherm). MIP: een vlak een stap lichter met lichte rand."""
    if d.am:
        d.gloed_ellips(cx, cy, r_ * .8, r_ * .65, dd['licht'], .4)
    else:
        pass      # MIP: geen harde ellips achter de held (keuring 8); het feest zit in vonkjes en bellen


def stofjes(d, dd):
    """Zwevende lichtjes in het water (diepte): klein en weinig, nooit achter tekst (alleen opzij)."""
    if dd is DAG:
        for x, y, r_ in [(20, 150, 1.1), (36, 146, .8), (240, 152, 1.1), (242, 140, .8), (214, 152, .7), (18, 160, .7),
                         (30, 92, 1), (230, 92, 1), (44, 136, .8), (216, 136, .8)]:
            d.rondje(x, y, r_ * (1 if d.am else 1.3), r_ * (1 if d.am else 1.3), (170, 255, 255))
        bellen(d, [(26, 132, 2.6), (234, 128, 2.2)], (170, 255, 255))
        return
    plankton = [(22, 112, 1.6), (34, 138, 1.1), (16, 158, 1.3), (48, 120, .9), (232, 104, 1.6), (244, 132, 1.1),
                (220, 146, 1.3), (208, 118, .9), (60, 150, 1), (196, 156, 1), (30, 92, .9), (236, 84, .9)]
    if d.am:
        for x, y, r_ in plankton: d.gloed_ellips(x, y, r_ * 2.4, r_ * 2.4, (0, 255, 170), .45, stappen=2, groei=.5)
    for x, y, r_ in plankton:
        d.rondje(x, y, r_, r_, (170, 255, 170) if d.am else (85, 255, 170))


def fonkel(d, x, y, k):
    """Feestvonkje: ster met vier punten in lichtgeel."""
    pts = []
    for i in range(8):
        a = i * math.pi / 4; rr = k if i % 2 == 0 else k * .28
        pts.append((x + rr * math.sin(a), y - rr * math.cos(a)))
    d.blob(pts, (255, 255, 170))


# ---------------- schermen ----------------
def adem_in(D_, am, dd, nacht, top=134, woord='breathe in', getal='12', onder='round 2 · 18 left', held_maat=36):
    """Boven water: het cijfer staat groot in de lucht, de krab dobbert groot en midden op de kam,
    eronder rijen golven die naar voren breder worden (diepte zonder bodem). Zon of maan links met een baan van licht."""
    d = Doek(D_, am)
    d.verloop(0, top, dd['lucht'][0], dd['lucht'][1], [(top - 28, dd['lucht'][1] if not nacht else (0, 0, 85))])   # nacht MIP: lucht donker, zee lichter
    if nacht:
        for x, y in [(56, 50), (204, 44), (222, 82), (34, 100), (184, 24), (96, 20), (238, 110)]:
            d.rondje(x, y, .9, .9, WIT)
        d.rondje(40, 84, 13, 13, (255, 255, 170), (170, 170, 255), dikte=1.6)       # maan (wassend), altijd boven de hoogste kam
        d.rondje(47, 82, 11, 12, dd['lucht'][1] if not am else (0, 25, 120))
    else:
        if am: d.gloed_ellips(40, 86, 20, 20, (255, 255, 170), .35)
        d.rondje(40, 86, 14, 14, ZON, WIT, glans=WIT, dikte=2)
    # zee: kam met schuim, daaronder drie golfrijen (achter smal en licht, voor breed en donker)
    golfkleur_am = [(0, 85, 175), (0, 65, 150), (0, 45, 125), (0, 28, 95)] if not nacht else \
                   [(0, 75, 150), (0, 55, 125), (0, 35, 100), (0, 15, 75)]
    golfkleur_mip = [(0, 85, 170), (0, 85, 170), (0, 0, 170), (0, 0, 170)] if not nacht else \
                    [(0, 0, 170), (0, 0, 170), (0, 0, 85), (0, 0, 85)]
    d.golf(top - 3, 262, WIT, 4, 2, 1.2)
    rijen = [(top, 4, 2, 1.2), (top + 34, 3, 4, .3), (top + 66, 3.5, 3, 2.0), (top + 98, 4, 2, .8)]
    for k, (y, a, n, fa) in enumerate(rijen):
        if k: d.golf(y - 1.6, 262, (85, 170, 255) if not nacht else (85, 85, 255), a, n, fa)   # lichte rand op elke rij
        d.golf(y, 262, golfkleur_am[k] if am else golfkleur_mip[k], a, n, fa)
    # grap: ver weg drijft de andere slipper van het paar (klein, op de kam links)
    zx, zy = 76, top - 2
    k = 1.7; d.blob([(zx - 7 * k, zy), (zx - 4 * k, zy - 2.6 * k), (zx + 3 * k, zy - 2.2 * k), (zx + 8 * k, zy - .4 * k), (zx + 3 * k, zy + 1.2 * k), (zx - 4 * k, zy + 1.2 * k)], ROZE, WIT, 1.4)
    d.dr.line([d.P(zx + 4 * k, zy - 1 * k), d.P(zx - 1 * k, zy - 2.4 * k), d.P(zx + 4 * k, zy + .2 * k)], fill=WIT, width=max(1, round(1.4 * d.s)))
    # boven water iets te zien: een wolkje (bij nacht donker) en overdag een meeuw
    wk = (255, 255, 255) if not nacht else (85, 85, 170); wr = (170, 255, 255) if not nacht else (0, 0, 170)
    for cx, cy, rx, ry in [(214, 70, 14, 8), (226, 64, 12, 10), (236, 72, 11, 7)]:
        d.rondje(cx, cy, rx, ry, wr)
    for cx, cy, rx, ry in [(214, 69, 12, 6.5), (226, 63, 10, 8.5), (236, 71, 9, 5.5)]:
        d.rondje(cx, cy, rx, ry, wk)
    if not nacht:
        for x0, sgn in ((62, -1), (62, 1)):
            d.dr.line([d.P(x0, 54), d.P(x0 + sgn * 5, 50), d.P(x0 + sgn * 9, 53)], fill=WIT, width=max(2, round(1.8 * d.s)), joint='curve')
    # held: krab in zijn slipper, groot en midden op de kam
    sch = held_maat / 34 * 1.45 * SLIP * 1.15
    hx = 124 if top > 140 else 154     # bij hoge zee schuift de krab naar rechts: het cijfer blijft vrij (punt 4)
    dy = 0 if top < 140 else -5      # bij lage zee iets hoger op de kam, zodat hij dobbert en niet verdrinkt
    r = slipper(d, hx + 4, top + 12 + dy * .6, sch, hoek=-5)    # hak onder de krab, neus en bandje steken rechts uit
    d.dier(hx, top + dy, held_maat); bandje(d, r, sch)
    d.tekst(130, 14 if top < 140 else 22, woord, 25, WIT)
    d.tekst(130, 32 if top < 140 else 42, getal, 56, WIT)
    d.tekst(130, top + 40, onder, 16, WIT, False)     # tussen twee golfrijen in, nooit op een lijn
    return d.klaar()


def hold(D_, am, dd, nacht):
    d = Doek(D_, am); water_onder(d, dd, nacht)
    wereld_onder(d, dd, held_y=184, held_maat=43)
    stofjes(d, dd)
    bellen(d, [(192, 160, 3), (198, 148, 2.2)], WIT)
    d.tekst(130, 24, 'hold', 24, GEEL)
    d.tekst(130, 48, 'press START to breathe', 14, WIT, False)
    d.tekst(130, 58, '1:45', 58, WIT)
    d.tekst(130, 118, '61 bpm · round 2', 16, WIT, False)
    return d.klaar()


def menu(D_, am, dd, nacht):
    d = Doek(D_, am); water_onder(d, dd, nacht)
    wereld_onder(d, dd, held_y=186, held_maat=38, spiegel=True, anem_dy=10)
    stofjes(d, dd)
    s = d.s
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for y, t in [(52, 'Rounds'), (86, 'Calm 4-7-8')]:
        if am:
            # vaste kleur (geen doorschijnende pil, dat kan het horloge niet)
            d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=(0, 30, 60) if dd is DAG else (0, 0, 50),
                                   outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        else:
            d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=(0, 0, 85),
                                   outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        d.tekst(130, y + 2, t, 20, WIT)
    d.tekst(130, 118, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    return d.klaar()


def eind(D_, am, dd, nacht):
    """Eindscherm: de krab in zijn slipper links, de nieuwe vriend (hier de garnaal) in een belletje rechts: dat heb je gewonnen."""
    d = Doek(D_, am); water_onder(d, dd, nacht, stralen=0, raster_y=146)
    bundel(d, dd, nacht, xo=184, xh=186, yh=164)     # het licht staat op de nieuwe vriend
    wereld_onder(d, dd, held=False, zak=22, met_slipper=False, anem_dy=14, anem_dx=-8)
    stofjes(d, dd)
    for x, y, r_ in [(40, 96, 2.6), (52, 82, 1.8), (224, 168, 2.4)]:
        bellen(d, [(x, y, r_)], WIT)
    for x, y, k in [(226, 82, 8), (146, 86, 5), (236, 146, 5)]:
        fonkel(d, x, y, k)
    # belletje van de sea log (zelfde stijl als in de app: vlak 0055AA, rand 00FFFF, glimpje)
    bx, by, brx, bry = 184, 122, 40, 35
    kring(d, dd, bx, by, 44)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 4, 4, WIT)
    d.dier(bx, by + 1, 31, D[1])
    hart = [(126 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 108 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)        # de krab vindt zijn nieuwe vriend leuk
    r = slipper(d, 70, 152, 1.25 * SLIP, hoek=-6)
    d.tekst(130, 30, '3 rounds done', 25, GEEL)
    d.tekst(130, 56, '1:20   1:45   1:58', 19, WIT)
    d.dier(76, 130, 34); bandje(d, r, 1.25 * SLIP)
    d.tekst(130, 163, 'new friend', 15, WIT, False)
    d.tekst(130, 171, 'Shrimp', 30, GEEL)       # de naam groot (keuring 8)
    stippen(d.dr, 130 * s_(d), 209 * s_(d), 3, 1, max(2, round(3.5 * s_(d))), round(13 * s_(d)))
    return d.klaar()


def s_(d): return d.s


def adem_uit(D_, am, dd, nacht):
    """Uitademen: de zee zakt, de krab zakt mee; meer lucht."""
    return adem_in(D_, am, dd, nacht, top=170, woord='breathe out', getal='9', onder='round 2 · 18 left')


def calm(D_, am, dd, nacht):
    """Calm 4-7-8: zelfde wereld boven water, de zee halverwege (uitademen 8 tellen)."""
    return adem_in(D_, am, dd, nacht, top=146, woord='breathe out', getal='5', onder='4-7-8 · 2 of 4')


SCHERMEN = [('in', adem_in), ('uit', adem_uit), ('calm', calm), ('hold', hold), ('menu', menu), ('eind', eind)]


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    rij = {}
    for nacht in (False, True):
        dd = NACHT if nacht else DAG
        for D_, am in ((454, True), (260, False)):
            for naam, fn in SCHERMEN:
                im = fn(D_, am, dd, nacht)
                nm = f'krab-{naam}-{"nacht" if nacht else "dag"}-{D_}.png'
                im.save(os.path.join(uit, nm)); rij[(naam, nacht, D_)] = im
    # overzicht: per maat een rij van 8 (4 dag, 4 nacht); 260 ook 2x voor het oog
    for D_, k in ((454, 1), (260, 2), (260, 1)):
        g = 12 * k; W = D_ * k
        n = len(SCHERMEN); ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
        for j, nacht in enumerate((False, True)):
            for i, (naam, _) in enumerate(SCHERMEN):
                ov.paste(rij[(naam, nacht, D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
        ov.save(os.path.join(uit, f'overzicht-{D_}-{k}x.png'))
