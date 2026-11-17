import sys, numpy as np
from PIL import Image
S='/tmp/claude-0/s/'
strook=Image.open(S+'strook.png').convert('RGBA')
blad=Image.open('/home/claude/dortus-hq/producten/steam-hol/godot/kunst/3d/hoeden.png').convert('RGBA')
CW,CH=63,49
def hoed(i,kantel=0):
    f=blad.crop((i*CW,0,i*CW+CW,CH))
    f=f.resize((round(CW*0.6),round(CH*0.6)),Image.LANCZOS)
    if kantel: f=f.rotate(kantel,resample=Image.BICUBIC,expand=True)
    a=np.asarray(f)[...,3]; ys=np.where(a.max(1)>40)[0]; xs=np.where(a.max(0)>40)[0]
    return f, ys[0], ys[-1], (xs[0]+xs[-1])/2
def toren(rij, plafond=True):
    im=strook.copy()
    # wis de oude toren boven Gloop met de wand links ernaast (zelfde rijen)
    patch=im.crop((1252,924,1296,990)); im.paste(patch,(1300,924))
    # Gloop terug (zijn kruin) uit het origineel
    g=strook.crop((1290,984,1352,1000)); im.paste(g,(1290,984))
    top=992; cx=1320
    for i,k in rij:
        f,y0,y1,mx=hoed(i,k)
        im.alpha_composite(f,(int(round(cx-mx)),int(top-y1-1+3)))
        top=top-(y1-y0+1)+3
    return im
voor=toren([(4,-3),(7,4),(5,-2)])
na=toren([(4,-3),(7,4),(10,5)])
for n,im in (('voor',voor),('na',na)):
    im.crop((0,880,1920,1080)).convert('RGB').save(S+f'toren-{n}-1x.png')
blad2=Image.new('RGB',(2*480+30,490),(30,30,30))
for k,im in enumerate((voor,na)):
    blad2.paste(im.crop((1250,915,1390,1040)).resize((420,375),Image.NEAREST).convert('RGB'),(40+k*490,10))
    blad2.paste(im.crop((1180,915,1460,1040)).convert('RGB'),(10+k*490+100,355))
blad2.save(S+'toren-voor-na.png')
