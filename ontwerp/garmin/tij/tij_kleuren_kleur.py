from PIL import Image, ImageDraw, ImageFont
import numpy as np, scipy.ndimage as nd
def h(c): return np.array([int(c[i:i+2],16) for i in (0,2,4)])
OLD={
 'fr255':dict(b=['AAFF55','55FF00','55AA00','005500'],line='FFFFAA',mn='AAFF55',txt='FFFFAA',punt='55AA55',outl=['555555']),
 'fr245':dict(b=['FFAA55','FF5500','AA0000','550000'],line='FFFFAA',mn='FFAA55',txt='FFFFAA',punt='AA5555',outl=['550000']),
 'fr55': dict(b=['FFFF00','FF0000','FF0000','FF0000'],line='FFFF00',mn='FFFF00',txt=None,punt='FF0000',outl=['FF0000']),
}
def eq(a,c): return (abs(a-h(c))<=8).all(2)
def comps(m):
    lab,n=nd.label(m); r=[]
    for i,s in enumerate(nd.find_objects(lab)):
        r.append((s, lab==i+1))
    return r
def recolor(dev, N):
    """N: dict b(4), line, sail, mn, txt, punt, outl"""
    a=np.array(Image.open(f'{dev}-1.png').convert('RGB')).astype(int)
    o=a.copy(); O=OLD[dev]
    reg=np.zeros(a.shape[:2],bool); reg[140:520,60:390]=True
    # top of big band0 component
    b0=eq(a,O['b'][0])&reg
    big=[(s,m) for s,m in comps(b0) if m.sum()>800 and s[1].stop-s[1].start>150]
    seatop=min(s[0].start for s,m in big); T1=seatop-30
    b1=eq(a,O['b'][1])&reg; ys=np.where(b1.any(1))[0]; b1top=ys.min()
    yy=np.arange(a.shape[0])[:,None]*np.ones(a.shape[1],int)[None,:]
    def put(m,c): o[m]=h(c)
    # deeper bands first (fr55 has b1..b3 the same old colour: split by depth fractions of old band boundaries unknown -> handled below)
    if dev=='fr55':
        red=eq(a,'FF0000')&reg
        punt=red&(yy<T1); put(punt,N['punt'])
        sea=red&(yy>=T1)
        # outline around number: red comps not touching bottom area
        for s,m in comps(sea):
            if m.sum()<400: put(m,N['outl'])
            else:
                # split big red into three depth bands using column-wise top
                top=np.full(a.shape[1],10**6)
                cols=np.where(m.any(0))[0]
                for x in cols: top[x]=np.where(m[:,x])[0].min()
                for x in cols:
                    col=np.where(m[:,x])[0]
                    for y in col:
                        d=y-top[x]
                        i=1 if d<7 else (2 if d<16 else 3)
                        o[y,x]=h(N['b'][i])
        yel=eq(a,'FFFF00')&reg
        for s,m in comps(yel):
            if s[0].start<T1: put(m,N['mn'])
            elif m.sum()<400: put(m,N['sail'])
            else:
                # waterline: top 3 px of each column -> line
                cols=np.where(m.any(0))[0]
                for x in cols:
                    col=np.where(m[:,x])[0]
                    for y in col: o[y,x]=h(N['line'] if y-col.min()<3 else N['b'][0])
        return o.astype(np.uint8)
    for i in (3,2,1):
        m=eq(a,O['b'][i])&reg
        if O['b'][i] in O['outl'] or i==3:
            put(m&(yy<b1top-2),N['outl']); put(m&(yy>=b1top-2),N['b'][i])
        else: put(m,N['b'][i])
    for c in O['outl']:
        if c not in O['b']: put(eq(a,c)&reg&(yy<seatop+5),N['outl'])
    for s,m in comps(b0):
        if s[0].start<T1: put(m,N['mn'])
        elif m.sum()<400: put(m,N['sail'])
        else: put(m,N['b'][0])
    ln=eq(a,O['line'])&reg
    put(ln&(yy<T1),N['txt']); put(ln&(yy>=T1),N['line'])
    put(eq(a,O['punt'])&reg&(yy<T1),N['punt'])
    return o.astype(np.uint8)
def crop(dev,arr):
    im=Image.fromarray(arr)
    W,H=im.size; return im.crop((40,120,W-40,H-110))
