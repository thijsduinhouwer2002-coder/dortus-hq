import numpy as np, math
from PIL import Image
SIZES=[35,36,40,54,56,60,61,62,65,70]
C=dict(zw=(0,0,0),b0=(0x00,0xAA,0xFF),b1=(0x00,0x55,0xAA),b2=(0x00,0x00,0x55),lijn=(0xAA,0xFF,0xFF),wit=(255,255,255),zon=(0xFF,0xAA,0x55))
def surf(x): return 0.70-0.20*x+0.035*math.sin(2*math.pi*(1.3*x+0.1))
def hull(px,py,X,Y,W):
    # trapezoid: top width W at y=Y-h, bottom width 0.6W at y=Y+.3h
    h=0.085; top=Y-h*0.55; bot=Y+h*0.45
    if py<top or py>bot: return False
    t=(py-top)/(bot-top); half=W/2*(1-0.35*t)
    return abs(px-X)<=half
def sail(px,py,X,Y):
    # right triangle: mast at X-0.01, from Y-0.07 up to Y-0.33, leaning to right/back
    yb=Y-0.095; yt=Y-0.44
    if py<yt or py>yb: return False
    t=(py-yt)/(yb-yt)
    return X-0.02<=px<=X-0.02+0.22*t
def kleur(px,py,X,Y):
    if (px-.5)**2+(py-.5)**2>0.25: return None
    if sail(px,py,X,Y): return 'wit'
    if hull(px,py,X,Y,0.30): return 'wit'
    s=surf(px)
    if py<s: return 'zw'
    d=py-s
    if d<0.035: return 'lijn'
    if d<0.12: return 'b0'
    if d<0.22: return 'b1'
    return 'b2'
def maak(n,ss=10):
    X=0.60; Y=surf(X)-0.005
    im=np.zeros((n,n,4),np.uint8)
    for j in range(n):
        for i in range(n):
            cnt={}
            for a in range(ss):
                for b in range(ss):
                    k=kleur((i+(a+.5)/ss)/n,(j+(b+.5)/ss)/n,X,Y); cnt[k]=cnt.get(k,0)+1
            k=max(cnt,key=lambda q:(cnt[q], q=='wit'))
            # small features win: sail/hull if >=35% coverage
            if cnt.get('wit',0)>=0.35*ss*ss: k='wit'
            elif k!='lijn' and cnt.get('lijn',0)>=0.3*ss*ss and k in('b0','zw'): k='lijn'
            if k is None:
                if sum(v for q,v in cnt.items() if q is not None)>=0.5*ss*ss: k='zw'
                else: continue
            im[j,i,:3]=C[k]; im[j,i,3]=255
    return Image.fromarray(im,'RGBA')
for n in SIZES: maak(n).save(f'ic/icoon-{n}.png')
# sheet: each at 1x and 6x on dark grey and on white
from PIL import ImageDraw
W=sum(n*6+20 for n in SIZES)+20
sh=Image.new('RGB',(W,560),(40,40,44)); d=ImageDraw.Draw(sh); x=20
for n in SIZES:
    im=Image.open(f'ic/icoon-{n}.png')
    big=im.resize((n*6,n*6),Image.NEAREST); sh.paste(big,(x,20),big)
    sh.paste(im,(x,460),im); d.text((x,440),f'{n} px',fill='white')
    x+=n*6+20
sh.save('icoon-blad.png')
