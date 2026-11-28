#!/usr/bin/env python3
"""regisseur-33 (#384, Short Click Cuts 1.1 Draw cut): kopie van regisseur-31/montage_cuts.py met nieuwe hook,
eindtekst op een donkere band (zoals v8b) en een kruisje als muiswijzer zolang Draw cut loopt (Blender toont dan een kruis).
Montage van de lanceer-Short Click Cuts (issue #135, Regisseur 27 nov 2026), in de vorm van v8c (montage8.py van
regisseur-30b): echte opname (scherm-ruw.ts, al 1080x1920), muispijl op de echte plek uit muis.txt, hook vast in beeld
de eerste seconden, eindtekst in de laatste 3 s, muziek met een vaste tel vanaf seconde 0.
Nieuw (Thijs 27 nov 16:14, lettertype van v8c niet mooi): het lettertype is te kiezen; drie OFL-kandidaten.
    python3 montage_cuts.py <opnamemap> <muziek.mp3> <muziek_begin_s> <uit.mp4> <font: tiktok|montserrat|poppins>
    python3 montage_cuts.py --eerste <opnamemap> <uit.jpg> <font>   (alleen het eerste beeld)"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, SR = 1080, 1920, 30, 48000
FONTMAP = Path(__file__).resolve().parent.parent / "regisseur-31" / "fonts"
FONTS = {   # alle drie SIL Open Font License 1.1, uit github.com/google/fonts (ofl/...)
    "tiktok": (FONTMAP / "TikTokSans.ttf", b"ExtraBold"),
    "montserrat": (FONTMAP / "Montserrat.ttf", b"ExtraBold"),
    "poppins": (FONTMAP / "Poppins-ExtraBold.ttf", None),
}
BOVEN = ["No seam through the face?", "Draw your own cut:"]   # r2: twee regels, onderin op een band (blinde test r1: tekst bedekte het model)
BOVEN_TOT = 3.6      # hook staat vast in beeld tot net na de getekende lijn
BOVEN_Y = 1690
SLOT = ["Click Cuts 1.1,", "add-on for Blender"]
SLOT_SEC = 3.0
SLOT_Y = 1500


def font(naam, grootte):
    pad, stijl = FONTS[naam]
    f = ImageFont.truetype(str(pad), grootte)
    if stijl:
        try:
            f.set_variation_by_name(stijl)
        except Exception:  # noqa: BLE001
            f.set_variation_by_axes([800])
    return f


def tekst_png(naam, regels, grootte, y_mid):
    f = font(naam, grootte)
    while max(ImageDraw.Draw(Image.new("L", (1, 1))).textlength(r, font=f) for r in regels) > 980 - 14:
        grootte -= 2
        f = font(naam, grootte)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    lh = int(grootte * 1.15)
    y = y_mid - lh * len(regels) / 2
    for r in regels:
        x = (W - d.textlength(r, font=f)) / 2
        d.text((x, y + 6), r, font=f, fill=(0, 0, 0, 150), stroke_width=7, stroke_fill=(0, 0, 0, 150))
        d.text((x, y), r, font=f, fill=(255, 255, 255), stroke_width=7, stroke_fill=(12, 12, 12))
        y += lh
    return im


def hook_laag(naam):
    tekst = tekst_png(naam, BOVEN, 100, BOVEN_Y)
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(band).rounded_rectangle((24, BOVEN_Y - 150, W - 24, BOVEN_Y + 150), radius=34, fill=(10, 10, 12, 200))
    return Image.alpha_composite(band, tekst)


def slot_laag(naam):
    tekst = tekst_png(naam, SLOT, 92, SLOT_Y)
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(band).rounded_rectangle((36, 1378, W - 36, 1630), radius=34, fill=(10, 10, 12, 215))
    return Image.alpha_composite(band, tekst)


def pijl():
    """Gewone witte muispijl met zwarte rand (zoals de standaardpijl van X en Blender), punt op (2, 2)."""
    s = 1.45 * 1.25
    pts = [(0, 0), (0, 17), (4, 13), (7, 20), (10, 19), (7, 12), (12, 12)]
    pts = [(2 + x * s, 2 + y * s) for x, y in pts]
    im = Image.new("RGBA", (44, 44), (0, 0, 0, 0))
    ImageDraw.Draw(im).polygon(pts, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)
    return im


KRUIS = [-1, -1]   # beelden waarin Draw cut loopt (film.json "kruis"): dan toont Blender een kruis als wijzer


def kruis():
    """Kruiswijzer zoals Blender bij Draw cut (cursor_modal_set CROSSHAIR): wit met zwarte rand, midden op (22, 22)."""
    im = Image.new("RGBA", (45, 45), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for w_, kl in ((5, (0, 0, 0, 255)), (2, (255, 255, 255, 255))):
        d.line((22, 2, 22, 17), fill=kl, width=w_)
        d.line((22, 27, 22, 42), fill=kl, width=w_)
        d.line((2, 22, 17, 22), fill=kl, width=w_)
        d.line((27, 22, 42, 22), fill=kl, width=w_)
    return im


KR = None


def beelden(pad, n):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(pad), "-frames:v", str(n), "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    k, laatste = W * H * 3, None
    for _ in range(n):
        b = p.stdout.read(k)
        if len(b) < k:
            b = laatste
        laatste = b
        yield b
    p.stdout.close()
    p.wait()


def muis_lees(opn):
    muis = {}
    for regel in (opn / "muis.txt").read_text().split("\n"):
        d = regel.split()
        if len(d) == 3:
            muis[int(round(float(d[0]) * FPS))] = (int(d[1]), int(d[2]))
    return muis


def beeld(b, i, n, muis, laatst, boven, slot, pl):
    im = Image.frombytes("RGB", (W, H), b)
    m = muis.get(i, laatst)
    if m is not None:
        if KRUIS[0] <= i < KRUIS[1]:
            im.paste(KR, (m[0] - 22, m[1] - 22), KR)
        else:
            im.paste(pl, (m[0] - 2, m[1] - 2), pl)
    t = i / FPS
    if t < BOVEN_TOT:
        a = min(1.0, (BOVEN_TOT - t) / 0.2)
        laag = boven if a >= 1.0 else boven.copy()
        if a < 1.0:
            laag.putalpha(laag.getchannel("A").point(lambda v: int(v * a)))
        im.paste(laag, (0, 0), laag)
    slot_van = n - int(SLOT_SEC * FPS)
    if i >= slot_van:
        a = min(1.0, (i - slot_van) / 8.0)
        laag = slot.copy()
        laag.putalpha(laag.getchannel("A").point(lambda v: int(v * a)))
        im.paste(laag, (0, 0), laag)
    return im, m


def main():
    global KR
    KR = kruis()
    if sys.argv[1] == "--eerste":
        opn, uit, naam = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
        b = next(beelden(opn / "scherm-ruw.ts", 1))
        im, _ = beeld(b, 0, 9999, muis_lees(opn), None, hook_laag(naam),
                      slot_laag(naam), pijl())
        im.save(uit, quality=92)
        return
    opn, muziek, begin, uit, naam = Path(sys.argv[1]), Path(sys.argv[2]), float(sys.argv[3]), Path(sys.argv[4]), \
        sys.argv[5]
    film = json.loads((opn / "film.json").read_text())
    if len(film.get("kruis", [])) == 2:
        KRUIS[:] = film["kruis"]
    n = int(round(film["delen"]["eind"] * FPS))
    totaal = n / FPS
    muis = muis_lees(opn)
    boven, slot, pl = hook_laag(naam), slot_laag(naam), pijl()
    tmp = uit.with_suffix(".beeld.mp4")
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(tmp)], stdin=subprocess.PIPE)
    laatst = None
    for i, b in enumerate(beelden(opn / "scherm-ruw.ts", n)):
        im, laatst = beeld(b, i, n, muis, laatst, boven, slot, pl)
        enc.stdin.write(im.tobytes())
    enc.stdin.close()
    enc.wait()

    dec = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{begin:.3f}", "-i", str(muziek), "-t", f"{totaal + 0.2:.2f}",
                          "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    mu = np.frombuffer(dec, np.float32).reshape(-1, 2).copy()
    ns = int(totaal * SR)
    mix = np.zeros((ns, 2), np.float32)
    mix[:min(ns, len(mu))] = mu[:ns]
    fi, fo = int(0.02 * SR), int(0.8 * SR)
    mix[:fi] *= np.linspace(0, 1, fi)[:, None]
    mix[ns - fo:] *= np.linspace(1, 0, fo)[:, None]
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
    print(json.dumps({"duur": round(totaal, 2), "font": naam, "boven": BOVEN, "slot": SLOT,
                      "muis_beelden": sum(1 for i in range(n) if i in muis)}))


if __name__ == "__main__":
    main()
