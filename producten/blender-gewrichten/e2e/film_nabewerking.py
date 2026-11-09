"""Nabewerking productfilm Click Joints, zonder nieuwe render (bouwt voort op film_label.py).

Gebruik: python3 film_nabewerking.py <bron.mp4> <uit.mp4> [map voor keurbeelden]
Bron is click-joints-filmisch.mp4 (render zonder label, met eindkaart).
Beeldnummers zijn 0-based (n zoals ffmpeg ze telt), gelijk aan de nummers van Daan.

Wat het doet:
1. Rand van het achtergrondvlak links (held-shot en slot met twee gewrichten):
   per beeld meten hoe breed het donkere vlak is en de linkerstrook tot net voorbij
   die rand vervangen door de lege achtergrond (uit beeld REF, waar die strook schoon is),
   met een zacht verloop. Stopt als de pop in de buurt van de vervanging komt.
2. Blender-stempel linksboven weg, Inter-label "Exploded view" erop (zoals film_label.py).
3. Spookbeeld van B: beeld 230 tot 235 overvloeien naar beeld 236 (zes beelden).
4. Beeld HOUD een halve seconde vasthouden, zodat het label langer te lezen is.
"""
import subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 30
REF = 119                      # schone linkerstrook, geen pop links van x=600
BEREIKEN = [(55, 125), (405, 475)]   # ruim om de klachten van Daan heen
MARGE, VERLOOP = 24, 48        # px voorbij de gemeten rand, daarna zacht verloop
LABEL = (236, 260)             # label in en uit
STEMPEL = (0, 0, 380, 80)      # Blender-stempel linksboven
GEEST = (230, 236)             # overvloeien van 230 naar 236
HOUD, HOUD_N = 250, 15         # 0,5 s vasthouden
FONT = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"


def lees_beeld(pad, n):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", pad, "-vf", f"select=eq(n\\,{n})",
                          "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(out, np.uint8).reshape(H, W, 3).astype(np.float32)


def luma_blur(a, breed=900):
    im = Image.fromarray(a[:, :breed].astype(np.uint8)).convert("L").filter(ImageFilter.BoxBlur(3))
    return np.asarray(im).astype(np.float32)


def zacht_masker(rand, verloop):
    """1 links van rand, smoothstep naar 0 over verloop px."""
    x = np.arange(W, dtype=np.float32)
    t = np.clip((x - rand) / verloop, 0, 1)
    return (1 - t * t * (3 - 2 * t))[None, :, None]


def strook_weg(a, ref, ref_l, n, log):
    d = ref_l - luma_blur(a)
    m = (d > 2.0).sum(0) > 5
    w = 0
    while w < len(m) and m[w]:
        w += 1
    if w == 0 and d[:, :40].max() >= 3:
        w = 8                      # puntje van het vlak dat net binnenkomt
    if w == 0:
        return a
    pop = np.where((d < -15).any(0))[0]
    pop_x = int(pop.min()) if len(pop) else W
    rand = w + MARGE
    if rand + VERLOOP + 10 > pop_x:            # nooit over de pop heen
        rand = max(w, pop_x - VERLOOP - 10)
        log.append(f"LET OP beeld {n}: rand ingekort, pop vanaf x={pop_x}")
    log.append(f"beeld {n}: vlak {w} px breed, vervangen tot {rand} px plus {VERLOOP} px verloop, pop vanaf x={pop_x}")
    k = zacht_masker(rand, VERLOOP)
    return a * (1 - k) + ref * k


def stempel_weg(a, ref):
    x0, y0, x1, y1 = STEMPEL
    k = np.zeros((H, W, 1), np.float32)
    k[y0:y1, x0:x1] = 1
    k = np.asarray(Image.fromarray((k[:, :, 0] * 255).astype(np.uint8))
                   .filter(ImageFilter.GaussianBlur(6))).astype(np.float32)[:, :, None] / 255
    k[y0:y1 - 12, x0:x1 - 12] = 1
    return a * (1 - k) + ref * k


def label(a, al, font):
    im = Image.fromarray(np.clip(a + 0.5, 0, 255).astype(np.uint8)).convert("RGBA")
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    g = ImageDraw.Draw(lay)
    x, y = 96, 72
    tekst = "Exploded view"
    w = g.textlength(tekst, font=font)
    g.rounded_rectangle((x - 18, y - 12, x + 26 + w + 18, y + 46), radius=29,
                        fill=(20, 22, 28, int(200 * al)), outline=(255, 255, 255, int(28 * al)), width=1)
    g.ellipse((x - 2, y + 11, x + 12, y + 25), fill=(62, 207, 142, int(255 * al)))
    g.text((x + 26, y - 2), tekst, font=font, fill=(236, 238, 241, int(255 * al)))
    return np.asarray(Image.alpha_composite(im, lay).convert("RGB")).astype(np.float32)


def main():
    bron, uit = sys.argv[1], sys.argv[2]
    keur = sys.argv[3] if len(sys.argv) > 3 else None
    font = ImageFont.truetype(FONT, 30)
    ref = lees_beeld(bron, REF)
    ref_l = luma_blur(ref)
    doel = stempel_weg(lees_beeld(bron, GEEST[1]), ref)   # beeld 236 zonder stempel
    log = []
    lees = subprocess.Popen(["ffmpeg", "-v", "error", "-i", bron, "-f", "rawvideo",
                             "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    schrijf = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264",
                                "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
                                "-movflags", "+faststart", uit], stdin=subprocess.PIPE)
    n, m_uit = 0, 0
    keurlijst = {75, 85, 95, 105, 420, 425, 435, 450, 230, 236, 250}
    while True:
        buf = lees.stdout.read(W * H * 3)
        if len(buf) < W * H * 3:
            break
        a = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
        if any(lo <= n <= hi for lo, hi in BEREIKEN):
            a = strook_weg(a, ref, ref_l, n, log)
        if GEEST[0] < n < GEEST[1]:
            t = (n - GEEST[0]) / (GEEST[1] - GEEST[0])
            a = a * (1 - t) + doel * t
        if LABEL[0] <= n <= LABEL[1]:
            a = stempel_weg(a, ref)
            k, tot = n - LABEL[0], LABEL[1] - LABEL[0] + 1
            a = label(a, min(1.0, (k + 1) / 4, (tot - k) / 4), font)
        b = np.clip(a + 0.5, 0, 255).astype(np.uint8)
        herhaal = 1 + (HOUD_N if n == HOUD else 0)
        for _ in range(herhaal):
            schrijf.stdin.write(b.tobytes())
            m_uit += 1
        if keur and n in keurlijst:
            Image.fromarray(b).save(f"{keur}/bron-{n:04d}.png")
        n += 1
    schrijf.stdin.close()
    schrijf.wait()
    lees.wait()
    print("\n".join(log))
    print(f"klaar: {n} beelden in, {m_uit} uit ({m_uit / FPS:.2f} s)")
    print(f"vasthouden: beeld {HOUD} staat in de nieuwe film op {HOUD}..{HOUD + HOUD_N}; "
          f"beelden na {HOUD} schuiven {HOUD_N} op")


if __name__ == "__main__":
    main()
