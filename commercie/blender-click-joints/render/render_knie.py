"""Eerlijke render van een knie uit Click Joints Pro (klus hoofdchat 16 nov 16:40).

Stappen, allemaal in echte Blender:
1. Open de .blend die e2e/maak_chris_figuur.py maakte (Meshy-figuur, Pro 1.0.2, scharnier met eindstop 115 in de knie).
2. Exporteer de delen met de add-on zelf naar STL (zoals een gebruiker doet).
3. Gooi de scene leeg, importeer alleen die STL-bestanden en render die, met een printplastic-materiaal.
4. Het onderbeen draait om het scharnierpunt van 0 graden tot het gemeten bereik van de add-on (cj_bereik_graden),
   blijft even staan en gaat terug. Er wordt niets nagemaakt: geen hand, geen print, geen extra hoek.

Gebruik: blender -b --factory-startup --python render_knie.py -- <betaalde zip> <figuur.blend> <uitmap> <stand>
stand: "snel" (drie stilstaande beelden, lage kwaliteit, om de buigrichting na te kijken) of "film" (240 beelden).
"""
import math
import os
import sys

import bpy
from mathutils import Matrix, Quaternion, Vector


def log(t):
    print(f"[cj-render] {t}", flush=True)


args = sys.argv[sys.argv.index("--") + 1:]
zip_pad, blend, uit, stand = args[0], args[1], args[2], args[3]
os.makedirs(uit, exist_ok=True)

# 1. add-on en figuur
if "plaats_scharnier" not in dir(bpy.ops.click_joints):
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
bpy.ops.wm.open_mainfile(filepath=blend)
log(f"add-on geladen: {'exporteer' in dir(bpy.ops.click_joints)}")
delen = [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_deel")]
a = next(o for o in delen if "cj_bereik_graden" in o and "_A" in o.name)
b = next(o for o in delen if o is not a and "cj_scharnier_punt" in o)
bereik = float(a["cj_bereik_graden"])
c = Vector(b["cj_scharnier_punt"])
lidas = Vector(b["cj_as"]).normalized()
buig = Vector(b["cj_buigkant"]).normalized()
draai_as = lidas.cross(buig).normalized()  # zelfde as als pose_q in scharnier_beweeg.py
log(f"A {a.name}, B {b.name}, bereik {bereik:.2f}, punt {tuple(round(x, 2) for x in c)}, "
    f"lidas {tuple(round(x, 2) for x in lidas)}, buigkant {tuple(round(x, 2) for x in buig)}")

# 2. export met de add-on
for o in delen:
    o["cj_pose_graden"] = 0.0
inst = bpy.context.scene.click_joints
inst.uit_elkaar = False
inst.formaat = "STL"
inst.exportmap = os.path.join(uit, "stl") + os.sep
for o in bpy.context.view_layer.objects:
    o.select_set(o in delen)
bpy.context.view_layer.objects.active = a
r = bpy.ops.click_joints.exporteer()
pad_a, pad_b = a.get("cj_stl", ""), b.get("cj_stl", "")
log(f"export {r}: {pad_a} ({os.path.getsize(pad_a)} B), {pad_b} ({os.path.getsize(pad_b)} B)")
ref = {k: (o.matrix_world @ Vector(o.bound_box[0]), o.matrix_world @ Vector(o.bound_box[6])) for k, o in (("A", a), ("B", b))}

# 3. lege scene, alleen de STL-bestanden
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
us = sc.unit_settings
us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"


def importeer(pad):
    voor = set(sc.objects)
    bpy.ops.wm.stl_import(filepath=pad, global_scale=1.0, use_scene_unit=False)
    ob = next(o for o in sc.objects if o not in voor)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    bpy.ops.object.shade_auto_smooth(angle=math.radians(35))
    ob.select_set(False)
    return ob


A, B = importeer(pad_a), importeer(pad_b)
for k, o in (("A", A), ("B", B)):
    lo, hi = o.matrix_world @ Vector(o.bound_box[0]), o.matrix_world @ Vector(o.bound_box[6])
    log(f"{k} terug uit STL: van {tuple(round(x, 2) for x in lo)} tot {tuple(round(x, 2) for x in hi)}, "
        f"verschil met de add-on {max((lo - ref[k][0]).length, (hi - ref[k][1]).length):.3f} mm")

# printplastic: PLA-achtig, licht laagjespatroon van 0,2 mm langs de eigen Z van elk deel (zo is het geprint)
mat = bpy.data.materials.new("PLA")
mat.use_nodes = True
nt = mat.node_tree
bsdf = nt.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.62, 0.60, 0.57, 1)
bsdf.inputs["Roughness"].default_value = 0.42
tc = nt.nodes.new("ShaderNodeTexCoord")
golf = nt.nodes.new("ShaderNodeTexWave")
golf.wave_type, golf.bands_direction = "BANDS", "Z"
golf.inputs["Scale"].default_value = 2 * math.pi / (20 * 0.2)
bump = nt.nodes.new("ShaderNodeBump")
bump.inputs["Strength"].default_value = 0.12
bump.inputs["Distance"].default_value = 0.04
nt.links.new(tc.outputs["Object"], golf.inputs["Vector"])
nt.links.new(golf.outputs["Fac"], bump.inputs["Height"])
nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
for o in (A, B):
    o.data.materials.clear()
    o.data.materials.append(mat)

# onderbeen aan een leeg punt op het scharnier; kies het teken waarbij de voet naar de buigkant gaat
spil = bpy.data.objects.new("spil", None)
sc.collection.objects.link(spil)
spil.location = c
spil.rotation_mode = "QUATERNION"
bpy.context.view_layer.update()
A.parent = spil
A.matrix_parent_inverse = spil.matrix_world.inverted()


def voet_bij(graden):
    spil.rotation_quaternion = Quaternion(draai_as, math.radians(graden))
    bpy.context.view_layer.update()
    ps = [A.matrix_world @ v.co for v in A.data.vertices]
    laag = sorted(ps, key=lambda p: p.dot(lidas))[: max(50, len(ps) // 20)]
    return sum(laag, Vector()) / len(laag)


v0 = voet_bij(0.0)
teken = 1.0 if (voet_bij(30.0) - v0).dot(buig) > (voet_bij(-30.0) - v0).dot(buig) else -1.0
log(f"teken {teken:+.0f}: voet gaat bij +30 graden {(voet_bij(30.0 * teken) - v0).dot(buig):.2f} mm naar de buigkant")
voet_bij(0.0)

# licht, vloer, camera
sc.render.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.use_denoising = True
sc.render.use_persistent_data = True
sc.render.resolution_x, sc.render.resolution_y = 1080, 1350
sc.view_settings.view_transform = "AgX"
wereld = bpy.data.worlds.new("w")
sc.world = wereld
wereld.use_nodes = True
wereld.node_tree.nodes["Background"].inputs["Color"].default_value = (0.012, 0.013, 0.016, 1)
wereld.node_tree.nodes["Background"].inputs["Strength"].default_value = 1.0

lo = min((o.matrix_world @ Vector(p)).z for o in (B,) for p in o.bound_box)
hi = max((o.matrix_world @ Vector(p)).z for o in (B,) for p in o.bound_box)
hoogte = hi - lo
midden = Vector((0, 0, lo + hoogte * 0.5))
bpy.ops.mesh.primitive_plane_add(size=hoogte * 20, location=(0, 0, lo))
vloer = bpy.context.active_object
vm = bpy.data.materials.new("vloer")
vm.use_nodes = True
vm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.035, 0.037, 0.045, 1)
vm.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.6
vloer.data.materials.append(vm)

zij = draai_as  # de scharnieras ligt links-rechts: van opzij zie je de knie buigen
voor = -buig


def lamp(naam, richting, kracht, grootte, kleur=(1, 1, 1)):
    ld = bpy.data.lights.new(naam, "AREA")
    ld.energy, ld.size, ld.color = kracht, grootte, kleur
    ob = bpy.data.objects.new(naam, ld)
    sc.collection.objects.link(ob)
    ob.location = midden + richting.normalized() * hoogte * 2.2
    ob.rotation_euler = (midden - ob.location).to_track_quat("-Z", "Y").to_euler()


s = hoogte / 150.0
lamp("hoofd", zij * 1.0 + voor * 0.7 + Vector((0, 0, 1.1)), 1.0e8 * s * s, hoogte * 0.9)
lamp("vul", -zij * 0.4 + voor * 1.0 + Vector((0, 0, 0.3)), 3.0e7 * s * s, hoogte * 1.2, (0.85, 0.9, 1.0))
lamp("rand", -voor * 1.0 + zij * 0.3 + Vector((0, 0, 0.8)), 6.0e7 * s * s, hoogte * 0.6, (0.75, 0.65, 1.0))

cd = bpy.data.cameras.new("cam")
cd.lens = 70
cam = bpy.data.objects.new("cam", cd)
sc.collection.objects.link(cam)
sc.camera = cam


def zet_camera(hoek):
    r = Quaternion(Vector((0, 0, 1)), math.radians(hoek))
    richting = r @ (zij * 1.0 + voor * 0.35 + Vector((0, 0, 0.18)))
    cam.location = midden + richting.normalized() * hoogte * 3.3
    cam.rotation_euler = (midden - cam.location).to_track_quat("-Z", "Y").to_euler()


def hoek_op(f):
    """Beeld 1 tot 240 (24 per s, 10 s): 1 s recht, 4 s buigen tot het bereik, 2 s stil, 2,5 s terug, rest stil."""
    def zacht(t):
        return t * t * (3 - 2 * t)
    if f <= 24:
        return 0.0
    if f <= 120:
        return bereik * zacht((f - 24) / 96)
    if f <= 168:
        return bereik
    if f <= 228:
        return bereik * (1 - zacht((f - 168) / 60))
    return 0.0


if stand == "snel":
    sc.cycles.samples = 24
    for g in (0.0, bereik * 0.5, bereik):
        voet_bij(g * teken)
        zet_camera(0.0)
        sc.render.filepath = os.path.join(uit, f"stil-{int(round(g)):03d}.png")
        bpy.ops.render.render(write_still=True)
        im = bpy.data.images.load(sc.render.filepath)
        px = list(im.pixels)
        log(f"stil {g:.1f} graden geschreven, gemiddelde helderheid {sum(px[0::4]) / (len(px) // 4):.3f}")
else:
    sc.cycles.samples = 40
    sc.render.fps = 24
    os.makedirs(os.path.join(uit, "beelden"), exist_ok=True)
    for f in range(1, 241):
        voet_bij(hoek_op(f) * teken)
        zet_camera(-6.0 + 12.0 * (f - 1) / 239)
        sc.frame_set(f)
        sc.render.filepath = os.path.join(uit, "beelden", f"{f:04d}.png")
        bpy.ops.render.render(write_still=True)
        if f % 20 == 0:
            log(f"beeld {f}/240, hoek {hoek_op(f):.1f}")
log(f"KLAAR bereik {bereik:.2f}")
