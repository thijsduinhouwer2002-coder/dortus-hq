#!/usr/bin/env python3
"""Ebb-filmpje met alle dieren (Regisseur run 28, 24 nov 2026; opdracht hoofdchat 16:55, Thijs 16:49).

Staand 1080x1920, ±21 s. Alleen echte schermbeelden uit de Garmin-simulator (fenix 8 47 mm):
  - run 74 (12 nov, proeftakken proef74a tot e, artefact ebb-plaatjes-fenix847mm): alle 25 dieren, dag en nacht;
  - tak schermen, garmin-adem/plaatjes/namen: de huidige ademronde (otter in, hold, uit), krab, sea log.
Het ronde scherm wordt strak uitgesneden (cirkel, geen horlogerand) en groot op een zee-achtergrond gezet.
Muziek en geluid zijn hier met code gemaakt (sinustonen en ruis): geen nummer van een ander.

Gebruik: python3 ebb_dieren.py <bronmap> <uitmap>
  <bronmap>/plat/<rij>__sessie-<plek>-<fase>-<dag|nacht>-fenix847mm.png (run 74) en <bronmap>/sch/<naam>.png (schermen)
Uit: ebb-dieren.mp4 (met geluid), ebb-dieren-script.json (scènes met tijden).
"""
import json
import math
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1080, 1920, 30
SR = 48000
BRON, UIT = Path(sys.argv[1]), Path(sys.argv[2])
UIT.mkdir(parents=True, exist_ok=True)

FONT = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FONT2 = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"

# run 74: welk dier staat op welke plek in welke proeftak (zelfde tabel als platformen/garmin/blad_alle25.py)
NAMEN = ["Fish", "Shrimp", "Jellyfish", "Turtle", "Crab", "Seahorse", "Starfish", "Clownfish", "Pufferfish", "Octopus",
         "Eel", "Ray", "Seal", "Dolphin", "Swordfish", "Sea otter", "Manta", "Shark", "Sunfish", "Orca", "Narwhal",
         "Giant squid", "Lobster", "Whale", "Sea cucumber"]
RIJ = {'a': [0, 1, 2, None, None, 3, 4, 5], 'b': [6, 7, 8, None, None, 9, 10, 11], 'c': [12, 13, 14, None, None, 15, 16, 17],
       'd': [18, 19, 20, None, None, 21, 22, 23], 'e': [None] * 5 + [24, None, None]}
PLEK = ['krab', 'schild', 'basis', 'eerste', 'terugval', 'komkommer', 'kreeft', 'otter']
WAAR = {d: (r, PLEK[i]) for r in RIJ for i, d in enumerate(RIJ[r]) if d is not None}

SCHERM = (135, 258, 589, 712)  # het ronde scherm (454 px) in de simulatorschermafdruk van 713x968 (gemeten)
D = 900                        # doorsnede van het scherm in het filmpje


def dier(nr, fase="in", dn="dag"):
    r, p = WAAR[nr]
    return BRON / "plat" / f"{r}__sessie-{p}-{fase}-{dn}-fenix847mm.png"


def sch(naam):
    return BRON / "sch" / f"{naam}.png"


_C = {}


def rond(pad, d=D):
    """Rond scherm, uitgesneden en vergroot, met een zachte rand (geen horlogerand)."""
    k = (str(pad), d)
    if k not in _C:
        im = Image.open(pad).convert("RGB").crop(SCHERM).resize((d, d), Image.LANCZOS)
        m = Image.new("L", (d * 4, d * 4), 0)
        ImageDraw.Draw(m).ellipse((6, 6, d * 4 - 6, d * 4 - 6), fill=255)
        im.putalpha(m.resize((d, d), Image.LANCZOS))
        _C[k] = im
    return _C[k]


# ---------- tijdlijn ----------
HOOK = [(7, "in", "dag"), (3, "hold", "dag"), (2, "in", "dag"), (9, "hold", "dag"), (17, "in", "dag"),
        (15, "hold", "dag"), (8, "in", "dag"), (23, "hold", "dag")]
SC = []  # (start, eind, soort, beelden, kop, onder)
t = 0.0
for i, h in enumerate(HOOK):
    SC.append((t, t + 0.3, "flits", [dier(*h)], "Which one breathes\nwith you tonight?", NAMEN[h[0]]))
    t += 0.3
SC.append((t, t + 3.6, "in", [sch("sessie-otter-in-dag")], "Breathe in", "")); t += 3.6
SC.append((t, t + 2.4, "hold", [sch("sessie-otter-hold-dag")], "Hold", "")); t += 2.4
SC.append((t, t + 3.6, "uit", [sch("sessie-otter-uit-dag")], "Breathe out", "")); t += 3.6
SC.append((t, t + 2.7, "wissel", [sch("sessie-krab-uit-dag"), dier(20, "in", "nacht"), dier(13, "hold", "nacht")],
           "New round,\nnew friend", "day or night")); t += 2.7
SC.append((t, t + 3.0, "log", [sch("sealog-3-alle25")], "Collect all 25", "your sea log fills up")); t += 3.0
SC.append((t, t + 2.8, "slot", [sch("einde-6b")], "Ebb", "on Garmin Connect IQ")); t += 2.8
DUUR = t


def zacht(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


# ---------- achtergrond: diepe zee met licht en belletjes ----------
def zee_bg():
    y = np.linspace(0, 1, H)[:, None]
    top, bodem = np.array([10, 110, 175]), np.array([4, 22, 60])
    a = top * (1 - y) ** 1.2 + bodem * (1 - (1 - y) ** 1.2)
    a = np.repeat(a[:, None, :], W, axis=1).reshape(H, W, 3)
    im = Image.fromarray(a.astype(np.uint8))
    # lichtbundels van boven
    l = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(l)
    for x0, b in [(120, 140), (420, 90), (700, 160), (930, 80)]:
        d.polygon([(x0, 0), (x0 + b, 0), (x0 + b * 2.4, H * 0.75), (x0 - b * 0.8, H * 0.75)], fill=28)
    l = l.filter(ImageFilter.GaussianBlur(40))
    im = Image.composite(Image.new("RGB", (W, H), (190, 235, 255)), im, l)
    return im


BG = zee_bg()
rng = np.random.default_rng(7)
BELLEN = [(rng.uniform(40, W - 40), rng.uniform(0, H), rng.uniform(5, 16), rng.uniform(60, 140)) for _ in range(34)]


def bellen(im, tt):
    d = ImageDraw.Draw(im, "RGBA")
    for x, y0, r, v in BELLEN:
        y = (y0 - v * tt) % (H + 60) - 30
        xx = x + 10 * math.sin(tt * 1.3 + y0)
        d.ellipse((xx - r, y - r, xx + r, y + r), outline=(220, 245, 255, 120), width=3)


def f(n, naam=FONT):
    return ImageFont.truetype(naam, n)


def tekst(im, s, y, grootte, kleur=(255, 255, 255), naam=FONT, alfa=255):
    d = ImageDraw.Draw(im, "RGBA")
    ft = f(grootte, naam)
    for i, regel in enumerate(s.split("\n")):
        b = d.textbbox((0, 0), regel, font=ft, stroke_width=8)
        x = (W - (b[2] - b[0])) / 2
        yy = y + i * int(grootte * 1.12)
        d.text((x, yy), regel, font=ft, fill=kleur + (alfa,), stroke_width=8, stroke_fill=(5, 25, 60, alfa))


def plak_rond(im, scherm, schaal, cy=1010, alfa=1.0, gloed=(120, 220, 255)):
    d = int(D * schaal)
    s = scherm.resize((d, d), Image.LANCZOS) if d != D else scherm
    x, y = (W - d) // 2, cy - d // 2
    # gloed en witte ring rond het scherm
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse((x - 26, y - 26, x + d + 26, y + d + 26), fill=gloed + (int(150 * alfa),))
    g = g.filter(ImageFilter.GaussianBlur(30))
    im.alpha_composite(g)
    ring = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse((x - 10, y - 10, x + d + 10, y + d + 10), outline=(255, 255, 255, int(235 * alfa)), width=9)
    im.alpha_composite(ring)
    if alfa < 1:
        s = s.copy()
        s.putalpha(s.getchannel("A").point(lambda v: int(v * alfa)))
    im.alpha_composite(s, (x, y))


def beeld(tt):
    im = BG.copy().convert("RGBA")
    bellen(im, tt)
    for i, (s0, s1, soort, bs, kop, onder) in enumerate(SC):
        if s0 <= tt < s1 or (i == len(SC) - 1 and tt >= s0):
            break
    u = (tt - s0) / (s1 - s0)
    k = tt - s0
    if soort == "flits":
        schaal = 1.0 + 0.07 * (1 - zacht(k / 0.18))
        plak_rond(im, rond(bs[0]), schaal)
        tekst(im, kop, 150, 92)
        tekst(im, onder, 1530, 70, (255, 226, 120))
    elif soort in ("in", "hold", "uit"):
        schaal = {"in": 0.92 + 0.12 * zacht(u), "hold": 1.04 + 0.004 * math.sin(k * 9), "uit": 1.04 - 0.12 * zacht(u)}[soort]
        a = zacht(k / 0.25) if soort != "in" else 1.0
        if soort == "in":
            a = zacht(k / 0.2)
        vorige = {"hold": "sessie-otter-in-dag", "uit": "sessie-otter-hold-dag"}.get(soort)
        if vorige and a < 1:
            plak_rond(im, rond(sch(vorige)), schaal)
        plak_rond(im, rond(bs[0]), schaal, alfa=a if (vorige or soort == "in") else 1.0)
        kleur = {"in": (150, 240, 255), "hold": (255, 226, 120), "uit": (255, 190, 210)}[soort]
        tekst(im, kop, 170, 120, kleur, alfa=int(255 * zacht(k / 0.2)))
        # adem-balk: groeit bij in, staat stil bij hold, krimpt bij uit
        p = {"in": zacht(u), "hold": 1.0, "uit": 1 - zacht(u)}[soort]
        dr = ImageDraw.Draw(im, "RGBA")
        dr.rounded_rectangle((190, 1560, 890, 1600), 20, fill=(255, 255, 255, 60))
        dr.rounded_rectangle((190, 1560, 190 + max(40, int(700 * p)), 1600), 20, fill=kleur + (255,))
    elif soort == "wissel":
        n = len(bs)
        j = min(n - 1, int(k / ((s1 - s0) / n)))
        kj = k - j * (s1 - s0) / n
        if j > 0 and kj < 0.2:
            plak_rond(im, rond(bs[j - 1]), 1.0)
        plak_rond(im, rond(bs[j]), 1.0 + 0.03 * zacht(kj / 0.9), alfa=zacht(kj / 0.2) if j > 0 else zacht(k / 0.2))
        tekst(im, kop, 150, 104)
        tekst(im, onder, 1530, 66, (255, 226, 120))
    elif soort == "log":
        plak_rond(im, rond(bs[0]), 0.98 + 0.05 * zacht(u), alfa=zacht(k / 0.25))
        tekst(im, kop, 180, 120, (255, 226, 120))
        tekst(im, onder, 1530, 62)
    else:  # slot
        a = zacht(k / 0.3)
        plak_rond(im, rond(bs[0], 760), 1.0 + 0.03 * zacht(u), cy=900, alfa=a)
        tekst(im, kop, 1330, 190, (255, 255, 255), alfa=int(255 * a))
        tekst(im, onder, 1560, 76, (150, 240, 255), naam=FONT2, alfa=int(255 * a))
    return im.convert("RGB")


# ---------- geluid: vrolijk muziekdoosje, zee die meeademt, zoem bij elke wissel ----------
def t_as(d):
    return np.arange(int(d * SR)) / SR


def plak(buf, s, stuk):
    i = int(s * SR)
    j = min(len(buf), i + len(stuk))
    if i < len(buf):
        buf[i:j] += stuk[:j - i]


def noot(freq, d=0.9, sterk=1.0):
    t = t_as(d)
    x = (np.sin(2 * np.pi * freq * t) + 0.35 * np.sin(2 * np.pi * 2 * freq * t) + 0.12 * np.sin(2 * np.pi * 3 * freq * t))
    return 0.13 * sterk * x * np.exp(-t / 0.28) * np.minimum(1, t / 0.004)


def pad(freqs, d):
    t = t_as(d)
    x = sum(np.sin(2 * np.pi * fq * t) for fq in freqs) / len(freqs)
    om = np.minimum(1, t / 0.6) * np.minimum(1, (d - t) / 0.6)
    return 0.05 * x * om


def zoem():
    t = t_as(0.28)
    return 0.12 * np.sin(2 * np.pi * 160 * t) * (0.7 + 0.3 * np.sin(2 * np.pi * 32 * t)) * np.sin(np.pi * t / 0.28) ** 2


def ruis(n, laag, hoog):
    x = rng.standard_normal(n)
    X = np.fft.rfft(x)
    fr = np.fft.rfftfreq(n, 1 / SR)
    X[(fr < laag) | (fr > hoog)] = 0
    x = np.fft.irfft(X, n)
    return x / (np.abs(x).max() + 1e-9)


def geluid():
    n = int(DUUR * SR)
    buf = np.zeros(n)
    C = {"C": 523.25, "D": 587.33, "E": 659.25, "G": 783.99, "A": 880.0, "c": 1046.5, "d": 1174.7, "e": 1318.5}
    # hook: bij elk dier een noot, omhoog (vrolijk)
    for i, nm in enumerate("CDEGAcde"):
        plak(buf, i * 0.3, noot(C[nm], 0.6, 1.1))
    # daarna een rustig muziekdoosje, 100 per minuut, pentatonisch
    melodie = "E.G.A.G.E.D.C.D.E.G.c.A.G.E.D.E.G.A.c.A.G.E.G.A.c.d.c.A.G.A.c.e.d.c.A.G.c"
    stap = 0.3
    tt = 2.4
    for nm in melodie.split("."):
        if tt > DUUR - 0.6:
            break
        plak(buf, tt, noot(C[nm] / 2, 1.0, 0.75))
        tt += stap * 2 if nm in "Gc" else stap
    # zachte akkoorden eronder
    for s, akk in [(2.4, (261.6, 329.6, 392.0)), (6.0, (220.0, 261.6, 329.6)), (8.4, (174.6, 220.0, 261.6)),
                   (12.0, (196.0, 246.9, 293.7)), (14.7, (261.6, 329.6, 392.0)), (17.7, (174.6, 220.0, 261.6, 392.0))]:
        plak(buf, s, pad(akk, min(3.8, DUUR - s)))
    # zee die meeademt: aanzwellen bij in, stil bij hold, wegebben bij uit
    om = np.full(n, 0.15)
    for s0, s1, soort, *_ in SC:
        i0, i1 = int(s0 * SR), min(n, int(s1 * SR))
        u = np.linspace(0, 1, i1 - i0, endpoint=False)
        if soort == "in":
            om[i0:i1] = 0.2 + 0.8 * np.sin(np.pi / 2 * u) ** 2
        elif soort == "hold":
            om[i0:i1] = 1.0 - 0.3 * u
        elif soort == "uit":
            om[i0:i1] = 0.7 * np.cos(np.pi / 2 * u) ** 2 + 0.15
    k = int(0.2 * SR)
    om = np.convolve(om, np.ones(k) / k, mode="same")
    buf += 0.10 * ruis(n, 80, 1600) * om
    # zoem als het horloge trilt: bij in, hold en uit
    for s0, s1, soort, *_ in SC:
        if soort in ("in", "hold", "uit"):
            plak(buf, s0, zoem())
    n_uit = int(0.5 * SR)
    buf[-n_uit:] *= np.linspace(1, 0, n_uit)
    st = np.stack([buf, np.concatenate([np.zeros(14), buf[:-14]])], axis=1)
    return st / (np.abs(st).max() + 1e-9) * 0.7


def main():
    stil = UIT / "stil.mp4"
    enc = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(stil)], stdin=subprocess.PIPE)
    for i in range(int(round(DUUR * FPS))):
        enc.stdin.write(beeld(i / FPS).tobytes())
    enc.stdin.close()
    enc.wait()
    wav = UIT / "geluid.wav"
    data = (np.clip(geluid(), -1, 1) * 32767).astype("<i2")
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    meet = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    m = json.loads(meet[meet.rindex("{"):meet.rindex("}") + 1])
    winst = min(-16.0 - float(m["input_i"]), -2.0 - float(m["input_tp"]))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-af", f"volume={winst:.2f}dB", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
                    "-t", f"{DUUR:.3f}", "-movflags", "+faststart", str(UIT / "ebb-dieren.mp4")], check=True)
    stil.unlink()
    wav.unlink()
    json.dump({"duur": round(DUUR, 2), "scenes": [{"start": round(a, 2), "eind": round(b, 2), "soort": s, "kop": k, "onder": o,
                                                     "beelden": [p.name for p in bs]} for a, b, s, bs, k, o in SC]},
              open(UIT / "ebb-dieren-script.json", "w"), indent=1, ensure_ascii=False)
    print("klaar", UIT / "ebb-dieren.mp4", round(DUUR, 2), "s")


if __name__ == "__main__":
    main()
