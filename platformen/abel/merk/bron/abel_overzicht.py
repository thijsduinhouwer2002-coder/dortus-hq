# Abel: een overzichtsblad met alle proeven onder elkaar, voor Thijs om 08:00.
# Draai vanuit platformen/abel/merk/:  python3 bron/abel_overzicht.py
from PIL import Image, ImageDraw, ImageFont
W=1400; PAD=40; NACHT=(29,20,38); LILA=(167,139,250); ROOM=(255,244,224)
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f_t=ImageFont.truetype(FB,44); f_h=ImageFont.truetype(FB,28); f_s=ImageFont.truetype(F,20)
rijen=[
 ('1. Steam: ontwikkelaarspagina','proef/steam-pagina-definitief-1920.png',(0,0,1920,1100),'Kop, logo, achtergrond en paginakleur Nacht. De spellen zijn van de mal (Klei).'),
 ('1. Steam: profiel dortusgames','proef/steam-profiel-kort-op-steam.png',None,'Avatar en korte profieltekst; de kleur komt van het profiel dat als mal diende.'),
 ('2. Polar: afrekenpagina','proef/polar-afrekenen-uitsnede.png',None,'Nu staat hier een grijze letter D.'),
 ('3. GitHub: repo Rollwright','proef/github-repo-light.png',None,'Profielfoto, en het vak About gevuld (beschrijving, website, topics: stap 2).'),
 ('4. Blender Extensions','proef/blender-avatar-uitsnede.png',None,'Nu een leeg poppetje.'),
 ('5. Obsidian-forum','proef/obsidian-draad-dark.png',None,'Nu een letter "t".'),
 ('6. dortus.com: nieuwe hoofdpagina (wacht op ja van Thijs)','../dortus-com/voorbeeld-desktop.png',(0,0,1280,1010),'Nu opent dortus.com nog met Confluence. Oude pagina\'s blijven staan, met een link onderaan.'),
]
blokken=[]
for kop,f,crop,uitleg in rijen:
    im=Image.open(f).convert('RGB')
    if crop: im=im.crop(crop)
    b=W-2*PAD; im=im.resize((b,round(im.height*b/im.width)),Image.LANCZOS)
    blokken.append((kop,im,uitleg))
H=PAD+70+30+sum(40+30+im.height+50 for _,im,_ in blokken)+PAD
o=Image.new('RGB',(W,H),NACHT); d=ImageDraw.Draw(o); y=PAD
d.text((PAD,y),'Dortus: zo ziet elk account er straks uit',font=f_t,fill=ROOM); y+=70
d.text((PAD,y),'Proeven op de echte pagina\'s, alleen in onze browser vervangen. Alles goedgekeurd door Daan (keuring 1 tot 5).',font=f_s,fill=LILA); y+=50
for kop,im,uitleg in blokken:
    d.text((PAD,y),kop,font=f_h,fill=ROOM); y+=40
    d.text((PAD,y),uitleg,font=f_s,fill=LILA); y+=34
    o.paste(im,(PAD,y)); d.rectangle([PAD-1,y-1,PAD+im.width,y+im.height],outline=(70,55,95)); y+=im.height+50
o.save('proef/overzicht-alle-accounts.png',optimize=True); print(o.size)
