# Blad werelden v1 (Mila, run 39, 11 nov nacht): elk dier zijn eigen stukje zee (besluit Thijs 11 nov 23:13).
# Eerst drie werelden helemaal af: schildpad (zeegrasweide), krab (rotsen met verloren slipper), clownvis (anemoon).
# Regels: alleen vlakken (fillPolygon) en cirkels (fillCircle), alleen de 64 MIP-kleuren (elke kleur 0, 55, AA of FF),
# hoogstens 120 punten per wereld, wereld onderin en aan de randen, achter tekst rustig (contrast gemeten).
# Coordinaten in 1/260 D, y van boven; op een ander horloge x D/260 (gehele getallen, afkappen zoals bij de dieren).
#   python3 werelden_v1.py <uitmap>
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from blad_v9 import rond, tekst, stippen, f, FM, FS, SCHUIM, LICHT, MIDDEN, DIEP, NACHT, WIT, D
from blad_v13 import kader, maat_in_vak, NIEUW
from PIL import Image, ImageDraw
GEEL = (255, 255, 170)
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')

def hx(s): s = int(s, 16); return ((s >> 16) & 255, (s >> 8) & 255, s & 255)

# ---------------- de werelden (data) ----------------
def spriet(x0, y0, x1, y1, b, buig, hap=False):
    """Zeegrasspriet: 4 punten (5 met hap). Onder breed b, punt bovenaan, buig = zijwaartse knik halverwege."""
    mx, my = (x0 + x1) / 2 + buig, (y0 + y1) / 2
    if hap:   # hapje uit de rechterkant: de schildpad eet zeegras (echt zo, groene zeeschildpad)
        return [(x0 - b, y0), (mx - b / 2, my), (x1, y1), (mx + 1, my + 4), (x0 + b, y0)]
    return [(x0 - b, y0), (mx - b / 2, my), (x1, y1), (x0 + b, y0)]

def vinger(punten_x, basis, top, golf=0):
    """Anemoon: één veelhoek met vingers (zigzag), basis-y onder, top-y van elke vinger."""
    p = [(punten_x[0], basis)]
    for i in range(len(punten_x) - 1):
        xa, xb = punten_x[i], punten_x[i + 1]
        p.append(((xa + xb) / 2 + golf, top[i]))
        p.append((xb, basis - 10))
    p[-1] = (punten_x[-1], basis)
    return p

def wereld_schildpad():
    z = []
    zand = [(0, 228), (45, 222), (95, 226), (135, 221), (175, 225), (220, 219), (260, 225), (260, 260), (0, 260)]
    z.append(('0xAAAA55', zand))
    z.append(('0xFFFFAA', [(70, 236), (100, 232), (128, 237), (100, 239)]))     # ribbel in het zand
    z.append(('0xFFFFAA', [(150, 244), (178, 240), (204, 245), (178, 247)]))
    # sprieten links (basis, top, breedte, buig, kleur)
    links = [((8, 232), (2, 150), 5, 6, '0x00AA55'), ((22, 232), (14, 168), 5, -5, '0x55AA00'),
             ((34, 230), (40, 178), 4, 5, '0x00AA55'), ((46, 228), (58, 196), 4, 4, '0x55AA00'),
             ((16, 234), (30, 186), 4, 8, '0x005500')]
    rechts = [((252, 230), (258, 152), 5, -6, '0x00AA55'), ((238, 230), (246, 166), 5, 5, '0x55AA00'),
              ((226, 228), (218, 180), 4, -5, '0x00AA55'), ((214, 226), (202, 198), 4, -3, '0x55AA00'),
              ((244, 232), (228, 188), 4, -8, '0x005500')]
    for i, (a, t, b, bu, c) in enumerate(links + rechts):
        z.append((c, spriet(a[0], a[1], t[0], t[1], b, bu, hap=(i == 6))))
    z.append(('0x55AA00', spriet(112, 230, 108, 223, 3, 2)))                   # twee korte in het midden, onder de tekst
    z.append(('0x00AA55', spriet(150, 229, 154, 223, 3, -2)))
    return 'Turtle', 'zeegrasweide', z, [('0xFFFFFF', 64, 214, 2), ('0xFFFFFF', 70, 205, 1)]

def wereld_krab():
    z = []
    zand = [(0, 230), (60, 224), (130, 227), (200, 223), (260, 229), (260, 260), (0, 260)]
    z.append(('0xFFFFAA', zand))
    z.append(('0xAAAA55', [(40, 246), (90, 241), (140, 246), (90, 249)]))
    # rotsen links: grote kei, kleine kei, lichtkant
    z.append(('0x555555', [(0, 168), (22, 160), (44, 172), (56, 200), (60, 232), (0, 236)]))
    z.append(('0xAAAAAA', [(4, 168), (22, 162), (36, 170), (20, 172)]))
    z.append(('0x5555AA', [(48, 232), (58, 212), (76, 208), (90, 222), (92, 234)]))
    z.append(('0xAAAAFF', [(60, 214), (74, 210), (80, 216), (68, 216)]))
    # rotsen rechts
    z.append(('0x555555', [(260, 176), (240, 170), (222, 182), (210, 206), (206, 232), (260, 236)]))
    z.append(('0xAAAAAA', [(256, 176), (240, 172), (228, 180), (244, 181)]))
    z.append(('0x5555AA', [(214, 233), (200, 218), (186, 220), (180, 234)]))
    # de grap: een verloren slipper op het zand (roze zool, witte band)
    z.append(('0xFF55AA', [(112, 239), (122, 233), (146, 232), (158, 236), (150, 243), (120, 244)]))
    z.append(('0xFFFFFF', [(124, 237), (138, 226), (152, 235), (148, 235), (138, 230), (128, 238)]))
    # schelp en zeepok
    z.append(('0xFFAAAA', [(170, 240), (176, 234), (182, 240), (176, 242)]))
    z.append(('0xFFAA55', [(30, 200), (36, 196), (40, 202), (34, 205)]))
    return 'Crab', 'rotsen met verloren slipper', z, [('0x00FFFF', 236, 158, 2), ('0x00FFFF', 242, 150, 1)]

def wereld_clownvis():
    z = []
    rif = [(0, 226), (50, 222), (110, 228), (160, 222), (210, 226), (260, 220), (260, 260), (0, 260)]
    z.append(('0x550055', rif))
    z.append(('0xAA5555', [(80, 240), (100, 234), (124, 240), (100, 244)]))
    # anemoon links: voet, achterste vingers (donker), voorste vingers (licht), toppen via de lichte laag
    z.append(('0xAA0055', [(2, 236), (8, 206), (52, 206), (58, 236)]))
    z.append(('0xFF55AA', vinger([-6, 6, 18, 30, 42, 54, 64], 212, [162, 170, 176, 182, 190, 200])))
    z.append(('0xFFAAFF', vinger([0, 14, 28, 40, 52, 62], 214, [178, 186, 190, 196, 204], golf=2)))
    # de haak: één vinger zwaait (staat hoger en buigt naar het midden, naar de vis)
    z.append(('0xFFAAFF', [(58, 212), (64, 196), (70, 186), (76, 186), (68, 198), (64, 214)]))
    # koraal rechts: waaier in paars en geel takje
    z.append(('0xAA55FF', [(260, 172), (238, 178), (220, 192), (212, 206), (224, 226), (260, 230)]))
    z.append(('0x550055', [(244, 222), (238, 190), (241, 190), (248, 222)]))         # nerf in de waaier
    z.append(('0xFFAA00', [(196, 228), (193, 212), (188, 204), (191, 202), (197, 208), (200, 198), (204, 199), (202, 214), (204, 228)]))
    return 'Clownfish', 'anemoon met zwaaiende arm', z, [('0xFFFFFF', 236, 190, 2), ('0xFFFFFF', 230, 181, 1)]

WERELDEN = [wereld_schildpad(), wereld_krab(), wereld_clownvis()]
DIER_NR = {'Turtle': 3, 'Crab': 4, 'Clownfish': 7}

def punten(w): return sum(len(p) for _, p in w[2]) + len(w[3])

def teken_wereld(dr, w, D_):
    s = D_ / 260
    for c, p in w[2]:
        dr.polygon([(int(x * D_ // 260) if x >= 0 else -int(-x * D_ // 260), int(y * D_ // 260)) for x, y in p], fill=hx(c))
    for c, x, y, r in w[3]:
        rr = max(1, round(r * s)); X, Y = x * D_ // 260, y * D_ // 260
        dr.ellipse([X - rr, Y - rr, X + rr, Y + rr], outline=hx(c), width=max(1, round(s)))

# ---------------- zee ----------------
def water(im, top, D_, lucht=NACHT):
    """Lucht nachtblauw (geen zwart meer), zee vlak MIDDEN met schuimkam en een diepere band; geen verloop (MIP)."""
    dr = ImageDraw.Draw(im); dr.rectangle([0, 0, D_, D_], fill=lucht)
    a = max(2, D_ // 90)
    for x in range(D_):
        yk = top + int(a * math.sin(x / D_ * 2 * math.pi * 3))
        dr.line([(x, yk), (x, D_)], fill=MIDDEN)
        dr.line([(x, yk), (x, yk + max(2, D_ // 100))], fill=SCHUIM)
    y0 = top + int((D_ - top) * 0.55)
    for x in range(D_):
        yk = max(y0, top + D_ // 12) + int(a * math.sin(x / D_ * 2 * math.pi * 2 + 1))
        dr.line([(x, yk), (x, D_)], fill=DIEP)

# ---------------- schermen ----------------
TEKSTVAK = []   # (scherm, tekst, bbox, kleur) voor de contrastmeting

def zet(dr, D_, naam, x, y, s, font, c):
    """Tekst zetten en de inkt (1 px verdikt) onthouden voor de contrastmeting."""
    w = dr.textlength(s, font=font)
    mk = Image.new('L', (D_, D_), 0); ImageDraw.Draw(mk).text((x - w / 2, y), s, font=font, fill=255, anchor='la')
    from PIL import ImageFilter
    TEKSTVAK.append((naam, s, mk.filter(ImageFilter.MaxFilter(3)), c)); tekst(dr, x, y, s, font, c)

def scherm_adem(D_, w, inn):
    s = D_ / 260; c = D_ // 2; im = Image.new('RGB', (D_, D_))
    top = round((92 if inn else 186) * s); water(im, top, D_)
    dr = ImageDraw.Draw(im); teken_wereld(dr, w, D_)
    nm = f'adem-{"in" if inn else "uit"}-{w[0]}-{D_}'
    zet(dr, D_, nm, c, 34 * s, 'breathe in' if inn else 'breathe out', f(FS, round(25 * s)), SCHUIM if not inn else WIT)
    zet(dr, D_, nm, c, 62 * s, 'round 2 · 18 left', f(FM, round(16 * s)), WIT)
    zet(dr, D_, nm, c, (104 if inn else 92) * s, '12', f(FS, round(70 * s)), WIT)
    d = D[DIER_NR[w[0]]]; m = 21 if D_ < 300 else 37
    _, hh, ox, oy = kader(d, m)
    h.teken(dr, d, round(c + 74 * s - ox), round(top + 3 * s - oy), m)   # dier dobbert in de kam, rechts van het cijfer
    return rond(im), nm

def scherm_hold(D_, w):
    s = D_ / 260; c = D_ // 2; im = Image.new('RGB', (D_, D_))
    water(im, round(30 * s), D_); dr = ImageDraw.Draw(im); teken_wereld(dr, w, D_)
    nm = f'hold-{w[0]}-{D_}'
    zet(dr, D_, nm, c, 36 * s, 'hold', f(FS, round(26 * s)), SCHUIM)
    zet(dr, D_, nm, c, 64 * s, 'press START to breathe', f(FM, round(16 * s)), WIT)
    zet(dr, D_, nm, c, 78 * s, '1:45', f(FS, round(88 * s)), WIT)
    d = D[DIER_NR[w[0]]]; m = 20 if D_ < 300 else 35; _, _, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round(187 * s - oy), m)
    zet(dr, D_, nm, c, 202 * s, '61 bpm · round 2', f(FM, round(16 * s)), WIT)
    return rond(im), nm

def scherm_eind(D_, w):
    s = D_ / 260; c = D_ // 2; L = NIEUW; im = Image.new('RGB', (D_, D_))
    water(im, round(L['zee'] * s), D_); dr = ImageDraw.Draw(im); teken_wereld(dr, w, D_)
    nm = f'eind-{w[0]}-{D_}'
    zet(dr, D_, nm, c, L['kop'] * s - 4 * s, '3 rounds done', f(FS, round(25 * s)), SCHUIM)
    zet(dr, D_, nm, c, L['tijd'] * s - 4 * s, '1:20   1:45   1:58', f(FS, round(24 * s)), WIT)
    d = D[DIER_NR[w[0]]]; m = maat_in_vak(d, round(L['vw'] * s), round(L['vh'] * s)); _, _, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round((L['vak'][0] + L['vak'][1]) / 2 * s - oy), m)
    zet(dr, D_, nm, c, L['naam'] * s - 5 * s, f'new friend: {w[0]}', f(FS, round(24 * s)), GEEL)
    stippen(dr, c, L['stip'] * s, 3, 1, max(2, round(3 * s)), round(12 * s))
    zet(dr, D_, nm, c, L['regel'] * s, '4 weeks in a row', f(FM, round(15 * s)), WIT)
    return rond(im), nm

def pil(dr, c, y, b, hh, tekst_, s, font, nm, D_):
    dr.rounded_rectangle([c - b / 2, y, c + b / 2, y + hh], radius=hh / 2, outline=LICHT, width=max(2, round(2 * s)), fill=NACHT)
    zet(dr, D_, nm, c, y + hh / 2 - 12 * s, tekst_, font, WIT)

def scherm_menu(D_, w):
    s = D_ / 260; c = D_ // 2; im = Image.new('RGB', (D_, D_))
    water(im, round(184 * s), D_); dr = ImageDraw.Draw(im); teken_wereld(dr, w, D_)
    nm = f'menu-{w[0]}-{D_}'
    zet(dr, D_, nm, c, 26 * s, 'Ebb', f(FS, round(28 * s)), SCHUIM)
    pil(dr, c, 62 * s, 150 * s, 34 * s, 'Rounds', s, f(FS, round(22 * s)), nm, D_)
    pil(dr, c, 104 * s, 150 * s, 34 * s, 'Calm 4-7-8', s, f(FS, round(22 * s)), nm, D_)
    zet(dr, D_, nm, c, 146 * s, 'Sea log  ·  Settings  ·  Today', f(FM, round(16 * s)), LICHT)
    d = D[DIER_NR[w[0]]]; m = 22 if D_ < 300 else 38; _, hh, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round(186 * s - oy), m)
    return rond(im), nm

def scherm_sealog_dier(D_, w, nr_in_log):
    s = D_ / 260; c = D_ // 2; im = Image.new('RGB', (D_, D_))
    water(im, round(70 * s), D_); dr = ImageDraw.Draw(im); teken_wereld(dr, w, D_)
    nm = f'sealog-{w[0]}-{D_}'
    zet(dr, D_, nm, c, 26 * s, w[0], f(FS, round(26 * s)), SCHUIM)
    zet(dr, D_, nm, c, 52 * s, f'friend {nr_in_log} of 24', f(FM, round(15 * s)), WIT)
    d = D[DIER_NR[w[0]]]; m = maat_in_vak(d, round(96 * s), round(74 * s)); _, _, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round(120 * s - oy), m)
    zet(dr, D_, nm, c, 164 * s, 'START: swims with you', f(FM, round(16 * s)), GEEL)
    return rond(im), nm

# ---------------- contrast ----------------
def lum(c):
    def k(v):
        v /= 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * k(c[0]) + 0.7152 * k(c[1]) + 0.0722 * k(c[2])

def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)

def meet(achter, vakken):
    """Laagste contrast tussen tekstkleur en elke achtergrondpixel onder het tekstvak (scherm zonder tekst)."""
    uit = []
    for nm, s, mk, c in vakken:
        kl = set(); bb = mk.getbbox() or (0, 0, 0, 0)
        for y in range(bb[1], bb[3]):
            for x in range(bb[0], bb[2]):
                if mk.getpixel((x, y)): kl.add(achter.getpixel((x, y)))
        laag = min(contrast(c, k) for k in kl) if kl else 99
        uit.append((nm, s, round(laag, 1), len(kl)))
    return uit

def mip_ok(w):
    return all(all(int(c[i:i + 2], 16) in (0, 85, 170, 255) for i in (2, 4, 6)) for c, _ in w[2])

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    data = {'versie': 'werelden v1', 'eenheid': '1/260 D, y van boven; schaal x*D/260 afkappen', 'werelden': []}
    for w in WERELDEN:
        assert mip_ok(w), w[0]
        data['werelden'].append({'dier': w[0], 'nr': DIER_NR[w[0]] + 1, 'plek': w[1], 'punten': punten(w),
            'vlakken': [{'kleur': c, 'p': [[round(x), round(y)] for x, y in p]} for c, p in w[2]],
            'cirkels_rand': [{'kleur': c, 'x': x, 'y': y, 'r': r} for c, x, y, r in w[3]]})
    json.dump(data, open(os.path.join(uit, 'ebb-werelden-v1-data.json'), 'w'), indent=1)
    rijen = {260: [], 454: []}; meting = []
    for D_ in (260, 454):
        for w in WERELDEN:
            rij = []
            for maak in (lambda: scherm_adem(D_, w, True), lambda: scherm_adem(D_, w, False), lambda: scherm_hold(D_, w),
                         lambda: scherm_eind(D_, w), lambda: scherm_menu(D_, w), lambda: scherm_sealog_dier(D_, w, DIER_NR[w[0]] + 1)):
                TEKSTVAK.clear(); im, nm = maak(); vak = list(TEKSTVAK)
                im.save(os.path.join(uit, nm + '.png')); rij.append(im)
                # achtergrond zonder tekst: zelfde scherm opnieuw, tekst overschilderen kan niet, dus teken zonder letters
                import blad_v9; oud = globals()['tekst']
                globals()['tekst'] = lambda *a, **k: None
                TEKSTVAK.clear(); kaal, _ = maak(); globals()['tekst'] = oud
                meting += meet(kaal, vak)
            rijen[D_].append(rij)
    for D_, rr in rijen.items():
        st = D_ + 10; ov = Image.new('RGB', (6 * st + 10, len(rr) * st + 10), (30, 30, 30))
        for r, rij in enumerate(rr):
            for i, im in enumerate(rij): ov.paste(im, (10 + i * st, 10 + r * st))
        ov.save(os.path.join(uit, f'werelden-{D_}-rij.png'))
        if D_ == 260: ov.resize((ov.width * 2, ov.height * 2), Image.NEAREST).save(os.path.join(uit, 'werelden-260-rij-2x.png'))
    with open(os.path.join(uit, 'contrast.txt'), 'w') as fo:
        fo.write('scherm | tekst | laagste contrast | aantal achtergrondkleuren onder de tekst\n')
        for m_ in meting: fo.write(' | '.join(str(v) for v in m_) + '\n')
    with open(os.path.join(uit, 'punten.txt'), 'w') as fo:
        for w in WERELDEN: fo.write(f'{w[0]} ({w[1]}): {punten(w)} punten, {len(w[2])} vlakken, {len(w[3])} cirkels\n')
    print(open(os.path.join(uit, 'punten.txt')).read()); print('laagste contrast', min(m[2] for m in meting))
