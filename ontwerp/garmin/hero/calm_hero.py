from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1440,720
bg=Image.new('RGB',(W,H)); d=ImageDraw.Draw(bg)
top=(14,74,122); bot=(5,30,58)
for y in range(H):
    t=y/H; d.line([(0,y),(W,y)],fill=tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3)))
for (x,y,r) in [(760,560,7),(735,500,4),(1400,160,6),(700,260,3)]:
    d.ellipse([x-r,y-r,x+r,y+r],outline=(150,210,240),width=2)
d.ellipse([-200,640,1700,1000],fill=(232,214,160))
src=Image.open('/home/claude/dortus-hq/ontwerp/garmin/winkel-calm/1-breathe-in.png').convert('RGBA')
w=src.crop((88,178,712,802)).resize((620,620),Image.LANCZOS)
m=Image.new('L',(620,620),0); ImageDraw.Draw(m).ellipse([2,2,617,617],fill=255)
sh=Image.new('RGBA',(W,H),(0,0,0,0)); sh.paste((0,0,0,120),(870,70),m); sh=sh.filter(ImageFilter.GaussianBlur(18))
bg=bg.convert('RGBA'); bg.alpha_composite(sh); bg.paste(w,(850,50),m)
d=ImageDraw.Draw(bg)
F=lambda n,s: ImageFont.truetype('/usr/share/fonts/opentype/inter/'+n,s)
d.text((96,190),'Ebb Calm',font=F('InterDisplay-Bold.otf',140),fill=(255,255,255))
d.text((100,360),'Free 4-7-8 breathing.',font=F('InterDisplay-SemiBold.otf',56),fill=(255,214,102))
d.text((100,442),'Follow the sea, or the vibration.',font=F('Inter-Regular.otf',34),fill=(200,225,245))
bg.convert('RGB').save('calm-hero.jpg',quality=90)
