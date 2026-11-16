"""Toets (16 nov run 16): Figure from rig op echte Meshy-figuren met Mixamo-botnamen, met eisen.

Gebruikt de opzet van proef_meshy_rig.py (figuur 150 mm, Make watertight, rig met Mixamo-namen uit doorsneden,
linkerknie Limit Rotation 120, rechts niets). Alleen heupen en knieën (`CJ_ALLEEN=hip,knee`), heupkop op 52%.
Eisen per figuur:
- linkerknie scharnier 0-120 `from rig`; rechterknie `mirrored` (in 4.2 mag een knie eerlijk ontbreken: Exact-solver);
- elk deel gesloten en één stuk (geen achtergelaten zool of blokje);
- een heup die er niet op komt heeft een leesbare reden (geen "not placed", geen kale "nothing was cut").

Gebruik: blender -b --factory-startup --python e2e/toetsen_meshy_rig.py -- <betaalde zip> <model.glb> [...]
"""
import importlib
import os
import sys

import bpy

HIER = os.path.dirname(os.path.abspath(__file__))
os.environ["CJ_ALLEEN"] = "hip,knee"
os.environ["CJ_HEUP_PCT"] = "52"
os.environ.pop("CJ_SPLEET", None)
_src = open(os.path.join(HIER, "proef_meshy_rig.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
P = {"__name__": "proef_meshy_rig", "__file__": os.path.join(HIER, "proef_meshy_rig.py")}
exec(compile(_src, "proef_meshy_rig.py", "exec"), P)
A = P["A"]
fouten = 0


def log(t):
    print(f"[cj-mtoets] {t}", flush=True)


def check(ok, t):
    global fouten
    if not ok:
        fouten += 1
    log(("OK   " if ok else "FOUT ") + t)


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad = args[0]
    A["installeer"](zip_pad)
    log(f"Blender {bpy.app.version_string}")
    oud = bpy.app.version < (4, 5, 0)
    inst = bpy.context.scene.click_joints
    rigm = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
    echt = rigm.gewrichten
    rigm.gewrichten = lambda a, meer=False: [x for x in echt(a, meer) if "hip" in x[2].lower() or "knee" in x[2].lower()]
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
    for pad in args[1:]:
        A["leeg"]()
        ob = A["laad"](pad)
        st = A["mesh_staat"](ob)
        if st["open_randen"] or st["randen_3plus"]:
            A["actief"](ob)
            bpy.ops.click_joints.maak_gesloten()
            nieuw = bpy.context.view_layer.objects.active
            if nieuw is not ob:
                bpy.data.objects.remove(ob)
                ob = nieuw
        naam = ob.name
        rig = P["maak_rig"](ob)
        check(rig is not None, f"{naam}: rig gemaakt")
        if rig is None:
            continue
        ob.modifiers.new("Armature", "ARMATURE").object = rig
        inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
        A["actief"](ob)
        try:
            r = bpy.ops.click_joints.figuur_uit_rig()
        except RuntimeError as e:
            r = f"fout {str(e).strip()[:200]}"
        alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
        per = {x["naam"]: x for x in alle}
        delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get()
                 and o.type == "MESH"]
        over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), "") or ""
        log(f"{naam}: uitslag {r}, gewrichten {[fig.regel(x) for x in alle]}, overgeslagen: {over}")
        lk = per.get("Left knee")
        # 4.2 (Exact-solver, plan punt 3): een knie mag eerlijk weigeren, met een echte reden in de lijst.
        lk_reden = next((s for s in over.split("; ") if s.startswith("Left knee (")), "")
        check((lk is not None and lk.get("herkomst") == "from rig" and round(lk.get("graden") or 0) == 120)
              or (oud and lk is None and lk_reden and "not placed" not in lk_reden),
              f"{naam}: linkerknie 0-120 from rig ({lk or lk_reden})")
        rk = per.get("Right knee")
        check((rk is not None and rk.get("herkomst") == "mirrored") or (oud and rk is None),
              f"{naam}: rechterknie mirrored ({rk})")
        check(all(ges.is_gesloten(o)[0] for o in delen), f"{naam}: alle {len(delen)} delen gesloten")
        st = [A["mesh_staat"](o)["losse_stukken"] for o in delen]
        check(all(s == 1 for s in st), f"{naam}: elk deel één stuk ({st})")
        for kant in ("Left hip", "Right hip"):
            if kant in per:
                continue
            stuk = next((s for s in over.split("; ") if s.startswith(kant + " (")), "")
            check(stuk and "not placed" not in stuk and stuk != f"{kant} (nothing was cut)",
                  f"{naam}: {kant} overgeslagen met leesbare reden ({stuk})")
    log(f"KLAAR {fouten} FOUT")


main()
