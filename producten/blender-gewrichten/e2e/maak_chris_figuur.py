"""Eén Meshy-figuur met knie en elleboog uit Pro 1.0.2, voor de render van Chris (hoofdchat 16 nov 16:40).

Leent laad, lussen en installeer uit proef_ai_model.py (zonder zijn main). Anders dan die proef bepaalt dit script
eerst hoe de figuur staat: links-rechts is de richting waarin de schouders het breedst zijn, voor is de kant waar
de tenen voorbij de enkel steken. Dan: Pro-scharnier met eindstop 115 in één knie (buigt naar achter) en in de
elleboog aan dezelfde kant (buigt naar voor), scharnieras links-rechts. Bewaart <uit>/<naam>-knie-elleboog.blend.
Gebruik: blender -b --factory-startup --python e2e/maak_chris_figuur.py -- <betaalde zip> <uitmap> <model.glb>
"""
import os
import sys

import bpy
from mathutils import Matrix, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HIER, "proef_ai_model.py"), encoding="utf-8").read()
src = src[:src.rstrip().rfind("main()")]
g = {"__name__": "proef_ai_model", "__file__": os.path.join(HIER, "proef_ai_model.py")}
exec(compile(src, "proef_ai_model.py", "exec"), g)
H = g["HOOGTE_MM"]


def log(t):
    print(f"[cj-chris] {t}", flush=True)


def zichtbaar():
    return [o for o in bpy.context.scene.objects if o.type == "MESH" and o.visible_get()]


def punten(ob):
    return [ob.matrix_world @ v.co for v in ob.data.vertices]


def stand_van(ob):
    """(zij, voor): eenheidsvectoren in het grondvlak."""
    ps = punten(ob)
    sch = [p for p in ps if 0.66 * H < p.z < 0.72 * H]
    bx = max(p.x for p in sch) - min(p.x for p in sch)
    by = max(p.y for p in sch) - min(p.y for p in sch)
    zij = Vector((0, 1, 0)) if by > bx else Vector((1, 0, 0))
    vr = Vector((1, 0, 0)) if by > bx else Vector((0, 1, 0))
    voet = [p for p in ps if p.z < 0.02 * H]
    enkel = [p for p in ps if 0.05 * H < p.z < 0.08 * H]
    d = (sum(voet, Vector()) / len(voet) - sum(enkel, Vector()) / len(enkel)).dot(vr)
    return zij, (vr if d > 0 else -vr)


def zet_cursor(c, as_, buig):
    h = buig.cross(as_)  # zelfde handigheid als in proef_ai_model: H = buigkant x lidas
    m = Matrix.Identity(4)
    for i, v in enumerate((h, buig, as_)):
        m.col[i][:3] = v
    m.col[3][:3] = c
    cur = bpy.context.scene.cursor
    cur.rotation_mode = "QUATERNION"
    cur.matrix = m


def lid_lus(zij, z, kant, max_breed=30.0):
    """Lus van een been of arm op hoogte z aan de kant `kant` (+1/-1 langs zij), het verst naar buiten."""
    beste = None
    for o in zichtbaar():
        for c, bx, by in g["lussen"](o, z):
            s = c.dot(zij) * kant
            if s > 3.0 and max(bx, by) < max_breed * H / 150.0 and (beste is None or s > beste[1]):
                beste = (o, s, c)
    return beste


def scharnier(doel, c, as_, buig, wat):
    zet_cursor(c, as_, buig)
    inst = bpy.context.scene.click_joints
    inst.as_bron, inst.uit_elkaar = "CURSOR", False
    g["actief"](doel)
    voor = set(o.name for o in bpy.context.scene.objects)
    try:
        r = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as e:
        r = f"fout {str(e)[:150]}"
    nieuw = [o for o in bpy.context.scene.objects if o.name not in voor and o.get("cj_deel")]
    log(f"{wat} op ({c.x:.1f}, {c.y:.1f}, {c.z:.1f}): {r}, delen {[(o.name, o.get('cj_bereik_graden')) for o in nieuw]}, "
        f"melding {next((o.get('cj_melding') for o in nieuw if o.get('cj_melding')), None)}")
    return bool(nieuw)


args = sys.argv[sys.argv.index("--") + 1:]
zip_pad, uit, pad = args[0], args[1], args[2]
os.makedirs(uit, exist_ok=True)
g["installeer"](zip_pad)
g["leeg"]()
ob = g["laad"](pad)
st = g["mesh_staat"](ob)
if st["open_randen"] or st["randen_3plus"]:
    g["actief"](ob)
    bpy.ops.click_joints.maak_gesloten()
    ob = bpy.context.view_layer.objects.active
naam = ob.name
zij, voor = stand_van(ob)
log(f"zij {tuple(zij)}, voor {tuple(round(x, 2) for x in voor)}")
omhoog = Vector((0, 0, 1))
kant = 1
gelukt = []
for pct in (27, 25, 29, 24, 31):
    l = lid_lus(zij, pct / 100 * H, kant)
    if l and scharnier(l[0], l[2], omhoog, -voor, "KNIE"):
        gelukt.append("knie")
        break
for pct in (59, 57, 61, 55, 63, 53):
    l = lid_lus(zij, pct / 100 * H, kant, 22.0)
    if l and scharnier(l[0], l[2], omhoog, voor, "ELLEBOOG"):
        gelukt.append("elleboog")
        break
for o in zichtbaar():
    log(f"deel {o.name} stand={o.get('cj_stand')} bereik={o.get('cj_bereik_graden')} passing={o.get('cj_passing')}")
log(f"gelukt: {gelukt}")
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uit, f"{naam}-knie-elleboog.blend"), compress=True)
log("KLAAR")
