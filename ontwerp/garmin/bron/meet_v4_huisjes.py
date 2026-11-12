# Gebruik: cd bron; python3 meet_v4_huisjes.py [dier ...]
# Contrast (zoals meet_contrast_v32: lichtste achtergrond in het vak van elke regel, eis 4,5) en veilige zone
# (zoals toets_veilige_zone_v32: afstand van elk tekstvak tot elke pixel van dier en grapvoorwerp, eis 6/260)
# voor de familie huisjes. Held-groep uitzetten gaat via ZONDER_HELD in werelden_v4_huisjes.
import sys; sys.path.insert(0, '.')
import werelden_v4_huisjes as v, werelden_v21 as w
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
slecht = 0; fout = 0; krap = []; n = 0
for dier in (sys.argv[1:] or v.DIEREN):
  for nacht in (False, True):
    dd = v.NACHT if nacht else v.DAG
    for D_, am in ((454, True), (260, False)):
        k = D_ / 260
        for naam in v.NAMEN:
            n += 1
            vakken.clear(); v.ZONDER_HELD[0] = False
            a = v.scherm(naam, dier)(D_, am, dd, nacht).convert('RGB'); vk = list(vakken)
            vakken.clear(); v.ZONDER_HELD[0] = True
            b = v.scherm(naam, dier)(D_, am, dd, nacht).convert('RGB'); v.ZONDER_HELD[0] = False
            tag0 = f'{dier} {naam} {"nacht" if nacht else "dag"} {D_}'
            px = a.load()
            for s, c, (x0, y0, x1, y1) in vk:
                if x1 <= x0 or y1 <= y0: continue
                hi = max(L(px[x, y]) for x in range(max(0, x0), min(D_, x1)) for y in range(max(0, y0), min(D_, y1)))
                kk = (L(c) + .05) / (hi + .05)
                if kk < 4.5: slecht += 1; print(f'CONTRAST {tag0}: "{s}" {kk:.1f}')
            mk = ImageChops.difference(a, b).convert('L').point(lambda q: 255 if q > 24 else 0)
            mp = mk.load(); pts = [(x, y) for y in range(D_) for x in range(D_) if mp[x, y]]
            for s, c, (x0, y0, x1, y1) in vk:
                if not pts: break
                dmin = min(max(x0 - x, 0, x - x1) ** 2 + max(y0 - y, 0, y - y1) ** 2 for x, y in pts) ** .5 / k
                tag = f'{tag0}: "{s}" {dmin:.1f}'
                if dmin < MARGE: fout += 1; print('TE DICHT', tag)
                elif dmin < MARGE + 4: krap.append(tag)
print('schermen:', n)
print('contrast, regels onder 4,5:', slecht)
print('krap (binnen marge + 4):', len(krap)); [print('  ', t) for t in krap[:20]]
print(f'veilige zone, regels te dicht (marge {MARGE}/260):', fout)
