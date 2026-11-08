# Daan run 18: GIF versie 3, aan het eind inzoomen op de NAT 20 en overvloeien naar de scherpe opname (crit.png, zoom 3).
import sys
from PIL import Image, ImageFilter
src, crit_p, out = sys.argv[1], sys.argv[2], sys.argv[3]
g = Image.open(src)
frames, durs = [], []
for i in range(g.n_frames):
    g.seek(i); frames.append(g.convert("RGB")); durs.append(g.info.get("duration", 80))
last = frames[-1]; W, H = last.size
S, OX, OY = 2.65, 120, 256
crit = Image.open(crit_p).convert("RGB")
mask = Image.new("L", crit.size, 0); mask.paste(255, (14, 14, crit.size[0]-14, crit.size[1]-14)); mask = mask.filter(ImageFilter.GaussianBlur(8))
def zoomed(t):
    # crop van het hele beeld (t=0) naar het doelvak (t=1), lineair in de randen
    x0 = 0 + (OX-0)*t; y0 = 0 + (OY-0)*t
    x1 = W + (OX+W/S - W)*t; y1 = H + (OY+H/S - H)*t
    return last.crop((round(x0), round(y0), round(x1), round(y1))).resize((W, H), Image.LANCZOS)
eind = zoomed(1.0).copy(); eind.paste(crit, (round((W-crit.size[0])/2), round((H-crit.size[1])/2)), mask)
durs[-1] = 700  # eerst even rust op de NAT 20, dan inzoomen
n = 12
for k in range(1, n+1):
    t = k/n; t = 1-(1-t)**3
    frames.append(zoomed(t)); durs.append(55)
for k in range(1, 5):
    frames.append(Image.blend(zoomed(1.0), eind, k/4)); durs.append(60)
frames.append(eind); durs.append(2600)
pal = frames
pal[0].save(out, save_all=True, append_images=pal[1:], duration=durs, loop=0, optimize=True, disposal=1)
print(len(frames), sum(durs)/1000, "s")
