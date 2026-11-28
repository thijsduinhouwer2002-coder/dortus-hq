"""YouTube-miniatuur Click Joints Pro (issue #346, Beeldmaker, 28 nov 2026).

Opent de .blend die hoofdbeeld.py met HB_BEWAAR=1 bewaarde (held uit ronde 3/4, alle delen gemaakt door de echte knop
Figure from rig van Pro) en zet alleen de kogels van de heupen in goud, zoals kom_kogel.py doet. Vorm en plek blijven
die van de add-on. Render zonder tekst; tekst komt erop met tekst.py (Pillow).

    blender -b <hoofdbeeld.blend> --python miniatuur.py -- <uitmap> [samples] [schaal%]
Variabelen: MN_METAAL (glans van het goud, standaard 0.25), MN_LENS_X (lens maal dit), MN_SHIFT=x,y.
"""
import bpy, os, sys, json, time
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:]
UIT = args[0]
SAMPLES = int(args[1]) if len(args) > 1 else 64
SCHAAL = int(args[2]) if len(args) > 2 else 100
os.makedirs(UIT, exist_ok=True)
sc = bpy.context.scene
meting = {}
delen = [o for o in sc.objects if o.type == "MESH" and o.get("cj_figuur") and not o.hide_render]
meting["delen"] = len(delen)
goud = bpy.data.materials["hb_goud"]
bs = next(n for n in goud.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
bs.inputs["Metallic"].default_value = float(os.environ.get("MN_METAAL", "0.25"))
kogels = [(Vector(o["cj_centrum"]), float(o["cj_kogel_r"]), o["cj_naam"]) for o in delen
          if o.get("cj_soort") == "KOGEL" and o.get("cj_deel") == "B" and str(o.get("cj_naam", "")).endswith("hip")]
meting["kogels"] = [(n, round(2 * r, 2)) for _c, r, n in kogels]
tel = 0
for o in delen:
    if o.get("cj_deel") == "B" and str(o.get("cj_naam", "")).endswith("hip"):
        continue   # de dij zelf: daar zit de kom al in goud
    loc = [(c, r) for c, r, _n in kogels]   # de mesh staat in rusthouding; pose en uit elkaar zitten in de matrix
    hits = [p.index for p in o.data.polygons if any((p.center - kc).length < kr * 1.06 for kc, kr in loc)]
    if not hits:
        continue
    if "hb_goud" not in [getattr(m, "name", "") for m in o.data.materials]:
        o.data.materials.append(goud)
    gi = [getattr(m, "name", "") for m in o.data.materials].index("hb_goud")
    for i in hits:
        o.data.polygons[i].material_index = gi
    tel += len(hits)
    o.data.update()
meting["kogel_vlakken_goud"] = tel
cam = sc.camera
cd = cam.data
cd.lens *= float(os.environ.get("MN_LENS_X", "1"))
if os.environ.get("MN_SHIFT"):
    cd.shift_x, cd.shift_y = (float(v) for v in os.environ["MN_SHIFT"].split(","))
sc.cycles.samples = SAMPLES
sc.render.resolution_percentage = SCHAAL
sc.render.filepath = os.path.join(UIT, "miniatuur-render.png")
t0 = time.time()
bpy.ops.render.render(write_still=True)
meting["render_s"] = round(time.time() - t0, 1)
json.dump(meting, open(os.path.join(UIT, "miniatuur.json"), "w"), indent=1)
print("[miniatuur] klaar", meting, flush=True)
