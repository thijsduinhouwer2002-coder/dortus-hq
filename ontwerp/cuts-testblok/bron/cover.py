"""Cover gratis testblok Click Cuts voor Printables, Thingiverse en Cults3D (Beeldmaker, 28 nov 2026, issue #423).

blender -b --factory-startup --python cover.py -- <hoofdbeeld.py> <click_cuts.zip> <uit.png> <json> [samples] [schaal%]

Precies wat in de download zit: het blok en de vier pennen uit de echte knop Make fit test van Click Cuts
(printer Bambu Lab A1, PLA, speling 0,20 mm, pen 5 mm). Voor het beeld staat één pen van de add-on boven het gat
0.20, de andere drie staan voor het blok. Render, geen foto van een print. Geen AI-beeld.
Omgeving: TB_DRAAI, TB_HOOG (camera), TB_LENS, TB_F (scherptediepte), TB_KLEUR (blok), TB_ZWEEF (mm boven het gat).
"""
import json
import os
import sys

import bmesh
import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

a = sys.argv[sys.argv.index("--") + 1:]
HB = a[0]
UIT_PNG, META_JSON = a[2], a[3]
SAMPLES = int(a[4]) if len(a) > 4 else 64
SCHAAL = int(a[5]) if len(a) > 5 else 100
sys.argv = [sys.argv[0], "--", a[1], "-", "-", "-"]
bron = open(HB).read().rsplit("\nmain()", 1)[0]
_bewaar = (UIT_PNG, META_JSON, SAMPLES, SCHAAL)
exec(compile(bron, HB, "exec"))  # noqa: S102  plastic(), goud(), studio(), camera(), punten(), srgb() ...
UIT_PNG, META_JSON, SAMPLES, SCHAAL = _bewaar
BX, BY = 1600, 1200
E = os.environ.get


def los_in_delen(ob):
    """Pennen-object van de add-on in losse pennen (elk eigen object, oorsprong in het midden van de voet)."""
    bpy.ops.object.select_all(action="DESELECT")
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob
    bpy.ops.mesh.separate(type="LOOSE")
    delen = [o for o in bpy.context.selected_objects]
    for o in delen:
        ps = [v.co for v in o.data.vertices]
        c = Vector((sum(p.x for p in ps) / len(ps), sum(p.y for p in ps) / len(ps), min(p.z for p in ps)))
        o.data.transform(__import__("mathutils").Matrix.Translation(-c))
        o.location = o.location + c
    return sorted(delen, key=lambda o: (o.location.y, o.location.x))


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
    pen_ob = next(o for o in s.objects if o.get("sj_passing") == "pennen")
    gaten = json.loads(blok["sj_gaten"])
    spel = list(blok["sj_spelingen"])
    pd, pl = float(blok["sj_pen_d"]), float(blok["sj_pen_lengte"])
    log("passing", r, "spelingen", spel, "gaten", len(gaten), "dicht", blok.get("sj_gesloten"))
    m = plastic("blok", srgb(E("TB_KLEUR", "F2994A")), rough=0.5, coat=0.1)
    pm = plastic("pen", srgb(E("TB_PENKLEUR", "4F7BFF")), rough=0.45, coat=0.15)
    blok.data.materials.clear()
    blok.data.materials.append(m)
    for f in blok.data.polygons:
        f.use_smooth = False
    ps = [blok.matrix_world @ v.co for v in blok.data.vertices]
    lo = Vector([min(p[i] for p in ps) for i in range(3)])
    hi = Vector([max(p[i] for p in ps) for i in range(3)])
    mid = Vector(((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, 0))
    blok.location -= mid
    pen_ob.location -= mid
    bpy.context.view_layer.update()
    gaten = [dict(g, p=[g["p"][0] - mid.x, g["p"][1] - mid.y, g["p"][2]]) for g in gaten]
    lo -= mid
    hi -= mid
    pens = los_in_delen(pen_ob)
    log("pennen", len(pens))
    for p in pens:
        p.data.materials.clear()
        p.data.materials.append(pm)
        for f in p.data.polygons:
            f.use_smooth = True
    # één pen boven het gat 0.20 (half erin), drie voor het blok op een rij
    doel = int(E("TB_GAT", "1"))
    g = gaten[doel]
    zweef = float(E("TB_ZWEEF", "5"))
    pens[0].location = Vector((g["p"][0], g["p"][1], g["p"][2] - g["diepte"] + zweef + g["diepte"]))
    voor_y = lo.y - pd * float(E("TB_VOOR", "2.2"))
    rest = pens[1:]
    for i, p in enumerate(rest):
        gx = gaten[[0, 2, 3][i]]["p"][0]
        p.location = Vector((gx, voor_y, 0.0))
    bpy.context.view_layer.update()
    alles = [blok] + pens
    pts = punten(alles)
    maat = (Vector([max(q[i] for q in pts) for i in range(3)]) - Vector([min(q[i] for q in pts) for i in range(3)])).length
    studio(maat * 1.2)
    ld = bpy.data.lights.new("strijk", "AREA")
    ld.shape, ld.size = "DISK", maat * 0.4
    ld.energy = float(E("TB_STRIJK", "1.2e6")) * (maat / 300) ** 2
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
    richting = Vector((float(E("TB_DRAAI", "0.35")), -1.0, float(E("TB_HOOG", "0.9"))))
    xb = [float(v) for v in E("TB_XB", "0.08,0.92").split(",")]
    yb = [float(v) for v in E("TB_YB", "0.12,0.66").split(",")]
    cam = camera(alles, richting, xb, yb, lens=float(E("TB_LENS", "85")))
    cam.data.dof.use_dof = True
    cam.data.dof.focus_distance = (cam.location - top).length
    cam.data.dof.aperture_fstop = float(E("TB_F", "8"))
    bpy.context.view_layer.update()

    def beeld(p):
        q = world_to_camera_view(s, cam, Vector(p))
        return [round(q.x, 4), round(1 - q.y, 4)]

    uv = [world_to_camera_view(s, cam, p) for p in punten(alles)]
    meta = {"knop": "Make fit test (Click Cuts, zip van main)", "printer": PRINTER, "materiaal": "PLA",
            "pen_d_mm": pd, "pen_lengte_mm": pl, "spelingen_mm": spel, "gaten": len(gaten), "pennen": len(pens),
            "blok_mm": [round(v, 1) for v in (hi - lo)], "waterdicht": bool(blok.get("sj_gesloten")),
            "gat_pen": beeld(g["p"]), "pen_top": beeld(pens[0].location + Vector((0, 0, pl))),
            "vak": [min(q.x for q in uv), max(q.x for q in uv), 1 - max(q.y for q in uv), 1 - min(q.y for q in uv)]}
    with open(META_JSON, "w") as f:
        json.dump(meta, f, indent=1)
    log("meta", json.dumps(meta))
    s.render.filepath = UIT_PNG
    bpy.ops.render.render(write_still=True)
    log("klaar", UIT_PNG)


main()
