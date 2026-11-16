"""Vleermuis voor het hol (Mila, 16 nov 2026): klein levend ding (bericht hoofdchat 09:45 NL, punt 1).
Hangt ondersteboven aan het plafond van de gang en fladdert op als een held eronder loopt.
    <venv>/bin/python vleermuis.py <uit.png> <breedte> <hoogte> <samples> <stand: hang|vlieg>
Zelfde camera en licht als alle 3D (gedeeld.py). Doorzichtig.
"""
import sys, os, math
M = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, M)
import bpy, bmesh
import gedeeld as g

def bol(naam, loc, schaal, mat, segs=32, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = naam; o.scale = schaal
    o.data.materials.append(mat); bpy.ops.object.shade_smooth(); return o

def vleugel(naam, kant, open_, mat):
    # plat vlak met drie schulpen aan de onderrand, als een cape
    me = bpy.data.meshes.new(naam); bm = bmesh.new()
    pts = [(0, 0), (0.55, 0.25), (0.9, 0.05), (0.75, -0.18), (0.6, -0.05), (0.45, -0.25), (0.3, -0.08), (0.15, -0.28), (0, -0.2)]
    vs = [bm.verts.new((kant * (x if open_ else 0.2 + x * 0.12), -0.02 - (0 if open_ else 0.05 + x * 0.12), z * (1 if open_ else 1.1))) for x, z in pts]
    bm.faces.new(vs); bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(naam, me); bpy.context.scene.collection.objects.link(o)
    o.data.materials.append(mat)
    mod = o.modifiers.new("dik", "SOLIDIFY"); mod.thickness = 0.03
    return o

def maak(stand):
    g.leeg(); g.camera(hoogte_midden=0.0, schaal=1.6); g.licht()
    lijf = g.mat("vm_lijf", "5b3a6e", rough=0.7, spec=0.2)
    vlies = g.mat("vm_vlies", "8a5aa0", rough=0.6, spec=0.2, sss=0.2)
    oog = g.mat("vm_oog", "ffffff", rough=0.2, spec=0.6)
    pupil = g.mat("vm_pupil", "1a1022", rough=0.2, spec=0.8)
    roze = g.mat("vm_roze", "f29bb0", rough=0.6)
    tand = g.mat("vm_tand", "fff6e8", rough=0.4)
    hang = stand == "hang"
    o = bpy.data.objects.new("vleermuis", None); bpy.context.scene.collection.objects.link(o)
    delen = []
    delen.append(bol("lijf", (0, 0, 0), (0.24, 0.2, 0.26), lijf))
    for k in (-1, 1):
        delen.append(bol("oor", (k * 0.14, 0, 0.26), (0.07, 0.04, 0.13), lijf, rot=(0, k * -0.35, 0)))
        delen.append(bol("oor_in", (k * 0.14, -0.03, 0.25), (0.04, 0.02, 0.08), roze, rot=(0, k * -0.35, 0)))
        delen.append(bol("oog", (k * 0.085, -0.17, 0.06), (0.075, 0.05, 0.085), oog))
        delen.append(bol("pupil", (k * 0.08, -0.215, 0.05), (0.04, 0.02, 0.05), pupil))
        delen.append(bol("wang", (k * 0.15, -0.16, -0.05), (0.04, 0.015, 0.025), roze))
        delen.append(vleugel("vleugel", k, not hang, vlies))
        delen.append(bol("voet", (k * 0.06, 0, -0.27), (0.03, 0.03, 0.05), lijf))
    delen.append(bol("tand", (0.03, -0.19, -0.07), (0.018, 0.01, 0.03), tand))
    for d in delen:
        d.parent = o
    if hang:
        o.rotation_euler[1] = math.pi   # ondersteboven, voetjes aan het plafond
        o.location.z = 0.0

if __name__ == "__main__":
    uit, W, H, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    maak(sys.argv[5]); g.render(uit, W, H, S, doorzichtig=True)
