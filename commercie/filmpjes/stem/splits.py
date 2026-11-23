#!/usr/bin/env python3
"""Eén lange voorlees-opname (bijvoorbeeld de ElevenLabs-mp3 die de hoofdchat maakt) in zinnen knippen.

Waarom (hoofdchat 23 nov 2026 ±19:00 NL): de tip-filmpjes krijgen een ElevenLabs-stem die de hoofdchat buiten CI
maakt, als één mp3 per filmpje. De montage verwacht per zin een wav. Met dit bestand hoeft er niets anders te
veranderen: zet STEM_MP3=<pad naar de mp3> en stem.maak_zinnen() knipt die opname in plaats van Kokoro te vragen.
De montage legt het beeld daarna zoals altijd op de gemeten lengtes (beeld volgt stem), dus de sync klopt vanzelf.

Hoe het knipt:
1. faster-whisper (WHISPER_MODEL, standaard small.en) geeft woorden met tijden.
2. De woorden worden op de zinnen van het script gelegd (difflib, verdraagt een verkeerd gehoord woord).
3. Tussen het laatste woord van zin i en het eerste van zin i+1 wordt geknipt op het stilste stukje van 10 ms.
Lukt stap 1 of 2 niet (whisper ontbreekt, of een grens valt niet te vinden), dan valt het terug op de N-1 langste
stiltes. Dat gaat mis als de stem binnen een zin langer pauzeert dan tussen zinnen; daarom staat in de uitvoer
welke manier is gebruikt.

Los draaien: python3 splits.py <mp3> <script.json> <uitmap>  (schrijft zin-01.wav ... en splits.json)."""
import difflib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

SR = 24000
STAP = int(0.01 * SR)  # 10 ms


def lees_audio(pad):
    """Elk formaat dat ffmpeg kent -> float32 mono 24 kHz."""
    ruw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(pad), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(ruw, np.float32).copy()


def _energie(x):
    n = len(x) // STAP
    return np.sqrt((x[:n * STAP].reshape(n, STAP) ** 2).mean(axis=1) + 1e-12)


def _woorden(tekst):
    """Kleine letters, alleen letters en cijfers; een streepje splitst ("Non-manifold" -> non, manifold)."""
    return re.findall(r"[a-z0-9]+", tekst.lower().replace("'", ""))


def _whisper_woorden(x):
    from faster_whisper import WhisperModel
    model = WhisperModel(os.environ.get("WHISPER_MODEL", "small.en"), device="cpu", compute_type="int8")
    # whisper wil 16 kHz
    x16 = np.interp(np.arange(0, len(x), SR / 16000), np.arange(len(x)), x).astype(np.float32)
    delen, _ = model.transcribe(x16, language="en", word_timestamps=True, beam_size=5)
    uit = []
    for d in delen:
        for w in d.words or []:
            for t in _woorden(w.word):
                uit.append((t, w.start, w.end))
    return uit


def grenzen_whisper(x, zinnen, woorden=None):
    """Per zingrens (i, i+1) het venster [eind laatste woord i, begin eerste woord i+1] in seconden, of None."""
    if woorden is None:
        woorden = _whisper_woorden(x)
    script, zin_van = [], []
    for i, z in enumerate(zinnen):
        for t in _woorden(z.get("uitspraak") or z["tekst"]):
            script.append(t)
            zin_van.append(i)
    gehoord = [w[0] for w in woorden]
    sm = difflib.SequenceMatcher(a=script, b=gehoord, autojunk=False)
    eerste, laatste, gevonden = {}, {}, set()
    for blok in sm.get_matching_blocks():
        for k in range(blok.size):
            i = zin_van[blok.a + k]
            gevonden.add(blok.a + k)
            _, s, e = woorden[blok.b + k]
            eerste[i] = min(eerste.get(i, s), s)
            laatste[i] = max(laatste.get(i, e), e)
    # is het laatste scriptwoord van zin i en het eerste van zin i+1 echt gehoord? Dan is die kant van het venster zeker.
    eind_tok = {zin_van[j]: j for j in range(len(script))}
    begin_tok = {}
    for j in range(len(script)):
        begin_tok.setdefault(zin_van[j], j)
    uit = []
    for i in range(len(zinnen) - 1):
        if i in laatste and i + 1 in eerste and laatste[i] <= eerste[i + 1] + 0.05:
            zeker = ("begin" if eind_tok[i] in gevonden else "") + ("eind" if begin_tok[i + 1] in gevonden else "")
            uit.append((laatste[i], eerste[i + 1], zeker))
        else:
            uit.append(None)
    return uit


def grenzen_stilte(x, n_zinnen, min_stil=0.12):
    """Terugval: de n-1 langste stiltes, als vensters in seconden, op volgorde van tijd."""
    e = _energie(x)
    stil = e < max(1e-4, np.percentile(e, 95) * 0.06)
    runs, i = [], 0
    while i < len(stil):
        if stil[i]:
            j = i
            while j < len(stil) and stil[j]:
                j += 1
            if i > 0 and j < len(stil) and (j - i) * 0.01 >= min_stil:  # niet de stilte aan begin en eind
                runs.append((i * 0.01, j * 0.01))
            i = j
        else:
            i += 1
    runs.sort(key=lambda r: r[0] - r[1])
    return sorted(runs[:n_zinnen - 1])


def knippunt(x, venster, rand=0.35):
    """Midden van het langste stille stuk in het venster, in samples.
    Het venster wordt aan beide kanten 0,35 s ruimer genomen: whisper legt woordgrenzen tot ±0,3 s mis (gemeten in
    toets_splits.py: "select" eindigde volgens whisper 0,18 s te vroeg, "run" begon 0,23 s te vroeg)."""
    a, b = venster[0], venster[1]
    e = _energie(x)
    i0 = max(0, int((min(a, b) - rand) * 100))
    i1 = min(len(e), int((max(a, b) + rand) * 100) + 1)
    if i1 <= i0:
        return int(a * SR)
    w = e[i0:i1]
    stil = w <= max(w.min() * 3, np.percentile(e, 95) * 0.02)
    runs, j = [], 0
    while j < len(w):
        if stil[j]:
            k = j
            while k < len(w) and stil[k]:
                k += 1
            runs.append((j, k))
            j = k
        else:
            j += 1
    if not runs:
        return (i0 + int(np.argmin(w))) * STAP + STAP // 2
    midden = ((a + b) / 2) * 100 - i0
    r = max(runs, key=lambda r: (r[1] - r[0], -abs((r[0] + r[1]) / 2 - midden)))
    return (i0 + (r[0] + r[1]) // 2) * STAP + STAP // 2


def knip(x, zinnen, woorden=None):
    """-> (lijst met audio per zin, verslag). Gooit een fout als het aantal stukken niet klopt."""
    n = len(zinnen)
    manier = "whisper"
    try:
        vensters = grenzen_whisper(x, zinnen, woorden)
    except Exception as fout:  # whisper niet geinstalleerd of kapot: terugvallen
        print(f"splits: whisper lukt niet ({fout}), terug naar stiltes")
        vensters = [None] * (n - 1)
    if any(v is None for v in vensters):
        stilte = grenzen_stilte(x, n)
        if len(stilte) != n - 1:
            raise RuntimeError(f"splits: {len(stilte) + 1} stukken gevonden, script heeft {n} zinnen")
        ontbrak = [i + 1 for i, v in enumerate(vensters) if v is None]
        if len(ontbrak) == n - 1:
            vensters, manier = stilte, "stilte"
        else:
            vensters = [v if v is not None else stilte[i] for i, v in enumerate(vensters)]
            manier = f"whisper, grens na zin {ontbrak} uit stiltes"
    punten = [0] + [knippunt(x, v) for v in vensters] + [len(x)]
    if any(b <= a for a, b in zip(punten, punten[1:])):
        raise RuntimeError(f"splits: knippunten niet oplopend {punten}")
    stukken = [x[a:b] for a, b in zip(punten, punten[1:])]
    verslag = {"manier": manier, "knippunten_s": [round(p / SR, 3) for p in punten[1:-1]]}
    return stukken, verslag


def main():
    mp3, script_pad, uit = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    sys.path.insert(0, str(Path(__file__).parent))
    import stem
    zinnen = json.loads(Path(script_pad).read_text())["scenes"]
    uit.mkdir(parents=True, exist_ok=True)
    stukken, verslag = knip(lees_audio(mp3), zinnen)
    lijst = []
    for i, s in enumerate(stukken):
        s = stem._stil_weg(s)
        pad = uit / f"zin-{i + 1:02d}.wav"
        stem.schrijf_wav(pad, s / (np.abs(s).max() + 1e-9) * 0.9)
        lijst.append({"wav": pad.name, "duur": round(len(s) / SR, 3), "tekst": zinnen[i]["tekst"]})
    verslag["zinnen"] = lijst
    (uit / "splits.json").write_text(json.dumps(verslag, indent=1, ensure_ascii=False))
    print(json.dumps(verslag, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
