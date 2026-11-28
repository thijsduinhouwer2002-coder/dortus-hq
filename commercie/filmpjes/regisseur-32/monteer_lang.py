#!/usr/bin/env python3
"""Montage zoekvideo Click Cuts (#332, Regisseur 28 nov 2026): stem eerst, beeld volgt.

In: de opnamemap van cuts_lang.py (scherm-ruw.ts, muis.txt, film.json; opgenomen met CC_TIJDEN) en de stemmap van
tijden_lang.py (stem-lang.wav, tijden.json). De opname wachtte bij elke stap op zijn zin, dus de stem gaat er zonder
knippen onder op t=0. Erbij: de echte muispijl op de plek uit muis.txt, grote ondertitels op de gemeten zinnen, een
klein hoofdstuklabel, en een zacht tikje bij elke echte klik. Geen muziek, geen ondergrond.
Uit: <uit>.mp4 (1920x1080, 30 bps), <uit>.srt, <uit>-hoofdstukken.txt.
    python3 monteer_lang.py <opnamemap> <stemmap> <uit.mp4>
    python3 monteer_lang.py --controle <uit.mp4> <stemmap>     (whisper: begin van elke zin binnen 0,3 s)
    python3 monteer_lang.py --beeld <opnamemap> <stemmap> <sec> <uit.jpg>   (één beeld met pijl en ondertitel)"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "geluid"))
import geluid as g  # noqa: E402

W, H, FPS, SR = 1920, 1080, 30, 48000
FONT = HIER.parent / "regisseur-31" / "fonts" / "Poppins-ExtraBold.ttf"   # OFL 1.1, won de blinde test lettertype
GROOT, BREED_MAX, ONDER_Y = 52, 1660, 1036


def font(k):
    return ImageFont.truetype(str(FONT), k)


def regels(tekst, f, breed):
    d = ImageDraw.Draw(Image.new("L", (1, 1)))
    uit, nu = [], ""
    for w in tekst.split():
        p = (nu + " " + w).strip()
        if d.textlength(p, font=f) > breed and nu:
            uit.append(nu)
            nu = w
        else:
            nu = p
    return uit + [nu] if nu else uit


def ondertitel_stukken(z):
    """Lange zin in stukken van hooguit 2 regels; tijd per stuk naar het aantal tekens."""
    f = font(GROOT)
    rs = regels(z["tekst"], f, BREED_MAX)
    groepen = [rs[i:i + 2] for i in range(0, len(rs), 2)]
    if len(groepen) > 1 and len(groepen[-1]) == 1 and len(groepen[-2]) == 2 and len(rs) == 3:
        groepen = [rs[:2], rs[2:]]
    tekens = [sum(len(r) for r in gr) for gr in groepen]
    t, duur, uit = z["begin"], z["eind"] - z["begin"], []
    for gr, n in zip(groepen, tekens):
        d = duur * n / sum(tekens)
        uit.append({"regels": gr, "begin": t, "eind": t + d})
        t += d
    return uit


def tekst_png(rs):
    f = font(GROOT)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    lh = int(GROOT * 1.22)
    breed = max(d.textlength(r, font=f) for r in rs)
    hoog = lh * len(rs)
    y0 = ONDER_Y - hoog
    d.rounded_rectangle([(W - breed) / 2 - 30, y0 - 16, (W + breed) / 2 + 30, y0 + hoog + 10], radius=18,
                        fill=(12, 12, 14, 200))
    y = y0
    for r in rs:
        x = (W - d.textlength(r, font=f)) / 2
        d.text((x, y), r, font=f, fill=(255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0))
        y += lh
    return im


def label_png(nr, naam):
    f = ImageFont.truetype(str(FONT), 30)
    t = f"{nr}  {naam}"
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    b = d.textlength(t, font=f)
    x, y = 96, 150
    d.rounded_rectangle([x, y, x + b + 40, y + 52], radius=26, fill=(255, 201, 74, 235))
    d.text((x + 20, y + 7), t, font=f, fill=(20, 20, 20))
    return im


def pijl():
    """Gewone witte muispijl met zwarte rand (standaardpijl van X en Blender), punt op (2, 2), zoals montage_cuts."""
    s = 1.45 * 1.25
    pts = [(0, 0), (0, 17), (4, 13), (7, 20), (10, 19), (7, 12), (12, 12)]
    pts = [(2 + x * s, 2 + y * s) for x, y in pts]
    im = Image.new("RGBA", (44, 44), (0, 0, 0, 0))
    ImageDraw.Draw(im).polygon(pts, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)
    return im


def muis_lees(opn):
    muis = {}
    for regel in (opn / "muis.txt").read_text().split("\n"):
        d = regel.split()
        if len(d) == 3:
            muis[int(round(float(d[0]) * FPS))] = (int(d[1]), int(d[2]))
    return muis


def beelden(pad, n, van=0):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(pad), "-vf", f"select=gte(n\\,{van})", "-vsync", "0",
                          "-frames:v", str(n), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    k, laatste = W * H * 3, None
    for _ in range(n):
        b = p.stdout.read(k)
        if len(b) < k:
            b = laatste
        laatste = b
        yield b
    p.stdout.close()


class Lagen:
    def __init__(self, tijden):
        self.subs = [s for z in tijden["zinnen"] for s in ondertitel_stukken(z)]
        self.hst = [(i + 1, h["naam"], h["begin"]) for i, h in enumerate(tijden["hoofdstukken"])]
        self.cache = {}

    def op(self, t):
        uit = []
        for i, s in enumerate(self.subs):
            if s["begin"] <= t < s["eind"] + 0.12:
                if ("s", i) not in self.cache:
                    self.cache[("s", i)] = tekst_png(s["regels"])
                uit.append(self.cache[("s", i)])
                break
        for nr, naam, b in self.hst[1:]:   # hoofdstuk 1 is de vraag zelf: geen label
            if b - 0.1 <= t < b + 2.8:
                if ("h", nr) not in self.cache:
                    self.cache[("h", nr)] = label_png(nr - 1, naam)
                uit.append(self.cache[("h", nr)])
        return uit


def maak_beeld(b, i, muis, laatst, lagen, pl):
    im = Image.frombytes("RGB", (W, H), b).convert("RGBA")
    for laag in lagen.op(i / FPS):
        im.alpha_composite(laag)
    m = muis.get(i, laatst)
    if m:
        im.alpha_composite(pl, (max(0, min(W - 44, m[0] - 2)), max(0, min(H - 44, m[1] - 2))))
    return im.convert("RGB"), m


def srt_tijd(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def main():
    opn, stemmap, uit = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    tijden = json.loads((stemmap / "tijden.json").read_text())
    film = json.loads((opn / "film.json").read_text())
    n = int(round(tijden["lengte"] * FPS))
    muis, lagen, pl = muis_lees(opn), Lagen(tijden), pijl()
    tmp = uit.with_suffix(".beeld.mp4")
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                            "-pix_fmt", "yuv420p", "-r", str(FPS), str(tmp)], stdin=subprocess.PIPE)
    laatst = None
    for i, b in enumerate(beelden(opn / "scherm-ruw.ts", n)):
        im, laatst = maak_beeld(b, i, muis, laatst, lagen, pl)
        enc.stdin.write(im.tobytes())
    enc.stdin.close()
    enc.wait()
    # geluid: alleen de stem en een zacht tikje bij elke echte klik
    ruw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(stemmap / "stem-lang.wav"), "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    sp = np.frombuffer(ruw, np.float32)
    ns = n * SR // FPS
    mix = np.zeros(ns, np.float32)
    mix[:min(ns, len(sp))] = sp[:ns]
    for kt in film["kliks"]:
        g.plak(mix, kt, g.tik() * 0.8)
    fo = int(0.6 * SR)
    mix[-fo:] *= np.linspace(1, 0, fo)
    st = np.stack([mix, mix], axis=1)
    wav = uit.with_suffix(".wav")
    with wave.open(str(wav), "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes((np.clip(st, -0.98, 0.98) * 32767).astype("<i2").tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-ar", "48000", "-t", f"{n / FPS:.3f}", "-movflags", "+faststart", str(uit)], check=True)
    tmp.unlink()
    wav.unlink()
    srt = []
    for k, s in enumerate(lagen.subs, 1):
        srt.append(f"{k}\n{srt_tijd(s['begin'])} --> {srt_tijd(s['eind'])}\n" + "\n".join(s["regels"]) + "\n")
    uit.with_suffix(".srt").write_text("\n".join(srt))
    hs = [f"{int(h['begin'] if i else 0) // 60}:{int(h['begin'] if i else 0) % 60:02d} {h['naam']}"
          for i, h in enumerate(tijden["hoofdstukken"])]
    Path(str(uit.with_suffix("")) + "-hoofdstukken.txt").write_text("\n".join(hs) + "\n")
    print(json.dumps({"duur": round(n / FPS, 2), "kliks": len(film["kliks"]), "vangnet": film["vangnet"],
                      "laat": film.get("laat", []), "hoofdstukken": hs, "stem": tijden["stem"].get("soort")}))


def controle():
    """Whisper hoort de klare film; per zin het eerste woord tegen het begin in tijden.json (moet binnen 0,3 s)."""
    import difflib
    import re
    from faster_whisper import WhisperModel
    mp4, stemmap = Path(sys.argv[2]), Path(sys.argv[3])
    tijden = json.loads((stemmap / "tijden.json").read_text())
    ruw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(mp4), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(ruw, np.float32)
    seg, _ = WhisperModel("small.en", compute_type="int8").transcribe(x, word_timestamps=True, language="en")
    ws = [(re.sub(r"[^a-z0-9]", "", w.word.lower()), w.start) for s in seg for w in s.words]
    ws = [w for w in ws if w[0]]
    script = []
    for i, z in enumerate(tijden["zinnen"]):
        for j, w in enumerate(z["tekst"].split()):
            w = re.sub(r"[^a-z0-9]", "", w.lower())
            if w:
                script.append((w, i, j))
    sm = difflib.SequenceMatcher(a=[s[0] for s in script], b=[w[0] for w in ws], autojunk=False)
    eerste = {}
    for blok in sm.get_matching_blocks():
        for k in range(blok.size):
            w, i, j = script[blok.a + k]
            if i not in eerste or j < eerste[i][0]:
                eerste[i] = (j, ws[blok.b + k][1])
    # whisper zegt welk woord waar ongeveer valt; het echte begin is waar de klank na een stil stuk opkomt
    # (ruwe woordtijden van whisper wijken tot ±0,5 s af, zie stem/LEESMIJ.md)
    k = 160   # 10 ms bij 16 kHz
    rms = np.sqrt(np.convolve(x.astype(np.float64) ** 2, np.ones(3 * k) / (3 * k), mode="same")[::k])
    drempel = 0.2 * np.percentile(rms, 95)

    def opkomst(t):
        """De opkomst in [t-0,6, t+0,6] met het langste stille stuk ervoor (de pauze tussen zinnen wint van een
        korte stilte binnen een zin)."""
        a_, b_ = max(1, int((t - 0.6) * 100)), min(len(rms) - 1, int((t + 0.6) * 100))
        beste, lang = t, 0
        for j in range(a_, b_):
            if rms[j] > drempel and rms[j - 1] <= drempel:
                n = 0
                while j - 1 - n >= 0 and rms[j - 1 - n] <= drempel:
                    n += 1
                if n > lang:
                    beste, lang = j / 100, n
        return beste
    uitslag, fout = [], 0
    for i, z in enumerate(tijden["zinnen"]):
        if i not in eerste or eerste[i][0] > 2:
            uitslag.append([z["nr"], None])
            continue
        verschil = round(opkomst(float(eerste[i][1])) - z["begin"], 2)
        fout += int(abs(verschil) > 0.3)
        uitslag.append([z["nr"], verschil])
    gemeten = [abs(u[1]) for u in uitslag if u[1] is not None]
    print(json.dumps({"zinnen": len(uitslag), "gemeten": len(gemeten), "buiten_0_3": fout,
                      "grootste": max(gemeten) if gemeten else None, "per_zin": uitslag}))
    sys.exit(1 if fout or len(gemeten) < len(uitslag) - 2 else 0)


def een_beeld():
    opn, stemmap, sec, uit = Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4]), Path(sys.argv[5])
    tijden = json.loads((stemmap / "tijden.json").read_text())
    i = int(round(sec * FPS))
    muis = muis_lees(opn)
    b = next(beelden(opn / "scherm-ruw.ts", 1, van=i))
    im, _ = maak_beeld(b, i, muis, muis.get(i), Lagen(tijden), pijl())
    im.save(uit, quality=90)


if __name__ == "__main__":
    {"--controle": controle, "--beeld": een_beeld}.get(sys.argv[1], main)()
