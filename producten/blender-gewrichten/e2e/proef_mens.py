"""Proef (17 nov run 18): Figure from rig op een echte mensfiguur met een echte rig, voor het eindbeeld van Daan.

Daan wil het eindbeeld van 1.1 op een echte figuur, niet op buizen. De Meshy-figuren hebben de armen langs het lijf en
de dijen tegen elkaar (heupen gaan naar 1.2). Deze proef neemt de basisfiguur van MakeHuman (base.obj, CC0 1.0,
github.com/makehumancommunity/makehuman, makehuman/data/3dobjs/base.obj): een mens in A-houding met losse armen en
benen. In dat bestand staan kleine kubusjes op elk gewricht (groepen joint-l-knee, joint-r-elbow ...); de botten van
de rig komen precies daar, met Mixamo-namen (mixamorig:LeftLeg ...). Linker knie Limit Rotation 120, linker elleboog
140, rechts niets: rechts moet dan `mirrored` worden. 150 mm hoog, kijkt naar -y, links is +x.

Gebruik: blender -b --factory-startup --python e2e/proef_mens.py -- <betaalde zip> <uitmap> <base.obj>
Uitslag in het log, regels met [cj-mens]. Bewaart <uitmap>/mens_rig.blend.
Knoppen: CJ_HOOGTE (mm, standaard 150), CJ_ALLEEN (stukjes van de gewone namen, zoals proef_rigify).
"""
import importlib
import math
import os
import sys

import bpy
from mathutils import Vector

HIER = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HIER, "proef_ai_model.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
A = {"__name__": "proef_ai_model", "__file__": os.path.join(HIER, "proef_ai_model.py")}
exec(compile(_src, "proef_ai_model.py", "exec"), A)
H = A["HOOGTE_MM"]


def log(t):
    print(f"[cj-mens] {t}", flush=True)


def midden(o):
    vs = [o.matrix_world @ v.co for v in o.data.vertices]
    return sum(vs, Vector()) / len(vs)


def laad_mens(pad):
    """Alleen de groep body; gewrichtspunten uit de joint-kubusjes, alles naar 150 mm met de voeten op z=0."""
    bpy.ops.wm.obj_import(filepath=pad, use_split_groups=True, use_split_objects=True)
    body = next(o for o in bpy.data.objects if o.name == "body")
    pj = {o.name[len("joint-"):]: midden(o) for o in bpy.data.objects if o.name.startswith("joint-")}
    for o in list(bpy.data.objects):
        if o is not body:
            bpy.data.objects.remove(o)
    A["actief"](body)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    vs = [v.co for v in body.data.vertices]
    lo = Vector((min(v.x for v in vs), min(v.y for v in vs), min(v.z for v in vs)))
    hi = Vector((max(v.x for v in vs), max(v.y for v in vs), max(v.z for v in vs)))
    f = H / (hi.z - lo.z)

    def zet(c):
        return Vector(((c.x - (lo.x + hi.x) / 2) * f, (c.y - (lo.y + hi.y) / 2) * f, (c.z - lo.z) * f))

    for v in body.data.vertices:
        v.co = zet(v.co)
    body.data.update()
    body.name = body.data.name = "mens"
    return body, {k: zet(c) for k, c in pj.items()}


def maak_rig(p):
    bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))
    rig = bpy.context.active_object
    rig.name = "mixamo_rig"
    eb = rig.data.edit_bones
    for b in list(eb):
        eb.remove(b)

    def bot(naam, kop, staart, ouder=None, z_naar=None):
        b = eb.new("mixamorig:" + naam)
        b.head, b.tail = kop, staart
        if ouder is not None:
            b.parent = eb["mixamorig:" + ouder]
        if z_naar is not None:
            b.align_roll(z_naar)
        return b

    bot("Hips", p["pelvis"], p["spine-4"])
    bot("Spine", p["spine-4"], p["spine-2"], "Hips")
    bot("Spine1", p["spine-2"], p["spine-1"], "Spine")
    bot("Spine2", p["spine-1"], p["neck"], "Spine1")
    bot("Neck", p["neck"], p["head"], "Spine2", Vector((0, -1, 0)))
    bot("Head", p["head"], p["head-2"], "Neck")
    for kn, k in (("Left", "l"), ("Right", "r")):
        bot(kn + "UpLeg", p[k + "-upper-leg"], p[k + "-knee"], "Hips", Vector((0, -1, 0)))
        bot(kn + "Leg", p[k + "-knee"], p[k + "-ankle"], kn + "UpLeg", Vector((0, 1, 0)))  # knie buigt naar achter
        bot(kn + "Foot", p[k + "-ankle"], p[k + "-foot-1"], kn + "Leg")
        bot(kn + "Shoulder", p[k + "-clavicle"], p[k + "-shoulder"], "Spine2")
        bot(kn + "Arm", p[k + "-shoulder"], p[k + "-elbow"], kn + "Shoulder", Vector((0, 1, 0)))
        bot(kn + "ForeArm", p[k + "-elbow"], p[k + "-hand"], kn + "Arm", Vector((0, -1, 0)))  # elleboog naar voren
        bot(kn + "Hand", p[k + "-hand"], p[k + "-hand-2"], kn + "ForeArm")
    bpy.ops.object.mode_set(mode="POSE")
    for naam, graden in (("LeftLeg", int(os.environ.get("CJ_KNIE", "120"))), ("LeftForeArm", 140)):
        c = rig.pose.bones["mixamorig:" + naam].constraints.new("LIMIT_ROTATION")
        c.use_limit_x, c.min_x, c.max_x, c.owner_space = True, 0.0, math.radians(graden), "LOCAL"
    bpy.ops.object.mode_set(mode="OBJECT")
    log(f"RIG: {len(rig.data.bones)} botten, knie L {tuple(round(x, 1) for x in p['l-knee'])}, "
        f"elleboog L {tuple(round(x, 1) for x in p['l-elbow'])}")
    return rig


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, uit, pad = args[0], args[1], args[2]
    os.makedirs(uit, exist_ok=True)
    A["installeer"](zip_pad)
    inst = bpy.context.scene.click_joints
    A["leeg"]()
    ob, punten = laad_mens(pad)
    st = A["mesh_staat"](ob)
    log(f"MESH: {len(ob.data.vertices)} punten, open randen {st['open_randen']}, stukken {st['losse_stukken']}")
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        try:
            bpy.ops.click_joints.maak_gesloten()
        except RuntimeError as fout:
            log(f"MAKE WATERTIGHT fout {str(fout)[:150]}")
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
        st = A["mesh_staat"](ob)
        log(f"NA WATERTIGHT: open randen {st['open_randen']}, stukken {st['losse_stukken']}, naam {ob.name}")
    naam = ob.name
    rig = maak_rig(punten)
    ob.modifiers.new("Armature", "ARMATURE").object = rig
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    if os.environ.get("CJ_ALLEEN"):
        _rigm = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
        _g = getattr(_rigm, "_cj_echt", _rigm.gewrichten)
        _rigm._cj_echt, _w = _g, os.environ["CJ_ALLEEN"].split(",")
        _rigm.gewrichten = lambda a, meer=False: [x for x in _g(a, meer) if any(w in x[2].lower() for w in _w)]
    try:
        r = bpy.ops.click_joints.figuur_uit_rig()
    except RuntimeError as e:
        r = f"fout {str(e).strip()[:300]}"
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
    alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
    log(f"FIGUUR: uitslag={r} gewrichten={len(alle)}")
    for x in alle:
        log(f"  {fig.regel(x)}")
    over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), None)
    log(f"OVERGESLAGEN: {over}")
    log(f"DELEN: {len(delen)}, open {[o.name for o in delen if not ges.is_gesloten(o)[0]]}, "
        f"stukken {[A['mesh_staat'](o)['losse_stukken'] for o in delen]}")
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uit, "mens_rig.blend"))
    log("KLAAR")


main()
