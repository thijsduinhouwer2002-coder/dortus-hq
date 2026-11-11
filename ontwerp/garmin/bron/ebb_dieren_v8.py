# Ebb dieren v8 (Mila, 11 nov run 28): "Voor Mila" in ontwerp/garmin/ebb-bouw-1-keuring-drie.md.
# Bouwt op ebb_dieren_v7.py. Alleen wat verandert staat hier.
# 1. Elk dier één eigen kenmerk dat ook als omtrek overeind blijft. Nieuw: rollen 'licht_k' en 'donker_k' (kenmerk):
#    gevonden tekenen ze als licht of donker, als silhouet (niet gevonden) in de randkleur 00AAFF, dus als uitsparing.
#    Orka: hoge rugvin + witte oogvlek (uitsparing). Haai: rechte hoge rugvin + drie kieuwen (uitsparing).
#    Dolfijn: gebogen rug (springt) + snuit. Zwaardvis: zwaard + sikkelstaart. Narwal: rechte gedraaide tand (draai als uitsparing).
#    Zeehond: kop omhoog + flippers. Clownvis: banden als uitsparing. Manta: kopvinnen. Rog: ronde schijf.
# 2. Opnieuw en compact (vak 40 x 32 op 260): zeeotter, zeekomkommer (zonder Zzz, mint in plaats van rood), kreeft, maanvis.
# 3. Silhouet: alleen de buitenomtrek (gaten en smalle spleten dicht, dus garnaal zonder binnenlijnen), plus de kenmerken.
#    Eén oogvorm: wit oog met pupil, glans vanaf maat 30; geen halfdicht oog meer. Zeepaardje even hoog als de rest.
#    Orka-lijf donkergrijs (85,85,85).
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
import ebb_dieren_v5 as dv5
import ebb_dieren_v6 as dv6
import ebb_dieren_v7 as dv7
from ebb_blad_v3 import bez, ellips, WIT, W0, W3
from ebb_dieren_v4 import poot
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from scipy import ndimage

v3.TINT.update({
    'orka':    ((85,85,85),    (255,255,255), (170,170,170)),   # lijf donkergrijs, zadel lichtgrijs
    'komkom':  ((85,255,170),  (170,255,255), (0,170,85)),      # mint, niet rood
    'kreeft':  ((255,85,85),   (255,170,170), (170,0,0)),
    'otter':   ((255,170,85),  (255,255,170), (170,85,0)),
    'maanvis': ((170,170,255), (255,255,255), (85,85,170)),
})
SIL = dv7.SIL; SIL_RAND = dv7.SIL_RAND
D_NU = 260
def rand_px(): return max(2, round(D_NU/130))

def buig(delen, ogen, k):
    """Gebogen rug: y + k*x^2 (springende dolfijn)."""
    f = lambda pts: [(x, y + k*x*x) for x, y in pts]
    return [(f(p), r) for p, r in delen], f(ogen)

def delen_v8(soort):
    if soort == 'orka':
        lijf = bez((-1.0,0.05),(-0.70,-0.40),(0.30,-0.28),10) + bez((0.30,-0.28),(0.65,-0.15),(0.78,0.0),6) \
             + bez((0.78,0.0),(0.40,0.30),(-0.20,0.30),6) + bez((-0.20,0.30),(-0.80,0.30),(-1.0,0.05),8)
        buik = bez((-0.95,0.12),(-0.40,0.05),(0.20,0.18),6) + bez((0.20,0.18),(-0.40,0.32),(-0.95,0.16),6)
        vin = [(-0.16,-0.30),(-0.02,-1.10),(0.10,-1.08),(0.22,-0.28)]           # hoog en recht: het orkateken
        staart = [(0.72,-0.04),(1.05,-0.35),(0.98,0.0),(1.05,0.30)]
        flip = [(-0.45,0.22),(-0.25,0.58),(-0.10,0.26)]
        zadel = ellips(0.32, -0.22, 0.17, 0.05)
        oogvlek = ellips(-0.44, -0.12, 0.22, 0.10)
        return [(staart,'lijf'), (vin,'lijf'), (flip,'lijf'), (lijf,'lijf'), (buik,'licht'), (zadel,'donker'), (oogvlek,'licht_k')], [(-0.66,-0.04)]
    if soort == 'haai':
        lijf = bez((-1.05,0.06),(-0.60,-0.36),(0.30,-0.24),10) + bez((0.30,-0.24),(0.65,-0.12),(0.80,-0.02),6) \
             + bez((0.80,-0.02),(0.50,0.24),(0.0,0.24),6) + bez((0.0,0.24),(-0.60,0.24),(-1.05,0.06),8)
        buik = bez((-1.0,0.09),(-0.40,0.04),(0.30,0.14),6) + bez((0.30,0.14),(-0.40,0.26),(-1.0,0.11),6)
        vin = [(-0.30,-0.28),(0.06,-0.92),(0.12,-0.90),(0.14,-0.24)]             # rechte achterkant, hoog
        staart = [(0.74,-0.04),(1.10,-0.62),(1.00,-0.02),(1.04,0.24)]            # bovenste lob lang
        flip = [(-0.40,0.20),(-0.18,0.56),(-0.06,0.22)]
        kieuw = [([(x,-0.12),(x+0.05,-0.12),(x+0.05,0.10),(x,0.10)],'donker_k') for x in (-0.52,-0.40,-0.28)]
        return [(staart,'lijf'), (vin,'lijf'), (flip,'donker'), (lijf,'lijf'), (buik,'licht')] + kieuw, [(-0.78,-0.08)]
    if soort == 'dolfijn':
        lijf = bez((-0.66,-0.02),(-0.55,-0.42),(0.30,-0.28),10) + bez((0.30,-0.28),(0.70,-0.16),(0.84,-0.04),6) \
             + bez((0.84,-0.04),(0.55,0.22),(0.05,0.24),6) + bez((0.05,0.24),(-0.50,0.24),(-0.66,0.08),8)
        snavel = [(-0.62,-0.02),(-1.10,0.04),(-1.10,0.12),(-0.60,0.12)]
        buik = bez((-1.0,0.08),(-0.40,0.02),(0.30,0.15),6) + bez((0.30,0.15),(-0.40,0.25),(-1.0,0.11),6)
        vin = bez((-0.12,-0.30),(0.02,-0.66),(0.34,-0.70),5) + bez((0.34,-0.70),(0.14,-0.48),(0.22,-0.26),5)
        staart = [(0.76,-0.06),(1.06,-0.36),(0.98,-0.02),(1.08,0.26)]
        flip = [(-0.30,0.18),(-0.06,0.50),(0.04,0.20)]
        return buig([(staart,'lijf'), (vin,'donker'), (flip,'donker'), (lijf,'lijf'), (snavel,'lijf'), (buik,'licht')], [(-0.48,-0.10)], 0.30)
    if soort == 'zwaard':
        lijf = bez((-0.62,0.0),(-0.40,-0.30),(0.20,-0.22),8) + bez((0.20,-0.22),(0.55,-0.10),(0.62,0.0),5) \
             + bez((0.62,0.0),(0.40,0.18),(0.0,0.20),5) + bez((0.0,0.20),(-0.45,0.22),(-0.62,0.0),8)
        zwaard = [(-0.58,-0.06),(-1.22,0.0),(-0.58,0.06)]
        buik = ellips(-0.05, 0.08, 0.50, 0.11, 0, 180)
        zeil = bez((-0.36,-0.20),(-0.20,-0.85),(0.30,-0.20),8)
        # sikkelstaart: halve maan, punten ver naar achteren
        staart = bez((0.56,0.0),(0.80,-0.30),(1.10,-0.62),5) + bez((1.10,-0.62),(0.86,-0.12),(0.78,0.0),4) \
               + bez((0.78,0.0),(0.86,0.12),(1.10,0.62),4) + bez((1.10,0.62),(0.80,0.30),(0.56,0.0),5)
        return [(staart,'donker'), (zeil,'donker'), (zwaard,'donker'), (lijf,'lijf'), (buik,'licht')], [(-0.40,-0.06)]
    if soort == 'narwal':
        lijf = bez((-0.70,0.02),(-0.72,-0.34),(-0.20,-0.32),10) + bez((-0.20,-0.32),(0.45,-0.26),(0.78,-0.02),8) \
             + bez((0.78,-0.02),(0.40,0.30),(-0.20,0.30),6) + bez((-0.20,0.30),(-0.70,0.32),(-0.70,0.02),8)
        buik = ellips(-0.10, 0.16, 0.50, 0.11)
        tand = [(-0.66,-0.15),(-1.32,-0.12),(-1.32,-0.04),(-0.66,-0.01)]          # recht en dikker, leest op 260
        draai = [([(x-0.03,-0.13),(x+0.01,-0.13),(x+0.05,-0.03),(x+0.01,-0.03)], 'donker_k') for x in (-0.82, -0.98, -1.14)]
        vlek = [(ellips(x, y, 0.06, 0.045), 'donker') for x, y in ((-0.15,-0.18), (0.10,-0.12), (0.34,-0.10), (0.50,-0.02))]
        staart = [(0.70,-0.04),(1.02,-0.34),(0.94,0.0),(1.02,0.30)]
        flip = [(-0.38,0.20),(-0.22,0.50),(-0.08,0.22)]
        return [(staart,'donker'), (flip,'donker'), (tand,'licht'), (lijf,'lijf'), (buik,'licht')] + vlek + draai, [(-0.48,-0.10)]
    if soort == 'zeehond':
        # banaan: kop hoog omhoog links, achterflippers omhoog rechts, voorflipper naar beneden
        lijf = bez((-0.62,-0.40),(-0.55,0.00),(-0.10,0.12),8) + bez((-0.10,0.12),(0.40,0.14),(0.80,-0.18),8) \
             + bez((0.80,-0.18),(0.82,0.30),(0.20,0.36),8) + bez((0.20,0.36),(-0.70,0.40),(-0.86,-0.36),10)
        kop = ellips(-0.74, -0.52, 0.24, 0.21)
        snuit = ellips(-0.95, -0.46, 0.13, 0.10)
        neus = ellips(-1.05, -0.52, 0.05, 0.04)
        buik = bez((-0.80,-0.10),(-0.50,0.30),(0.40,0.28),6) + bez((0.40,0.28),(-0.40,0.40),(-0.82,0.00),6)
        flip = [(-0.40,0.26),(-0.30,0.66),(-0.10,0.64),(-0.16,0.26)]
        staart = [(0.70,-0.10),(0.86,-0.56),(0.96,-0.30),(1.14,-0.48),(0.92,-0.04)]
        vlek = [(ellips(x, y, 0.05, 0.04), 'donker') for x, y in ((-0.40,0.10), (0.05,0.20), (0.45,0.10))]
        return [(staart,'donker'), (lijf,'lijf'), (buik,'licht'), (flip,'donker'), (kop,'lijf'), (snuit,'licht'), (neus,'zwart')] + vlek, [(-0.72,-0.60)]
    if soort == 'clown':
        delen, ogen = dv7.delen_v7('clown')
        return [(p, 'licht_k' if r == 'licht' else r) for p, r in delen], ogen
    if soort == 'manta':
        lijf = bez((-1.15,-0.04),(-0.55,-0.42),(-0.18,-0.26),8) + bez((0.18,-0.26),(0.55,-0.42),(1.15,-0.04),8) \
             + bez((1.15,-0.04),(0.45,0.10),(0.12,0.32),6) + bez((-0.12,0.32),(-0.45,0.10),(-1.15,-0.04),6)
        kopvin = [[(k*0.10,-0.24),(k*0.12,-0.58),(k*0.22,-0.66),(k*0.30,-0.56),(k*0.26,-0.24)] for k in (-1, 1)]   # twee hoorns naar voren
        staart = [(-0.03,0.28),(0.03,0.28),(0.01,0.78),(-0.01,0.78)]
        buik = bez((-0.70,0.0),(0,0.06),(0.70,0.0),6) + bez((0.70,0.0),(0.20,0.18),(-0.70,0.0),6)
        mond = ellips(0, 0.05, 0.16, 0.05)
        return [(staart,'lijf'), (kopvin[0],'lijf'), (kopvin[1],'lijf'), (lijf,'lijf'), (buik,'licht'), (mond,'zwart')], [(-0.15,-0.14), (0.15,-0.14)]
    if soort == 'rog':
        schijf = ellips(0, 0, 0.60, 0.54)
        staart = [(-0.03,0.45),(0.03,0.45),(0.02,1.0),(-0.02,1.0)]
        stip = [(ellips(x, y, 0.06, 0.05), 'donker') for x, y in ((-0.34,0.06), (0.34,0.06), (0.0,0.26), (-0.18,-0.32), (0.18,-0.32))]
        return [(staart,'donker'), (schijf,'lijf')] + stip, [(-0.16,-0.10), (0.16,-0.10)]
    if soort == 'maanvis':   # compact: korte vinnen schuin naar achteren
        lijf = ellips(0, 0, 0.60, 0.54)
        vin_b = [(0.02,-0.48),(0.42,-0.86),(0.40,-0.38)]; vin_o = [(0.02,0.48),(0.42,0.86),(0.40,0.38)]
        staart = bez((0.52,-0.36),(0.74,-0.20),(0.70,0.0),4) + bez((0.70,0.0),(0.74,0.20),(0.52,0.36),4)
        buik = ellips(-0.02, 0.10, 0.48, 0.36, 20, 160)
        mond = ellips(-0.58, 0.06, 0.06, 0.05)
        return [(vin_b,'donker'), (vin_o,'donker'), (staart,'donker'), (lijf,'lijf'), (buik,'licht'), (mond,'donker')], [(-0.30,-0.14)]
    if soort == 'kreeft':    # bovenaanzicht, scharen breed open: past in 40 x 32
        lijf = ellips(0, 0.0, 0.24, 0.36)
        staart = [(-0.18,0.30),(0.18,0.30),(0.14,0.58),(0.30,0.76),(0,0.70),(-0.30,0.76),(-0.14,0.58)]
        ringen = [([(-0.22,y),(0.22,y),(0.22,y+0.05),(-0.22,y+0.05)],'donker') for y in (0.10, 0.24)]
        delen = []
        for k in (-1, 1):
            delen.append((poot(k*0.18, -0.20, k*0.50, -0.20, k*0.62, -0.42, 0.09), 'lijf'))
            delen.append((ellips(k*0.70, -0.56, 0.24, 0.17), 'licht'))
            delen.append(([(k*0.64,-0.62),(k*0.62,-0.84),(k*0.80,-0.76)], 'zwart'))   # schaar open
        voel = [(poot(k*0.06, -0.32, k*0.22, -0.70, k*0.06, -0.86, 0.035), 'donker') for k in (-1, 1)]
        pootjes = [(poot(k*0.20, y, k*0.42, y+0.04, k*0.50, y+0.14, 0.035), 'donker') for k in (-1, 1) for y in (-0.02, 0.12)]
        return voel + pootjes + delen + [(staart,'lijf'), (lijf,'lijf')] + ringen, [(-0.11,-0.24), (0.11,-0.24)]
    if soort == 'otter':     # compact: op de rug, opgekruld, schelp op de buik, voeten omhoog
        lijf = bez((-0.40,0.05),(-0.05,-0.36),(0.48,-0.14),8) + bez((0.48,-0.14),(0.66,0.04),(0.50,0.22),4) \
             + bez((0.50,0.22),(0.05,0.36),(-0.40,0.24),8)
        buik = bez((-0.32,-0.02),(0.05,-0.26),(0.44,-0.10),6) + bez((0.44,-0.10),(0.10,0.04),(-0.32,0.08),6)
        kop = ellips(-0.56, -0.02, 0.32, 0.29)
        gezicht = ellips(-0.60, 0.03, 0.23, 0.19)
        oor = [ellips(-0.76, -0.25, 0.07, 0.06), ellips(-0.38, -0.28, 0.07, 0.06)]
        neus = ellips(-0.78, 0.00, 0.06, 0.05)
        schelp = bez((-0.24,-0.06),(-0.02,-0.48),(0.20,-0.06),6) + [(-0.02,0.00)]
        handen = [ellips(-0.18, -0.10, 0.08, 0.07), ellips(0.14, -0.10, 0.08, 0.07)]
        voet1 = [(0.38,-0.14),(0.46,-0.52),(0.58,-0.50),(0.54,-0.10)]
        voet2 = [(0.54,-0.06),(0.72,-0.40),(0.82,-0.32),(0.66,0.02)]
        return [(voet1,'donker'), (voet2,'donker'), (lijf,'lijf'), (buik,'licht'), (oor[0],'lijf'), (oor[1],'lijf'),
                (kop,'lijf'), (gezicht,'licht'), (neus,'zwart'), (schelp,'muts'), (handen[0],'donker'), (handen[1],'donker')], [(-0.56,-0.08)]
    if soort == 'komkom':    # bonus: dikke boon met voetjes en een kroontje voelers, glimlach, zonder Zzz
        lijf = bez((-0.70,0.06),(-0.70,-0.40),(-0.10,-0.38),8) + bez((-0.10,-0.38),(0.62,-0.36),(0.70,0.04),8) \
             + bez((0.70,0.04),(0.66,0.36),(0.0,0.36),8) + bez((0.0,0.36),(-0.70,0.38),(-0.70,0.06),8)
        buik = bez((-0.58,0.16),(0.0,0.10),(0.58,0.16),6) + bez((0.58,0.16),(0.0,0.40),(-0.58,0.16),6)
        bult = [(ellips(x, -0.30 + 0.10*abs(x), 0.09, 0.07), 'donker') for x in (-0.30, 0.0, 0.30, 0.54)]
        voet = [(ellips(x, 0.38, 0.06, 0.06), 'donker') for x in (-0.40, -0.14, 0.12, 0.38)]
        kroon = [(ellips(-0.80 + 0.10*math.cos(a), -0.12 + 0.12*math.sin(a), 0.07, 0.06), 'licht') for a in (math.radians(140), math.radians(180), math.radians(220))]
        lach = bez((-0.66,0.10),(-0.56,0.20),(-0.44,0.10),4) + bez((-0.44,0.10),(-0.56,0.15),(-0.66,0.10),4)
        return voet + kroon + [(lijf,'lijf'), (buik,'licht')] + bult + [(lach,'zwart')], [(-0.50,-0.10)]
    if soort == 'garnaal':   # rol 'sil': alleen in het silhouet, vult de krul zodat de omtrek geen binnenlijnen heeft
        delen, ogen = dv7.delen_v7('garnaal')
        return [(ellips(0.05, 0.08, 0.44, 0.40), 'sil')] + delen, ogen
    return dv7.delen_v7(soort)

KENMERK = {'licht_k': 'licht', 'donker_k': 'donker'}

def _vorm(delen, s, c, W, stil=False):
    m = Image.new('L', (W, W), 0); d = ImageDraw.Draw(m)
    for pts, r in delen:
        if r != 'zz' and (stil or r != 'sil'): d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=255)
    return m

SLUIT = {'krab': 0.03}   # alleen hier spleten dichtmaken (garnaal: de krul); armen en poten van de rest blijven los
def buitenvorm(vorm, s, soort=None):
    """Alleen de buitenomtrek: gaten gevuld; bij de dieren in SLUIT ook smalle spleten dicht."""
    a = np.array(vorm) > 0
    if soort not in SLUIT: return Image.fromarray((ndimage.binary_fill_holes(a)*255).astype('uint8'))
    r = max(1, round(s*SLUIT[soort]))
    st = np.ones((2*r+1, 2*r+1), bool)
    dicht = ndimage.binary_closing(np.pad(a, r+2), structure=st)[r+2:-(r+2), r+2:-(r+2)]
    dicht = ndimage.binary_fill_holes(dicht | a)
    return Image.fromarray((dicht*255).astype('uint8'))

def dier_beeld(soort, s, kleur_override=None, hoek=0, oog_s=None):
    delen, ogen = delen_v8(soort)
    lijf, licht, donker = v3.TINT[soort]
    rol = {'lijf': lijf, 'licht': licht, 'donker': donker, 'zwart': (0,0,0), 'muts': dv5.MUTS, 'witp': WIT, 'zz': WIT,
           'licht_k': licht, 'donker_k': donker}
    if kleur_override == 'hint': kleur_override = 'silhouet'      # v8: het silhouet ís al met kenmerk
    stil = kleur_override == 'silhouet'
    if isinstance(kleur_override, dict): rol.update(kleur_override)
    elif kleur_override and not stil: rol = {k: kleur_override for k in rol}
    if hoek:
        ca, sa = math.cos(math.radians(-hoek)), math.sin(math.radians(-hoek))
        R_ = lambda pts: [(x*ca - y*sa, x*sa + y*ca) for x, y in pts]
        delen = [(R_(p), r) for p, r in delen]; ogen = R_(ogen)
    W = int(s*3.2) + 12; c = W/2
    vorm = _vorm(delen, s, c, W, stil)
    k = rand_px()
    im = Image.new('RGBA', (W, W), (0,0,0,0))
    if stil:
        buiten = buitenvorm(vorm, s, soort)
        groot = buiten.filter(ImageFilter.MaxFilter(2*k + 1))
        im.paste(Image.new('RGBA', (W, W), SIL_RAND + (255,)), (0, 0), groot)
        im.paste(Image.new('RGBA', (W, W), SIL + (255,)), (0, 0), buiten)
        d = ImageDraw.Draw(im)
        for pts, r in delen:
            if r in KENMERK: d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=SIL_RAND + (255,))
    else:
        if not kleur_override:
            groot = vorm.filter(ImageFilter.MaxFilter(2*k + 1))
            im.paste(Image.new('RGBA', (W, W), WIT + (255,)), (0, 0), groot)
        d = ImageDraw.Draw(im)
        for pts, r in delen:
            if (r == 'zz' and kleur_override) or r == 'sil': continue
            d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=rol[r] + (255,))
        if not kleur_override:      # één oogvorm voor alle dieren
            os_ = oog_s or s
            for ox, oy in ogen:
                R = max(2.0, 0.13*os_); p = max(1.2, 0.07*os_); x, y = c + ox*s, c + oy*s
                d.ellipse([x-R, y-R, x+R, y+R], fill=WIT + (255,))
                d.ellipse([x-p-R*0.3, y-p, x+p-R*0.3, y+p], fill=W3 + (255,))
                if os_ >= 30:
                    g = max(1, 0.035*os_); d.ellipse([x-R*0.55-g, y-R*0.5-g, x-R*0.55+g, y-R*0.5+g], fill=WIT + (255,))
    a = np.array(im)[:, :, 3] > 0; ys, xs = np.nonzero(a)
    return im, (xs.mean() + 0.5, ys.mean() + 0.5), a.sum()

def maat_voor_vak(soort, w, h):
    delen, _ = delen_v8(soort)
    xs = [x for p, _ in delen for x, _ in p]; ys = [y for p, _ in delen for _, y in p]
    bw, bh = max(xs)-min(xs), max(ys)-min(ys)
    # zeepaardje: hele vakhoogte, net als kwal, krab, zeester en kreeft (37 px met rand op 260); geen uitzondering meer
    return min(w/bw, h/bh)

v3.dier_delen = delen_v8
v3.dier_beeld = dier_beeld
dv7.delen_v7_oud = dv7.delen_v7

ALLE = dv7.ALLE
RAND = {s: WIT for s, _ in ALLE}
ROL_V8 = {'lijf': 0, 'licht': 1, 'donker': 2, 'zwart': 3, 'muts': 4, 'witp': 5, 'zz': 6, 'licht_k': 7, 'donker_k': 8, 'sil': 9}
