# Richting voor de walvis van Ebb (Daan, keuring 3). Alleen MIP-kleuren, geen verloop.
# Punten in eenheden rond het midden (0,0) = midden van het kader van het hele dier,
# zodat cx,cy in de app ook echt het midden van de walvis is (eis W2).
import math
from PIL import Image, ImageDraw

KORAAL=(255,85,85); BUIK=(255,170,170); DONKER=(170,0,0); BEL=(85,170,255)
WIT=(255,255,255); NACHT=(0,0,85); WATER=(0,0,170); SCHUIM=(85,255,255); ZACHT=(85,170,170)

def bez(p0,p1,p2,n=10):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0],(1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/n for i in range(n+1)]]

def lijf():
    # bolle kop, rug zakt naar staartsteel, buik vlak en naar boven lopend
    p=[]
    p+=bez((-12,1.0),(-12.6,-5.2),(-6,-5.6))
    p+=bez((-6,-5.6),(2,-6.0),(8.5,-1.6))
    p+=bez((8.5,-1.6),(10,-0.8),(11,-0.6))
    p+=[(11,0.6)]
    p+=bez((11,0.6),(6,2.0),(-2,3.4))
    p+=bez((-2,3.4),(-9,4.2),(-12,1.0))
    return p
def buik():
    p=bez((-11.6,1.0),(-6,0.6),(5,0.9))
    p+=bez((5,0.9),(-1,3.3),(-6,3.6))
    p+=bez((-6,3.6),(-10,3.6),(-11.4,1.6))
    return p
STAART=bez((10.4,0),(12.5,-1.0),(14.8,-4.4))+bez((14.8,-4.4),(13.6,-0.4),(15.0,3.0))+[(10.4,0.6)]
VIN=bez((-5.0,2.2),(-2.4,2.6),(-1.4,5.4))+bez((-1.4,5.4),(-1.6,6.4),(-2.6,6.0))+bez((-2.6,6.0),(-4.6,4.6),(-5.0,2.2))

def teken(d,e,cx,cy,water=True):
    def T(pts): return [(cx+x*e,cy+y*e) for x,y in pts]
    d.polygon(T(lijf()),fill=KORAAL)
    d.polygon(T(STAART),fill=KORAAL)
    d.polygon(T(buik()),fill=BUIK)
    # keelgroeven
    w=max(1,int(e*0.35))
    for i in range(3):
        d.line(T([(-10.2+i*1.4,2.3+i*0.25),(-5.6+i*1.4,2.6+i*0.25)]),fill=KORAAL,width=w)
    d.polygon(T(VIN),fill=KORAAL,outline=DONKER)
    # bek: zachte lijn met mondhoek omhoog (glimlach)
    d.line(T(bez((-12.2,0.4),(-10,1.3),(-7.6,0.3),6)),fill=DONKER,width=max(1,int(e*0.45)))
    # oog met glans
    r=max(2,e*0.85); ox,oy=cx-8.4*e,cy-1.3*e
    d.ellipse([ox-r,oy-r,ox+r,oy+r],fill=NACHT)
    g=max(1,r*0.4); d.ellipse([ox-r*0.15-g,oy-r*0.35-g,ox-r*0.15+g,oy-r*0.35+g],fill=WIT)
    # spuitje
    sw=max(1,int(e*0.6))
    for a,b in [((-6.6,-6.4),(-8.4,-9.4)),((-6.0,-6.6),(-6.0,-10.0)),((-5.4,-6.4),(-3.6,-9.4))]:
        d.line(T([a,b]),fill=BEL,width=sw)
    if water:
        # waterlijnen achter de staart: hij zwemt
        for y,x0,x1 in [(-2.6,16.2,19.0),(0.4,16.6,20.4),(3.2,16.2,18.6)]:
            d.line(T([(x0,y),(x1,y)]),fill=ZACHT,width=max(1,int(e*0.4)))

def patrijspoort(S=600):
    im=Image.new('RGB',(S,S),(0,0,0)); d=ImageDraw.Draw(im)
    c=S/2; R=S*0.46
    d.ellipse([c-R,c-R,c+R,c+R],fill=(40,52,70))
    r=S*0.38
    d.ellipse([c-r,c-r,c+r,c+r],fill=WATER)
    # kader van het dier: x -12.6..20.4 (met waterlijnen), y -10..6 -> midden ~(3.9,-2)
    breed=33.0; e=(2*r*0.78)/breed
    teken(d,e,c-3.9*e,c+2.0*e)
    for k in range(8):
        a=math.pi/8+k*math.pi/4; bx=c+R*0.9*math.cos(a); by=c+R*0.9*math.sin(a)
        d.ellipse([bx-S*0.018,by-S*0.018,bx+S*0.018,by+S*0.018],fill=(170,190,210))
    return im

def horloge(D=454):
    im=Image.new('RGB',(D,D),(0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse([0,0,D-1,D-1],fill=NACHT)
    e=D*1.5/100
    teken(d,e,D/2-1.2*e,D*0.80)  # midden onder de klok
    return im

if __name__=='__main__':
    import sys
    uit=sys.argv[1] if len(sys.argv)>1 else '.'
    p=patrijspoort(); h=horloge()
    vel=Image.new('RGB',(1500,620),(12,14,22))
    vel.paste(p,(10,10)); vel.paste(h,(640,83))
    klein=horloge(260); vel.paste(klein,(1180,180))
    vel.save(f'{uit}/walvis-richting-daan.png')
