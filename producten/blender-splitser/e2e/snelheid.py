"""Speed test for Click Cuts on heavy models (opdracht hoofdchat 24 nov 07:25). Not part of every push:
workflow click-cuts-snelheid.yml, or by hand, one case per Blender process so the peak memory is per case:

blender -b --factory-startup --python e2e/snelheid.py -- <zip> <case> <target polygons> [skull.glb]

Cases:
- scan:   the ScatteringSkull scan (CC0 1.0, KhronosGroup glTF-Sample-Assets), 300 mm long, voxel remeshed to
          about <target> polygons, so it is watertight and dense like a sculpt or a scan. Split to fit goes
          straight to Plan and Split (no remesh in the add-on).
- open:   Suzanne 300 mm wide, subdivided to about <target> polygons and left open (not watertight), like an
          AI model or a sculpt straight out of a program. Split to fit first makes a watertight copy (voxel
          remesh with the default voxel size), as a buyer would see it.

Measured with time.perf_counter around the operators, peak memory of the process with resource.getrusage.
Every line starts with [sj-snel]; the last line is SNEL KLAAR <case> or SNEL FOUT <case> <why>."""
import math
import os
import resource
import sys
import tempfile
import time
import traceback

import bmesh
import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modellen  # noqa: E402


def log(t):
    print(f"[sj-snel] {t}", flush=True)


def piek_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0  # Linux: kB


def driehoeken(ob):
    me = ob.data
    me.calc_loop_triangles()
    return len(me.loop_triangles)


def remesh_tot(ob, doel):
    """Voxel remesh (Blender's own modifier, applied) with a voxel size chosen so the result is about doel
    polygons: polygons scale with 1 / voxel squared, so two tries are enough."""
    voxel = 2.0
    for _ in range(3):
        kopie = ob.copy()
        kopie.data = ob.data.copy()
        bpy.context.scene.collection.objects.link(kopie)
        m = kopie.modifiers.new("vox", "REMESH")
        m.mode = "VOXEL"
        m.voxel_size = voxel
        modellen.actief(kopie)
        bpy.ops.object.modifier_apply(modifier=m.name)
        n = len(kopie.data.polygons)
        log(f"remesh voxel {voxel:.4f} mm -> {n} polygons")
        if abs(n - doel) / doel < 0.15:
            bpy.data.objects.remove(ob)
            return kopie
        bpy.data.objects.remove(kopie)
        voxel *= math.sqrt(n / doel)
    raise RuntimeError("remesh did not reach the target")


def scan(pad, doel):
    ob = modellen.gltf(pad, "")
    modellen.schaal_naar(ob, 1, 300.0)
    return remesh_tot(ob, doel)


def open_suzanne(doel):
    bm = bmesh.new()
    bmesh.ops.create_monkey(bm)
    n = len(bm.faces)
    niveau = 0
    while n * 4 < doel * 1.2:  # every subdivision level gives about 4 times the faces
        n *= 4
        niveau += 1
    bm.free()
    ob = modellen.suzanne_open(300.0)
    m = ob.modifiers.new("sub", "SUBSURF")
    m.levels = niveau
    m.render_levels = niveau
    modellen.actief(ob)
    bpy.ops.object.modifier_apply(modifier=m.name)
    modellen.schaal_naar(ob, 0, 300.0)
    return ob


def meet(naam, fn):
    t = time.perf_counter()
    try:
        r = fn()
    except RuntimeError as e:
        r = f"error: {str(e).strip()[:200]}"
    dt = time.perf_counter() - t
    log(f"TIJD {naam} {dt:.1f} s, uitslag {r}, piek {piek_mb():.0f} MB")
    return dt, r


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_, geval, doel = args[0], args[1], int(args[2])
    bpy.ops.extensions.package_install_files(filepath=zip_, repo="user_default", enable_on_install=True)
    log(f"Blender {bpy.app.version_string}, geval {geval}, doel {doel} polygons, "
        f"solver {__import__('bl_ext.user_default.click_cuts.splitsen', fromlist=['x']).solver_naam()}")
    s = modellen.mm_scene()
    s.split_joints.printer = "A1MINI"
    s.split_joints.speling_mm = 0.2
    t = time.perf_counter()
    ob = scan(args[3], doel) if geval == "scan" else open_suzanne(doel)
    log(f"MODEL {ob.name}: {len(ob.data.polygons)} polygons, {driehoeken(ob)} triangles, "
        f"{len(ob.data.vertices)} vertices, size {[round(x) for x in ob.dimensions]} mm, "
        f"gemaakt in {time.perf_counter() - t:.1f} s, piek {piek_mb():.0f} MB")
    modellen.actief(ob)
    dt, r = meet("split_to_fit", bpy.ops.split_joints.split_to_fit)
    stukken = [o for o in s.objects if o.get("sj_stuk")]
    groen = [o for o in stukken if o.get("sj_status") == "groen"]
    tri = sum(driehoeken(o) for o in stukken)
    log(f"STUKKEN {len(stukken)}, groen {len(groen)}, triangles in pieces {tri}, "
        f"klikstappen '{s.get('sj_klik_stappen', '')}', uitslag '{s.split_joints.uitslag}'")
    if r != {"FINISHED"} or not stukken:
        log(f"SNEL FOUT {geval} split_to_fit gaf {r}")
        return
    uit = tempfile.mkdtemp(prefix="cc_snel_")
    for formaat in ("STL", "3MF"):
        s.split_joints.formaat = formaat
        s.split_joints.exportmap = os.path.join(uit, formaat.lower()) + os.sep
        dt, r = meet(f"export_{formaat}", bpy.ops.split_joints.exporteer)
        bestanden = s.get("sj_laatste_export", [])
        mb = sum(os.path.getsize(p) for p in bestanden) / 1e6
        log(f"EXPORT {formaat}: {len(bestanden)} files, {mb:.0f} MB")
    log(f"SNEL KLAAR {geval} piek {piek_mb():.0f} MB")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        log("SNEL FOUT onverwacht")
