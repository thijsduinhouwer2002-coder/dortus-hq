# Blad strand v1 (Mila, run 41): Today als strand, 8 weeks als kustlijn (besluit hoofdchat 12 nov 01:20).
# Geen staafjes waarvan de hoogte de inhoudtijd is. Today: elke sessie laat op haar uur een schelp achter op de
# getijdenlijn, alle schelpen even groot; het dier zit op het zand op het uur van nu. 8 weeks: acht golven,
# een gehaald weekdoel is een volle brekende golf, een gemiste week een vlakke deining; de huidige week groeit
# met de voortgang en het dier surft erop. Alleen vlakken, 64 MIP-kleuren, maten in 1/260 D.
#   python3 strand_v1.py <uitmap>
import sys, os, math, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v1 as V
from werelden_v1 import hx, zet, TEKSTVAK, meet, D, kader, f, FM, FS, SCHUIM, LICHT, MIDDEN, NACHT, WIT, rond
from werelden_v11 import S, lucht, pixeltoets
import horloge_sim as h
from PIL import Image, ImageDraw

ZAND, NAT, DONKERZAND, INKT = hx('0xFFFFAA'), hx('0xAAAA55'), hx('0x555500'), hx('0x000055')
ROZE, ROZEDONKER = hx('0xFFAAAA'), hx('0xFF5555')
SCHELP = [(0, 0), (-7, -5), (-6, -11), (-2, -14), (2, -14), (6, -11), (7, -5)]       # 14 x 14, punt onder
RIBBEN = [[(0, -1), (-3, -12), (-1, -12)], [(0, -1), (1, -12), (3, -12)]]

def golfrand(dr, D_, y, a, n, kleur, tot):
    s = D_ / 260
    for x in range(D_):
        yk = S(y, D_) + int(a * s * math.sin(x / D_ * 2 * math.pi * n))
        dr.line([(x, yk), (x, S(tot, D_))], fill=kleur)

def zee_strand(D_, kam, natlijn, droog):
    im = Image.new('RGB', (D_, D_)); dr = ImageDraw.Draw(im); dr.rectangle([0, 0, D_, D_], fill=NACHT); lucht(dr, D_)
    s = D_ / 260
    golfrand(dr, D_, kam, 3, 3, MIDDEN, 260)
    for x in range(D_):   # schuimkam
        yk = S(kam, D_) + int(3 * s * math.sin(x / D_ * 2 * math.pi * 3))
        dr.line([(x, yk), (x, yk + round(2 * s) - 1)], fill=hx('0x00FFFF'))
        dr.line([(x, yk + round(2 * s)), (x, yk + round(4 * s))], fill=hx('0x00AAFF'))
    golfrand(dr, D_, natlijn, 2, 4, NAT, 260)            # nat zand
    for x in range(D_):                                   # getijdenlijn: dunne schuimrand waar het water stopte
        yk = S(natlijn, D_) + int(2 * s * math.sin(x / D_ * 2 * math.pi * 4))
        dr.line([(x, yk), (x, yk + max(1, round(s)) - 1)], fill=WIT)
    golfrand(dr, D_, droog, 1, 2, ZAND, 260)             # droog zand
    return im, dr

def poly(dr, D_, pts, x0, y0, c, k=1.0):
    dr.polygon([(S(x0 + x * k, D_), S(y0 + y * k, D_)) for x, y in pts], fill=c)

def schelp(dr, D_, x, y, k=1.6):
    poly(dr, D_, SCHELP, x, y, ROZE, k)
    for r in RIBBEN: poly(dr, D_, r, x, y, ROZEDONKER, k)

def dier(dr, D_, nr, x, y, m, spiegel=False):
    d = D[nr]; _, _, ox, oy = kader(d, m)
    if not spiegel: h.teken(dr, d, round(S(x, D_) - ox), round(S(y, D_) - oy), m); return
    tmp = Image.new('RGBA', (4 * m * 8, 4 * m * 8), (0, 0, 0, 0)); td = ImageDraw.Draw(tmp)
    h.teken(td, d, 2 * m * 8 - ox, 2 * m * 8 - oy, m); tmp = tmp.transpose(Image.FLIP_LEFT_RIGHT)
    dr._image.paste(tmp, (round(S(x, D_) - 2 * m * 8), round(S(y, D_) - 2 * m * 8)), tmp)

def X_uur(u): return 36 + u / 24 * 188          # 00:00 op x 36, 24:00 op x 224

def today(D_, sessies, nu, nr, gemiddeld):
    nm = f'today-{len(sessies)}-{D_}'; c = D_ // 2; s = D_ / 260
    kam, nat, droog = 74, 128, 150
    im, dr = zee_strand(D_, kam, nat, droog)
    zet(dr, D_, nm, c, 26 * s, 'today', f(FS, round(26 * s)), SCHUIM)
    # uurstreepjes en labels op het droge zand
    for u in (0, 6, 12, 18, 24):
        x = S(X_uur(u), D_); dr.rectangle([x, S(150, D_), x + max(1, round(s)) - 1, S(153, D_)], fill=DONKERZAND)
        zet(dr, D_, nm, x, 153 * s, str(u), f(FM, round(14 * s)), DONKERZAND)
    # nu: een klein wit golfje op de getijdenlijn dat met de klok meeschuift
    poly(dr, D_, [(-6, 0), (-3, -3), (0, -4), (3, -3), (6, 0), (3, -1), (0, -2), (-3, -1)], X_uur(nu), nat - 1, WIT)
    # schelpen: op het uur van de sessie, op de getijdenlijn; zelfde uur: 9 naar rechts schuiven
    eind = [-99, -99]; vorige = -99          # per rij de x van de laatste schelp; rij 1 ligt 14 hoger in het ondiepe water
    for u in sessies:
        x = X_uur(u)
        if x - eind[0] >= 16: rij = 0
        elif x - eind[1] >= 16: rij = 1
        else: rij = 0; x = eind[0] + 16
        schelp(dr, D_, x, nat + 12 - rij * 14); eind[rij] = x; vorige = max(vorige, x)
    # lopers (schildpad, krab) zitten op het natte zand; zwemmers kijken uit het ondiepe water net boven de getijdenlijn
    loper = nr in (3, 4)
    xd = X_uur(nu) if not sessies else (vorige + 26 if vorige + 26 <= 210 else vorige - 28)   # naast de nieuwste schelp, nooit erover
    dier(dr, D_, nr, min(xd, 212), 134 if loper else 110, round(24 * s), spiegel=True)
    for x0, y0 in ((84, 226), (150, 228), (112, 240)):    # ribbels in het droge zand
        poly(dr, D_, [(0, 0), (8, -2), (16, 0), (8, -1)], x0, y0, NAT)
    n = len(sessies)
    zet(dr, D_, nm, c, 176 * s, f'{n} shell{"s" if n != 1 else ""} today' if n else 'no shells yet', f(FS, round(22 * s)), INKT)
    if gemiddeld: zet(dr, D_, nm, c, 202 * s, f'first shell {gemiddeld}', f(FM, round(16 * s)), INKT)
    else: zet(dr, D_, nm, c, 202 * s, 'one session leaves one', f(FM, round(16 * s)), INKT)
    return rond(im), nm

def golf(dr, D_, x, basis, hoog, vol, kop=True):
    """Golf van 22 breed. vol: brekende golf met schuimkrul; anders vlakke deining van 3 hoog."""
    if not vol:
        poly(dr, D_, [(0, 0), (6, -hoog * 0.28), (12, -hoog * 0.33), (18, -hoog * 0.26), (24, 0)], x, basis, hx('0x00AAFF'))
        poly(dr, D_, [(4, -hoog * 0.24), (8, -hoog * 0.32), (13, -hoog * 0.36), (18, -hoog * 0.3), (13, -hoog * 0.3), (8, -hoog * 0.27)], x, basis, WIT); return
    lijf = [(0, 0), (4, -hoog * 0.45), (10, -hoog * 0.9), (16, -hoog), (21, -hoog * 0.85), (22, -hoog * 0.6), (18, -hoog * 0.7), (16, -hoog * 0.5), (22, 0)]
    poly(dr, D_, lijf, x, basis, hx('0x00AAFF'))
    krul = [(8, -hoog * 0.82), (12, -hoog * 0.98), (16, -hoog - 2), (21, -hoog * 0.9), (23, -hoog * 0.62), (20, -hoog * 0.78), (16, -hoog * 0.86), (12, -hoog * 0.84)]
    if kop: poly(dr, D_, krul, x, basis, WIT)

def weken(D_, gehaald, voortgang, nr):
    nm = f'weeks-{sum(gehaald)}-{D_}'; c = D_ // 2; s = D_ / 260
    kam, nat, droog = 150, 162, 176
    im, dr = zee_strand(D_, kam, nat, droog)
    zet(dr, D_, nm, c, 26 * s, '8 weeks', f(FS, round(26 * s)), SCHUIM)
    basis = 152; hoog = 34
    for i, g in enumerate(gehaald + [None]):
        x = 30 + i * 25
        if g is None:      # deze week: groeit met de voortgang, het dier surft erop
            hh = max(8, hoog * voortgang); golf(dr, D_, x, basis, hh, True, kop=voortgang >= 1)
            dier(dr, D_, nr, x + 15, basis - hh - 7, round(14 * s))
        else: golf(dr, D_, x, basis, hoog, g)
    zet(dr, D_, nm, c, 70 * s, f'{sum(gehaald)} big waves', f(FS, round(22 * s)), WIT)
    zet(dr, D_, nm, c, 94 * s, 'one wave a week', f(FM, round(15 * s)), LICHT)
    zet(dr, D_, nm, S(48, D_), 182 * s, '8 wk ago', f(FM, round(14 * s)), DONKERZAND)
    zet(dr, D_, nm, S(214, D_), 182 * s, 'now', f(FM, round(14 * s)), DONKERZAND)
    zet(dr, D_, nm, c, 204 * s, 'this week: 2 of 3', f(FM, round(16 * s)), INKT)
    return rond(im), nm

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    beelden = []; meting = []; vreemd = 0
    for D_ in (260, 454):
        rij = []
        for maak in (lambda: today(D_, [7.2, 12.6, 21.1], 21.5, 3, '7:12'), lambda: today(D_, [], 9.0, 4, None),
                     lambda: today(D_, [7.0, 7.3, 7.6, 13.0, 18.5], 19.0, 7, '7:00'),
                     lambda: weken(D_, [True, True, False, True, True, True, False], 0.66, 3)):
            TEKSTVAK.clear(); im, nm = maak(); vak = list(TEKSTVAK); im.save(os.path.join(uit, nm + '.png')); rij.append(im)
            oud = V.tekst; V.tekst = lambda *a, **k: None; TEKSTVAK.clear(); kaal, _ = maak(); V.tekst = oud
            meting += meet(kaal, vak); vreemd += pixeltoets(kaal)
        beelden.append(rij)
    for D_, rij in zip((260, 454), beelden):
        st = D_ + 10; ov = Image.new('RGB', (len(rij) * st + 10, st + 10), (30, 30, 30))
        for i, im in enumerate(rij): ov.paste(im, (10 + i * st, 10))
        ov.save(os.path.join(uit, f'strand-{D_}-rij.png'))
        if D_ == 260: ov.resize((ov.width * 2, ov.height * 2), Image.NEAREST).save(os.path.join(uit, 'strand-260-rij-2x.png'))
    with open(os.path.join(uit, 'contrast.txt'), 'w') as fo:
        for m_ in sorted(meting, key=lambda r: r[2]): fo.write(' | '.join(str(v) for v in m_) + '\n')
    print('pixels buiten MIP', vreemd); print('laagste contrast', sorted(meting, key=lambda r: r[2])[:5])
