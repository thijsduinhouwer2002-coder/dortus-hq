# Blad v13 (Mila, run 37, 11 nov avond): eindscherm op 260 (vraag Gijs 20:40 UTC, keuring bouw 7 punt 4).
# Keuring: dieren op het eindscherm 50 tot 55 px breed op 260, en (bouw 6) helemaal onder de kamlijn.
# Regel: tijden en kamlijn schuiven omhoog, het dier krijgt een vak van 54 x 46 onder de kamlijn,
# tekst en stippen schuiven mee. Maat per dier = grootste maat die in het vak past (kader incl. stickerrand).
#   python3 blad_v13.py <uitmap>
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from blad_v9 import zee, rond, tekst, stippen, f, FM, FS, SCHUIM, LICHT, WIT, D
from PIL import Image, ImageDraw
GEEL = (255, 255, 170)

# Alles in px op 260 (x D/260 voor andere maten). Oud = gemeten in fr255-scene17/33/36 (run 43001614437).
OUD = dict(kop=40, tijd=74, zee=112, vak=(113, 142), naam=163, stap=32, stip=190, regel=204, vw=54, vh=29)
NIEUW = dict(kop=34, tijd=63, zee=94, vak=(98, 144), naam=152, stap=23, stip=180, regel=190, vw=54, vh=46)


def kader(d, maat):
    im = Image.new('RGB', (400, 400)); dr = ImageDraw.Draw(im); h.teken(dr, d, 200, 200, maat)
    b = im.getbbox(); return b[2] - b[0], b[3] - b[1], (b[0] + b[2]) / 2 - 200, (b[1] + b[3]) / 2 - 200


def maat_in_vak(d, vw, vh):
    m = 8
    while True:
        w, hh, _, _ = kader(d, m + 1)
        if w > vw or hh > vh: return m
        m += 1


def eind(D_, L, dier, kopregel, tijden, naam, regel, actief=1, oud=False):
    s = D_ / 260; c = D_ // 2
    im = Image.new('RGB', (D_, D_)); zee(im, round(L['zee'] * s), D_); dr = ImageDraw.Draw(im)
    tekst(dr, c, L['kop'] * s - 4 * s, kopregel, f(FS, round(25 * s)), SCHUIM)
    if tijden: tekst(dr, c, L['tijd'] * s - 4 * s, tijden, f(FS, round(24 * s)), WIT)
    d = D[dier]
    if oud: m = 11                      # zoals nu (zeester 21 px breed)
    else: m = maat_in_vak(d, round(L['vw'] * s), round(L['vh'] * s))
    _, _, ox, oy = kader(d, m)
    vy = (L['vak'][0] + L['vak'][1]) / 2 * s
    h.teken(dr, d, round(c - ox), round(vy - oy), m)
    y = L['naam'] * s; fn = f(FS, round(24 * s))
    regels = naam if isinstance(naam, list) else [naam]
    for i, r in enumerate(regels): tekst(dr, c, y - 5 * s + i * L['stap'] * s, r, fn, GEEL)
    extra = (len(regels) - 1) * L['stap'] * s
    stippen(dr, c, L['stip'] * s + extra, 3, actief, max(2, round(3 * s)), round(12 * s))
    tekst(dr, c, L['regel'] * s + extra, regel, f(FM, round(15 * s)), WIT)
    return rond(im), m


SCENES = [  # (naam, dier, kop, tijden, naamregel(s), regel)
    ('s17-zeester', 6, '3 rounds done', '1:10   1:25   1:40', 'new friend: Starfish', '4 weeks in a row'),
    ('s33-zeekomkommer', 24, '3 rounds done', '1:20   1:45   1:58', ['new friend:', 'Sea cucumber'], 'back after a break'),
    ('s36-walvis', 23, '3 rounds done', '1:20   1:45   1:58', '24 of 24 friends', '12 weeks in a row'),
    ('s34-krab-calm', 4, 'calm done', '4 min · 12 breaths', 'new friend: Crab', '5 weeks in a row'),
    ('s17-reuzeninktvis', 21, '3 rounds done', '1:20   1:45   1:58', 'new friend: Giant squid', '9 weeks in a row'),
]


def groot(im, k): return im.resize((im.width * k, im.height * k), Image.NEAREST)


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    rijen = []
    for oud in (True, False):
        rij = []
        for nm, dier, kop, tij, naam, rg in SCENES:
            im, m = eind(260, OUD if oud else NIEUW, dier, kop, tij, naam, rg, oud=oud)
            if not oud: im.save(os.path.join(uit, f'eind-260-{nm}.png'))
            rij.append(im)
        rijen.append(rij)
    W = len(SCENES) * 270 + 10
    ov = Image.new('RGB', (W, 2 * 270 + 10), (30, 30, 30))
    for r, rij in enumerate(rijen):
        for i, im in enumerate(rij): ov.paste(im, (10 + i * 270, 10 + r * 270))
    ov.save(os.path.join(uit, 'eind-260-oud-nieuw-1x.png')); groot(ov, 2).save(os.path.join(uit, 'eind-260-oud-nieuw-2x.png'))
    for nm, dier, kop, tij, naam, rg in SCENES[:3]:
        eind(454, NIEUW, dier, kop, tij, naam, rg)[0].save(os.path.join(uit, f'eind-454-{nm}.png'))
    # maattabel
    with open(os.path.join(uit, 'maten.txt'), 'w') as fo:
        fo.write('nr naam maat260 b x h (px) maat454 b x h (px)\n')
        for i, d in enumerate(D):
            m1 = maat_in_vak(d, 54, 46); w1, h1, _, _ = kader(d, m1)
            m2 = maat_in_vak(d, 94, 80); w2, h2, _, _ = kader(d, m2)
            fo.write(f'{i + 1} {d["naam"]} {m1} {w1}x{h1} {m2} {w2}x{h2}\n')
    print('klaar', uit)
