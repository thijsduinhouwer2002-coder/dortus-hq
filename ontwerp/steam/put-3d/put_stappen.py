"""Voorstel 3D-put per gekochte stap (Daan, 14 nov 2026).

Draait Mila's hol.py ongewijzigd (alleen de laatste render-regel niet) en past daarna de put aan:
  STAP=0  zoals nu (dichte put zonder stappen)
  STAP=1  Rusty Spikes: roestige, iets scheve stekels, roestvlekken op de rand
  STAP=2  Deep Pit: dieper zwart gat, langere stekels (staal met roestige voet)
Draai:  STAP=1 <venv>/bin/python put_stappen.py uit.png 720 120 16
"""
import os, sys, math, random
HIER = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(HIER, "..", "..", "..", "producten", "steam-hol", "modellen")
sys.path.insert(0, MOD)
STAP = int(os.environ.get("STAP", "0"))
bron = open(os.path.join(MOD, "hol.py"), encoding="utf-8").read()
cut = bron.rindex("g.render(uit")
ns = {"__file__": os.path.join(MOD, "hol.py"), "__name__": "hol"}
exec(compile(bron[:cut], "hol.py", "exec"), ns)
bpy, g, cil, blok, PUT_X = ns["bpy"], ns["g"], ns["cil"], ns["blok"], ns["PUT_X"]
sc = bpy.context.scene
rnd = random.Random(4)

def weg(prefix):
    for o in list(sc.objects):
        if o.name.split(".")[0] == prefix:
            bpy.data.objects.remove(o, do_unlink=True)

if STAP >= 1:
    ROEST = g.mat("roest", "a4552a", rough=0.75, spec=0.3, metaal=0.35)
    ROEST_L = g.mat("roest_l", "d9894a", rough=0.5, spec=0.5, metaal=0.5, emis=0.08)
    STAAL_L = bpy.data.materials["staal_l"]
    STAAL_D = g.mat("staal_d", "8c8a90", rough=0.55, spec=0.5, metaal=0.6)
    ROEST = g.mat("roest_d", "7a3a1a", rough=0.85, spec=0.2, metaal=0.2)
    weg("stekel")
    for i in range(6):
        for j in range(3):
            if STAP == 1:
                hoog = (0.6 if (i + j) % 2 == 0 else 0.48) + rnd.uniform(-0.05, 0.05)
                # ronde c (frisse kijker: "egaal oranje leest als koper of vuur"): grijs staal met roestbanden
                m = ROEST if (i + j) % 3 == 0 else STAAL_D
                kant = (math.radians(rnd.uniform(-14, 14)), math.radians(rnd.uniform(-14, 14)), 0)
                x, y = PUT_X - 0.6 + i * 0.24, 0.15 + j * 0.38
                cil("stekel", (x, y, -0.25 + hoog / 2), 0.075, hoog, m, rot=kant, verts=8, r2=0.0)
                for zb in (0.12, 0.3):
                    cil("roestband", (x, y, -0.25 + zb), 0.075 * (1 - zb / hoog) + 0.008, 0.06, ROEST, rot=kant, verts=8)
            else:
                hoog = (0.92 if (i + j) % 2 == 0 else 0.78)
                z0 = -0.42
                x, y = PUT_X - 0.6 + i * 0.24, 0.15 + j * 0.38
                cil("stekel", (x, y, z0 + 0.18 + hoog / 2), 0.07, hoog, STAAL_L, verts=8, r2=0.0)
                cil("stekelvoet", (x, y, z0 + 0.1), 0.08, 0.2, ROEST, verts=8)
    if STAP == 1:
        # roestvlekken op de rand van het gat (lezen op 120 als warme rand)
        for dx in (-0.82, 0.8):
            blok("roestrand", (PUT_X + dx, 0.2, 0.0), (0.12, 0.35, 0.03), ROEST)
if STAP == 2:
    ZWART = g.mat("diep", "0b0610", rough=1.0, spec=0.0)
    weg("put_bodem")
    blok("put_diep", (PUT_X, 0.7, -0.66), (1.5, 1.5, 0.05), ZWART)
    # binnenwanden van de put donker, zodat het gat diep leest
    for dx in (-0.76, 0.76):
        blok("put_wand", (PUT_X + dx, 0.6, -0.35), (0.04, 1.6, 0.62), ZWART)
    blok("put_wand", (PUT_X, 1.35, -0.35), (1.55, 0.04, 0.62), ZWART)
    # stenen rand om het diepe gat
    STEEN = bpy.data.materials.get("steen") or g.mat("steen2", "7a5f80", rough=0.8)
    # Ronde b: het diepe gat zie je bijna niet (camera 15 graden), dus het verschil moet boven de vloer zitten:
    # langere stekels en twee donkere stenen randen met een rode waarschuwingsband (zoals een mijnschacht)
    # ronde c (frisse kijker: "lijkt op 0"): een zwarte, bredere opening op vloerhoogte, die zie je wel
    blok("put_mond", (PUT_X, 0.45, 0.004), (1.62, 0.9, 0.01), ZWART)
    RAND = g.mat("putrand_d", "3a2a40", rough=0.85)
    BAND = g.mat("band", "c23a2a", rough=0.6, emis=0.1)
    for dx in (-0.84, 0.84):
        blok("putrand", (PUT_X + dx, 0.25, 0.08), (0.12, 0.5, 0.16), RAND)
        blok("putband", (PUT_X + dx, 0.0, 0.1), (0.125, 0.02, 0.05), BAND)

g.render(ns["uit"], ns["W"], ns["H"], ns["SAMPLES"], doorzichtig=True)
print("klaar", ns["uit"])
