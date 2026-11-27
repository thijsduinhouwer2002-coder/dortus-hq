# Header v11 "bureaublad": echt spelbeeld onderaan, werkvenster en logo erboven.
import sys, math, random, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(__file__)); from logo import logo
R=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..",".."))
k=2; W,H=920*k,430*k
TB=40*k; SCH=float(os.environ.get("SCH","1.25")); X0=int(os.environ.get("X0","730"))
bron=Image.open(R+"/producten/steam-hol/itch/bron-omslag-f5850.png").convert("RGB")
uw=round(920/SCH); sh=round(160*SCH*k)
strook=bron.crop((X0,0,X0+uw,160)).resize((W,sh),Image.LANCZOS)
SY=H-TB-sh
# behang: warme avond, lila naar perzik, zachte heuvels
im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im)
top=tuple(int(c) for c in os.environ.get("TOP","92,96,170").split(",")); bot=tuple(int(c) for c in os.environ.get("BOT","246,176,150").split(","))
for y in range(H):
    t=min(1,y/(SY+20)); t=t**0.9
    d.line([(0,y),(W,y)],fill=tuple(int(a+(b-a)*t) for a,b in zip(top,bot)))
hv=Image.new("RGBA",(W,H),(0,0,0,0)); dh=ImageDraw.Draw(hv)
for kl,basis,amp,f in [((176,120,150),SY-40*k,22*k,0.4),((132,92,136),SY-14*k,16*k,2.1)]:
    pts=[(0,H)]+[(x,basis-amp*(0.6*math.sin(x/(W/2.4)+f)+0.4*math.sin(x/(W/5.3)+2*f))) for x in range(0,W+1,6)]+[(W,H)]
    dh.polygon(pts,fill=kl+(255,))
im.paste(hv,(0,0),hv)
# sterretjes
random.seed(4)
for i in range(40):
    x,y=random.uniform(0,W),random.uniform(0,SY*0.5); r=random.choice([1,1,1.5,2])*k
    d.ellipse([x-r,y-r,x+r,y+r],fill=(255,240,220))
im=im.convert("RGBA")
# werkvenster rechtsboven: een spreadsheet
WX0,WY0,WX1,WY1=[int(v*k) for v in (548,26,896,SY/k+30)]
sch=Image.new("RGBA",(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sch)
ds.rounded_rectangle([WX0+6*k,WY0+10*k,WX1+6*k,WY1+10*k],radius=8*k,fill=(30,10,40,110)); sch=sch.filter(ImageFilter.GaussianBlur(8*k)); im.alpha_composite(sch)
d=ImageDraw.Draw(im)
d.rounded_rectangle([WX0,WY0,WX1,WY1],radius=7*k,fill=(250,250,252))
d.rounded_rectangle([WX0,WY0,WX1,WY0+24*k],radius=7*k,fill=(232,234,240)); d.rectangle([WX0,WY0+16*k,WX1,WY0+24*k],fill=(232,234,240))
fs=ImageFont.truetype("/usr/share/fonts/truetype/inter/Inter-Regular.ttf" if os.path.exists("/usr/share/fonts/truetype/inter/Inter-Regular.ttf") else "DejaVuSans.ttf",11*k)
d.text((WX0+12*k,WY0+12*k),"Q4 budget.xlsx",font=fs,fill=(60,64,76),anchor="lm")
for i,c in enumerate([(236,106,94),(244,190,80),(110,196,120)]):
    cx=WX1-16*k-i*16*k; d.ellipse([cx-4*k,WY0+8*k,cx+4*k,WY0+16*k],fill=c)
# raster
gy=WY0+24*k; rh=16*k; cw=[28,80,60,60,60,60]
x=WX0
for j in range(int((WY1-gy)/rh)+1):
    y=gy+j*rh
    d.line([(WX0,y),(WX1,y)],fill=(220,222,230),width=1*k//1)
xs=[WX0]
for c in cw: xs.append(xs[-1]+c*k)
for xx in xs[1:]:
    if xx<WX1: d.line([(xx,gy),(xx,WY1)],fill=(220,222,230),width=1)
d.rectangle([WX0,gy,WX1,gy+rh],fill=(240,242,247))
hdr=["","Item","Oct","Nov","Dec","Total"]
for i,h in enumerate(hdr):
    if xs[i]+4*k<WX1: d.text((xs[i]+6*k,gy+rh//2),h,font=fs,fill=(110,114,128),anchor="lm")
random.seed(9)
items=["Rent","Coffee","Hosting","Snacks","Travel","Books"]
for j,it in enumerate(items):
    y=gy+(j+1)*rh+rh//2
    d.text((xs[0]+6*k,y),str(j+1),font=fs,fill=(150,154,168),anchor="lm")
    d.text((xs[1]+6*k,y),it,font=fs,fill=(50,54,66),anchor="lm")
    for i in range(2,6):
        if xs[i]+30*k<WX1: d.text((xs[i]+6*k,y),f"{random.randint(20,980)}",font=fs,fill=(50,54,66),anchor="lm")
# geselecteerde cel
d.rectangle([xs[3],gy+3*rh,xs[4],gy+4*rh],outline=(60,140,90),width=2*k)
# spelstrook
im.paste(strook,(0,SY))
d=ImageDraw.Draw(im)
# taakbalk
d.rectangle([0,H-TB,W,H],fill=(26,28,40)); d.line([(0,H-TB),(W,H-TB)],fill=(70,78,100),width=k)
knop=24*k; y0=H-TB+(TB-knop)//2
kl=[(77,148,240),(110,200,130),(240,196,72),(230,108,90)]
ik=30*k; n=len(kl); gap=12*k; x0=W//2-(n*knop+n*gap+ik)//2
for i,c in enumerate(kl):
    x=x0+i*(knop+gap); d.rounded_rectangle([x,y0,x+knop,y0+knop],radius=5*k,fill=c)
xi=x0+n*(knop+gap); yi=H-TB+(TB-ik)//2
gl=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(gl).rounded_rectangle([xi-5*k,H-TB+3*k,xi+ik+5*k,H-3*k],radius=7*k,fill=(120,190,255,80)); im.alpha_composite(gl)
ico=Image.open(R+"/ontwerp/steam/icoon/icoon-tegel-256.png").convert("RGBA").resize((ik,ik),Image.LANCZOS); im.alpha_composite(ico,(xi,yi))
d=ImageDraw.Draw(im)
d.rounded_rectangle([xi+7*k,H-4*k,xi+ik-7*k,H-2*k],radius=k,fill=(140,210,255))
fk=ImageFont.truetype(R+"/ontwerp/steam/capsule-3d/LilitaOne-Regular.ttf",14*k)
d.text((W-16*k,H-TB//2),"16:40",font=fk,fill=(230,236,248),anchor="rm")
# muispijl bij Gloop
mx,my,ms=float(os.environ.get("MX","700"))*k,float(os.environ.get("MY","300"))*k,1.2*k
pijl=[(0,0),(0,17),(4,13),(7,20),(10,19),(7,12),(12,12)]
pts=[(mx+x*ms,my+y*ms) for x,y in pijl]
s2=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(s2).polygon([(x+2*k,y+2*k) for x,y in pts],fill=(0,0,0,100)); im.alpha_composite(s2.filter(ImageFilter.GaussianBlur(1.5*k)))
d=ImageDraw.Draw(im); d.polygon(pts,fill=(255,255,255),outline=(20,20,28),width=int(1.4*k))
# logo
L=logo(os.environ.get("FONT",os.path.join(os.path.dirname(os.path.abspath(__file__)),"letters","Jersey10-Regular.ttf")),int(os.environ.get("LS","118")),k=k,txt2=os.environ.get("T2","of the Fallen"))
im.alpha_composite(L,(int(float(os.environ.get("LX","6"))*k),int(float(os.environ.get("LY","0"))*k)))
im=im.convert("RGB")
out=sys.argv[1]
im.resize((920,430),Image.LANCZOS).save(out); im.resize((460,215),Image.LANCZOS).save(out.replace(".png","-460.png")); im.save(out.replace(".png","-2x.png"))
print("klaar")
