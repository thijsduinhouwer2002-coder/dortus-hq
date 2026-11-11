# Meet per dier en per maat of het zwarte oog (v8.3) op een lichte plek valt: welk deel van de ring van 1 px rond het oog
# haalt 3:1 tegen zwart (eis: minstens 75%).
# Maten zoals in de app (d * factor): sea log 0,078, inhouden 0,095, eindscherm 0,15; op 260 en 454.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from PIL import Image, ImageDraw
J = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'ebb-dieren-v83-data.json')
D = h.laad(J)
def lum(c):
    f = lambda v: v/255/12.92 if v/255 <= 0.03928 else ((v/255 + 0.055)/1.055)**2.4
    r, g, b = [f(x) for x in c]; return 0.2126*r + 0.7152*g + 0.0722*b
MATEN = sorted({int(d*f) for d in (260, 454) for f in (0.078, 0.095, 0.15)})
slecht = []
for d in D:
    rij = []
    for maat in MATEN:
        im = Image.new('RGB', (300, 300)); dr = ImageDraw.Draw(im)
        o = h.delen(dr, d, 150, 150, maat, None, 0); b = d['bytes']
        for k in range(b[o]):
            x = 150 + h.idiv(b[o+1+2*k]*maat, 90); y = 150 + h.idiv(b[o+2+2*k]*maat, 90)
            e = max(2, (8*maat + 50)//100); r = max(3, maat//20)
            # ring van 1 px rond het oog (vierkant tot maat 60, daarboven rond): welk deel is licht genoeg (3:1 tegen zwart)?
            if maat < 60: oog = {(x - e//2 + dx, y - e//2 + dy) for dx in range(e) for dy in range(e)}
            else: oog = {(x+dx, y+dy) for dx in range(-r, r+1) for dy in range(-r, r+1) if dx*dx + dy*dy <= r*r}
            ring = {(px+ax, py+ay) for px, py in oog for ax in (-1, 0, 1) for ay in (-1, 0, 1)} - oog
            goed = sum((lum(im.getpixel(q)) + 0.05)/0.05 >= 3 for q in ring) / len(ring)
            rij.append(f'{maat}:{100*goed:.0f}%')
            if goed < 0.75: slecht.append((d['naam'], maat, f'{100*goed:.0f}%'))
    print(f"{d['naam']:13s}", ' '.join(rij))
print('ring onder 75% licht:', slecht if slecht else 'geen')
