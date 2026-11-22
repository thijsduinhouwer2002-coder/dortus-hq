"""Fit test strip als losse STL (opdracht Afkijker 22 nov, plek: gratis op dortus.com, besluit hoofdchat 12:40).

Gebruik (vanuit producten/blender-gewrichten):
  bash e2e/maak_zip.sh betaald
  blender -b --factory-startup --python ../../commercie/blender-click-joints/testprint/maak_strip.py -- <uitmap>

Wat het doet:
1. Pro installeren, scene in mm, knop "Fit test: ball" (standaard) met de echte code `betaald/testkaart.py`.
   Het getal in reliëf van Pro zetten we hier uit: het zou bij het printen op het bed liggen.
2. Per paar het getal 0,6 mm ingegraveerd in het platte eind van beide delen (A onder, B boven), zodat je na het
   printen weet welke A bij welke B hoort. Gesloten na de snede, anders zonder getal (en melden).
3. Klaar om te printen: A-delen staan zoals ze zijn (plat eind op het bed), B-delen 180 graden om X gekanteld met
   het platte eind op het bed (les keuring echte print A4: anders support in de kom). Rij A voor, rij B erachter.
4. Schrijft fit-test-strip.stl en, als testset-4-delen.stl naast dit script staat, fit-test-strip-plus-testset.stl.
"""
import importlib
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
UIT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else HIER
ZIP = "/tmp/click_joints_betaald.zip"
DIEP_MM = 0.6   # zo diep gaat het getal in het deel
UIT_MM = 0.3    # zo ver steekt de snijvorm buiten het vlak (geen samenvallende vlakken)
RIJ_MM = 12.0   # ruimte tussen rij A en rij B

bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
cj = importlib.import_module("bl_ext.user_default.click_joints")
sys.modules.setdefault("click_joints", cj)
tk = importlib.import_module("bl_ext.user_default.click_joints.betaald.testkaart")
gesloten = importlib.import_module("bl_ext.user_default.click_joints.gesloten").is_gesloten

for ob in list(bpy.data.objects):
    bpy.data.objects.remove(ob)
us = bpy.context.scene.unit_settings
us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"

tk._zet_getal = lambda *a, **k: True  # geen reliëf: wij graveren straks zelf
uit = bpy.ops.click_joints.testkaart(soort="KOGEL")
print("KNOP", uit)
delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
assert len(delen) == 10, f"verwacht 10 delen, kreeg {len(delen)}"


def toepassen(ob):
    """Wereldmatrix in de mesh, zodat we in wereld-mm rekenen."""
    ob.data.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)


def graveer(deel, tekst, onder):
    pts = [v.co for v in deel.data.vertices]
    zmin, zmax = min(p.z for p in pts), max(p.z for p in pts)
    mx = (min(p.x for p in pts) + max(p.x for p in pts)) / 2
    my = (min(p.y for p in pts) + max(p.y for p in pts)) / 2
    cu = bpy.data.curves.new("cj_strip_tekst", "FONT")
    cu.body = tekst
    cu.size = tk.LETTER_MM
    cu.align_x, cu.align_y = "CENTER", "CENTER"
    cu.extrude = (DIEP_MM + UIT_MM) / 2
    cu.fill_mode = "BOTH"
    tijd = bpy.data.objects.new("cj_strip_tekst", cu)
    bpy.context.scene.collection.objects.link(tijd)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(tijd.evaluated_get(dg))
    bpy.data.objects.remove(tijd)
    bpy.data.curves.remove(cu)
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
    if onder:  # van onderen gelezen: spiegelen, zodat het goed leest als je het deel omdraait
        bmesh.ops.scale(bm, vec=(-1, 1, 1), verts=bm.verts)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()
    getal = bpy.data.objects.new("cj_strip_getal", me)
    h = DIEP_MM + UIT_MM
    z = (zmin - UIT_MM + h / 2) if onder else (zmax + UIT_MM - h / 2)
    getal.location = (mx, my, z)
    bpy.context.scene.collection.objects.link(getal)
    m = deel.modifiers.new("cj_graveer", "BOOLEAN")
    m.operation, m.object, m.solver = "DIFFERENCE", getal, "EXACT"
    dg = bpy.context.evaluated_depsgraph_get()
    nieuw = bpy.data.meshes.new_from_object(deel.evaluated_get(dg))
    deel.modifiers.remove(m)
    bpy.data.objects.remove(getal)
    ok, _ = gesloten(nieuw)
    if ok and len(nieuw.vertices) > len(deel.data.vertices):
        oud = deel.data
        deel.data = nieuw
        bpy.data.meshes.remove(oud)
        return True
    bpy.data.meshes.remove(nieuw)
    return False


fouten = []
for d in delen:
    toepassen(d)
paren = {}
for d in delen:
    paren.setdefault(round(float(d["cj_speling_mm"]), 2), []).append(d)
for s, paar in sorted(paren.items()):
    paar.sort(key=lambda o: min(v.co.z for v in o.data.vertices))
    a, b = paar
    tekst = f"{s:.2f}"
    for deel, onder in ((a, True), (b, False)):
        if not graveer(deel, tekst, onder):
            fouten.append(f"{deel.name}: geen getal")

# Opleggen: A blijft staan, B 180 graden om X om zijn eigen midden, alles op z = 0.
breedte = 0.0
for s, (a, b) in sorted(paren.items()):
    pts = [v.co for v in b.data.vertices]
    c = sum(pts, Vector()) / len(pts)
    b.data.transform(Matrix.Translation(c) @ Matrix.Rotation(3.141592653589793, 4, "X") @ Matrix.Translation(-c))
    for d in (a, b):
        zmin = min(v.co.z for v in d.data.vertices)
        d.data.transform(Matrix.Translation((0, 0, -zmin)))
ya = max(v.co.y for a, _ in paren.values() for v in a.data.vertices)
yb = min(v.co.y for _, b in paren.values() for v in b.data.vertices)
for _, b in paren.values():
    b.data.transform(Matrix.Translation((0, ya + RIJ_MM - yb, 0)))
# Linksvoor op de oorsprong.
alle = [v.co for d in delen for v in d.data.vertices]
x0, y0 = min(p.x for p in alle), min(p.y for p in alle)
for d in delen:
    d.data.transform(Matrix.Translation((-x0, -y0, 0)))
    ok, _ = gesloten(d.data)
    if not ok:
        fouten.append(f"{d.name}: niet gesloten")
alle = [v.co for d in delen for v in d.data.vertices]
maat = [max(p[i] for p in alle) - min(p[i] for p in alle) for i in range(3)]
print("MAAT_MM", " x ".join(f"{m:.1f}" for m in maat))


def exporteer(objs, pad):
    for o in bpy.context.view_layer.objects:
        o.select_set(o in objs)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True, global_scale=1.0, use_scene_unit=False,
                          ascii_format=False, apply_modifiers=True)
    print("STL", pad, sum(len(o.data.polygons) for o in objs), "vlakken")


os.makedirs(UIT, exist_ok=True)
exporteer(delen, os.path.join(UIT, "fit-test-strip.stl"))

testset = os.path.join(HIER, "testset-4-delen.stl")
if os.path.exists(testset):
    voor = set(bpy.data.objects)
    bpy.ops.wm.stl_import(filepath=testset)
    nieuw = [o for o in bpy.data.objects if o not in voor]
    for o in nieuw:
        toepassen(o)
        pts = [v.co for v in o.data.vertices]
        dx, dy = -min(p.x for p in pts), -min(p.y for p in pts) + maat[1] + RIJ_MM
        o.data.transform(Matrix.Translation((dx, dy, -min(p.z for p in pts))))
    exporteer(delen + nieuw, os.path.join(UIT, "fit-test-strip-plus-testset.stl"))

print("FOUTEN", fouten if fouten else "geen")
