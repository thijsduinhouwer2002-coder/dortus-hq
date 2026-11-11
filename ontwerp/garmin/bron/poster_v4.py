# Winkelposter Ebb v4 (Mila, run 36, 11 nov avond), opdracht keuring bouw 7 "Voor Mila" punt 1:
# poster in v4-stijl, één stijl met de kaarten (nachtblauw, zee met schuimlijn, kop wit met één woord geel,
# horloge als patrijspoort zonder band), groot scherm, leesbaar op 150 px, "no extra account".
# Eerlijk: het scherm met de kastring is de echte opname (scène 24, inhouden 1:45 met krab), alleen vergroot.
# De 24 vrienden zijn de app-dieren (dieren v8.3, zoals in de sea log en sea complete), in de volgorde waarin je ze vindt.
#   python3 poster_v4.py <fenix847mm-scene24.png> <uit.png>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
import winkel_v4 as k
from PIL import Image, ImageDraw
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')
D = h.laad(os.path.join(G, 'ebb-dieren-v83-data.json'))
NACHT, DIEP, MIDDEN, SCHUIM, LICHT, WIT, GEEL = k.NACHT, k.DIEP, k.MIDDEN, k.SCHUIM, k.LICHT, k.WIT, k.GEEL
W = 1000
CX, CY, RS = 500, 596, 250          # patrijspoort: schermstraal 262, dus scherm 50 procent van de breedte, met ring 58 procent

def golf(dr, y0, a, kleur, fase=0, lijn=None, n=2.0):
    pts = [(x, y0 + a * math.sin(x / W * 2 * math.pi * n + fase)) for x in range(0, W + 1, 4)]
    dr.polygon(pts + [(W, W), (0, W)], fill=kleur)
    if lijn: dr.line(pts, fill=lijn, width=5)

def kop(dr, y, tekst, geel, font):
    tw = dr.textlength(tekst, font=font); x = (W - tw) / 2
    i = tekst.index(geel) if geel in tekst else len(tekst)
    for deel, kl in [(tekst[:i], WIT), (tekst[i:i + len(geel)], GEEL), (tekst[i + len(geel):], WIT)]:
        if deel: dr.text((x, y), deel, font=font, fill=kl); x += dr.textlength(deel, font=font)

# Boog van de optocht: links omlaag om de patrijspoort, langs de bodem, rechts omhoog naar de walvis.
PAD = [(128, 330), (128, 330), (118, 560), (180, 775), (330, 893), (500, 916), (670, 893), (822, 775), (884, 600), (884, 468), (884, 468)]
def boog(t):
    n = len(PAD) - 3; u = min(t * n, n - 1e-9); i = int(u); u -= i
    p0, p1, p2, p3 = PAD[i:i + 4]
    return tuple(0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * u + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * u * u
                        + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * u ** 3) for j in (0, 1))

def maat(i, g): return round((31 + 6 * i / 22) * g)

def halve(i, m):
    im = Image.new('RGB', (300, 300)); h.teken(ImageDraw.Draw(im), D[i], 150, 150, m)
    x0, y0, x1, y1 = im.getbbox(); return (x1 - x0) / 2, (y1 - y0) / 2

def optocht(dr, n=23):
    """Dier 0 tot n-1 op de boog, op echte maat met 5 px ruimte, zo groot als past."""
    N = 2000; pts = [boog(i / N) for i in range(N + 1)]
    L = [0]
    for i in range(1, N + 1): L.append(L[-1] + math.dist(pts[i], pts[i - 1]))
    for g in [1.0 - 0.02 * i for i in range(30)]:
        r = [halve(i, maat(i, g)) for i in range(n)]
        s = [0.0]
        for i in range(n - 1):
            j = min(range(N + 1), key=lambda q: abs(L[q] - s[-1]))
            j2 = min(j + 5, N); dx, dy = pts[j2][0] - pts[j][0], pts[j2][1] - pts[j][1]; nn = math.hypot(dx, dy) or 1
            s.append(s[-1] + abs(dx / nn) * (r[i][0] + r[i + 1][0]) + abs(dy / nn) * (r[i][1] + r[i + 1][1]) + 5)
        if s[-1] <= L[-1]: break
    s = [v * L[-1] / s[-1] for v in s]
    for i, v in enumerate(s):
        x, y = pts[min(range(N + 1), key=lambda q: abs(L[q] - v))]
        h.teken(dr, D[i], round(x), round(y), maat(i, g))
    return g

def poster(sim, uit):
    im = Image.new('RGB', (W, W), NACHT); dr = ImageDraw.Draw(im)
    # zee zoals de kaarten: schuimlijn, dan dieper donkerder
    golf(dr, 470, 11, MIDDEN, 0.6, lijn=SCHUIM)
    golf(dr, 640, 9, DIEP, 2.1)
    golf(dr, 820, 7, (0, 0, 120), 4.0)
    golf(dr, 952, 5, (0, 0, 50), 1.0)
    for bx, by, br in [(0.30, 0.52, 9), (0.27, 0.57, 5), (0.74, 0.55, 7), (0.76, 0.61, 4), (0.05, 0.86, 7), (0.95, 0.88, 6)]:
        dr.ellipse([W * bx - br, W * by - br, W * bx + br, W * by + br], outline=LICHT, width=3)
    # kop: twee korte regels, zo groot dat ze op 150 px nog leesbaar zijn (17 px hoog)
    fk = k.f(k.FX, 116)
    kop(dr, 14, 'Hold your breath.', '', fk)
    kop(dr, 128, 'Make sea friends.', 'sea friends', fk)
    dr.text((W / 2, 262), 'Come back, and a new friend swims in.', font=k.f(k.FM, 46), fill=WIT, anchor='mt')
    g = optocht(dr)
    # walvis (nr. 24) bovenaan rechts, groot, met fontein: het eind van de optocht
    h.teken(dr, D[23], 846, 388, 66)
    for bx, by, br in [(818, 334, 7), (832, 318, 5), (812, 312, 4)]:
        dr.ellipse([bx - br, by - br, bx + br, by + br], outline=SCHUIM, width=3)
    w = k.uitsnede(sim, RS)
    im.paste(w, (CX - w.width // 2, CY - w.height // 2), w)
    # onderregel op de donkerste band
    dr.text((W / 2, 990), 'One payment  ·  no subscription  ·  no extra account', font=k.f(k.FM, 40), fill=WIT, anchor='md')
    im.save(uit, optimize=True)
    if os.path.getsize(uit) > 300_000:
        im.quantize(colors=200, method=Image.Quantize.FASTOCTREE).save(uit, optimize=True)
    print(uit, os.path.getsize(uit), 'groei', round(g, 2), 'scherm', round(2 * RS / W, 2), 'met ring', round(2 * RS * k.RAND / W, 2))

if __name__ == '__main__':
    poster(sys.argv[1], sys.argv[2])
