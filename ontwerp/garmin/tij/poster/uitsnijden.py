from PIL import Image, ImageDraw
import sys
src,dst=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB')
w,h=im.size
im=im.crop((2,30,w-2,h-34))
w,h=im.size
mask=Image.new('L',(w,h),0)
# flood fill on a copy marking background
c=im.copy()
for p in [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0),(w//2,h-1),(0,h//2),(w-1,h//2)]:
    ImageDraw.floodfill(c,p,(255,0,255),thresh=40)
px=c.load();a=Image.new('L',(w,h),255);ap=a.load()
for y in range(h):
    for x in range(w):
        if px[x,y]==(255,0,255): ap[x,y]=0
from PIL import ImageFilter
a=a.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
im.putalpha(a); im=im.crop(im.getbbox()); im.save(dst); print(dst,im.size)
