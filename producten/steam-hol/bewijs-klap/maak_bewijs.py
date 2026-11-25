import sys
from PIL import Image, ImageChops
import numpy as np
W='/tmp/claude-0/w/'
film=Image.open(W+'film.gif')
def fr(i):
    film.seek(i); return film.convert('RGBA').copy()
ster=Image.open(sys.argv[1]).convert('RGBA')   # 4 cellen
bord=Image.open(sys.argv[2]).convert('RGBA')
out=sys.argv[3]
S=3; CEL=16*S
cells=[ster.crop((i*ster.height,0,(i+1)*ster.height,ster.height)).convert('RGBa').resize((CEL,CEL),Image.LANCZOS).convert('RGBA') for i in range(4)]

def nine(src, rect, m, R=128):
    x0,y0,x1,y1=rect; Sz=src.width
    xs=[x0,x0+m,x1-m,x1]; ys=[y0,y0+m,y1-m,y1]; bx=[0,R,Sz-R,Sz]
    lay=Image.new('RGBA',(1024,120),(0,0,0,0))
    for i in range(3):
        for j in range(3):
            w=round(xs[i+1])-round(xs[i]); h=round(ys[j+1])-round(ys[j])
            if w<=0 or h<=0: continue
            part=src.crop((bx[i],bx[j],bx[i+1],bx[j+1])).convert('RGBa').resize((w,h),Image.BILINEAR).convert('RGBA')
            lay.alpha_composite(part,(round(xs[i]),round(ys[j])))
    return lay

RECT=(697,57,1018,117); M=13.5
BG=np.array([74,49,41],float)
def kader(im):
    a=np.array(im.convert('RGB')).astype(float)
    # tekst losmaken van het oude bruine vlak
    x0,y0,x1,y1=705,64,1010,110
    sub=a[y0:y1,x0:x1]
    L=sub.mean(2); Lbg=BG.mean()
    al=np.clip((L-Lbg)/ (np.maximum(sub.max(2),1)-Lbg+1e-6),0,1)
    al=np.clip((L-Lbg)/120.0,0,1)
    al[al<0.12]=0
    col=np.clip((sub-(1-al[...,None])*BG)/np.maximum(al[...,None],1e-3),0,255)
    lay=nine(bord,RECT,M)
    im=im.copy(); im.alpha_composite(lay)
    t=np.dstack([col,al*255]).astype(np.uint8)
    im.alpha_composite(Image.fromarray(t,'RGBA'),(x0,y0))
    return im

def zonder_oude_ster(im):
    schoon=fr(30)
    box=(286,66,334,112)
    im=im.copy(); im.paste(schoon.crop(box),box[:2]); return im

def flits(im, sterkte):
    a=np.array(im).astype(float); b=np.array(fr(43)).astype(float)
    reg=np.zeros(a.shape[:2],bool); reg[60:115,288:334]=True
    d=np.abs(a[...,:3]-b[...,:3]).sum(2)>40
    m=reg&d
    a[m,:3]=a[m,:3]*(1-sterkte)+255*sterkte
    return Image.fromarray(a.astype(np.uint8),'RGBA')

C=(309,90)
beelden=[]  # (beeld, ms)
for f in (39,40,41):
    beelden.append((kader(fr(f)),600))
h=kader(fr(42))
beelden.append((h,240)); beelden.append((flits(h,1.0),120)); beelden.append((flits(h,0.5),120))
b44=kader(zonder_oude_ster(fr(44)))
for i in range(4):
    k=b44.copy(); k.alpha_composite(cells[i],(C[0]-CEL//2,C[1]-CEL//2)); beelden.append((k,125))
beelden.append((b44,100))
for f in (45,46,47):
    beelden.append((kader(fr(f)),600))
def gif(pad,schaal):
    ims=[b.convert('RGB').resize((1024*schaal,120*schaal),Image.NEAREST) if schaal>1 else b.convert('RGB') for b,_ in beelden]
    ims[0].save(pad,save_all=True,append_images=ims[1:],duration=[d for _,d in beelden],loop=0,optimize=False)
gif(out+'/val-klap-120-ware-maat.gif',1)
# 2x: alleen het stuk rond de val en het bord, anders te groot
ims=[b.convert('RGB').resize((2048,240),Image.NEAREST) for b,_ in beelden]
ims[0].save(out+'/val-klap-2x.gif',save_all=True,append_images=ims[1:],duration=[d for _,d in beelden],loop=0)
# stilstaand: reeks van de klap op 2x (val tot vonken)
sel=[3,4,5,6,7,8,9]
st=Image.new('RGB',(160*2*len(sel),240))
for n,i in enumerate(sel):
    st.paste(beelden[i][0].convert('RGB').crop((230,0,390,120)).resize((320,240),Image.NEAREST),(320*n,0))
st.save(out+'/klap-reeks-2x.png')
beelden[7][0].convert('RGB').save(out+'/strook-120-klap-en-bord.png')
beelden[7][0].convert('RGB').resize((2048,240),Image.NEAREST).save(out+'/strook-120-klap-en-bord-2x.png')
# voor en na op ware maat
vn=Image.new('RGB',(1024,240)); vn.paste(fr(44).convert('RGB'),(0,0)); vn.paste(beelden[7][0].convert('RGB'),(0,120)); vn.save(out+'/voor-boven-na-onder-120.png')
print('klaar',len(beelden))
