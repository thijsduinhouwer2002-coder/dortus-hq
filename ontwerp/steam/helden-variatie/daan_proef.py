import sys
from PIL import Image
K="/home/claude/dortus-hq/producten/steam-hol/godot/kunst/3d/"
bg=Image.open("/tmp/claude-0/k/los-059.png").convert("RGBA")
def cel(blad,i,w,h): return Image.open(K+blad+".png").convert("RGBA").crop((i*w,0,i*w+w,h))
hoeden=[cel("hoeden",i,63,46) for i in range(10)]
S=0.6
def held(blad,sx,sy,hoed,skin=None):
    c=cel(blad,0,109,70)
    if skin:
        px=c.load()
        for y in range(70):
            for x in range(109):
                r,g,b,a=px[x,y]
                if a>0 and r>225 and g>200 and 150<b<232 and r-b>18:
                    f=skin
                    px[x,y]=(int(r*f[0]),int(g*f[1]),int(b*f[2]),a)
    W,H=int(109*S*sx),int(70*S*sy)
    c=c.resize((W,H),Image.LANCZOS)
    hz=hoeden[hoed]; hz=hz.resize((int(63*S),int(46*S)),Image.LANCZOS)
    return c,hz
def zet(img,blad,x,sx,sy,hoed,skin=None,voet=110):
    c,hz=held(blad,sx,sy,hoed,skin)
    ax=54*S*sx; ny=64.45*S*sy
    ox=int(x-ax); oy=int(voet-ny)
    img.alpha_composite(c,(ox,oy))
    # hoed nul op 50.45 bladpx boven voeten (geschaald), x op anker+0.5 spelpx
    hy=voet-50.45*S*sy; hx=x+2.5*S*sx
    img.alpha_composite(hz,(int(hx-32*S),int(hy-37.7*S)))
def strook(var):
    img=bg.crop((80,0,560,120)).copy()
    # leeg vloer: overdek bestaande helden met vloerstukje
    vl=bg.crop((230,40,300,118)); 
    for x in (0,70,140,210,280,350,420): img.paste(vl,(x,40))
    hs=[3,6,7,1,9]
    sc=[(1,1)]*5 if var=="A" else [(1.0,0.9),(1.2,1.0),(0.86,1.1),(1.1,0.88),(0.92,1.14)]
    sk=[None]*5 if var!="C" else [(0.98,0.86,0.76),(0.74,0.55,0.42),(1,0.9,0.84),(0.52,0.37,0.30),(0.9,0.74,0.6)]
    for i in range(5): zet(img,"held%d"%i,60+i*85,sc[i][0],sc[i][1],hs[i],sk[i])
    return img.convert("RGB")
rows=[strook(v) for v in "ABC"]
import sys
out=Image.new("RGB",(480,3*120+20),(40,40,40))
for i,r in enumerate(rows): out.paste(r,(0,i*130))
out.save("helden-1x.png"); out.resize((out.width*3,out.height*3),Image.LANCZOS).save("helden-3x.png")
