import sys, os
sys.path.insert(0, "/home/claude/dortus-hq/producten/steam-hol/modellen")
import bpy, held, hoeden, gedeeld as g
from mathutils import Vector
uit = sys.argv[1]
g.leeg()
paren = [("ridder", 0), ("heks", 1), ("ridder", 4), ("heks", 2), ("ridder", 7), ("heks", 5), ("ridder", 6), ("heks", 8), ("ridder", 9), ("heks", 3)]
for i, (soort, nr) in enumerate(paren):
    x = (i - 4.5) * 1.5
    voor = set(bpy.data.objects)
    DR = float(os.environ.get("HELD_DRAAI", "20"))
    h = held.bouw(soort, "rust", (x, 0, 0), draai=DR)
    bpy.context.view_layer.update()
    for o in list(bpy.data.objects):
        if o not in voor and o.name.startswith("hoed_"):
            bpy.data.objects.remove(o)
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    hoog, hx = -9, x
    for o in bpy.data.objects:
        if o in voor or o.type != "MESH" or o.hide_render: continue
        e = o.evaluated_get(dg)
        for v in e.data.vertices:
            w = e.matrix_world @ v.co
            if abs(w.x - x) < 0.3 and w.z > hoog:
                hoog, hx = w.z, w.x
    # Daan 13 nov 21:40: HOED_DRAAI=1 laat de hoed mee draaien met de held, HOED_HAP=1 geeft elke hoed een hap
    hoeden.bouw(nr, (x, 0, hoog - 0.08), schaal=float(os.environ.get("HOED_SCHAAL", "1.3")),
                draai=DR if os.environ.get("HOED_DRAAI") == "1" else 0, hap=os.environ.get("HOED_HAP") == "1")
bpy.ops.mesh.primitive_plane_add(size=40); bpy.context.object.is_shadow_catcher = True
g.camera(hoogte_midden=1.25, schaal=15.5)
g.licht()
g.render(uit, int(sys.argv[2]), int(sys.argv[3]), 24, doorzichtig=True)
