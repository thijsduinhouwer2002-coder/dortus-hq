from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
W,H=1440,720
bg=Image.new('RGB',(W,H))
d=ImageDraw.Draw(bg)
top=(14,74,122); bot=(5,30,58)
for y in range(H):
    t=y/H; d.line([(0,y),(W,y)],fill=tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3)))
# light rays
rays=Image.new('L',(W,H),0); rd=ImageDraw.Draw(rays)
for x0,w in [(820,90),(980,60),(1180,110)]:
    rd.polygon([(x0,0),(x0+w,0),(x0+w+160,H),(x0+160-40,H)],fill=28)
rays=rays.filter(ImageFilter.GaussianBlur(30))
bg.paste(Image.new('RGB',(W,H),(120,190,230)),(0,0),rays)
# bubbles
for (x,y,r) in [(760,560,7),(735,500,4),(1390,180,6),(1360,120,3),(700,260,3)]:
    d.ellipse([x-r,y-r,x+r,y+r],outline=(150,210,240),width=2)
# sand
d.ellipse([-200,640,1700,1000],fill=(232,214,160))
# watch
w=Image.open(sys.argv[1]).convert('RGBA')
px=w.load()
from collections import deque
q=deque([(0,0),(599,0),(0,599),(599,599)]); seen=set()
while q:
    x,y=q.popleft()
    if (x,y) in seen or not(0<=x<600 and 0<=y<600): continue
    seen.add((x,y)); r,g,b,a=px[x,y]
    if r>235 and g>235 and b>235:
        px[x,y]=(0,0,0,0); q.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
w=w.resize((640,640),Image.LANCZOS)
sh=Image.new('RGBA',(W,H),(0,0,0,0)); sh.paste((0,0,0,110),(850,60),w.split()[3])
sh=sh.filter(ImageFilter.GaussianBlur(18))
bg=bg.convert('RGBA'); bg.alpha_composite(sh); bg.alpha_composite(w,(830,40))
d=ImageDraw.Draw(bg)
F='/usr/share/fonts/truetype/inter/'
import glob
def font(name,size):
    c=glob.glob(f'/usr/share/fonts/**/{name}',recursive=True); return ImageFont.truetype(c[0],size)
d.text((96,190),sys.argv[3],font=font('InterDisplay-Bold.otf',150),fill=(255,255,255))
d.text((100,370),sys.argv[4],font=font('InterDisplay-SemiBold.otf',56),fill=(255,214,102))
d.text((100,452),sys.argv[5],font=font('Inter-Regular.otf',34),fill=(200,225,245))
bg.convert('RGB').save(sys.argv[2],quality=90)
