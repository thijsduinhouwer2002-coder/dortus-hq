# Ebb dieren v5 (Mila, 11 nov run 23): moet-punt V6 van de keuring van blad v4.1.
# Eén tekenregel voor alle 24: zelfde oog (wit, pupil naar voren, glans), lijf / licht / donker,
# en een lichte rand (1 tot 2 px) om donkere dieren zodat ze op diep water niet verdwijnen.
# Opnieuw: zeekomkommer (met slaapmuts: de grap), zeeotter, zeehond. Rog en manta uit elkaar.
# Zeldzame dieren (haai, orka, manta, zwaardvis) lichter of met rand, en iets groter op het eindscherm.
# Gebruik: python3 ebb_dieren_v5.py <uitmap> <font>
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
import ebb_dieren_v4 as dv4
from ebb_blad_v3 import bez, ellips, leeg, rand, zee, W1, W2, W3, SCHUIM, WIT, teken, niet_mip
from ebb_dieren_v4 import poot, ALLE
from PIL import Image, ImageDraw
import numpy as np

v3.TINT.update({
    'komkom': ((255,85,85),  (255,170,170), (170,0,0)),      # koraalroze, ligt goed op elk blauw
    'otter':  ((170,85,0),   (255,255,170), (85,0,0)),       # bruin met een licht gezicht en buik
    'zeehond':((170,170,170),(255,255,255), (85,85,85)),     # grijs met vlekjes
    'rog':    ((85,170,170), (170,255,255), (0,85,85)),      # klein, teal, stippen, ruit
    'manta':  ((85,85,85),   (255,255,255), (0,0,0)),        # breed, zwart met witte buik en rand
    'haai':   ((170,170,255),(255,255,255), (85,85,170)),    # lichter
    'zwaard': ((85,170,255), (255,255,255), (85,85,255)),    # zwaard, zeil en staart zichtbaar op diep water
    'orka':   ((0,0,0),      (255,255,255), (85,85,85)),
})
RAND = {'orka': (170,170,255), 'manta': (170,170,255), 'zwaard': (170,255,255), 'haai': (85,85,170)}
MUTS = (85, 85, 255)
# Spook (dier dat je nog niet hebt): geen platte vlek maar het dier in drie donkere blauwen, zodat staart, vinnen,
# banden en buik te zien blijven, plus een klein licht oog. De lichte rand tekent blad_v5.silhouet eromheen.
SPOOK = {'lijf': (0,0,85), 'licht': (0,0,170), 'donker': (0,85,170), 'zwart': (0,0,0), 'muts': (0,0,170), 'witp': (0,85,170)}
SPOOK_OOG = (170,255,255)

def delen_v5(soort):
    if soort == 'komkom':
        # zeekomkommer: zacht en bobbelig, pootjes eronder, halfdichte ogen en een slaapmuts (komt terug na een pauze)
        lijf = bez((-0.95,0.10),(-0.95,-0.38),(-0.40,-0.34),8) + bez((-0.40,-0.34),(0.30,-0.30),(0.92,-0.10),8) \
             + bez((0.92,-0.10),(1.02,0.22),(0.60,0.28),6) + bez((0.60,0.28),(-0.20,0.32),(-0.95,0.10),8)
        buik = bez((-0.85,0.14),(-0.20,0.10),(0.80,0.12),6) + bez((0.80,0.12),(0.20,0.30),(-0.85,0.20),6)
        bobbels = [(ellips(x, -0.31 + 0.10*(x > 0.4), 0.10, 0.08), 'donker') for x in (-0.15, 0.15, 0.45, 0.72)]
        pootjes = [(ellips(x, 0.30, 0.06, 0.07), 'donker') for x in (-0.55, -0.25, 0.05, 0.35, 0.62)]
        muts = [(-0.95,-0.22),(-0.40,-0.36),(-0.30,-0.86)]           # puntmuts over de kop, punt naar achteren
        pompon = ellips(-0.22, -0.92, 0.10, 0.10)
        rand_ = [(-0.98,-0.20),(-0.38,-0.38),(-0.36,-0.28),(-0.96,-0.10)]
        return pootjes + [(lijf,'lijf'), (buik,'licht')] + bobbels + [(muts,'muts'), (rand_,'witp'), (pompon,'witp')], [(-0.66,-0.04)]
    if soort == 'otter':
        # zeeotter drijft op zijn rug: kop links met licht gezicht en oortjes, buik boven, schelp op de buik, voetjes rechts omhoog
        lijf = bez((-0.55,-0.05),(-0.10,-0.40),(0.55,-0.20),8) + bez((0.55,-0.20),(0.95,-0.05),(0.80,0.20),6) \
             + bez((0.80,0.20),(0.20,0.40),(-0.55,0.25),8)
        buik = bez((-0.45,-0.10),(0.05,-0.36),(0.55,-0.18),6) + bez((0.55,-0.18),(0.10,-0.10),(-0.45,0.02),6)
        kop = ellips(-0.68, -0.02, 0.32, 0.30)
        gezicht = ellips(-0.74, 0.04, 0.22, 0.18)
        oor = [ellips(-0.86, -0.30, 0.08, 0.07), ellips(-0.52, -0.31, 0.08, 0.07)]
        neus = ellips(-0.90, 0.04, 0.06, 0.05)
        schelp = ellips(-0.10, -0.38, 0.16, 0.11)
        ribbel = [(-0.10,-0.48),(-0.08,-0.48),(-0.08,-0.28),(-0.10,-0.28)]
        poot_l = ellips(-0.28, -0.36, 0.08, 0.07); poot_r = ellips(0.08, -0.37, 0.08, 0.07)
        voet = [(0.62,-0.18),(0.80,-0.52),(0.92,-0.46),(0.80,-0.12)]
        staart = [(0.80,0.10),(1.10,0.02),(1.08,0.20),(0.82,0.24)]
        return [(staart,'donker'), (voet,'donker'), (lijf,'lijf'), (buik,'licht'), (oor[0],'lijf'), (oor[1],'lijf'), (kop,'lijf'),
                (gezicht,'licht'), (neus,'donker'), (schelp,'witp'), (ribbel,'lijf'), (poot_l,'donker'), (poot_r,'donker')], [(-0.66,-0.10)]
    if soort == 'zeehond':
        # zeehond: dikke traan die naar links kijkt, snuit met snorpuntjes, vlekjes, achterflippers als staart
        lijf = bez((-0.90,0.02),(-0.85,-0.42),(-0.35,-0.38),8) + bez((-0.35,-0.38),(0.35,-0.30),(0.82,0.04),8) \
             + bez((0.82,0.04),(0.35,0.36),(-0.35,0.32),8) + bez((-0.35,0.32),(-0.90,0.30),(-0.90,0.02),6)
        buik = bez((-0.80,0.16),(-0.20,0.10),(0.55,0.14),6) + bez((0.55,0.14),(-0.20,0.34),(-0.80,0.26),6)
        flip = [(-0.30,0.22),(-0.05,0.58),(0.10,0.26)]
        staart = [(0.74,0.02),(1.08,-0.20),(0.98,0.06),(1.08,0.30)]
        snuit = ellips(-0.86, 0.04, 0.12, 0.10)
        neus = ellips(-0.96, -0.02, 0.05, 0.04)
        vlek = [(ellips(x, y, 0.05, 0.04), 'donker') for x, y in ((-0.10,-0.22), (0.18,-0.14), (0.40,-0.04), (0.05,-0.02))]
        snor = [(ellips(-0.82+dx, 0.06+dy, 0.018, 0.018), 'donker') for dx, dy in ((0,0), (0.05,0.03), (-0.02,0.05))]
        return [(staart,'donker'), (lijf,'lijf'), (buik,'licht'), (flip,'donker'), (snuit,'licht'), (neus,'zwart')] + vlek + snor, [(-0.58,-0.18)]
    if soort == 'rog':
        # rog: kleine ruit, stippen, dunne staart; ogen bovenop
        lijf = [(-0.80,0.0),(0.0,-0.55),(0.80,0.0),(0.0,0.45)]
        staart = [(-0.03,0.40),(0.03,0.40),(0.02,1.0),(-0.02,1.0)]
        stip = [(ellips(x, y, 0.06, 0.05), 'donker') for x, y in ((-0.35,0.02), (0.35,0.02), (0.0,0.22), (-0.15,-0.30), (0.15,-0.30))]
        return [(staart,'donker'), (lijf,'lijf')] + stip, [(-0.16,-0.10), (0.16,-0.10)]
    if soort == 'manta':
        # manta: heel breed met puntige vleugels, hoorntjes, witte buik en brede mond
        lijf = bez((-1.15,-0.10),(-0.55,-0.40),(-0.16,-0.28),8) + [(-0.22,-0.55),(-0.08,-0.32),(0.08,-0.32),(0.22,-0.55)] \
             + bez((0.16,-0.28),(0.55,-0.40),(1.15,-0.10),8) + bez((1.15,-0.10),(0.45,0.10),(0.12,0.32),6) + bez((-0.12,0.32),(-0.45,0.10),(-1.15,-0.10),6)
        staart = [(-0.03,0.28),(0.03,0.28),(0.01,0.75),(-0.01,0.75)]
        buik = bez((-0.70,-0.02),(0,0.05),(0.70,-0.02),6) + bez((0.70,-0.02),(0.20,0.18),(-0.70,-0.02),6)
        mond = ellips(0, 0.05, 0.16, 0.05)
        return [(staart,'lijf'), (lijf,'lijf'), (buik,'licht'), (mond,'zwart')], [(-0.15,-0.16), (0.15,-0.16)]
    return dv4.nieuwe_delen(soort)

SLAPERIG = {'komkom'}
def dier_beeld(soort, s, kleur_override=None, hoek=0):
    delen, ogen = delen_v5(soort)
    lijf, licht, donker = v3.TINT[soort]
    rol = {'lijf': lijf, 'licht': licht, 'donker': donker, 'zwart': (0,0,0), 'muts': MUTS, 'witp': WIT}
    spook = isinstance(kleur_override, dict)
    if spook: rol = dict(kleur_override)
    elif kleur_override: rol = {k: kleur_override for k in rol}
    if hoek:
        ca, sa = math.cos(math.radians(-hoek)), math.sin(math.radians(-hoek))
        R_ = lambda pts: [(x*ca - y*sa, x*sa + y*ca) for x, y in pts]
        delen = [(R_(p), r) for p, r in delen]; ogen = R_(ogen)
    W = int(s*2.8) + 6; c = W/2
    im = Image.new('RGBA', (W, W), (0,0,0,0)); d = ImageDraw.Draw(im)
    if soort in RAND and not kleur_override and not spook:   # lichte rand: hetzelfde dier, iets verschoven, eronder
        k = max(1, round(s/45))
        for ox, oy in ((-k,0),(k,0),(0,-k),(0,k)):
            for pts, r in delen:
                d.polygon([(c + x*s + ox, c + y*s + oy) for x, y in pts], fill=RAND[soort] + (255,))
    for pts, r in delen:
        d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=rol[r] + (255,))
    if spook:   # klein licht oog, zodat je ziet waar de kop zit
        for ox, oy in ogen:
            R = max(1.5, 0.08*s); x, y = c + ox*s, c + oy*s
            d.ellipse([x-R, y-R, x+R, y+R], fill=SPOOK_OOG + (255,))
    elif not kleur_override:
        for ox, oy in ogen:
            R = max(2.0, 0.13*s); p = max(1.2, 0.07*s); x, y = c + ox*s, c + oy*s
            d.ellipse([x-R, y-R, x+R, y+R], fill=WIT + (255,))
            d.ellipse([x-p-R*0.3, y-p, x+p-R*0.3, y+p], fill=W3 + (255,))
            if soort in SLAPERIG:
                d.chord([x-R, y-R, x+R, y+R], 180, 360, fill=donker + (255,))
            elif s >= 30:
                g = max(1, 0.035*s); d.ellipse([x-R*0.55-g, y-R*0.5-g, x-R*0.55+g, y-R*0.5+g], fill=WIT + (255,))
    a = np.array(im)[:, :, 3] > 0; ys, xs = np.nonzero(a)
    return im, (xs.mean() + 0.5, ys.mean() + 0.5), a.sum()

v3.dier_delen = delen_v5
v3.dier_beeld = dier_beeld

def maak(uit):
    """Blad met alle 24 op 454 (dier op ±1/5 van de breedte) en op 260, op diep water (W2 en W3) zoals in de app."""
    os.makedirs(uit, exist_ok=True)
    gap = 20; cel = 230; kol = 6; rijen = 4
    blad = Image.new('RGB', (gap + kol*(2*cel + gap), 90 + rijen*(cel + 50)), (14, 16, 24)); dd = ImageDraw.Draw(blad)
    dd.text((gap, 24), 'Ebb dieren v5 (Mila): één tekenregel, op diep water. Per dier links 454 (verkleind), rechts 260 ware grootte',
            font=v3.f(36), fill=(220, 230, 240))
    for i, (soort, naam) in enumerate(ALLE):
        r, k = divmod(i, kol); x = gap + k*(2*cel + gap); y = 90 + r*(cel + 50)
        for j, D in enumerate((454, 260)):
            def scherm(DD, soort=soort):
                im = leeg(DD); zee(im, DD, [(DD*0.10, W2), (DD*0.55, W3)], amp=DD*0.012, schuim=False)
                opp = (DD*0.20)**2*0.55
                v3.dier(im, soort, DD/2, DD/2, v3.schaal_voor_gewicht(soort, opp)); rand(im, DD); return im
            im = teken(scherm, D)
            im.save(f'{uit}/dier-{soort}-{D}.png')
            if D == 454: im = im.resize((cel, cel), Image.LANCZOS)
            else: im = im.crop((15, 15, 245, 245))
            blad.paste(im, (x + j*cel, y))
        dd.text((x, y + cel + 8), f'{i+1} {naam}', font=v3.f(30), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-dieren-v5.png')
    return [f'{s:12s} buiten MIP op 260: {niet_mip(Image.open(f"{uit}/dier-{s}-260.png"))}' for s, _ in ALLE]

if __name__ == '__main__':
    v3.FONT = sys.argv[2]
    print('\n'.join(maak(sys.argv[1])))
