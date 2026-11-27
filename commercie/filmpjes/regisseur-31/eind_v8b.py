import sys, subprocess
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import montage_cuts as m
from PIL import Image, ImageDraw
SRC = "/home/claude/dortus-hq/marketing/wachtrij/2026-12-01-yt-short-cuts-v8.mp4"
W, H, FPS = 1080, 1920, 30
N = 516            # eind op 17,2 s: paard schuin van voren, alle kleuren in beeld
VAN = N - 90       # eindtekst de laatste 3 s
tekst = m.tekst_png("poppins", m.SLOT, 92, m.SLOT_Y)
band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(band).rounded_rectangle((36, 1378, W - 36, 1630), radius=34, fill=(10, 10, 12, 215))
laag = Image.alpha_composite(band, tekst)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30",
    "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "beeld.mp4"], stdin=subprocess.PIPE)
for i, b in enumerate(m.beelden(SRC, N)):
    im = Image.frombytes("RGB", (W, H), b)
    if i >= VAN:
        a = min(1.0, (i - VAN + 1) / 8.0)
        l = laag if a >= 1 else laag.copy()
        if a < 1:
            l.putalpha(l.getchannel("A").point(lambda v: int(v * a)))
        im.paste(l, (0, 0), l)
    enc.stdin.write(im.tobytes())
enc.stdin.close(); enc.wait()
