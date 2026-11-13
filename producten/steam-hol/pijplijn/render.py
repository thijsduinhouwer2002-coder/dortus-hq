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


def render_sprite(naam, s, bpy_python, snel):
    w, h = s["render"]
    samples = max(8, s["samples"] // 4) if snel else s["samples"]
    namen = list(s["frames"].keys())
    ruw = [os.path.join(UIT, f"{naam}_ruw_{i}.png") for i in range(len(namen))]
    duur = 0.0
    if os.environ.get("HOL_HERGEBRUIK") == "1" and all(os.path.exists(p) for p in ruw):
        beelden = [Image.open(p).convert("RGBA") for p in ruw]   # alleen bijsnijden en schalen opnieuw (proef)
    else:
        beelden, duur = _render(naam, s, bpy_python, samples, namen)
        os.makedirs(UIT, exist_ok=True)
        for b, p in zip(beelden, ruw):
            b.save(p)
    return _blad(naam, s, beelden, namen, samples, duur)


def _render(naam, s, bpy_python, samples, namen):
    """Een beeld is [breed, hoog] of {"schaal": [breed, hoog], "stand": "hap"}. Beelden met dezelfde stand komen
    uit één Blender-run; {stand} in de argumenten wordt ingevuld (standaard "rust")."""
    w, h = s["render"]
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
            r = subprocess.run([bpy_python, os.path.join(MODELLEN, s["model"])] + args, env=env,
                               capture_output=True, text=True)
            if r.returncode != 0:
                print(r.stdout[-3000:], r.stderr[-3000:])
                raise SystemExit(f"FOUT: model {s['model']} faalde voor {naam} (stand {stand})")
            for k, (i, _) in enumerate(lijst):
                beelden[i] = Image.open(os.path.join(tmp, f"{stand}_{k}.png")).convert("RGBA")
    duur = time.time() - t0
    print(f"{naam}: {len(namen)} beelden gerenderd in {duur:.0f} s")
    return beelden, duur


def _blad(naam, s, beelden, namen, samples, duur):
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
    cel_w = max(cw * px, round((x1 - x0) * schaal)); cel_h = max(ch * px, round((y1 - y0) * schaal))
    blad = Image.new("RGBA", (cel_w * len(namen), cel_h), (0, 0, 0, 0))
    midden = w / 2   # camera staat op x = 0, dus x = 0 van het model is het midden van de render
    anker_x = round(cel_w / 2)
    tops = []
    for i, b in enumerate(beelden):
        stuk = b.crop((x0, y0, x1, y1))
        klein = verklein(stuk, (max(1, round(stuk.width * schaal)), max(1, round(stuk.height * schaal))))
        # links zo dat x = 0 van het model op anker_x valt, onderkant op de bodem van de cel
        links = anker_x - round((midden - x0) * schaal)
        boven = cel_h - klein.height
        blad.alpha_composite(klein, (i * cel_w + max(0, links), max(0, boven)))
        vak = blad.crop((i * cel_w, 0, (i + 1) * cel_w, cel_h)).getchannel("A").point(lambda a: 255 if a > 40 else 0).getbbox()
        tops.append(round(vak[1] / px, 2) if vak else 0)
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
    print(f"{naam}: blad {blad.width}x{blad.height}, top {tops}")
    return info


def main():
    with open(os.path.join(HIER, "sprites.json")) as f:
        alles = json.load(f)["sprites"]
    kies = sys.argv[1:] or list(alles)
    bpy_python = os.environ.get("BPY_PYTHON", "python3")
    snel = os.environ.get("HOL_SNEL") == "1"
    pad = os.path.join(DOEL, "sprites.json")
    index = json.load(open(pad)) if os.path.exists(pad) else {}
    for naam in kies:
        index[naam] = render_sprite(naam, alles[naam], bpy_python, snel)
    with open(pad, "w") as f:
        json.dump(index, f, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main()
