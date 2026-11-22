"""Opname voor YouTube Shorts reeks 5: een CC0-monster van Quaternius door Figure from rig (22 nov 2026, Chris).
Opdracht Afkijker 22 nov ±09:45: elke Short een ander figuur, nooit de productnaam in de titel.
Draait de opname van reeks 4 (../youtube-shorts-4/opname.py, echte Blender, echte muis, OCR) met één ander figuur:
in plaats van de MakeHuman-pop met eigen rig komt een monster uit Quaternius "Ultimate Monsters" (CC0 1.0,
https://quaternius.com/packs/ultimatemonsters.html) met zijn eigen rig. Rusthouding, wapens weg, CJ_HOOGTE mm hoog
(standaard 225, zo staat het midden waar de camera van reeks 4 kijkt), zo nodig Make watertight.
    CJ_MONSTER_BLEND=<Yeti.blend> blender --gpu-backend opengl start.blend --python opname.py -- <map> <betaalde zip>
Verder alles gelijk aan reeks 4 (zelfde delen en regels "KORT OK <deel>"); de grens voor de knop is 2 gewrichten in
plaats van 6, omdat de proef op deze monsters 2 tot 4 gaf (commercie/filmpjes/monsters/proef-2026-11-22.md)."""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.abspath(os.path.join(HIER, "..", "youtube-shorts-4", "opname.py"))
src = open(BRON, encoding="utf-8").read()

MONSTER = r'''
HOOGTE = float(os.environ.get("CJ_HOOGTE", "225"))
BUIK = (0.0, 0.0, 0.55 * HOOGTE)


def laad_monster(pad):
    with bpy.data.libraries.load(pad, link=False) as (van, naar):
        naar.objects = list(van.objects)
    for o in naar.objects:
        if o is not None:
            bpy.context.scene.collection.objects.link(o)
    arm = next(o for o in bpy.context.scene.objects if o.type == "ARMATURE")
    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    body = max(meshes, key=lambda o: len(o.data.vertices))   # lichaam; wapens en losse stukken weg
    for o in meshes:
        if o is not body:
            bpy.data.objects.remove(o)
    for o in [o for o in bpy.context.scene.objects if o.type not in ("MESH", "ARMATURE")]:
        bpy.data.objects.remove(o)
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
    hoeken = [body.matrix_world @ Vector(h) for h in body.bound_box]
    f = HOOGTE / (max(h.z for h in hoeken) - min(h.z for h in hoeken))
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


def punten_uit_rig(arm):
    b = arm.data.bones
    w = arm.matrix_world
    p = {}
    for kant, z in (("l", "L"), ("r", "R")):
        p[f"{kant}-upper-leg"] = w @ b[f"UpperLeg.{z}"].head_local
        p[f"{kant}-knee"] = w @ b[f"LowerLeg.{z}"].head_local
        p[f"{kant}-ankle"] = w @ b[f"LowerLeg.{z}"].tail_local
        p[f"{kant}-shoulder"] = w @ b[f"UpperArm.{z}"].head_local
        p[f"{kant}-elbow"] = w @ b[f"LowerArm.{z}"].head_local
    return p


def figuur():
    A["leeg"]()
    pad = os.environ["CJ_MONSTER_BLEND"]
    arm, ob = laad_monster(pad)
    st = A["mesh_staat"](ob)
    log(f"KORT monster {os.path.basename(pad)} punten {len(ob.data.vertices)} open {st['open_randen']} stukken {st['losse_stukken']}")
    if st["open_randen"] or st["randen_3plus"] or st["losse_stukken"] > 1:
        A["actief"](ob)
        try:
            bpy.ops.click_joints.maak_gesloten()
        except RuntimeError as fout:
            log(f"KORT watertight fout {str(fout)[:150]}")
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob and nieuw is not None and nieuw.type == "MESH":
            bpy.data.objects.remove(ob)
            ob = nieuw
        if not any(m.type == "ARMATURE" for m in ob.modifiers):
            ob.modifiers.new("Armature", "ARMATURE").object = arm
    arm.data.display_type = "STICK"
    arm.show_in_front = True
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    exportmap = os.path.join(scherm_basis.uitmap, "export")
    os.makedirs(exportmap, exist_ok=True)
    inst.exportmap = exportmap
    film["metingen"]["monster"] = os.path.splitext(os.path.basename(pad))[0]
    return ob, arm, punten_uit_rig(arm)

'''

vervang = [
    ("gang = verloop()", MONSTER + "\ngang = verloop()"),
    ("'OK' if len(lijst) >= 6 else 'FOUT'", "'OK' if len(lijst) >= 2 else 'FOUT'"),
    ("scherm_punt((9.0, -8.0, 128.0))", "scherm_punt(BUIK)"),
]
for oud, nieuw in vervang:
    assert src.count(oud) == 1, f"niet gevonden of dubbel: {oud}"
    src = src.replace(oud, nieuw)
g = {"__name__": "__main__", "__file__": BRON}
exec(compile(src, BRON, "exec"), g)   # noqa: S102 (eigen code uit de repo)
