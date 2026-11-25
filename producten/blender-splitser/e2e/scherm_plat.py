"""Picture of Lay parts flat (1.0.0): the exported STL files of one model, read back from disk, standing in a
row on a grey print bed. Top row: Lay parts flat off (pieces as they stand in the model). Bottom row: on
(largest cut face down, lowest point on z = 0). Workbench, needs a display: run under xvfb-run.
blender -b --factory-startup --python e2e/scherm_plat.py -- <dir with <model>/plat_uit and plat_aan> <out dir> [model]
Logs SCHERM OK plat-<model>."""
import glob
import os
import sys

import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scherm_kern import kader, log, render  # noqa: E402  (scherm_kern only runs its pictures under __main__)

args = sys.argv[sys.argv.index("--") + 1:]
bron, uitmap = args[0], args[1]
model = args[2] if len(args) > 2 else "schedel"
KLEUREN = [(0.04, 0.57, 0.84, 1), (1.0, 0.42, 0.21, 1), (0.36, 0.78, 0.45, 1), (0.85, 0.35, 0.75, 1),
           (0.95, 0.8, 0.2, 1), (0.3, 0.85, 0.85, 1), (0.6, 0.45, 0.95, 1), (0.9, 0.3, 0.35, 1)]


def lees(map_, y):
    objs = []
    x = 0.0
    for i, pad in enumerate(sorted(glob.glob(os.path.join(map_, "piece_*.stl")))):
        bpy.ops.wm.stl_import(filepath=pad)
        ob = bpy.context.selected_objects[0]
        ob.color = KLEUREN[i % len(KLEUREN)]
        lo = min((ob.matrix_world @ Vector(c)).x for c in ob.bound_box)
        hi = max((ob.matrix_world @ Vector(c)).x for c in ob.bound_box)
        ylo = min((ob.matrix_world @ Vector(c)).y for c in ob.bound_box)
        yhi = max((ob.matrix_world @ Vector(c)).y for c in ob.bound_box)
        zlo = min((ob.matrix_world @ Vector(c)).z for c in ob.bound_box)
        ob.location += Vector((x - lo, y - (ylo + yhi) / 2, -zlo))  # each piece on the bed, side by side
        x += hi - lo + 25.0
        objs.append(ob)
    return objs, x


def main():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.unit_settings.scale_length = 0.001
    boven, b1 = lees(os.path.join(bron, model, "plat_uit"), 260.0)
    onder, b2 = lees(os.path.join(bron, model, "plat_aan"), 0.0)
    if not boven or not onder:
        log(f"SCHERM FOUT plat-{model}: geen STL-bestanden")
        return
    breed = max(b1, b2)
    bpy.ops.mesh.primitive_plane_add(size=1.0, location=(breed / 2 - 20, 130.0, -0.5))
    bed = bpy.context.active_object
    bed.scale = (breed + 60, 620.0, 1)
    bed.color = (0.32, 0.33, 0.36, 1)
    kader(boven + onder, Vector((0.0, -1.0, 0.75)), lens=50, marge=0.04)
    render(f"plat-{model}.png")


main()
