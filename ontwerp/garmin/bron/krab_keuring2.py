# Krab na frisse keuring 2 (Mila, run 52, 12 nov): drie punten van de hoofdchat (05:25 NL).
#  1. De slipper wordt een rood-witte zwemband: de krab zit erin en dobbert op de golf. Onder water draagt hij hem nog.
#  2. Nacht als een kleurregel voor alle werelden: alles behalve de tekst gaat door NACHT_REGEL (bijna zwart, geen groen).
#  3. Omtrek op MIP: wit (zoals nu), donker 1 px, of geen. Naast elkaar op 260.
# Gebruik: python3 krab_keuring2.py <uitmap>
# Bouwt op werelden_v32.py; verandert daar niets.
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
import werelden_v21 as w
# werelden_v3 zonder de tweede slipper en zonder het teenpaaltje (alleen in dit voorstel; het bestand zelf blijft gelijk)
import types
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'werelden_v3.py')).read()
_weg = [l for l in _src.split('\n') if ('zx, zy = 72' in l or 'zx + 4 * k' in l or '(zx - 7 * k' in l or 'teenpaaltje duidelijker' in l)]
assert len(_weg) == 6, len(_weg)
for l in _weg:
    _src = _src.replace(l + '\n', '')
v3 = types.ModuleType('werelden_v3'); v3.__file__ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'werelden_v3.py')
sys.modules['werelden_v3'] = v3
exec(compile(_src, v3.__file__, 'exec'), v3.__dict__)
import werelden_v32 as v32
from PIL import Image, ImageDraw, ImageChops, ImageFilter

ROOD, ROOD_D, WIT = (255, 0, 0), (170, 0, 0), (255, 255, 255)


# ---------- 1. zwemband ----------
def band_punten(r, sch, a0, a1, rx=23, ry=8.5, buis=6.5):
    """Een stuk van de band tussen hoek a0 en a1 (graden, 0 = rechts, 90 = voor/onder)."""
    pts = []
    for i in range(9):
        a = math.radians(a0 + (a1 - a0) * i / 8)
        pts.append(r((rx + buis / 2) * math.cos(a), (ry + buis / 2) * math.sin(a)))
    for i in range(9):
        a = math.radians(a1 - (a1 - a0) * i / 8)
        pts.append(r((rx - buis / 2) * math.cos(a), (ry - buis / 2) * math.sin(a)))
    return pts


def teken_band(d, r, sch, voor):
    # achterhelft: 180..360 (boven het midden), voorhelft: 0..180
    a0 = 0 if voor else 180
    stuk = 22.5
    if voor:   # donkere onderkant voor diepte
        d.blob([(x, y + 2.2 * sch) for x, y in band_punten(r, sch, 0, 180)], ROOD_D)
    for i in range(8):
        aa = a0 + i * stuk
        d.blob(band_punten(r, sch, aa, aa + stuk + .6), ROOD if i % 2 == 0 else WIT)
    if voor:   # glimlijntje op de band
        g = [r(-14 + t, 6.6 + .02 * t * t - .5) for t in range(0, 10, 2)]
        d.dr.line([d.P(*p) for p in g], fill=WIT, width=max(1, round(1.4 * d.s)))


def zwemband(d, cx, cy, sch=1.0, hoek=-8):
    """Vervangt slipper(): tekent de achterkant van de band, de krab komt erin, bandje() tekent de voorkant."""
    a = math.radians(hoek * .4)
    k = sch * 1.05

    def r(x, y):
        return (cx - 4 * sch + (x * math.cos(a) - y * math.sin(a)) * k, cy - 3 * sch + (x * math.sin(a) + y * math.cos(a)) * k)
    r.sch = k
    teken_band(d, r, k, voor=False)
    return r


def band_voor(d, r, sch=1.0):
    teken_band(d, r, r.sch, voor=True)


def zet_band():
    w.slipper = zwemband; w.bandje = band_voor
    v32.slipper = zwemband; v32.bandje = band_voor


# Doek.blob met alleen een vlak (bestaat al in v21? zo niet: hier)
if not hasattr(w.Doek, 'blob'):
    def _blob(self, pts, c, rand=None, dikte=2.2):
        self.dr.polygon([self.P(x, y) for x, y in pts], fill=c)
    w.Doek.blob = _blob


# ---------- 3. omtrek ----------
_teken_orig = h.teken
OMTREK = {'modus': 'wit'}


def teken_omtrek(dr, dier, cx, cy, maat, oog_modus='v83'):
    m = OMTREK['modus']
    if m == 'wit':
        return _teken_orig(dr, dier, cx, cy, maat, oog_modus)
    if m == 'donker1':
        kl = OMTREK.get('kleur', '000000')
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)):
            h.delen(dr, dier, cx + dx, cy + dy, maat, h.hx(kl), 2)
    o = h.delen(dr, dier, cx, cy, maat, None, 0)
    h.ogen(dr, dier, o, cx, cy, maat, oog_modus)


h.teken = teken_omtrek


# ---------- 2. nachtregel ----------
def nacht_kanaal_amoled(v):
    """Donker en gedempt: v' = 0,7 * 255 * (v/255)^2. Wit 178, 170 wordt 79, 105 wordt 30, 85 wordt 20."""
    return round(.7 * 255 * (v / 255) ** 2)


MIP_STAP = {0: 0, 85: 0, 170: 85, 255: 170}   # elke MIP-kleur een trede omlaag: blijft in de 64 kleuren


def nacht_pixel(c, am):
    if am:
        r, g, b = (nacht_kanaal_amoled(v) for v in c)
    else:
        r, g, b = (MIP_STAP[min(MIP_STAP, key=lambda k: abs(k - v))] for v in c)
    g = min(g, max(r, b))          # geen groen: groen nooit sterker dan rood of blauw
    return (r, g, b)


def nacht_lut(am):
    lut = []
    for kanaal in range(3):
        lut += [nacht_pixel((v, v, v), am)[kanaal] for v in range(256)]
    return lut


def nachtregel(im_met, im_zonder, am):
    """im_met = scherm met tekst, im_zonder = zelfde scherm zonder tekst. Tekst blijft, de rest gaat door de regel."""
    mk = ImageChops.difference(im_met, im_zonder).convert('L').point(lambda v: 255 if v > 8 else 0)
    mk = mk.filter(ImageFilter.MaxFilter(3))
    # kanaal voor kanaal, daarna de groenregel
    r, g, b = im_zonder.split()
    if am:
        f = [nacht_kanaal_amoled(v) for v in range(256)]
    else:
        f = [MIP_STAP[min(MIP_STAP, key=lambda k: abs(k - v))] for v in range(256)]
    r, g, b = r.point(f), g.point(f), b.point(f)
    g = ImageChops.darker(g, ImageChops.lighter(r, b))
    donker = Image.merge('RGB', (r, g, b))
    return Image.composite(im_met, donker, mk)


def zonder_tekst(fn):
    oud = w.tekst
    w.tekst = lambda *a, **k: None
    try:
        return fn()
    finally:
        w.tekst = oud


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']


def maak(naam, D_, am, nacht):
    f = v32.scherm(naam, 'krab')
    dd = w.NACHT if nacht else w.DAG
    im = f(D_, am, dd, nacht)
    if not nacht:
        return im
    leeg = zonder_tekst(lambda: f(D_, am, dd, nacht))
    return nachtregel(im, leeg, am)


def overzicht(beelden, D_, k, pad):
    g = 12 * k; W = D_ * k; n = len(NAMEN)
    ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
    for j, nacht in enumerate((False, True)):
        for i, naam in enumerate(NAMEN):
            ov.paste(beelden[(naam, nacht)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
    ov.save(pad)


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    zet_band()
    # A. hele krab met band en nachtregel, omtrek wit (zoals nu) op 454, en elke omtrek op 260
    for modus in ('wit', 'donker1', 'geen'):
        OMTREK['modus'] = modus
        for D_, am in ((454, True), (260, False)):
            if D_ == 454 and modus != 'wit':
                continue
            b = {}
            for nacht in (False, True):
                for naam in NAMEN:
                    im = maak(naam, D_, am, nacht); b[(naam, nacht)] = im
                    im.save(os.path.join(uit, f'krab-{naam}-{"nacht" if nacht else "dag"}-{D_}-{modus}.png'))
            for k in ((1, 2) if D_ == 260 else (1,)):
                overzicht(b, D_, k, os.path.join(uit, f'overzicht-krab-{D_}-{k}x-{modus}.png'))
    OMTREK['modus'] = 'wit'
