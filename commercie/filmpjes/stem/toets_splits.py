#!/usr/bin/env python3
"""Toets voor splits.py: maakt met Kokoro een 'vreemde' opname (andere stem dan af_heart, wisselende pauzes, en
in één zin een pauze die langer is dan de pauzes tussen zinnen, zoals ElevenLabs bij een komma kan doen) en kijkt
of elk knippunt in de echte pauze tussen twee zinnen valt.

Draaien: KOKORO_MODEL=... KOKORO_VOICES=... python3 toets_splits.py <script.json>
Zonder whisper en Kokoro: python3 toets_splits.py --zonder-whisper (de twee gevallen uit de keuring van Daan, 23 nov:
M1 een niet verstaan eerste woord, M2 een hele zin niet verstaan; tonen met bekende pauzes en nepwoorden).
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


def _opname(delen):
    """delen: lijst van (woord of "st", duur). -> (audio, woorden met tijden) met een ruisvloer van -50 dB."""
    x, woorden, t = [], [], 0.0
    for w, d in delen:
        n = int(round(d * SR))
        if w == "st":
            x.append(np.zeros(n, np.float32))
        else:
            x.append((0.5 * np.sin(2 * np.pi * 220 * np.arange(n) / SR)).astype(np.float32))
            woorden.append((w, t, t + d))
        t += d
    x = np.concatenate(x)
    return x + np.random.default_rng(1).normal(0, 0.003, len(x)).astype(np.float32), woorden


def _geval(naam, delen, zinnen, mis, gaten, onzeker):
    x, woorden = _opname(delen)
    gehoord = [w for w in woorden if w[0] not in mis]
    _, verslag = splits.knip(x, zinnen, gehoord)
    fout = 0
    for i, (p, (a, b)) in enumerate(zip(verslag["knippunten_s"], gaten)):
        goed = a - 0.02 <= p <= b + 0.02
        fout += not goed
        print(f"{naam} grens {i + 1}|{i + 2}: knip {p:.2f} s, pauze {a:.2f}-{b:.2f}  {'GOED' if goed else 'FOUT'}")
    if sorted(verslag["onzeker"]) != sorted(onzeker):
        fout += 1
        print(f"{naam}: onzeker {verslag['onzeker']}, verwacht {onzeker}  FOUT")
    print(f"{naam}: manier {verslag['manier']!r}")
    return fout


def zonder_whisper():
    zinnen = [{"tekst": "a b"}, {"tekst": "c d"}, {"tekst": "g h"}, {"tekst": "e f"}]
    fouten = 0
    # M1: eerste woord van zin 3 niet verstaan, en in zin 3 een adempauze (0,5 s) langer dan het gat ervoor (0,4 s)
    fouten += _geval("M1", [("st", .3), ("a", .3), ("st", .05), ("b", .3), ("st", .5), ("c", .3), ("st", .05),
                            ("d", .3), ("st", .4), ("g", .3), ("st", .5), ("h", .3), ("st", .45), ("e", .3),
                            ("st", .05), ("f", .3), ("st", .4)],
                     zinnen, {"g"}, [(1.0, 1.5), (2.15, 2.55), (3.65, 4.1)], ["2|3"])
    # M2: zin 2 helemaal niet verstaan, en in zin 1 een pauze van 0,9 s (toets van Daan)
    fouten += _geval("M2", [("st", .3), ("a", .3), ("st", .9), ("b", .3), ("st", .5), ("c", .3), ("st", .05),
                            ("d", .3), ("st", .4), ("g", .3), ("st", .05), ("h", .3), ("st", .45), ("e", .3),
                            ("st", .05), ("f", .3), ("st", .4)],
                     zinnen, {"c", "d"}, [(1.8, 2.3), (2.95, 3.35), (4.0, 4.45)], ["1|2", "2|3"])
    # te weinig stiltes tussen de zekere grenzen: fout in plaats van gokken
    x, woorden = _opname([("st", .3), ("a", .3), ("st", .4), ("b", .3), ("c", .3), ("st", .4), ("e", .3),
                          ("st", .3)])
    try:
        splits.knip(x, [{"tekst": "a"}, {"tekst": "b"}, {"tekst": "c"}, {"tekst": "e"}],
                    [w for w in woorden if w[0] not in ("b", "c")])
        print("te weinig stiltes: geen fout gegeven  FOUT")
        fouten += 1
    except RuntimeError as e:
        print(f"te weinig stiltes: fout gegeven ({e})  GOED")
    print(f"UITSLAG: {fouten} FOUT")
    sys.exit(1 if fouten else 0)


def main():
    if sys.argv[1:] == ["--zonder-whisper"]:
        zonder_whisper()
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
