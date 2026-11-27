"""Bouwt het figuur voor het hoofdbeeld 'held' (#285): Blender Human Base Meshes v1.4.1, GEO-body_male_realistic
(CC0 1.0, Blender Studio, download.blender.org/demo/asset-bundles/human-base-meshes/), multires op niveau 2 vastgezet,
met een eigen rig (Rigify-namen) op plekken die uit de mesh zelf gemeten worden. Geen gewichten nodig: Figure from rig
leest alleen de botten.
    blender -b --factory-startup --python maak_held.py -- <human_base_meshes_bundle.blend> <uit.blend> [niveau]
"""
import os, sys, bpy
from mathutils import Vector
a = sys.argv[sys.argv.index("--") + 1:]
BRON, UIT = a[0], a[1]
NIVEAU = int(a[2]) if len(a) > 2 else 2
bpy.ops.wm.open_mainfile(filepath=BRON)
ob = bpy.data.objects["GEO-body_male_realistic"]
for o in list(bpy.data.objects):
    if o is not ob:
        bpy.data.objects.remove(o)
for c in list(bpy.data.collections):
    bpy.data.collections.remove(c)
if ob.name not in bpy.context.scene.collection.objects:
    bpy.context.scene.collection.objects.link(ob)
ob.hide_set(False); ob.hide_viewport = False
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
for m in list(ob.modifiers):
    if m.type == "MULTIRES":
        m.levels = NIVEAU
        bpy.ops.object.modifier_apply(modifier=m.name)
    else:
        ob.modifiers.remove(m)
ob.parent = None
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
# midden op x=0 en voeten op z=0 (laad() kijkt naar het teken van x om links en rechts te bepalen)
_v = [v.co for v in ob.data.vertices]
_m = Vector(((min(c.x for c in _v) + max(c.x for c in _v)) / 2, 0, min(c.z for c in _v)))
for v in ob.data.vertices:
    v.co -= _m
V = [v.co.copy() for v in ob.data.vertices]
lo = Vector([min(v[i] for v in V) for i in range(3)]); hi = Vector([max(v[i] for v in V) for i in range(3)])
H = hi.z - lo.z
cx = (lo.x + hi.x) / 2
cy = (lo.y + hi.y) / 2
print("MAAT", len(V), lo, hi, H)

def snee(z, d=0.006, kant=None, xmin=None, xmax=None):
    p = [v for v in V if abs(v.z - z) < d and (kant is None or (v.x - cx) * kant > 0)
         and (xmin is None or abs(v.x - cx) >= xmin) and (xmax is None or abs(v.x - cx) <= xmax)]
    if not p:
        return None
    return sum(p, Vector()) / len(p), p

def z(f):
    return lo.z + f * H

def romp_y(zz):
    return snee(zz, d=0.01, xmax=0.10)[0].y

def R(f):
    return Vector((cx, romp_y(z(f)), z(f)))
# armen: punten ver buiten de romp, hoofdas per kant
bones = {}
for kant, s in ((1, "L"), (-1, "R")):
    # links = +x (de add-on rekent met voorkant -y); welke kant +x is bepaalt laad() zelf
    arm = [v for v in V if (v.x - cx) * kant > 0.20 * H * 0.6 and z(0.30) < v.z < z(0.83)]
    # hand: laagste 10% van de armpunten
    arm.sort(key=lambda v: v.z)
    hand_top = arm[int(len(arm) * 0.12)].z
    wrist = sum((v for v in arm if abs(v.z - hand_top) < 0.01), Vector()) / max(1, len([v for v in arm if abs(v.z - hand_top) < 0.01]))
    vinger = sum(arm[:20], Vector()) / 20
    # schouder: midden van de dwarsdoorsnede waar de arm de romp verlaat, schat op 0.815 H en 0.105 H naast het midden
    sch = Vector((cx + kant * 0.105 * H, 0.0, z(0.805)))
    sch.y = snee(z(0.80), d=0.01, kant=kant, xmin=0.13, xmax=0.22)[0].y
    elleboog = sch.lerp(wrist, 0.52)
    # elleboog op de mesh: midden van punten dicht bij die plek (dwars op de arm)
    rond = [v for v in V if (v - elleboog).length < 0.045 and (v.x - cx) * kant > 0]
    if rond:
        elleboog = sum(rond, Vector()) / len(rond)
    bones[f"shoulder.{s}"] = (Vector((cx + kant * 0.02 * H, R(0.80).y, z(0.80))), sch)
    bones[f"upper_arm.{s}"] = (sch, elleboog)
    bones[f"forearm.{s}"] = (elleboog, wrist)
    bones[f"hand.{s}"] = (wrist, vinger)
    # benen
    heup = snee(z(0.47), kant=kant, xmax=0.15)[0]
    knie = snee(z(0.285), kant=kant, xmax=0.15)[0]
    enkel = snee(z(0.05), kant=kant, xmin=0.02, xmax=0.15)[0]
    teen = Vector((enkel.x, lo.y + 0.02, z(0.015)))
    heup.z = z(0.505)
    heup.y = romp_y(z(0.505))
    bones[f"thigh.{s}"] = (heup, knie)
    bones[f"shin.{s}"] = (knie, enkel)
    bones[f"foot.{s}"] = (enkel, teen)
bek = R(0.53)
borst = R(0.72)
hals = Vector((cx, snee(z(0.845), d=0.008, xmax=0.045)[0].y, z(0.84)))
kin = Vector((cx, snee(z(0.865), d=0.008, xmax=0.05)[0].y, z(0.875)))
bones["spine"] = (bek, R(0.60))
bones["spine.001"] = (R(0.60), borst)
bones["spine.002"] = (borst, R(0.80))
bones["spine.003"] = (R(0.80), hals)
bones["neck"] = (hals, kin)
bones["head"] = (kin, Vector((cx, kin.y, hi.z)))
ad = bpy.data.armatures.new("rig")
arm = bpy.data.objects.new("rig", ad)
bpy.context.scene.collection.objects.link(arm)
bpy.context.view_layer.objects.active = arm
bpy.ops.object.mode_set(mode="EDIT")
eb = {}
for n, (k, t) in bones.items():
    b = ad.edit_bones.new(n)
    b.head, b.tail = k, t
    eb[n] = b
ouder = {"spine.001": "spine", "spine.002": "spine.001", "spine.003": "spine.002", "neck": "spine.003", "head": "neck"}
for s in "LR":
    ouder.update({f"shoulder.{s}": "spine.003", f"upper_arm.{s}": f"shoulder.{s}", f"forearm.{s}": f"upper_arm.{s}",
                  f"hand.{s}": f"forearm.{s}", f"thigh.{s}": "spine", f"shin.{s}": f"thigh.{s}", f"foot.{s}": f"shin.{s}"})
for n, p in ouder.items():
    eb[n].parent = eb[p]
    eb[n].use_connect = False
bpy.ops.object.mode_set(mode="OBJECT")
for n, (k, t) in bones.items():
    print("BOT", n, tuple(round(c, 3) for c in k), tuple(round(c, 3) for c in t))
# kleur per deel, zoals delen in verschillende kleuren filament (het midden van elk vlak naar het dichtstbijzijnde bot)
KLEUR = {"kop": "EDE3D2", "romp": "6EC6C0", "bovenarm": "B9A3E3", "onderarm": "B9A3E3", "hand": "EDE3D2",
         "dij": "F08A7E", "scheen": "7FA8E8", "voet": "7FA8E8"}
DEEL = {"head": "kop", "neck": "kop", "spine": "romp", "spine.001": "romp", "spine.002": "romp", "spine.003": "romp",
        "shoulder": "romp", "upper_arm": "bovenarm", "forearm": "onderarm", "hand": "hand", "thigh": "dij",
        "shin": "scheen", "foot": "voet"}
if os.environ.get("HELD_KLEUR", "1") == "1":
    ob.data.materials.clear()
    namen = list(dict.fromkeys(KLEUR))
    for n in namen:
        m = bpy.data.materials.new("held_" + n)
        h = KLEUR[n]
        c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        m.diffuse_color = (*c, 1)
        m.use_nodes = True
        m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*c, 1)
        ob.data.materials.append(m)
    segs = [(n, k, t) for n, (k, t) in bones.items()]
    def dichtst(p):
        best, bn = 1e9, None
        for n, k, t in segs:
            d = t - k
            u = max(0.0, min(1.0, (p - k).dot(d) / max(d.length_squared, 1e-12)))
            a = (p - (k + d * u)).length
            if a < best:
                best, bn = a, n
        return bn
    for f in ob.data.polygons:
        n = dichtst(f.center).split(".")[0] if not dichtst(f.center).startswith("spine") else "spine"
        f.material_index = namen.index(DEEL.get(n, "romp"))
else:   # één materiaal held_huid; hoofdbeeld.py (HB_DEELKLEUR) geeft daarna elk deel een eigen kleur
    ob.data.materials.clear()
    m = bpy.data.materials.new("held_huid")
    m.diffuse_color = (0.8, 0.8, 0.8, 1)
    ob.data.materials.append(m)
ob.parent = arm
ob.modifiers.new("Armature", "ARMATURE").object = arm
ob.name = "held"
ob["bron"] = "Blender Human Base Meshes v1.4.1, GEO-body_male_realistic, CC0 1.0 (Blender Studio)"
bpy.ops.wm.save_as_mainfile(filepath=UIT)
print("KLAAR", UIT, len(ob.data.vertices))
