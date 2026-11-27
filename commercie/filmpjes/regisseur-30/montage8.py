#!/usr/bin/env python3
"""Montage v8 van de procesvorm-Short (Thijs 27 nov 11:05 tot 11:25): hook "This changes how you 3D print poseable
figures:", eindregel "Click Joints Pro, add-on for Blender" (geen sale in beeld), de echte muiswijzer op de plek waar
de muis per beeld echt stond (muis.txt, zoals ffmpeg x11grab hem tekent: het echte cursorbeeld DMZ-White van de X-server),
en muziek met een vaste tel vanaf seconde 0 (Mixkit Stock Music Free License).
Muziekmap: https://assets.mixkit.co/music/267/267.mp3 (en 989, 726) met curl ophalen als 267.mp3, 989.mp3, 726.mp3.
Oorspronkelijke uitleg v7:
Montage v7 van de sale-Short (issue #159, Regisseur 26 nov 2026), zoals het voorbeeld dat Thijs stuurde:
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
BOVEN = ["This changes how you", "3D print poseable figures:"]
BOVEN_TOT = 9.0
SLOT = ["Click Joints Pro,", "add-on for Blender"]
SLOT_SEC = 3.0
MUZIEK = [  # (bestand, begin in s, naam voor de bron); begin = een stuk dat vol en gelijkmatig is (gemeten)
    ("267.mp3", 11.5, "Need for speed (Mixkit, mixkit.co, Stock Music Free License)"),
    ("989.mp3", 36.0, "Sports Highlights (Mixkit, mixkit.co, Stock Music Free License)"),
    ("726.mp3", 35.0, "Stylz (Mixkit, mixkit.co, Stock Music Free License)"),
]
NAAM = "pro-proces-v8"
CURSOR = "/usr/share/icons/DMZ-White/cursors/left_ptr"


def cursor_beeld(pad=CURSOR, maat=48):
    """Leest het echte X-cursorbestand (Xcursor-formaat) en geeft (RGBA-beeld, xhot, yhot)."""
    import struct
    d = open(pad, "rb").read()
    assert d[:4] == b"Xcur"
    _hs, _v, ntoc = struct.unpack_from("<III", d, 4)
    beste = None
    for i in range(ntoc):
        typ, sub, pos = struct.unpack_from("<III", d, 16 + 12 * i)
        if typ == 0xFFFD0002 and (beste is None or abs(sub - maat) < abs(beste[0] - maat)):
            beste = (sub, pos)
    _h, _t, _s, _v, w, h, xh, yh, _dl = struct.unpack_from("<IIIIIIIII", d, beste[1])
    px = np.frombuffer(d, "<u4", w * h, beste[1] + 36).reshape(h, w)
    a = (px >> 24) & 255
    rgb = [((px >> s) & 255) for s in (16, 8, 0)]
    rgba = np.dstack([np.where(a > 0, c * 255 // np.maximum(a, 1), 0) for c in rgb] + [a]).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA"), xh, yh


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
    boven = tekst_png(BOVEN, 74, 175)
    muis = [tuple(int(v) for v in r.split()[1:3]) for r in (opn / "muis.txt").read_text().splitlines() if r.strip()]
    b0 = int(round(van * FPS))
    cur, xh, yh = cursor_beeld()
    slot = tekst_png(SLOT, 78, 1700)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(uit / "beeld.mp4")], stdin=subprocess.PIPE)
    for i, b in enumerate(beelden(ts, van, nv)):
        im = Image.frombytes("RGB", (W, H), b)
        if b0 + i < len(muis):
            mx, my = muis[b0 + i]
            im.paste(cur, (mx - xh, my - yh), cur)
        b = im.tobytes()
        if i / FPS < BOVEN_TOT:
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
        fi, fo = int(0.02 * SR), int(1.0 * SR)          # v8: vol vanaf de eerste tel, geen opbouw
        mix[:fi] *= np.linspace(0, 1, fi)[:, None]
        mix[n - fo:] *= np.linspace(1, 0, fo)[:, None]
        with wave.open(str(uit / f"m{k}.wav"), "wb") as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(SR)
            wf.writeframes((np.clip(mix, -0.98, 0.98) * 32767).astype("<i2").tobytes())
        naam = f"{NAAM}-muziek{k}"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(uit / "beeld.mp4"), "-i", str(uit / f"m{k}.wav"),
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-13:TP=-1.5:LRA=7",
                        "-ar", "48000", "-shortest", "-movflags", "+faststart", str(uit / f"{naam}.mp4")], check=True)
        (uit / f"m{k}.wav").unlink()
        bronnen[naam] = bron
    (uit / f"{NAAM}-montage.json").write_text(json.dumps(
        {"duur": round(totaal, 2), "weergave_s": round(nv / FPS, 2), "eind_s": round(eind_n / FPS, 2),
         "boven": BOVEN, "boven_tot": BOVEN_TOT, "slot": SLOT, "slot_s": SLOT_SEC, "muziek": bronnen}, indent=1))
    (uit / "beeld.mp4").unlink()


if __name__ == "__main__":
    main()
