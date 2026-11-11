# Winkelkaarten Ebb v4 (Mila, run 35, 11 nov), opdracht keuring bouw 6 "Voor Mila" punt 1:
# ingezoomd (scherm minstens 60 procent van de kaartbreedte), geen band, minder zwart, kop zonder rood (wit met één woord geel).
# Eerlijk: het scherm en de rand van de kast zijn de echte opname uit de plaatjesrun, alleen vergroot en rond uitgesneden.
#   python3 winkel_v4.py kaart <simulator-fenix847mm.png> "<kop>" "<geel woord>" "<ondertekst>" <uit.png>
#   python3 winkel_v4.py alles <map met fenix847mm-scene<k>.png> <uitmap>
# Schermcirkel in de fenix847mm-opname (713 x 968, met menubalk): midden (361, 476), straal 227 (gemeten op scène 24).
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
B = os.path.dirname(os.path.abspath(__file__))
FX = os.path.join(B, 'fonts', 'BarlowCondensed-ExtraBold.woff')
FM = os.path.join(B, 'fonts', 'BarlowCondensed-Medium.ttf')
def f(p, s): return ImageFont.truetype(p, s)
NACHT, DIEP, MIDDEN, SCHUIM, LICHT = (0, 0, 85), (0, 0, 170), (0, 85, 170), (0, 255, 255), (0, 170, 255)
WIT, GEEL = (255, 255, 255), (255, 255, 85)
CX, CY, R = 361, 476, 227          # schermcirkel in de opname
RAND = 1.16                        # hoeveel kast er rond het scherm meekomt (stukje rand met de 60-streepjes)
W = H = 800
SCHERM = 0.66                      # schermbreedte op de kaart (eis: minstens 0,60)


def uitsnede(pad, rs):
    """Rond stuk uit de opname: scherm plus een ring kast, geschaald zodat het scherm rs px straal heeft."""
    im = Image.open(pad).convert('RGB')
    rr = R * RAND
    vak = im.crop((int(CX - rr), int(CY - rr), int(CX + rr), int(CY + rr)))
    d = int(2 * rr * rs / R)
    vak = vak.resize((d, d), Image.LANCZOS)
    m = Image.new('L', (d * 4, d * 4), 0); ImageDraw.Draw(m).ellipse([0, 0, d * 4 - 1, d * 4 - 1], fill=255)
    vak.putalpha(m.resize((d, d), Image.LANCZOS))
    return vak


def golf(dr, y0, a, kleur, fase=0, lijn=None, n=2.0):
    pts = [(x, y0 + a * math.sin(x / W * 2 * math.pi * n + fase)) for x in range(0, W + 1, 4)]
    dr.polygon(pts + [(W, H), (0, H)], fill=kleur)
    if lijn: dr.line(pts, fill=lijn, width=4)


def kop(dr, y, tekst, geel, font):
    tw = dr.textlength(tekst, font=font); x = (W - tw) / 2
    i = tekst.index(geel) if geel and geel in tekst else len(tekst)
    for deel, kl in [(tekst[:i], WIT), (tekst[i:i + len(geel)] if geel else '', GEEL), (tekst[i + len(geel or ''):], WIT)]:
        if deel: dr.text((x, y), deel, font=font, fill=kl); x += dr.textlength(deel, font=font)


def kaart(sim, tekst, geel, onder, uit):
    im = Image.new('RGB', (W, H), NACHT); dr = ImageDraw.Draw(im)
    # zee achter het horloge: drie lagen zoals in de app (dieper is donkerder), schuimlijn op de bovenste
    golf(dr, H * 0.60, 10, MIDDEN, 0.6, lijn=SCHUIM)
    golf(dr, H * 0.74, 8, DIEP, 2.1)
    golf(dr, H * 0.88, 6, (0, 0, 120), 4.0)
    for bx, by, br in [(0.07, 0.70, 11), (0.11, 0.78, 6), (0.92, 0.67, 9), (0.89, 0.76, 5), (0.94, 0.86, 7), (0.06, 0.90, 7)]:
        dr.ellipse([W * bx - br, H * by - br, W * bx + br, H * by + br], outline=LICHT, width=3)
    maat = int(H * 0.105)
    while dr.textlength(tekst, font=f(FX, maat)) > W * 0.93: maat -= 2   # lange kop past altijd, kleiner in plaats van afgesneden
    kop(dr, H * 0.025 + (int(H * 0.105) - maat) * 0.6, tekst, geel, f(FX, maat))
    dr.text((W / 2, H * 0.165), onder, font=f(FM, int(H * 0.044)), fill=SCHUIM, anchor='mt')
    rs = int(W * SCHERM / 2)
    w = uitsnede(sim, rs)
    cy = int(H * 0.605)
    im.paste(w, (W // 2 - w.width // 2, cy - w.height // 2), w)
    im.save(uit, optimize=True)
    for kl in (256, 200, 160, 128):          # onze grens 150 KB per kaart (zoals v1 tot v3)
        if os.path.getsize(uit) < 150_000: break
        im.quantize(colors=kl, method=Image.Quantize.FASTOCTREE).save(uit, optimize=True)
    print(uit, os.path.getsize(uit), 'scherm', round(2 * rs / W, 2), 'van de breedte')


# Keuze vijf (met Gijs na te lopen): wat het meest verkoopt, in de volgorde van de winkel.
KAARTEN = [
    (24, '1-hold.png', 'Hold. Bring a friend.', 'friend', 'Breath-hold rounds. The sea darkens as you hold.'),
    (34, '2-new-friend.png', 'Come back. Meet a crab.', 'crab', 'New sea friends for sessions and weeks in a row.'),
    (23, '3-sea-log.png', 'Fill your sea log.', 'sea log', '24 sea friends to find, plus one bonus.'),
    (25, '4-sea-complete.png', 'Then the whole sea parties.', 'parties', 'Find all 24 and every friend comes to celebrate.'),
    (35, '5-pause.png', 'Pause. The sea waits.', 'waits', 'Resume, save or discard. Any time.'),
    (7, 'extra-calm.png', 'Calm 4-7-8, drawn as water.', '4-7-8', 'Breathe in 4, hold 7, out 8. A buzz per phase.'),
]


def alles(bron, uitmap):
    os.makedirs(uitmap, exist_ok=True)
    for k, naam, t, g, o in KAARTEN:
        kaart(os.path.join(bron, f'fenix847mm-scene{k}.png'), t, g, o, os.path.join(uitmap, naam))


if __name__ == '__main__':
    a = sys.argv
    if a[1] == 'kaart': kaart(a[2], a[3], a[4], a[5], a[6])
    elif a[1] == 'alles': alles(a[2], a[3])
