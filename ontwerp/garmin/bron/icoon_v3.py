# Icoon Ebb v3 (Mila, run 36, 11 nov avond), opdracht keuring bouw 7 "Voor Mila" punt 2:
# blauwe walvis (het app-dier nr. 24, dieren v8.3) in plaats van de rode, passend bij de app en de winkelkaarten.
# Winkelicoon: patrijspoort (zoals de kaarten en de poster), walvis half boven de kamlijn met fontein.
# Startpictogram (40 tot 80 px): zonder ring, alleen zee en walvis, zodat hij klein nog leest.
#   python3 icoon_v3.py winkel <uit.png> [maat=500]
#   python3 icoon_v3.py start <uit.png> <maat>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from PIL import Image, ImageDraw, ImageFilter, ImageChops
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')
D = h.laad(os.path.join(G, 'ebb-dieren-v83-data.json'))
NACHT, DIEP, MIDDEN, SCHUIM, LICHT = (0, 0, 85), (0, 0, 170), (0, 85, 170), (0, 255, 255), (0, 170, 255)
STAAL, STAAL2, KLINK = (44, 56, 74), (24, 30, 42), (168, 186, 206)
WALVIS = 23
X = 4   # overmaat: teken op 4x, verklein daarna glad


def binnen(n, cx, cy, r, ring):
    """Zee in een cirkel met straal r: nacht boven, kamlijn in schuim, banden dieper donkerder, walvis met fontein."""
    im = Image.new('RGB', (n, n), NACHT); dr = ImageDraw.Draw(im)
    top = cy - 0.02 * r
    a = r * 0.05
    def band(y0, kl, fase, lijn=False):
        pts = [(x, y0 + a * math.sin((x - cx) / r * math.pi * 1.5 + fase)) for x in range(0, n + 1, 2)]
        dr.polygon(pts + [(n, n), (0, n)], fill=kl)
        if lijn: dr.line(pts, fill=SCHUIM, width=max(2, round(r * 0.06)))
    band(top, MIDDEN, 0.3, True)
    band(top + r * 0.42, DIEP, 1.4)
    band(top + r * 0.78, (0, 0, 120), 2.6)
    # walvis: breed, half boven het water, kijkt naar links (zoals in de app)
    m = r * (0.70 if ring else 0.78)
    wx, wy = cx + r * 0.05, cy + r * (0.12 if ring else 0.16)
    sh = 0
    if not ring or r > 0.45 * n:   # startpictogram (zonder staalring)
        # run 37: startpictogram met het kader van de walvis in het midden (de staart viel er op 54 en 56 px af)
        t_ = Image.new('RGB', (n, n)); h.teken(ImageDraw.Draw(t_), D[WALVIS], round(wx), round(wy), round(m))
        bx = t_.getbbox(); sh = cx - (bx[0] + bx[2]) / 2; wx += sh
    # walvis op een eigen laag, met een dikke witte stickerrand eromheen: blauw op blauw moet ook op 64 px opvallen
    laag = Image.new('RGB', (n, n), (255, 0, 255)); h.teken(ImageDraw.Draw(laag), D[WALVIS], round(wx), round(wy), round(m))
    mk = ImageChops.difference(laag, Image.new('RGB', (n, n), (255, 0, 255))).convert('L').point(lambda v: 255 if v > 8 else 0)
    dik = max(3, round(r * (0.035 if ring else 0.05))) | 1
    rand = mk.filter(ImageFilter.MaxFilter(dik * 2 + 1)) if dik < 24 else mk.resize((n // 4, n // 4)).filter(ImageFilter.MaxFilter((dik // 4) * 2 + 1)).resize((n, n))
    im.paste((255, 255, 255), (0, 0), rand)
    im.paste(laag, (0, 0), mk)
    # fontein: drie belletjes boven de kop (alleen als het icoon groot genoeg is)
    if ring:
        for bx, by, br in [(-0.62, -0.46, 0.08), (-0.47, -0.60, 0.06), (-0.70, -0.66, 0.05)]:
            dr.ellipse([cx + sh + bx * r - br * r, cy + by * r - br * r, cx + sh + bx * r + br * r, cy + by * r + br * r],
                       outline=SCHUIM, width=max(2, round(r * 0.035)))
    m_ = Image.new('L', (n, n), 0); ImageDraw.Draw(m_).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    return im, m_


def winkel(uit, maat=500):
    n = maat * X; c = n / 2
    im = Image.new('RGBA', (n, n), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    R = n * 0.49; r = n * 0.385
    dr.ellipse([c - R, c - R, c + R, c + R], fill=STAAL)
    dr.ellipse([c - r - n * 0.018, c - r - n * 0.018, c + r + n * 0.018, c + r + n * 0.018], fill=STAAL2)
    for i in range(8):
        hk = math.radians(22.5 + 45 * i); rk = (R + r) / 2; kr = n * 0.028
        x, y = c + rk * math.cos(hk), c + rk * math.sin(hk)
        dr.ellipse([x - kr, y - kr, x + kr, y + kr], fill=KLINK)
        dr.ellipse([x - kr * 0.45 - kr * 0.25, y - kr * 0.45 - kr * 0.25, x + kr * 0.45 - kr * 0.25, y + kr * 0.45 - kr * 0.25], fill=(230, 240, 250))
    zee, m = binnen(n, c, c, r, True)
    im.paste(zee, (0, 0), m)
    im.resize((maat, maat), Image.LANCZOS).save(uit, optimize=True)
    print(uit, maat)


def start(uit, maat):
    n = maat * X; c = n / 2
    im = Image.new('RGBA', (n, n), (0, 0, 0, 0))
    zee, m = binnen(n, c, c, n * 0.5, maat >= 60)
    im.paste(zee, (0, 0), m)
    im.resize((maat, maat), Image.LANCZOS).save(uit, optimize=True)
    print(uit, maat)


if __name__ == '__main__':
    a = sys.argv
    if a[1] == 'winkel': winkel(a[2], int(a[3]) if len(a) > 3 else 500)
    else: start(a[2], int(a[3]))
