# Blad werelden v1.1 (Mila, run 39): na de frisse keuring van v1 (5 van 10).
# Nieuw: maan en sterren in de nachtlucht (Ebb = eb, de maan trekt het water), golvende kam met lichte band,
# geen rechte diepe band meer, werelden aan de randen tot y 120, elk dier heeft een thuis en gedrag
# (schildpad komt boven om lucht te happen, krab blijft op de bodem en blaast belletjes, clownvis zit in zijn anemoon),
# grappen groter. Pixels worden getoetst: alleen MIP-kleuren buiten de letters.
#   python3 werelden_v11.py <uitmap>
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v1 as V
import horloge_sim as h
from werelden_v1 import spriet, vinger, hx, zet, TEKSTVAK, meet, mip_ok, D, kader, maat_in_vak, NIEUW, f, FM, FS, \
    SCHUIM, LICHT, MIDDEN, NACHT, WIT, GEEL, rond, stippen
from PIL import Image, ImageDraw

# ---------------- werelden ----------------
def schildpad():
    z = []
    z.append(('0xAAAA55', [(0, 228), (45, 222), (95, 226), (135, 221), (175, 225), (220, 219), (260, 225), (260, 260), (0, 260)]))
    z.append(('0xFFFFAA', [(70, 236), (100, 232), (128, 237), (100, 239)]))
    z.append(('0xFFFFAA', [(150, 244), (178, 240), (204, 245), (178, 247)]))
    sp = [((6, 234), (0, 118), 6, 7, '0x00AA55'), ((20, 234), (22, 140), 6, -6, '0x55AA00'),
          ((16, 236), (34, 176), 4, 8, '0x005500'), ((40, 230), (48, 182), 4, 5, '0x55AA00'),
          ((254, 232), (260, 122), 6, -7, '0x00AA55'), ((240, 232), (236, 140), 6, 6, '0x55AA00'),
          ((244, 234), (226, 178), 4, -8, '0x005500'), ((218, 228), (210, 186), 4, -4, '0x55AA00')]
    for a, t, b, bu, c in sp: z.append((c, spriet(a[0], a[1], t[0], t[1], b, bu)))
    # de hap: brede spriet vooraan links, met een duidelijke halve hap uit de rechterkant
    z.append(('0x00AA55', [(50, 232), (54, 206), (60, 196), (66, 200), (62, 204), (62, 212), (66, 216), (64, 232)]))
    z.append(('0x55AA00', spriet(112, 230, 108, 223, 3, 2)))
    z.append(('0x00AA55', spriet(150, 229, 154, 223, 3, -2)))
    return dict(dier='Turtle', nr=3, plek='zeegrasweide', vlak=z, voor=[], cirkels=[],
                thuis=(84, 214), haak='een spriet met een hap eruit: hij eet zeegras, en bij inademen komt hij boven om lucht te happen')

def krab():
    z = []
    z.append(('0xFFFFAA', [(0, 230), (60, 224), (130, 227), (200, 223), (260, 229), (260, 260), (0, 260)]))
    z.append(('0xAAAA55', [(40, 248), (90, 243), (140, 248), (90, 251)]))
    z.append(('0x555555', [(0, 126), (16, 120), (32, 134), (36, 170), (52, 198), (60, 232), (0, 236)]))
    z.append(('0xAAAAAA', [(2, 128), (16, 122), (28, 132), (14, 134)]))
    z.append(('0x5555AA', [(46, 232), (58, 210), (78, 206), (92, 220), (94, 234)]))
    z.append(('0xAAAAFF', [(60, 212), (76, 208), (82, 214), (68, 214)]))
    z.append(('0x555555', [(260, 132), (244, 126), (228, 140), (224, 172), (210, 204), (206, 232), (260, 236)]))
    z.append(('0xAAAAAA', [(258, 134), (244, 128), (232, 138), (246, 140)]))
    z.append(('0x5555AA', [(214, 233), (200, 218), (184, 220), (178, 234)]))
    # de grap: verloren slipper, 34 x 13, rand AA0055, wit V-bandje
    z.append(('0xAA0055', [(108, 240), (118, 232), (146, 230), (160, 235), (152, 245), (116, 246)]))
    z.append(('0xFF55AA', [(111, 239), (119, 234), (145, 232), (157, 235), (150, 243), (117, 244)]))
    z.append(('0xFFFFFF', [(124, 239), (140, 224), (154, 236), (150, 236), (140, 228), (129, 240)]))
    z.append(('0xFFAAAA', [(170, 240), (176, 234), (182, 240), (176, 242)]))
    z.append(('0xFFAA55', [(20, 190), (27, 185), (31, 192), (24, 196)]))
    return dict(dier='Crab', nr=4, plek='rotsen met verloren slipper', vlak=z, voor=[], cirkels=[],
                thuis=(178, 214), haak='een verloren roze slipper, en de krab blijft op de bodem en blaast belletjes')

def clownvis():
    z = []
    z.append(('0xAA5555', [(0, 226), (50, 222), (110, 228), (160, 222), (210, 226), (260, 220), (260, 260), (0, 260)]))
    z.append(('0xFFAA55', [(80, 240), (100, 234), (124, 240), (100, 244)]))
    z.append(('0xFFAA55', [(150, 236), (166, 232), (180, 237), (166, 240)]))
    z.append(('0xAA0055', [(0, 236), (6, 204), (60, 204), (66, 236)]))
    z.append(('0xFF55AA', vinger([-8, 4, 14, 24, 34, 46, 58, 70], 210, [130, 144, 156, 166, 176, 186, 196])))
    voor = [('0xFFAAFF', vinger([-2, 12, 26, 40, 54, 68], 214, [168, 178, 186, 194, 202], golf=2)),
            # zwaaiende arm: dik, met een gele top, knik naar het midden (naar zijn vis)
            ('0xFFAAFF', [(60, 214), (66, 198), (72, 188), (82, 182), (84, 190), (74, 196), (72, 214)]),
            ('0xFFFFAA', [(78, 182), (84, 178), (88, 184), (84, 190)])]
    z.append(('0xAA55FF', [(260, 128), (238, 136), (226, 172), (212, 206), (224, 226), (260, 230)]))
    z.append(('0x550055', [(246, 222), (240, 160), (243, 160), (250, 222)]))
    z.append(('0xFFAA00', [(196, 228), (193, 212), (188, 204), (191, 202), (197, 208), (200, 198), (204, 199), (202, 214), (204, 228)]))
    return dict(dier='Clownfish', nr=7, plek='anemoon met zwaaiende arm', vlak=z, voor=voor, cirkels=[],
                thuis=(36, 196), haak='hij zit thuis in zijn anemoon, en één arm zwaait naar hem')

WERELDEN = [schildpad(), krab(), clownvis()]
LUCHT = [('0xFFFFAA', 214, 40, 8), ('0x000055', 218, 37, 7)]           # maansikkel: geel rondje min nachtblauw rondje
STERREN = [(46, 70), (60, 52), (224, 66), (200, 22), (34, 96)]          # 1 px wit (op 454 2 px)

def punten(w): return sum(len(p) for _, p in w['vlak'] + w['voor']) + len(w['cirkels'])

def S(v, D_): return int(v * D_ // 260) if v >= 0 else -int(-v * D_ // 260)

def veelhoeken(dr, lijst, D_):
    for c, p in lijst: dr.polygon([(S(x, D_), S(y, D_)) for x, y in p], fill=hx(c))

def lucht(dr, D_):
    s = D_ / 260
    for x, y in STERREN:
        e = 1 if D_ < 300 else 2; dr.rectangle([S(x, D_), S(y, D_), S(x, D_) + e - 1, S(y, D_) + e - 1], fill=WIT)
    for c, x, y, r in LUCHT:
        R = round(r * s); X, Y = S(x, D_), S(y, D_); dr.ellipse([X - R, Y - R, X + R, Y + R], fill=hx(c))

def water(im, top, D_):
    """Nachtlucht met maan, dan zee 0055AA met golvende kam: 5 golven, ±4/260 hoog, schuim 00FFFF 2 px en band 00AAFF 4 px."""
    dr = ImageDraw.Draw(im); dr.rectangle([0, 0, D_, D_], fill=NACHT); lucht(dr, D_)
    s = D_ / 260; a = 4 * s
    for x in range(D_):
        yk = top + int(a * math.sin(x / D_ * 2 * math.pi * 2.5))
        dr.line([(x, yk), (x, D_)], fill=MIDDEN)
        dr.line([(x, yk + round(2 * s)), (x, yk + round(5 * s))], fill=LICHT)
        dr.line([(x, yk), (x, yk + round(2 * s) - 1)], fill=SCHUIM)

def belletjes(dr, x, y, D_, n=3):
    s = D_ / 260
    for i in range(n):
        r = max(1, round((1 + i % 2) * s)); X, Y = S(x + (4 if i % 2 else -2), D_), S(y - 10 - 11 * i, D_)
        dr.ellipse([X - r, Y - r, X + r, Y + r], outline=WIT, width=max(1, round(s)))

def dier_op(dr, w, D_, x, y, m):
    d = D[w['nr']]; _, _, ox, oy = kader(d, m); h.teken(dr, d, round(S(x, D_) - ox), round(S(y, D_) - oy), m)

def thuis(dr, w, D_, m, top_tekst=None):
    """Dier op zijn thuisplek; voorste laag (anemoon) eroverheen; krab blaast belletjes."""
    x, y = w['thuis']; dier_op(dr, w, D_, x, y, m); veelhoeken(dr, w['voor'], D_)
    if w['dier'] == 'Crab': belletjes(dr, x + 8, y - 8, D_, 2)

def basis(D_, top, w):
    im = Image.new('RGB', (D_, D_)); water(im, round(top * D_ / 260), D_); dr = ImageDraw.Draw(im)
    veelhoeken(dr, w['vlak'], D_); return im, dr

# ---------------- schermen ----------------
def adem(D_, w, inn):
    s = D_ / 260; c = D_ // 2; top = 92 if inn else 186
    im, dr = basis(D_, top, w); nm = f'adem-{"in" if inn else "uit"}-{w["dier"]}-{D_}'
    m = 21 if D_ < 300 else 37
    if w['dier'] == 'Turtle' and inn: dier_op(dr, w, D_, 204, top + 4, m); veelhoeken(dr, w['voor'], D_)   # kop boven water
    elif w['dier'] == 'Clownfish' and inn: dier_op(dr, w, D_, 200, 150, m); veelhoeken(dr, w['voor'], D_)  # zwemt uit
    else: thuis(dr, w, D_, m)
    zet(dr, D_, nm, c, 34 * s, 'breathe in' if inn else 'breathe out', f(FS, round(25 * s)), WIT if inn else SCHUIM)
    zet(dr, D_, nm, c, 62 * s, 'round 2 · 18 left', f(FM, round(16 * s)), WIT)
    zet(dr, D_, nm, c, (104 if inn else 92) * s, '12', f(FS, round(70 * s)), WIT)
    return rond(im), nm

def hold(D_, w):
    s = D_ / 260; c = D_ // 2; im, dr = basis(D_, 30, w); nm = f'hold-{w["dier"]}-{D_}'
    thuis(dr, w, D_, 20 if D_ < 300 else 35)
    zet(dr, D_, nm, c, 36 * s, 'hold', f(FS, round(26 * s)), SCHUIM)
    zet(dr, D_, nm, c, 64 * s, 'press START to breathe', f(FM, round(16 * s)), WIT)
    zet(dr, D_, nm, c, 76 * s, '1:45', f(FS, round(80 * s)), WIT)
    zet(dr, D_, nm, c, 162 * s, '61 bpm · round 2', f(FM, round(16 * s)), WIT)
    return rond(im), nm

def eind(D_, w):
    s = D_ / 260; c = D_ // 2; L = NIEUW; im, dr = basis(D_, L['zee'], w); nm = f'eind-{w["dier"]}-{D_}'
    d = D[w['nr']]; m = maat_in_vak(d, round(L['vw'] * s), round(L['vh'] * s)); _, _, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round((L['vak'][0] + L['vak'][1]) / 2 * s - oy), m)
    zet(dr, D_, nm, c, L['kop'] * s - 4 * s, '3 rounds done', f(FS, round(25 * s)), SCHUIM)
    zet(dr, D_, nm, c, L['tijd'] * s - 4 * s, '1:20   1:45   1:58', f(FS, round(24 * s)), WIT)
    zet(dr, D_, nm, c, L['naam'] * s - 5 * s, f'new friend: {w["dier"]}', f(FS, round(24 * s)), GEEL)
    stippen(dr, c, L['stip'] * s, 3, 1, max(2, round(3 * s)), round(12 * s))
    zet(dr, D_, nm, c, L['regel'] * s, '4 weeks in a row', f(FM, round(15 * s)), WIT)
    return rond(im), nm

def menu(D_, w):
    s = D_ / 260; c = D_ // 2; im, dr = basis(D_, 176, w); nm = f'menu-{w["dier"]}-{D_}'
    thuis(dr, w, D_, 20 if D_ < 300 else 35)
    zet(dr, D_, nm, c, 26 * s, 'Ebb', f(FS, round(28 * s)), SCHUIM)
    for y, t in ((62, 'Rounds'), (104, 'Calm 4-7-8')):
        dr.rounded_rectangle([c - 75 * s, y * s, c + 75 * s, (y + 34) * s], radius=17 * s, outline=LICHT, width=max(2, round(2 * s)), fill=NACHT)
        zet(dr, D_, nm, c, (y + 5) * s, t, f(FS, round(22 * s)), WIT)
    zet(dr, D_, nm, c, 146 * s, 'Sea log  ·  Settings  ·  Today', f(FM, round(16 * s)), LICHT)
    return rond(im), nm

def sealog(D_, w):
    s = D_ / 260; c = D_ // 2; im, dr = basis(D_, 80, w); nm = f'sealog-{w["dier"]}-{D_}'
    d = D[w['nr']]; m = maat_in_vak(d, round(96 * s), round(70 * s)); _, _, ox, oy = kader(d, m)
    h.teken(dr, d, round(c - ox), round(124 * s - oy), m)
    zet(dr, D_, nm, c, 24 * s, w['dier'], f(FS, round(26 * s)), SCHUIM)
    zet(dr, D_, nm, c, 52 * s, f'friend {w["nr"] + 1} of 24', f(FM, round(15 * s)), WIT)
    zet(dr, D_, nm, c, 166 * s, 'START: swims with you', f(FM, round(16 * s)), GEEL)
    return rond(im), nm

def pixeltoets(kaal):
    mip = {0, 85, 170, 255}
    return sum(1 for p in kaal.getdata() if not all(v in mip for v in p))

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    data = {'versie': 'werelden v1.1', 'eenheid': '1/260 D, y van boven; schaal x*D/260 afkappen',
            'lucht': {'maan': [{'kleur': c, 'x': x, 'y': y, 'r': r} for c, x, y, r in LUCHT], 'sterren_1px': STERREN},
            'kam': 'golf: y = top + 4/260 D * sin(x/D * 2pi * 2,5); schuim 00FFFF 2/260, band 00AAFF tot 5/260, water 0055AA', 'werelden': []}
    for w in WERELDEN:
        assert mip_ok((0, 0, w['vlak'] + w['voor'])), w['dier']
        assert punten(w) <= 120, (w['dier'], punten(w))
        data['werelden'].append({'dier': w['dier'], 'nr': w['nr'] + 1, 'plek': w['plek'], 'haak': w['haak'], 'punten': punten(w),
            'thuis': w['thuis'], 'vlakken': [{'kleur': c, 'p': [[round(x), round(y)] for x, y in p]} for c, p in w['vlak']],
            'voor_het_dier': [{'kleur': c, 'p': [[round(x), round(y)] for x, y in p]} for c, p in w['voor']]})
    json.dump(data, open(os.path.join(uit, 'ebb-werelden-v11-data.json'), 'w'), indent=1)
    rijen = {260: [], 454: []}; meting = []; vreemd = 0; botsing = []
    for D_ in (260, 454):
        for w in WERELDEN:
            rij = []
            for maak in (lambda: adem(D_, w, True), lambda: adem(D_, w, False), lambda: hold(D_, w),
                         lambda: eind(D_, w), lambda: menu(D_, w), lambda: sealog(D_, w)):
                TEKSTVAK.clear(); im, nm = maak(); vak = list(TEKSTVAK); im.save(os.path.join(uit, nm + '.png')); rij.append(im)
                oud = V.tekst; V.tekst = lambda *a, **k: None; TEKSTVAK.clear(); kaal, _ = maak(); V.tekst = oud
                meting += meet(kaal, vak); vreemd += pixeltoets(kaal)
                from PIL import ImageChops, ImageFilter
                for i in range(len(vak)):
                    for j in range(i + 1, len(vak)):
                        a = vak[i][2].filter(ImageFilter.MaxFilter(5))
                        if ImageChops.multiply(a, vak[j][2]).getbbox(): botsing.append((nm, vak[i][1], vak[j][1]))
            rijen[D_].append(rij)
    for D_, rr in rijen.items():
        st = D_ + 10; ov = Image.new('RGB', (6 * st + 10, len(rr) * st + 10), (30, 30, 30))
        for r, rij in enumerate(rr):
            for i, im in enumerate(rij): ov.paste(im, (10 + i * st, 10 + r * st))
        ov.save(os.path.join(uit, f'werelden-{D_}-rij.png'))
        if D_ == 260: ov.resize((ov.width * 2, ov.height * 2), Image.NEAREST).save(os.path.join(uit, 'werelden-260-rij-2x.png'))
    with open(os.path.join(uit, 'contrast.txt'), 'w') as fo:
        fo.write('scherm | tekst | laagste contrast | aantal achtergrondkleuren onder de inkt\n')
        for m_ in sorted(meting, key=lambda r: r[2]): fo.write(' | '.join(str(v) for v in m_) + '\n')
    with open(os.path.join(uit, 'punten.txt'), 'w') as fo:
        for w in WERELDEN: fo.write(f"{w['dier']} ({w['plek']}): {punten(w)} punten, {len(w['vlak']) + len(w['voor'])} vlakken\n")
        fo.write(f'maan en sterren: 2 cirkels en {len(STERREN)} punten (gedeeld door alle werelden)\n')
        fo.write(f'teksten die elkaar raken (minder dan 3 px ertussen): {len(botsing)} {botsing}\n')
        fo.write(f'pixels buiten de 64 MIP-kleuren (alle schermen zonder letters): {vreemd}\n')
    print(open(os.path.join(uit, 'punten.txt')).read()); print('laagste contrast', min(m[2] for m in meting))
    for m_ in sorted(meting, key=lambda r: r[2])[:5]: print(m_)
