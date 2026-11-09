# Maakt van de Movie Maker-beelden (f00000000.png ...) een GIF op 5 fps, en bewaart drie losse beelden. Olaf, 9 nov 2026.
import sys, glob, os
from PIL import Image
bron, uit = sys.argv[1], sys.argv[2]
beelden = sorted(glob.glob(os.path.join(bron, "f*.png")))
print("beelden:", len(beelden))
if not beelden:
    sys.exit(0)
gekozen = beelden[::3]
frames = []
for p in gekozen:
    im = Image.open(p).convert("RGBA")
    achter = Image.new("RGBA", im.size, (40, 60, 90, 255))  # waar de strook doorzichtig is: blauw bureaublad
    achter.alpha_composite(im)
    frames.append(achter.convert("RGB").quantize(colors=128, dither=Image.Dither.NONE))
frames[0].save(uit, save_all=True, append_images=frames[1:], duration=200, loop=0, optimize=True)
for i in (len(beelden) // 6, len(beelden) // 2, len(beelden) - 1):
    Image.open(beelden[i]).save(os.path.join(bron, "los-%03d.png" % (i // 15)))
print("gif:", uit, os.path.getsize(uit), "bytes,", len(frames), "beelden")
