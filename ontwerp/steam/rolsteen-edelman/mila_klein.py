import sys
from PIL import Image
src, uit, f = sys.argv[1], sys.argv[2], float(sys.argv[3])
im = Image.open(src)
w, h = im.size
k = im.resize((round(w*f), round(h*f)), Image.LANCZOS)
bg = Image.new('RGBA', k.size, (92, 52, 70, 255)); bg.alpha_composite(k)
b = bg.convert('RGB'); b4 = b.resize((b.width*4, b.height*4), Image.NEAREST)
out = Image.new('RGB', (b4.width, b4.height + b.height + 8), (20,20,20)); out.paste(b4,(0,0)); out.paste(b,(0,b4.height+8)); out.save(uit)
