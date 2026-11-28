"""Zet in de rig van het held-figuur een Limit Rotation (X, lokaal) op de knieën: 0 tot KG_GRADEN (standaard 115).
Zo leest de echte knop Figure from rig de eindstop uit de rig ("from rig"), zoals een koper die zijn rig begrenst.
    blender -b <held.blend> --python knie_grens.py -- <uit.blend>
"""
import math, os, sys, bpy
uit = sys.argv[sys.argv.index("--") + 1]
g = math.radians(float(os.environ.get("KG_GRADEN", "115")))
arm = next(o for o in bpy.data.objects if o.type == "ARMATURE")
for n in ("shin.L", "shin.R"):
    pb = arm.pose.bones[n]
    c = pb.constraints.new("LIMIT_ROTATION")
    c.use_limit_x = True; c.min_x = 0.0; c.max_x = g; c.owner_space = "LOCAL"
    print("GRENS", n, round(math.degrees(g), 1))
bpy.ops.wm.save_as_mainfile(filepath=uit)
