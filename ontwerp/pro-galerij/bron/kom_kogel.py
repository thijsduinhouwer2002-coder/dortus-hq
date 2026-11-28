"""Galerijbeeld Click Joints Pro: kom en kogel van de heup, met het echte gaas (issue #331, Beeldmaker, 28 nov 2026).

Waarom: Gemini vroeg in beide rondes van held-knie-r4 om "a close-up of the resulting mesh topology around the
socket". Dit script opent de .blend die hoofdbeeld.py met HB_BEWAAR=1 bewaart (de held uit r4, alle delen gemaakt
door de echte knop Figure from rig van Pro), laat alleen romp en linkerdij zien, schuift de dij langs de as van het
gewricht naar beneden (uit elkaar) en kantelt hem naar de camera zodat je in de kom kijkt. Over de vlakken komt het
echte gaas als dunne lijnen (Wireframe-modifier op een kopie, alleen voor het beeld). Vorm en gaas zijn die van de
add-on; alleen kleur, plek en stand veranderen.

    blender -b <hoofdbeeld.blend> --python kom_kogel.py -- <uitmap> [samples] [schaal%]
Uit: kom-kogel-render.png (1920x1080, zonder tekst) en kom-kogel.json (maten uit de add-on, open randen per deel,
en waar kogel, kom en snederand in beeld staan, voor tekst.py).
Variabelen: KK_GEWRICHT (standaard Left hip), KK_UIT (mm uit elkaar langs de as), KK_KANTEL (graden dat de dij naar de
camera kantelt), KK_CAM (afstand,draai,hoogte in mm en graden), KK_DOEL (x,y,z verschuiving van het midden in mm),
KK_LENS, KK_GAAS (lijndikte in mm), KK_GAAS_ALFA, KK_MAAT (breedtexhoogte, standaard 1920x1080).
"""
import json
import math
import os
import sys
import time

import bmesh
import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Matrix, Vector

args = sys.argv[sys.argv.index("--") + 1:]
UIT = args[0]
SAMPLES = int(args[1]) if len(args) > 1 else 64
SCHAAL = int(args[2]) if len(args) > 2 else 100
os.makedirs(UIT, exist_ok=True)
NAAM = os.environ.get("KK_GEWRICHT", "Left hip")
meting = {"gewricht": NAAM}


def log(*a):
    print("[kom_kogel]", *a, flush=True)


def srgb(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c) + (1.0,)


def open_randen(o):
    bm = bmesh.new()
    bm.from_mesh(o.data)
    n = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return n


sc = bpy.context.scene
delen = [o for o in sc.objects if o.type == "MESH" and o.get("cj_figuur") and not o.hide_render]
meting["delen"] = len(delen)
meting["open_randen"] = {o.name: open_randen(o) for o in delen}   # zelfde maat als gesloten.foute_randen
log("open randen", meting["open_randen"])

# het deel B van dit gewricht (de dij) en het deel waar de kogel aan zit (de romp: meeste punten op de kogel)
dij = next(o for o in delen if o.get("cj_naam") == NAAM and o.get("cj_deel") == "B")
c = Vector(dij["cj_centrum"])
as_ = Vector(dij["cj_as"]).normalized()
r = float(dij["cj_kogel_r"])
meting.update({"kogel_r_mm": round(r, 3), "kogel_d_mm": round(2 * r, 2), "speling_mm": round(float(dij["cj_speling_mm"]), 3),
               "speling_gemeten_mm": round(float(dij.get("cj_speling_gemeten_mm", 0)), 4),
               "naad_r_mm": round(float(dij.get("cj_naad_r", 0)), 2), "graden": float(dij.get("cj_hoek", 0)),
               "grens_graden": float(dij.get("cj_grens_graden", 0))})


def bij_kogel(o):
    mw = o.matrix_world
    return sum(1 for v in o.data.vertices if ((mw @ v.co) - c).length < r + 0.6)


romp = max((o for o in delen if o is not dij), key=bij_kogel)
meting["kogel_op"], meting["kom_in"] = romp.name, dij.name
for o in sc.objects:
    if o not in (romp, dij):
        o.hide_render = True
romp.hide_render = dij.hide_render = False
ANDER = [n for n in os.environ.get("KK_ANDER", "").split(",") if n]   # andere delen B die op hun plek blijven (de rechterdij)
ander = [o for o in delen if o.get("cj_naam") in ANDER and o.get("cj_deel") == "B"]
for o in ander:
    o.hide_render = False
meting["op_plek"] = [o.name for o in ander]
MEE = [n for n in os.environ.get("KK_MEE", "").split(",") if n]   # delen B die met de dij mee bewegen (het linkeronderbeen)
mee = [o for o in delen if o.get("cj_naam") in MEE and o.get("cj_deel") == "B"]
for o in mee:
    o.hide_render = False
meting["mee"] = [o.name for o in mee]
meting["punten"] = {romp.name: len(romp.data.vertices), dij.name: len(dij.data.vertices)}

# kogel in goud (alleen kleur): vlakken van de romp op de kogel, zoals de kom in de dij al goud is
goud = bpy.data.materials["hb_goud"]
bs = next(n for n in goud.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
bs.inputs["Metallic"].default_value = float(os.environ.get("KK_METAAL", "0.25"))
if "hb_goud" not in [m.name for m in romp.data.materials if m]:
    romp.data.materials.append(goud)
gi = [getattr(m, "name", "") for m in romp.data.materials].index("hb_goud")
tel = 0
kogels = [(Vector(o["cj_centrum"]), float(o["cj_kogel_r"])) for o in delen
          if o.get("cj_soort") == "KOGEL" and o.get("cj_deel") == "B" and str(o.get("cj_naam", "")).endswith("hip")]
for p in romp.data.polygons:
    if any((p.center - kc).length < kr * 1.06 for kc, kr in kogels):
        p.material_index = gi
        tel += 1
meting["kogel_vlakken_goud"] = tel

# snijvlakken die nog antraciet of zonder kleur zijn: de kleur van hun eigen deel, iets donkerder (zoals HB_NEK_TINT)
f = float(os.environ.get("KK_SNEDE_TINT", "0.72"))
for o in [romp, dij] + ander + mee:
    mats = list(o.data.materials)
    donker = {i for i, m in enumerate(mats) if m is None or m.name in ("toy_donker", "studio_gewricht") or m.name.startswith("Click Joints")}
    eigen = next(m for m in mats if m is not None and m.name.startswith("hb_deel_") and not m.name.endswith("_nek"))
    g = eigen.copy()
    g.name = eigen.name + "_snede"
    b = next(n for n in g.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    kl = b.inputs["Base Color"].default_value
    b.inputs["Base Color"].default_value = (kl[0] * f, kl[1] * f, kl[2] * f, 1)
    o.data.materials.append(g)
    si = len(o.data.materials) - 1
    n = 0
    for p in o.data.polygons:
        if p.material_index in donker:
            p.material_index = si
            n += 1
    meting.setdefault("snede_vlakken", {})[o.name] = n

# dij uit elkaar langs de as en gekanteld naar de camera, om een punt bovenin de dij
uit = float(os.environ.get("KK_UIT", "24"))
kantel = math.radians(float(os.environ.get("KK_KANTEL", "38")))
cam_d, cam_draai, cam_hoog = (float(v) for v in os.environ.get("KK_CAM", "150,28,-6").split(","))
draai = math.radians(cam_draai)
naar_cam = Vector((math.sin(draai), -math.cos(draai), 0)).normalized()
kant_as = as_.cross(naar_cam).normalized()          # kantel om deze as: de opening van de kom draait naar de camera
M = (Matrix.Translation(c + as_ * uit) @ Matrix.Rotation(-kantel, 4, kant_as) @ Matrix.Translation(-c))
dij.matrix_world = M @ dij.matrix_world
for o in mee:
    o.matrix_world = M @ o.matrix_world
kom = M @ c                                          # midden van de kom na de stap
meting["uit_mm"], meting["kantel_graden"] = uit, round(math.degrees(kantel), 1)

# gaas: kopie met Wireframe-modifier, alleen voor het beeld
dik = float(os.environ.get("KK_GAAS", "0.07"))
alfa = float(os.environ.get("KK_GAAS_ALFA", "0.55"))
lijn = bpy.data.materials.new("kk_gaas")
lijn.use_nodes = True
nt = lijn.node_tree
for n in list(nt.nodes):
    nt.nodes.remove(n)
out = nt.nodes.new("ShaderNodeOutputMaterial")
mix = nt.nodes.new("ShaderNodeMixShader")
tr = nt.nodes.new("ShaderNodeBsdfTransparent")
df = nt.nodes.new("ShaderNodeBsdfPrincipled")
df.inputs["Base Color"].default_value = srgb(os.environ.get("KK_GAAS_KLEUR", "22162B"))
df.inputs["Roughness"].default_value = 0.6
mix.inputs[0].default_value = alfa
nt.links.new(tr.outputs[0], mix.inputs[1])
nt.links.new(df.outputs[0], mix.inputs[2])
nt.links.new(mix.outputs[0], out.inputs["Surface"])
for o in [romp, dij] + ander + mee:
    k = o.copy()
    k.data = o.data.copy()
    k.data.materials.clear()
    k.data.materials.append(lijn)
    sc.collection.objects.link(k)
    w = k.modifiers.new("gaas", "WIREFRAME")
    w.thickness = dik
    w.offset = 1.0
    w.use_even_offset = True
    w.use_replace = True
    w.use_boundary = True
    k.visible_shadow = False
    k.hide_render = False
    k.name = "kk_gaas_" + o.name

# wereld, vloer weg, licht
for nm in ("hb_vloer", "hb_wand"):
    if nm in sc.objects:
        sc.objects[nm].hide_render = True
for o in list(sc.objects):
    if o.type == "LIGHT":
        o.hide_render = True
wl = sc.world
bg = next(n for n in wl.node_tree.nodes if n.type == "BACKGROUND")
bg.inputs[0].default_value = srgb("140C1A")
bg.inputs[1].default_value = 1.0

dx, dy, dz = (float(v) for v in os.environ.get("KK_DOEL", "0,0,-12").split(","))
doel = (c + kom) / 2 + Vector((dx, dy, dz))
richting = Vector((math.sin(draai) * math.cos(math.radians(cam_hoog)), -math.cos(draai) * math.cos(math.radians(cam_hoog)),
                   math.sin(math.radians(cam_hoog))))


def lamp(naam, plek, maat, kracht, kleur):
    ld = bpy.data.lights.new(naam, "AREA")
    ld.shape = "DISK"
    ld.size = maat
    ld.energy = kracht
    ld.color = srgb(kleur)[:3]
    lo = bpy.data.objects.new(naam, ld)
    sc.collection.objects.link(lo)
    lo.location = plek
    lo.rotation_euler = (doel - Vector(plek)).to_track_quat("-Z", "Y").to_euler()
    lo.visible_glossy = False
    return lo


k = float(os.environ.get("KK_LICHT", "1.0"))
links = naar_cam.cross(Vector((0, 0, 1))).normalized()
lamp("kk_key", doel + naar_cam * 160 + links * 140 + Vector((0, 0, 150)), 140, 9.0e4 * k, "FFF3E2")
lamp("kk_vul", doel + naar_cam * 170 - links * 170 + Vector((0, 0, 20)), 200, 2.5e4 * k, "C9D8FF")
lamp("kk_rand_goud", doel - naar_cam * 140 + links * 130 + Vector((0, 0, 60)), 70, 6.0e4 * k, "FFB547")
lamp("kk_rand_blauw", doel - naar_cam * 140 - links * 130 + Vector((0, 0, 80)), 70, 6.0e4 * k, "5FA8FF")
lamp("kk_onder", doel + naar_cam * 90 + Vector((0, 0, -120)), 120, 1.6e4 * k, "FFD9A8")

cd = bpy.data.cameras.new("kk_cam")
cd.lens = float(os.environ.get("KK_LENS", "85"))
cd.sensor_width = 36
cd.clip_start, cd.clip_end = 1, 5000
cam = bpy.data.objects.new("kk_cam", cd)
sc.collection.objects.link(cam)
sc.camera = cam
cam.location = doel + richting * cam_d
cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
cd.shift_x = float(os.environ.get("KK_SHIFT", "-0.18"))
cd.dof.use_dof = bool(os.environ.get("KK_DOF"))
if cd.dof.use_dof:
    cd.dof.focus_distance = (doel - cam.location).length
    cd.dof.aperture_fstop = float(os.environ["KK_DOF"])
RW, RH = (int(v) for v in os.environ.get("KK_MAAT", "1920x1080").split("x"))   # 2400x1200 voor Superhive (#338 M2)
sc.render.resolution_x, sc.render.resolution_y = RW, RH
sc.render.resolution_percentage = SCHAAL
sc.render.use_border = False
sc.render.film_transparent = bool(os.environ.get("KK_DOORZICHTIG"))   # achtergrond komt dan uit tekst.py
sc.render.engine = "CYCLES"
sc.cycles.samples = SAMPLES
sc.cycles.use_denoising = True
sc.view_settings.view_transform = "AgX"
try:
    sc.view_settings.look = "AgX - Medium High Contrast"
except Exception:  # noqa: BLE001
    pass
bpy.context.view_layer.update()


def px(w):
    q = world_to_camera_view(sc, cam, w)
    return [round(q.x * RW, 1), round((1 - q.y) * RH, 1)]


# ankerpunten voor de labels: onderkant van de kogel, midden van de kom, rand van de snede op de dij
rand = M @ (c + as_ * 0.0)
meting["beeld"] = {"kogel": px(c + as_ * r * 0.6), "kogel_midden": px(c), "kom": px(kom), "rand_dij": px(M @ (c + kant_as * meting["naad_r_mm"] * 0.9)),
                   "romp_snede": px(c - kant_as * meting["naad_r_mm"] * 0.9 - as_ * 2)}
pad = os.path.join(UIT, "kom-kogel-render.png")
sc.render.filepath = pad
sc.render.image_settings.file_format = "PNG"
sc.render.image_settings.color_mode = "RGBA" if sc.render.film_transparent else "RGB"
t0 = time.time()
bpy.ops.render.render(write_still=True)
meting["render_s"] = round(time.time() - t0, 1)
json.dump(meting, open(os.path.join(UIT, "kom-kogel.json"), "w"), indent=1, ensure_ascii=False)
log("klaar", pad, meting)
