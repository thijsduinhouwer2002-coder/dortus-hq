# Blad v9 (run 33, 11 nov): de vier punten "Voor Mila" uit keuring bouw 4.
# 1. sea log op 260 groter (2 rijen van 3, maat 24 in plaats van 15), 2. gladde silhouetten,
# 3. een eigen viering voor "sea complete", 4. silhouet van het volgende dier als schaduw in het water.
# Alles getekend met horloge_sim.py (nabootsing van DierenData.mc) en Barlow Condensed (OFL).
# Gebruik: python3 blad_v9.py <uitmap>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from PIL import Image, ImageDraw, ImageFont
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')
uit = sys.argv[1] if len(sys.argv) > 1 else os.path.join(G, 'blad9'); os.makedirs(uit, exist_ok=True)
D = h.laad(os.path.join(G, 'ebb-dieren-v83-data.json'))
FM = os.path.join(B, 'fonts', 'BarlowCondensed-Medium.ttf'); FS = os.path.join(B, 'fonts', 'BarlowCondensed-SemiBold.ttf')
def f(p, s): return ImageFont.truetype(p, s)

SCHUIM, LICHT, MIDDEN, DIEP, NACHT = (0, 255, 255), (0, 170, 255), (0, 85, 170), (0, 0, 170), (0, 0, 85)
WIT, GEEL = (255, 255, 255), (255, 255, 170)

# ---------- silhouetten ----------
def sil_oud(dr, d, cx, cy, m):
    h.silhouet(dr, d, cx, cy, m)

def sil_v9(dr, d, cx, cy, m, vlak=NACHT, rand=LICHT, k=1):
    """Gladder: rand 1 px in 8 richtingen (recht en schuin) in plaats van 2 px in 4 schuine,
    en geen binnenlijnen (rol 7, 8, 10). Bij dunne vinnen gaven 4 schuine kopieen op 2 px een dubbele, getande rand."""
    for dx in (-k, 0, k):
        for dy in (-k, 0, k):
            if dx or dy: h.delen(dr, d, cx + dx, cy + dy, m, rand, 1)
    h.delen(dr, d, cx, cy, m, vlak, 1)

def schaduw(dr, d, cx, cy, m, k=2):
    """Volgend dier in het water: zwarte schaduw met schuimrand. Zwart op elke zeetint (AMOLED en MIP) is 4:1 of meer."""
    sil_v9(dr, d, cx, cy, m, vlak=(0, 0, 0), rand=SCHUIM, k=1 if m < 40 else 2)

# ---------- zee en scherm ----------
def zee(im, top, D_):
    """Eén zee onderaan: kamlijn in schuim, daaronder banden LICHT, MIDDEN, DIEP, NACHT (MIP-tinten)."""
    dr = ImageDraw.Draw(im); a = max(2, D_ // 90)
    for x in range(D_):
        yk = top + int(a * math.sin(x / D_ * 2 * math.pi * 3))
        dr.line([(x, yk), (x, D_)], fill=MIDDEN)
        dr.line([(x, yk), (x, yk + max(2, D_ // 100))], fill=SCHUIM)
    b = D_ - top
    for i, c in enumerate((DIEP, NACHT)):
        y0 = top + int(b * (0.45 + 0.27 * i))
        for x in range(D_):
            yk = y0 + int(a * math.sin(x / D_ * 2 * math.pi * 2 + i))
            dr.line([(x, yk), (x, D_)], fill=c)

def rond(im):
    D_ = im.width; m = Image.new('L', (D_, D_), 0); ImageDraw.Draw(m).ellipse([0, 0, D_ - 1, D_ - 1], fill=255)
    z = Image.new('RGB', (D_, D_), (0, 0, 0)); z.paste(im, (0, 0), m); return z

def tekst(dr, x, y, s, font, c):
    w = dr.textlength(s, font=font); dr.text((x - w / 2, y), s, font=font, fill=c, anchor='la')

def stippen(dr, cx, y, n, actief, r, stap):
    x0 = cx - (n - 1) * stap / 2
    for i in range(n):
        x = x0 + i * stap
        if i == actief: dr.ellipse([x - r, y - r, x + r, y + r], fill=SCHUIM)
        else: dr.ellipse([x - r, y - r, x + r, y + r], outline=LICHT)

# ---------- 1. sea log ----------
def sealog(D_, blad, gevonden, kies, naam, regel):
    """Blad 1 tot 4: 6 dieren in 2 rijen van 3. Blad 5: alleen de zeekomkommer (bonus) in het midden."""
    s = D_ / 260; im = Image.new('RGB', (D_, D_)); dr = ImageDraw.Draw(im); c = D_ // 2
    m = 23 if D_ < 300 else 40
    tekst(dr, c, 28 * s, 'sea log', f(FS, round(26 * s)), SCHUIM)
    tekst(dr, c, 58 * s, f'{gevonden} of 24', f(FM, round(17 * s)), LICHT)
    if blad < 5:
        for j in range(6):
            nr = (blad - 1) * 6 + j; d = D[nr]
            cx = c + (j % 3 - 1) * round(62 * s); cy = round((103 + (j // 3) * 47) * s)
            if nr < gevonden: h.teken(dr, d, cx, cy, m)
            else: sil_v9(dr, d, cx, cy, m, k=1 if m < 40 else 2)
            if nr == kies: dr.ellipse([cx - 2*s, cy + 27*s, cx + 2*s, cy + 31*s], fill=SCHUIM)
    else:
        h.teken(dr, D[24], c, round(132 * s), m + 14)
        tekst(dr, c, 88 * s, 'bonus', f(FM, round(16 * s)), GEEL)
    tekst(dr, c, 184 * s, naam, f(FS, round(26 * s)), WIT)
    tekst(dr, c, 210 * s, regel, f(FM, round(15 * s)), LICHT)
    stippen(dr, c, 236 * s, 5, blad - 1, max(2, round(2 * s)), round(9 * s))
    return rond(im)

# ---------- 3. sea complete ----------
def sea_complete(D_, weken=12):
    """Eigen viering, geen gewoon eindscherm: de walvis groot in het midden met een fontein van belletjes,
    en de 23 andere vrienden zwemmen in een glimlach onder hem (twee bogen). De zee staat hoog: de hele zee is van jou.
    Geen tijden op dit scherm (die staan een knop verder in het duikprofiel); dit scherm is alleen het feest."""
    s = D_ / 260; im = Image.new('RGB', (D_, D_)); c = D_ // 2
    zee(im, round(77 * s), D_); dr = ImageDraw.Draw(im)
    for dx, dy, r in ((0, 88, 4), (-7, 81, 3), (8, 78, 3)):
        x, y, rr = c + dx * s, dy * s, max(1, r * s)
        dr.ellipse([x - rr, y - rr, x + rr, y + rr], outline=SCHUIM, width=max(1, round(s)))
    h.teken(dr, D[23], c, round(108 * s), 38 if D_ < 300 else 66)
    m = 11 if D_ < 300 else 19; mx, my = c, 98 * s
    bogen = ((93, 14, 32, 148), (62, 9, 46, 134))      # straal, aantal, van hoek, tot hoek (graden, 90 = onder)
    nr = 0
    for R, n, a0, a1 in bogen:
        for i in range(n):
            hoek = math.radians(a0 + (a1 - a0) * i / (n - 1))
            h.teken(dr, D[nr], round(mx + R * s * math.cos(hoek)), round(my + R * s * math.sin(hoek)), m); nr += 1
    tekst(dr, c, 26 * s, 'sea complete', f(FS, round(23 * s)), GEEL)
    tekst(dr, c, 51 * s, '24 of 24 friends', f(FM, round(16 * s)), SCHUIM)
    tekst(dr, c, 206 * s, f'{weken} weeks in a row', f(FM, round(14 * s)), SCHUIM)
    return rond(im)

# ---------- 4. eindscherm met schaduw van het volgende dier ----------
def einde_schaduw(D_, nr=7, oud=False):
    s = D_ / 260; im = Image.new('RGB', (D_, D_)); c = D_ // 2
    zee(im, round(86 * s), D_); dr = ImageDraw.Draw(im)
    tekst(dr, c, 30 * s, '3 rounds done', f(FS, round(25 * s)), SCHUIM)
    tekst(dr, c, 58 * s, '1:20   1:45   3:04', f(FS, round(22 * s)), WIT)
    m = 26 if D_ < 300 else 45
    if oud: h.silhouet(dr, D[nr], c, round(112 * s), m)
    else: schaduw(dr, D[nr], c, round(112 * s), m)
    tekst(dr, c, 146 * s, '1 more session:', f(FM, round(16 * s)), WIT)
    tekst(dr, c, 166 * s, 'a new friend', f(FS, round(18 * s)), GEEL)
    tekst(dr, c, 194 * s, '4 weeks in a row', f(FM, round(15 * s)), SCHUIM)
    return rond(im)

def groot(im, k): return im.resize((im.width * k, im.height * k), Image.NEAREST)

if __name__ == '__main__':
    sch = {}
    for D_ in (260, 454):
        sch[f'sealog-1-{D_}'] = sealog(D_, 1, 8, 4, 'Crab', 'START: swims with you')
        sch[f'sealog-2-{D_}'] = sealog(D_, 2, 8, 7, 'Clownfish', '1 more session')
        sch[f'sealog-4-{D_}'] = sealog(D_, 4, 24, 23, 'Whale', 'START: swims with you')
        sch[f'sealog-5-{D_}'] = sealog(D_, 5, 24, 24, 'Sea cucumber', 'back after a break')
        sch[f'sea-complete-{D_}'] = sea_complete(D_)
        sch[f'einde-schaduw-{D_}'] = einde_schaduw(D_)
        sch[f'einde-schaduw-oud-{D_}'] = einde_schaduw(D_, oud=True)
    for k, v in sch.items(): v.save(os.path.join(uit, k + '.png'))
    # silhouet-toets: orka, haai, zwaardvis (en manta, rog) oud en v9, op 260-maat 24, 4x
    t = Image.new('RGB', (5 * 70, 2 * 64)); dr = ImageDraw.Draw(t)
    for i, nr in enumerate((19, 17, 14, 16, 11)):
        sil_oud(dr, D[nr], 35 + i * 70, 32, 24); sil_v9(dr, D[nr], 35 + i * 70, 96, 24)
    groot(t, 4).save(os.path.join(uit, 'silhouet-oud-boven-v9-onder-4x.png'))
    print('ok', len(sch))
