# Omtrektoets dieren v8: alle 25 als silhouet (niet gevonden) in het sea-log-vak van 40 x 32 op 260, zonder naam,
# in een geschudde volgorde (vaste seed), zodat je eerlijk kunt toetsen of elk dier zonder naam te benoemen is.
# Gebruik: python3 omtrek_toets_v8.py <uitmap>   -> omtrek-260.png (ware grootte), omtrek-4x.png, omtrek-sleutel.txt
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_dieren_v8 as dv8
from PIL import Image
VW, VH = 40, 32; CEL = 52; KOL = 5
uit = sys.argv[1] if __name__ == '__main__' else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dieren8'); os.makedirs(uit, exist_ok=True)
volg = list(dv8.ALLE); random.Random(8).shuffle(volg)
rijen = (len(volg) + KOL - 1)//KOL
im = Image.new('RGB', (KOL*CEL, rijen*CEL), (0,0,0))
for i, (soort, naam) in enumerate(volg):
    r, k = divmod(i, KOL)
    s = dv8.maat_voor_vak(soort, VW, VH)
    b, (zx, zy), _ = dv8.dier_beeld(soort, s, 'silhouet')
    im.paste(b, (round(k*CEL + CEL/2 - zx), round(r*CEL + CEL/2 - zy)), b)
im.save(f'{uit}/omtrek-260.png'); im.resize((im.width*4, im.height*4), Image.NEAREST).save(f'{uit}/omtrek-4x.png')
open(f'{uit}/omtrek-sleutel.txt', 'w').write('\n'.join(f'{i+1:2d} {n}' for i, (_, n) in enumerate(volg)) + '\n')
