#!/usr/bin/env python3
"""Montage in procesvorm voor de sale-Short van issue #159 (Regisseur, 26 nov 2026).

Opbouw en tempo van het voorbeeld dat Thijs stuurde (overgangen gemeten door de hoofdchat, GEZIEN): elke 0,5 tot 1,4 s
een nieuw stuk uit de echte schermopname (scherm.mkv van proces.py), van grijze robot naar kleur, tijdlijn en de klik
op Render Animation; daarna ±6 s de eindfilm (eind.mp4) met in de laatste seconden de saleregel. Eén vaste korte tekst
bovenin de eerste ±9 s. Geluid: alleen muziek (rechtenvrij, bron en licentie in het scènebestand) plus zachte klikjes
op de echte kliks. Geen stem, geen zoem.
    python3 montage_proces.py <scènes.json> <opnamemap: scherm.mkv film.json start.txt muis.txt eind.mp4> <uitmap>"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "regisseur-26"))
from montage3 import frames_uit_scherm, klikgeluid, lees_muis, muis_op, naar_beeld, pijl_beeld  # noqa: E402

W, H, FPS, SR = 1080, 1920, 30, 48000
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FONT2 = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"


def tekst_png(regels, grootte, y_mid, font=FONT, kleur=(255, 255, 255)):
    f = ImageFont.truetype(font, grootte)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    lh = int(grootte * 1.18)
    y = y_mid - lh * len(regels) / 2
    for r in regels:
        x = (W - d.textlength(r, font=f)) / 2
        d.text((x, y), r, font=f, fill=kleur, stroke_width=max(4, grootte // 11), stroke_fill=(8, 10, 14))
        y += lh
    return im


def label_png(tekst, y_mid, grootte=64):
    """Korte staptekst in een donker pilletje (Daan #193: bij elke stap zeggen wat er gebeurt, leesbaar op een telefoon)."""
    f = ImageFont.truetype(FONT, grootte)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    tw = d.textlength(tekst, font=f)
    px, py = 38, 22
    x0, y0 = (W - tw) / 2 - px, y_mid - grootte / 2 - py
    d.rounded_rectangle((x0, y0, x0 + tw + 2 * px, y0 + grootte + 2 * py + 8), radius=34, fill=(12, 14, 20, 225))
    d.text(((W - tw) / 2, y0 + py), tekst, font=f, fill=(255, 255, 255))
    return im


def ring_png(s, rect):
    """Gele rand om een echte knop: rect = [x, y, w, h] in schermpunten, omgerekend naar dit stuk."""
    a = naar_beeld(rect[0], rect[1], s)
    b = naar_beeld(rect[0] + rect[2], rect[1] + rect[3], s)
    if not a or not b:
        return None
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((a[0] - 10, a[1] - 10, b[0] + 10, b[1] + 10), radius=14,
                                         outline=(255, 206, 40, 255), width=8)
    return im


def frames_uit_film(pad, n, start=0.0):
    data = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-i", str(pad), "-frames:v", str(n),
                           "-vf", f"fps={FPS},scale={W}:{H}:flags=lanczos", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                          capture_output=True, check=True).stdout
    k = W * H * 3
    b = [data[i:i + k] for i in range(0, len(data) - k + 1, k)]
    while len(b) < n:
        b.append(b[-1])
    return b


def main():
    sc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    opn, uit = Path(sys.argv[2]), Path(sys.argv[3])
    uit.mkdir(parents=True, exist_ok=True)
    film = json.loads((opn / "film.json").read_text())
    start = float((opn / "start.txt").read_text().strip())
    mkv = opn / "scherm.mkv"
    muis = lees_muis(opn / "muis.txt")
    pijl = pijl_beeld()
    boven = tekst_png(sc["boven"], 70, sc.get("boven_y", 250))
    slot = tekst_png(sc["slot"], 74, sc.get("slot_y", 1250), kleur=(255, 255, 255))
    totaal = sum(s["duur"] for s in sc["stukken"]) + sc["eind_duur"]
    nbeeld = int(round(totaal * FPS))
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(uit / "beeld.mp4")], stdin=subprocess.PIPE)
    kliks, overgangen, gemaakt = [], [], 0
    eind_t = 0.0
    for s in sc["stukken"]:
        eind_t += s["duur"]
        n = int(round(eind_t * FPS)) - gemaakt
        van = film["delen"][s["deel"]] - start + s.get("na", 0.0)
        beelden = frames_uit_scherm(mkv, van, n, s.get("x", 0), s.get("split"), s.get("zoom"))
        overgangen.append(round(gemaakt / FPS, 2))
        lab = label_png(s["label"], s.get("label_y", sc.get("label_y", 1560))) if s.get("label") else None
        ring = ring_png(s, s["ring"]) if s.get("ring") else None
        for kt in ([] if s.get("geen_muis") else film.get("kliks", [])):
            rel = kt - start - van
            if 0 <= rel < n / FPS:
                kliks.append(gemaakt / FPS + rel)
        for i, b in enumerate(beelden[:n]):
            t = (gemaakt + i) / FPS
            im = Image.frombytes("RGB", (W, H), b)
            if ring and i / FPS < s.get("ring_tot", 99.0):
                im.paste(ring, (0, 0), ring)
            mp = naar_beeld(*muis_op(muis, start + van + i / FPS), s) if muis and not s.get("geen_muis") else None
            if mp:
                pj = pijl if mp[2] == 1.0 else pijl.resize((int(24 * mp[2]), int(34 * mp[2])), Image.LANCZOS)
                im.paste(pj, (int(round(mp[0] - 2 * mp[2])), int(round(mp[1] - 2 * mp[2]))), pj)
            if t < sc["boven_tot"]:
                im.paste(boven, (0, 0), boven)
            elif lab and i / FPS < s.get("label_tot", 99.0):
                im.paste(lab, (0, 0), lab)
            enc.stdin.write(im.tobytes())
        gemaakt += n
        print(f"{overgangen[-1]:6.2f} s  {s['deel']:<14} +{s.get('na', 0.0):.1f}  {n} beelden")
    n = nbeeld - gemaakt
    overgangen.append(round(gemaakt / FPS, 2))
    eind = frames_uit_film(opn / "eind.mp4", n, sc.get("eind_start", 0.0))
    slot_van = n - int(sc["slot_duur"] * FPS)
    zoom = float(sc.get("eind_zoom", 1.0))   # langzaam inzoomen op de eigen render (proef 7: de camera stond stil)
    for i, b in enumerate(eind):
        if zoom > 1.0:
            f = 1.0 + (zoom - 1.0) * (i / max(1, n - 1))
            bw, bh = W / f, H / f
            x0, y0 = (W - bw) / 2, (H - bh) * 0.42
            b = Image.frombytes("RGB", (W, H), b).resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + bw, y0 + bh)).tobytes()
        if i >= slot_van:
            im = Image.frombytes("RGB", (W, H), b)
            a = min(1.0, (i - slot_van) / 8.0)
            laag = slot.copy()
            laag.putalpha(laag.getchannel("A").point(lambda v: int(v * a)))
            im.paste(laag, (0, 0), laag)
            b = im.tobytes()
        enc.stdin.write(b)
    print(f"{overgangen[-1]:6.2f} s  eindfilm  {n} beelden")
    enc.stdin.close()
    enc.wait()

    # geluid: muziek (zacht in en uit) plus zachte klikjes op de echte kliks
    dec = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(sc["muziek_start"]), "-i", str(opn / sc["muziek"]),
                          "-t", f"{totaal + 0.2:.2f}", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    mu = np.frombuffer(dec, np.float32).copy()
    mix = np.zeros(int((totaal + 0.2) * SR), np.float32)
    mix[:len(mu)] += mu[:len(mix)] * 0.8
    fi, fo = int(0.25 * SR), int(1.6 * SR)
    mix[:fi] *= np.linspace(0, 1, fi)
    e = int(totaal * SR)
    mix[e - fo:e] *= np.linspace(1, 0, fo)
    mix[e:] = 0
    kl = klikgeluid() * 2.0
    for kt in kliks:
        i = int(kt * SR)
        if 0 <= i < len(mix) - len(kl):
            mix[i:i + len(kl)] += kl
    mix = np.clip(mix, -0.98, 0.98)
    with wave.open(str(uit / "geluid.wav"), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes((mix * 32767).astype("<i2").tobytes())
    naam = sc["naam"]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(uit / "beeld.mp4"), "-i", str(uit / "geluid.wav"),
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                    "-ar", "48000", "-shortest", "-movflags", "+faststart", str(uit / f"{naam}.mp4")], check=True)
    (uit / f"{naam}-montage.json").write_text(json.dumps(
        {"duur": round(totaal, 2), "overgangen_s": overgangen, "kliks_s": [round(k, 2) for k in kliks],
         "muziek": sc["muziek_bron"]}, indent=1, ensure_ascii=False))
    (uit / "beeld.mp4").unlink()
    print(f"klaar: {naam}.mp4, {totaal:.1f} s, {len(overgangen)} stukken, {len(kliks)} klikjes")


if __name__ == "__main__":
    main()
