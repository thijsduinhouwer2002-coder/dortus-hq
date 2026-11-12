# Vergelijkingsblad run 73: per scène oud (run 72, c6761f19) naast nieuw (proef73).
import sys, os
from PIL import Image, ImageDraw, ImageFont
S = sys.argv[1]; h = sys.argv[2]; vak = tuple(int(x) for x in sys.argv[3].split(',')); uit = sys.argv[4]; hnaam = sys.argv[5]
NAAM = {'basis': 'dolfijn', 'krab': 'zwaardvis', 'schild': 'narwal', 'komkommer': 'orka', 'kreeft': 'octopus', 'otter': 'reuzeninktvis'}
sc = open(os.path.join(S, 'sc.txt')).read().split()
C = 300; G = 14; PER = 3
def f(n):
    try: return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', n)
    except Exception: return ImageFont.load_default()
bw = 2 * C + G; rijen = (len(sc) + PER - 1) // PER
W = G + PER * (bw + 2 * G); H = 70 + rijen * (C + 60 + G) + G
blad = Image.new('RGB', (W, H), (38, 40, 48)); dr = ImageDraw.Draw(blad)
dr.text((G, 14), 'Ebb, dieren bij dag en nacht op de %s. Links oud (run 72), rechts nieuw (run 73)' % hnaam, fill=(255, 255, 255), font=f(26))
for i, s in enumerate(sc):
    d = s.split('-'); dier = NAAM[d[1]]; fase = {'in': 'inademen', 'hold': 'inhouden', 'uit': 'uitademen'}[d[2]]
    x = G + (i % PER) * (bw + 2 * G); y = 70 + (i // PER) * (C + 60 + G)
    dr.text((x, y), '%s, %s, %s' % (dier, fase, d[3]), fill=(255, 230, 120), font=f(22))
    for j, m in enumerate(['oud', 'nieuw']):
        p = os.path.join(S, m, '%s-%s.png' % (s, h)); xx = x + j * (C + G)
        if os.path.exists(p):
            blad.paste(Image.open(p).convert('RGB').crop(vak).resize((C, C), Image.LANCZOS), (xx, y + 30))
        else:
            dr.rectangle([xx, y + 30, xx + C - 1, y + 30 + C - 1], fill=(60, 60, 70)); dr.text((xx + 20, y + 160), 'geen beeld (niet in run 72)' if m == 'oud' else 'ontbreekt', fill=(200, 200, 200), font=f(16))
        dr.text((xx + 4, y + 32 + C), m, fill=(150, 220, 255), font=f(18))
blad.save(uit); print(uit, blad.size)
