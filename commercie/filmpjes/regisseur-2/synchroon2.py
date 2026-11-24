#!/usr/bin/env python3
"""Kopie voor regisseur-2 (vorm groot: ander tekstvak). Synchroon-controle: valt elke gesproken zin binnen 0,3 s van zijn scène? (opdracht hoofdchat 23 nov 2026)

    python3 synchroon.py <film.mp4> <script.json van montage.py> <uitmap>

Twee metingen uit het klare mp4-bestand zelf, los van de tijden die montage.py opschreef:
1. Stem: faster-whisper maakt een transcript met tijden per woord (audio als numpy-array). Per zin uit het script
   zoeken we het eerste woord in het transcript (difflib over de woorden) en nemen we de begintijd.
2. Beeld: per beeld het verschil in het tekstvak (label, kop, zin); een sprong = een nieuwe scène.
Whisper vindt de zin en zijn eerste woord; de woordtijden van whisper wijken soms 0,2 tot 0,5 s af, dus de begintijd
wordt verfijnd tot het begin van de klank (energie boven 1 kHz na een stilte) binnen 0,6 s van die woordtijd.
Per zin: verschil = begin van de stem min begin van de scène (beeld). Goed als |verschil| <= 0,3 s.
Uit: transcript.json, transcript.srt, synchroon.json, synchroon.md. Exit 1 als een zin buiten 0,3 s valt."""
import difflib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

GRENS = 0.3
GETALLEN = {"0": "zero", "120": "one hundred and twenty", "3mf": "three m f", "9": "nine"}


def woorden(tekst):
    uit = []
    for w in re.findall(r"[a-z0-9']+", tekst.lower().replace("°", " degrees ")):
        w = w.replace("'", "")
        uit += GETALLEN.get(w, w).split()
    return [stam(w) for w in uit if w]


def stam(w):
    """Grove stam, zodat "measured" en "measure" gelijk tellen (whisper hoort soms een uitgang anders)."""
    for eind in ("ed", "e", "s"):
        if len(w) > 3 and w.endswith(eind):
            w = w[:-len(eind)]
    return w


def audio(mp4):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(mp4), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).copy()


def klankbegin(a, sr=16000):
    """Per 10 ms of er stem klinkt: energie boven 1 kHz (de ondergrond van geluid.py zit onder 600 Hz)."""
    spec = np.fft.rfft(a)
    f = np.fft.rfftfreq(len(a), 1 / sr)
    spec[f < 1000] = 0
    hp = np.fft.irfft(spec, len(a))
    k = sr // 100
    n = len(hp) // k
    db = 10 * np.log10((hp[:n * k].reshape(n, k) ** 2).mean(axis=1) + 1e-12)
    laag, hoog = np.percentile(db, 20), np.percentile(db, 90)
    return db > laag + 0.35 * (hoog - laag)


def verfijn(aan, t):
    """Begin van de klank het dichtst bij whisper-tijd t, binnen 0,6 s ervoor of erna.
    Regisseur 2: eerst gezocht na minstens 300 ms stil (tussen twee zinnen zit 350 ms stilte, binnen een zin
    zijn de pauzes korter), pas daarna na 150 ms stil zoals in het origineel. Reden: whisper legt het eerste woord
    van een nieuw stuk soms 0,4 tot 0,5 s te vroeg, midden in de vorige zin (run 45187577798, zin 8), en het
    origineel zocht maar 0,4 s vooruit."""
    if t is None:
        return None
    i = int(round(t * 100))
    for stil in (30, 15):
        beste = None
        for j in range(max(stil, i - 60), min(len(aan) - 5, i + 61)):
            if aan[j] and aan[j:j + 5].all() and not aan[j - stil:j].any():
                if beste is None or abs(j - i) < abs(beste - i):
                    beste = j
        if beste is not None:
            return round(beste / 100, 3)
    return None


def scenewissels(mp4, vak, breed, hoog):
    """Tijden (s) waarop het tekstvak ineens verandert. vak = (x0, y0, x1, y1) in pixels van de film."""
    s = 4  # op een kwart van de grootte meten
    w, h = breed // s, hoog // s
    r = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(mp4), "-vf", f"scale={w}:{h}", "-f", "rawvideo",
                          "-pix_fmt", "gray", "-"], stdout=subprocess.PIPE)
    x0, y0, x1, y1 = [v // s for v in vak]
    vorig, n, verschil = None, 0, []
    while True:
        buf = r.stdout.read(w * h)
        if len(buf) < w * h:
            break
        b = np.frombuffer(buf, np.uint8).reshape(h, w)[y0:y1, x0:x1].astype(np.float32)
        verschil.append(0.0 if vorig is None else float(np.abs(b - vorig).mean()))
        vorig = b
        n += 1
    r.wait()
    v = np.array(verschil)
    drempel = max(1.5, float(np.percentile(v, 99)) * 0.25)
    wissel = [i / 30.0 for i in range(1, len(v)) if v[i] > drempel and v[i - 1] <= drempel and
              (i < 3 or v[i - 3:i].max() <= drempel)]
    return wissel, drempel


def main():
    mp4, scr, uitmap = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text()), Path(sys.argv[3])
    uitmap.mkdir(parents=True, exist_ok=True)
    from faster_whisper import WhisperModel
    model_naam = os.environ.get("WHISPER_MODEL", "small.en")
    model = WhisperModel(model_naam, device="cpu", compute_type="int8")
    geluid = audio(mp4)
    aan = klankbegin(geluid)
    segs, _ = model.transcribe(geluid, language=os.environ.get("WHISPER_TAAL", "en"), word_timestamps=True, beam_size=5,
                               condition_on_previous_text=False)
    segs = list(segs)
    tw = []
    for sg in segs:
        for w in sg.words:
            for d in woorden(w.word):
                tw.append({"w": d, "start": round(float(w.start), 3), "eind": round(float(w.end), 3)})
    (uitmap / "transcript.json").write_text(json.dumps(
        {"model": f"faster-whisper {model_naam}", "segmenten": [{"start": round(float(s.start), 2), "eind": round(float(s.end), 2),
         "tekst": s.text.strip()} for s in segs], "woorden": tw}, indent=1, ensure_ascii=False))

    def ts(x):
        return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{int(round((x % 1) * 1000)) % 1000:03d}"
    (uitmap / "transcript.srt").write_text("".join(f"{i + 1}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n\n"
                                                    for i, s in enumerate(segs)))

    # zinnen uit het script naast de woorden van whisper leggen
    sw, eigenaar = [], []
    for k, z in enumerate(scr["zinnen"]):
        for d in woorden(z["tekst"]):
            sw.append(d)
            eigenaar.append(k)
    sm = difflib.SequenceMatcher(a=sw, b=[t["w"] for t in tw], autojunk=False)
    paar = {}
    for blok in sm.get_matching_blocks():
        for j in range(blok.size):
            paar[blok.a + j] = blok.b + j
    staand = scr["vorm"] in ("staand", "groot")
    breed, hoog = (1080, 1920) if staand else (1920, 1080)
    # vorm groot (regisseur-2): label en kop staan in de bovenste 330 pixels, daaronder loopt het beeld
    vak = (40, 70, 1040, 330) if scr["vorm"] == "groot" else (40, 150, 1040, 630) if staand else (1300, 200, 1900, 760)
    wissels, drempel = scenewissels(mp4, vak, breed, hoog)
    rijen, fout = [], 0
    for k, z in enumerate(scr["zinnen"]):
        idx = [i for i, e in enumerate(eigenaar) if e == k]
        gevonden = [(i, paar[i]) for i in idx if i in paar]
        eerste_goed = bool(gevonden) and gevonden[0][0] <= idx[0] + 1   # eerste of tweede woord gevonden
        st_w = tw[gevonden[0][1]]["start"] if gevonden else None
        st = verfijn(aan, st_w) if st_w is not None else None
        st = st if st is not None else st_w
        en = tw[gevonden[-1][1]]["eind"] if gevonden else None
        if k == 0:
            sc = 0.0
        else:
            dichtbij = [w for w in wissels if abs(w - z["scene_start"]) < 1.0]
            sc = min(dichtbij, key=lambda w: abs(w - z["scene_start"])) if dichtbij else None
        verschil = None if st is None or sc is None else round(st - sc, 3)
        goed = verschil is not None and abs(verschil) <= GRENS and eerste_goed and en is not None and en <= z["scene_eind"] + 0.15
        if k == 0:  # eerste zin: geen wissel, beeld begint op 0; stem moet binnen 0,3 s na het begin komen
            goed = st is not None and st <= GRENS + 0.05 and eerste_goed
        fout += 0 if goed else 1
        rijen.append({"nr": k + 1, "tekst": z["tekst"], "scene_gemeten": sc, "scene_gepland": z["scene_start"],
                      "stem_whisper": st_w, "stem_begin_klank": st, "stem_eind_whisper": en, "stem_gepland": z["stem_start"],
                      "verschil_s": verschil, "eerste_woord_gevonden": bool(eerste_goed),
                      "woorden_gevonden": f"{len(gevonden)}/{len(idx)}", "goed": bool(goed)})
    gemeten = [abs(r["verschil_s"]) for r in rijen if r["verschil_s"] is not None]
    samen = {"film": mp4.name, "grens_s": GRENS, "model": f"faster-whisper {model_naam}", "drempel_beeld": round(drempel, 2),
             "wissels_beeld_s": [round(w, 3) for w in wissels], "max_verschil_s": max(gemeten) if gemeten else None,
             "gemiddeld_verschil_s": round(float(np.mean(gemeten)), 3) if gemeten else None,
             "zinnen_goed": len(rijen) - fout, "zinnen": rijen, "uitslag": "GOED" if fout == 0 else "FOUT"}
    (uitmap / "synchroon.json").write_text(json.dumps(samen, indent=1, ensure_ascii=False))
    md = [f"# Synchroon-meting {mp4.name}", "",
          f"Gemeten uit het mp4-bestand (GEZIEN): stem met {samen['model']} (woordtijden), scène uit de sprong in het tekstvak.",
          f"Uitslag: **{samen['uitslag']}**, {samen['zinnen_goed']} van {len(rijen)} zinnen binnen {GRENS} s; "
          f"grootste verschil {samen['max_verschil_s']} s, gemiddeld {samen['gemiddeld_verschil_s']} s.", "",
          "Stem = woordtijd van whisper, verfijnd tot het begin van de klank (energie boven 1 kHz, na een stilte) binnen 0,6 s van die woordtijd.", "",
          "| Zin | Scène (beeld) s | Stem whisper s | Stem begin klank s | Verschil s | Woorden | Goed | Tekst |", "|---|---|---|---|---|---|---|---|"]
    for r in rijen:
        sg = None if r['scene_gemeten'] is None else round(r['scene_gemeten'], 2)
        md.append(f"| {r['nr']} | {sg} | {r['stem_whisper']} | {r['stem_begin_klank']} | {r['verschil_s']} | {r['woorden_gevonden']} | "
                  f"{'ja' if r['goed'] else 'NEE'} | {r['tekst']} |")
    (uitmap / "synchroon.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    sys.exit(0 if fout == 0 else 1)


if __name__ == "__main__":
    main()
