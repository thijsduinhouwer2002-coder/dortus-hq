# Mila: proefblad, alleen uit de kit en wijzerplaat.json samengesteld.
import os, json, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maak_kit as M
J = json.load(open(os.path.join(M.UIT, 'wijzerplaat.json')))
def rij(maat, standen, naam):
    w, h = M.MATEN[maat]; L = J[maat]; ims = []
    for s, u, mi in standen:
        im, lagen = M.proef(maat, L, s, uur=u, minu=mi)
        ims.append(im)
    if not M.mip(maat):
        ims.append(M.proef(maat, L, 7612, uur='14', minu='37', aod=True)[0])
    B = Image.new('RGB', (len(ims) * (w + 10), h), (60, 60, 60))
    for i, im in enumerate(ims): B.paste(im, (i * (w + 10), 0))
    B.save(os.path.join(M.HIER, naam)); return B
ST = [(3420, '10', '08'), (7612, '14', '37'), (10000, '18', '05'), (14800, '21', '52')]
rij('454', ST, 'proef-454.png'); rij('260-mip', ST, 'proef-260-mip.png'); rij('320', ST, 'proef-320.png'); rij('208-mip', ST, 'proef-208-mip.png')
