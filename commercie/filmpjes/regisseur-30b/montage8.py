#!/usr/bin/env python3
"""Montage v8 van de sale-Short (issue #159, Regisseur 27 nov 2026). Zoals montage7.py, met drie verschillen:
1. de muispijl: een X-schermafbeelding (mss) bevat de muis niet, dus de pijl komt op de echte plek uit muis.txt (per
   beeld geschreven door de opname), zoals een schermrecorder dat doet;
2. hook van Thijs bovenin (11:05: "This changes how you 3D print poseable figures:") en eindtekst zonder sale;
3. muziek met een vaste tel vanaf seconde 0 (Mixkit, Stock Music Free License), luid en gelijkmatig zoals het voorbeeld.
    python3 montage8.py <opnamemap: scherm-ruw.ts film.json start.txt muis.txt> <eind.mp4> <muziek.mp3> <begin_s>
                        <uit.mp4> [eind_sec]"""
import json
import os
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, SR = 1080, 1920, 30, 48000
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
BOVEN = ["This changes how you", "3D print poseable figures:"]
BOVEN_TOT = 9.0
SLOT = ["Click Joints Pro,", "add-on for Blender"]
SLOT_SEC = 3.0


def font(grootte):
    for f in (FONT, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(f, grootte)
        except OSError:
            continue
    return ImageFont.load_default()


def tekst_png(regels, grootte, y_mid):
    f = font(grootte)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    lh = int(grootte * 1.2)
    y = y_mid - lh * len(regels) / 2
    for r in regels:
        x = (W - d.textlength(r, font=f)) / 2
        d.text((x + 3, y + 4), r, font=f, fill=(0, 0, 0, 160))
        d.text((x, y), r, font=f, fill=(255, 255, 255), stroke_width=4, stroke_fill=(15, 15, 15))
        y += lh
    return im


def pijl():
    """Gewone witte muispijl met zwarte rand (zoals de standaardpijl van X en Blender), punt op (2, 2)."""
    s = 1.45
    pts = [(0, 0), (0, 17), (4, 13), (7, 20), (10, 19), (7, 12), (12, 12)]
    pts = [(2 + x * s * 1.25, 2 + y * s * 1.25) for x, y in pts]
    im = Image.new("RGBA", (44, 44), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.polygon(pts, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)
    return im


def beelden(pad, van, n, schaal=False):
    vf = f"scale={W}:{H}:flags=lanczos" if schaal else "null"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(pad), "-ss", f"{van:.4f}", "-frames:v", str(n), "-vf", vf,
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    k = W * H * 3
    laatste = None
    for _ in range(n):
        b = p.stdout.read(k)
        if len(b) < k:
            b = laatste
        laatste = b
        yield b
    p.stdout.close()
    p.wait()


def main():
    opn, eind, muziek, begin, uit = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4]), \
        Path(sys.argv[5])
    eind_sec = float(sys.argv[6]) if len(sys.argv) > 6 else 5.5
    film = json.loads((opn / "film.json").read_text())
    start = float((opn / "start.txt").read_text().strip())
    muis = {}
    for regel in (opn / "muis.txt").read_text().split("\n"):
        d = regel.split()
        if len(d) == 3:
            muis[int(round((float(d[0]) - start) * FPS))] = (int(d[1]), int(d[2]))
    van = film["delen"]["start"] - start
    # de laatste 0,7 s van de opname staat de muis stil (rust vóór het eind): weg, nergens een rustig stuk
    tot = film["delen"]["eind_weergave"] - start - float(os.environ.get("CJ_KNIP_EIND", "0.7"))
    i0 = int(round(van * FPS))
    nv = int(round((tot - van) * FPS))
    eind_n = int(round(eind_sec * FPS))
    totaal = (nv + eind_n) / FPS
    boven = tekst_png(BOVEN, 74, 300)
    slot = tekst_png(SLOT, 80, 1680)
    pl = pijl()
    tmp = uit.with_suffix(".beeld.mp4")
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(tmp)], stdin=subprocess.PIPE)
    laatst = None
    for i, b in enumerate(beelden(opn / "scherm-ruw.ts", van, nv)):
        im = Image.frombytes("RGB", (W, H), b)
        m = muis.get(i0 + i, laatst)
        if m is not None:
            laatst = m
            im.paste(pl, (m[0] - 2, m[1] - 2), pl)
        if i / FPS < BOVEN_TOT:
            a = min(1.0, (BOVEN_TOT - i / FPS) / 0.25)
            laag = boven if a >= 1.0 else boven.copy()
            if a < 1.0:
                laag.putalpha(laag.getchannel("A").point(lambda v: int(v * a)))
            im.paste(laag, (0, 0), laag)
        enc.stdin.write(im.tobytes())
    slot_van = eind_n - int(SLOT_SEC * FPS)
    for i, b in enumerate(beelden(eind, 0.0, eind_n, schaal=True)):
        if i >= slot_van:
            im = Image.frombytes("RGB", (W, H), b)
            a = min(1.0, (i - slot_van) / 8.0)
            laag = slot.copy()
            laag.putalpha(laag.getchannel("A").point(lambda v: int(v * a)))
            im.paste(laag, (0, 0), laag)
            b = im.tobytes()
        enc.stdin.write(b)
    enc.stdin.close()
    enc.wait()

    dec = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{begin:.3f}", "-i", str(muziek), "-t", f"{totaal + 0.2:.2f}",
                          "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    mu = np.frombuffer(dec, np.float32).reshape(-1, 2).copy()
    n = int(totaal * SR)
    mix = np.zeros((n, 2), np.float32)
    mix[:min(n, len(mu))] = mu[:n]
    fi, fo = int(0.02 * SR), int(0.8 * SR)      # vol vanaf de eerste tel, alleen een korte uitloop
    mix[:fi] *= np.linspace(0, 1, fi)[:, None]
    mix[n - fo:] *= np.linspace(1, 0, fo)[:, None]
    wav = uit.with_suffix(".wav")
    with wave.open(str(wav), "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes((np.clip(mix, -0.98, 0.98) * 32767).astype("<i2").tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-i", str(wav), "-c:v", "copy", "-c:a", "aac",
                    "-b:a", "192k", "-af", "loudnorm=I=-12:TP=-1.2:LRA=7", "-ar", "48000", "-shortest",
                    "-movflags", "+faststart", str(uit)], check=True)
    tmp.unlink()
    wav.unlink()
    print(json.dumps({"duur": round(totaal, 2), "weergave_s": round(nv / FPS, 2), "eind_s": round(eind_n / FPS, 2),
                      "muis_beelden": sum(1 for i in range(nv) if (i0 + i) in muis), "boven": BOVEN, "slot": SLOT}))


if __name__ == "__main__":
    main()
