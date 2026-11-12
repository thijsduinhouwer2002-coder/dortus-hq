# Blad werelden v1.3 (Mila, run 41): eigen schatjes per wereld met een grap in week 4, geen Y-koraal, kasteel binnen de rand,
# aankomst en vertrek per wereld (besluit 12 nov 01:20). Daaronder v1.2:
# Blad werelden v1.2 (Mila, run 40): de acht punten van de frisse keuring v1.1 plus de bouwvragen van Gijs (11 nov 23:55)
# en besluit 12 nov 00:25 (diepte in drie lagen, lichtstralen, wereld ademt mee, wereld groeit met weekdoelen).
# Elk vlak heeft nu: laag (ver, midden, voor), optioneel p2 (tweede stand bij inademen, zelfde aantal punten)
# en week (vanaf welk gehaald weekdoel het verschijnt, 0 = altijd). Per scherm staan kam, dier en tekstregels in de data.
#   python3 werelden_v12.py <uitmap>
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v1 as V
import horloge_sim as h
from werelden_v1 import spriet, vinger, hx, zet, TEKSTVAK, meet, D, kader, maat_in_vak, NIEUW, f, FM, FS, \
    SCHUIM, LICHT, MIDDEN, NACHT, WIT, GEEL, rond, stippen
from werelden_v11 import S, lucht, LUCHT, STERREN, pixeltoets
from PIL import Image, ImageDraw, ImageChops, ImageFilter

STROOK = 118          # alles van de wereld ligt op of onder deze y (bitmapstrook van Gijs)
MIP = (0, 85, 170, 255)

def it(c, p, laag='midden', p2=None, week=0):
    return dict(kleur=c, p=[(round(x), round(y)) for x, y in p], laag=laag,
                p2=[(round(x), round(y)) for x, y in p2] if p2 else None, week=week)

def zeegras(x0, y0, x1, y1, b, buig, c, laag='midden', week=0, zwaai=6):
    """Spriet met tweede stand: bij inademen buigt de top zwaai/260 naar rechts (stroming omhoog)."""
    return it(c, spriet(x0, y0, x1, y1, b, buig), laag, spriet(x0, y0, x1 + zwaai, y1 + 2, b, buig + zwaai / 2), week)

def draai(pts, cx, cy, gr):
    a = math.radians(gr); ca, sa = math.cos(a), math.sin(a)
    return [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in pts]

def ver_rug(c='0x0000AA', mid=216):
    """Verre laag: donkere rug achter alles, laag in het midden, hoger aan de randen (diepte)."""
    return it(c, [(0, 150), (24, 174), (56, 206), (110, mid), (150, mid - 2), (204, 206), (236, 176), (260, 152),
                  (260, 240), (0, 240)], 'ver')

def visjes(c='0x0000AA'):
    """Twee verre visjes als silhouet (ver), aan de randen, buiten de tekst."""
    v1 = [(26, 136), (36, 131), (43, 136), (48, 131), (48, 141), (36, 141)]
    v2 = [(234, 128), (224, 123), (217, 128), (212, 123), (212, 133), (224, 133)]
    return [it(c, v1, 'ver'), it(c, v2, 'ver')]

def vlekjes(lijst, c='0x00AAFF', week=0):
    """Lichtvlekjes op de bodem (zon door de golven): ruitjes van 4 punten."""
    return [it(c, [(x - w, y), (x, y - 2), (x + w, y), (x, y + 2)], 'midden', week=week) for x, y, w in lijst]

# groei: vier schatjes van ±12 x 12 op een vaste rij in het zand (x 72, 88, 104, 120; onderkant y 240), elk in een eigen felle kleur
SCHELP = [(0, 0), (-6, -5), (-4, -11), (4, -11), (6, -5)]
STER = [(0, -12), (2, -7), (7, -7), (3, -4), (5, 1), (0, -2), (-5, 1), (-3, -4), (-7, -7), (-2, -7)]
SLAK = [(-6, 0), (-6, -5), (-2, -10), (4, -9), (6, -4), (7, 0)]
KORAAL = [(-1, 0), (-1, -5), (-6, -9), (-4, -11), (0, -7), (3, -12), (5, -11), (1, -4), (1, 0)]
FLES = [(-3, 0), (-3, -7), (-1, -9), (-1, -12), (1, -12), (1, -9), (3, -7), (3, 0)]          # flesje met briefje (8)
EMMER = [(-5, -11), (5, -11), (4, 0), (-4, 0)]                                                # zandemmertje (4) + hengsel apart
HENGSEL = [(-5, -11), (-3, -16), (3, -16), (5, -11), (3, -11), (2, -14), (-2, -14), (-3, -11)]
PAREL = [(-4, 0), (-6, -3), (-4, -6), (0, -7), (4, -6), (6, -3), (4, 0)]                      # open mosseltje (7)
PARELBOL = [(-2, -3), (0, -5), (2, -3), (0, -1)]
MUNT = [(-3, 0), (-6, -3), (-6, -7), (-3, -10), (3, -10), (6, -7), (6, -3), (3, 0)]           # gouden munt (8)
GARNAAL = [(-6, -2), (-3, -8), (3, -10), (7, -7), (4, -6), (1, -6), (-2, -2), (-2, 0)]       # gebogen garnaal (8)
VORM = {'schelp': SCHELP, 'zeester': STER, 'slak': SLAK, 'koraaltak': KORAAL, 'fles': FLES, 'emmer': EMMER,
        'parel': PAREL, 'munt': MUNT, 'garnaal': GARNAAL}

def schatten(rij, x0=72, stap=16, y0=240):
    """rij: [(naam, kleur)] voor week 1 tot 3 (week 4 is per wereld de grap)."""
    return [it(c, [(x + x0 + stap * i, y + y0) for x, y in VORM[n]], week=i + 1) for i, (n, c) in enumerate(rij)]

def los(n, c, x0, y0, week, laag='midden'):
    return it(c, [(x + x0, y + y0) for x, y in VORM.get(n, n) if True], laag, week=week) if isinstance(n, str) else \
           it(c, [(x + x0, y + y0) for x, y in n], laag, week=week)

# ---------------- werelden ----------------
def schildpad():
    z = [ver_rug()]
    z.append(it('0xFFFFAA', [(0, 228), (45, 222), (95, 226), (135, 221), (175, 225), (220, 219), (260, 225), (260, 260), (0, 260)]))
    z.append(it('0xAAAA55', [(130, 244), (144, 241), (156, 245), (144, 247)]))
    z += vlekjes([(140, 232, 6), (60, 236, 5)])
    for a, t, b, bu, c in [((6, 234), (0, 120), 6, 7, '0x00AA55'), ((20, 234), (22, 140), 6, -6, '0x55AA00'),
                           ((16, 236), (34, 176), 4, 8, '0x005500'), ((40, 230), (48, 184), 4, 5, '0x55AA00'),
                           ((254, 232), (260, 124), 6, -7, '0x00AA55'), ((240, 232), (236, 140), 6, 6, '0x55AA00'),
                           ((244, 234), (226, 178), 4, -8, '0x005500')]:
        z.append(zeegras(*a, *t, b, bu, c))
    # de haak: een zandkasteel met kantelen en vlaggetje (schildpadden graven met hun vinnen, deze bouwt dus ook)
    z.append(it('0xFFAA55', [(169, 240), (169, 222), (188, 222), (188, 198), (192, 198), (192, 201), (196, 201), (196, 198),
                             (200, 198), (200, 222), (219, 222), (219, 240)]))
    z.append(it('0x550000', [(191, 240), (191, 232), (194, 229), (197, 232), (197, 240)]))     # deurtje
    z.append(it('0xFFFFFF', [(193, 198), (195, 198), (195, 188), (193, 188)]))                # stokje
    z.append(it('0xFF0000', [(195, 188), (208, 191), (195, 195)]))                           # vlag
    z += schatten([('schelp', '0xFFAAAA'), ('zeester', '0xFF5500'), ('fles', '0x00FFAA')], 76, 16, 238)
    # week 4, de grap: zijn eigen zandemmertje naast het kasteel
    # omgekeerd emmertje: wijd op de muur, smal boven, rood hengsel hangt aan de zijkanten omlaag
    z.append(it('0xFFFF00', [(170, 222), (172, 208), (184, 208), (186, 222)], week=4))
    z.append(it('0xFF0000', [(169, 222), (167, 214), (171, 210), (172, 212), (169, 215), (171, 222)], week=4))
    return dict(dier='Turtle', nr=3, plek='zeegrasweide', items=z, thuis=(92, 214),
                haak='een zandkasteel met kantelen en rood vlaggetje: de schildpad graaft toch al, dus hij bouwt ook',
                details={1: 'schelp (roze)', 2: 'zeester (oranje)', 3: 'flesje met briefje (zeegroen)', 4: 'zijn eigen geel emmertje met rood hengsel naast het kasteel'},
                aankomst=dict(baan=[[290, 150], [210, 160], [140, 196], [92, 214]], spiegel=True, sec=2, wat='glijdt van rechtsboven schuin omlaag naar huis'),
                vertrek=dict(baan=[[92, 214], [60, 180], [10, 140], [-30, 128]], spiegel=True, sec=2, wat='peddelt linksboven weg naar de lucht'))

def krab():
    z = [ver_rug()]
    z.append(it('0xFFFFAA', [(0, 230), (60, 224), (130, 227), (200, 223), (260, 229), (260, 260), (0, 260)]))
    # linker kei: donkere kant 555555, grote lichte kant AAAAAA, paarse vlek 5555AA
    z.append(it('0x555555', [(0, 126), (16, 120), (32, 134), (36, 170), (52, 198), (60, 232), (0, 236)]))
    z.append(it('0xAAAAAA', [(0, 130), (16, 122), (30, 136), (32, 168), (20, 178), (0, 160)]))
    z.append(it('0x5555AA', [(20, 178), (32, 168), (40, 196), (24, 206)]))      # middentint: kei krijgt drie tinten
    z.append(it('0x00AA55', [(30, 150), (36, 132), (36, 146), (44, 136), (36, 156)]))     # plukje wier op de kei
    z.append(it('0xFFFFFF', [(234, 152), (238, 146), (242, 152)]))                          # zeepok
    z.append(it('0x5555AA', [(238, 182), (228, 170), (220, 196), (232, 204)]))   # middentint rechts
    z.append(it('0xFF5500', [(214, 206), (216, 194), (224, 196), (222, 206)]))   # anemoontje in de spleet
    z.append(it('0x555555', [(260, 132), (244, 126), (228, 140), (224, 172), (210, 204), (206, 232), (260, 236)]))
    z.append(it('0xAAAAAA', [(260, 134), (244, 128), (230, 140), (228, 170), (238, 182), (260, 166)]))
    # de grap: teenslipper van boven, 36 x 14: ronde brede teen, smalle hiel, donkere V met punt op 1/4 vanaf de teen
    zool = [(18, 0), (16, -5), (10, -7), (2, -6), (-6, -4), (-13, -4), (-18, -2), (-18, 2), (-13, 4), (-6, 4), (2, 6), (10, 7), (16, 5)]
    band = [(10, 0), (0, -6), (-2, -4), (7, 0), (-2, 4), (0, 6)]
    z.append(it('0xFF55AA', draai([(x * 1.3, y * 1.3) for x, y in zool], 172, 236, -15)))
    z.append(it('0xAA0055', draai([(x * 1.3, y * 1.3) for x, y in band], 172, 236, -15)))
    z += schatten([('schelp', '0xFFFFFF'), ('parel', '0xAA55FF'), ('munt', '0xFFFF00')], 70, 11, 236)
    z.append(los(PARELBOL, '0xFFFFFF', 81, 236, 2))
    # week 4, de grap: de tweede slipper komt aanspoelen, het paar is compleet
    zool2 = [(18, 0), (14, 6), (2, 6), (-12, 4), (-18, 1), (-13, -4), (2, -6), (14, -6)]   # spiegelbeeld: de andere voet
    band2 = [(x, -y) for x, y in band]
    z.append(it('0xFF55AA', draai([(x * 1.3, y * 1.3) for x, y in zool2], 124, 240, -15), week=4)); z.append(it('0xAA0055', draai([(x * 1.3, y * 1.3) for x, y in band2], 124, 240, -15), week=4))
    return dict(dier='Crab', nr=4, plek='rotsen met verloren slipper', items=z, thuis=(200, 214),
                haak='een verloren roze teenslipper; de krab blijft op de bodem ernaast en blaast belletjes',
                details={1: 'schelp (wit)', 2: 'mosseltje met parel', 3: 'gouden munt', 4: 'de tweede roze slipper spoelt aan: het paar is compleet'},
                aankomst=dict(baan=[[290, 226], [240, 222], [200, 214]], spiegel=False, sec=2, wat='loopt zijwaarts over het zand van rechts naar huis'),
                vertrek=dict(baan=[[200, 214], [222, 222], [236, 230]], spiegel=False, sec=2, wat='schuift zijwaarts onder de rechterkei (dier achter de kei tekenen, dan weg)'))

def clownvis():
    z = [ver_rug('0x000055')]
    z.append(it('0xFFAAAA', [(0, 226), (50, 222), (110, 228), (160, 222), (210, 226), (260, 220), (260, 260), (0, 260)]))
    z.append(it('0xFFAA55', [(150, 236), (166, 232), (180, 237), (166, 240)]))
    z.append(it('0xAA0055', [(0, 236), (4, 206), (64, 206), (70, 236)]))
    xs = [-10, 2, 12, 22, 32, 44, 56, 70]; tops = [134, 146, 158, 166, 176, 184, 196]
    z.append(it('0xFF55AA', vinger(xs, 212, tops), p2=vinger(xs, 212, tops, golf=4)))
    # voor het dier: alleen de twee voorste vingers (oog en banden van de vis blijven vrij)
    voor = [it('0xFFAAFF', [(18, 216), (22, 196), (28, 216)], 'voor', [(18, 216), (25, 196), (28, 216)]),
            it('0xFFAAFF', [(54, 216), (58, 200), (64, 216)], 'voor', [(54, 216), (61, 200), (64, 216)])]
    # zwaaiende arm met knik en drie vingertoppen van 3 x 3; hoogste top op 192 (bpm-regel eindigt op ±180)
    arm = [(53, 218), (55, 206), (63, 200), (67, 196), (66, 192), (70, 192), (71, 195), (73, 192), (77, 192), (77, 196),
           (80, 194), (81, 198), (71, 204), (63, 210), (63, 218)]
    z.append(it('0xFFAAFF', arm, p2=[(x + (0 if y > 207 else 3), y) for x, y in arm]))
    z.append(it('0xAA55FF', [(260, 128), (238, 136), (226, 172), (212, 206), (224, 226), (260, 230)]))
    z.append(it('0x550055', [(246, 222), (240, 160), (243, 160), (250, 222)]))
    z.append(it('0xFFAA00', [(198, 228), (186, 214), (184, 204), (190, 196), (200, 194), (210, 198), (214, 208), (206, 220), (202, 228)]))   # waaierkoraal
    z.append(it('0xAA5500', [(199, 226), (193, 200), (207, 200)]))   # nerven
    z += schatten([('schelp', '0xFFFFFF'), ('zeester', '0xFFFF00'), ('garnaal', '0xFFAA55')], 80)
    # week 4, de grap: een klein vriendje in de anemoon (oranje met witte band)
    z.append(it('0xFF5500', [(74, 212), (83, 206), (92, 206), (98, 212), (104, 206), (104, 218), (98, 212), (92, 218), (83, 218)], week=4))
    z.append(it('0xFFFFFF', [(84, 206), (88, 206), (88, 218), (84, 218)], week=4))
    return dict(dier='Clownfish', nr=7, plek='anemoon met zwaaiende arm', items=z + voor, thuis=(44, 188),
                haak='hij zit thuis in zijn anemoon, en één arm zwaait met drie vingers naar hem',
                details={1: 'schelp (wit)', 2: 'zeester (geel)', 3: 'garnaal (zalm)', 4: 'een klein clownvisje als vriendje'},
                aankomst=dict(baan=[[-30, 170], [20, 150], [60, 166], [44, 188]], spiegel=False, sec=2, wat='schiet van links binnen in een boogje terug zijn anemoon in'),
                vertrek=dict(baan=[[44, 188], [40, 200], [36, 214]], spiegel=False, sec=1.5, wat='duikt de anemoon in (voorste vingers erover), weg'))

WERELDEN = [schildpad(), krab(), clownvis()]
# lichtstralen: gedeeld, geen werelddata; top volgt de kam, onderkant y 205, alleen aan de randen
STRALEN = [dict(x_top=14, x_onder=46, breed=8), dict(x_top=40, x_onder=64, breed=4), dict(x_top=230, x_onder=206, breed=8)]
STRAAL_KLEUR = '0x0055FF'
VIS_KLEUR = '0x00AAFF'
def vis(x, y, r=1):   # 8 x 4 met staartknip; r=-1 zwemt naar links
    return [(x, y), (x + 3 * r, y - 2), (x + 6 * r, y), (x + 8 * r, y - 2), (x + 8 * r, y + 2), (x + 3 * r, y + 2)]
VISJES = [vis(24, 136), vis(34, 131), vis(32, 142), vis(236, 128, -1), vis(226, 134, -1), vis(238, 140, -1)]   # twee scholen van drie

def punten(w): return sum(len(i['p']) for i in w['items'])

def zichtbaar(w, laag, week):
    return [i for i in w['items'] if i['laag'] in laag and i['week'] <= week]

def teken(dr, items, D_, inn=False):
    for i in items:
        p = i['p2'] if inn and i['p2'] else i['p']
        dr.polygon([(S(x, D_), S(y, D_)) for x, y in p], fill=hx(i['kleur']))

def water(im, top, D_):
    dr = ImageDraw.Draw(im); dr.rectangle([0, 0, D_, D_], fill=NACHT); lucht(dr, D_)
    s = D_ / 260; a = 4 * s
    for x in range(D_):
        yk = top + int(a * math.sin(x / D_ * 2 * math.pi * 2.5))
        dr.line([(x, yk), (x, D_)], fill=MIDDEN)
    for r in STRALEN:   # stralen eerst, dan de kam erover
        t = top / s + 8
        if t < 200:
            dr.polygon([(S(r['x_top'], D_), S(t, D_)), (S(r['x_top'] + r['breed'], D_), S(t, D_)),
                        (S(r['x_onder'] + r['breed'] / 2, D_), S(205, D_)), (S(r['x_onder'], D_), S(205, D_))], fill=hx(STRAAL_KLEUR))
    for v in VISJES:
        if top / s + 10 < min(y for _, y in v):
            dr.polygon([(S(x, D_), S(y, D_)) for x, y in v], fill=hx(VIS_KLEUR))
    for x in range(D_):
        yk = top + int(a * math.sin(x / D_ * 2 * math.pi * 2.5))
        dr.line([(x, yk + round(2 * s)), (x, yk + round(5 * s))], fill=LICHT)
        dr.line([(x, yk), (x, yk + round(2 * s) - 1)], fill=SCHUIM)

def belletjes(dr, x, y, D_, n=3):
    s = D_ / 260
    for i in range(n):
        r = max(1, round((1 + i % 2) * s)); X, Y = S(x + (4 if i % 2 else -2), D_), S(y - 10 - 11 * i, D_)
        dr.ellipse([X - r, Y - r, X + r, Y + r], outline=WIT, width=max(1, round(s)))

def dier_op(dr, w, D_, x, y, m):
    d = D[w['nr']]; _, _, ox, oy = kader(d, m); h.teken(dr, d, round(S(x, D_) - ox), round(S(y, D_) - oy), m)

SCHERMEN = {}   # voor de data: per scherm kam, dier, tekstregels (y = bovenkant tekst, 1/260 D)

def noteer(nm, **k):
    SCHERMEN.setdefault(nm, k)

def basis(D_, top, w, week, inn=False):
    im = Image.new('RGB', (D_, D_)); water(im, round(top * D_ / 260), D_); dr = ImageDraw.Draw(im)
    teken(dr, zichtbaar(w, ('ver', 'midden'), week), D_, inn); return im, dr

def thuis(dr, w, D_, m, week, inn=False, plek=None):
    x, y = plek or w['thuis']; dier_op(dr, w, D_, x, y, m); teken(dr, zichtbaar(w, ('voor',), week), D_, inn)
    if w['dier'] == 'Crab': belletjes(dr, x + 8, y - 8, D_, 2)
    return (x, y)

def M(D_, a, b): return a if D_ < 300 else b

# ---------------- schermen ----------------
def adem(D_, w, inn, week):
    s = D_ / 260; c = D_ // 2; top = 92 if inn else 186
    im, dr = basis(D_, top, w, week, inn); nm = f'adem-{"in" if inn else "uit"}-{w["dier"]}-{D_}'
    m = M(D_, 27, 47)
    if w['dier'] == 'Turtle' and inn: pos = thuis(dr, w, D_, m, week, inn, (204, top + 4))     # kop boven water: lucht happen
    elif w['dier'] == 'Clownfish' and inn: pos = thuis(dr, w, D_, m, week, inn, (200, 150))    # zwemt uit
    else: pos = thuis(dr, w, D_, m, week, inn, (w['thuis'][0], w['thuis'][1] - (6 if inn else 0)))  # drijft iets op bij inademen
    zet(dr, D_, nm, c, 34 * s, 'breathe in' if inn else 'breathe out', f(FS, round(25 * s)), WIT if inn else SCHUIM)
    zet(dr, D_, nm, c, 62 * s, 'round 2 · 18 left', f(FM, round(16 * s)), WIT)
    yc = 104 if inn else 92
    zet(dr, D_, nm, c, yc * s, '12', f(FS, round(70 * s)), WIT)
    noteer(f'adem-{"in" if inn else "uit"}', kam=top, kam_beweegt='lineair tussen 92 (in) en 186 (uit) over de adem',
           dier=dict(x=pos[0], y=pos[1], maat_260=27, maat_454=47, waar='Turtle: (204, kam+4) bij in; Clownfish: (200,150) bij in; anders thuis, bij in 6 hoger'),
           regels=[dict(tekst='breathe in / breathe out', y=34, maat=25), dict(tekst='round 2 · 18 left', y=62, maat=16),
                   dict(tekst='tel', y=yc, maat=70)], planten='p2' if inn else 'p')
    return rond(im), nm

def hold(D_, w, week):
    s = D_ / 260; c = D_ // 2; im, dr = basis(D_, 30, w, week); nm = f'hold-{w["dier"]}-{D_}'
    pos = thuis(dr, w, D_, M(D_, 27, 47), week)
    zet(dr, D_, nm, c, 36 * s, 'hold', f(FS, round(26 * s)), SCHUIM)
    zet(dr, D_, nm, c, 64 * s, 'press START to breathe', f(FM, round(16 * s)), WIT)
    zet(dr, D_, nm, c, 76 * s, '1:45', f(FS, round(80 * s)), WIT)
    zet(dr, D_, nm, c, 162 * s, '61 bpm · round 2', f(FM, round(16 * s)), WIT)
    noteer('hold', kam=30, dier=dict(x=pos[0], y=pos[1], maat_260=27, maat_454=47, waar='thuis'),
           regels=[dict(tekst='hold', y=36, maat=26), dict(tekst='press START to breathe', y=64, maat=16),
                   dict(tekst='timer', y=76, maat=80), dict(tekst='bpm · round', y=162, maat=16)], planten='p')
    return rond(im), nm

def eind(D_, w, week):
    s = D_ / 260; c = D_ // 2; L = NIEUW; im, dr = basis(D_, L['zee'], w, week); nm = f'eind-{w["dier"]}-{D_}'
    d = D[w['nr']]; m = maat_in_vak(d, round(L['vw'] * s), round(L['vh'] * s)); _, _, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round((L['vak'][0] + L['vak'][1]) / 2 * s - oy), m)
    zet(dr, D_, nm, c, L['kop'] * s - 4 * s, '3 rounds done', f(FS, round(25 * s)), SCHUIM)
    zet(dr, D_, nm, c, L['tijd'] * s - 4 * s, '1:20   1:45   1:58', f(FS, round(24 * s)), WIT)
    zet(dr, D_, nm, c, L['naam'] * s - 5 * s, f'new friend: {w["dier"]}', f(FS, round(24 * s)), GEEL)
    stippen(dr, c, L['stip'] * s, 3, 1, max(2, round(3 * s)), round(12 * s))
    zet(dr, D_, nm, c, L['regel'] * s, '4 weeks in a row', f(FM, round(15 * s)), WIT)
    noteer('eind', kam=L['zee'], dier=dict(vak=[c * 0 + 130 - L['vw'] // 2, L['vak'][0], L['vw'], L['vh']], waar='grootste maat in vak (blad v13)'),
           regels=[dict(tekst='kop', y=L['kop'] - 4, maat=25), dict(tekst='tijden', y=L['tijd'] - 4, maat=24),
                   dict(tekst='naam', y=L['naam'] - 5, maat=24), dict(tekst='stippen (midden)', y=L['stip']),
                   dict(tekst='weekregel', y=L['regel'], maat=15)], planten='p')
    return rond(im), nm

def menu(D_, w, week):
    s = D_ / 260; c = D_ // 2; im, dr = basis(D_, 176, w, week); nm = f'menu-{w["dier"]}-{D_}'
    pos = thuis(dr, w, D_, M(D_, 27, 47), week)
    zet(dr, D_, nm, c, 26 * s, 'Ebb', f(FS, round(28 * s)), SCHUIM)
    for y, t in ((62, 'Rounds'), (104, 'Calm 4-7-8')):
        dr.rounded_rectangle([c - 75 * s, y * s, c + 75 * s, (y + 34) * s], radius=17 * s, outline=LICHT, width=max(2, round(2 * s)), fill=NACHT)
        zet(dr, D_, nm, c, (y + 5) * s, t, f(FS, round(22 * s)), WIT)
    zet(dr, D_, nm, c, 146 * s, 'Sea log  ·  Settings  ·  Today', f(FM, round(16 * s)), LICHT)
    noteer('menu', kam=176, dier=dict(x=pos[0], y=pos[1], maat_260=27, maat_454=47, waar='thuis'),
           regels=[dict(tekst='Ebb', y=26, maat=28), dict(tekst='pil Rounds', y=62, hoog=34), dict(tekst='pil Calm', y=104, hoog=34),
                   dict(tekst='menuregel', y=146, maat=16)], planten='p')
    return rond(im), nm

def sealog(D_, w, week):
    s = D_ / 260; c = D_ // 2; im, dr = basis(D_, 80, w, week); nm = f'sealog-{w["dier"]}-{D_}'
    d = D[w['nr']]; m = maat_in_vak(d, round(96 * s), round(70 * s)); _, _, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round(124 * s - oy), m)
    zet(dr, D_, nm, c, 24 * s, w['dier'], f(FS, round(26 * s)), SCHUIM)
    zet(dr, D_, nm, c, 52 * s, f'friend {w["nr"] + 1} of 24', f(FM, round(15 * s)), WIT)
    zet(dr, D_, nm, c, 166 * s, 'START: swims with you', f(FM, round(16 * s)), GEEL)
    noteer('sealog', kam=80, dier=dict(vak=[82, 89, 96, 70], midden_y=124, waar='grootste maat in vak 96 x 70'),
           regels=[dict(tekst='naam', y=24, maat=26), dict(tekst='friend x of 24', y=52, maat=15),
                   dict(tekst='START: swims with you', y=166, maat=16)], planten='p')
    return rond(im), nm

def maak_alle(D_, w, week):
    return [lambda: adem(D_, w, True, week), lambda: adem(D_, w, False, week), lambda: hold(D_, w, week),
            lambda: eind(D_, w, week), lambda: menu(D_, w, week), lambda: sealog(D_, w, week)]

def rij_beeld(rr, D_):
    st = D_ + 10; ov = Image.new('RGB', (len(rr[0]) * st + 10, len(rr) * st + 10), (30, 30, 30))
    for r, rij in enumerate(rr):
        for i, im in enumerate(rij): ov.paste(im, (10 + i * st, 10 + r * st))
    return ov

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    for w in WERELDEN:
        for i in w['items']:
            assert all(int(i['kleur'][k:k + 2], 16) in MIP for k in (2, 4, 6)), (w['dier'], i['kleur'])
            assert len(i['p']) <= 64 and (i['p2'] is None or len(i['p2']) == len(i['p']))
            assert min(y for _, y in i['p'] + (i['p2'] or [])) >= STROOK, (w['dier'], i['p'])
        assert punten(w) <= 120, (w['dier'], punten(w))
    rijen = {260: [], 454: []}; meting = []; vreemd = 0; botsing = []
    for D_ in (260, 454):
        for w in WERELDEN:
            rij = []
            for maak in maak_alle(D_, w, 4):
                TEKSTVAK.clear(); im, nm = maak(); vak = list(TEKSTVAK); im.save(os.path.join(uit, nm + '.png')); rij.append(im)
                oud = V.tekst; V.tekst = lambda *a, **k: None; TEKSTVAK.clear(); kaal, _ = maak(); V.tekst = oud
                meting += meet(kaal, vak); vreemd += pixeltoets(kaal)
                for i in range(len(vak)):
                    for j in range(i + 1, len(vak)):
                        if ImageChops.multiply(vak[i][2].filter(ImageFilter.MaxFilter(5)), vak[j][2]).getbbox():
                            botsing.append((nm, vak[i][1], vak[j][1]))
            rijen[D_].append(rij)
    for D_, rr in rijen.items():
        ov = rij_beeld(rr, D_); ov.save(os.path.join(uit, f'werelden-{D_}-rij.png'))
        if D_ == 260: ov.resize((ov.width * 2, ov.height * 2), Image.NEAREST).save(os.path.join(uit, 'werelden-260-rij-2x.png'))
    # groei: menu op 260 bij week 0 tot 4, per wereld
    TEKSTVAK.clear()
    groei = [[menu(260, w, wk)[0] for wk in range(5)] for w in WERELDEN]
    g = rij_beeld(groei, 260); g.resize((g.width * 2, g.height * 2), Image.NEAREST).save(os.path.join(uit, 'groei-260-2x.png'))
    # ware grootte: hold van alle drie, adem-in krab, eind krab, sealog clownvis
    TEKSTVAK.clear()
    ware = [hold(260, w, 4)[0] for w in WERELDEN] + [adem(260, WERELDEN[0], True, 4)[0], eind(260, WERELDEN[1], 4)[0], sealog(260, WERELDEN[2], 4)[0]]
    rij_beeld([ware], 260).save(os.path.join(uit, 'ware-grootte-1x.png'))
    data = {'versie': 'werelden v1.3', 'eenheid': '1/260 D, y van boven; schaal x*D/260 afkappen',
            'strook_vanaf_y': STROOK,
            'lagen': 'teken op volgorde: lucht, water, stralen, kam, vlakken laag ver, vlakken laag midden, dier, voor_het_dier (laag voor)',
            'p2': 'tweede stand bij inademen (zelfde aantal punten); bij uitademen en inhouden p. Wissel alleen als de adem omslaat, niet vaker hertekenen.',
            'week': 'vlak verschijnt vanaf dit aantal gehaalde weekdoelen voor dit dier (0 = altijd); een gemiste week haalt niets weg',
            'lucht': {'maan': [{'kleur': c, 'x': x, 'y': y, 'r': r} for c, x, y, r in LUCHT], 'sterren_1px': STERREN,
                      'maan_waar': 'alleen waar lucht te zien is (adem uit, menu, eind, sea log); op hold dekt het water hem, dus het maanverhaal pas in de winkeltekst als het gebouwd is'},
            'kam': 'golf: y = top + 4/260 D * sin(x/D * 2pi * 2,5); schuim 00FFFF 2/260, band 00AAFF tot 5/260, water 0055AA',
            'stralen': {'kleur': STRAAL_KLEUR, 'top': 'kam + 8, alleen als dat boven 200 ligt', 'onder_y': 205, 'lijst': STRALEN,
                        'vorm': 'vierhoek (x_top, top), (x_top+breed, top), (x_onder+breed/2, 205), (x_onder, 205); gedeeld, geen werelddata'},
            'visjes': {'kleur': VIS_KLEUR, 'lijst': VISJES, 'waar': 'gedeeld, met het water getekend, alleen als de kam minstens 10 boven het visje staat (geen vliegende vissen)'},
            'schermen': SCHERMEN, 'werelden': []}
    for w in WERELDEN:
        def vl(lst): return [{'kleur': i['kleur'], 'p': [list(q) for q in i['p']], 'laag': i['laag'], 'week': i['week'],
                              **({'p2': [list(q) for q in i['p2']]} if i['p2'] else {})} for i in lst]
        data['werelden'].append({'dier': w['dier'], 'nr': w['nr'] + 1, 'plek': w['plek'], 'haak': w['haak'], 'punten': punten(w),
                                 'thuis': list(w['thuis']), 'details_per_week': w['details'], 'aankomst': w['aankomst'], 'vertrek': w['vertrek'],
                                 'vlakken': vl([i for i in w['items'] if i['laag'] != 'voor']),
                                 'voor_het_dier': vl([i for i in w['items'] if i['laag'] == 'voor'])})
    json.dump(data, open(os.path.join(uit, 'ebb-werelden-v13-data.json'), 'w'), indent=1)
    with open(os.path.join(uit, 'contrast.txt'), 'w') as fo:
        fo.write('scherm | tekst | laagste contrast | aantal achtergrondkleuren onder de inkt\n')
        for m_ in sorted(meting, key=lambda r: r[2]): fo.write(' | '.join(str(v) for v in m_) + '\n')
    with open(os.path.join(uit, 'punten.txt'), 'w') as fo:
        for w in WERELDEN:
            fo.write(f"{w['dier']} ({w['plek']}): {punten(w)} punten, {len(w['items'])} vlakken, "
                     f"{sum(1 for i in w['items'] if i['p2'])} met p2, kleuren {len({i['kleur'] for i in w['items']})}\n")
        fo.write(f'teksten die elkaar raken (minder dan 3 px ertussen): {len(botsing)} {botsing}\n')
        fo.write(f'pixels buiten de 64 MIP-kleuren (alle schermen zonder letters): {vreemd}\n')
        fo.write(f'hoogste punt van alle werelden: y {min(y for w in WERELDEN for i in w["items"] for _, y in i["p"])} (strook vanaf {STROOK})\n')
    print(open(os.path.join(uit, 'punten.txt')).read()); print('laagste contrast', min(m[2] for m in meting))
    for m_ in sorted(meting, key=lambda r: r[2])[:6]: print(m_)
