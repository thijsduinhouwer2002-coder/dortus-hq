#!/usr/bin/env python3
"""Stem eerst, beeld volgt (#332, Regisseur 28 nov 2026).

Leest de 24 zinnen uit voorlees.md, maakt per zin een wav (STEM_MP3 gezet: de ElevenLabs-opname van de hoofdchat,
geknipt met stem/splits.py; anders Kokoro als tijdelijke proef, nooit voor keuring), en legt ze achter elkaar met een
vaste pauze (PAUZE tussen zinnen, HOOFDSTUK_PAUZE vóór een nieuw hoofdstuk). Uit:
  <uit>/stem-lang.wav   de stem zoals hij in de film komt (begint op VOORLOOP s)
  <uit>/tijden.json     per zin begin en eind in filmtijd, plus hoofdstukken
De opname (cuts_lang.py met CC_TIJDEN=<uit>/tijden.json) wacht bij elke stap op zijn zin, dus beeld en stem lopen
gelijk zonder te knippen. De montage (monteer_lang.py) legt stem-lang.wav op t=0 onder de opname.
    python3 tijden_lang.py <uitmap>"""
import json
import os
import re
import sys
from pathlib import Path

import numpy as np

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "stem"))
import stem  # noqa: E402

VOORLOOP = float(os.environ.get("VOORLOOP", "0.35"))
PAUZE = float(os.environ.get("PAUZE", "0.45"))
HOOFDSTUK_PAUZE = float(os.environ.get("HOOFDSTUK_PAUZE", "0.9"))
STAART = float(os.environ.get("STAART", "2.4"))


def lees_zinnen(pad=HIER / "voorlees.md"):
    zinnen, hoofdstuk = [], None
    for regel in pad.read_text().split("\n"):
        if regel.startswith("## Bron"):
            break
        m = re.match(r"\*\*(?:\d+:\d+ )?(.+?)\*\*$", regel.strip())
        if m:
            hoofdstuk = m.group(1)
            continue
        m = re.match(r"(\d+)\. (.+)$", regel.strip())
        if m and hoofdstuk:
            zinnen.append({"nr": int(m.group(1)), "tekst": m.group(2).strip(), "hoofdstuk": hoofdstuk})
    assert [z["nr"] for z in zinnen] == list(range(1, len(zinnen) + 1)), "zinnen niet op volgorde"
    return zinnen


def main():
    uit = Path(sys.argv[1])
    uit.mkdir(parents=True, exist_ok=True)
    zinnen = lees_zinnen()
    wavs, info = stem.maak_zinnen(zinnen, uit / "zinnen")
    t = VOORLOOP
    stukken = [np.zeros(int(VOORLOOP * stem.SR), np.float32)]
    for i, (z, w) in enumerate(zip(zinnen, wavs)):
        if i:
            p = HOOFDSTUK_PAUZE if z["hoofdstuk"] != zinnen[i - 1]["hoofdstuk"] else PAUZE
            stukken.append(np.zeros(int(round(p * stem.SR)), np.float32))
            t += p
        x = stem.lees_wav(w["wav"])[0].astype(np.float32)
        z["begin"], z["eind"] = round(t, 3), round(t + len(x) / stem.SR, 3)
        stukken.append(x)
        t += len(x) / stem.SR
    stukken.append(np.zeros(int(STAART * stem.SR), np.float32))
    x = np.concatenate(stukken) * 0.85
    stem.schrijf_wav(uit / "stem-lang.wav", x)
    lengte = round(len(x) / stem.SR, 3)
    hoofdstukken = []
    for z in zinnen:
        if not hoofdstukken or hoofdstukken[-1]["naam"] != z["hoofdstuk"]:
            hoofdstukken.append({"naam": z["hoofdstuk"], "begin": z["begin"]})
    (uit / "tijden.json").write_text(json.dumps({"stem": info, "lengte": lengte, "zinnen": zinnen,
                                                 "hoofdstukken": hoofdstukken}, indent=1, ensure_ascii=False))
    print(f"tijden: {len(zinnen)} zinnen, film {lengte:.1f} s, stem {info.get('soort')}")


if __name__ == "__main__":
    main()
