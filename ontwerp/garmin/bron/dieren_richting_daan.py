# Richting v2 voor walvis en schildpad van Ebb (Daan, keuring 4). Alleen MIP-kleuren, geen verloop, geen lijnen
# die op klein formaat wegvallen: alles zijn gevulde vlakken. Punten in eenheden e = D/100 (zoals Teken.mc),
# na verschuiving zo dat het kader van het hele dier (met spuitje en vin) rond (0,0) ligt: cx,cy is het midden.
import math
from PIL import Image, ImageDraw, ImageFont

KORAAL=(255,85,85); LICHT=(255,170,170); DONKER=(170,0,0); BEL=(85,170,255)
WIT=(255,255,255); NACHT=(0,0,85); WATER=(0,0,170); SCHUIM=(85,255,255); ZACHT=(85,170,170)

def bez(p0,p1,p2,n=8):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0],(1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/n for i in range(n+1)]]

# ---------- walvis (kijkt naar links) ----------
W_LIJF = (bez((-12,1.0),(-12.6,-5.2),(-6,-5.6)) + bez((-6,-5.6),(2,-6.0),(8.5,-1.6),6)
          + [(11,-0.7),(11,0.7)] + bez((11,0.7),(6,2.0),(-2,3.4),6) + bez((-2,3.4),(-9,4.2),(-12,1.0),6))
# staart als tekenfilmwalvis: de staartsteel buigt omhoog, de twee liggende vinnen wijken uit elkaar (geen vissenstaart)
W_STAART = (bez((9.6,-1.4),(12.0,-1.6),(12.8,-3.6),4) + bez((12.8,-3.6),(11.0,-5.4),(9.6,-6.2),4)
            + bez((9.6,-6.2),(12.4,-6.0),(13.6,-4.8),3) + bez((13.6,-4.8),(15.0,-6.4),(17.4,-6.6),3)
            + bez((17.4,-6.6),(15.6,-4.4),(14.0,-3.2),4) + bez((14.0,-3.2),(13.0,0.4),(10.0,0.8),4))
W_BUIK = bez((-11.8,1.0),(-5,0.4),(5.5,0.9),6) + bez((5.5,0.9),(-1,3.4),(-6,3.7),5) + bez((-6,3.7),(-10.4,3.6),(-11.8,1.0),4)
W_VIN = bez((-5.2,2.0),(-1.6,2.2),(1.6,4.6),5) + bez((1.6,4.6),(1.6,5.8),(0.2,5.6),3) + bez((0.2,5.6),(-3.8,4.6),(-5.2,2.0),4)   # schuin naar achteren
W_BEK = [(-12.3,0.3),(-10.5,1.1),(-8.4,0.7),(-7.6,0.1),(-8.4,1.3),(-10.6,1.8),(-12.1,1.0)]   # gevulde glimlach, mondhoek omhoog
W_SPUIT = [[(-7.0,-6.2),(-7.8,-6.4),(-9.6,-9.4),(-8.6,-9.8)], [(-6.4,-6.4),(-5.6,-6.4),(-5.6,-10.2),(-6.4,-10.2)], [(-5.0,-6.4),(-4.2,-6.2),(-2.6,-9.4),(-3.4,-9.8)]]
W_OOG = (-8.4,-1.6,1.15)   # x, y, straal; glans 45% linksboven

# ---------- schildpad (kijkt naar links) ----------
S_ACHTERPOOT = bez((4.0,1.6),(6.6,1.8),(8.0,4.0),4) + bez((8.0,4.0),(6.0,4.2),(3.0,2.6),4)
S_VOORPOOT = bez((-3.4,1.6),(-0.6,2.6),(1.4,5.6),5) + bez((1.4,5.6),(0.6,6.4),(-0.6,5.8),3) + bez((-0.6,5.8),(-3.4,4.6),(-5.0,2.2),4)
S_KOP = bez((-5.2,-0.6),(-7.4,-2.8),(-10.2,-1.6),5) + bez((-10.2,-1.6),(-11.0,0.2),(-9.0,0.9),3) + bez((-9.0,0.9),(-7.0,1.0),(-5.0,1.4),3)
S_STAART = [(6.4,0.6),(8.6,0.9),(6.4,1.8)]
S_SCHILD = bez((-6.2,1.6),(-6.0,-6.4),(1.0,-6.4),7) + bez((1.0,-6.4),(7.4,-6.0),(7.4,1.6),7)
S_RAND = bez((-6.4,1.0),(0.6,0.6),(7.6,1.0),6) + bez((7.6,1.0),(7.0,2.8),(5.0,2.8),3) + bez((5.0,2.8),(0.6,3.2),(-4.4,2.8),4) + bez((-4.4,2.8),(-6.4,2.6),(-6.4,1.0),3)   # buikschild, lichte tint zoals de buik van de walvis
S_PLATEN = [[(-0.6,-4.6),(2.2,-4.6),(3.4,-2.4),(2.2,-0.4),(-0.6,-0.4),(-1.8,-2.4)],   # zeshoek in het midden
            [(-2.8,-4.0),(-1.6,-4.9),(-2.6,-2.4)][:0] + [(-4.6,-0.4),(-4.2,-3.0),(-2.6,-4.4),(-2.4,-2.6),(-1.6,-0.4)],
            [(3.6,-4.4),(5.2,-3.2),(5.8,-0.4),(4.2,-0.4),(4.6,-2.4)]]
S_OOG = (-8.4,-1.4,0.9)

def kader(lijsten):
    xs=[p[0] for l in lijsten for p in l]; ys=[p[1] for l in lijsten for p in l]
    return (min(xs)+max(xs))/2,(min(ys)+max(ys))/2,max(xs)-min(xs),max(ys)-min(ys)

def schuif(groepen,dx,dy):
    return [[(x-dx,y-dy) for x,y in g] for g in groepen]

def walvis_delen():
    alles=[W_LIJF,W_STAART,W_BUIK,W_VIN,W_BEK]+W_SPUIT
    mx,my,b,h=kader(alles)
    return alles,(mx,my,b,h)

def schildpad_delen():
    alles=[S_ACHTERPOOT,S_VOORPOOT,S_KOP,S_STAART,S_SCHILD,S_RAND]+S_PLATEN
    mx,my,b,h=kader(alles)
    return alles,(mx,my,b,h)

def cirkel(d,x,y,r,kleur): d.ellipse([x-r,y-r,x+r,y+r],fill=kleur)

def walvis(d,cx,cy,e):
    alles,(mx,my,b,h)=walvis_delen()
    T=lambda pts:[(cx+(x-mx)*e,cy+(y-my)*e) for x,y in pts]
    d.polygon(T(W_STAART),fill=KORAAL); d.polygon(T(W_LIJF),fill=KORAAL)
    d.polygon(T(W_BUIK),fill=LICHT); d.polygon(T(W_VIN),fill=KORAAL)
    d.polygon(T(W_BEK),fill=DONKER)
    for s in W_SPUIT: d.polygon(T(s),fill=BEL)
    ox,oy,r=W_OOG; X,Y=cx+(ox-mx)*e,cy+(oy-my)*e; R=max(1.6,r*e)
    cirkel(d,X,Y,R,NACHT)
    if R>=2.5: cirkel(d,X-R*0.3,Y-R*0.3,max(1,R*0.42),WIT)

def schildpad(d,cx,cy,e):
    alles,(mx,my,b,h)=schildpad_delen()
    T=lambda pts:[(cx+(x-mx)*e,cy+(y-my)*e) for x,y in pts]
    for g in (S_ACHTERPOOT,S_STAART,S_KOP,S_VOORPOOT): d.polygon(T(g),fill=KORAAL)
    d.polygon(T(S_SCHILD),fill=KORAAL)
    for p in S_PLATEN: d.polygon(T(p),fill=LICHT)
    d.polygon(T(S_RAND),fill=LICHT)
    d.polygon(T(S_VOORPOOT),fill=KORAAL)
    ox,oy,r=S_OOG; X,Y=cx+(ox-mx)*e,cy+(oy-my)*e; R=max(1.4,r*e)
    cirkel(d,X,Y,R,NACHT)
    if R>=2.5: cirkel(d,X-R*0.3,Y-R*0.3,max(1,R*0.42),WIT)

def font(px):
    for f in ['/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        try: return ImageFont.truetype(f,int(px))
        except: pass
    return ImageFont.load_default()

def horloge(D, dier='walvis', tijd='3:03', diepte='183 m'):
    im=Image.new('RGB',(D,D),(0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse([0,0,D-1,D-1],fill=NACHT)
    f=font(D*0.30); d.text((D/2,D*0.47),tijd,font=f,fill=WIT,anchor='mm')
    d.text((D/2,D*0.25),diepte,font=font(D*0.065),fill=ZACHT,anchor='mm')
    # dier in het midden onder het getal, kader rond (D/2, 0.79 D)
    if dier=='walvis': walvis(d,D/2,D*0.79,D*1.25/100)
    else: schildpad(d,D/2,D*0.79,D*1.25/100)
    return im

def patrijspoort(S, dier='walvis'):
    im=Image.new('RGB',(S,S),(0,0,0)); d=ImageDraw.Draw(im)
    c=S/2; R=S*0.46; r=S*0.38
    d.ellipse([c-R,c-R,c+R,c+R],fill=(40,52,70)); d.ellipse([c-r,c-r,c+r,c+r],fill=WATER)
    _,(mx,my,b,h)=(walvis_delen() if dier=='walvis' else schildpad_delen())
    e=(2*r*0.74)/max(b,h)
    (walvis if dier=='walvis' else schildpad)(d,c,c,e)
    for k in range(8):
        a=math.pi/8+k*math.pi/4; bx=c+R*0.9*math.cos(a); by=c+R*0.9*math.sin(a)
        cirkel(d,bx,by,S*0.018,(170,190,210))
    return im

def zeelog(D):
    # vier rijen met dezelfde optische breedte; de walvis het breedst
    im=Image.new('RGB',(D,D),(0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse([0,0,D-1,D-1],fill=(0,0,0),outline=(30,30,30))
    d.text((D/2,D*0.22),'met so far',font=font(D*0.06),fill=ZACHT,anchor='mm')
    f=font(D*0.065)
    rij=[0.36,0.48,0.60,0.72]
    # vis en kwal zoals in de app (dier(), r = 0.06 D)
    r=D*0.06*0.75; x=D*0.40
    y=D*rij[0]; d.ellipse([x-r,y-r*0.6,x+r,y+r*0.6],fill=KORAAL); d.polygon([(x+r-2,y),(x+r+r*0.7,y-r*0.6),(x+r+r*0.7,y+r*0.6)],fill=KORAAL)
    y=D*rij[1]; d.pieslice([x-r,y-r,x+r,y+r],180,360,fill=KORAAL)
    for i in (-1,0,1): d.line([(x+i*r*0.6,y+2),(x+i*r*0.6+2,y+r*0.9)],fill=KORAAL,width=max(2,int(D/130)))
    schildpad(d,x,D*rij[2],D*0.75/100)
    walvis(d,x,D*rij[3],D*0.62/100)
    for y,t in zip(rij,['1:00','1:30','2:00','3:00']): d.text((D*0.60,D*y),t,font=f,fill=WIT,anchor='mm')
    return im

if __name__=='__main__':
    import sys
    uit=sys.argv[1] if len(sys.argv)>1 else '.'
    vel=Image.new('RGB',(2120,1240),(12,14,22)); dv=ImageDraw.Draw(vel)
    vel.paste(patrijspoort(560,'walvis'),(20,20)); vel.paste(patrijspoort(560,'schildpad'),(20,640))
    vel.paste(horloge(454,'walvis'),(620,73)); vel.paste(horloge(454,'schildpad','2:03','123 m'),(620,713))
    vel.paste(horloge(260,'walvis'),(1110,170)); vel.paste(horloge(260,'schildpad','2:03','123 m'),(1110,810))
    vel.paste(zeelog(454),(1400,73)); vel.paste(zeelog(260),(1500,810))
    for x,y,t in [(20,600,'patrijspoort (loep en icoon)'),(620,540,'454 px, midden onder het getal'),(1110,440,'260 px (fenix 7, FR255)'),(1400,540,'Sea log 454 px'),(1500,1080,'Sea log 260 px')]:
        dv.text((x,y),t,font=font(20),fill=(200,200,200))
    vel.save(f'{uit}/dieren-richting-daan-v2.png')
    # punten voor Teken.mc, al gecentreerd
    for naam,(alles,(mx,my,b,h)) in [('walvis',walvis_delen()),('schildpad',schildpad_delen())]:
        print(naam,'kader b=%.1f h=%.1f, verschuiving dx=%.2f dy=%.2f'%(b,h,mx,my))
