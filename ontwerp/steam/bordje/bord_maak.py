from PIL import Image, ImageDraw
import sys
base=Image.open(sys.argv[1]).convert('RGB')
D={'1':["010","110","010","010","111"],'2':["111","001","111","100","111"],'5':["111","100","111","001","111"],'0':["111","101","101","101","111"],'2b':[]}
# 4x6 vette cijfers
F={'5':["1111","1000","1110","0001","1001","0110"],'1':["0110","1110","0110","0110","0110","1111"],'2':["0110","1001","0010","0100","1000","1111"]}
GOUD=(255,224,122); GOUDD=(196,140,40); HOUT=(122,74,40); HOUTL=(160,102,56); HOUTD=(70,40,22); RAND=(40,22,12); BALKLEEG=(58,34,20)
def cijfer(d,x,y,s,kleur,schaduw):
    for r,row in enumerate(F[s]):
        for c,v in enumerate(row):
            if v=='1':
                d.point((x+c,y+r+1),fill=schaduw); d.point((x+c,y+r),fill=kleur)
def bord_a(niv,deel):
    # plank op paaltje, 13x9 spelpixels plus paal
    w,h=13,11; im=Image.new('RGBA',(w,h+4),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rectangle((5,h-1,7,h+3),fill=HOUTD); d.rectangle((6,h-1,6,h+3),fill=HOUT)
    d.rectangle((0,0,w-1,h-1),fill=RAND); d.rectangle((1,1,w-2,h-2),fill=HOUT); d.line((1,1,w-2,1),fill=HOUTL)
    s=str(niv); x=(w-len(s)*5+1)//2
    for k,ch in enumerate(s): cijfer(d,x+k*5,2,ch,GOUD,HOUTD)
    d.line((2,h-2,w-3,h-2),fill=BALKLEEG); n=round((w-4)*deel)
    if n: d.line((2,h-2,2+n-1,h-2),fill=GOUD)
    return im
def bord_b(niv,deel):
    # schildje op de sluitsteen van de boog, 9x10
    w,h=9,10; im=Image.new('RGBA',(w,h+2),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.polygon([(0,0),(w-1,0),(w-1,h-4),(w//2,h-1),(0,h-4)],fill=RAND)
    d.polygon([(1,1),(w-2,1),(w-2,h-4),(w//2,h-2),(1,h-4)],fill=(150,40,40))
    d.line((1,1,w-2,1),fill=(200,80,70))
    cijfer(d,(w-4)//2,2,str(niv)[-1],GOUD,(90,20,20))
    d.line((0,h+1,w-1,h+1),fill=BALKLEEG); n=round(w*deel)
    if n: d.line((0,h+1,n-1,h+1),fill=GOUD)
    return im
def plak(img,bord,gx,gy):
    b=bord.resize((bord.width*3,bord.height*3),Image.NEAREST); img.paste(b,(gx*3,gy*3),b)
out=[]
for naam,f,pos in (('A plank naast de ingang',bord_a,(4,0)),('B schildje op de boog',bord_b,(20,-1))):
    im=base.copy()
    for niv,deel in ((5,0.4),):
        plak(im,f(niv,deel),*pos)
    out.append(im)
# wide plank variant with two digits
im=base.copy(); plak(im,bord_a(12,1.0),4,0); out.append(im)
W=1024; crop=lambda i:i.crop((0,0,340,120))
sheet=Image.new('RGB',(340*3*3+40, 120*3+0),(60,60,60))
for k,i in enumerate(out): sheet.paste(crop(i).resize((1020,360),Image.NEAREST),(k*(1020+20),0))
sheet.save('bord-voorstel-3x.png')
ware=Image.new('RGB',(1024,120*3+20),(60,60,60))
for k,i in enumerate(out): ware.paste(i,(0,k*130))
ware.save('bord-voorstel-1x.png')
