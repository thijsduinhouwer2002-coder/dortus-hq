#!/usr/bin/env python3
"""Uitlegfilm Hats voor Thijs (Sanne 28 nov, #370).

Neemt de ruwe opname uit de workflow steam-hol-uitlegfilm.yml (1920 breed, echte opname, 30 fps) en maakt er een film
van 1920 x 1080 van: bovenaan stap en titel, in het midden de hele strook op ware maat, daaronder een 2x uitvergroting
van waar het om gaat, onderaan een grote ondertitel. Een gouden ring wijst aan wat je aanklikt (op strook en uitvergroting).

Gebruik: python3 maak_film.py ruw.mp4 scenes.json uit.mp4
"""
import json, math, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
FPS = 30
HIER = Path(__file__).resolve().parent
FONT = str(HIER.parent / "godot/kunst/letters/Fredoka.ttf")

def font(px, gewicht=600):
    f = ImageFont.truetype(FONT, px)
    try:
        f.set_variation_by_axes([gewicht])
    except Exception:
        pass
    return f

F_STAP, F_TITEL, F_ZIN = font(34, 500), font(64, 650), font(50, 500)
GOUD = (255, 200, 60)
DONKER = (24, 18, 14)

def ruw_beelden(ruw, start, dur, sw, sh):
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-i", ruw, "-t", f"{dur:.3f}", "-r", str(FPS),
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    n = sw * sh * 3
    while True:
        b = p.stdout.read(n)
        if len(b) < n:
            break
        yield Image.frombytes("RGB", (sw, sh), b)
    p.wait()

def grootte(ruw):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                   "stream=width,height", "-of", "csv=p=0", ruw]).decode().strip()
    w, h = out.split(",")
    return int(w), int(h)

def tekst_midden(d, y, tekst, f, kleur=(255, 255, 255)):
    regels = tekst.split("\n")
    for r in regels:
        b = d.textbbox((0, 0), r, font=f)
        x = (W - (b[2] - b[0])) // 2
        for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (3, 3)]:
            d.text((x + dx, y + dy), r, font=f, fill=(0, 0, 0))
        d.text((x, y), r, font=f, fill=kleur)
        y += int(f.size * 1.25)

def ring(d, cx, cy, r, t, dik=6):
    # ademende gouden ring met donkere rand, zodat hij op elke achtergrond leest
    rr = r * (1.0 + 0.08 * math.sin(t * 2 * math.pi * 1.2))
    for extra, kleur, w in [(dik, (0, 0, 0), dik + 6), (0, GOUD, dik)]:
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=kleur, width=w)

def pijl(d, cx, cy, r, t):
    # pijl van boven naar de ring, wipt zacht
    wip = 8 * math.sin(t * 2 * math.pi * 1.5)
    top = cy - r - 70 + wip
    punt = cy - r - 8 + wip
    d.line([cx, top, cx, punt - 18], fill=(0, 0, 0), width=14)
    d.line([cx, top, cx, punt - 18], fill=GOUD, width=8)
    d.polygon([(cx - 22, punt - 24), (cx + 22, punt - 24), (cx, punt + 4)], fill=GOUD, outline=(0, 0, 0))

def maak(ruw, scenes_pad, uit):
    sw, sh = grootte(ruw)
    sc = json.loads(Path(scenes_pad).read_text())
    strook_y = 150
    zoom_y = strook_y + sh + 30
    zoom_h = 2 * sh
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                           "-pix_fmt", "yuv420p", "-movflags", "+faststart", uit], stdin=subprocess.PIPE)
    for i, s in enumerate(sc):
        zx = int(s.get("zoom_x", sw // 2))
        x0 = max(0, min(sw - W // 2, zx - W // 4))
        if s.get("stil"):
            eerste = next(ruw_beelden(ruw, s["start"], 0.2, sw, sh))
            bron = (eerste for _ in range(int(s["dur"] * FPS)))
        else:
            bron = ruw_beelden(ruw, s["start"], s["dur"], sw, sh)
        for k, beeld in enumerate(bron):
            t = k / FPS
            doek = Image.new("RGB", (W, H), DONKER)
            # strook (bij een bredere opname verkleind naar 1920)
            strook = beeld if sw == W else beeld.resize((W, int(sh * W / sw)), Image.LANCZOS)
            doek.paste(strook, (0, strook_y))
            uitv = beeld.crop((x0, 0, x0 + W // 2, sh)).resize((W, zoom_h), Image.LANCZOS)
            doek.paste(uitv, (0, zoom_y))
            d = ImageDraw.Draw(doek)
            d.rectangle([0, zoom_y - 3, W, zoom_y], fill=(70, 55, 40))
            # kader op de strook: welk stuk is uitvergroot
            d.rectangle([x0 * W / sw, strook_y, (x0 + W // 2) * W / sw, strook_y + strook.size[1] - 1], outline=(255, 255, 255), width=2)
            stap = s.get("stap", "")
            if stap:
                tekst_midden(d, 18, stap, F_STAP, (230, 210, 170))
            tekst_midden(d, 58, s["titel"], F_TITEL, GOUD)
            ringen = s.get("ringen", [])
            if s.get("ring_vanaf", 0) <= t <= s.get("ring_tot", 999):
                for (rx, ry, rr) in ringen:
                    ring(d, rx * W / sw, strook_y + ry * W / sw, rr * 0.5, t, 4)
                    zx_, zy_ = (rx - x0) * 2, zoom_y + ry * 2
                    if 0 <= zx_ <= W:
                        ring(d, zx_, zy_, rr, t)
                        if s.get("pijl", True):
                            pijl(d, zx_, zy_, rr, t)
            tekst_midden(d, zoom_y + zoom_h + 25, s["zin"], F_ZIN)
            kaart = s.get("kaart")
            if kaart:
                kx, ky = kaart.get("x", 1350), kaart.get("y", zoom_y + 40)
                regels = kaart["regels"]
                bw, bh = 470, 30 + 56 * len(regels)
                d.rounded_rectangle([kx + 6, ky + 6, kx + bw + 6, ky + bh + 6], 14, fill=(0, 0, 0))
                d.rounded_rectangle([kx, ky, kx + bw, ky + bh], 14, fill=(245, 240, 230), outline=(90, 90, 90), width=2)
                for j, r in enumerate(regels):
                    if r == "-":
                        d.line([kx + 20, ky + 15 + 56 * j + 28, kx + bw - 20, ky + 15 + 56 * j + 28], fill=(180, 180, 180), width=2)
                    else:
                        d.text((kx + 30, ky + 22 + 56 * j), r, font=font(38, 450), fill=(20, 20, 20))
            if kaart:
                # muispijl bij de linkerbovenhoek van het menu, en eerlijk erbij dat het menu nagetekend is
                mx, my = kx - 4, ky - 4
                d.polygon([(mx, my), (mx, my + 52), (mx + 13, my + 40), (mx + 24, my + 62), (mx + 33, my + 57), (mx + 22, my + 36), (mx + 38, my + 36)], fill=(255, 255, 255), outline=(0, 0, 0), width=3)
                d.text((kx, ky + bh + 14), "menu van Windows, nagetekend", font=font(26, 400), fill=(255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0))
            ff.stdin.write(doek.tobytes())
    ff.stdin.close()
    ff.wait()

if __name__ == "__main__":
    maak(sys.argv[1], sys.argv[2], sys.argv[3])
