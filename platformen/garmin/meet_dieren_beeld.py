# Ebb: zichtbaarheid van een dier gemeten op ECHTE schermbeelden (Gijs, run 74, 12 nov 2026, nachtlijst punt 1).
# Gebruik: python3 meet_dieren_beeld.py <map met beelden> <horloge> <uit.csv> [map voor controlebeelden]
# Beelden heten <ronde>__sessie-<plek>-<in|hold>-<dag|nacht>-<horloge>.png.
# Werkwijze per dier en fase (in of hold), dag en nacht samen omdat het dier dan op dezelfde plek staat:
# 1. Venster rond de plek van het dier. Beeld 3x3 vervaagd (zo wordt het raster op MIP één mengkleur).
# 2. Achtergrond per pixel, vier kandidaten: de rand van het venster links en rechts in dezelfde rij, boven en onder in
#    dezelfde kolom (mediaan). Het verschil is de afstand in Lab tot de DICHTSTBIJZIJNDE kandidaat (streng voor het dier).
# 3. Wat meer dan DREMPEL_MASK van die achtergrond afwijkt en aan het midden vastzit is het dier; dunne lijnen
#    (golfrand, schuim) gaan er met twee openingen af (3x3 en een staande van 11 px op de FR255, 5x5 en 19 px op de fenix 8), gaten worden gevuld. Het silhouet is dag en nacht samen.
# 4. Getal: het deel van het silhouet (procent) dat minstens DREMPEL_ZIEN (Lab) van de achtergrond afwijkt.
# Zwakte: een dier dat bij dag EN bij nacht helemaal wegvalt heeft geen silhouet; daarom staat de oppervlakte erbij.
import sys, os, glob, csv
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
from skimage import color
DREMPEL_MASK = 12.0; DREMPEL_ZIEN = 20.0
# midden van het dier (x, y), half venster (bx, by) en maat van de opening, in pixels van het simulatorbeeld
PLEK = {'fr255': {'in': (211, 322, 56, 34, 3), 'hold': (211, 375, 56, 32, 3)},
        'fenix847mm': {'in': (362, 493, 104, 66, 5), 'hold': (362, 588, 104, 62, 5)}}
def lab(im): return color.rgb2lab(np.asarray(im.convert('RGB').filter(ImageFilter.BoxBlur(1)), dtype=float) / 255.0)
def meet(paden, plek):
    cx, cy, bx, by, op = plek; vak = (cx - bx, cy - by, cx + bx, cy + by)
    de = {}
    for k, p in paden.items():
        L = lab(Image.open(p).crop(vak))
        kand = [np.median(L[:, :8], axis=1)[:, None, :], np.median(L[:, -8:], axis=1)[:, None, :],
                np.median(L[:6], axis=0)[None, :, :], np.median(L[-6:], axis=0)[None, :, :]]
        de[k] = np.min([np.sqrt(((L - b) ** 2).sum(axis=2)) for b in kand], axis=0)
    sil = np.zeros((2 * by, 2 * bx), bool)
    for k in de:
        m = ndimage.binary_opening(de[k] > DREMPEL_MASK, np.ones((op, op)))
        m = ndimage.binary_opening(m, np.ones((op * 4 - 1, 1)))  # weg met liggende banden (golfrand, schuim): lager dan 11 px (FR255) of 19 px (fenix 8)
        lbl, n = ndimage.label(m)
        kern = set(np.unique(lbl[by // 2:by + by // 2, bx // 2:bx + bx // 2])) - {0}
        sil |= np.isin(lbl, list(kern))
    sil = ndimage.binary_fill_holes(sil)
    raakt = bool(sil[0].any() or sil[-1].any())
    uit = {}
    for k in de:
        a = int(sil.sum())
        uit[k] = (round(100.0 * float((de[k][sil] >= DREMPEL_ZIEN).mean()), 0) if a else 0.0, a, raakt, round(float(np.median(de[k][sil])), 0) if a else 0.0)
    return uit, sil, vak
if __name__ == '__main__':
    S, h, uitpad = sys.argv[1], sys.argv[2], sys.argv[3]; ctrl = sys.argv[4] if len(sys.argv) > 4 else None
    rijen = []
    sleutels = sorted({os.path.basename(p).rsplit('-', 2)[0] for p in glob.glob(os.path.join(S, '*-%s.png' % h))})
    for s in sleutels:
        paden = {n: os.path.join(S, '%s-%s-%s.png' % (s, n, h)) for n in ('dag', 'nacht')}
        paden = {n: p for n, p in paden.items() if os.path.exists(p)}
        fase = s.rsplit('-', 1)[1]
        u, sil, vak = meet(paden, PLEK[h][fase])
        for n in u: rijen.append([s, n, h, u[n][0], u[n][3], u[n][1], 'ja' if u[n][2] else 'nee'])
        if ctrl:
            os.makedirs(ctrl, exist_ok=True)
            for n, p in paden.items():
                c = np.asarray(Image.open(p).convert('RGB').crop(vak)).copy()
                r = sil & ~ndimage.binary_erosion(sil); c[r] = (255, 0, 255)
                Image.fromarray(c).resize((c.shape[1] * 3, c.shape[0] * 3), Image.NEAREST).save(os.path.join(ctrl, '%s-%s-%s.png' % (s, n, h)))
    with open(uitpad, 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['scene', 'dagnacht', 'horloge', 'procent_zichtbaar', 'mediaan_verschil', 'oppervlak_px', 'raakt_rand']); w.writerows(rijen)
    for r in rijen: print(*r)
