import glob,re
from PIL import Image, ImageDraw
fr=sorted(glob.glob('gif-*.png'))
pos={'Initiative':(262,440),'Damage':(500,496),'Wisdom':(395,553)}
def cursor(im,x,y):
    d=ImageDraw.Draw(im); s=1.25
    pts=[(0,0),(0,17),(4,13),(7,20),(10,19),(7,12),(12,12)]
    p=[(x+a*s,y+b*s) for a,b in pts]
    d.polygon(p,fill='white',outline='black')
frames=[];durs=[]
for i,f in enumerate(fr):
    n=f[4:-4]; im=Image.open(f).convert('RGB')
    m=re.match(r'\d+-(hover-)?(Initiative|Damage|Wisdom)',n)
    if m and 'rust' not in n: cursor(im,*pos[m.group(2)])
    im=im.crop((60,130,1000,696)).resize((800,482),Image.LANCZOS)
    frames.append(im)
    ms=re.search(r'-(\d+)ms',n)
    if 'start' in n: d=1100
    elif 'hover' in n: d=200
    elif 'rust' in n: d=500
    else:
        nxt=re.search(r'-(\d+)ms',fr[i+1]) if i+1<len(fr) else None
        d=(int(nxt.group(1))-int(ms.group(1))) if nxt else 70
    durs.append(max(40,d))
frames[0].save('/tmp/claude-0/raw.gif',save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=True,disposal=1)
print(len(frames),sum(durs))
