# Blad v11 (run 35, 11 nov): keuzemarkering in de sea log, opdracht keuring bouw 6 "Voor Mila" punt 2.
# Het gekozen dier (dat met START meezwemt) zit in een belletje: platte ellips in MIDDEN, rand in SCHUIM, wit glimpje linksboven.
# Een ronde ring om het dier past niet: dieren zijn op 260 tot 45 px breed en de rijen staan 47 px uit elkaar; de ellips 60 x 44 wel.
# Waarom een belletje: belletjes zijn al het teken van Ebb (inhouden), dus de keuze leest als "dit dier zit bij jou in het water".
# Alleen fillEllipse, drawEllipse en fillCircle nodig. Varianten A (alleen ring) en B (belletje) naast elkaar voor de keuze.
# Gebruik: python3 blad_v11.py <uitmap>
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from PIL import Image, ImageDraw, ImageFont
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')
D = h.laad(os.path.join(G, 'ebb-dieren-v83-data.json'))
FM = os.path.join(B, 'fonts', 'BarlowCondensed-Medium.ttf'); FS = os.path.join(B, 'fonts', 'BarlowCondensed-SemiBold.ttf')
def f(p, s): return ImageFont.truetype(p, s)
SCHUIM, LICHT, MIDDEN, DIEP, NACHT = (0, 255, 255), (0, 170, 255), (0, 85, 170), (0, 0, 170), (0, 0, 85)
WIT, GEEL = (255, 255, 255), (255, 255, 170)


def maten(D_):
    """Belletje: straal 20 op 260 (35 op 454), rand 2 px (3 px vanaf 390), glimpje straal 3 (5)."""
    s = D_ / 260
    return dict(rx=round(30 * s), ry=round(22 * s), rand=2 if D_ < 390 else 3, glim=max(2, round(2.2 * s)))


def sil(dr, d, cx, cy, m, k=1):
    for dx in (-k, 0, k):
        for dy in (-k, 0, k):
            if dx or dy: h.delen(dr, d, cx + dx, cy + dy, m, LICHT, 1)
    h.delen(dr, d, cx, cy, m, NACHT, 1)


def belletje(dr, cx, cy, D_, variant):
    M = maten(D_); rx, ry, w = M['rx'], M['ry'], M['rand']
    if variant == 'B':
        dr.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=MIDDEN)                # fillEllipse(cx, cy, rx, ry) in MIDDEN
    for i in range(w):                                                              # drawEllipse rx, ry (en 1 px naar binnen) in SCHUIM
        dr.ellipse([cx - rx + i, cy - ry + i, cx + rx - i, cy + ry - i], outline=SCHUIM)
    if variant == 'B':
        g = M['glim']; gx, gy = cx - round(rx * 0.62), cy - round(ry * 0.50)          # glimpje linksboven, binnen de rand
        dr.ellipse([gx - g, gy - g, gx + g, gy + g], fill=WIT)


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


def sealog(D_, blad, gevonden, kies, naam, regel, variant='B'):
    """Zoals blad v9 (2 rijen van 3, raster in het midden), maar de keuzestip onder het dier is weg: het belletje is de keuze."""
    s = D_ / 260; im = Image.new('RGB', (D_, D_)); dr = ImageDraw.Draw(im); c = D_ // 2
    m = 23 if D_ < 300 else 40
    tekst(dr, c, 28 * s, 'sea log', f(FS, round(26 * s)), SCHUIM)
    tekst(dr, c, 58 * s, f'{gevonden} of 24', f(FM, round(17 * s)), LICHT)
    for j in range(6):
        nr = (blad - 1) * 6 + j; d = D[nr]
        cx = c + (j % 3 - 1) * round(62 * s); cy = round((103 + (j // 3) * 47) * s)
        if nr == kies: belletje(dr, cx, cy, D_, variant)                         # eerst het belletje, dan het dier erin
        if nr < gevonden: h.teken(dr, d, cx, cy, m)
        else: sil(dr, d, cx, cy, m, k=1 if m < 40 else 2)
    tekst(dr, c, 184 * s, naam, f(FS, round(26 * s)), WIT)
    tekst(dr, c, 210 * s, regel, f(FM, round(15 * s)), LICHT)
    stippen(dr, c, 236 * s, 5, blad - 1, max(2, round(2 * s)), round(9 * s))
    return rond(im)


if __name__ == '__main__':
    uit = sys.argv[1] if len(sys.argv) > 1 else os.path.join(G, 'blad11'); os.makedirs(uit, exist_ok=True)
    rij = []
    for D_ in (260, 454):
        for v in ('A', 'B'):
            a = sealog(D_, 1, 8, 4, 'Crab', 'START: swims with you', v)
            b = sealog(D_, 4, 24, 18, 'Sunfish', 'START: swims with you', v)
            a.save(os.path.join(uit, f'sealog-1-{v}-{D_}.png')); b.save(os.path.join(uit, f'sealog-4-{v}-{D_}.png'))
            rij += [a, b]
    # overzicht: 260 dubbel (zoals op de pols bekeken), 454 op ware grootte
    W_ = 4 * 520 + 50; o = Image.new('RGB', (W_, 520 + 30 + 454), (40, 40, 40)); dr = ImageDraw.Draw(o)
    for i, im in enumerate(rij[:4]): o.paste(im.resize((520, 520), Image.NEAREST), (i * 530, 0))
    for i, im in enumerate(rij[4:]): o.paste(im, (i * 530 + 33, 550))
    for i, t in enumerate(['A ring', 'A ring', 'B belletje', 'B belletje']):
        dr.text((i * 530 + 10, 525), t + (' (260 x2 boven, 454 onder)' if i == 0 else ''), fill=WIT)
    o.save(os.path.join(uit, 'keuze-A-B.png'))
    for k, v in maten(260).items(): print('260', k, v)
    for k, v in maten(454).items(): print('454', k, v)
