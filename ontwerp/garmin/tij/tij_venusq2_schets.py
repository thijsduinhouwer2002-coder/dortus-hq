from PIL import Image, ImageDraw, ImageFont
import math
W,H=320,360; SS=4
TH=dict(zb=(0xFF,0x8C,0x3C),zo=(0x6E,0x19,0x28),uren=(0xFF,0xEE,0xD6),mn=(0xFF,0xAA,0x50),txt=(0xFF,0xE2,0xBE),punt=(0x96,0x68,0x4C),boot=(0xFF,0xF6,0xE6))
def meng(a,b,i,n): return tuple(int(a[k]+(b[k]-a[k])*i/n) for k in range(3))
def lichter(c,e): return tuple(min(255,v+e) for v in c)
im=Image.new('RGB',(W*SS,H*SS),'black'); d=ImageDraw.Draw(im)
B='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'
def F(px): return ImageFont.truetype(B,int(px*SS/0.73))
def txt(x,y,s,px,c): d.text((x*SS,y*SS),s,font=F(px),fill=c,anchor='mm')
txt(160,34,'TUE 17',19,TH['txt'])
# time (squeezed like the condensed tijd font)
f=F(90); tmp=Image.new('RGBA',(700*SS,140*SS),(0,0,0,0)); td=ImageDraw.Draw(tmp)
w1=td.textlength('04',font=f); gap=30*SS
td.text((0,70*SS),'04',font=f,fill=TH['uren'],anchor='lm')
cx=w1+gap/2
td.rectangle([cx-5*SS,(70-24)*SS,cx+5*SS,(70-14)*SS],fill=TH['punt']); td.rectangle([cx-5*SS,(70+14)*SS,cx+5*SS,(70+24)*SS],fill=TH['punt'])
td.text((w1+gap,70*SS),'22',font=f,fill=TH['mn'],anchor='lm')
tw=int(w1+gap+td.textlength('22',font=f)); tmp=tmp.crop((0,0,tw,140*SS))
tmp=tmp.resize((int(tw*0.62),140*SS))
im.paste(tmp,(160*SS-tmp.width//2,(106-70)*SS),tmp)
# fields
for x,v,ic in [(90,'80','♥'),(160,'35','⚡'),(230,'0','▲')]:
    txt(x,164,ic,14,TH['mn'] if ic=='♥' else TH['txt']); txt(x,186,v,21,TH['txt'])
# sea: BB history over day rising 20 -> 72, full width
top,bot=248,318
def lvl(v): return bot-(bot-top)*v/100
hist=[20,22,25,24,30,38,45,52,55,60,63,66,68,70,72]
nuX=250
def surf(x):
    if x>=nuX: v=hist[-1]
    else:
        t=x/nuX*(len(hist)-1); i=int(t); f_=t-i; v=hist[i]+(hist[min(i+1,len(hist)-1)]-hist[i])*f_
    return lvl(v)+2.5*math.sin(x/320*2*math.pi*2.5)
pts=[(x,surf(x)) for x in range(0,W+1,2)]
bands=[0,12,26,45]
for i,o in enumerate(bands):
    c=meng(TH['zb'],TH['zo'],i,3)
    poly=[(x*SS,(y+o)*SS) for x,y in pts]+[(W*SS,H*SS),(0,H*SS)]
    d.polygon(poly,fill=c)
d.line([(x*SS,y*SS) for x,y in pts],fill=lichter(TH['zb'],70),width=3*SS)
# boat
by=surf(nuX); s=16
hull=[(nuX-s,by-5),(nuX+s,by-5),(nuX+s*0.6,by+4),(nuX-s*0.6,by+4)]
d.polygon([(x*SS,y*SS) for x,y in hull],fill=TH['boot'])
d.line([(nuX*SS,(by-5)*SS),(nuX*SS,(by-29)*SS)],fill=TH['boot'],width=2*SS)
d.polygon([(nuX+2)*SS,(by-29)*SS,(nuX+2)*SS,(by-8)*SS,(nuX+16)*SS,(by-8)*SS],fill=TH['mn'])
# BB number with outline + golfje
f=F(36); bx=150; byy=222
oc=meng(TH['zo'],(0,0,0),4,10)
for dx in (-2,0,2):
    for dy in (-2,0,2):
        d.text(((bx+dx)*SS,(byy+dy)*SS),'72',font=f,fill=oc,anchor='mm')
d.text((bx*SS,byy*SS),'72',font=f,fill='white',anchor='mm')
gx=bx+d.textlength('72',font=f)/SS/2+5
for k in (-3,3):
    d.line([((gx+t/8*16)*SS,(byy+k+2.5*math.sin(t/8*3*math.pi))*SS) for t in range(9)],fill=lichter(TH['zb'],70),width=3*SS)
im=im.resize((W,H),Image.LANCZOS)
# rounded screen mask
m=Image.new('L',(W,H),0); ImageDraw.Draw(m).rounded_rectangle([0,0,W-1,H-1],radius=44,fill=255)
out=Image.new('RGB',(W,H),(30,30,30)); out.paste(im,(0,0),m); out.save('vsq-1x.png')
sheet=Image.new('RGB',(W*2+W+60,H*2+40),(244,241,234)); sheet.paste(out.resize((W*2,H*2),Image.NEAREST),(20,20)); sheet.paste(out,(W*2+40,20)); sheet.save('vsq-blad.png')
