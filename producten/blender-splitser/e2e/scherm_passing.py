"""Renders of the fit test (Workbench, run under xvfb-run, like scherm_kern.py).
blender -b --factory-startup --python e2e/scherm_passing.py -- <dir with passing.blend> <out dir>
passing-1.png: block and pins from the front, above. passing-2.png: top view of the block, the engraved
clearances readable. Logs SCHERM OK per picture."""
import os
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:]
bron, uitmap = args[0], args[1]
os.makedirs(uitmap, exist_ok=True)


def log(t):
    print(f"[sj-scherm] {t}", flush=True)


def hoeken(objs):
    pts = []
    for o in objs:
        pts += [o.matrix_world @ Vector(c) for c in o.bound_box]
    return pts


def camera(doel, richting, afstand, lens=50):
    cam = bpy.data.objects.get("SJ camera")
    if cam is None:
        cam = bpy.data.objects.new("SJ camera", bpy.data.cameras.new("SJ camera"))
        bpy.context.scene.collection.objects.link(cam)
    cam.data.lens = lens
    cam.data.clip_end = 100000.0
    cam.location = doel + richting.normalized() * afstand
    cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = cam
    bpy.context.view_layer.update()
    return cam


def kader(objs, richting, lens=50, marge=0.06):
    pts = hoeken(objs)
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    doel = (lo + hi) / 2
    afstand = (hi - lo).length
    for _ in range(40):
        cam = camera(doel, richting, afstand, lens)
        uv = [world_to_camera_view(bpy.context.scene, cam, p) for p in pts]
        if min(q.x for q in uv) < marge or max(q.x for q in uv) > 1 - marge or \
                min(q.y for q in uv) < marge or max(q.y for q in uv) > 1 - marge:
            afstand *= 1.08
        elif min(q.x for q in uv) > 2 * marge and max(q.x for q in uv) < 1 - 2 * marge and \
                min(q.y for q in uv) > 2 * marge and max(q.y for q in uv) < 1 - 2 * marge:
            afstand *= 0.95
        else:
            break


def render(naam):
    s = bpy.context.scene
    s.render.engine = "BLENDER_WORKBENCH"
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = 1600, 1000, 100
    sh = s.display.shading
    sh.light, sh.color_type = "STUDIO", "OBJECT"
    sh.show_cavity = True
    sh.cavity_type = "BOTH"
    sh.show_object_outline = True
    s.world = s.world or bpy.data.worlds.new("SJ wereld")
    s.world.color = (0.09, 0.10, 0.12)
    pad = os.path.join(uitmap, naam)
    s.render.filepath = pad
    bpy.ops.render.render(write_still=True)
    ok = os.path.exists(pad) and os.path.getsize(pad) > 10000
    log(f"{'SCHERM OK' if ok else 'SCHERM FOUT'} {naam} {os.path.getsize(pad) if os.path.exists(pad) else 0} bytes")
    return ok


bpy.ops.wm.open_mainfile(filepath=os.path.join(bron, "passing.blend"))
proef = [o for o in bpy.context.scene.objects if o.get("sj_passing")]
for o in bpy.context.scene.objects:
    if o.type == "MESH" and o not in proef:
        o.hide_render = True
for o in proef:
    o.color = (0.86, 0.66, 0.28, 1.0) if o["sj_passing"] == "blok" else (0.55, 0.38, 0.62, 1.0)
if not proef:
    log("SCHERM FOUT geen fit test in passing.blend")
else:
    kader(proef, Vector((0.25, -1.0, 0.9)), lens=60)
    render("passing-1.png")
    blok = [o for o in proef if o["sj_passing"] == "blok"]
    kader(blok, Vector((0.0, -0.08, 1.0)), lens=60, marge=0.04)
    render("passing-2.png")
