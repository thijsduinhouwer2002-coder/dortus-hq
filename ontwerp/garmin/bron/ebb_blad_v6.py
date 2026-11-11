# Ontwerpblad Ebb v6 (Mila, 11 nov run 24): de 12 moet-punten van de keuring van blad v5 door drie beoordelaars
# (ontwerp/garmin/ebb-blad-v5-keuring-drie.md) en de besluiten van de hoofdchat over zee en reeks.
# Bouwt op ebb_blad_v5.py: alleen wat verandert staat hier.
# Gebruik: python3 ebb_blad_v6.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
from ebb_blad_v3 import *
import ebb_blad_v4 as v4
from ebb_blad_v4 import omlijnd, dagstippen
import ebb_blad_v5 as v5
from ebb_blad_v5 import LICHTCYAAN, regel_hart_ronde, veilig, instel
import ebb_dieren_v6 as dv6
from ebb_dieren_v6 import ALLE
from PIL import Image, ImageDraw
dier = v3.dier

# ---------------- punt 5: zee elke 30 s donkerder tot 2:30, daarna gelijk ----------------
ZEE_STAND = [
    [(0.12, W0), (0.19, W1), (0.62, W2), (0.90, W3)],   # 0:00
    [(0.12, W0), (0.16, W1), (0.50, W2), (0.78, W3)],   # 0:30
    [(0.12, W1), (0.40, W2), (0.68, W3)],               # 1:00
    [(0.12, W1), (0.26, W2), (0.52, W3)],               # 1:30
    [(0.12, W2), (0.40, W3)],                           # 2:00
    [(0.12, W3)],                                       # 2:30 en verder: diepste blauw, alleen de dunne schuimrand
]
def stand(sec): return min(5, sec // 30)
def duik_zee6(im, D, sec):
    st = stand(sec)
    zee(im, D, [(D*p, c) for p, c in ZEE_STAND[st]], amp=D*0.014, stralen=st < 4)   # lichtstralen weg vanaf 2:00
    if amo(D):
        k = 1 - 0.10*st
        im.paste(Image.eval(im, lambda v: int(v*k)), (0, 0))

def trilboog(d, D, cx, cy, breed, kleur):
    """Twee trilboogjes links en rechts van een regel, gespiegeld, zodat het midden blijft."""
    lw = max(2, round(D/150))
    for k in (-1, 1):
        for j, r in enumerate((0.030, 0.052)):
            x = cx + k*(breed/2 + D*0.018); R = r*D
            box = [x - R, cy - R, x + R, cy + R]
            d.arc(box, 300, 60, fill=kleur, width=lw) if k == 1 else d.arc(box, 120, 240, fill=kleur, width=lw)

# belletjes: links en rechts verdeeld (punt 11); vanaf 2:30 geen belletjes meer (punt 5)
BELLEN = {30: [(0.29, 0.66, 0.012), (0.72, 0.61, 0.008)],
          105: [(0.71, 0.64, 0.013), (0.28, 0.60, 0.008), (0.74, 0.56, 0.005)],
          150: [], 184: []}

def s_duik6(D, sec, ronde, bpm, hoek):
    im = leeg(D); duik_zee6(im, D, sec); d = ImageDraw.Draw(im)
    if sec < 180:
        tekst(d, D, (D/2, D*0.200), 'hold', D*0.085, SCHUIM)
    else:   # punt 3: trilteken bij "time to breathe" (gespiegelde boogjes)
        px = D*0.080; tekst(d, D, (D/2, D*0.200), 'time to breathe', px, WIT)
        trilboog(d, D, D/2, D*0.200, f(max(px, MIN*D)).getlength('time to breathe'), GEEL)
    tekst(d, D, (D/2, D*0.290), 'press  START  to breathe' if D < 300 else 'press START to breathe', D*0.056, LICHTCYAAN)   # punt 3: zo stop je
    tekst(d, D, (D/2, D*0.455), f'{sec//60}:{sec%60:02d}', D*0.28, WIT)
    bellen(d, D, BELLEN[sec])
    dier(im, 'pad', D/2, D*0.665, D*0.10, hoek=hoek)
    d = ImageDraw.Draw(im)
    regel_hart_ronde(d, D, D*0.825, bpm, ronde)
    rand(im, D); return im
def s_duik_a(D): return s_duik6(D, 30, 1, 66, -4)
def s_duik_b(D): return s_duik6(D, 105, 2, 61, 0)    # punt 11: schildpad recht, niet op zijn schild
def s_duik_d(D): return s_duik6(D, 150, 3, 59, -2)
def s_duik_c(D): return s_duik6(D, 184, 3, 57, -2)

# ---------------- punt 12: menu, beide keuzes dezelfde knop; selectie = schuimrand ----------------
def knop(d, D, y, w, h, gekozen):
    lw = max(2, round(D/130)) * (2 if gekozen else 1)
    kleur = SCHUIM if gekozen else (W1 if not amo(D) else AM[W1])
    d.rounded_rectangle([D/2-w*D/2, y*D-h*D/2, D/2+w*D/2, y*D+h*D/2], radius=h*D/2, fill=ZWART, outline=kleur, width=lw)

def s_menu6(D):
    im = leeg(D)
    zee(im, D, [(D*0.775, W1), (D*0.86, W2)], amp=D*0.008)
    dier(im, 'pad', D/2, D*0.875, D*0.070, hoek=-4)     # je eigen dier helemaal onder water
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.165), 'Ebb', D*0.10, TITEL)
    knop(d, D, 0.335, 0.62, 0.15, True)
    tekst(d, D, (D/2, D*0.335), 'Rounds', D*0.085, WIT)
    knop(d, D, 0.510, 0.62, 0.15, False)
    tekst(d, D, (D/2, D*0.510), 'Calm 4-7-8', D*0.085, WIT)
    tekst(d, D, (D/2, D*0.655), 'Sea log  ·  Settings', D*0.066, LICHTCYAAN)
    rand(im, D); return im

# ---------------- 1b en 2: teksten (punt 4) ----------------
def s_start6(D):
    im = leeg(D)
    zee(im, D, [(D*0.80, W1), (D*0.88, W2)], amp=D*0.010)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), '3 rounds · 30 breaths', D*0.070, TITEL)
    tekst(d, D, (D/2, D*0.38), 'Seated', D*0.12, WIT)
    tekst(d, D, (D/2, D*0.49), 'or lying?', D*0.12, WIT)
    v4.pil(d, D, 0.655, 0.40, 0.13)
    tekst(d, D, (D/2, D*0.655), 'Start', D*0.080, WIT)
    rand(im, D); return im

def s_ademen6(D):
    im = leeg(D)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'breathe in', D*0.090, TITEL)
    tekst(d, D, (D/2, D*0.41), '23', D*0.32, WIT)
    tekst(d, D, (D/2, D*0.80), 'of 30  ·  round 2', D*0.068, WIT)
    rand(im, D); return im

# ---------------- punt 1 en 2: today met staande staven, neutraal ----------------
OCHTEND = [70, 85, 100]    # 6b: sessie 8, krijgt de Starfish; holds korter dan in de avond (punt 1)
AVOND = [80, 105, 184]     # 3a tot 3c en 6c: sessie 9, geen dier
def mmss(s): return f'{s//60}:{s%60:02d}'
def s_today6(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'today', D*0.085, TITEL)
    sessies = [('7:40', OCHTEND), ('21:15', AVOND)]
    L, R, bod, hoog = D*0.20, D*0.80, D*0.62, D*0.27
    gat = D*0.08; kol = (R - L - gat)/6; bw = kol*0.62
    m = Image.new('L', (D, D), 0); md = ImageDraw.Draw(m); kop = []
    for si, (_, tijden) in enumerate(sessies):
        for j, sec in enumerate(tijden):
            xm = L + (si*3 + j + 0.5)*kol + si*gat; yt = bod - hoog*sec/200
            md.rounded_rectangle([xm-bw/2, yt, xm+bw/2, bod], radius=bw*0.30, fill=255); kop.append(xm)
    im.paste(Image.new('RGB', (D, D), W1 if not amo(D) else AM[W1]), (0, 0), m)   # één egale tint: geen nadruk op de langste
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    d.line([(L - D*0.01, bod), (R + D*0.01, bod)], fill=SCHUIM, width=lw)
    for si, (klok, _) in enumerate(sessies):
        xm = L + (si*3 + 1.5)*kol + si*gat
        tekst(d, D, (xm, bod + D*0.055), klok, D*0.062, LICHTCYAAN)
    tot = OCHTEND + AVOND
    tekst(d, D, (D/2, D*0.775), f'6 holds · avg {mmss(sum(tot)//len(tot))}', D*0.072, WIT)
    rand(im, D); return im

# ---------------- 6b en 6c (punt 1, 6, 10) ----------------
def einde_zee(im, D):   # punt 10: golf iets hoger, zodat het dier helemaal onder water past met ruimte tot de tekst
    zee(im, D, [(D*0.320, W1), (D*0.60, W2), (D*0.84, W3)], amp=D*0.010, schuim=True, stralen=True)

def einde_kop6(d, D, tijden):
    tekst(d, D, (D/2, D*0.150), '3 rounds done', D*0.075, TITEL)
    for k, t in enumerate(tijden):
        tekst(d, D, (D/2 + (-0.15, 0, 0.15)[k]*D, D*0.235), t, D*0.068, WIT)

def s_einde6(D):
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop6(d, D, [mmss(s) for s in OCHTEND])
    bellen(d, D, [(0.24, 0.56, 0.011), (0.21, 0.51, 0.006), (0.78, 0.58, 0.010), (0.81, 0.53, 0.006)])
    dier(im, 'ster', D/2, D*0.525, D*0.165)       # punt 10: 20 % kleiner, helemaal onder water, geen stralenkrans
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.750), 'new friend!', D*0.085, GEEL)
    tekst(d, D, (D/2, D*0.815), 'Starfish · 4 days in a row', D*0.066, WIT)
    dagstippen(d, D, D*0.872, 4)
    rand(im, D); return im

def silhouet6(im, D, soort, x, y, s, nr):
    """Punt 6: egaal silhouet 0000AA met dunne rand 0055FF, geen ogen of strepen, met het nummer erop."""
    dier(im, soort, x, y, s, kleur='silhouet')
    d = ImageDraw.Draw(im)
    tekst(d, D, (x, y), str(nr), max(D*0.060, MIN*D), LICHTCYAAN)

def s_einde_gewoon6(D):
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop6(d, D, [mmss(s) for s in AVOND])
    silhouet6(im, D, 'clown', D/2, D*0.525, D*0.17, 8)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.750), 'next: Clownfish', D*0.075, WIT)
    tekst(d, D, (D/2, D*0.815), 'in 1 more session', D*0.066, LICHTCYAAN)
    dagstippen(d, D, D*0.872, 4)
    rand(im, D); return im

# ---------------- punt 9: 8 weeks hoger, alle weken zichtbaar ----------------
WEKEN = [0, 0, 0, 0, 0, 0, 3, 6]
def s_weken6(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), '8 weeks', D*0.085, TITEL)
    L, R, top, bod = D*0.20, D*0.80, D*0.33, D*0.58
    kol = (R-L)/8; bw = kol*0.66; hoog = 7
    m = Image.new('L', (D, D), 0); md = ImageDraw.Draw(m)
    for i, n in enumerate(WEKEN):
        if n:
            xm = L + (i+0.5)*kol; md.rounded_rectangle([xm-bw/2, bod - (bod-top)*n/hoog, xm+bw/2, bod], radius=bw*0.30, fill=255)
    im.paste(Image.new('RGB', (D, D), W1 if not amo(D) else AM[W1]), (0, 0), m)
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    d.line([(L, bod), (R, bod)], fill=SCHUIM, width=lw)
    for i, n in enumerate(WEKEN):
        xm = L + (i+0.5)*kol
        if n: tekst(d, D, (xm, bod - (bod-top)*n/hoog - D*0.045), str(n), D*0.066, WIT)
        else:
            rr = D*0.013; d.ellipse([xm-rr, bod-D*0.03-rr, xm+rr, bod-D*0.03+rr], fill=W0 if not amo(D) else AM[W0])   # lege week: stip
    tekst(d, D, (D/2, D*0.665), 'sessions per week', D*0.066, LICHTCYAAN)
    tekst(d, D, (D/2, D*0.750), 'avg hold 1:41', D*0.075, WIT)
    rand(im, D); return im

# ---------------- 8 sea log: 24 + bonus, silhouetten met nummer ----------------
SESSIES_NU = 9
SCHEMA = ['1x', '2x', '2d', '3d', '4x', '6x', '4d', '10x', '5d', '12x', '14x', '16x', '6d', '18x', '20x',
          '22x', '7d', '25x', '28x', '32x', '36x', '42x', '46x', '50x', 'bonus']
def _eis(n):
    naam = ALLE[n][1]; dr = SCHEMA[n]
    if dr == 'bonus': return 'bonus · a surprise'
    if dr.endswith('x'): return f'{naam} · {int(dr[:-1]) - SESSIES_NU} more sessions'
    return f'{naam} · {dr[:-1]} days in a row'
EIS = {n: _eis(n) for n in range(25)}

def s_rooster6(D, pagina, gevonden=7, kies=3):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.135), 'sea log', D*0.075, TITEL)
    tekst(d, D, (D/2, D*0.205), EIS[kies] if kies >= gevonden else f'{gevonden} of 24', D*0.060, WIT if kies >= gevonden else LICHTCYAAN)
    xs = (-0.25, 0, 0.25); ys = (0.37, 0.555, 0.74)
    opp = (D*0.112)**2*0.55
    n_op = min(9, 25 - pagina*9)
    for i in range(n_op):
        n = pagina*9 + i; soort = ALLE[n][0]; r_, k_ = divmod(i, 3)
        rij_n = min(3, n_op - r_*3)                          # halve laatste rij in het midden
        x = D/2 + (xs[k_] + (3 - rij_n)*0.125)*D; y = ys[r_]*D
        sc = v3.schaal_voor_gewicht(soort, opp) * dv6.GROTER.get(soort, 1)
        if n == kies:
            rr = D*0.098; d.ellipse([x-rr, y-rr, x+rr, y+rr], outline=SCHUIM, width=max(2, round(D/130)))
        if n < gevonden: dier(im, soort, x, y, sc)
        else: silhouet6(im, D, soort, x, y, sc*0.92, n+1 if n < 24 else '+')
        d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.875), f'{pagina+1} / 3', D*0.058, LICHTCYAAN)
    rand(im, D); return im
def s_rooster_1(D): return s_rooster6(D, 0)
def s_rooster_2(D): return s_rooster6(D, 1, kies=9)
def s_rooster_3(D): return s_rooster6(D, 2, kies=23)

# ---------------- 9b: gewone woorden (punt 4) ----------------
def s_instel_b(D): return instel(D, 'Buzz last 3 breaths  on', 'Sound', 'off', ['Touch lock  on', 'Safety info'])

SCHERMEN = [('1 menu', s_menu6), ('1b start', s_start6), ('2 ademen', s_ademen6), ('3a hold 0:30', s_duik_a),
            ('3b hold 1:45', s_duik_b), ('3d hold 2:30', s_duik_d), ('3c hold 3:04', s_duik_c), ('4 herstel', v5.s_boven5),
            ('5 rustig 4-7-8', v3.s_rustig), ('6 today', s_today6), ('6b einde met dier', s_einde6), ('6c einde zonder dier', s_einde_gewoon6),
            ('7 8 weeks', s_weken6), ('8 sea log 1 van 3', s_rooster_1), ('8b sea log 2 van 3', s_rooster_2), ('8d sea log 3 van 3', s_rooster_3),
            ('8c sea log dier', v5.s_zeelog5), ('9 settings', v5.s_instel_a), ('9b settings', s_instel_b), ('10 veilig 1', v5.s_veilig_a),
            ('10b veilig 2', v5.s_veilig_b), ('10c veilig 3', v5.s_veilig_c)]

def maak(uit):
    os.makedirs(uit, exist_ok=True); rap = []; beelden = {}
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = teken(fn, D); beelden[(naam, D)] = im; im.save(f'{uit}/ebb-v6-{naam.split()[0]}-{D}.png')
            if D == 260:
                rap.append(f'{D:4d}  {naam:22s} kader x {kader_x(im, D):+5.1f} px   optisch x {optisch_x(im, D):+5.1f} px   buiten MIP {niet_mip(im)}')
            else:
                rap.append(f'{D:4d}  {naam:22s} kader x {kader_x(im, D):+5.1f} px')
    klein = sorted({(t, p) for D, t, p in v3.LOG if D == 260}, key=lambda z: z[1])[:6]
    rap.append('kleinste tekst op 260: ' + ', '.join(f'"{t}" {p} px' for t, p in klein))
    gap = 30; cel_b = 454 + 24 + 260; kol = 4; cel_h = 454 + 64
    rijen = (len(SCHERMEN) + kol - 1)//kol
    W = gap + kol*(cel_b + gap); H = 110 + rijen*(cel_h + gap)
    blad = Image.new('RGB', (W, H), (14, 16, 24)); d = ImageDraw.Draw(blad)
    d.text((gap, 30), 'Ebb blad v6 (Mila): zee donkerder tot 2:30 en dan gelijk, dieren voor trouw, 24 + bonus. Links 454 AMOLED, rechts 260 MIP, ware grootte',
           font=f(44), fill=(220, 230, 240))
    for i, (naam, fn) in enumerate(SCHERMEN):
        r, k = divmod(i, kol); x = gap + k*(cel_b + gap); y = 110 + r*(cel_h + gap)
        blad.paste(beelden[(naam, 454)], (x, y)); blad.paste(beelden[(naam, 260)], (x+478, y+194))
        d.text((x, y+462), naam, font=f(32), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-blad-v6.png')
    # punt 5: vier inhoudschermen naast elkaar, op 454 en op 260
    for D in (454, 260):
        rij = Image.new('RGB', (4*D + 5*30, D + 80), (14, 16, 24)); d = ImageDraw.Draw(rij)
        for i, naam in enumerate(('3a hold 0:30', '3b hold 1:45', '3d hold 2:30', '3c hold 3:04')):
            rij.paste(beelden[(naam, D)], (30 + i*(D+30), 20)); d.text((30 + i*(D+30) + D/2, D + 50), naam, font=f(30), fill=(200, 220, 235), anchor='mm')
        rij.save(f'{uit}/vier-holds-{D}.png')
    # dieren: alle 25 op 260 ware grootte op diep water, gevonden en als silhouet
    Dd = 260; cel = 120; dk = Image.new('RGB', (25*cel + 20, 2*cel + 80), (14, 16, 24)); dd = ImageDraw.Draw(dk)
    for i, (soort, naam) in enumerate(ALLE):
        for j in (0, 1):
            vak = Image.new('RGB', (cel, cel), W2 if j == 0 else W3)
            sc = v3.schaal_voor_gewicht(soort, (Dd*0.13)**2*0.55) * dv6.GROTER.get(soort, 1)
            v3.dier(vak, soort, cel/2, cel/2, sc, kleur=None if j == 0 else 'silhouet')
            dk.paste(vak, (10 + i*cel, 10 + j*cel))
        dd.text((10 + i*cel + cel/2, 2*cel + 30), str(i+1) if i < 24 else '+', font=f(26), fill=(200, 220, 235), anchor='mm')
    dk.save(f'{uit}/../ebb-dieren-v6.png')
    return rap

if __name__ == '__main__':
    v3.FONT = sys.argv[2]
    rap = maak(sys.argv[1])
    print('\n'.join(rap))
    with open(os.path.join(sys.argv[1], 'meting-v6.txt'), 'w') as fh: fh.write('\n'.join(rap) + '\n')
