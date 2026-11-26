"""Worm en mot voor het rustige leven in het hol (Mila, 26 nov 2026, issue #179; vraag Olaf 25 nov 23:30).
Daan #106 vond de oude worm (roze blokje) en mot (wit streepje) kapotte pixels. Nu in de huisstijl van de vleermuis:
rond, groot oog, donkere rand rondom (zodat ze op de roodbruine aarde en in het fakkellicht los blijven staan).
    <venv>/bin/python beestjes.py <uit.png> <breedte> <hoogte> <samples> <stand>
Standen worm: piek (kop half uit de aarde), op (rechtop, kijkt je aan), links, rechts (buigt en kijkt opzij).
Standen mot: open (vleugels wijd), dicht (vleugels omhoog tegen elkaar).
Zelfde camera en licht als alle 3D (gedeeld.py). Doorzichtig.
Donkere rand: een omgekeerde schil om elk deel (Backfacing: voorkant doorzichtig, achterkant donker),
dezelfde dikte in Blender-eenheden, dus na verkleinen ±1 spelpixel. Geen Freestyle nodig.
"""
import sys, os, math
M = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, M)
import bpy, bmesh
from mathutils import Vector
import gedeeld as g

RAND = "2a1418"   # donkere rand: pruimbruin, donkerder dan de aarde en de gangwand


def rand_mat():
    m = bpy.data.materials.get("rand")
    if m:
        return m
    m = bpy.data.materials.new("rand")
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    uit = nt.nodes.new("ShaderNodeOutputMaterial")
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    mix = nt.nodes.new("ShaderNodeMixShader")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*g.hex2(RAND), 1)
    em.inputs["Strength"].default_value = 1.0
    door = nt.nodes.new("ShaderNodeBsdfTransparent")
    nt.links.new(geo.outputs["Backfacing"], mix.inputs["Fac"])
    nt.links.new(em.outputs["Emission"], mix.inputs[1])
    nt.links.new(door.outputs["BSDF"], mix.inputs[2])
    nt.links.new(mix.outputs["Shader"], uit.inputs["Surface"])
    return m


def met_rand(o, dikte):
    """Schil om object o: kopie van het net, dikte langs de normalen naar buiten, normalen omgedraaid."""
    bpy.ops.object.select_all(action="DESELECT")
    o.select_set(True); bpy.context.view_layer.objects.active = o
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    me = o.data.copy()
    bm = bmesh.new(); bm.from_mesh(me)
    bm.normal_update()
    for v in bm.verts:
        v.co += v.normal * dikte
    bmesh.ops.reverse_faces(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free()
    me.materials.clear(); me.materials.append(rand_mat())
    s = bpy.data.objects.new(o.name + "_rand", me)
    bpy.context.scene.collection.objects.link(s)
    s.parent = o
    s.visible_shadow = False
    for p in me.polygons:
        p.use_smooth = True
    return s


def bol(naam, loc, schaal, mat, segs=32, rot=(0, 0, 0), rand=0.022):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = naam; o.scale = schaal
    o.data.materials.append(mat); bpy.ops.object.shade_smooth()
    if rand:
        met_rand(o, rand)
    return o


# ---------------------------------------------------------------- worm
def worm(stand):
    g.leeg(); g.camera(hoogte_midden=0.32, schaal=1.4); g.licht()
    huid = g.mat("worm_huid", "ff7d98", rough=0.45, spec=0.35, sss=0.15)
    ring = g.mat("worm_ring", "a8304e", rough=0.5, spec=0.3)
    buik = g.mat("worm_buik", "ffb3c1", rough=0.45, spec=0.3)
    oog = g.mat("worm_oog", "oogwit", rough=0.2, spec=0.6)
    pupil = g.mat("worm_pupil", "pupil", rough=0.2, spec=0.8)
    blos = g.mat("worm_blos", "ff9aa8", rough=0.6)
    aarde = g.mat("worm_aarde", "4e2e26", rough=0.95, spec=0.1)
    aarde_l = g.mat("worm_kruim", "7a4a36", rough=0.95, spec=0.1)
    gat = g.mat("worm_gat", "1c0e0e", rough=1.0, spec=0.0)

    # hoopje aarde (altijd even breed, zodat het nulpunt in elk beeld op dezelfde plek staat)
    bol("hoop", (0, 0, 0.02), (0.36, 0.22, 0.1), aarde, rand=0.02)
    bol("gat", (0, -0.06, 0.1), (0.17, 0.09, 0.035), gat, rand=0)
    for x, y, z, r in ((-0.30, -0.12, 0.04, 0.05), (0.31, -0.10, 0.035, 0.045), (-0.16, -0.19, 0.075, 0.04),
                       (0.18, -0.18, 0.07, 0.035), (0.05, -0.21, 0.05, 0.03)):
        bol("kruim", (x, y, z), (r, r, r * 0.8), aarde_l, segs=16, rand=0.015)

    # lijf als ketting van bollen langs een boog; kop bovenaan
    hoog = {"piek": 0.26, "op": 0.56, "links": 0.52, "rechts": 0.52}[stand]
    buig = {"piek": 0.0, "op": 0.03, "links": -0.24, "rechts": 0.24}[stand]
    n = 4 if stand != "piek" else 2
    ys = -0.05
    punten = []
    for i in range(n + 1):
        t = i / n
        z = 0.1 + t * (hoog - 0.1)
        x = buig * t * t + (0.03 * math.sin(t * math.pi * 1.5) if stand == "op" else 0)
        punten.append((x, ys, z))
    for i, (x, y, z) in enumerate(punten[:-1]):
        r = 0.15 - 0.006 * i
        bol(f"lijf{i}", (x, y, z), (r, r, r * 0.95), huid, rand=0.022)
        # ring (iets donkerder, smal) tussen de bollen: geeft de wormstreepjes
        if i > 0:
            bol(f"ring{i}", (x, y - 0.005, z - 0.035), (r * 1.04, r * 1.04, r * 0.26), ring, rand=0)
    kx, ky, kz = punten[-1]
    kijk = {"piek": 0.0, "op": 0.0, "links": -1.0, "rechts": 1.0}[stand]
    kop = bol("kop", (kx, ky, kz), (0.2, 0.17, 0.185), huid, rand=0.026)
    bol("snuit", (kx + kijk * 0.05, ky - 0.13, kz - 0.065), (0.1, 0.06, 0.055), buik, rand=0)
    for k in (-1, 1):
        ox = kx + k * 0.08 + kijk * 0.045
        bol("oog", (ox, ky - 0.135, kz + 0.04), (0.075, 0.05, 0.09), oog, rand=0.014)
        bol("pupil", (ox + kijk * 0.028, ky - 0.18, kz + 0.033), (0.045, 0.024, 0.055), pupil, rand=0)
        bol("glim", (ox + kijk * 0.028 - 0.015, ky - 0.2, kz + 0.058), (0.014, 0.007, 0.014),
            g.mat("worm_glim", "ffffff", rough=0.1, emis=1.0), segs=12, rand=0)
        if stand != "piek":
            bol("blos", (kx + k * 0.145 + kijk * 0.04, ky - 0.11, kz - 0.06), (0.035, 0.014, 0.02), blos, rand=0)


# ---------------------------------------------------------------- mot
def vleugel(naam, kant, stand, mat, vlek, voor=True):
    """Ronde vleugel als platte schijf; open = wijd opzij, dicht = omhoog geklapt."""
    me = bpy.data.meshes.new(naam); bm = bmesh.new()
    if voor:
        pts = [(0.0, 0.03), (0.10, 0.17), (0.30, 0.25), (0.50, 0.24), (0.50, 0.12), (0.36, 0.0), (0.12, -0.05)]
    else:
        pts = [(0.0, -0.02), (0.12, -0.04), (0.30, -0.06), (0.34, -0.16), (0.24, -0.25), (0.10, -0.22), (0.02, -0.10)]
    hoek = {"open": 0.1, "dicht": 0.45}[stand]
    vs = []
    for x, z in pts:
        # draai om de lijfas (y), zodat de vleugel omhoog klapt
        xr = x * math.cos(hoek)
        zr = z + x * math.sin(hoek)
        vs.append(bm.verts.new((kant * (0.05 + xr), 0.0 if voor else 0.02, zr)))
    bm.faces.new(vs if kant > 0 else list(reversed(vs)))
    bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(naam, me); bpy.context.scene.collection.objects.link(o)
    o.data.materials.append(mat)
    mod = o.modifiers.new("dik", "SOLIDIFY"); mod.thickness = 0.035
    sub = o.modifiers.new("rond", "SUBSURF"); sub.levels = 2; sub.render_levels = 2
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active = o; o.select_set(True)
    bpy.ops.object.modifier_apply(modifier="dik"); bpy.ops.object.modifier_apply(modifier="rond")
    bpy.ops.object.shade_smooth()
    met_rand(o, 0.02)
    # vlek op de voorvleugel (oogvlek), helpt "mot" lezen
    if voor:
        xr = 0.36 * math.cos(hoek); zr = 0.15 + 0.36 * math.sin(hoek)
        bol("vlek", (kant * (0.05 + xr), -0.03, zr), (0.045, 0.012, 0.045), vlek, segs=16, rand=0)
    return o


def mot(stand):
    g.leeg(); g.camera(hoogte_midden=0.05, schaal=1.4); g.licht()
    vleugel_m = g.mat("mot_vleugel", "efe0bf", rough=0.75, spec=0.15, sss=0.15)
    achter_m = g.mat("mot_achter", "d9bb8c", rough=0.75, spec=0.15)
    vlek = g.mat("mot_vlek", "7a4a34", rough=0.7)
    lijf = g.mat("mot_lijf", "c9ae86", rough=0.9, spec=0.1)
    kraag = g.mat("mot_kraag", "fff6e4", rough=0.95, spec=0.05)
    oog = g.mat("mot_oog", "pupil", rough=0.15, spec=0.9)
    spriet = g.mat("mot_spriet", "5a3a2c", rough=0.7)

    for k in (-1, 1):
        vleugel("achtervleugel", k, stand, achter_m, vlek, voor=False)
        vleugel("voorvleugel", k, stand, vleugel_m, vlek, voor=True)
    bol("lijf", (0, -0.03, -0.06), (0.075, 0.07, 0.17), lijf, rand=0.02)
    bol("kraag", (0, -0.05, 0.08), (0.1, 0.09, 0.07), kraag, rand=0.02)
    bol("kop", (0, -0.07, 0.16), (0.085, 0.08, 0.075), lijf, rand=0.02)
    for k in (-1, 1):
        bol("oog", (k * 0.05, -0.135, 0.165), (0.04, 0.03, 0.045), oog, rand=0)
        bol("glim", (k * 0.05 - 0.012, -0.165, 0.18), (0.01, 0.005, 0.01),
            g.mat("mot_glim", "ffffff", rough=0.1, emis=1.0), segs=12, rand=0)
        # geveerde spriet: steel plus drie veertjes per kant
        bpy.ops.curve.primitive_bezier_curve_add()
        c = bpy.context.active_object; c.name = "spriet"
        sp = c.data.splines[0]
        sp.bezier_points[0].co = (k * 0.03, -0.08, 0.22)
        sp.bezier_points[0].handle_left = (k * 0.02, -0.08, 0.18)
        sp.bezier_points[0].handle_right = (k * 0.05, -0.08, 0.30)
        sp.bezier_points[1].co = (k * 0.15, -0.08, 0.32)
        sp.bezier_points[1].handle_left = (k * 0.10, -0.08, 0.36)
        sp.bezier_points[1].handle_right = (k * 0.22, -0.08, 0.36)
        c.data.bevel_depth = 0.014
        c.data.materials.append(spriet)
        for t, l in ((0.45, 0.05), (0.7, 0.055), (0.92, 0.045)):
            px = k * (0.03 + 0.14 * t); pz = 0.22 + 0.14 * math.sin(t * math.pi / 2)
            bol("veer", (px + k * 0.015, -0.085, pz + 0.018), (0.034, 0.012, l * 0.8), spriet, segs=12,
                rot=(0, k * -0.7, 0), rand=0)
    # pootjes: twee donkere stipjes onder het lijf
    for k in (-1, 1):
        bol("poot", (k * 0.05, -0.06, -0.2), (0.018, 0.018, 0.04), spriet, segs=12, rand=0)


if __name__ == "__main__":
    uit, W, H, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    stand = sys.argv[5]
    if stand in ("open", "dicht"):
        mot(stand)
    else:
        worm(stand)
    g.render(uit, W, H, S, doorzichtig=True)
