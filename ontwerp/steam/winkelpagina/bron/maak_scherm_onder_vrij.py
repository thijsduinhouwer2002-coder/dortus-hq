# Mila 15 nov: twee rijen uit één echt beeld, nu met de onderste rij vrij gekozen (x0,x1,y0,y1)
# en de bovenste rij die de rest vult rond een gekozen midden. Niets bijgetekend, alleen uitsnede en vergroting.
#   python3 maak_scherm_onder_vrij.py <opname.png> <x0,x1,y0,y1 onder> <xmidden,y0,y1 boven> <uit.png>
import sys
from PIL import Image
W,H,LIJN=1920,1080,4
def maak(opname,onder,boven,uit):
    s=Image.open(opname).convert('RGBA')
    bg=Image.new('RGBA',s.size,(0x2a,0x1c,0x36,255)); bg.alpha_composite(s); s=bg
    x0,x1,y0,y1=onder; zb=W/(x1-x0); hb=round((y1-y0)*zb)
    b=s.crop((x0,y0,x1,y1)).resize((W,hb),Image.LANCZOS)
    ha=H-hb-LIJN; xm,ty0,ty1=boven; w=round((ty1-ty0)*W/ha)
    tx0=max(0,min(s.size[0]-w,xm-w//2))
    a=s.crop((tx0,ty0,tx0+w,ty1)).resize((W,ha),Image.LANCZOS)
    im=Image.new('RGB',(W,H),(0x1a,0x12,0x22))
    im.paste(a.convert('RGB'),(0,0)); im.paste(b.convert('RGB'),(0,H-hb))
    print('boven x',tx0,tx0+w,'y',ty0,ty1,'zoom %.2f'%(W/w),'| onder',onder,'zoom %.2f'%zb)
    im.save(uit)
if __name__=='__main__':
    o=[int(v) for v in sys.argv[2].split(',')]; b=[int(v) for v in sys.argv[3].split(',')]
    maak(sys.argv[1],o,b,sys.argv[4])
