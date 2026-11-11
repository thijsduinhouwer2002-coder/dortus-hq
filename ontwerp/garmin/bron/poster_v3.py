# Winkelposter Ebb v3 (run 34, 11 nov), opdracht keuring bouw 5: één beeld dat zegt wat Ebb is:
# ademrondes op je pols, de zee, en dieren die je krijgt door terug te komen (trouw), niet door langer inhouden.
# Ontwerp van Mila; Gijs vult het horloge met een echte opname uit de plaatjesrun (inhouden met dier, s2).
#   python3 poster_v3.py <simulator.png> <uit.png>
# <simulator.png>: schermafbeelding uit de simulator met menubalk en witte rand (zoals op de tak schermen).
# De optocht van dieren wordt getekend met horloge_sim.py, de nabootsing van DierenData.mc: precies hoe de app ze tekent.
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from PIL import Image, ImageDraw, ImageFont, ImageOps
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')
D = h.laad(os.path.join(G, 'ebb-dieren-v83-data.json'))
FX = os.path.join(B, 'fonts', 'BarlowCondensed-ExtraBold.woff')
FS = os.path.join(B, 'fonts', 'BarlowCondensed-SemiBold.ttf'); FM = os.path.join(B, 'fonts', 'BarlowCondensed-Medium.ttf')
def f(p, s): return ImageFont.truetype(p, s)
ZWART, NACHT, DIEP, MIDDEN, SCHUIM, LICHT = (0, 0, 0), (0, 0, 85), (0, 0, 170), (0, 85, 170), (0, 255, 255), (0, 170, 255)
WIT, GEEL = (255, 255, 255), (255, 255, 170)
W = 1000

def horloge(pad):
    """Knip het horloge uit de simulator-opname: menubalk en statusbalk eraf, wit om het horloge doorzichtig."""
    im = Image.open(pad).convert('RGB')
    im = im.crop((4, 30, im.width - 4, im.height - 28))
    vul = im.copy(); ImageDraw.floodfill(vul, (2, 2), (255, 0, 255), thresh=40)
    ImageDraw.floodfill(vul, (vul.width - 3, vul.height - 3), (255, 0, 255), thresh=40)
    ImageDraw.floodfill(vul, (2, vul.height - 3), (255, 0, 255), thresh=40)
    ImageDraw.floodfill(vul, (vul.width - 3, 2), (255, 0, 255), thresh=40)
    m = Image.eval(vul.convert('RGB').split()[1], lambda v: 0)  # leeg
    px = vul.load(); mp = Image.new('L', vul.size, 255); mq = mp.load()
    for y in range(vul.height):
        for x in range(vul.width):
            if px[x, y] == (255, 0, 255): mq[x, y] = 0
    im.putalpha(mp); return im.crop(mp.getbbox())

def golf(dr, y0, a, kleur, fase=0, lijn=None):
    pts = [(x, y0 + a * math.sin(x / W * 2 * math.pi * 2.5 + fase)) for x in range(0, W + 1, 4)]
    dr.polygon(pts + [(W, W), (0, W)], fill=kleur)
    if lijn: dr.line(pts, fill=lijn, width=5)

def tekst(dr, x, y, s, font, c, anker='ma'): dr.text((x, y), s, font=font, fill=c, anchor=anker)

# Optocht: 24 dieren op volgorde (Fish 1 sessie ... Whale 50 sessies), ze groeien langs een boog
# van het horloge naar rechtsboven; de walvis groot aan het eind. De zeekomkommer (bonus) zit niet in de optocht.
PAD = [(150, 372), (150, 372), (128, 560), (160, 760), (300, 878), (500, 896), (700, 878), (840, 760), (872, 590), (858, 478), (858, 478)]
def boog(t):
    """Vloeiende lijn (Catmull-Rom) door PAD: een U om het horloge, links omlaag, langs de bodem, rechts omhoog naar de walvis."""
    n = len(PAD) - 3; u = min(t * n, n - 1e-9); i = int(u); u -= i
    p0, p1, p2, p3 = PAD[i:i + 4]
    return tuple(0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * u + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * u * u
                        + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * u ** 3) for j in (0, 1))

def maat(k, g=1.0): return round((30 + 6 * k / 22) * g)

def straal(k, m):
    """Halve breedte van het echte dier (met stickerrand), gemeten op een proefbeeld."""
    im = Image.new('RGB', (300, 300)); h.teken(ImageDraw.Draw(im), D[k], 150, 150, m)
    x0, y0, x1, y1 = im.getbbox(); return (x1 - x0) / 2, (y1 - y0) / 2

def optocht(dr):
    """23 dieren op de boog, achter elkaar op hun echte maat met 6 px ruimte; zo groot als past zonder te raken."""
    N = 3000; pts = [boog(i / N) for i in range(N + 1)]
    L = [0]
    for i in range(1, N + 1): L.append(L[-1] + math.dist(pts[i], pts[i - 1]))
    for g in [1.0 - 0.02 * i for i in range(30)]:
        r = [straal(k, maat(k, g)) for k in range(23)]
        s = [0.0]
        for k in range(22):
            i = min(range(N + 1), key=lambda j: abs(L[j] - s[-1]))
            i2 = min(i + 5, N); dx, dy = pts[i2][0] - pts[i][0], pts[i2][1] - pts[i][1]; n = math.hypot(dx, dy) or 1
            # afstand langs de looprichting: hoe breed het dier in die richting is
            a = abs(dx / n) * (r[k][0] + r[k + 1][0]) + abs(dy / n) * (r[k][1] + r[k + 1][1])
            s.append(s[-1] + a + 6)
        if s[-1] <= L[-1]: break
    plek = [pts[min(range(N + 1), key=lambda j: abs(L[j] - v))] for v in s]
    for k, (x, y) in enumerate(plek):
        h.teken(dr, D[k], round(x), round(y), maat(k, g))
    print('groei', round(g, 2), 'maat', maat(0, g), 'tot', maat(22, g))
    return plek

def zee(dr, top):
    """Eén zee zoals in de app: kamlijn in schuim, dan banden die dieper donkerder worden."""
    golf(dr, top, 9, MIDDEN, 0.0, lijn=SCHUIM)
    golf(dr, top + 150, 9, (0, 0, 140), 1.1)
    golf(dr, top + 330, 8, NACHT, 2.2)
    golf(dr, top + 520, 7, (0, 0, 40), 0.4)
    golf(dr, top + 625, 6, (0, 0, 20), 1.7)

def poster(sim, uit):
    im = Image.new('RGB', (W, W), ZWART); dr = ImageDraw.Draw(im)
    zee(dr, 300)
    # kop
    tekst(dr, W / 2, 26, 'Breathe in rounds.', f(FX, 96), WIT)
    k2 = f(FX, 96); a, b = 'Make ', 'sea friends.'
    wa, wb = dr.textlength(a, font=k2), dr.textlength(b, font=k2); x0 = W / 2 - (wa + wb) / 2
    dr.text((x0, 124), a, font=k2, fill=WIT); dr.text((x0 + wa, 124), b, font=k2, fill=SCHUIM)
    tekst(dr, W / 2, 240, 'Come back, and a new friend swims in.  24 to find.', f(FM, 36), LICHT)
    # horloge links
    hw = horloge(sim); s = 520 / hw.height; hw = hw.resize((round(hw.width * s), 520), Image.LANCZOS)
    im.paste(hw, (W // 2 - hw.width // 2 - 10, 318), hw)
    # optocht en walvis: de walvis komt boven aan de kamlijn en blaast (jij houdt je adem in, hij niet)
    plek = optocht(dr)
    wx, wy = 842, 352
    h.teken(dr, D[23], wx, wy, 82)
    # labels bij drie dieren: kale feiten uit het schema in de app (TrouwDieren.mc)
    fl = f(FS, 28)
    x, y = plek[0]; tekst(dr, x + 34, y - 12, '1 session', fl, WIT, 'lm')
    x, y = plek[9]; tekst(dr, x + 36, y, '12 sessions', fl, WIT, 'lm')
    tekst(dr, wx - 100, wy + 4, '50', f(FX, 44), GEEL, 'rm'); tekst(dr, wx - 100, wy + 40, 'sessions', fl, GEEL, 'rm')
    # voet
    tekst(dr, W / 2, 950, 'One payment  ·  no subscription  ·  no account', f(FS, 34), WIT)
    im.save(uit); return im

if __name__ == '__main__':
    poster(sys.argv[1], sys.argv[2])
