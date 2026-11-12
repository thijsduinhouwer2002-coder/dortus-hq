# Veiligheidstoets (codekeuring bouw 9 punt 8): de wereld van het dier mag langer inhouden nooit belonen.
# Gebruik: python3 bron/wereld_gelijk.py <beeld 0:30> <beeld 2:30> resources/werelden/werelden.xml wereld3
# Vergelijkt twee schermafbeeldingen van hetzelfde horloge. Elke pixel die in het ene beeld een kleur van de wereld
# heeft, moet in het andere beeld precies dezelfde kleur hebben. Wat mag verschillen: de zee (wordt donkerder), de
# cijfers, en de belletjes (kleur BEL, vanaf 2:30 weg): een pixel waar in het andere beeld een belletje staat telt niet.
# Wit, zwart en de kleuren van zee en tekst tellen niet als wereldkleur (die komen ook buiten de wereld voor).
# Rood (exit 1) bij een verschil, bij ongelijke maten, of als er te weinig wereld in beeld staat (dan is er niets bewezen).
import json, re, sys
from PIL import Image
a, b, xml, wid = sys.argv[1:5]
m = re.search(r'<jsonData id="%s">(.*?)</jsonData>' % wid, open(xml).read(), re.S)
w = json.loads(m.group(1))
BEL = (0x55, 0xAA, 0xFF)
NIET = {0xFFFFFF, 0x000000, 0x00AAFF, 0x0055AA, 0x0000AA, 0x000055, 0x55FFFF, 0x55AAAA, 0x55AAFF, 0xAAFFFF, 0xFFFF55}
kl = set(v[0] for v in w['v'] + w['f'] + w.get('p', [])) | set(v[1] for v in w['d'])
kl = set(((k >> 16) & 255, (k >> 8) & 255, k & 255) for k in kl if k not in NIET)
# AMOLED-horloges tekenen in 16 bits kleur (AAAA55 wordt ACAA52), dus een kleur telt als hij per kanaal hoogstens
# 8 afwijkt (run 43125340595: met precies gelijke kleuren bleven er op fr165, fr965 en venu3 te weinig pixels over).
def bij(c, lijst):
    for k in lijst:
        if abs(c[0] - k[0]) <= 8 and abs(c[1] - k[1]) <= 8 and abs(c[2] - k[2]) <= 8:
            return True
    return False
_m = {}
def isw(c):
    if c not in _m:
        _m[c] = bij(c, kl)
    return _m[c]
A, B = Image.open(a).convert('RGB'), Image.open(b).convert('RGB')
if A.size != B.size:
    print('NIET TE VERGELIJKEN: maten verschillen', A.size, B.size); sys.exit(1)
pa, pb = A.load(), B.load()
wereld = fout = bel = 0
eerste = []
for y in range(A.size[1]):
    for x in range(A.size[0]):
        ca, cb = pa[x, y], pb[x, y]
        if isw(ca) or isw(cb):
            wereld += 1
            if ca != cb:
                if bij(ca, [BEL]) or bij(cb, [BEL]):
                    bel += 1
                else:
                    fout += 1
                    if len(eerste) < 10:
                        eerste.append((x, y, '%02X%02X%02X' % ca, '%02X%02X%02X' % cb))
print('WERELD GELIJK %s: wereldpixels %d, verschil %d, onder een belletje %d, kleuren %d, maat %s' % (wid, wereld, fout, bel, len(kl), A.size))
if eerste:
    print('eerste verschillen (x, y, 0:30, 2:30):', eerste)
if wereld < A.size[0] * A.size[1] // 100:
    print('TE WEINIG WERELD in beeld, niets bewezen'); sys.exit(1)
sys.exit(1 if fout else 0)
