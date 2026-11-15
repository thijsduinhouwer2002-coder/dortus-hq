import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGBA'); px = im.load()
ref = (0x5e, 0x3e, 0x33); doel = (0x4a, 0x31, 0x29)
rat = [d / r for d, r in zip(doel, ref)]
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]
        d = ((r-ref[0])**2 + (g-ref[1])**2 + (b-ref[2])**2) ** 0.5
        w = max(0.0, min(1.0, 1 - (d - 25) / 45))   # bruin binnenvlak helemaal, overgang naar goud zacht
        n = [round(c * (1 - w) + c * k * w) for c, k in zip((r, g, b), rat)]
        px[x, y] = (*n, a)
im.save(dst)
