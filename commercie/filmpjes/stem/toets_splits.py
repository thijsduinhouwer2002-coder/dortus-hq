#!/usr/bin/env python3
"""Toets voor splits.py: maakt met Kokoro een 'vreemde' opname (andere stem dan af_heart, wisselende pauzes, en
in één zin een pauze die langer is dan de pauzes tussen zinnen, zoals ElevenLabs bij een komma kan doen) en kijkt
of elk knippunt in de echte pauze tussen twee zinnen valt.

Draaien: KOKORO_MODEL=... KOKORO_VOICES=... python3 toets_splits.py <script.json>
Exit 0 = alle knippunten goed. Standaard met een ruisvloer van -50 dB (TOETS_RUIS). Laat ook zien dat alleen-stiltes in dit geval fout knipt (daarom whisper eerst)."""
import json
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import splits  # noqa: E402
import stem  # noqa: E402

SR = stem.SR


def main():
    zinnen = json.loads(Path(sys.argv[1]).read_text())["scenes"]
    os.environ.setdefault("KOKORO_STEM", "bm_george")
    k = stem.Kokoro()
    rng = np.random.default_rng(7)
    stukken, gaten, t = [], [], 0
    lange_zin = max(range(len(zinnen)), key=lambda i: len(zinnen[i]["tekst"]))
    for i, z in enumerate(zinnen):
        tekst = z.get("uitspraak") or z["tekst"]
        woorden = tekst.split()
        if i == lange_zin and len(woorden) > 5:  # pauze van 0,9 s midden in de zin
            h = len(woorden) // 2
            a, b = stem._stil_weg(k.zeg(" ".join(woorden[:h]))), stem._stil_weg(k.zeg(" ".join(woorden[h:])))
            x = np.concatenate([a, np.zeros(int(0.9 * SR), np.float32), b])
        else:
            x = stem._stil_weg(k.zeg(tekst))
        stukken.append(x.astype(np.float32))
        t += len(x)
        if i < len(zinnen) - 1:
            p = int(rng.uniform(0.25, 0.6) * SR)
            gaten.append((t / SR, (t + p) / SR))
            stukken.append(np.zeros(p, np.float32))
            t += p
    x = np.concatenate([np.zeros(int(0.3 * SR), np.float32)] + stukken + [np.zeros(int(0.4 * SR), np.float32)])
    gaten = [(a + 0.3, b + 0.3) for a, b in gaten]
    # ruisvloer zoals een echte opname (ademruis, ruis van de stem-dienst): standaard -50 dB, TOETS_RUIS=0 voor geen
    x = x + np.random.default_rng(3).normal(0, float(os.environ.get("TOETS_RUIS", "0.003")), len(x)).astype(np.float32)
    if os.environ.get("TOETS_MP3"):  # ook het hele pad via een mp3 en STEM_MP3 nalopen
        stem.schrijf_wav(Path(os.environ["TOETS_MP3"]).with_suffix(".wav"), x)

    fouten = 0
    _, verslag = splits.knip(x, zinnen)
    print("manier:", verslag["manier"])
    for i, (p, (a, b)) in enumerate(zip(verslag["knippunten_s"], gaten)):
        goed = a - 0.02 <= p <= b + 0.02
        fouten += not goed
        print(f"grens {i + 1}|{i + 2}: knip {p:.2f} s, pauze {a:.2f}-{b:.2f}  {'GOED' if goed else 'FOUT'}")
    stilte = splits.grenzen_stilte(x, len(zinnen))
    mis = sum(not (a - 0.02 <= (s0 + s1) / 2 <= b + 0.02) for (s0, s1), (a, b) in zip(stilte, gaten))
    print(f"ter vergelijking alleen stiltes: {mis} van {len(gaten)} grenzen fout (lange pauze zat in zin {lange_zin + 1})")
    print(f"UITSLAG: {fouten} FOUT")
    sys.exit(1 if fouten else 0)


if __name__ == "__main__":
    main()
