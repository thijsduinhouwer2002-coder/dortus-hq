import sys; sys.path.insert(0,'.')
from kleur import *
T={
'Dusk':dict(b=['AA5555','AA0055','550055','000055'],line='FFAAAA',sail='FFFFFF',mn='FFAA55',txt='FFFFAA',punt='AA5555',outl='000000'),
'Tide':dict(b=['55AAAA','0055AA','0000AA','000055'],line='AAFFFF',sail='FFFFFF',mn='55FFFF',txt='AAFFFF',punt='5555AA',outl='000000'),
'Kelp':dict(b=['AAAA55','55AA55','005555','000055'],line='FFFFAA',sail='FFFFFF',mn='AAFFAA',txt='FFFFAA',punt='55AA55',outl='000000'),
'Night':dict(b=['5555AA','5500AA','0000AA','000055'],line='AAAAFF',sail='FFFFFF',mn='AAAAFF',txt='FFFFFF',punt='5555AA',outl='000000'),
}
ACHT=dict(b=['00FFFF','00FFFF','0000FF','0000FF'],line='00FFFF',sail='FFFFFF',mn='00FFFF',txt='FFFFFF',punt='00FFFF',outl='000000')
try: F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18); f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
except: F=f=ImageFont.load_default()
def tile(dev,N): 
    im=crop(dev,recolor(dev,N)); return im.resize((300,int(300*im.height/im.width)))
rows=[('Forerunner 255 (64 kleuren)','fr255'),('Forerunner 245 (64 kleuren)','fr245')]
TW=300; TH=tile('fr255',T['Dusk']).height; TH2=tile('fr245',T['Dusk']).height
lab=40; W=lab+TW*5+40; H=60+(TH+30)+(TH2+30)+150
s=Image.new('RGB',(W,H),'#f4f1ea'); d=ImageDraw.Draw(s)
d.text((lab,15),'Tij op 64 en 8 kleuren: voorstel Mila 17 nov (kleuren vervangen in de echte opnames van run 44015762562)',fill='black',font=F)
y=60
for (naam,dev),th in zip(rows,[TH,TH2]):
    d.text((lab,y+5),naam,fill='black',font=F)
    for i,(k,N) in enumerate(T.items()):
        s.paste(tile(dev,N),(lab+i*TW,y+30)); d.text((lab+i*TW+120,y+30+th-28),k,fill='white',font=F)
    y+=th+30
# 8 kleuren column
x8=lab+4*TW+40
d.text((x8,60+5),'Forerunner 55 (8 kleuren)',fill='black',font=F)
t8=tile('fr55',ACHT); s.paste(t8,(x8,60+30)); d.text((x8+60,60+30+t8.height-28),'alle thema\'s gelijk',fill='white',font=F)
# legend
y+=10
def chips(x,y,naam,N):
    d.text((x,y),naam,fill='black',font=F)
    for j,c in enumerate(N['b']+[N['line'],N['sail'],N['mn']]):
        d.rectangle([x+j*38,y+24,x+j*38+34,y+58],fill='#'+c,outline='#888')
        d.text((x+j*38,y+60),c,fill='black',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',9) if f!=F else f)
for i,(k,N) in enumerate(T.items()): chips(lab+i*TW,y,k,N)
chips(x8,y,'8 kleuren',ACHT)
d.text((lab,y+85),'Per thema: band 0 t/m 3 (boven naar onder), waterlijn, zeil, minuten. Elk kanaal 00, 55, AA of FF. Getalrand op 64 en 8 kleuren: zwart.',fill='black',font=f)
s.save('mila-tij-kleuren-64-8.png'); print(s.size)
