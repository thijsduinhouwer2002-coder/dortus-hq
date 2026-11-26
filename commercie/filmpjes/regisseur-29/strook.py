#!/usr/bin/env python3
"""Naast-elkaar-strook (issue #159): 1 beeld per seconde van het voorbeeld (boven) en van onze film (onder).
Beelden van anderen horen niet in de openbare repo: haal het voorbeeld zelf op met curl (playAddr uit de JSON van de
TikTok-pagina) en maak de strook lokaal. Zonder voorbeeld maakt hij alleen onze rij.
    python3 strook.py <onze.mp4> <uit.jpg> [voorbeeld.mp4]"""
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

HB = 300   # hoogte per beeldje


def rij(pad, n):
    uit = []
    for s in range(n):
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{s + 0.5:.2f}", "-i", pad, "-frames:v", "1", "-vf",
                            f"scale=-2:{HB}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
        if not r.stdout:
            break
        from io import BytesIO
        uit.append(Image.open(BytesIO(r.stdout)).convert("RGB"))
    return uit


def duur(pad):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", pad],
                                capture_output=True, text=True).stdout)


def main():
    ons, uit = sys.argv[1], sys.argv[2]
    vb = sys.argv[3] if len(sys.argv) > 3 else None
    n = int(max(duur(ons), duur(vb) if vb else 0))
    rijen = ([("voorbeeld", rij(vb, n))] if vb else []) + [("v7", rij(ons, n))]
    bw = 170
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22) if True else None
    kolommen = 14
    blokken = (n + kolommen - 1) // kolommen
    im = Image.new("RGB", (kolommen * bw + 10, blokken * (len(rijen) * (HB + 6) + 34) + 10), (24, 24, 28))
    d = ImageDraw.Draw(im)
    for bl in range(blokken):
        y0 = 10 + bl * (len(rijen) * (HB + 6) + 34)
        for k in range(kolommen):
            s = bl * kolommen + k
            if s >= n:
                break
            d.text((10 + k * bw + 4, y0), f"{s} s", font=f, fill=(230, 230, 230))
            for r_i, (_naam, beelden) in enumerate(rijen):
                if s < len(beelden):
                    b = beelden[s]
                    b = b.resize((bw - 6, int(b.height * (bw - 6) / b.width)))
                    im.paste(b, (10 + k * bw, y0 + 28 + r_i * (HB + 6)))
    im.save(uit, quality=85)
    print(f"strook: {uit}, {n} s, rijen: {', '.join(r[0] for r in rijen)}")


if __name__ == "__main__":
    main()
