"""Renders of the split models (Workbench, needs a display: run under xvfb-run).
blender -b --factory-startup --python e2e/scherm_kern.py -- <dir with suzanne.blend, vaas.blend, schedel.blend> <out dir>
Per model: the pieces in exploded view with the pins (color per piece, pins gold: kleuren.py), and a
close-up of one cut face with its pin holes and engraved number.
magneet.blend (toetsen_magneet.py, issue #144): the same pictures in Magnets mode, for the gallery. Logs SCHERM OK per picture."""
import json
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


def model(naam):
    pad = os.path.join(bron, f"{naam}.blend")
    if not os.path.exists(pad):
        log(f"SCHERM FOUT {naam}: geen {pad}")
        return
    bpy.ops.wm.open_mainfile(filepath=pad)
    s = bpy.context.scene
    stukken = sorted((o for o in s.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])
    pennen = [o for o in s.objects if o.get("sj_pennen")]
    for o in s.objects:
        o.hide_render = not (o.get("sj_stuk") or o.get("sj_pennen"))
    log(f"{naam}: {len(stukken)} stukken, {[o.get('sj_status') for o in stukken]}, pennen {[o.name for o in pennen]}")
    kader(stukken + pennen, Vector((1.0, -1.5, 0.9)))
    render(f"{naam}-1-stukken.png")
    # close-up: the first piece with a number, looking straight at that cut face
    for o in stukken:
        lbs = json.loads(o.get("sj_labels", "[]"))
        if naam == "vrij":  # the free cut face, not a grid face
            lbs = [lb for lb in lbs if lb.get("vrij")]
        if not lbs:
            continue
        lb = lbs[0]
        for p in s.objects:
            p.hide_render = p is not o
        if "n" in lb:  # free cut: the normal of the plane
            n = Vector(lb["n"]) * float(lb["teken"])
        else:
            n = Vector((0.0, 0.0, 0.0))
            n[lb["as"]] = float(lb["teken"])
        midden = o.matrix_world @ Vector(lb["p"])
        gaten = [g for g in json.loads(o.get("sj_gaten", "[]")) if g["as"] == lb["as"]]
        straal = max([lb["h"] * len(lb["tekst"])] + [(Vector(g["p"]) - Vector(lb["p"])).length + 8 for g in gaten])
        schuin = n + Vector((0.18, -0.12, 0.15))
        camera(midden, schuin, straal * 2.6, lens=50)
        render(f"{naam}-2-snijvlak-{lb['tekst']}.png")
        break


if __name__ == "__main__":  # scherm_plat.py imports the helpers above
    for m in ("suzanne", "vaas", "schedel", "vrij", "magneet"):
        try:
            model(m)
        except Exception as e:
            log(f"SCHERM FOUT {m}: {e!r}")
    log("SCHERM KLAAR")
