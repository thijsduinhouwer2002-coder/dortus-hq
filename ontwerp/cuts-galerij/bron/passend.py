"""Galerijbeeld Click Cuts "Pins that fit your printer" (Beeldmaker, 25 nov 2026, issue #39).

blender -b --factory-startup --python passend.py -- <hoofdbeeld.py> <click_cuts.zip> <modelmap> <uit.png> <json> [samples] [schaal%]

Het proefblokje uit de echte knop Make fit test van Click Cuts (zip van main, printer Bambu Lab A1, PLA, speling
0,20 mm): je eigen pen op vier spelingen, de spelingen gegraveerd voor elk gat. De add-on maakt het blok en de pennen;
alleen voor het beeld staan gouden pennen half in drie gaten en ligt er één voor het blok. Geen model nodig (de
modelmap gaat alleen door naar hoofdbeeld.py). Het beeld is een render, geen foto van een print.
Omgeving: PB_HOOG, PB_DRAAI (camera), PB_LENS, PB_F (scherptediepte), PB_X0 (linkerrand van het blok in beeld).
"""
import json
import math
import os
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

a = sys.argv[sys.argv.index("--") + 1:]
HB = a[0]
UIT_PNG, META_JSON = a[3], a[4]
SAMPLES = int(a[5]) if len(a) > 5 else 64
SCHAAL = int(a[6]) if len(a) > 6 else 100
sys.argv = [sys.argv[0], "--"] + a[1:]
bron = open(HB).read().rsplit("\nmain()", 1)[0]
_bewaar = (UIT_PNG, META_JSON, SAMPLES, SCHAAL)
exec(compile(bron, HB, "exec"))  # noqa: S102  plastic(), goud(), studio(), camera(), punten(), srgb() ...
UIT_PNG, META_JSON, SAMPLES, SCHAAL = _bewaar


def pen(mat, d, lengte, plek, liggend=False):
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=d / 2, depth=lengte)
    p = bpy.context.active_object
    bv = p.modifiers.new("afschuin", "BEVEL")
    bv.width, bv.segments = 0.4, 3
    p.data.materials.append(mat)
    for f in p.data.polygons:
        f.use_smooth = True
    if liggend:
        p.rotation_euler = (0, math.pi / 2, math.radians(12))
    p.location = plek
    p["pb_pen"] = 1
    return p


def main():
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    s = bpy.context.scene
    for o in list(s.objects):
        bpy.data.objects.remove(o)
    s.unit_settings.system = "METRIC"
    s.unit_settings.scale_length = 0.001
    s.unit_settings.length_unit = "MILLIMETERS"
    inst = s.split_joints
    inst.printer, inst.materiaal, inst.speling_mm = PRINTER, "PLA", 0.2
    r = bpy.ops.split_joints.passing_maak()
    blok = next(o for o in s.objects if o.get("sj_passing") == "blok")
    addon_pennen = next(o for o in s.objects if o.get("sj_passing") == "pennen")
    gaten = json.loads(blok["sj_gaten"])
    spel = list(blok["sj_spelingen"])
    log("passing", r, "spelingen", spel, "gaten", len(gaten), "dicht", blok.get("sj_gesloten"))
    pd, pl = float(blok["sj_pen_d"]), float(blok["sj_pen_lengte"])
    addon_pennen.hide_render = True
    addon_pennen.hide_set(True)
    # blok: kleur van stuk 1 uit het hoofdbeeld (oranje van Dortus), gravure leest door strijklicht
    m = plastic("blok", srgb(os.environ.get("PB_KLEUR", "F2994A")), rough=0.5, coat=0.1)
    blok.data.materials.clear()
    blok.data.materials.append(m)
    for f in blok.data.polygons:
        f.use_smooth = False
    ps = [blok.matrix_world @ v.co for v in blok.data.vertices]
    lo = Vector([min(p[i] for p in ps) for i in range(3)])
    hi = Vector([max(p[i] for p in ps) for i in range(3)])
    # alles naar het midden
    mid = Vector(((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, 0))
    blok.location -= mid
    bpy.context.view_layer.update()
    gaten = [dict(g, p=[g["p"][0] - mid.x, g["p"][1] - mid.y, g["p"][2]]) for g in gaten]
    lo -= mid
    hi -= mid
    mat = goud()
    pens = []
    leeg = [int(x) for x in os.environ.get("PB_LEEG", "2").split(",") if x != ""]
    for i, g in enumerate(gaten):
        if i in leeg:
            continue
        # half in het gat: de pen steekt de helft van zijn lengte boven het vlak uit
        p = Vector(g["p"]) + Vector((0, 0, pl / 2 - g["diepte"] + float(os.environ.get("PB_UIT", "3"))))
        pens.append(pen(mat, pd, pl, p))
    # de pen van het lege gat ligt voor het blok
    for i in leeg:
        g = gaten[i]
        pens.append(pen(mat, pd, pl, Vector((g["p"][0] + 2, lo.y - pd * 1.6, pd / 2)), liggend=True))
    bpy.context.view_layer.update()
    maat = (hi - lo).length
    studio(maat * 1.2)
    # strijklicht van links laag over het bovenvlak, zodat de gravure en de gaten lezen
    ld = bpy.data.lights.new("strijk", "AREA")
    ld.shape, ld.size = "DISK", maat * 0.4
    ld.energy = float(os.environ.get("PB_STRIJK", "1.2e6")) * (maat / 300) ** 2
    ld.color = srgb("FFF0DA")[:3]
    sl = bpy.data.objects.new("strijk", ld)
    s.collection.objects.link(sl)
    top = Vector((0, 0, hi.z))
    sl.location = top + Vector((-maat * 1.1, -maat * 0.5, maat * 0.35))
    sl.rotation_euler = (top - sl.location).to_track_quat("-Z", "Y").to_euler()

    s.render.engine = "CYCLES"
    s.cycles.device = "CPU"
    s.cycles.samples = SAMPLES
    s.cycles.use_denoising = True
    s.cycles.max_bounces = 6
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = BX, BY, SCHAAL
    s.view_settings.view_transform = "AgX"
    try:
        s.view_settings.look = "AgX - Punchy"
    except Exception:  # noqa: BLE001
        pass
    richting = Vector((float(os.environ.get("PB_DRAAI", "0.35")), -1.0, float(os.environ.get("PB_HOOG", "1.1"))))
    x0 = float(os.environ.get("PB_X0", "0.46"))
    cam = camera([blok] + pens, richting, (x0, 0.97), (float(os.environ.get("PB_Y0", "0.10")), 0.90),
                 lens=float(os.environ.get("PB_LENS", "100")))
    cam.data.dof.use_dof = True
    cam.data.dof.focus_distance = (cam.location - top).length
    cam.data.dof.aperture_fstop = float(os.environ.get("PB_F", "5.6"))
    bpy.context.view_layer.update()

    def beeld(p):
        q = world_to_camera_view(s, cam, Vector(p))
        return [round(q.x, 4), round(1 - q.y, 4)]

    nummers = [{"speling": g["speling"], "gat": beeld(g["p"]),
                "tekst": beeld((g["p"][0], g["p"][1] - (g["r_gat"] + 1.5 + 2.0), g["p"][2]))} for g in gaten]
    uv = [world_to_camera_view(s, cam, p) for p in punten([blok] + pens)]
    meta = {"knop": "Make fit test (Click Cuts, zip van main)", "printer": PRINTER, "materiaal": "PLA",
            "pen_d_mm": pd, "pen_lengte_mm": pl, "spelingen_mm": spel, "gaten": len(gaten),
            "blok_mm": [round(v, 1) for v in (hi - lo)], "waterdicht": bool(blok.get("sj_gesloten")),
            "nummers": nummers,
            "vak": [min(q.x for q in uv), max(q.x for q in uv), 1 - max(q.y for q in uv), 1 - min(q.y for q in uv)]}
    with open(META_JSON, "w") as f:
        json.dump(meta, f, indent=1)
    log("meta", json.dumps(meta))
    s.render.filepath = UIT_PNG
    bpy.ops.render.render(write_still=True)
    log("klaar", UIT_PNG)


main()
