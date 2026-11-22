"""Proef (22 nov 2026, Chris, opdracht Afkijker 09:45): Figure from rig op een CC0-monster van Quaternius.

Bron: Quaternius "Ultimate Monsters" (CC0 1.0, https://quaternius.com/packs/ultimatemonsters.html), map Big/Blends.
Elk monster heeft een eigen rig (botten UpperArm.L, LowerArm.L, UpperLeg.L, LowerLeg.L, Neck): die herkent de add-on.
Stappen: pose en animatie wissen (rusthouding), wapens en losse stukken weg, schaal naar CJ_HOOGTE mm (standaard 150)
met voeten op z=0, zo nodig Make watertight, dan de knop Figure from rig. Alleen meten, geen beeld.

Gebruik: blender -b --factory-startup --python proef_monster.py -- <betaalde zip> <monster.blend> [uitmap]
Uitslag: regels [cj-monster], laatste regel "MONSTER <naam> gewrichten=<n> delen=<n>".
"""
import importlib
import os
import sys

import bpy
from mathutils import Vector

E2E = os.environ.get("CJ_E2E", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../producten/blender-gewrichten/e2e"))
_p = os.path.join(E2E, "proef_ai_model.py")
A = {"__name__": "proef_ai_model", "__file__": _p}
exec(compile(open(_p, encoding="utf-8").read().replace("\nmain()\n", "\n"), _p, "exec"), A)
H = A["HOOGTE_MM"]


def log(t):
    print(f"[cj-monster] {t}", flush=True)


def laad_monster(pad):
    with bpy.data.libraries.load(pad, link=False) as (van, naar):
        naar.objects = list(van.objects)
    for o in naar.objects:
        if o is not None:
            bpy.context.scene.collection.objects.link(o)
    arm = next(o for o in bpy.context.scene.objects if o.type == "ARMATURE")
    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    # Het lichaam is de mesh met de meeste punten; wapens en losse stukken gaan weg.
    body = max(meshes, key=lambda o: len(o.data.vertices))
    for o in meshes:
        if o is not body:
            bpy.data.objects.remove(o)
    # Rusthouding: animatie en pose weg.
    if arm.animation_data:
        arm.animation_data_clear()
    for pb in arm.pose.bones:
        pb.location = (0, 0, 0)
        pb.rotation_quaternion = (1, 0, 0, 0)
        pb.rotation_euler = (0, 0, 0)
        pb.scale = (1, 1, 1)
    for m in list(body.modifiers):
        if m.type != "ARMATURE":
            body.modifiers.remove(m)
    bpy.context.view_layer.update()
    # Schaal: hele boom (rig + lichaam) zodat het lichaam H mm hoog is, voeten op 0.
    hoeken = [body.matrix_world @ Vector(h) for h in body.bound_box]
    lo = Vector((min(h.x for h in hoeken), min(h.y for h in hoeken), min(h.z for h in hoeken)))
    hi = Vector((max(h.x for h in hoeken), max(h.y for h in hoeken), max(h.z for h in hoeken)))
    f = H / (hi.z - lo.z)
    arm.scale = arm.scale * f
    bpy.context.view_layer.update()
    hoeken = [body.matrix_world @ Vector(h) for h in body.bound_box]
    lo = Vector((min(h.x for h in hoeken), min(h.y for h in hoeken), min(h.z for h in hoeken)))
    hi = Vector((max(h.x for h in hoeken), max(h.y for h in hoeken), max(h.z for h in hoeken)))
    arm.location -= Vector(((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, lo.z))
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    arm.select_set(True)
    body.select_set(True)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    return arm, body


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, pad = args[0], args[1]
    uit = args[2] if len(args) > 2 else None
    naam_m = os.path.splitext(os.path.basename(pad))[0]
    A["installeer"](zip_pad)
    inst = bpy.context.scene.click_joints
    A["leeg"]()
    arm, ob = laad_monster(pad)
    st = A["mesh_staat"](ob)
    log(f"MESH {naam_m}: {len(ob.data.vertices)} punten, open randen {st['open_randen']}, stukken {st['losse_stukken']}, "
        f"maat {tuple(round(d, 1) for d in ob.dimensions)}")
    if st["open_randen"] or st["randen_3plus"] or st["losse_stukken"] > 1:
        A["actief"](ob)
        try:
            bpy.ops.click_joints.maak_gesloten()
        except RuntimeError as fout:
            log(f"MAKE WATERTIGHT fout {str(fout)[:150]}")
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
        if not any(m.type == "ARMATURE" for m in ob.modifiers):
            ob.modifiers.new("Armature", "ARMATURE").object = arm
        st = A["mesh_staat"](ob)
        log(f"NA WATERTIGHT: open randen {st['open_randen']}, stukken {st['losse_stukken']}, naam {ob.name}")
    naam = ob.name
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    try:
        r = bpy.ops.click_joints.figuur_uit_rig()
    except RuntimeError as e:
        r = f"fout {str(e).strip()[:300]}"
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
    log(f"FIGUUR: uitslag={r} gewrichten={len(alle)}")
    for x in alle:
        log(f"  {fig.regel(x)}")
    over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), None)
    log(f"OVERGESLAGEN: {over}")
    log(f"DELEN: {len(delen)}, stukken {[A['mesh_staat'](o)['losse_stukken'] for o in delen]}")
    if uit:
        os.makedirs(uit, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uit, f"{naam_m}_figuur.blend"))
    log(f"MONSTER {naam_m} gewrichten={len(alle)} delen={len(delen)}")


main()
