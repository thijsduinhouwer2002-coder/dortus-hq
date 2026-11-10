# Abel: achtergrond zonder grote D; het licht valt uit de D van het logo (zie merk/voor-mila.md).
import os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'maak_uniform.py')).read().split('if __name__')[0]
src=src.replace('os.path.dirname(os.path.abspath(__file__)) + "/.."', repr(os.path.dirname(os.path.abspath(__file__))))
exec(src)
W,H=1920,1200
# logo 1200x460 staat gecentreerd bovenaan: D van het logo op x 441..691, y 106..386 (s=0.5)
dx,dy,s=441,106,0.5
inhoud=(f'<rect width="{W}" height="{H}" fill="{NACHT}"/>'
 f'<rect y="{dy+560*s:.0f}" width="{W}" height="{H-dy-560*s:.0f}" fill="url(#vloerdonker)"/>'
 f'<circle cx="960" cy="250" r="700" fill="url(#gloed)" opacity="0.45"/>'
 f'<circle cx="{dx+300*s:.0f}" cy="{dy+300*s:.0f}" r="460" fill="url(#gloed)" opacity="0.9"/>'
 + straal(dx,dy,s,H,760) + sterren(W,H*0.8,int(W*H/9000))
 + kroon(190,800,110) + dobbel(260,1010,88) + haakjes(1745,700,96))
schrijf('steam-achtergrond-1920-v1b',W,H,inhoud)
