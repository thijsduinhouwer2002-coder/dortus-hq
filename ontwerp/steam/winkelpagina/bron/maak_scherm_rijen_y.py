# Mila 15 nov: als maak_scherm_twee_rijen.py, maar de bovenste rij mag ook in de hoogte gesneden worden
# (minder gras, groter spel), en de onderste rij vult precies de rest. Niets bijgetekend, alleen uitsnede en vergroting.
#   python3 maak_scherm_rijen_y.py <opname.png> <x0,x1,y0,y1 boven> <x1 onder (rechterrand)> <uit.png> [y0 onder]
# De breedte van de onderste rij volgt uit de hoogte die overblijft, gerekend vanaf de rechterrand naar links.
import sys
from PIL import Image
W,H=1920,1080
def rij(s,x0,x1,y0,y1,hoog=None):
    c=s.crop((x0,y0,x1,y1)); z=W/(x1-x0)
    return c.resize((W,hoog or round((y1-y0)*z)),Image.LANCZOS)
def maak(opname,boven,onder_x1,uit,lijn=4,onder_y0=0):
    s=Image.open(opname).convert('RGBA')
    bg=Image.new('RGBA',s.size,(0x2a,0x1c,0x36,255)); bg.alpha_composite(s); s=bg
    a=rij(s,*boven)
    rest=H-a.size[1]-lijn
    w=round((160-onder_y0)*W/rest); x1=onder_x1; x0=x1-w
    b=rij(s,x0,x1,onder_y0,160,hoog=rest)
    im=Image.new('RGB',(W,H),(0x1a,0x12,0x22))
    im.paste(a.convert('RGB'),(0,0)); im.paste(b.convert('RGB'),(0,H-rest))
    print('boven',boven,'hoogte',a.size[1],'onder x',x0,x1,'hoogte',rest)
    im.save(uit)
if __name__=='__main__':
    bv=[int(v) for v in sys.argv[2].split(',')]
    maak(sys.argv[1],bv,int(sys.argv[3]),sys.argv[4],onder_y0=int(sys.argv[5]) if len(sys.argv)>5 else 0)
