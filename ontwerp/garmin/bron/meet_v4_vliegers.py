# Gebruik: cd bron; python3 meet_v4_vliegers.py
# Contrast (elke tekstregel 4,5:1 of hoger) en veilige zone (6/260 tussen tekst en held plus grapvoorwerp) voor de familie vliegers.
# Werkwijze zoals meet_contrast_v32 en toets_veilige_zone_v32; held en grap vallen weg met HELD_AAN = False.
import sys; sys.path.insert(0, '.')
import werelden_v4_vliegers as v, werelden_v21 as w
from PIL import ImageChops
MARGE = 6
vakken = []
def nep(self, x, y, s, maat, c, dik=True):
    f = w.f(w.FS if dik else w.FM, round(maat * self.s)); l, t, r, b = f.getbbox(s)
    ww = self.dr.textlength(s, font=f); X = x * self.s - ww / 2; Y = y * self.s
    K = self.k; vakken.append((s, c, (int(X/K), int((Y + t)/K), int((X + ww)/K), int((Y + b)/K))))
w.Doek.tekst = nep
def L(c):
    r = [(q/255)/12.92 if q/255 <= 0.03928 else ((q/255+0.055)/1.055)**2.4 for q in c[:3]]
    return 0.2126*r[0]+0.7152*r[1]+0.0722*r[2]
slecht = fout = 0; krap = []; laagste = 99
for dier in v.DIEREN:
  for nacht in (False, True):
    dd = v.NACHT if nacht else v.DAG
    for D_, am in ((454, True), (260, False)):
        k = D_ / 260
        for naam in v.NAMEN:
            vakken.clear(); v.HELD_AAN = True; a = v.scherm(naam, dier)(D_, am, dd, nacht).convert('RGB'); vk = list(vakken)
            vakken.clear(); v.HELD_AAN = False; b = v.scherm(naam, dier)(D_, am, dd, nacht).convert('RGB'); v.HELD_AAN = True
            px = a.load(); tag0 = f'{dier} {naam} {"nacht" if nacht else "dag"} {D_}'
            for s, c, (x0, y0, x1, y1) in vk:
                if x1 <= x0 or y1 <= y0: continue
                hi = max(L(px[x, y]) for x in range(max(0, x0), min(D_, x1)) for y in range(max(0, y0), min(D_, y1)))
                kk = (L(c) + .05) / (hi + .05); laagste = min(laagste, kk)
                if kk < 4.5: slecht += 1; print(f'CONTRAST {tag0}: "{s}" {kk:.1f}')
            mk = ImageChops.difference(a, b).convert('L').point(lambda q: 255 if q > 24 else 0); m = mk.load()
            pts = [(x, y) for y in range(D_) for x in range(D_) if m[x, y]]
            for s, c, (x0, y0, x1, y1) in vk:
                if not pts: break
                dmin = min(max(x0 - x, 0, x - x1) ** 2 + max(y0 - y, 0, y - y1) ** 2 for x, y in pts) ** .5 / k
                if dmin < MARGE: fout += 1; print(f'TE DICHT {tag0}: "{s}" {dmin:.1f}')
                elif dmin < MARGE + 4: krap.append(f'{tag0}: "{s}" {dmin:.1f}')
print('krap (binnen marge + 4):', len(krap)); [print('  ', t) for t in krap[:12]]
print(f'regels onder 4,5: {slecht} (laagste {laagste:.1f})')
print(f'regels te dicht bij held of grap (marge {MARGE}/260): {fout}')
