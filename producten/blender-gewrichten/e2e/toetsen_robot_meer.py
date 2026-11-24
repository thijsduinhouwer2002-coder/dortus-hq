"""Toets (Pro 1.2.6, Olaf 24 nov): "More bones" op de studio-robot (commercie/filmpjes/studio/figuur_robot.py).

Regisseur zag op 24 nov (release regisseur-17) dat de robot geen enkels kreeg. Na 1.2.5 bleef de reden "the cut lost
part of the model": het vangnet keek buiten een bol van 15 mm (0,6 keer het korte voetbot), en de uitsnede voor
0-90 graden buigen op een blokvoet ligt verder. Sinds 1.2.6 krijgt die bol de maat van het scheenbot, zoals de knie.
Gemeten lokaal 5.3.0: 11 gewrichten met beide enkels 0-90, knieën 0-120.

Eisen vanaf Blender 4.5: beide enkels geplaatst en minstens 45 graden, knieën nog 0-120, alle delen gesloten en elk
deel één stuk. In 4.2 (alleen Exact): elk overgeslagen gewricht met reden, en dezelfde eisen voor gesloten en één stuk.

Gebruik: blender -b --factory-startup --python e2e/toetsen_robot_meer.py -- <betaalde zip>
Uitslag: regels [cj-robot-toets], laatste regel "KLAAR n FOUT".
"""
import importlib
import os
import sys

import bpy

os.environ["CJ_HOOGTE"] = "220"
HIER = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
M = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
exec(compile(_src, "proef_mens.py", "exec"), M)
A = M["A"]
STUDIO = os.path.abspath(os.path.join(HIER, "..", "..", "..", "commercie", "filmpjes", "studio"))
FOUT = []


def log(t):
    print(f"[cj-robot-toets] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    A["installeer"](args[0])
    sys.path.insert(0, STUDIO)
    import figuur_laden as FL
    _rig, ob, _p = FL.laad_figuur("robot", 220.0)
    naam = ob.name
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    try:
        r = bpy.ops.click_joints.figuur_uit_rig(meer=True)
    except RuntimeError as e:
        r = f"fout {str(e).strip()[:300]}"
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
    alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    per = {x["naam"]: x for x in alle}
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
    over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), "") or ""
    log(f"uitslag={r} gewrichten={len(alle)}: {[fig.regel(x) for x in alle]}")
    log(f"overgeslagen: {over}")

    def graden(n):
        x = per.get(n)
        return None if x is None or x.get("graden") is None else float(x["graden"])

    if bpy.app.version >= (4, 5, 0):
        for n in ("Left ankle", "Right ankle"):
            g = graden(n)
            check(g is not None and g >= 45.0, f"{n} geplaatst en buigt minstens 45 graden ({g}; {over[:300]})")
        for n in ("Left knee", "Right knee"):
            g = graden(n)
            check(g is not None and abs(g - 120.0) <= 3.0, f"met enkels: {n} nog 0-120 ({g})")
    standaard = [f"{k} {w}" for k in ("Left", "Right") for w in ("knee", "elbow", "hip", "shoulder", "ankle")] + ["Neck"]
    mis = [n for n in standaard if n not in per]
    check(all(f"{n} (" in over for n in mis), f"elk overgeslagen gewricht met reden ({mis})")
    check(bool(delen) and all(ges.is_gesloten(o)[0] for o in delen), f"alle {len(delen)} delen gesloten")
    st = [A["mesh_staat"](o)["losse_stukken"] for o in delen]
    check(all(s == 1 for s in st), f"elk deel één stuk ({st})")
    log(f"KLAAR {len(FOUT)} FOUT")


main()
