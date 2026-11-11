# Ebb dieren v7 (Mila, 11 nov run 26): punt 1 en 2 van de keuring van blad v6 (ontwerp/garmin/ebb-blad-v6-keuring-drie.md).
# Bouwt op ebb_dieren_v6.py. Alleen wat verandert staat hier.
# Eén tekenregel voor alle gevonden dieren, en die is de haak: de sea log is een stickerboek.
#   - Elk gevonden dier heeft dezelfde witte stickerrand (2 px op 260, 3 px op 454), ook tijdens het inhouden.
#     Daardoor haalt elk dier 3:1 op elk blauw (wit op 0000AA is 12:1), ook kwal, maanvis en zeekomkommer.
#   - Zelfde passende maat per vak: elk dier past in hetzelfde vak (maat_voor_vak), geen "groter voor zeldzaam" meer in de sea log.
#   - Zelfde oog: straal volgt de vakmaat, niet de dierschaal.
# Nieuw of opnieuw: Squid (11) vervangen door Eel (murene, groen, golvend lijf, open bek): geen twee inktvissen meer.
#   Garnaal opnieuw als gekrulde C met waaierstaart; clownvis met zwart omrande witte banden; orka met grote witte oogvlek;
#   zeeotter met grotere kop; zeekomkommer (bonus) slaapt met "z z" boven zijn kop: de grap, terug na een pauze.
# Niet gevonden: egaal 000055 met buitenrand 00AAFF (W0, 8:1 op zwart, 5:1 op 0000AA), zelfde dikte als de stickerrand, geen nummer.
# Gijs: maak_dieren_data.py kan delen_v7 / TINT lezen zoals bij v5; de stickerrand is één extra laag: alle delen in wit,
#   2 px groter (op het horloge: hetzelfde dier eerst 8 keer in wit verschoven tekenen, dan in kleur erover).
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
import ebb_dieren_v5 as dv5
import ebb_dieren_v6 as dv6
from ebb_blad_v3 import bez, ellips, WIT, W0, W3
from ebb_dieren_v4 import poot
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

v3.TINT.update({
    'aal':     ((170,255,85),  (255,255,170), (0,170,0)),     # murene: geelgroen met donkere vlekjes
    'garnaal': ((255,170,170), (255,255,255), (255,85,85)),
    'orka':    ((0,0,0),       (255,255,255), (85,85,85)),
})
D_NU = 260                       # schermmaat waarop nu getekend wordt (blad_v7 zet hem); bepaalt de randdikte
def rand_px(): return max(2, round(D_NU/130))
SIL = (0,0,85); SIL_RAND = W0

def _buis(punten, dik):
    """Lijf als buis langs een lijn: dikte per punt."""
    links, rechts = [], []
    for i, (x, y) in enumerate(punten):
        a = punten[max(0, i-1)]; b = punten[min(len(punten)-1, i+1)]
        dx, dy = b[0]-a[0], b[1]-a[1]; n = math.hypot(dx, dy) or 1
        nx, ny = -dy/n, dx/n; t = dik[i]
        links.append((x + nx*t, y + ny*t)); rechts.append((x - nx*t, y - ny*t))
    return links + rechts[::-1]

def delen_v7(soort):
    if soort == 'aal':
        N = 26
        lijn = [(-0.95 + 1.95*i/(N-1), 0.16*math.sin(i/(N-1)*2.6*math.pi - 0.4)) for i in range(N)]
        dik = [0.22 if i < 4 else 0.22 - 0.15*(i-4)/(N-5) for i in range(N)]
        lijf = _buis(lijn, dik)
        vin = _buis([(x, y - d*0.95) for (x, y), d in zip(lijn[3:], dik[3:])], [0.07]*len(lijn[3:]))
        bek = [(-1.10,0.02),(-0.80,-0.02),(-0.80,0.10),(-1.08,0.12)]
        tand = [(-1.02,0.02),(-0.98,0.08),(-0.94,0.02)]
        vlek = [(ellips(x, y, 0.035, 0.03), 'donker') for x, y in zip([lijn[i][0] for i in (7, 11, 15, 19)], [lijn[i][1] for i in (7, 11, 15, 19)])]
        return [(vin, 'donker'), (lijf, 'lijf'), (bek, 'zwart'), (tand, 'witp')] + vlek, [(-0.78,-0.06)]
    if soort == 'garnaal':   # gekrulde C: kop links boven, rug omhoog, staart krult onder naar links terug
        N = 16; hoek = [math.radians(200 - 250*i/(N-1)) for i in range(N)]
        lijn = [(0.05 + 0.50*math.cos(a), 0.05 - 0.50*math.sin(a)) for a in hoek]
        dik = [0.26 - 0.15*i/(N-1) for i in range(N)]
        lijf = _buis(lijn, dik)
        ex, ey = lijn[-1]
        staart = [(ex+0.02, ey-0.04), (ex-0.30, ey-0.18), (ex-0.34, ey+0.06), (ex-0.02, ey+0.08)]
        segs = []
        for i in (4, 6, 8, 10, 12):
            (x, y), t = lijn[i], dik[i]
            a = lijn[i-1]; b = lijn[i+1]; dx, dy = b[0]-a[0], b[1]-a[1]; n = math.hypot(dx, dy); nx, ny = -dy/n, dx/n
            ux, uy = dx/n*0.025, dy/n*0.025
            segs.append(([(x+nx*t-ux, y+ny*t-uy), (x+nx*t+ux, y+ny*t+uy), (x-nx*t+ux, y-ny*t+uy), (x-nx*t-ux, y-ny*t-uy)], 'donker'))
        kx, ky = lijn[0]
        voel = [(poot(kx-0.05, ky-0.10, kx-0.10, ky-0.60, kx+0.35, ky-0.85, 0.035), 'donker'),
                (poot(kx-0.02, ky-0.05, kx+0.20, ky-0.50, kx+0.70, ky-0.62, 0.035), 'donker')]
        pootjes = [(poot(lijn[i][0], lijn[i][1], lijn[i][0]*0.6+0.02, lijn[i][1]*0.6+0.04, lijn[i][0]*0.35+0.03, lijn[i][1]*0.35+0.06, 0.04), 'donker') for i in (3, 5, 7)]
        snuit = [(kx-0.10, ky-0.12), (kx-0.42, ky-0.02), (kx-0.10, ky+0.06)]
        return voel + pootjes + [(staart, 'donker'), (lijf, 'lijf'), (snuit, 'donker')] + segs, [(kx+0.02, ky-0.08)]
    if soort == 'clown':     # witte banden met zwarte rand (het kenmerk van de clownvis, ook op 260)
        delen, ogen = dv5.delen_v5('clown')
        uit = []
        for p, r in delen:
            if r == 'licht':
                cx = sum(x for x, _ in p)/len(p)
                breed = [(cx + (x - cx)*1.55, y*1.0) for x, y in p]
                uit.append((breed, 'zwart'))
            uit.append((p, r))
        return uit, ogen
    if soort == 'orka':      # grote witte oogvlek en witte buik: het orkagezicht
        delen, ogen = dv5.delen_v5('orka')
        uit = [(p, r) for p, r in delen]
        uit.append((ellips(-0.46, -0.13, 0.20, 0.09), 'licht'))
        uit.append((ellips(0.30, -0.22, 0.16, 0.05), 'donker'))   # grijs zadel achter de vin
        return uit, ogen
    if soort == 'otter':     # kop 1,25 keer: het gezicht is wat je herkent
        delen, ogen = dv6.delen_v6('otter')
        kx, ky = -0.72, 0.02; k = 1.25
        kop_rollen = 5   # oren, kop, gezicht, neus staan op plek 5 tot 9
        uit = []
        for i, (p, r) in enumerate(delen):
            if 5 <= i <= 9:
                p = [(kx + (x - kx)*k, ky + (y - ky)*k) for x, y in p]
            uit.append((p, r))
        return uit, [(kx + (ogen[0][0]-kx)*k, ky + (ogen[0][1]-ky)*k)]
    if soort == 'komkom':    # slaapt: halfdichte ogen en "z z" boven zijn kop
        delen, ogen = dv6.delen_v6('komkom')
        def z(x0, y0, h):
            t = h*0.28
            return [(x0, y0), (x0+h, y0), (x0+h, y0+t), (x0+t*1.1, y0+h-t), (x0+h, y0+h-t), (x0+h, y0+h),
                    (x0, y0+h), (x0, y0+h-t), (x0+h-t*1.1, y0+t), (x0, y0+t)]
        return delen + [(z(-0.70, -0.80, 0.30), 'zz'), (z(-0.30, -1.25, 0.42), 'zz')], ogen
    return dv6.delen_v6(soort)

def dier_beeld(soort, s, kleur_override=None, hoek=0, oog_s=None):
    delen, ogen = delen_v7(soort)
    lijf, licht, donker = v3.TINT[soort]
    rol = {'lijf': lijf, 'licht': licht, 'donker': donker, 'zwart': (0,0,0), 'muts': dv5.MUTS, 'witp': WIT, 'zz': WIT}
    stil = kleur_override == 'silhouet'
    if isinstance(kleur_override, dict): rol = dict(kleur_override)
    elif kleur_override and not stil: rol = {k: kleur_override for k in rol}
    if hoek:
        ca, sa = math.cos(math.radians(-hoek)), math.sin(math.radians(-hoek))
        R_ = lambda pts: [(x*ca - y*sa, x*sa + y*ca) for x, y in pts]
        delen = [(R_(p), r) for p, r in delen]; ogen = R_(ogen)
    W = int(s*3.0) + 12; c = W/2
    vorm = Image.new('L', (W, W), 0); vd = ImageDraw.Draw(vorm)
    for pts, r in delen:
        if r != 'zz': vd.polygon([(c + x*s, c + y*s) for x, y in pts], fill=255)
    k = rand_px()
    groot = vorm.filter(ImageFilter.MaxFilter(2*k + 1))
    im = Image.new('RGBA', (W, W), (0,0,0,0))
    if stil:
        im.paste(Image.new('RGBA', (W, W), SIL_RAND + (255,)), (0, 0), groot)
        im.paste(Image.new('RGBA', (W, W), SIL + (255,)), (0, 0), vorm)
    else:
        if not kleur_override:   # de stickerrand: zelfde dikte voor elk dier
            im.paste(Image.new('RGBA', (W, W), WIT + (255,)), (0, 0), groot)
        d = ImageDraw.Draw(im)
        for pts, r in delen:
            if r == 'zz' and kleur_override: continue
            d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=rol[r] + (255,))
        if not kleur_override:
            os_ = oog_s or s
            for ox, oy in ogen:
                R = max(2.0, 0.13*os_); p = max(1.2, 0.07*os_); x, y = c + ox*s, c + oy*s
                d.ellipse([x-R, y-R, x+R, y+R], fill=WIT + (255,))
                d.ellipse([x-p-R*0.3, y-p, x+p-R*0.3, y+p], fill=W3 + (255,))
                if soort in dv5.SLAPERIG:
                    d.chord([x-R, y-R, x+R, y+R], 180, 360, fill=donker + (255,))
                elif os_ >= 30:
                    g = max(1, 0.035*os_); d.ellipse([x-R*0.55-g, y-R*0.5-g, x-R*0.55+g, y-R*0.5+g], fill=WIT + (255,))
    a = np.array(im)[:, :, 3] > 0; ys, xs = np.nonzero(a)
    return im, (xs.mean() + 0.5, ys.mean() + 0.5), a.sum()

def maat_voor_vak(soort, w, h):
    """Schaal waarbij het dier (zonder rand) precies in een vak van w bij h px past: zelfde passende maat voor elk dier."""
    delen, _ = delen_v7(soort)
    xs = [x for p, _ in delen for x, _ in p]; ys = [y for p, _ in delen for _, y in p]
    return min(w/(max(xs)-min(xs)), h/(max(ys)-min(ys)))

v3.dier_delen = delen_v7
v3.dier_beeld = dier_beeld

ALLE = [(('aal', 'Eel') if s == 'inktvis' else (s, n)) for s, n in dv6.ALLE]
