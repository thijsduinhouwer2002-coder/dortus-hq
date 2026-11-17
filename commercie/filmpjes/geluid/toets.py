#!/usr/bin/env python3
"""Toets voor geluid.py: python3 toets.py <origineel.mp4> <met-geluid.mp4> <golf.png>

Faalt (exit 1) als: het beeld niet bit voor bit gelijk is, er geen stereo AAC-geluid is,
de lengte meer dan 0,05 s afwijkt, de luidheid niet tussen -19 en -14 LUFS zit,
de echte piek boven -1 dB komt, of er ergens een stil gat van meer dan 0,5 s is.
Maakt ook een plaatje van de golfvorm met de klikmomenten, om te bekijken.
"""
import json
import subprocess
import sys

import numpy as np

sys.path.insert(0, __import__("os").path.dirname(__file__))
from geluid import GELUID  # noqa: E402


def uit(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def video_md5(pad):
    return uit(["ffmpeg", "-v", "error", "-i", pad, "-map", "0:v:0", "-c", "copy", "-f", "md5", "-"]).strip()


def main():
    orig, nieuw, png = sys.argv[1:4]
    naam = orig.rsplit("/", 1)[-1][:-4]
    fouten = []
    if video_md5(orig) != video_md5(nieuw):
        fouten.append("beeld is veranderd")
    a = json.loads(uit(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                        "stream=codec_name,channels,sample_rate", "-of", "json", nieuw]))["streams"]
    if not a or a[0]["codec_name"] != "aac" or a[0]["channels"] != 2:
        fouten.append(f"geen stereo AAC: {a}")
    dv = float(uit(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                    "stream=duration", "-of", "csv=p=0", nieuw]))
    da = float(uit(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries",
                    "stream=duration", "-of", "csv=p=0", nieuw]))
    if abs(dv - da) > 0.05:
        fouten.append(f"lengte beeld {dv} en geluid {da} verschillen")
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", nieuw, "-af",
                        "loudnorm=I=-16:TP=-1.5:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    m = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    li, tp = float(m["input_i"]), float(m["input_tp"])
    if not -19 <= li <= -14:
        fouten.append(f"luidheid {li} LUFS")
    if tp > -1.0:
        fouten.append(f"piek {tp} dBTP")
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", nieuw, "-ac", "1", "-ar", "8000",
                          "-f", "s16le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, "<i2").astype(float) / 32768
    blok = 400  # 0,05 s
    rms = np.sqrt(np.mean(x[: len(x) // blok * blok].reshape(-1, blok) ** 2, axis=1))
    stil = rms < 10 ** (-50 / 20)
    langste, nu = 0, 0
    for s in stil[:-8]:  # het uitfaden aan het eind telt niet
        nu = nu + 1 if s else 0
        langste = max(langste, nu)
    if langste * 0.05 > 0.5:
        fouten.append(f"stil gat van {langste * 0.05:.2f} s")
    print(f"{naam}: beeld gelijk, {li:.1f} LUFS, piek {tp:.1f} dBTP, beeld {dv:.2f} s, geluid {da:.2f} s")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        t = np.arange(len(x)) / 8000
        fig, ax = plt.subplots(figsize=(10, 2.2), dpi=100)
        ax.plot(t, x, lw=0.4, color="#2a7")
        for k in GELUID[naam].get("klik", []):
            ax.axvline(k, color="#e33", lw=0.8)
        ax.set_xlim(0, t[-1])
        ax.set_title(f"{naam}: golfvorm, rode lijn = klik (groen licht in beeld)", fontsize=8)
        fig.tight_layout()
        fig.savefig(png)
    except ImportError:
        pass
    if fouten:
        print("FOUT: " + "; ".join(fouten))
        sys.exit(1)


if __name__ == "__main__":
    main()
