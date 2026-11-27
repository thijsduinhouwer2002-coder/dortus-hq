# Logo van Hats in Jersey 10 (SIL OFL, letters/), Mila 27 nov 2026, issue #30. Geen AI.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
def logo(font, size, txt1="Hats", txt2="of the Fallen", fill=(255,226,140), rand=(44,22,30), k=2, size2=None, var=None):
    f=ImageFont.truetype(font, size*k); f2=ImageFont.truetype(font, (size2 or int(size*0.42))*k)
    if var:
        try: f.set_variation_by_axes([var]); f2.set_variation_by_axes([var])
        except Exception as e: pass
    W,H=900*k,260*k
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    sw=int(size*0.07*k)
    # schaduw
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    ds.text((20*k+5*k,10*k+7*k),txt1,font=f,fill=(20,10,20,150),stroke_width=sw,stroke_fill=(20,10,20,150))
    im.alpha_composite(sh)
    d.text((20*k,10*k),txt1,font=f,fill=fill,stroke_width=sw,stroke_fill=rand)
    bb=d.textbbox((20*k,10*k),txt1,font=f)
    d.text((24*k,bb[3]+6*k),txt2,font=f2,fill=(255,246,226),stroke_width=int(sw*0.6),stroke_fill=rand)
    return im
