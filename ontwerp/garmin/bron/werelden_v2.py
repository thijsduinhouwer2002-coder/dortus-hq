# Blad werelden v2 (Mila, run 43, 12 nov): nieuwe richting van de hoofdchat (12 nov 01:45 NL), eerst alleen de krab.
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
WIT, GEEL = (255, 255, 255), (255, 255, 170)
DAG = dict(lucht=[(0, 85, 170), (0, 170, 255)], zee_top=(0, 110, 205), zee_bodem=(0, 20, 95), licht=(85, 255, 255),
           ver=(0, 0, 85), mip_water=[(0, 85, 170), (0, 0, 170)], mip_licht=(0, 85, 255), mip_zee=(0, 85, 170))
NACHT = dict(lucht=[(0, 0, 85), (0, 0, 170)], zee_top=(0, 0, 140), zee_bodem=(0, 0, 35), licht=(170, 170, 255),
             ver=(0, 0, 60), mip_water=[(0, 0, 170), (0, 0, 85)], mip_licht=(0, 0, 255), mip_zee=(0, 0, 170))
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

    def tekst(self, x, y, s, maat, c, dik=True):
        tekst(self.dr, x * self.s, y * self.s, s, f(FS if dik else FM, round(maat * self.s)), c)

    def dier(self, cx, cy, maat260):
        m = round(maat260 * self.D / 260)
        lag = Image.new('RGB', (self.D, self.D)); ld = ImageDraw.Draw(lag)
        _, _, ox, oy = kader(KRAB, m)
        lag = Image.new('RGB', (self.D, self.D), (1, 2, 3)); ld = ImageDraw.Draw(lag)
        h.teken(ld, KRAB, round(cx * self.D / 260 - ox), round(cy * self.D / 260 - oy), m)
        from PIL import ImageChops
        mk = ImageChops.difference(lag, Image.new('RGB', (self.D, self.D), (1, 2, 3))).convert('L').point(lambda v: 255 if v else 0)
        lag = lag.resize((self.N, self.N), Image.NEAREST); mk = mk.resize((self.N, self.N), Image.NEAREST)
        self.im.paste(lag, (0, 0), mk)

    def klaar(self):
        im = self.im.resize((self.D, self.D), Image.LANCZOS) if self.am else self.im
        return rond(im)


# ---------------- de krab en zijn wereld ----------------
def slipper(d, cx, cy, sch=1.0, hoek=-8):
    """Grote roze teenslipper (de haak): zool met witte rand en glans, bandje in V naar het teenpaaltje."""
    def r(x, y):
        a = math.radians(hoek); return (cx + (x * math.cos(a) - y * math.sin(a)) * sch, cy + (x * math.sin(a) + y * math.cos(a)) * sch)
    zool = [r(36 * math.cos(t), 11 * math.sin(t) * (1.0 if math.cos(t) > 0 else 0.86)) for t in [i / 24 * 2 * math.pi for i in range(24)]]
    d.blob(zool, ROZE, WIT, 2.4)
    d.blob([r(-28, -3), r(10, -6), r(26, -4), r(10, -2)], (255, 170, 255))      # glans op de zool
    return r


def bandje(d, r, sch=1.0):
    """Het witte bandje komt voor de krab langs: hij ligt erin."""
    for a, b in [((-22, -2), (14, -17)), ((14, -17), (20, -1))]:
        (x0, y0), (x1, y1) = r(*a), r(*b)
        d.dr.line([d.P(x0, y0), d.P(x1, y1)], fill=WIT, width=max(2, round(4.2 * sch * d.s)))
    x, y = r(14, -17); d.rondje(x, y, 3.2 * sch, 3.2 * sch, WIT)


def bellen(d, lijst, c):
    for x, y, r_ in lijst:
        d.dr.ellipse([(x - r_) * d.s, (y - r_) * d.s, (x + r_) * d.s, (y + r_) * d.s], outline=c, width=max(1, round(1.3 * d.s)))
        d.dr.ellipse([(x - r_ * .45) * d.s, (y - r_ * .55) * d.s, (x - r_ * .05) * d.s, (y - r_ * .15) * d.s], fill=c)


def wereld_onder(d, dd, held_y=200, held_maat=30, held=True, slipper_y=None, zak=0, met_slipper=True):
    """Krab onder water: ver de donkere ruggen, dan zand, twee ronde rotsen (anemoon, zeester), vooraan de held in zijn slipper."""
    s = d.s
    # ver: donkere ronde ruggen over de hele breedte (silhouet)
    for cx, cy, rx, ry in [(10, 186, 52, 40), (78, 204, 46, 22), (186, 202, 50, 22), (252, 180, 50, 44)]:
        d.rondje(cx, cy, rx, ry, dd['ver'])
    # zand: een lage ronde heuvel
    d.dr.ellipse([-60 * s, 214 * s, 320 * s, 330 * s], fill=ZAND_DONKER)
    d.dr.ellipse([-50 * s, 218 * s, 310 * s, 330 * s], fill=ZAND)
    # rots links met anemoon (paarse bolletjes die meeademen)
    d.rondje(36, 202 + zak, 34, 26, ROTS, ROTS_R, glans=ROTS_R)
    for x, y, r_ in [(30, 172, 7), (41, 169, 7.5), (51, 175, 6.5), (21, 178, 6)]:
        d.rondje(x, y + zak, r_, r_, PAARS, WIT, glans=(255, 170, 255), dikte=1.8)
    # rots rechts met zeester
    d.rondje(222 - zak / 3, 210 + zak, 30, 22, ROTS, ROTS_R, glans=ROTS_R)
    ster = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rr = 11 if i % 2 == 0 else 4.6
        ster.append((218 - zak / 3 + rr * math.cos(a), 197 + zak + rr * math.sin(a)))
    d.blob(ster, ZON, WIT, 1.8)
    # held: krab in zijn slipper
    sy = slipper_y if slipper_y is not None else held_y + 14
    if met_slipper:
        r = slipper(d, 130, sy, held_maat / 30 * 1.25)
        bandje(d, r, held_maat / 30 * 1.25)
    if held:
        d.dier(132, held_y, held_maat)


def water_onder(d, dd, maan=False, stralen=3):
    if d.am:
        d.verloop(0, 260, dd['zee_top'], dd['zee_bodem'])
    else:
        d.verloop(0, 260, dd['mip_water'][0], None, [(150, dd['mip_water'][1])])
    # oppervlak: lichte golvende rand bovenin
    d.golf(-2, -2, dd['licht'])
    d.dr.polygon([d.P(x, 7 + 2.5 * math.sin(x / 260 * 2 * math.pi * 5)) for x in range(0, 261, 2)] + [d.P(260, 0), d.P(0, 0)],
                 fill=dd['licht'] if not d.am else tuple((a + b) // 2 for a, b in zip(dd['licht'], dd['zee_top'])))
    if maan:      # maanvlek op het oppervlak, in de stand van de maan (hier: links boven)
        if d.am:
            laag = Image.new('L', (d.N, d.N), 0)
            ImageDraw.Draw(laag).ellipse([60 * d.s, -16 * d.s, 116 * d.s, 26 * d.s], fill=150)
            d.im.paste(Image.new('RGB', (d.N, d.N), (200, 200, 255)), (0, 0), laag.filter(ImageFilter.GaussianBlur(7 * d.s)))
        else:
            d.rondje(88, 6, 24, 12, (85, 85, 255)); d.rondje(88, 5, 14, 7, (170, 170, 255))
    if d.am: d.stralen(dd['licht'], dd['zee_top'], stralen if not maan else 1)


# ---------------- schermen ----------------
def adem_in(D_, am, dd, nacht):
    d = Doek(D_, am)
    d.verloop(0, 96, dd['lucht'][0], dd['lucht'][1], [(66, dd['lucht'][1])])
    if nacht:
        for x, y in [(52, 52), (200, 40), (222, 74), (36, 92), (178, 22), (104, 18)]:
            d.rondje(x, y, .9, .9, WIT)
        d.rondje(44, 74, 12, 12, (255, 255, 170), (170, 170, 255), dikte=1.6)       # maan (wassend, schaduw rechts)
        d.rondje(51, 72, 10, 11, dd['lucht'][1] if not am else (0, 30, 130))
    else:
        d.rondje(44, 76, 13, 13, ZON, WIT, glans=WIT, dikte=2)
    # grote zee met kam en schuim
    top = 98
    d.golf(top - 3, 262, WIT, 4, 2, 1.2)
    zl = Image.new('RGB', (d.N, d.N)); zd = Doek(D_, am); zd.verloop(top, 260, (0, 120, 210) if am and not nacht else (dd['zee_top'] if am else dd['mip_zee']), dd['zee_bodem'] if am else dd['mip_zee'])
    mk = Image.new('L', (d.N, d.N), 0)
    ImageDraw.Draw(mk).polygon([d.P(x, top + 2 + 4 * math.sin(x / 260 * 4 * math.pi + 1.2)) for x in range(0, 261, 2)] + [d.P(260, 262), d.P(0, 262)], fill=255)
    d.im.paste(zd.im, (0, 0), mk)
    # krab dobbert in zijn slipper op de kam, rechts van het cijfer
    # glinstering van zon of maan op het water, onder de lichtbron
    for x, y, b in [(44, 112, 22), (40, 122, 14), (50, 131, 9), (44, 140, 5)]:
        d.dr.rounded_rectangle([(x - b / 2) * d.s, y * d.s, (x + b / 2) * d.s, (y + 2.4) * d.s], radius=1.2 * d.s,
                               fill=(255, 255, 170) if not nacht else (170, 170, 255))
    d.golf(196, 262, (0, 85, 170) if not nacht else (0, 0, 170), 3.5, 3, 0.4) if not am else None
    if am:
        g = Image.new('L', (d.N, d.N), 0)
        ImageDraw.Draw(g).polygon([d.P(x, 196 + 3.5 * math.sin(x / 260 * 6 * math.pi + .4)) for x in range(0, 261, 2)] + [d.P(260, 262), d.P(0, 262)], fill=90)
        d.im.paste(Image.new('RGB', (d.N, d.N), (0, 0, 40)), (0, 0), g)
    r = slipper(d, 128, top + 12, 1.12, hoek=-6)
    bandje(d, r, 1.12); d.dier(130, top + 1, 26)
    d.tekst(130, 30, 'breathe in', 25, WIT)
    d.tekst(130, 53, 'round 2 · 18 left', 15, WIT, False)
    d.tekst(130, 130, '12', 62, WIT)
    return d.klaar()


def hold(D_, am, dd, nacht):
    d = Doek(D_, am); water_onder(d, dd, nacht)
    wereld_onder(d, dd, held_y=200, held_maat=36)
    bellen(d, [(172, 170, 3), (178, 160, 2.2)], WIT)
    d.tekst(130, 30, 'hold', 26, GEEL)
    d.tekst(130, 58, 'press START to breathe', 15, WIT, False)
    d.tekst(130, 70, '1:45', 66, WIT)
    d.tekst(130, 140, '61 bpm · round 2', 16, WIT, False)
    return d.klaar()


def menu(D_, am, dd, nacht):
    d = Doek(D_, am); water_onder(d, dd, nacht)
    wereld_onder(d, dd, held_y=200, held_maat=34)
    s = d.s
    d.tekst(130, 22, 'Ebb', 28, GEEL)
    for y, t in [(56, 'Rounds'), (96, 'Calm 4-7-8')]:
        d.dr.rounded_rectangle([55 * s, y * s, 205 * s, (y + 32) * s], radius=16 * s, fill=(0, 0, 85),
                               outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        d.tekst(130, y + 3, t, 22, WIT)
    d.tekst(130, 132, 'Sea log  ·  Settings  ·  Today', 17, GEEL, False)
    return d.klaar()


def eind(D_, am, dd, nacht):
    d = Doek(D_, am); water_onder(d, dd, nacht, stralen=2)
    wereld_onder(d, dd, held=False, zak=22, met_slipper=False)
    r = slipper(d, 128, 136, 1.05, hoek=-6); bandje(d, r, 1.05)
    d.tekst(130, 30, '3 rounds done', 25, GEEL)
    d.tekst(130, 58, '1:20   1:45   1:58', 24, WIT)
    d.dier(130, 120, 28)
    bellen(d, [(172, 104, 2.6), (178, 94, 1.8)], WIT)
    d.tekst(130, 156, 'new friend: Crab', 24, GEEL)
    stippen(d.dr, 130 * s_(d), 194 * s_(d), 3, 1, max(2, round(3.5 * s_(d))), round(13 * s_(d)))
    return d.klaar()


def s_(d): return d.s


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    rij = {}
    for nacht in (False, True):
        dd = NACHT if nacht else DAG
        for D_, am in ((454, True), (260, False)):
            for naam, fn in [('in', adem_in), ('hold', hold), ('menu', menu), ('eind', eind)]:
                im = fn(D_, am, dd, nacht)
                nm = f'krab-{naam}-{"nacht" if nacht else "dag"}-{D_}.png'
                im.save(os.path.join(uit, nm)); rij[(naam, nacht, D_)] = im
    # overzicht: per maat een rij van 8 (4 dag, 4 nacht); 260 ook 2x voor het oog
    for D_, k in ((454, 1), (260, 2), (260, 1)):
        g = 12 * k; W = D_ * k
        ov = Image.new('RGB', (4 * W + 5 * g, 2 * W + 3 * g), (30, 30, 30))
        for j, nacht in enumerate((False, True)):
            for i, naam in enumerate(['in', 'hold', 'menu', 'eind']):
                ov.paste(rij[(naam, nacht, D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
        ov.save(os.path.join(uit, f'overzicht-{D_}-{k}x.png'))
