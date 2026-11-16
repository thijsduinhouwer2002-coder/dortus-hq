# Maakt het blad met maten voor Tij (plaat 1) voor Gijs: tabel in px per scherm + een plaatje met hulplijnen.
# Alle maten komen uit stijl_proef_v3.py en v5 (golfje, BB-getal met ruimte-eis), zodat proef en blad nooit uit elkaar lopen.  python3 maten_blad_tij.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stijl_proef_v3 as P
import stijl_proef_v5 as V  # v5: plafond 0,715 en BB-getal 0,632 (ruimte-eis Daan 23:30)
from PIL import ImageDraw
HIER = os.path.dirname(os.path.abspath(__file__))
MATEN = [208, 218, 240, 260, 280, 390, 416, 454]
rij = lambda naam, fn: '| ' + naam + ' | ' + ' | '.join(str(fn(S)) for S in MATEN) + ' |'
r = lambda v: int(round(v))
regels = ['| wat | ' + ' | '.join(f'{S}' for S in MATEN) + ' |', '|---|' + '---|' * len(MATEN),
  rij('datum: midden y, letter px (gewicht 700)', lambda S: f'{r(S*.13)}, {r(S*.065)}'),
  rij('tijd: midden y, letter px (gewicht 900)', lambda S: f'{r(S*.30)}, {r(S*.30)}'),
  rij('velden: x links/midden/rechts', lambda S: f'{r(S/2-S*.22)}/{r(S/2)}/{r(S/2+S*.22)}'),
  rij('veld-icoon: midden y, hoogte px', lambda S: f'{r(S*V.IKOON_Y)}, {r(max(12,S*.04))}'),
  rij('veld-getal: midden y, letter px (800)', lambda S: f'{r(S*V.VELD_Y)}, {r(S*.065)}'),
  rij('water bij 100 (plafond) y', lambda S: r(S*P.TOP)),
  rij('water bij 0 (kleinste zee) y', lambda S: r(S*P.BODEM)),
  rij('nu (bootje) x, begin', lambda S: r(S*P.NU_X)),
  rij('lijn begint x', lambda S: r(S*P.LINKS_X)),
  rij('banden onder de lijn, px', lambda S: '/'.join(str(r(S*o)) for o in P.BANDEN)),
  rij('waterlijn dikte px', lambda S: max(2, S//110)),
  rij('bootje halve breedte, mast px', lambda S: f'{r(S*.05)}, {r(S*.075)}'),
  rij('BB-getal: midden y, letter px, rand px (getal + golfje samen gecentreerd op x = S/2)', lambda S: f'{r(S*V.BB_Y)}, {r(S*.11)}, {max(2,S//120)}'),
  rij('ruimte-eis: px tussen onderkant getal (met rand) en golftop/zeil eronder; bootje nooit links van rechterkant getal + halve romp + deze ruimte', lambda S: f'{V.ruimte(S):.1f}'),
  rij('golfje (2 golven, kleur waterlijn): breedte, lijndikte, afstand tot getal px', lambda S: f'{r(max(12,S*.05))}, {max(2,r(max(12,S*.05)*.17))}, {r(max(12,S*.05)*.25)}'),
  rij('veilige straal bootje px', lambda S: r(S*P.VEILIG)),
]
kleur = ['| thema | zee boven | zee onder | uren | minuten, zeil, hart | tekst, iconen | dubbele punt | boot |', '|---|---|---|---|---|---|---|---|']
hx = lambda c: '#%02X%02X%02X' % c
for n, t in P.THEMAS.items(): kleur.append(f'| {n} | ' + ' | '.join(hx(c) for c in t) + ' |')
open(os.path.join(HIER, 'maten-tij-tabel.md'), 'w').write('\n'.join(regels) + '\n\n' + '\n'.join(kleur) + '\n')
# plaatje met hulplijnen op 454
S = 454; im = V.plaat(S, 'Dusk', P.NACHT, 0).resize((S * 2, S * 2)); d = ImageDraw.Draw(im); k = 2
for y, lab in ((.13, 'datum'), (.30, 'tijd'), (V.IKOON_Y, 'iconen'), (V.VELD_Y, 'veldgetal'), (V.BB_Y, 'BB-getal'), (P.TOP, 'water 100'), (P.BODEM, 'water 0')):
    d.line([(0, y*S*k), (S*k, y*S*k)], fill=(0, 255, 160), width=1); d.text((8, y*S*k - 18), f'{lab} y={round(y*S)}', font=P.f(22, 600), fill=(0, 255, 160))
d.line([(P.NU_X*S*k, 0), (P.NU_X*S*k, S*k)], fill=(255, 0, 200), width=1); d.text((P.NU_X*S*k + 6, 40), f'nu x={round(P.NU_X*S)}', font=P.f(22, 600), fill=(255, 0, 200))
d.ellipse([S*k/2 - P.VEILIG*S*k, S*k/2 - P.VEILIG*S*k, S*k/2 + P.VEILIG*S*k, S*k/2 + P.VEILIG*S*k], outline=(255, 255, 0))
im.save(os.path.join(HIER, 'maten-tij-454.png')); print('klaar')
