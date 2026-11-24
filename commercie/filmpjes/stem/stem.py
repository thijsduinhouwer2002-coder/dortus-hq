#!/usr/bin/env python3
"""Voice-over per zin, met verwisselbare stem (opdracht hoofdchat 23 nov 2026 ±11:45 NL).

Eén functie: maak_zinnen(zinnen, map) -> per zin een wav (24 kHz mono), stilte voor en na weggeknipt, met de
gemeten lengte. De montage legt daarna de beeldscènes op die lengtes (beeld volgt stem).

Welke stem:
- Staat ELEVENLABS_API_KEY in de omgeving (geheim in de repo), dan ElevenLabs (betaald plan nodig voor commercieel
  gebruik; daar beslist Thijs over). Stem-id uit ELEVENLABS_VOICE_ID, model uit ELEVENLABS_MODEL.
- Anders de open stem Kokoro-82M (Apache 2.0) via kokoro-onnx (MIT), stem uit KOKORO_STEM (standaard af_heart).
  Modelbestanden: KOKORO_MODEL en KOKORO_VOICES (paden). Licenties en bronnen: LEESMIJ.md in deze map.
Beide geven dezelfde uitvoer, dus de timing en de rest van de film werken voor allebei hetzelfde.

Elke zin is een dict met "tekst" (wat in beeld en in het transcript staat) en eventueel "uitspraak" (wat de stem
leest, bijvoorbeeld "three M F" voor "3MF")."""
import json
import os
import urllib.request
import wave
from pathlib import Path

import numpy as np

SR = 24000


def _stil_weg(x, drempel=0.012, marge=0.03):
    """Knipt stilte voor en na weg, met een kleine marge, zodat de lengte = de echte spraak."""
    a = np.abs(x)
    k = int(0.01 * SR)
    glad = np.convolve(a, np.ones(k) / k, mode="same")
    boven = np.where(glad > drempel * max(1e-6, glad.max()) * 4)[0]
    if len(boven) == 0:
        return x
    i0 = max(0, boven[0] - int(marge * SR))
    i1 = min(len(x), boven[-1] + int(marge * SR))
    return x[i0:i1]


def schrijf_wav(pad, x, sr=SR):
    data = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(str(pad), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(data.tobytes())


def lees_wav(pad):
    with wave.open(str(pad), "rb") as w:
        n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
        x = np.frombuffer(w.readframes(n), "<i2").astype(np.float32) / 32768.0
    if ch == 2:
        x = x.reshape(-1, 2).mean(axis=1)
    return x, sr


class Kokoro:
    naam = "kokoro"

    def __init__(self):
        from kokoro_onnx import Kokoro as K
        self.stem = os.environ.get("KOKORO_STEM", "af_heart")
        self.snelheid = float(os.environ.get("KOKORO_SNELHEID", "0.95"))
        self.k = K(os.environ.get("KOKORO_MODEL", "kokoro-v1.0.onnx"), os.environ.get("KOKORO_VOICES", "voices-v1.0.bin"))
        # taal uit KOKORO_TAAL (bijv. "es" voor ef_dora/em_alex, Spaanse proef Skillful Toys 24 nov); standaard als voorheen
        self.taal = os.environ.get("KOKORO_TAAL") or ("es" if self.stem[:1] == "e" else "en-gb" if self.stem.startswith("b") else "en-us")

    def info(self):
        return {"stem": "Kokoro-82M v1.0", "stemnaam": self.stem, "snelheid": self.snelheid,
                "licentie": "Apache-2.0 (model en stemmen, hexgrad/Kokoro-82M); kokoro-onnx MIT"}

    def zeg(self, tekst):
        x, sr = self.k.create(tekst, voice=self.stem, speed=self.snelheid, lang=self.taal)
        x = np.asarray(x, np.float32)
        if sr != SR:
            x = np.interp(np.arange(int(len(x) * SR / sr)) * sr / SR, np.arange(len(x)), x).astype(np.float32)
        return x


class ElevenLabs:
    naam = "elevenlabs"

    def __init__(self):
        self.sleutel = os.environ["ELEVENLABS_API_KEY"]
        # standaard een rustige Engelse stem uit de eigen bibliotheek van ElevenLabs; te wisselen met het geheim/var
        self.stem = os.environ.get("ELEVENLABS_VOICE_ID") or "JBFqnCBsd6RMkjVDRZzb"
        # let op: in de blinde Speech Arena scoort Multilingual v2 maar iets boven Kokoro (Elo 1092 tegen 1060), Eleven v4
        # veel hoger (1340), DERDEN https://artificialanalysis.ai/text-to-speech/leaderboard (23 nov 2026). Kies dus het
        # nieuwste model via de repo-variabele ELEVENLABS_MODEL zodra er een betaald plan is.
        self.model = os.environ.get("ELEVENLABS_MODEL") or "eleven_multilingual_v2"

    def info(self):
        return {"stem": "ElevenLabs " + self.model, "stemnaam": self.stem,
                "licentie": "alleen commercieel met een betaald plan (https://elevenlabs.io/docs/overview/administration/billing)"}

    def zeg(self, tekst):
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.stem}?output_format=pcm_24000"
        body = json.dumps({"text": tekst, "model_id": self.model,
                           "voice_settings": {"stability": 0.55, "similarity_boost": 0.75}}).encode()
        req = urllib.request.Request(url, data=body, method="POST", headers={
            "xi-api-key": self.sleutel, "Content-Type": "application/json", "Accept": "audio/pcm"})
        with urllib.request.urlopen(req, timeout=120) as r:
            pcm = r.read()
        return np.frombuffer(pcm, "<i2").astype(np.float32) / 32768.0


def kies_stem():
    if os.environ.get("ELEVENLABS_API_KEY", "").strip():
        return ElevenLabs()
    return Kokoro()


def maak_zinnen(zinnen, map_):
    """zinnen: [{"tekst":..., "uitspraak":...}] -> (lijst met {"wav", "duur"}, info van de stem)."""
    map_ = Path(map_)
    map_.mkdir(parents=True, exist_ok=True)
    if os.environ.get("STEM_MP3", "").strip():
        return _zinnen_uit_bestand(zinnen, map_, os.environ["STEM_MP3"].strip())
    stem = kies_stem()
    uit = []
    for i, z in enumerate(zinnen):
        x = _stil_weg(stem.zeg(z.get("uitspraak") or z["tekst"]))
        x = x / (np.abs(x).max() + 1e-9) * 0.9
        pad = map_ / f"zin-{i + 1:02d}.wav"
        schrijf_wav(pad, x)
        uit.append({"wav": str(pad), "duur": round(len(x) / SR, 3)})
        print(f"stem {stem.naam}: zin {i + 1} {len(x) / SR:.2f} s  {z['tekst']}")
    return uit, dict(stem.info(), soort=stem.naam)


def _zinnen_uit_bestand(zinnen, map_, pad):
    """STEM_MP3 gezet: één opname met alle zinnen (bijvoorbeeld ElevenLabs, door de hoofdchat gemaakt) knippen
    met splits.py, zelfde uitvoer als hierboven. STEM_BRON zet de naam in de info (standaard elevenlabs)."""
    import splits
    stukken, verslag = splits.knip(splits.lees_audio(pad), zinnen)
    if verslag.get("onzeker"):
        print(f"stem bestand: naluisteren, onzekere grenzen {verslag['onzeker']} ({verslag['manier']})")
    uit = []
    for i, (z, x) in enumerate(zip(zinnen, stukken)):
        x = _stil_weg(x)
        x = x / (np.abs(x).max() + 1e-9) * 0.9
        p = map_ / f"zin-{i + 1:02d}.wav"
        schrijf_wav(p, x)
        uit.append({"wav": str(p), "duur": round(len(x) / SR, 3)})
        print(f"stem bestand: zin {i + 1} {len(x) / SR:.2f} s  {z['tekst']}")
    bron = os.environ.get("STEM_BRON", "elevenlabs")
    return uit, {"soort": bron, "bestand": Path(pad).name, "knippen": verslag["manier"],
                 "onzeker": verslag.get("onzeker", [])}
