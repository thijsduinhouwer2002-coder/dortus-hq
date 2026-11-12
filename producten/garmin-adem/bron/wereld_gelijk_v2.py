# Veiligheidstoets voor de werelden in de echte sessie (run 63; vervangt wereld_gelijk.py, die de kleuren van de
# oude werelden uit werelden.xml zocht). De wereld mag langer inhouden nooit belonen: het beeld op 0:30 en op 2:30
# moet gelijk zijn, op de cijfers van de tijd na.
# Gebruik: python3 bron/wereld_gelijk_v2.py <beeld 0:30> <beeld 2:30>
# Alle pixels die meer dan 24 per kanaal verschillen moeten in één smalle band liggen (de regel met de tijd):
# hoogstens een kwart van de hoogte en 70 procent van de breedte, en in de bovenste 70 procent van het beeld.
# Rood (exit 1) als er buiten die band iets verschilt, bij ongelijke maten, of als er niets verschilt (dan staan
# er geen twee tijden in beeld en is er niets bewezen). Wat deze toets niet ziet: een verschil dat precies binnen de
# band van de cijfers valt.
import sys
from PIL import Image
a, b = sys.argv[1:3]
A, B = Image.open(a).convert('RGB'), Image.open(b).convert('RGB')
if A.size != B.size:
    print('NIET TE VERGELIJKEN: maten verschillen', A.size, B.size); sys.exit(1)
W, H = A.size
pa, pb = A.load(), B.load()
xs, ys = [], []
for y in range(H):
    for x in range(W):
        ca, cb = pa[x, y], pb[x, y]
        if max(abs(ca[0] - cb[0]), abs(ca[1] - cb[1]), abs(ca[2] - cb[2])) > 24:
            xs.append(x); ys.append(y)
n = len(xs)
if n < 20:
    print('NIETS BEWEZEN: maar %d pixels verschillen, staan er wel twee tijden in beeld?' % n); sys.exit(1)
x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
goed = (y1 - y0) <= H * 0.25 and (x1 - x0) <= W * 0.70 and y1 <= H * 0.70
print('WERELD VERGELEKEN v2: %d pixels verschillen, band x %d tot %d, y %d tot %d, beeld %d x %d, uitslag %s'
      % (n, x0, x1, y0, y1, W, H, 'GELIJK op de tijd na' if goed else 'VERSCHIL buiten de regel van de tijd'))
sys.exit(0 if goed else 1)
