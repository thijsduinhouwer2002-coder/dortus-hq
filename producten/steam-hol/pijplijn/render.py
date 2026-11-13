"""3D-pijplijn van Het Hol (Bram, 13 nov 2026): van een .py-model in Blender naar een blad voor Godot.

Draai:  python3 render.py [naam ...]      (zonder naam: alle sprites uit sprites.json)
Omgeving:
  BPY_PYTHON   python met het pakket bpy (standaard: python3), bv. ~/bpyenv/bin/python
  HOL_SNEL=1   proefstand: kwart van de samples (sneller, niet voor het spel)

Per sprite:
 1. het model draait in Blender (bpy) met HOL_FRAMES (rust, plat, ...) en HOL_RUIMTE (ruimer kader);
    gedeeld.render maakt dan per beeld een PNG met doorzichtige achtergrond.
 2. strak bijsnijden op wat er in alle beelden staat (alfa), schalen zodat het eerste beeld in de cel past
    (alle beelden dezelfde schaal, dus plat is echt breder), onderkant op de vloer.
 3. verkleinen met Lanczos op voorvermenigvuldigde alfa (geen donkere randjes), naast elkaar in één blad.
 4. schrijft godot/kunst/3d/<naam>.png, <naam>.png.import (lineair, mipmaps) en sprites.json met maten:
    cel_px (breedte, hoogte in bladpixels), px (bladpixels per spelpixel), anker_x (waar x = 0 van het model
    staat in de cel), top (bovenste rij met inhoud per beeld, in spelpixels), frames (namen in volgorde).
Ook een vergroting naast ware grootte in pijplijn/uit/ (niet in git) om naar te kijken.
"""
import json, os, subprocess, sys, tempfile, time
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
HOL = os.path.dirname(HIER)
MODELLEN = os.path.join(HOL, "modellen")
DOEL = os.path.join(HOL, "godot", "kunst", "3d")
UIT = os.path.join(HIER, "uit")

IMPORT = """[remap]

importer="texture"
type="CompressedTexture2D"
path="res://.godot/imported/{naam}.png.ctex"
metadata={{
"vram_texture": false
}}

[deps]

source_file="res://kunst/3d/{naam}.png"
dest_files=["res://.godot/imported/{naam}.png.ctex"]

[params]

compress/mode=0
compress/high_quality=false
compress/lossy_quality=0.7
compress/hdr_compression=1
compress/normal_map=0
compress/channel_pack=0
mipmaps/generate=true
mipmaps/limit=-1
roughness/mode=0
roughness/src_normal=""
process/fix_alpha_border=true
process/premult_alpha=false
process/normal_map_invert_y=false
process/hdr_as_srgb=false
process/hdr_clamp_exposure=false
process/size_limit=0
detect_3d/compress_to=1
"""


def verklein(im, maat):
    """Lanczos op voorvermenigvuldigde alfa, anders krijgen de randen een donkere zoom."""
    return im.convert("RGBa").resize(maat, Image.LANCZOS).convert("RGBA")


def render_sprite(naam, s, bpy_python, snel, index=None):
    w, h = s["render"]
    samples = max(8, s["samples"] // 4) if snel else s["samples"]
    namen = list(s["frames"].keys())
    ruw = [os.path.join(UIT, f"{naam}_ruw_{i}.png") for i in range(len(namen))]
    duur = 0.0
    if s.get("maat_zonder_verberg") and s.get("verberg"):
        s = dict(s, eenheid_px=_maat_zonder_verberg(naam, s, bpy_python, samples, namen[0]))
    if os.environ.get("HOL_HERGEBRUIK") == "1" and all(os.path.exists(p) for p in ruw):
        beelden = [Image.open(p).convert("RGBA") for p in ruw]   # alleen bijsnijden en schalen opnieuw (proef)
    else:
        beelden, duur, cam = _render(naam, s, bpy_python, samples, namen)
        os.makedirs(UIT, exist_ok=True)
        for b, p in zip(beelden, ruw):
            b.save(p)
        with open(os.path.join(UIT, f"{naam}_cam.json"), "w") as f:
            json.dump(cam, f)
    return _blad(naam, s, beelden, namen, samples, duur, _lees_cam(naam), index)


def _maat_zonder_verberg(naam, s, bpy_python, samples, eerste):
    """Held zonder eigen hoed even groot houden als met (Bram 13 nov 20:40): render het eerste beeld nog een keer
    zonder 'verberg', pas dat in de cel zoals altijd, en geef die schaal terug als eenheid_px (bladpixels per eenheid).
    Zo blijft het lijf even groot als Daan het bedoelde, ook als hij het model later verandert."""
    s2 = dict(s, verberg=[], frames={eerste: s["frames"][eerste]})
    (b,), _, cam = _render(naam + "_maat", s2, bpy_python, max(8, samples // 4), [eerste])
    if not cam:
        raise SystemExit(f"FOUT: {naam}: geen camera uit het model, maat_zonder_verberg kan niet")
    v = b.getchannel("A").point(lambda a: 255 if a > 60 else 0).getbbox()
    marge = round(0.04 * (v[2] - v[0]))
    y1 = min(b.height, v[3] + marge // 2)
    cw, ch = s["cel"]; px = s["px"]
    schaal = min(cw * px / (v[2] - v[0]), ch * px / (y1 - v[1]))
    e = schaal * max(cam["breed"], cam["hoog"]) / cam["ortho"]
    print(f"{naam}: maat met eigen hoed geeft eenheid_px {e:.3f}")
    return e


def _lees_cam(naam):
    p = os.path.join(UIT, f"{naam}_cam.json")
    return json.load(open(p)) if os.path.exists(p) else None


def _render(naam, s, bpy_python, samples, namen):
    """Een beeld is [breed, hoog] of {"schaal": [breed, hoog], "stand": "hap"}. Beelden met dezelfde stand komen
    uit één Blender-run; {stand} in de argumenten wordt ingevuld (standaard "rust")."""
    w, h = s["render"]
    verberg = s.get("verberg", [])
    if not isinstance(verberg, list) or not all(isinstance(b, str) and b for b in verberg):
        raise SystemExit(f"FOUT: {naam}: 'verberg' moet een lijst met namen zijn, bv. [\"hoed\"]")
    cam = None
    groepen = {}
    for i, n in enumerate(namen):
        f = s["frames"][n]
        stand, schaal = (f.get("stand", "rust"), f.get("schaal", [1, 1])) if isinstance(f, dict) else ("rust", f)
        groepen.setdefault(stand, []).append((i, schaal))
    beelden = [None] * len(namen)
    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        for stand, lijst in groepen.items():
            uit = os.path.join(tmp, f"{stand}.png")
            args = [a.format(uit=uit, w=w, h=h, samples=samples, stand=stand) for a in s["args"]]
            env = dict(os.environ, HOL_FRAMES=json.dumps([sc for _, sc in lijst]),
                       HOL_RUIMTE=str(s.get("ruimte", 1.0)))
            env.pop("HOL_VERBERG", None)
            if verberg:
                env["HOL_VERBERG"] = json.dumps(verberg)   # bv. helden zonder eigen hoed: de spelhoed komt los
            r = subprocess.run([bpy_python, os.path.join(MODELLEN, s["model"])] + args, env=env,
                               capture_output=True, text=True)
            if r.returncode != 0:
                print(r.stdout[-3000:], r.stderr[-3000:])
                raise SystemExit(f"FOUT: model {s['model']} faalde voor {naam} (stand {stand})")
            for k, (i, _) in enumerate(lijst):
                beelden[i] = Image.open(os.path.join(tmp, f"{stand}_{k}.png")).convert("RGBA")
            pc = os.path.join(tmp, f"{stand}_cam.json")
            if os.path.exists(pc):
                c = json.load(open(pc))
                if cam and abs(c["ortho"] - cam["ortho"]) > 1e-6:
                    raise SystemExit(f"FOUT: {naam}: stand {stand} heeft een andere camera dan de rest, dan klopt de schaal niet")
                cam = c
    duur = time.time() - t0
    print(f"{naam}: {len(namen)} beelden gerenderd in {duur:.0f} s")
    return beelden, duur, cam


def _blad(naam, s, beelden, namen, samples, duur, cam=None, index=None):
    w, h = s["render"]
    # wat duidelijk zichtbaar is (alfa boven 60 van 255): de vage uitloop van de schaduw telt niet mee voor de maat,
    # anders wordt het figuur klein in zijn cel. Rondom een kleine marge zodat de schaduw zacht afloopt.
    vakken = [b.getchannel("A").point(lambda a: 255 if a > 60 else 0).getbbox() for b in beelden]
    if any(v is None for v in vakken):
        raise SystemExit(f"FOUT: {naam}: een beeld is leeg")
    marge = round(0.04 * max(v[2] - v[0] for v in vakken))
    x0 = max(0, min(v[0] for v in vakken) - marge); y0 = min(v[1] for v in vakken)
    x1 = min(w, max(v[2] for v in vakken) + marge); y1 = min(h, max(v[3] for v in vakken) + marge // 2)
    # schaal: het eerste beeld (rust) past precies in de cel
    cw, ch = s["cel"]; px = s["px"]
    v = vakken[0]
    schaal = min(cw * px / (v[2] - v[0]), ch * px / (y1 - v[1]))
    # Vaste maat (Bram 13 nov 20:30): "eenheid_px" = bladpixels per Blender-eenheid, of "schaal_van": {"sprite": "ridder",
    # "maal": 1.3} = dezelfde eenheid als een ander blad maal een factor (hoeden op de helden). Zonder: passen in de cel.
    rpe = max(cam["breed"], cam["hoog"]) / cam["ortho"] if cam else None   # renderpixels per eenheid
    if "eenheid_px" in s or "schaal_van" in s:
        if not rpe:
            raise SystemExit(f"FOUT: {naam}: vaste maat gevraagd maar het model gaf geen camera door (gedeeld.render)")
        if "eenheid_px" in s:
            doel = float(s["eenheid_px"])
        else:
            ref = (index or {}).get(s["schaal_van"]["sprite"], {})
            if "eenheid_px" not in ref:
                raise SystemExit(f"FOUT: {naam}: {s['schaal_van']['sprite']} heeft nog geen eenheid_px; render die eerst")
            doel = float(ref["eenheid_px"]) * float(s["schaal_van"].get("maal", 1.0))
        schaal = doel / rpe
    cel_w = max(cw * px, round((x1 - x0) * schaal)); cel_h = max(ch * px, round((y1 - y0) * schaal))
    blad = Image.new("RGBA", (cel_w * len(namen), cel_h), (0, 0, 0, 0))
    midden = w / 2   # camera staat op x = 0, dus x = 0 van het model is het midden van de render
    anker_x = round(cel_w / 2)
    tops, nul_y, kruin = [], [], []
    for i, b in enumerate(beelden):
        stuk = b.crop((x0, y0, x1, y1))
        klein = verklein(stuk, (max(1, round(stuk.width * schaal)), max(1, round(stuk.height * schaal))))
        # links zo dat x = 0 van het model op anker_x valt, onderkant op de bodem van de cel
        links = anker_x - round((midden - x0) * schaal)
        boven = cel_h - klein.height
        blad.alpha_composite(klein, (i * cel_w + max(0, links), max(0, boven)))
        cel_a = blad.crop((i * cel_w, 0, (i + 1) * cel_w, cel_h)).getchannel("A").point(lambda a: 255 if a > 40 else 0)
        vak = cel_a.getbbox()
        tops.append(round(vak[1] / px, 2) if vak else 0)
        if cam:
            nul_y.append(round((boven + (cam["nul_px"][1] - y0) * schaal) / px, 2))
            # kruin: bovenste rij met inhoud in een strook rond het midden (+-0,35 eenheid), daar het midden in x
            band = 0.35 * schaal * rpe
            xa, xb = max(0, round(anker_x - band)), min(cel_w, round(anker_x + band) + 1)
            strook = cel_a.crop((xa, 0, xb, cel_h)).getbbox()
            if strook:
                rij = cel_a.crop((xa, strook[1], xb, strook[1] + 1))
                xs = [xa + k for k in range(rij.width) if rij.getpixel((k, 0))]
                kruin.append([round((sum(xs) / len(xs) - anker_x) / px, 2), round(strook[1] / px, 2)])
            else:
                kruin.append([0, 0])
    os.makedirs(DOEL, exist_ok=True)
    blad.save(os.path.join(DOEL, f"{naam}.png"), optimize=True)
    with open(os.path.join(DOEL, f"{naam}.png.import"), "w") as f:
        f.write(IMPORT.format(naam=naam))
    # om naar te kijken: ware grootte op schaal 3 (strook 120) en 4x vergroot, op het pruim van het hol
    os.makedirs(UIT, exist_ok=True)
    s3 = verklein(blad, (round(blad.width * 3 / px), round(blad.height * 3 / px)))
    groot = blad.resize((blad.width * 2, blad.height * 2), Image.LANCZOS)
    kijk = Image.new("RGBA", (max(groot.width, s3.width) + 20, groot.height + s3.height + 30), (29, 20, 38, 255))
    kijk.alpha_composite(s3, (10, 10)); kijk.alpha_composite(groot, (10, s3.height + 20))
    kijk.save(os.path.join(UIT, f"{naam}-kijk.png"))
    info = {"blad": f"res://kunst/3d/{naam}.png", "frames": namen, "cel_px": [cel_w, cel_h], "px": px,
            "anker_x": anker_x, "top": tops, "model": s["model"], "samples": samples, "bytes": os.path.getsize(os.path.join(DOEL, f"{naam}.png"))}
    if cam:
        # eenheid_px: bladpixels per Blender-eenheid; nul_y: rij (spelpixels vanaf de bovenkant van de cel) van het
        # nulpunt van het model (helden: de vloer, hoeden: midden van de onderrand); kruin: [x vanaf anker, y] per beeld.
        info.update({"eenheid_px": round(schaal * rpe, 4), "nul_y": nul_y, "kruin": kruin})
    print(f"{naam}: blad {blad.width}x{blad.height}, top {tops}")
    return info


def render_stukken(naam, s, bpy_python, snel):
    """Soort "stukken" (voor het hol): het model rendert één keer per laag het hele beeld, op vaste schaal en
    zonder bijsnijden. Daarna knipt de pijplijn vakken eruit, in spelpixels, precies op maat. Zo passen
    tegels op elkaar en hebben ze allemaal dezelfde schaal en hetzelfde licht als het hele hol.
    In sprites.json:
      "beeld": [breed, hoog]        het hele modelbeeld in spelpixels (zelfde verhouding als de args van het model)
      "over": 2                     zoveel keer groter renderen dan het blad, daarna verkleinen (scherper)
      "lagen": {"vol": [], "achter": ["kist", "buit"]}   per laag de naambegins die verborgen worden (HOL_VERBERG)
      "stukken": {"gang": {"laag": "achter", "vak": [x, y, b, h]}}   vak in spelpixels, linksboven = 0, 0
    Het blad zet de stukken naast elkaar (elk zijn eigen maat); sprites.json in kunst/3d geeft per stuk
    de plek in het blad (vak_px) en de maat in spelpixels (maat)."""
    bw, bh = s["beeld"]; px = s["px"]; over = s.get("over", 2)
    samples = max(8, s["samples"] // 4) if snel else s["samples"]
    w, h = bw * px * over, bh * px * over
    if not s.get("stukken"):
        raise SystemExit(f"FOUT: {naam}: geen stukken")
    for laag, lijst in s["lagen"].items():
        if not isinstance(lijst, list) or not all(isinstance(b, str) and b for b in lijst):
            raise SystemExit(f"FOUT: {naam}: laag {laag} moet een lijst met namen zijn")
    nodig = sorted({st["laag"] for st in s["stukken"].values()})
    for laag in nodig:
        if laag not in s["lagen"]:
            raise SystemExit(f"FOUT: {naam}: laag {laag} staat niet in 'lagen' (tikfout?)")
    lagen = {}
    t0 = time.time()
    os.makedirs(UIT, exist_ok=True)
    for laag in nodig:
        sleutel = "-".join(sorted(s["lagen"][laag])) or "niets"   # andere verberglijst = ander bestand (HOL_HERGEBRUIK)
        ruw = os.path.join(UIT, f"{naam}_laag_{laag}_{sleutel}.png")
        if not (os.environ.get("HOL_HERGEBRUIK") == "1" and os.path.exists(ruw)):
            with tempfile.TemporaryDirectory() as tmp:
                uit = os.path.join(tmp, "laag.png")
                args = [a.format(uit=uit, w=w, h=h, samples=samples, stand="rust") for a in s["args"]]
                env = dict(os.environ, HOL_VERBERG=json.dumps(s["lagen"][laag]))
                env.pop("HOL_FRAMES", None); env.pop("HOL_RUIMTE", None)
                r = subprocess.run([bpy_python, os.path.join(MODELLEN, s["model"])] + args, env=env,
                                   capture_output=True, text=True)
                if r.returncode != 0:
                    print(r.stdout[-3000:], r.stderr[-3000:])
                    raise SystemExit(f"FOUT: model {s['model']} faalde voor {naam} (laag {laag})")
                Image.open(uit).convert("RGBA").save(ruw)
        b = Image.open(ruw).convert("RGBA")
        if b.size != (w, h):
            raise SystemExit(f"FOUT: {naam}: laag {laag} is {b.size}, verwacht {(w, h)} (klopt 'beeld' met het model?)")
        lagen[laag] = verklein(b, (bw * px, bh * px))
    duur = time.time() - t0
    print(f"{naam}: {len(nodig)} lagen in {duur:.0f} s")
    # stukken naast elkaar, elk op zijn eigen maat, met een rand van RAND bladpixels waarin de buitenste pixels
    # van het stuk zijn doorgetrokken: zo geeft lineair filteren en mipmaps geen doorzichtige naad tussen tegels.
    # Elk stuk begint op een veelvoud van 4 (px), dan vallen de mipmap-blokken netjes.
    RAND = 4
    namen = list(s["stukken"])
    vakken = {}
    for n in namen:
        x, y, b_, h_ = s["stukken"][n]["vak"]
        if not all(isinstance(v, int) for v in (x, y, b_, h_)) or b_ <= 0 or h_ <= 0:
            raise SystemExit(f"FOUT: {naam}: vak van {n} moet vier hele getallen zijn, breed en hoog boven 0")
        if x < 0 or y < 0 or x + b_ > bw or y + h_ > bh:
            raise SystemExit(f"FOUT: {naam}: stuk {n} valt buiten het beeld {bw}x{bh}")
        vakken[n] = (x, y, b_, h_)
    breed = sum(v[2] * px + 2 * RAND for v in vakken.values())
    hoog = max(v[3] * px for v in vakken.values()) + 2 * RAND
    blad = Image.new("RGBA", (breed, hoog), (0, 0, 0, 0))
    info_stukken = {}
    links = 0
    for n in namen:
        x, y, b_, h_ = vakken[n]
        stuk = lagen[s["stukken"][n]["laag"]].crop((x * px, y * px, (x + b_) * px, (y + h_) * px))
        sw, sh = stuk.size
        met_rand = Image.new("RGBA", (sw + 2 * RAND, sh + 2 * RAND))
        met_rand.paste(stuk.resize((sw + 2 * RAND, sh + 2 * RAND), Image.NEAREST), (0, 0))   # grof doortrekken
        # randen precies: elke randstrook is de buitenste rij of kolom van het stuk, uitgerekt
        met_rand.paste(stuk.crop((0, 0, sw, 1)).resize((sw, RAND)), (RAND, 0))
        met_rand.paste(stuk.crop((0, sh - 1, sw, sh)).resize((sw, RAND)), (RAND, sh + RAND))
        kol = met_rand.crop((RAND, 0, RAND + 1, sh + 2 * RAND))
        met_rand.paste(kol.resize((RAND, sh + 2 * RAND)), (0, 0))
        kol = met_rand.crop((RAND + sw - 1, 0, RAND + sw, sh + 2 * RAND))
        met_rand.paste(kol.resize((RAND, sh + 2 * RAND)), (RAND + sw, 0))
        met_rand.paste(stuk, (RAND, RAND))
        blad.paste(met_rand, (links, 0))
        info_stukken[n] = {"vak_px": [links + RAND, RAND, b_ * px, h_ * px], "maat": [b_, h_], "uit": [x, y]}
        links += sw + 2 * RAND
    os.makedirs(DOEL, exist_ok=True)
    blad.save(os.path.join(DOEL, f"{naam}.png"), optimize=True)
    with open(os.path.join(DOEL, f"{naam}.png.import"), "w") as f:
        f.write(IMPORT.format(naam=naam))
    # om naar te kijken: elke laag op ware grootte (schaal 3, strook 120) en het blad 2x
    kijk_lagen = [verklein(l, (bw * 3, bh * 3)) for l in lagen.values()]
    groot = blad.resize((blad.width * 2, blad.height * 2), Image.LANCZOS)
    kw = max([groot.width] + [k.width for k in kijk_lagen]) + 20
    kh = sum(k.height + 10 for k in kijk_lagen) + groot.height + 20
    kijk = Image.new("RGBA", (kw, kh), (29, 20, 38, 255))
    yy = 10
    for k in kijk_lagen:
        kijk.alpha_composite(k, (10, yy)); yy += k.height + 10
    kijk.alpha_composite(groot, (10, yy))
    kijk.save(os.path.join(UIT, f"{naam}-kijk.png"))
    print(f"{naam}: blad {blad.width}x{blad.height}, stukken {namen}")
    return {"soort": "stukken", "blad": f"res://kunst/3d/{naam}.png", "px": px, "beeld": [bw, bh],
            "stukken": info_stukken, "model": s["model"], "samples": samples,
            "bytes": os.path.getsize(os.path.join(DOEL, f"{naam}.png"))}


def main():
    with open(os.path.join(HIER, "sprites.json")) as f:
        alles = json.load(f)["sprites"]
    kies = sys.argv[1:] or list(alles)
    bpy_python = os.environ.get("BPY_PYTHON", "python3")
    snel = os.environ.get("HOL_SNEL") == "1"
    pad = os.path.join(DOEL, "sprites.json")
    index = json.load(open(pad)) if os.path.exists(pad) else {}
    for naam in kies:
        s = alles[naam]
        if s.get("soort") == "stukken":
            index[naam] = render_stukken(naam, s, bpy_python, snel)
        else:
            index[naam] = render_sprite(naam, s, bpy_python, snel, index)
    with open(pad, "w") as f:
        json.dump(index, f, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main()
