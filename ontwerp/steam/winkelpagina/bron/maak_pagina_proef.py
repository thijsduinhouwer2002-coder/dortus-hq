import sys
from PIL import Image, ImageDraw, ImageFont
R=sys.argv[1]; uit=sys.argv[2]
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f=lambda s,b=False: ImageFont.truetype(FB if b else F,s)
W,H=1280,1000
im=Image.new('RGB',(W,H),(27,40,56)); d=ImageDraw.Draw(im)
x0=(W-940)//2
d.text((x0,22),'All Software > Simulation > Hats of the Fallen',font=f(12),fill=(143,152,160))
d.text((x0,42),'Hats of the Fallen',font=f(26),fill=(255,255,255))
# media links 600x338
sch=R+'/ontwerp/steam/winkelpagina/schermen-3d/'
big=Image.open(sch+'voorstel-scherm-1-bureaublad-kleurh-daan.png').convert('RGB').resize((600,338),Image.LANCZOS)
im.paste(big,(x0,90))
thumbs=['scherm-5-royal-daan.png','scherm-1-hoedentoren.png','scherm-3-wrok.png','scherm-4-kaartje.png','scherm-2-bureaublad.png']
for k,t in enumerate(thumbs):
    th=Image.open(sch+t).convert('RGB').resize((116,65),Image.LANCZOS); im.paste(th,(x0+k*121,90+338+8))
d.text((x0,520),'Thumbnails 2 to 5 are still the old purple versions.',font=f(11),fill=(200,120,120))
# rechts header 324x151
hx=x0+616
hd=Image.open(R+'/ontwerp/steam/capsule-3d/header-920x430.png').convert('RGB').resize((324,151),Image.LANCZOS)
im.paste(hd,(hx,90))
txt="A tiny dungeon lives on top of your taskbar. Heroes climb in, fall into your traps and get eaten by Gloop, who wears their hats. The ones who flee come back with scars, nicknames and a grudge."
import textwrap
y=250
for line in textwrap.wrap(txt,48):
    d.text((hx,y),line,font=f(12),fill=(214,215,216)); y+=17
y+=10
for a,b in [('RECENT REVIEWS:','No user reviews'),('RELEASE DATE:','Coming soon'),('DEVELOPER:','Dortus')]:
    d.text((hx,y),a,font=f(10),fill=(85,103,114)); d.text((hx+110,y),b,font=f(10),fill=(103,193,245)); y+=18
# zoekresultaat / aanbevolen: hoofdbeeld 616x353 onder
d.text((x0,560),'Featured (main capsule) and search row (small capsule):',font=f(13,True),fill=(255,255,255))
hb=Image.open(R+'/ontwerp/steam/capsule-3d/hoofdbeeld-1232x706.png').convert('RGB').resize((560,321),Image.LANCZOS)
im.paste(hb,(x0,590))
kl=Image.open(R+'/ontwerp/steam/capsule-3d/klein-462x174.png').convert('RGB').resize((184,69),Image.LANCZOS)
d.rectangle((x0+576,590,x0+940,659),fill=(22,32,45)); im.paste(kl,(x0+576,590))
d.text((x0+768,600),'Hats of the Fallen',font=f(12),fill=(199,213,224)); d.text((x0+768,620),'Coming soon',font=f(10),fill=(143,152,160))
bi=Image.open(R+'/ontwerp/steam/capsule-3d/bibliotheek-600x900.png').convert('RGB').resize((200,300),Image.LANCZOS)
im.paste(bi,(x0+576,680))
d.text((x0+786,690),'Library',font=f(12),fill=(199,213,224))
im.save(uit)
