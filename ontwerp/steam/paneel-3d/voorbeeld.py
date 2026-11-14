from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
st=Image.open('s160.png').convert('RGBA').crop((0,598,1024,768))
src=Image.open('paneel384.png').convert('RGBA')
def nine(dst, rect, m, src, b=128):
    x0,y0,x1,y1=rect; S=src.size[0]
    xs=[x0,x0+m,x1-m,x1]; ys=[y0,y0+m,y1-m,y1]; bs=[0,b,S-b,S]
    for i in range(3):
        for j in range(3):
            w=xs[i+1]-xs[i]; h=ys[j+1]-ys[j]
            part=src.crop((bs[i],bs[j],bs[i+1],bs[j+1])).resize((w,h),Image.LANCZOS)
            dst.alpha_composite(part,(xs[i],ys[j]))
def font(sz,w):
    f=ImageFont.truetype('font/fredoka.ttf',sz); f.set_variation_by_axes([w,100]); return f
def mock(st):
    a=st.copy(); R=(694,12,1022,120)
    sh=Image.new('RGBA',a.size,(0,0,0,0)); d=ImageDraw.Draw(sh); d.rounded_rectangle((R[0]+2,R[1]+4,R[2]+2,R[3]+4),12,fill=(20,8,24,140))
    a.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4))); nine(a,R,18,src)
    d=ImageDraw.Draw(a)
    d.text((712,28),"Big Gloop",font=font(18,600),fill=(255,210,90))
    d.text((712,53),"Bought.",font=font(15,450),fill=(246,232,206))
    S=4; c=Image.new('RGBA',(18*S,18*S),(0,0,0,0)); cd=ImageDraw.Draw(c)
    cd.ellipse((0,0,17*S,17*S),fill=(170,105,30)); cd.ellipse((1*S,1*S,15*S,15*S),fill=(242,182,50)); cd.ellipse((4*S,3*S,9*S,7*S),fill=(255,236,150))
    a.alpha_composite(c.resize((18,18),Image.LANCZOS),(968,30))
    d.text((991,28),"27",font=font(17,600),fill=(246,232,206))
    bx=(712,80,816,104)
    d.rounded_rectangle(bx,12,fill=(224,168,58)); d.rounded_rectangle((bx[0]+2,bx[1]+2,bx[2]-2,bx[3]-2),10,fill=(74,48,84))
    d.text(((bx[0]+bx[2])//2,(bx[1]+bx[3])//2+1),"Undo  +45",font=font(15,550),fill=(255,226,150),anchor='mm')
    return a
oud=st.copy(); nieuw=mock(st); nieuw.save('kaart_nieuw.png')
both=Image.new('RGBA',(1024,340),(30,20,35,255)); both.alpha_composite(oud,(0,0)); both.alpha_composite(nieuw,(0,170)); both.save('kaart_voor_na.png')
z=Image.new('RGBA',(990,660)); z.alpha_composite(oud.crop((692,10,1022,120)).resize((990,330),Image.NEAREST),(0,0)); z.alpha_composite(nieuw.crop((692,10,1022,120)).resize((990,330),Image.LANCZOS),(0,330)); z.save('kaart_voor_na_3x.png')
