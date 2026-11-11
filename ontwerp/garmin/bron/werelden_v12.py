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

# ---------------- werelden ----------------
def schildpad():
    z = [ver_rug()]
    z.append(it('0xFFFFAA', [(0, 228), (45, 222), (95, 226), (135, 221), (175, 225), (220, 219), (260, 225), (260, 260), (0, 260)]))
    z.append(it('0xAAAA55', [(66, 240), (80, 237), (92, 241), (80, 243)]))
    z += vlekjes([(118, 232, 6), (140, 246, 5)])
    for a, t, b, bu, c, wk in [((6, 234), (0, 120), 6, 7, '0x00AA55', 0), ((20, 234), (22, 140), 6, -6, '0x55AA00', 0),
                               ((16, 236), (34, 176), 4, 8, '0x005500', 0), ((40, 230), (48, 184), 4, 5, '0x55AA00', 0),
                               ((254, 232), (260, 124), 6, -7, '0x00AA55', 0), ((240, 232), (236, 140), 6, 6, '0x55AA00', 0),
                               ((244, 234), (226, 178), 4, -8, '0x005500', 0), ((122, 230), (118, 214), 3, -2, '0x55AA00', 2)]:
        z.append(zeegras(*a, *t, b, bu, c, week=wk))
    # de haak: een zandkasteel met vlaggetje (schildpadden graven met hun vinnen, deze bouwt dus ook)
    z.append(it('0xFFAA55', [(181, 242), (181, 222), (200, 222), (200, 204), (212, 204), (212, 222), (231, 222), (231, 242)]))
    z.append(it('0xAA5500', [(202, 242), (202, 232), (206, 228), (210, 232), (210, 242)]))     # deurtje
    z.append(it('0xFFFFFF', [(205, 201), (207, 201), (207, 184), (205, 184)]))                # stokje
    z.append(it('0xFF0000', [(207, 184), (222, 188), (207, 194)]))                           # vlag
    # groeit met trouw: week 1 schelp, week 2 extra spriet (hierboven), week 3 de hap uit de brede spriet, week 4 zeester
    z.append(it('0xFFAAAA', [(106, 237), (116, 229), (126, 237), (116, 240)], week=1))
    z.append(it('0x00AA55', [(52, 232), (56, 206), (60, 198), (66, 202), (62, 206), (62, 212), (66, 216), (64, 232)],
                p2=[(52, 232), (58, 206), (64, 198), (70, 202), (66, 206), (64, 212), (68, 216), (64, 232)], week=3))
    z.append(it('0xFF5500', [(151, 233), (154, 225), (157, 233), (165, 235), (159, 238), (160, 246), (154, 241), (148, 246),
                             (149, 238), (143, 235)], week=4))
    return dict(dier='Turtle', nr=3, plek='zeegrasweide', items=z, thuis=(92, 214),
                haak='een zandkasteel met rood vlaggetje op de bodem: de schildpad graaft toch al, dus hij bouwt ook',
                details={1: 'schelp', 2: 'extra spriet', 3: 'hap uit de brede spriet', 4: 'zeester'})

def krab():
    z = [ver_rug()]
    z.append(it('0xFFFFAA', [(0, 230), (60, 224), (130, 227), (200, 223), (260, 229), (260, 260), (0, 260)]))
    z.append(it('0xAAAA55', [(40, 248), (90, 243), (140, 248), (90, 251)]))
    z += vlekjes([(196, 246, 6)])
    # linker kei: donkere kant 555555, grote lichte kant AAAAAA, paarse vlek 5555AA
    z.append(it('0x555555', [(0, 126), (16, 120), (32, 134), (36, 170), (52, 198), (60, 232), (0, 236)]))
    z.append(it('0xAAAAAA', [(0, 130), (16, 122), (30, 136), (32, 168), (20, 178), (0, 160)]))
    z.append(it('0x5555AA', [(10, 196), (20, 190), (26, 198), (16, 204)]))
    z.append(it('0x5555AA', [(46, 232), (58, 210), (78, 206), (92, 220), (94, 234)]))
    z.append(it('0x555555', [(260, 132), (244, 126), (228, 140), (224, 172), (210, 204), (206, 232), (260, 236)]))
    z.append(it('0xAAAAAA', [(260, 134), (244, 128), (230, 140), (228, 170), (238, 182), (260, 166)]))
    z.append(it('0x5555AA', [(238, 204), (248, 198), (254, 206), (244, 212)]))
    z.append(it('0x5555AA', [(214, 233), (200, 218), (184, 220), (178, 234)]))
    # de grap: teenslipper van boven, zool 40 x 14, 15 graden schuin, V-bandje vanaf de teen
    zool = [(-20, 0), (-15, -6), (-2, -5), (14, -7), (21, 0), (14, 7), (-2, 5), (-15, 6)]
    rand = [(x * 1.12, y * 1.25) for x, y in zool]
    band = [(13, -1), (13, 1), (-3, 6), (-5, 5), (10, 0), (-5, -5), (-3, -6)]
    z.append(it('0xAA0055', draai(rand, 128, 238, -15)))
    z.append(it('0xFF55AA', draai(zool, 128, 238, -15)))
    z.append(it('0xFFFFFF', draai(band, 128, 238, -15)))
    # groeit met trouw
    z.append(it('0xFFAAAA', [(166, 241), (176, 231), (186, 241), (176, 244)], week=1))              # schelp
    z.append(it('0xFFFFFF', [(222, 149), (228, 142), (234, 149), (228, 152)], week=2))               # zeepok op de kei
    z.append(it('0xFF5500', [(66, 244), (76, 238), (86, 244), (76, 249)], week=3))                   # oranje steentje
    z.append(it('0xAA0055', [(191, 250), (204, 245), (220, 250), (204, 255)], week=4))               # roze steentje (past bij de slipper)
    return dict(dier='Crab', nr=4, plek='rotsen met verloren slipper', items=z, thuis=(184, 214),
                haak='een verloren roze teenslipper; de krab blijft op de bodem ernaast en blaast belletjes',
                details={1: 'schelp', 2: 'zeepok op de kei', 3: 'oranje steentje', 4: 'roze steentje'})

def clownvis():
    z = [ver_rug('0x000055')]
    z.append(it('0xAA5555', [(0, 226), (50, 222), (110, 228), (160, 222), (210, 226), (260, 220), (260, 260), (0, 260)]))
    z.append(it('0xFFAA55', [(84, 240), (100, 235), (120, 240), (100, 244)]))
    z.append(it('0xFFAA55', [(150, 236), (166, 232), (180, 237), (166, 240)]))
    z += vlekjes([(130, 232, 5)], '0xFFAAAA')
    z.append(it('0xAA0055', [(0, 236), (4, 206), (64, 206), (70, 236)]))
    xs = [-10, 2, 12, 22, 32, 44, 56, 70]; tops = [134, 146, 158, 166, 176, 184, 196]
    z.append(it('0xFF55AA', vinger(xs, 212, tops), p2=vinger(xs, 212, tops, golf=4)))
    # voor het dier: alleen de twee voorste vingers (oog en banden van de vis blijven vrij)
    voor = [it('0xFFAAFF', [(18, 216), (22, 196), (28, 216)], 'voor', [(18, 216), (25, 196), (28, 216)]),
            it('0xFFAAFF', [(54, 216), (58, 200), (64, 216)], 'voor', [(54, 216), (61, 200), (64, 216)])]
    # zwaaiende arm met knik en drie vingertoppen; top op 190, dus 10/260 onder de bpm-regel (onderkant 180)
    arm = [(58, 216), (60, 204), (68, 198), (74, 194), (72, 190), (76, 188), (78, 192), (81, 189), (84, 192), (82, 196),
           (76, 202), (68, 208), (68, 216)]
    z.append(it('0xFFAAFF', arm, p2=[(x + (0 if y > 205 else 3), y) for x, y in arm]))
    z.append(it('0xFFFFAA', [(71, 191), (73, 188), (75, 191)]))
    z.append(it('0xFFFFAA', [(77, 189), (79, 186), (81, 189)]))
    z.append(it('0xAA55FF', [(260, 128), (238, 136), (226, 172), (212, 206), (224, 226), (260, 230)]))
    z.append(it('0x550055', [(246, 222), (240, 160), (243, 160), (250, 222)]))
    z.append(it('0xFFAA00', [(196, 228), (193, 212), (188, 204), (191, 202), (197, 208), (200, 198), (204, 199), (202, 214), (204, 228)]))
    z.append(it('0xFFFFFF', [(148, 243), (154, 236), (160, 243), (154, 246)], week=1))     # schelp
    z.append(it('0xFF5500', [(230, 194), (236, 187), (242, 194), (236, 200)], week=2))     # zeesterretje op de waaier
    z.append(it('0xAA55FF', [(108, 240), (114, 230), (120, 240)], week=3))                 # paars koraaltje
    z.append(it('0x55FFFF', [(174, 237), (180, 230), (186, 237), (180, 240)], week=4))     # blauw steentje
    return dict(dier='Clownfish', nr=7, plek='anemoon met zwaaiende arm', items=z + voor, thuis=(44, 188),
                haak='hij zit thuis in zijn anemoon, en één arm zwaait met drie vingers naar hem',
                details={1: 'schelp', 2: 'zeesterretje', 3: 'paars koraaltje', 4: 'blauw steentje'})

WERELDEN = [schildpad(), krab(), clownvis()]
# lichtstralen: gedeeld, geen werelddata; top volgt de kam, onderkant y 205, alleen aan de randen
STRALEN = [dict(x_top=14, x_onder=46, breed=8), dict(x_top=40, x_onder=64, breed=4), dict(x_top=230, x_onder=206, breed=8)]
STRAAL_KLEUR = '0x0055FF'
VIS_KLEUR = '0x0000AA'
VISJES = [[(26, 136), (36, 131), (43, 136), (48, 131), (48, 141), (36, 141)],
          [(234, 128), (224, 123), (217, 128), (212, 123), (212, 133), (224, 133)]]

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
    m = M(D_, 21, 37)
    if w['dier'] == 'Turtle' and inn: pos = thuis(dr, w, D_, m, week, inn, (204, top + 4))     # kop boven water: lucht happen
    elif w['dier'] == 'Clownfish' and inn: pos = thuis(dr, w, D_, m, week, inn, (200, 150))    # zwemt uit
    else: pos = thuis(dr, w, D_, m, week, inn, (w['thuis'][0], w['thuis'][1] - (6 if inn else 0)))  # drijft iets op bij inademen
    zet(dr, D_, nm, c, 34 * s, 'breathe in' if inn else 'breathe out', f(FS, round(25 * s)), WIT if inn else SCHUIM)
    zet(dr, D_, nm, c, 62 * s, 'round 2 · 18 left', f(FM, round(16 * s)), WIT)
    yc = 104 if inn else 92
    zet(dr, D_, nm, c, yc * s, '12', f(FS, round(70 * s)), WIT)
    noteer(f'adem-{"in" if inn else "uit"}', kam=top, kam_beweegt='lineair tussen 92 (in) en 186 (uit) over de adem',
           dier=dict(x=pos[0], y=pos[1], maat_260=21, maat_454=37, waar='Turtle: (204, kam+4) bij in; Clownfish: (200,150) bij in; anders thuis, bij in 6 hoger'),
           regels=[dict(tekst='breathe in / breathe out', y=34, maat=25), dict(tekst='round 2 · 18 left', y=62, maat=16),
                   dict(tekst='tel', y=yc, maat=70)], planten='p2' if inn else 'p')
    return rond(im), nm

def hold(D_, w, week):
    s = D_ / 260; c = D_ // 2; im, dr = basis(D_, 30, w, week); nm = f'hold-{w["dier"]}-{D_}'
    pos = thuis(dr, w, D_, M(D_, 20, 35), week)
    zet(dr, D_, nm, c, 36 * s, 'hold', f(FS, round(26 * s)), SCHUIM)
    zet(dr, D_, nm, c, 64 * s, 'press START to breathe', f(FM, round(16 * s)), WIT)
    zet(dr, D_, nm, c, 76 * s, '1:45', f(FS, round(80 * s)), WIT)
    zet(dr, D_, nm, c, 162 * s, '61 bpm · round 2', f(FM, round(16 * s)), WIT)
    noteer('hold', kam=30, dier=dict(x=pos[0], y=pos[1], maat_260=20, maat_454=35, waar='thuis'),
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
    pos = thuis(dr, w, D_, M(D_, 20, 35), week)
    zet(dr, D_, nm, c, 26 * s, 'Ebb', f(FS, round(28 * s)), SCHUIM)
    for y, t in ((62, 'Rounds'), (104, 'Calm 4-7-8')):
        dr.rounded_rectangle([c - 75 * s, y * s, c + 75 * s, (y + 34) * s], radius=17 * s, outline=LICHT, width=max(2, round(2 * s)), fill=NACHT)
        zet(dr, D_, nm, c, (y + 5) * s, t, f(FS, round(22 * s)), WIT)
    zet(dr, D_, nm, c, 146 * s, 'Sea log  ·  Settings  ·  Today', f(FM, round(16 * s)), LICHT)
    noteer('menu', kam=176, dier=dict(x=pos[0], y=pos[1], maat_260=20, maat_454=35, waar='thuis'),
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
    data = {'versie': 'werelden v1.2', 'eenheid': '1/260 D, y van boven; schaal x*D/260 afkappen',
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
                                 'thuis': list(w['thuis']), 'details_per_week': w['details'],
                                 'vlakken': vl([i for i in w['items'] if i['laag'] != 'voor']),
                                 'voor_het_dier': vl([i for i in w['items'] if i['laag'] == 'voor'])})
    json.dump(data, open(os.path.join(uit, 'ebb-werelden-v12-data.json'), 'w'), indent=1)
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
