#!/usr/bin/env python3
"""Montage "echt" voor de sale-Shorts van issue #75 (Regisseur run 29, 25 nov 2026).

Wens Thijs 25 nov 11:25: alsof iemand het op zijn eigen pc opnam. Dus anders dan regisseur-2/montage2.py:
- Elk beeld komt uit de echte schermopname (scherm.mkv, 2160x1920, x11grab met de echte muis). Het paneel pixel
  voor pixel; op de robot mag worden ingezoomd ("zoom", of een split-stuk met bron_w), zodat hij het beeld vult
  (feedback Thijs 25 nov 21:40 "kan spectaculairder"). De pijl volgt het muisspoor en schaalt mee.
- Geen geluidsbed (geen zoem of brom): alleen de stem en een zacht tikje op de echte klikken uit film.json.
- Grote ondertitels per 1 tot 3 woorden, synchroon met de stem (beeld volgt stem: elke scène is zo lang als zijn zin).
- Eerste zin = de hook op het eerste beeld (thumbnail, al door de blinde test), laatste zin = een slotkaart.

    python3 montage3.py <scènes.json> <opnamemap met scherm.mkv, film.json, start.txt> <uitmap>

scènes.json: {"naam", "eerste_beeld", "slot_beeld", "zinnen": [{"tekst", "uitspraak"?, "soort": "beeld"|"scherm"|"slot",
  "stukken": [{"deel", "na" (s na het begin van dat deel), "duur"? (laatste stuk vult aan), "x" (0 of 1080)}]}]}
Uit: <naam>-geluid.mp4 en <naam>-script.json (voor synchroon.py)."""
import json
import os
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "stem"))
import stem as st  # noqa: E402

W, H, FPS = 1080, 1920, 30
SR = 48000
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
TUSSEN = 0.28          # stilte na elke zin
VOOR = 0.12            # beeld voor de eerste klank
ONDER_Y = 1330         # midden van de ondertitel (boven de knoppen van YouTube)


def lees(pad):
    return json.loads(Path(pad).read_text(encoding="utf-8"))


def stukjes(tekst, max_w=3):
    """Ondertitel in stukjes van 1 tot 3 woorden; leestekens blijven bij het woord."""
    w = tekst.split()
    uit, nu = [], []
    for x in w:
        nu.append(x)
        if len(nu) >= max_w or x[-1] in ",.:?!":
            uit.append(" ".join(nu))
            nu = []
    if nu:
        uit.append(" ".join(nu))
    return uit


def ondertitel_png(tekst, f):
    im = Image.new("RGBA", (W, 300), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    regels = [tekst]
    if d.textlength(tekst, font=f) > W - 80:
        w = tekst.split()
        h = (len(w) + 1) // 2
        regels = [" ".join(w[:h]), " ".join(w[h:])]
    y = 150 - len(regels) * 55
    for r in regels:
        x = (W - d.textlength(r, font=f)) / 2
        kleur = (255, 214, 0) if any(c.isdigit() for c in r) else (255, 255, 255)
        d.text((x, y), r, font=f, fill=kleur, stroke_width=9, stroke_fill=(10, 12, 16))
        y += 110
    return im


def deel_vf(r, label_in, label_uit):
    """Eén stuk van het scherm: [x, y, h] pixel voor pixel (1080 breed), of [x, y, h, bron_w]: een echt stuk scherm
    van bron_w breed en h*bron_w/1080 hoog, vergroot naar 1080 x h (inzoomen op de robot, wens Thijs 25 nov 21:40)."""
    x, y, h = r[:3]
    if len(r) > 3:
        bw = int(r[3])
        bh = int(round(h * bw / W))
        return f"[{label_in}]crop={bw}:{bh}:{x}:{y},scale={W}:{h}:flags=lanczos[{label_uit}]"
    return f"[{label_in}]crop={W}:{h}:{x}:{y}[{label_uit}]"


def frames_uit_scherm(mkv, van, n, x, split=None, zoom=None):
    """n beelden 1080x1920 vanaf seconde van, uitsnede vanaf x; te weinig = laatste beeld vasthouden.
    split = {"boven": [x, y, h(, bron_w)], "onder": [...]}: twee echte stukken van het scherm onder elkaar.
    zoom = [x, y, bron_w]: een echt stuk scherm (bron_w breed, 16:9 staand) vergroot tot het hele beeld."""
    vf = f"crop={W}:{H}:{x}:0,fps={FPS}"
    complex_ = False
    if zoom:
        bw = int(zoom[2])
        bh = int(round(H * bw / W))
        vf = f"fps={FPS},crop={bw}:{bh}:{zoom[0]}:{zoom[1]},scale={W}:{H}:flags=lanczos"
    if split:
        complex_ = True
        vf = (f"[0:v]fps={FPS},split[a][b];" + deel_vf(split["boven"], "a", "t") + ";" +
              deel_vf(split["onder"], "b", "o0") + f";[o0]drawbox=x=0:y=0:w={W}:h=4:color=black@0.9:t=fill[o];[t][o]vstack")
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{max(0.0, van):.3f}", "-i", str(mkv), "-frames:v", str(n),
           "-filter_complex" if complex_ else "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    data = subprocess.run(cmd, capture_output=True, check=True).stdout
    k = W * H * 3
    beelden = [data[i:i + k] for i in range(0, len(data) - k + 1, k)]
    if not beelden:
        raise SystemExit(f"FOUT: geen beelden op {van:.2f} s")
    while len(beelden) < n:
        beelden.append(beelden[-1])
    return beelden


def frames_uit_beeld(pad, n, zoom=0.04):
    im = Image.open(pad).convert("RGB").resize((W, H))
    uit = []
    for i in range(n):
        # uitsnede op subpixels: met hele pixels springt de zoom af en toe en staat hij soms stil (haperen)
        z = 1.0 + zoom * i / max(1, n - 1)
        b, h = W / z, H / z
        x0, y0 = (W - b) / 2, (H - h) / 2
        uit.append(im.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + b, y0 + h)).tobytes())
    return uit


def pijl_beeld():
    """Gewone witte muispijl met zwarte rand, 32 px hoog: zo groot als de pijl op een echt scherm van deze maat."""
    k = 4
    pts = [(0, 0), (0, 25), (6, 19), (10.5, 29), (14, 27.3), (9.7, 18), (18, 18)]
    im = Image.new("RGBA", (24 * k, 34 * k), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.polygon([(2 * k + x * k * 1.05, 2 * k + y * k * 1.05) for x, y in pts], fill=(255, 255, 255, 255),
              outline=(0, 0, 0, 255), width=int(1.6 * k))
    return im.resize((24, 34), Image.LANCZOS)


def lees_muis(pad):
    if not Path(pad).exists():
        return None
    a = np.loadtxt(pad, ndmin=2)
    return a[:, 0], a[:, 1], a[:, 2]


def muis_op(muis, t):
    tt, xx, yy = muis
    return float(np.interp(t, tt, xx)), float(np.interp(t, tt, yy))


def naar_beeld(x, y, s):
    """Schermpunt naar (punt in het 1080x1920-beeld, schaal) van dit stuk (None = buiten beeld)."""
    z = s.get("zoom")
    if z:
        f = W / z[2]
        bx, by = (x - z[0]) * f, (y - z[1]) * f
        return (bx, by, f) if 0 <= bx < W and 0 <= by < H else None
    sp = s.get("split")
    if not sp:
        cx = s.get("x", 0)
        return (x - cx, y, 1.0) if cx <= x < cx + W else None
    top = 0
    for r in (sp["boven"], sp["onder"]):
        rx, ry, rh = r[:3]
        bw = r[3] if len(r) > 3 else W
        f = W / bw
        bx, by = (x - rx) * f, (y - ry) * f
        if 0 <= bx < W and 0 <= by < rh:
            return bx, top + by, f
        top += rh
    return None


def klikgeluid():
    """Zacht muisklikje: 6 ms ruis met snelle daling, hoog gefilterd. Geen toon, geen bed."""
    rng = np.random.default_rng(7)
    n = int(0.012 * SR)
    x = rng.standard_normal(n) * np.exp(-np.arange(n) / (0.0018 * SR))
    x = np.diff(x, prepend=0.0)
    return (x / np.abs(x).max() * 0.10).astype(np.float32)


def main():
    sc, opn, uit = lees(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    uit.mkdir(parents=True, exist_ok=True)
    film = lees(opn / "film.json")
    start = float((opn / "start.txt").read_text().strip())
    mkv = opn / "scherm.mkv"
    basis = Path(sys.argv[1]).resolve().parent

    muis = lees_muis(opn / "muis.txt")
    pijl = pijl_beeld()
    zinnen = sc["zinnen"]
    wavs, info = st.maak_zinnen([{"tekst": z["tekst"], "uitspraak": z.get("uitspraak")} for z in zinnen],
                                uit / "zinnen")
    f = ImageFont.truetype(FONT, 92)

    tijd = 0.0
    lijn = []
    for k, (z, w) in enumerate(zip(zinnen, wavs)):
        lead = VOOR if k == 0 else 0.08
        duur = lead + w["duur"] + (TUSSEN if k < len(zinnen) - 1 else 1.0)
        lijn.append({"tekst": z["tekst"], "scene_start": round(tijd, 3), "scene_eind": round(tijd + duur, 3),
                     "stem_start": round(tijd + lead, 3), "stem_duur": w["duur"], "wav": w["wav"]})
        tijd += duur
    totaal = tijd
    nbeeld = int(round(totaal * FPS))

    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                            "-pix_fmt", "yuv420p", str(uit / "beeld.mp4")], stdin=subprocess.PIPE)
    kliks = []
    gemaakt = 0
    for k, (z, l) in enumerate(zip(zinnen, lijn)):
        n = int(round(l["scene_eind"] * FPS)) - gemaakt
        soort = z.get("soort", "scherm")
        if soort == "beeld":
            beelden = frames_uit_beeld(basis / sc["eerste_beeld"], n)
        elif soort == "slot":
            beelden = frames_uit_beeld(basis / sc["slot_beeld"], n, zoom=0.03)
        else:
            beelden = []
            plek = []
            stukken = z["stukken"]
            for i, s in enumerate(stukken):
                rest = n - len(beelden)
                m = rest if i == len(stukken) - 1 else min(rest, int(round(s["duur"] * FPS)))
                if m <= 0:
                    break
                van = film["delen"][s["deel"]] - start + s.get("na", 0.0)
                beelden += frames_uit_scherm(mkv, van, m, s.get("x", 0), s.get("split"), s.get("zoom"))
                for i2 in range(m):
                    p2 = naar_beeld(*muis_op(muis, start + van + i2 / FPS), s) if muis else None
                    plek.append(p2)
                for kt in film.get("kliks", []):
                    rel = kt - start - van
                    if 0 <= rel < m / FPS:
                        kliks.append(l["scene_start"] + len(beelden) / FPS - m / FPS + rel)
        # ondertitels (niet op de hook: die staat groot in het eerste beeld; slot: tekst staat op de kaart)
        laag = []
        if soort == "scherm":
            delen = stukjes(z["tekst"])
            tekens = [max(3, len(d)) for d in delen]
            t0 = l["stem_start"] - l["scene_start"]
            per = l["stem_duur"] / sum(tekens)
            acc = t0
            for d, c in zip(delen, tekens):
                laag.append((acc, acc + c * per if d != delen[-1] else n / FPS, ondertitel_png(d, f)))
                acc += c * per
        for i, b in enumerate(beelden[:n]):
            t = i / FPS
            act = [p for a, e, p in laag if a - 0.05 <= t < e]
            mp = plek[i] if soort == "scherm" and i < len(plek) else None
            if act or mp:
                im = Image.frombytes("RGB", (W, H), b)
                if mp:
                    pj = pijl if mp[2] == 1.0 else pijl.resize((int(24 * mp[2]), int(34 * mp[2])), Image.LANCZOS)
                    im.paste(pj, (int(round(mp[0] - 2 * mp[2])), int(round(mp[1] - 2 * mp[2]))), pj)
                if act:
                    im.paste(act[0], (0, z.get("ondertitel_y", ONDER_Y) - 150), act[0])
                b = im.tobytes()
            enc.stdin.write(b)
        gemaakt += n
        print(f"zin {k + 1}: {soort} {n} beelden, {l['scene_start']:.2f} tot {l['scene_eind']:.2f} s  {z['tekst']}")
    enc.stdin.close()
    enc.wait()

    # geluid: stem plus zachte klikjes, verder stilte
    mix = np.zeros(int((totaal + 0.5) * SR), np.float32)
    for l in lijn:
        x, bron_sr = st.lees_wav(l["wav"])
        x = np.interp(np.arange(0, len(x) * SR / bron_sr) * bron_sr / SR, np.arange(len(x)), x).astype(np.float32)
        i = int(l["stem_start"] * SR)
        mix[i:i + len(x)] += x[:len(mix) - i] * 0.85
    kl = klikgeluid()
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
                    "-ar", "48000", "-shortest", "-movflags", "+faststart", str(uit / f"{naam}-geluid.mp4")],
                   check=True)
    (uit / f"{naam}-script.json").write_text(json.dumps(
        {"vorm": "echt", "duur": round(totaal, 3), "stem": info, "kliks_s": [round(k, 2) for k in kliks],
         "zinnen": [{k2: v for k2, v in l.items() if k2 != "wav"} for l in lijn]}, indent=1, ensure_ascii=False))
    os.remove(uit / "beeld.mp4")
    print(f"klaar: {naam}-geluid.mp4, {totaal:.1f} s, {len(kliks)} klikjes, stem {info.get('soort')}")


if __name__ == "__main__":
    main()
