#!/usr/bin/env python3
"""Geluidscontrole voor filmpjes: weigert een mp4 zonder hoorbaar geluid.

R6 roestronde, 18 nov 2026 (filmpjes gingen stil live op TikTok en Shorts, Joris 17 nov 06:50).

Gebruik:
  python3 organisatie/controle/geluid_check.py film1.mp4 [film2.mp4 ...]

Faalt (exit 1) als een filmpje:
  1. geen geluidsspoor heeft (ffprobe vindt geen audiostream);
  2. een geluidsspoor heeft dat korter is dan 90% van het beeld (een tikje van 1 s onder 15 s beeld);
  3. vrijwel stil is: gemiddeld (ffmpeg volumedetect, mean_volume) onder -50 dB, of
     het hardste punt (max_volume) onder -30 dB.

Waarom deze grenzen:
- Onze eigen filmpjes met geluid zitten op -19 tot -14 LUFS (toets.py van filmpjes-geluid); een
  gewone Short met muziek of stem meet in volumedetect gemiddeld ongeveer -15 tot -30 dB. Digitale
  stilte geeft -91 dB, een leeg spoor met alleen ruis -60 tot -80 dB. -50 dB ligt ruim 20 dB onder
  zacht maar hoorbaar geluid en ruim boven een leeg spoor, dus het vangt stilte zonder rustige
  achtergrondmuziek te weigeren. Het is ook de grens die toets.py al gebruikt voor een "stil gat".
- max_volume onder -30 dB: dan is zelfs het hardste moment nauwelijks te horen op een telefoon.
Nodig: ffprobe en ffmpeg in het pad.
"""
import json
import re
import subprocess
import sys

GRENS_GEMIDDELD = -50.0  # dB, volumedetect mean_volume
GRENS_PIEK = -30.0  # dB, volumedetect max_volume
MIN_DEEL = 0.9  # geluid minstens 90% van de beeldduur


def probe(pad):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,duration:format=duration",
                        "-of", "json", pad], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffprobe kan het bestand niet lezen: {r.stderr.strip()[:200]}")
    return json.loads(r.stdout)


def duur(stream, fmt):
    for v in (stream.get("duration"), fmt.get("duration")):
        try:
            return float(v)
        except (TypeError, ValueError):
            continue
    return None


def volume(pad):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", pad, "-map", "0:a:0", "-af", "volumedetect",
                        "-f", "null", "-"], capture_output=True, text=True)
    gem = re.search(r"mean_volume:\s*(-?[\d.]+|-inf) dB", r.stderr)
    piek = re.search(r"max_volume:\s*(-?[\d.]+|-inf) dB", r.stderr)
    f = lambda m: float("-inf") if not m or m.group(1) == "-inf" else float(m.group(1))  # noqa: E731
    return f(gem), f(piek)


def controleer(pad):
    """Geeft (goed, uitleg)."""
    try:
        info = probe(pad)
    except (RuntimeError, ValueError) as e:
        return False, str(e)
    fmt = info.get("format", {})
    beeld = [s for s in info.get("streams", []) if s.get("codec_type") == "video"]
    geluid = [s for s in info.get("streams", []) if s.get("codec_type") == "audio"]
    if not geluid:
        return False, "geen geluidsspoor"
    db = duur(beeld[0], fmt) if beeld else None
    da = duur(geluid[0], fmt)
    if db and da is not None and da < MIN_DEEL * db:
        return False, f"geluid duurt {da:.2f} s, beeld {db:.2f} s (minder dan {MIN_DEEL:.0%})"
    gem, piek = volume(pad)
    tekst = f"gemiddeld {gem:.1f} dB, piek {piek:.1f} dB"
    if gem < GRENS_GEMIDDELD:
        return False, f"vrijwel stil: {tekst} (grens gemiddeld {GRENS_GEMIDDELD:.0f} dB)"
    if piek < GRENS_PIEK:
        return False, f"te zacht: {tekst} (grens piek {GRENS_PIEK:.0f} dB)"
    return True, tekst


def main(paden):
    if not paden:
        print(__doc__)
        return 2
    fout = 0
    for p in paden:
        goed, uitleg = controleer(p)
        print(f"{'GOED' if goed else 'FOUT'}: {p}: {uitleg}")
        fout += not goed
    if fout:
        print(f"{fout} van {len(paden)} filmpjes zonder hoorbaar geluid: niet uploaden of inplannen.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
