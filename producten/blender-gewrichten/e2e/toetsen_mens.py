"""Toets (17 nov run 20): Figure from rig op een echte mensfiguur (MakeHuman base.obj, CC0) met Mixamo-rig.

Zelfde figuur en rig als proef_mens.py (run 18), nu met eisen, zodat de figuur van het eindbeeld voor Daan in de CI
blijft werken. Standaard 220 mm hoog (zet CJ_HOOGTE niet zelf; deze toets zet hem).

Eisen in Blender 5.x (gemeten run 18 en 20):
- minstens 6 gewrichten, waaronder beide ellebogen en beide knieën;
- Left knee `from rig` met 0–120, Right knee `mirrored` met 0–120; Left elbow `from rig` 0–140, Right elbow
  `mirrored` 0–140 (het getal is het gemeten bereik, binnen 3 graden);
- elk standaardgewricht dat niet geplaatst is, staat in de melding met een reden tussen haakjes;
- alle delen gesloten en elk deel één stuk;
- handen, voeten en hoofd liggen nog in een deel (geen stil verloren lid).
In Blender 4.2 (alleen de Exact-solver, bekende losse boolean-fout, zie toetsen_rig_armen.py): minstens 3
gewrichten met de ellebogen (gemeten: ellebogen en nek), de rest met reden, en dezelfde eisen voor gesloten, één stuk en niets kwijt.

Gebruik: blender -b --factory-startup --python e2e/toetsen_mens.py -- <betaalde zip> <base.obj>
Uitslag: regels [cj-mens-toets], laatste regel "KLAAR n FOUT".
"""
import importlib
import os
import sys

import bpy

os.environ["CJ_HOOGTE"] = os.environ.get("CJ_TOETS_HOOGTE", "220")
HIER = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
M = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
exec(compile(_src, "proef_mens.py", "exec"), M)
A = M["A"]

FOUT = []


def log(t):
    print(f"[cj-mens-toets] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def mod(naam):
    return importlib.import_module("bl_ext.user_default.click_joints." + naam)


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, pad = args[0], args[1]
    A["installeer"](zip_pad)
    inst = bpy.context.scene.click_joints
    A["leeg"]()
    ob, punten = M["laad_mens"](pad)
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    naam = ob.name
    rig = M["maak_rig"](punten)
    ob.modifiers.new("Armature", "ARMATURE").object = rig
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    try:
        r = bpy.ops.click_joints.figuur_uit_rig()
    except RuntimeError as e:
        r = f"fout {str(e).strip()[:300]}"
    fig = mod("betaald.figuur")
    ges = mod("gesloten")
    rigm = mod("betaald.rig")
    alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    per = {x["naam"]: x for x in alle}
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
    over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), "") or ""
    log(f"uitslag={r} gewrichten={len(alle)}: {[fig.regel(x) for x in alle]}")
    log(f"overgeslagen: {over}")
    oud = bpy.app.version < (4, 5, 0)

    def bereik(n, graden, herkomst):
        x = per.get(n)
        ok = x is not None and x.get("herkomst") == herkomst and x.get("graden") is not None \
            and abs(float(x["graden"]) - graden) <= 3.0
        return ok, (fig.regel(x) if x else "ontbreekt")

    if oud:
        # Gemeten run 20 (4.2.23): ellebogen en nek lukken, knieën, heupen en schouders vallen af met reden
        # (overlap of geen gesloten delen met alleen Exact). Eerlijk in de tekst: "best in Blender 4.5 and newer".
        check(len(alle) >= 3, f"4.2: minstens 3 gewrichten ({len(alle)})")
    else:
        check(len(alle) >= 6, f"minstens 6 gewrichten ({len(alle)})")
        for n, g, h in (("Left knee", 120, "from rig"), ("Right knee", 120, "mirrored")):
            ok, t = bereik(n, g, h)
            check(ok, f"{n}: 0–{g} {h} ({t})")
    for n, g, h in (("Left elbow", 140, "from rig"), ("Right elbow", 140, "mirrored")):
        ok, t = bereik(n, g, h)
        check(ok, f"{n}: 0–{g} {h} ({t})")
    standaard = [f"{k} {w}" for k in ("Left", "Right") for w in ("knee", "elbow", "hip", "shoulder")] + ["Neck"]
    mis = [n for n in standaard if n not in per]
    check(all(f"{n} (" in over for n in mis), f"elk overgeslagen gewricht met reden ({mis})")
    check(all(ges.is_gesloten(o)[0] for o in delen), f"alle {len(delen)} delen gesloten")
    stukken = [A["mesh_staat"](o)["losse_stukken"] for o in delen]
    check(all(s == 1 for s in stukken), f"elk deel één stuk ({stukken})")
    dg = bpy.context.evaluated_depsgraph_get()
    for p_naam in ("l-hand", "r-hand", "l-ankle", "r-ankle", "head"):
        p = punten[p_naam]
        binnen = any(rigm._in_kader(o, p) and rigm.binnen(o, p, dg)[0] for o in delen)
        check(binnen, f"{p_naam} {tuple(round(c, 1) for c in p)} ligt nog in een deel")
    log(f"KLAAR {len(FOUT)} FOUT")


main()
