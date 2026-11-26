#!/usr/bin/env python3
"""Montage v7 van de sale-Short (issue #159, Regisseur 26 nov 2026), zoals het voorbeeld dat Thijs stuurde:
één doorlopend stuk uit de echte opname van de weergave (geen knip, geen staptekst), één vaste tekst bovenin de eerste
±9 s, dan de Cycles-eindfilm met bewegende camera en de saleregel pas in de laatste 3 s. Geluid: alleen muziek met
vrije licentie (3 opties, Thijs kiest), zacht opbouwend; geen stem, geen zoem.
    python3 montage7.py <opnamemap: scherm-ruw.ts film.json start.txt eind.mp4> <muziekmap> <uitmap>"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, SR = 1080, 1920, 30, 48000
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
BOVEN = ["Turning a rig into", "a poseable figure:"]
BOVEN_TOT = 9.0
SLOT = ["Click Joints Pro", "25% off this week,", "on Gumroad"]
SLOT_SEC = 3.0
MUZIEK = [  # (bestand, begin in s, naam voor de bron)
    ("Dreamer.mp3", 0.0, "Dreamer, Kevin MacLeod (incompetech.com), CC BY 4.0"),
    ("Floating_Cities.mp3", 0.0, "Floating Cities, Kevin MacLeod (incompetech.com), CC BY 4.0"),
    ("Lasting_Hope.mp3", 0.0, "Lasting Hope, Kevin MacLeod (incompetech.com), CC BY 4.0"),
]


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
        d.text((x + 3, y + 4), r, font=f, fill=(0, 0, 0, 150))
        d.text((x, y), r, font=f, fill=(255, 255, 255), stroke_width=3, stroke_fill=(20, 20, 20))
        y += lh
    return im


def beelden(pad, van, n, schaal=False):
    """Geeft n beelden (rgb24) een voor een, zonder alles in het geheugen te houden."""
    vf = f"scale={W}:{H}:flags=lanczos" if schaal else "null"
    # -ss na -i: beeldnauwkeurig (zoeken vóór -i in een .ts viel in proef 1 seconden verkeerd)
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
    opn, mu_map, uit = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    uit.mkdir(parents=True, exist_ok=True)
    film = json.loads((opn / "film.json").read_text())
    ts = opn / "scherm-ruw.ts"
    start = float((opn / "start.txt").read_text().strip())
    van = film["delen"]["start"] - start
    tot = film["delen"]["eind_weergave"] - start
    nv = int(round((tot - van) * FPS))
    eind_n = int(round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                             "csv=p=0", str(opn / "eind.mp4")], capture_output=True, text=True).stdout)
                       * FPS))
    totaal = (nv + eind_n) / FPS
    boven = tekst_png(BOVEN, 76, 165)
    slot = tekst_png(SLOT, 78, 1700)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(uit / "beeld.mp4")], stdin=subprocess.PIPE)
    for i, b in enumerate(beelden(ts, van, nv)):
        if i / FPS < BOVEN_TOT:
            im = Image.frombytes("RGB", (W, H), b)
            a = min(1.0, (BOVEN_TOT - i / FPS) / 0.25)
            laag = boven if a >= 1.0 else boven.copy()
            if a < 1.0:
                laag.putalpha(laag.getchannel("A").point(lambda v: int(v * a)))
            im.paste(laag, (0, 0), laag)
            b = im.tobytes()
        enc.stdin.write(b)
    slot_van = eind_n - int(SLOT_SEC * FPS)
    for i, b in enumerate(beelden(opn / "eind.mp4", 0.0, eind_n, schaal=True)):
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
    print(f"beeld: weergave {nv / FPS:.2f} s (vanaf {van:.2f} s in de opname), eindfilm {eind_n / FPS:.2f} s, "
          f"totaal {totaal:.2f} s")

    bronnen = {}
    for k, (bestand, b0, bron) in enumerate(MUZIEK, 1):
        dec = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(b0), "-i", str(mu_map / bestand), "-t",
                              f"{totaal + 0.2:.2f}", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                             capture_output=True, check=True).stdout
        mu = np.frombuffer(dec, np.float32).reshape(-1, 2).copy()
        n = int(totaal * SR)
        mix = np.zeros((n, 2), np.float32)
        mix[:min(n, len(mu))] = mu[:n]
        groei = np.linspace(0.6, 1.0, n)[:, None]          # zacht opbouwend, zoals het voorbeeld
        mix *= groei
        fi, fo = int(0.15 * SR), int(1.2 * SR)
        mix[:fi] *= np.linspace(0, 1, fi)[:, None]
        mix[n - fo:] *= np.linspace(1, 0, fo)[:, None]
        with wave.open(str(uit / f"m{k}.wav"), "wb") as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(SR)
            wf.writeframes((np.clip(mix, -0.98, 0.98) * 32767).astype("<i2").tobytes())
        naam = f"pro-sale-proces-v7-muziek{k}"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(uit / "beeld.mp4"), "-i", str(uit / f"m{k}.wav"),
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                        "-ar", "48000", "-shortest", "-movflags", "+faststart", str(uit / f"{naam}.mp4")], check=True)
        (uit / f"m{k}.wav").unlink()
        bronnen[naam] = bron
    (uit / "pro-sale-proces-v7-montage.json").write_text(json.dumps(
        {"duur": round(totaal, 2), "weergave_s": round(nv / FPS, 2), "eind_s": round(eind_n / FPS, 2),
         "boven": BOVEN, "boven_tot": BOVEN_TOT, "slot": SLOT, "slot_s": SLOT_SEC, "muziek": bronnen}, indent=1))
    (uit / "beeld.mp4").unlink()


if __name__ == "__main__":
    main()
