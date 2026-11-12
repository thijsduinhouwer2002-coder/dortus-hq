# Gebruik: cd bron; python3 meet_contrast_v32.py
# Meet het contrast van elke tekstregel: tekent elk scherm zonder tekst, en neemt de lichtste achtergrond in het vak van de regel.
import sys; sys.path.insert(0, '.')
import werelden_v32 as v, werelden_v21 as w
from PIL import ImageFont
vakken = []
orig = w.Doek.tekst
def nep(self, x, y, s, maat, c, dik=True):
    f = w.f(w.FS if dik else w.FM, round(maat * self.s)); l, t, r, b = f.getbbox(s)
    ww = self.dr.textlength(s, font=f); X = x * self.s - ww / 2; Y = y * self.s
    K = self.k; vakken.append((s, c, (int(X/K), int((Y + t)/K), int((X + ww)/K), int((Y + b)/K))))
w.Doek.tekst = nep
def L(c):
    r = [(v_/255)/12.92 if v_/255 <= 0.03928 else ((v_/255+0.055)/1.055)**2.4 for v_ in c[:3]]
    return 0.2126*r[0]+0.7152*r[1]+0.0722*r[2]
slecht = 0
for wereld in ['krab', 'schild', 'clown']:
  for nacht in (False, True):
    dd = v.NACHT if nacht else v.DAG
    for D_, am in ((454, True), (260, False)):
        for naam in v.NAMEN:
            vakken.clear(); im = v.scherm(naam, wereld)(D_, am, dd, nacht).convert('RGB'); px = im.load()
            for s, c, (a, b, cc, e) in vakken:
                if cc <= a or e <= b: continue
                hi = max(L(px[x, y]) for x in range(max(0,a), min(D_,cc)) for y in range(max(0,b), min(D_,e)))
                k = (L(c) + .05) / (hi + .05)
                if k < 4.5: slecht += 1; print(f'{wereld} {naam} {"nacht" if nacht else "dag"} {D_}: "{s}" {k:.1f}')
print('regels onder 4,5:', slecht)
