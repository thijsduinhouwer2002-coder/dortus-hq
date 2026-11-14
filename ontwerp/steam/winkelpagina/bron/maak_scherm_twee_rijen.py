# Mila 14 nov: scherm 1 in twee rijen uit één echt beeld van de strook (moet Daan 18:33). Niets bijgetekend, alleen uitsnede en vergroting.
#   python3 maak_scherm_twee_rijen.py <opname.png> <x0,x1 boven> <x0,x1 onder> <uit.png>
import sys
from PIL import Image
W,H=1920,1080
def rij(strook,x0,x1,y0=0,y1=160):
    c=strook.crop((x0,y0,x1,y1)); z=W/(x1-x0)
    return c.resize((W,round((y1-y0)*z)),Image.LANCZOS)
def maak(opname,boven,onder,uit,band=(0x1a,0x12,0x22)):
    s=Image.open(opname).convert('RGBA')
    bg=Image.new('RGBA',s.size,(0x2a,0x1c,0x36,255)); bg.alpha_composite(s); s=bg  # lucht van de strook is doorzichtig
    a=rij(s,*boven); b=rij(s,*onder)
    rest=H-a.size[1]-b.size[1]
    im=Image.new('RGB',(W,H),band)
    im.paste(a.convert('RGB'),(0,0)); im.paste(b.convert('RGB'),(0,H-b.size[1]))
    print('hoogtes',a.size[1],b.size[1],'band',rest)
    im.save(uit)
if __name__=='__main__':
    o=sys.argv[1]; bv=[int(v) for v in sys.argv[2].split(',')]; on=[int(v) for v in sys.argv[3].split(',')]
    maak(o,bv,on,sys.argv[4])
