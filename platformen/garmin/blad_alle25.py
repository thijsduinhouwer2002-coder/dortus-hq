# Blad run 74: alle 25 dieren uit de echte schermbeelden (proef74a tot e), per horloge en per dag of nacht. Per dier links inademen, rechts inhouden.
import sys
from PIL import Image, ImageDraw, ImageFont
S, h, dn, uit = sys.argv[1:5]
NAMEN=["Fish","Shrimp","Jellyfish","Turtle","Crab","Seahorse","Starfish","Clownfish","Pufferfish","Octopus","Eel","Ray","Seal","Dolphin","Swordfish","Sea otter","Manta","Shark","Sunfish","Orca","Narwhal","Giant squid","Lobster","Whale","Sea cucumber"]
RIJ={'a':[0,1,2,None,None,3,4,5],'b':[6,7,8,None,None,9,10,11],'c':[12,13,14,None,None,15,16,17],'d':[18,19,20,None,None,21,22,23],'e':[None]*5+[24,None,None]}
PLEK=['krab','schild','basis','eerste','terugval','komkommer','kreeft','otter']
VAK={'fr255':(85,195,345,460),'fenix847mm':(130,235,595,735)}[h]; T=190
waar={d:(r,PLEK[i]) for r in RIJ for i,d in enumerate(RIJ[r]) if d is not None}
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15)
b=Image.new('RGB',(5*(2*T+12)+8,5*(T+30)+40),(38,40,48)); dr=ImageDraw.Draw(b)
dr.text((8,8),'Ebb run 74, alle 25 dieren, %s, %s. Per dier: links inademen, rechts inhouden. Echte schermbeelden.'%(h,dn),fill=(255,255,255),font=f)
for d in range(25):
    r,p=waar[d]; x=8+(d%5)*(2*T+12); y=36+(d//5)*(T+30)
    dr.text((x,y),'%d %s'%(d,NAMEN[d]),fill=(255,230,120),font=f)
    for j,fa in enumerate(('in','hold')):
        b.paste(Image.open('%s/%s__sessie-%s-%s-%s-%s.png'%(S,r,p,fa,dn,h)).convert('RGB').crop(VAK).resize((T,T),Image.LANCZOS),(x+j*T,y+20))
b.save(uit); print(uit,b.size)
