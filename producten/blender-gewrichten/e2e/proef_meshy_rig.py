"""Proef (geen toets, 16 nov run 14): Figure from rig op echte Meshy-figuren met Mixamo-botnamen.

Plan punt 2 van Pro 1.1: werkt de knop op figuren uit een AI-generator, met een rig met Mixamo-namen? Een echt
Mixamo-bestand kunnen wij niet halen (Adobe-account). Daarom: de Meshy-figuur (Hugging Face, MIT) inladen zoals
proef_ai_model.py (150 mm, Make watertight), en er een armature in zetten met de namen die Mixamo gebruikt
(mixamorig:Hips, LeftUpLeg, LeftLeg, LeftArm, LeftForeArm, Neck ...). De botten komen op plekken die dit script uit
doorsneden van de mesh meet (been- en armlussen), zoals een koper ze ongeveer zou neerzetten. Linker knie en elleboog
krijgen Limit Rotation (120 en 140), rechts niets: rechts moet dan `mirrored` worden.
Links is +x (de figuur kijkt naar -y, zoals in Blenders vooraanzicht en de Rigify-metarig).

Gebruik: blender -b --factory-startup --python e2e/proef_meshy_rig.py -- <betaalde zip> <uitmap> <model.glb> [...]
Uitslag in het log, regels met [cj-mrig]. Per model <uitmap>/<naam>_rig.blend.
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
    print(f"[cj-mrig] {t}", flush=True)


def been(ob, kant, pcts):
    for p in pcts:
        c, _b = A["doorsnede"](ob, p / 100.0 * H, kant)
        if c is not None:
            return c
    return None


def arm(ob, kant, pcts):
    """Midden van een hangende arm aan kant +1 (x>0) of -1: de lus het verst naar buiten, niet het lijf."""
    for p in pcts:
        z = p / 100.0 * H
        alle = A["lussen"](ob, z)
        if len(alle) < 2:
            continue
        lijf = max(alle, key=lambda l: l[1] * l[2])
        kand = [l for l in alle if l is not lijf and (l[0].x - lijf[0].x) * kant > 5.0 and 4.0 <= l[1] <= 25.0
                and 4.0 <= l[2] <= 25.0]
        if kand:
            return max(kand, key=lambda l: l[0].x * kant)[0]
    return None


def nek_punt(ob):
    beste = None
    for p in range(80, 93, 2):
        for c, bx, by in A["lussen"](ob, p / 100.0 * H):
            if abs(c.x) < 15.0 and bx >= 6.0 and (beste is None or bx < beste[1]):
                beste = (c, bx)
    return beste[0] if beste else Vector((0, 0, 0.86 * H))


def maak_rig(ob):
    """Armature met Mixamo-namen, of None als de benen niet te vinden zijn. Meldt welke botten er kwamen."""
    p = {}
    for k, kn in ((1, "Left"), (-1, "Right")):
        p[kn + "UpLeg"] = been(ob, k, (45, 43, 41, 39, 37))
        p[kn + "Leg"] = been(ob, k, (27, 25, 29, 24, 31))
        p[kn + "Foot"] = been(ob, k, (7, 9, 11, 5))
        if p[kn + "UpLeg"] is None and p[kn + "Leg"] is not None:
            # benen boven de knie niet los (tuniek, kort jasje): heupkop recht boven de knie, zoals een koper hem zet
            p[kn + "UpLeg"] = Vector((p[kn + "Leg"].x, p[kn + "Leg"].y, 0.47 * H))
        if p[kn + "UpLeg"] is not None and os.environ.get("CJ_HEUP_PCT"):
            # Mixamo en Rigify zetten de kop van de dij in het bekken (heupgewricht ±52% van de lengte), niet waar het
            # been loskomt; de add-on schuift de kogel zelf uit de romp (schuif_uit_romp)
            p[kn + "UpLeg"].z = float(os.environ["CJ_HEUP_PCT"]) / 100.0 * H
        p[kn + "Arm"] = None
        e = arm(ob, k, (60, 58, 62, 56, 64))
        w = arm(ob, k, (47, 45, 50, 43))
        if e is not None and w is not None:
            p[kn + "ForeArm"], p[kn + "Hand"] = e, w
            p[kn + "Arm"] = Vector((e.x, e.y, 0.81 * H))
    if any(p.get(n) is None for n in ("LeftUpLeg", "LeftLeg", "LeftFoot", "RightUpLeg", "RightLeg", "RightFoot")):
        log(f"{ob.name} RIG: benen niet gevonden {[(n, v is not None) for n, v in p.items()]}")
        return None
    nek = nek_punt(ob)
    my = (p["LeftUpLeg"].y + p["RightUpLeg"].y) / 2
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
            b.align_roll(z_naar)  # Z van het bot naar de buigkant: draaien om +X buigt daarheen
        return b

    heup = Vector((0, my, 0.50 * H))
    bot("Hips", heup, Vector((0, my, 0.58 * H)))
    bot("Spine", Vector((0, my, 0.58 * H)), Vector((0, my, 0.68 * H)), "Hips")
    bot("Spine1", Vector((0, my, 0.68 * H)), Vector((0, my, 0.76 * H)), "Spine")
    bot("Spine2", Vector((0, my, 0.76 * H)), Vector((nek.x, nek.y, nek.z - 4)), "Spine1")
    bot("Neck", Vector((nek.x, nek.y, nek.z - 4)), Vector((nek.x, nek.y, nek.z + 6)), "Spine2", Vector((0, -1, 0)))
    bot("Head", Vector((nek.x, nek.y, nek.z + 6)), Vector((nek.x, nek.y, H)), "Neck")
    for kn in ("Left", "Right"):
        bot(kn + "UpLeg", p[kn + "UpLeg"], p[kn + "Leg"], "Hips", Vector((0, -1, 0)))
        bot(kn + "Leg", p[kn + "Leg"], p[kn + "Foot"], kn + "UpLeg", Vector((0, 1, 0)))  # knie buigt naar achter
        bot(kn + "Foot", p[kn + "Foot"], p[kn + "Foot"] + Vector((0, -12, -p[kn + "Foot"].z + 1)), kn + "Leg")
        if p[kn + "Arm"] is not None:
            sx = math.copysign(max(abs(p[kn + "Arm"].x) - 8, 2), p[kn + "Arm"].x)
            bot(kn + "Shoulder", Vector((sx * 0.3, my, 0.81 * H)), Vector((sx, my, 0.81 * H)), "Spine2")
            bot(kn + "Arm", p[kn + "Arm"], p[kn + "ForeArm"], kn + "Shoulder", Vector((0, 1, 0)))
            bot(kn + "ForeArm", p[kn + "ForeArm"], p[kn + "Hand"], kn + "Arm", Vector((0, -1, 0)))  # elleboog naar voren
            bot(kn + "Hand", p[kn + "Hand"], p[kn + "Hand"] + Vector((0, 0, -8)), kn + "ForeArm")
    bpy.ops.object.mode_set(mode="POSE")
    for naam, graden in (("LeftLeg", int(os.environ.get("CJ_KNIE", "120"))), ("LeftForeArm", 140)):
        pb = rig.pose.bones.get("mixamorig:" + naam)
        if pb is None:
            continue
        c = pb.constraints.new("LIMIT_ROTATION")
        c.use_limit_x, c.min_x, c.max_x, c.owner_space = True, 0.0, math.radians(graden), "LOCAL"
    bpy.ops.object.mode_set(mode="OBJECT")
    log(f"{ob.name} RIG: {len(rig.data.bones)} botten, armen {'ja' if p['LeftArm'] is not None else 'nee'} links, "
        f"{'ja' if p['RightArm'] is not None else 'nee'} rechts; knie L {tuple(round(x, 1) for x in p['LeftLeg'])}")
    return rig


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, uit = args[0], args[1]
    os.makedirs(uit, exist_ok=True)
    A["installeer"](zip_pad)
    inst = bpy.context.scene.click_joints
    for pad in args[2:]:
        A["leeg"]()
        ob = A["laad"](pad)
        st = A["mesh_staat"](ob)
        if st["open_randen"] or st["randen_3plus"]:
            A["actief"](ob)
            try:
                bpy.ops.click_joints.maak_gesloten()
            except RuntimeError as fout:
                log(f"{ob.name} MAKE WATERTIGHT fout {str(fout)[:150]}")
            nieuw = bpy.context.view_layer.objects.active
            if nieuw is not ob:
                bpy.data.objects.remove(ob)
                ob = nieuw
        naam = ob.name
        rig = maak_rig(ob)
        if rig is None:
            continue
        ob.modifiers.new("Armature", "ARMATURE").object = rig
        inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
        A["actief"](ob)
        if os.environ.get("CJ_ALLEEN"):  # zoals proef_rigify: alleen gewrichten met deze stukjes naam
            _rigm = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
            _g, _w = _rigm.gewrichten, os.environ["CJ_ALLEEN"].split(",")
            _rigm.gewrichten = lambda a, meer=False: [x for x in _g(a, meer) if any(w in x[2].lower() for w in _w)]
        try:
            r = bpy.ops.click_joints.figuur_uit_rig()
        except RuntimeError as e:
            r = f"fout {str(e).strip()[:200]}"
        fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
        ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
        alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
        delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get()
                 and o.type == "MESH"]
        log(f"{naam} FIGUUR: uitslag={r} gewrichten={len(alle)}")
        for x in alle:
            log(f"{naam}   {fig.regel(x)}")
        over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), None)
        log(f"{naam} OVERGESLAGEN: {over}")
        log(f"{naam} DELEN: {len(delen)}, open {[o.name for o in delen if not ges.is_gesloten(o)[0]]}, "
            f"stukken {[A['mesh_staat'](o)['losse_stukken'] for o in delen]}")
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uit, naam + "_rig.blend"))
    log("KLAAR")


main()
