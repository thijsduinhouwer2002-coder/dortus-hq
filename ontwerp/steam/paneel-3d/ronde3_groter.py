from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
F='/home/claude/dortus-hq/ontwerp/steam/paneel-3d/Fredoka.ttf'
im=Image.open('strook-160.png').convert('RGB')
orig=im.copy()
a=np.array(im)
# knop en munt bewaren
knop=orig.crop((708,668,788,692))
munt=orig.crop((966,630,989,654))
x0,x1,y0,y1=699,1012,621,708
for y in range(y0,y1):
    a[y,x0:x1]=a[y,950]
im=Image.fromarray(a)
def font(sz,w):
    f=ImageFont.truetype(F,sz)
    try: f.set_variation_by_axes([w])
    except Exception as e: print(e)
    return f
d=ImageDraw.Draw(im)
T=font(18,600); B=font(15,450)
gold=(255,214,102); wit=(236,226,214)
# schaduw titel
lay=Image.new('RGBA',im.size,(0,0,0,0)); dl=ImageDraw.Draw(lay)
dl.text((713,628),'Big Gloop',font=T,fill=(20,8,20,170))
dl.text((990,628),'27',font=T,fill=(20,8,20,170))
im.paste(lay,(0,0),lay)
d=ImageDraw.Draw(im)
d.text((712,627),'Big Gloop',font=T,fill=gold)
d.text((989,627),'27',font=T,fill=wit)
mz=munt.resize((28,28),Image.LANCZOS); im.paste(mz,(958,624))
d.text((712,651),'Bought.',font=B,fill=wit)
kz=knop.resize((104,31),Image.LANCZOS); im.paste(kz,(707,673))
im.crop((688,605,1024,722)).resize((336*3,117*3),Image.LANCZOS).save('mock-3x.png')
# voor/na ware grootte
v=orig.crop((560,590,1024,722)); n=im.crop((560,590,1024,722))
out=Image.new('RGB',(464,132*2+6),(255,255,255)); out.paste(v,(0,0)); out.paste(n,(0,138)); out.resize((928,540),Image.NEAREST).save('voor-na-160-2x.png')
