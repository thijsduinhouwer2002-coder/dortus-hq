# Gebruik: cd bron; python3 meet_v4_koud.py
# Contrast (elke tekstregel 4,5:1 of hoger, lichtste achtergrond in het vak) en veilige zone (6/260 tussen tekst en
# dier, grapvoorwerp of vriend) voor de familie koud. Zelfde werkwijze als meet_contrast_v32.py en toets_veilige_zone_v32.py;
# de held-groep gaat hier uit via werelden_v4_koud.HELD_AAN.
import sys; sys.path.insert(0, '.')
import werelden_v4_koud as v, werelden_v21 as w
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
slecht = fout = 0; krap = []; laagste = 99; mip_fout = 0
OK = {0, 0x55, 0xAA, 0xFF}
for dn in sys.argv[1:] or v.DIEREN:
  for nacht in (False, True):
    dd = v.NACHT if nacht else v.DAG
    for D_, am in ((454, True), (260, False)):
        k = D_ / 260
        for naam in v.NAMEN:
            tag0 = f'{dn} {naam} {"nacht" if nacht else "dag"} {D_}'
            vakken.clear(); v.HELD_AAN[0] = True; a = v.scherm(naam, dn)(D_, am, dd, nacht).convert('RGB'); vk = list(vakken)
            vakken.clear(); v.HELD_AAN[0] = False; b = v.scherm(naam, dn)(D_, am, dd, nacht).convert('RGB'); v.HELD_AAN[0] = True
            if not am:
                verkeerd = [c for n_, c in a.getcolors(1 << 16) if not set(c) <= OK]
                if verkeerd: mip_fout += 1; print('MIP-KLEUR', tag0, verkeerd[:4])
            px = b.load()     # contrast: achtergrond zonder tekst (held-groep valt niet achter tekst, toets hieronder)
            pa = a.load()
            for s, c, (x0, y0, x1, y1) in vk:
                if x1 <= x0 or y1 <= y0: continue
                hi = max(max(L(pa[x, y]), L(px[x, y])) for x in range(max(0, x0), min(D_, x1)) for y in range(max(0, y0), min(D_, y1)))
                kk = (L(c) + .05) / (hi + .05); laagste = min(laagste, kk)
                if kk < 4.5: slecht += 1; print(f'CONTRAST {tag0}: "{s}" {kk:.1f}')
            mk = ImageChops.difference(a, b).convert('L').point(lambda q: 255 if q > 24 else 0)
            if D_ == 260 and naam in ('hold', 'menu'):
                bb = mk.getbbox(); print(f'BREEDTE {tag0}: held-groep {bb[2] - bb[0]} px')
            m_ = mk.load(); pts = [(x, y) for y in range(D_) for x in range(D_) if m_[x, y]]
            for s, c, (x0, y0, x1, y1) in vk:
                if not pts: break
                dmin = min(max(x0 - x, 0, x - x1) ** 2 + max(y0 - y, 0, y - y1) ** 2 for x, y in pts) ** .5 / k
                tag = f'{tag0}: "{s}" {dmin:.1f}'
                if dmin < MARGE: fout += 1; print('TE DICHT', tag)
                elif dmin < MARGE + 4: krap.append(tag)
print(f'laagste contrast: {laagste:.1f}   regels onder 4,5: {slecht}')
print('krap (binnen marge + 4):', len(krap)); [print('  ', t) for t in krap[:12]]
print(f'regels te dicht bij dier of grap (marge {MARGE}/260): {fout}')
print('MIP-schermen met kleuren buiten de 64:', mip_fout)
