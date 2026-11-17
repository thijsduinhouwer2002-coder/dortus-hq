"""Toets Pro 1.1 stap 2a: scharnier met een vrije eindstop (eigenschap `graden`, 30 tot 150), voor Rig to Figure.

Per getal N een nieuwe staaf (straal 6 mm, langs X, mm-scene), scharnier met graden=N:
- twee gesloten delen; stop uit de wig (2a + s/r) binnen 0,1 graad van N;
- gemeten bereik uit de beweegproef tussen N - 2 en N + 0,2 (nooit meer dan gevraagd);
- 20 en 170 geweigerd (buiten 30 tot 150), niets gesneden.
Gebruik: blender -b --factory-startup --python e2e/toetsen_vrije_stop.py -- <betaalde zip>
"""
import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

FOUT = []
GETALLEN = (30, 45, 60, 75, 90, 100, 120, 135, 150)


def log(t):
    print(f"[cj-vrij] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def gesloten(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return fout == 0


def proef(n):
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    staaf = figuren.staaf("lid", 6.0, lengte=60.0)
    figuren.maak_actief(staaf)
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):
        m.col[i][:3] = v
    m.col[3][:3] = (0.031, 0.013, 0.021)
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m
    try:
        r = bpy.ops.click_joints.plaats_scharnier(graden=n)
    except RuntimeError as e:
        r = f"fout {e}"
    return r, bpy.data.objects.get("lid_A"), bpy.data.objects.get("lid_B")


def main():
    zip_pad = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    import importlib
    vorm = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_vorm")
    log(f"Blender {bpy.app.version_string}")
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar = 0.2, "CURSOR", False
    for n in GETALLEN:
        r, a, b = proef(n)
        if r != {"FINISHED"} or a is None or b is None:
            check(False, f"{n}: geplaatst ({r})")
            continue
        stop = vorm.stop_graden(math.radians(float(b["cj_wig_graden"])), float(b["cj_theta_s"]))
        gemeten = float(b["cj_bereik_graden"])
        log(f"{n}: stand {b['cj_stand']} stop {stop:.3f} gemeten {gemeten:.2f} achter {b['cj_achter_graden']} "
            f"duur {b.get('cj_duur_s')} s")
        check(gesloten(a) and gesloten(b), f"{n}: twee gesloten delen")
        check(int(b["cj_stand"]) == n and abs(stop - n) <= 0.1, f"{n}: stop uit de wig {stop:.3f}")
        check(n - 2.0 <= gemeten <= n + 0.2, f"{n}: gemeten bereik {gemeten:.2f}")
    for n in (20, 170):
        r, a, b = proef(n)
        check(r == {"CANCELLED"} and a is None and b is None, f"{n}: geweigerd ({r})")
    log(f"KLAAR {len(FOUT)} FOUT")


main()
