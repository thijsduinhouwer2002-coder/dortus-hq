# Daan 15 nov: scherm 4 zonder grasnaad. Boven de hele hoogte (gras als bovenrand), onder alleen aarde en kaartje, band in de kleur van de vloer ertussen (leest als dikkere vloer). Niets bijgetekend.
#   python3 maak_scherm4_zonder_naad.py <opname.png> <uit.png> 0 36
import sys
from PIL import Image
W,H=1920,1080
s=Image.open(sys.argv[1]).convert('RGBA')
bg=Image.new('RGBA',s.size,(0x2c,0x34,0x40,255)); bg.alpha_composite(s); s=bg
def rij(x0,x1,y0,y1):
    c=s.crop((x0,y0,x1,y1)); z=W/(x1-x0); return c.resize((W,round((y1-y0)*z)),Image.LANCZOS).convert('RGB')
ty0=int(sys.argv[3]); by0=int(sys.argv[4])
a=rij(818,1415,ty0,160); b=rij(1456,1920,by0,160)
im=Image.new('RGB',(W,H),(80,43,36))
im.paste(a,(0,0)); im.paste(b,(0,H-b.size[1]))
print(a.size,b.size,'gap',H-a.size[1]-b.size[1])
im.save(sys.argv[2])
