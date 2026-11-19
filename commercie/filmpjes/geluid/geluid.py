#!/usr/bin/env python3
"""Zelf gemaakt geluid onder de korte filmpjes (Chris, 17 nov 2026, verhaal 31 van Joris).

Alles is met code gemaakt (sinustonen en ruis), geen nummer of geluid van een ander,
dus TikTok heeft niets om te dempen. Het beeld wordt niet opnieuw gemaakt: de video
wordt 1 op 1 gekopieerd (-c:v copy), zodat het gekeurde beeld precies hetzelfde blijft.

Gebruik: python3 geluid.py <filmpje.mp4> <uit.mp4>
De tijden per filmpje staan in GELUID hieronder; ze komen uit een meting van het
groene oplichten per beeld (de klik) en de knippen in f2.json, f7.json en f9.json.
"""
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

SR = 48000
RNG = np.random.default_rng(17112026)

# Per filmpje: lengte, toon onder alles, en momenten (seconden).
GELUID = {
    "click-joints-7-tip-day-1-clearance": {
        "duur": 12.5,
        "bed": "joints",
        # zachte tik bij elke nieuwe tekst (knip 3,3 en 7,8 in f7.json)
        "tik": [3.3, 7.8],
        # delen zweven naar elkaar toe en lichten op (gemeten 8,63 tot 9,43 s)
        "zoef": [(8.55, 0.9)],
        # gewricht klikt dicht: groen licht begint op 10,97 s, stijgt het snelst op 11,03 s
        "klik": [11.0],
    },
    "click-joints-2-satisfying-bend": {
        "duur": 10.2,
        "bed": "joints",
        "tik": [0.5, 4.4],
        "zoef": [(6.0, 0.85)],
        # klik bij het oplichten: 0,17 s en 8,37 s (gemeten)
        "klik": [0.17, 8.37],
        # de arm buigt van ±2,6 tot ±4,3 s: zacht oplopende toon
        "buig": [(2.6, 1.7)],
    },
    "click-joints-5-pro-hinge-stops": {
        # hoofdchat 19 nov ±02:55 NL: gemeten met beeldverschil per beeld (30 fps)
        "duur": 14.7,
        "bed": "joints",
        # zachte tik bij elke nieuwe tekst (f5.json: 2,0 / 3,7 / 8,2 / 11,4)
        "tik": [2.0, 3.7, 8.2, 11.4],
        # de knie buigt: 0,3 tot 1,5 s, 4,0 tot 7,1 s, en voorbij de stop 8,3 tot 9,1 s
        "buig": [(0.3, 1.2), (4.0, 3.1), (8.3, 0.8)],
        # tok waar de beweging stilvalt tegen de stop (1,5 en 7,1 s)
        "klik": [1.5, 7.1],
    },
    "ebb-tip-1-eyes-closed": {
        "duur": 11.0,
        "bed": "ebb",
        # schermen in f9.json: in 0-2, uit 2-4, in 4-6, uit 6-8, rustig 8-11
        "adem": [("in", 0.0, 2.0), ("uit", 2.0, 2.0), ("in", 4.0, 2.0),
                 ("uit", 6.0, 2.0), ("rust", 8.0, 3.0)],
        # zacht zoemen (trilling) aan het begin van elke fase
        "zoem": [0.0, 2.0, 4.0, 6.0, 8.0],
    },
}


def t_as(duur):
    return np.arange(int(round(duur * SR))) / SR


def plak(buf, start, stuk):
    i = int(round(start * SR))
    if i >= len(buf):
        return
    n = min(len(stuk), len(buf) - i)
    buf[i:i + n] += stuk[:n]


def ruis_band(n, laag, hoog):
    """Ruis tussen laag en hoog Hz via de FFT."""
    spec = np.fft.rfft(RNG.standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    spec[(f < laag) | (f > hoog)] = 0
    x = np.fft.irfft(spec, n)
    return x / (np.abs(x).max() + 1e-9)


def bed_joints(duur):
    """Rustige warme toon: A-majeur zonder scherpe randen, zacht ademend."""
    t = t_as(duur)
    tonen = [220.0, 329.63, 440.0, 554.37]
    sterk = [0.5, 0.4, 0.3, 0.2]
    x = np.zeros_like(t)
    for f, s in zip(tonen, sterk):
        x += s * np.sin(2 * np.pi * f * t + RNG.uniform(0, 6.28))
        x += 0.25 * s * np.sin(2 * np.pi * f * 1.003 * t)  # licht zweven
    x *= 0.85 + 0.15 * np.sin(2 * np.pi * 0.25 * t)
    return 0.07 * x / np.abs(x).max()


def bed_ebb(duur):
    """Heel zachte lage toon (D) onder de zee."""
    t = t_as(duur)
    x = np.sin(2 * np.pi * 73.42 * t) + 0.5 * np.sin(2 * np.pi * 110.0 * t)
    return 0.05 * x / np.abs(x).max()


def klik():
    """Kort plastic 'tok': ruisstootje, twee heldere tonen en een kleine bons."""
    t = t_as(0.12)
    stoot = ruis_band(len(t), 1500, 9000) * np.exp(-t / 0.002)
    tok = (np.sin(2 * np.pi * 1850 * t) + 0.6 * np.sin(2 * np.pi * 3170 * t)) * np.exp(-t / 0.018)
    bons = np.sin(2 * np.pi * 130 * t) * np.exp(-t / 0.035)
    x = 0.55 * stoot + 0.5 * tok + 0.45 * bons
    return 0.16 * x / np.abs(x).max()


def tik():
    t = t_as(0.05)
    x = np.sin(2 * np.pi * 2600 * t) * np.exp(-t / 0.006)
    return 0.12 * x


def zoef(duur):
    n = int(duur * SR)
    t = np.arange(n) / SR
    x = ruis_band(n, 300, 3000)
    omhul = np.sin(np.pi * t / duur) ** 2
    return 0.05 * x * omhul


def buig(duur):
    t = t_as(duur)
    f = 330 + 110 * (t / duur)  # langzaam omhoog
    fase = 2 * np.pi * np.cumsum(f) / SR
    omhul = np.sin(np.pi * t / duur)
    return 0.03 * np.sin(fase) * omhul


def zee(fasen, duur):
    """Zee-achtig ruisen dat meegaat met de adem: aanzwellen bij in, wegebben bij uit."""
    n = int(round(duur * SR))
    x = ruis_band(n, 60, 1800)
    omhul = np.zeros(n)
    for soort, start, lang in fasen:
        i0, i1 = int(start * SR), min(n, int((start + lang) * SR))
        u = np.linspace(0, 1, i1 - i0, endpoint=False)
        if soort == "in":
            omhul[i0:i1] = 0.25 + 0.75 * np.sin(np.pi / 2 * u) ** 2
        elif soort == "uit":
            omhul[i0:i1] = 0.25 + 0.75 * np.cos(np.pi / 2 * u) ** 2
        else:
            omhul[i0:i1] = 0.25 * (1 - 0.6 * u)
    # omhulling gladstrijken zodat er geen sprongen zijn
    k = int(0.15 * SR)
    omhul = np.convolve(omhul, np.ones(k) / k, mode="same")
    return 0.35 * x * omhul


def zoem():
    """Zacht zoemen als een horloge dat trilt: 160 Hz, kort en rond."""
    t = t_as(0.28)
    omhul = np.sin(np.pi * t / 0.28) ** 2
    x = np.sin(2 * np.pi * 160 * t) * (0.7 + 0.3 * np.sin(2 * np.pi * 32 * t))
    return 0.10 * x * omhul


def maak_geluid(naam):
    g = GELUID[naam]
    duur = g["duur"]
    buf = bed_joints(duur) if g["bed"] == "joints" else bed_ebb(duur)
    for s in g.get("tik", []):
        plak(buf, s, tik())
    for s, d in g.get("zoef", []):
        plak(buf, s, zoef(d))
    for s, d in g.get("buig", []):
        plak(buf, s, buig(d))
    for s in g.get("klik", []):
        plak(buf, s, klik())
    if "adem" in g:
        buf += zee(g["adem"], duur)
    for s in g.get("zoem", []):
        plak(buf, s, zoem())
    # zacht in en uit (lus op TikTok loopt dan rustig door)
    n_in, n_uit = int(0.04 * SR), int(0.3 * SR)
    buf[:n_in] *= np.linspace(0, 1, n_in)
    buf[-n_uit:] *= np.linspace(1, 0, n_uit)
    # stereo: klein verschil links en rechts geeft ruimte
    links = buf
    rechts = np.concatenate([np.zeros(12), buf[:-12]])
    st = np.stack([links, rechts], axis=1)
    return st / (np.abs(st).max() + 1e-9) * 0.7


def schrijf_wav(pad, st):
    data = (np.clip(st, -1, 1) * 32767).astype("<i2")
    with wave.open(str(pad), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


def loop(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def main():
    if len(sys.argv) != 3:
        sys.exit("gebruik: python3 geluid.py <filmpje.mp4> <uit.mp4>")
    bron, uit = Path(sys.argv[1]), Path(sys.argv[2])
    naam = bron.stem
    if naam not in GELUID:
        sys.exit(f"FOUT: geen geluid bekend voor {naam}")
    wav = Path(tempfile.mkdtemp()) / "geluid.wav"
    schrijf_wav(wav, maak_geluid(naam))
    # luidheid: één vaste versterking (geen compressor, dus de klik blijft een klik).
    # Doel -16 LUFS, maar nooit boven -2 dB piek; dan wordt het wat zachter.
    meet = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af",
                           "loudnorm=print_format=json", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    try:
        m = json.loads(meet[meet.rindex("{"):meet.rindex("}") + 1])
    except ValueError:
        sys.exit("FOUT: luidheid meten lukte niet:\n" + meet[-800:])
    winst = min(-16.0 - float(m["input_i"]), -2.0 - float(m["input_tp"]))
    af = f"volume={winst:.2f}dB"
    loop(["ffmpeg", "-v", "error", "-y", "-i", str(bron), "-i", str(wav),
          "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
          "-af", af, "-c:a", "aac", "-b:a", "160k", "-ac", "2",
          "-t", str(GELUID[naam]["duur"]), "-movflags", "+faststart", str(uit)])
    wav.unlink()
    print(f"{uit}: klaar")


if __name__ == "__main__":
    main()
