import sys, numpy as np
from PIL import Image
from scipy import ndimage
grot=np.array(Image.open(sys.argv[1]).convert('RGB'))
uit=[]
for f in sys.argv[3:]:
    a=np.array(Image.open(f).convert('RGB'))
    pure=lambda c:(a[:,:,0]==c[0])&(a[:,:,1]==c[1])&(a[:,:,2]==c[2])
    m=np.zeros(a.shape[:2],bool)
    for c in [(255,0,0),(255,255,0)]:
        l,n=ndimage.label(pure(c)); s=np.bincount(l.ravel()); s[0]=0
        for i in np.nonzero(s>150)[0]: m|=l==i
    ys,xs=np.nonzero(m); x0=95; y0=178
    print(f,x0,y0,xs.max()-x0+1,ys.max()-y0+1)
    # vloer: zwart onder in de cirkel
    o=a.copy()
    sub=o[y0:y0+208,x0:x0+208]; mm=m[y0:y0+208,x0:x0+208]
    blk=(sub.sum(2)==0)
    yy,xx=np.mgrid[0:208,0:208]; inc=(xx-103.5)**2+(yy-103.5)**2<103**2
    lk,n=ndimage.label(blk&inc&(yy>170)); s=np.bincount(lk.ravel()); s[0]=0
    fl=lk==np.argmax(s)
    sel=mm|fl
    sub[sel]=grot[sel]
    uit.append(Image.fromarray(o).crop((x0-20,y0-20,x0+228,y0+228)))
w=sum(i.width for i in uit); B=Image.new('RGB',(w,248),(255,255,255)); x=0
for i in uit: B.paste(i,(x,0)); x+=i.width
B.save(sys.argv[2]); B.resize((B.width*3,B.height*3),Image.NEAREST).save(sys.argv[2].replace('.png','-3x.png'))
