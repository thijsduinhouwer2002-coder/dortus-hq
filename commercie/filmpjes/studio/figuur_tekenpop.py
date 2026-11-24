"""Houten tekenpop voor de winkelbeelden van Click Joints Pro (23 nov 2026, opdracht hoofdchat ±22:35 NL: Thijs vindt
dat een mooie "ragdoll" beter werkt dan de robot; wij lezen dat als de klassieke houten tekenpop).

Helemaal door ons gemaakt met dit script (geen download, geen AI-model, geen merk): een eivormig hoofd zonder gezicht,
een slanke romp in twee delen met een bal in de taille, ovale ledematen die bij elk gewricht smal worden, en
peddelvormige handen en voeten. Eén materiaal: licht beukenhout met een fijne nerf en een zachte glans. De gewrichten
maakt de knop Figure from rig van Click Joints Pro; die kleuren we in renders messing (`goud()`).

Gebruik (na het installeren van de Pro-zip, want Make watertight van de add-on maakt er één gesloten mesh van):
    import figuur_tekenpop as T
    arm, fig, punten = T.laad_tekenpop(220.0)
of `figuur_laden.laad_figuur("tekenpop")`. Rig met Mixamo-namen (dezelfde rig als de robot en e2e/proef_mens.py).
Kijkt naar -y, links is +x, voeten op z=0, maten in mm (bij 220 mm hoog).

Wat de add-on nodig heeft (geleerd met de robot, zie LEESMIJ): elleboog en knie dicht bij de huid aan de buigkant
(4,4 en 6 mm), niets dwars op de schouder (de bovenarm begint met een bol die de zijkant van de borst net raakt),
ruimte tussen de benen (heupen op x = +-17) en het lid bij een kogel hoogstens 1,3 keer zo breed als zijn smalste stuk.
"""
import math
import os

import bpy
import bmesh
from mathutils import Matrix, Vector

import figuur_laden as FL

HOUT = "E4B47C"     # licht beukenhout (sRGB), vroeghout
NERF = "AE7542"     # laathout, de lijnen van de nerf
MESSING = "FFC24A"  # gewrichten in renders
HUID = "cj_tekenpop_huid"

ELLEBOOG_R = 6.6   # straal van de arm bij de elleboog (mm bij 220 mm)
KNIE_R = 9.0       # straal van het been bij de knie


def punten(h=220.0):
    """Gewrichtspunten in mm bij hoogte h (zelfde sleutels als de robot, voor maak_rig)."""
    f = h / 220.0
    p = {
        "pelvis": (0, 0, 118), "spine-4": (0, 0, 124), "spine-2": (0, 0, 145), "spine-1": (0, 0, 163),
        "neck": (0, 0, 180), "head": (0, 0, 192), "head-2": (0, 0, 219),
    }
    for k, s in (("l", 1), ("r", -1)):
        p.update({
            f"{k}-upper-leg": (17 * s, 0, 116), f"{k}-knee": (18 * s, -1, 60), f"{k}-ankle": (19 * s, 1, 13),
            f"{k}-foot-1": (19 * s, -16, 3),
            f"{k}-clavicle": (4 * s, 0, 175), f"{k}-shoulder": (27.5 * s, 0, 175), f"{k}-elbow": (45.5 * s, 1, 131),
            f"{k}-hand": (55.5 * s, -1, 100), f"{k}-hand-2": (58.5 * s, -2, 90),
        })
    return {n: Vector(c) * f for n, c in p.items()}


def rig_punten(p, f=1.0):
    """Elleboog en knie dicht bij de huid aan de buigkant (4,4 en 6 mm), zoals bij de robot. Elleboog buigt naar
    voren (-y), knie naar achteren (+y)."""
    q = dict(p)
    for k in "lr":
        q[f"{k}-elbow"] = p[f"{k}-elbow"] + Vector((0, -ELLEBOOG_R + 4.4, 0)) * f
        q[f"{k}-knee"] = p[f"{k}-knee"] + Vector((0, KNIE_R - 6.0, 0)) * f
    return q


def _richting(a, b, op=Vector((0, -1, 0))):
    """Draaiing die z naar (b - a) zet en y zo veel mogelijk naar `op`."""
    z = (Vector(b) - Vector(a)).normalized()
    x = op.cross(z).normalized()
    y = z.cross(x).normalized()
    return Matrix((x, y, z)).transposed()


def _klaar(bm, oud, m):
    nieuw = [v for v in bm.verts if v not in oud]
    bmesh.ops.transform(bm, matrix=m, verts=nieuw)
    for fc in {f for v in nieuw for f in v.link_faces}:
        fc.smooth = True


def ei(bm, mid, r, taps=0.0, macht=2.0, draai=None, plat_onder=None):
    """Afgeronde vorm: superellipsoïde met stralen r (x, y, z). taps > 0: bovenkant breder (x en y schalen met
    1 + taps * z/rz). macht 2 = ellipsoïde, hoger = meer als een afgeronde doos. plat_onder: lokale z waaronder alles
    plat wordt (zool)."""
    oud = set(bm.verts)
    bmesh.ops.create_uvsphere(bm, u_segments=48, v_segments=28, radius=1.0)
    e = 2.0 / macht
    for v in [v for v in bm.verts if v not in oud]:
        n = v.co.normalized()
        x, y, z = (math.copysign(abs(c) ** e, c) for c in n)
        s = 1.0 + taps * z
        v.co = Vector((x * r[0] * s, y * r[1] * s, z * r[2]))
        if plat_onder is not None and v.co.z < plat_onder:
            v.co.z = plat_onder
    m = Matrix.Translation(Vector(mid)) @ (draai.to_4x4() if draai is not None else Matrix.Identity(4))
    _klaar(bm, oud, m)


def lid(bm, a, b, ra, rm, rb, tm=0.35, ovaal=(1.0, 1.0), op=Vector((0, -1, 0))):
    """Ovaal lid van a naar b: straal ra bij a, dikst (rm) op fractie tm, rb bij b, met bolle einden (die vallen in
    het buurlid, zodat het één gladde vorm wordt die bij elk gewricht smal is, zoals bij een tekenpop)."""
    a, b = Vector(a), Vector(b)
    L = (b - a).length

    def straal(t):
        if t <= tm:
            return ra + (rm - ra) * math.sin(0.5 * math.pi * t / tm)
        return rb + (rm - rb) * math.cos(0.5 * math.pi * (t - tm) / (1 - tm))
    prof = []   # (z, straal)
    for k in range(1, 9):
        g = 0.5 * math.pi * k / 9
        prof.append((-ra * math.cos(g), ra * math.sin(g)))
    for i in range(0, 41):
        t = i / 40
        prof.append((L * t, straal(t)))
    for k in range(8, 0, -1):
        g = 0.5 * math.pi * k / 9
        prof.append((L + rb * math.cos(g), rb * math.sin(g)))
    n = 40
    oud = set(bm.verts)
    ringen = []
    for z, r in prof:
        ringen.append([bm.verts.new((r * ovaal[0] * math.cos(2 * math.pi * j / n),
                                     r * ovaal[1] * math.sin(2 * math.pi * j / n), z)) for j in range(n)])
    pa = bm.verts.new((0, 0, -ra))
    pb = bm.verts.new((0, 0, L + rb))
    for r0, r1 in zip(ringen, ringen[1:]):
        for j in range(n):
            bm.faces.new((r0[j], r0[(j + 1) % n], r1[(j + 1) % n], r1[j]))
    for j in range(n):
        bm.faces.new((pa, ringen[0][(j + 1) % n], ringen[0][j]))
        bm.faces.new((pb, ringen[-1][j], ringen[-1][(j + 1) % n]))
    _klaar(bm, oud, Matrix.Translation(a) @ _richting(a, b, op).to_4x4())


def bouw_vormen(p, f=1.0):
    """Alle vormen van de tekenpop (maten in mm bij 220 mm, f schaalt mee). Geeft een bmesh."""
    bm = bmesh.new()

    def P(*c):
        return Vector(c) * f
    s = f
    # ---- hoofd en hals: ei zonder gezicht, smalle kant naar onder (kin), iets naar voren gekanteld ----
    ei(bm, P(0, -1.5, 205), (10.6 * s, 12.2 * s, 15.0 * s), taps=0.13, draai=Matrix.Rotation(math.radians(-8), 3, "X"))
    lid(bm, P(0, 0.5, 177), P(0, -0.5, 194), 5.6 * s, 5.0 * s, 5.0 * s, tm=0.5)
    # ---- romp in twee delen: borstkas (breed bij de schouders), bal in de taille, bekken ----
    ei(bm, P(0, 0.5, 162), (21.5 * s, 12.0 * s, 17.5 * s), taps=0.20, macht=3.0)
    ei(bm, P(0, 0.0, 146.5), (8.5 * s, 7.5 * s, 7.0 * s))
    ei(bm, P(0, 0.5, 127), (17.0 * s, 11.0 * s, 12.0 * s), taps=-0.10, macht=2.6)
    for k in "lr":
        # ---- armen: bovenarm begint met een bol die de zijkant van de borst net raakt ----
        sh, el, ha, h2 = p[f"{k}-shoulder"], p[f"{k}-elbow"], p[f"{k}-hand"], p[f"{k}-hand-2"]
        lid(bm, sh, el, 7.6 * s, 8.0 * s, ELLEBOOG_R * s, tm=0.25)
        lid(bm, el, ha, ELLEBOOG_R * s, 7.0 * s, 4.4 * s, tm=0.28)
        # hand: peddel, plat in de richting van de duim, handpalm naar binnen; duim als klein ovaal aan de voorkant
        z = (h2 - ha).normalized()
        sx = 1 if k == "l" else -1
        dr = _richting(ha, h2)
        ei(bm, ha + z * 9.5 * s, (3.6 * s, 6.4 * s, 10.5 * s), draai=dr)
        ei(bm, ha + z * 4.5 * s + dr @ P(-1.2 * sx, -5.6, 0), (2.4 * s, 2.6 * s, 5.0 * s),
           draai=dr @ Matrix.Rotation(math.radians(22 * sx), 3, "Y"))
        # ---- benen ----
        hp, kn, an = p[f"{k}-upper-leg"], p[f"{k}-knee"], p[f"{k}-ankle"]
        lid(bm, hp, kn, 10.8 * s, 11.6 * s, KNIE_R * s, tm=0.22)
        lid(bm, kn, an, KNIE_R * s, 9.6 * s, 5.4 * s, tm=0.3)
        # voet: peddel met een platte zool, naar voren
        ei(bm, P(19 * sx, -6.5, 5.2), (7.4 * s, 15.0 * s, 5.6 * s), plat_onder=-5.2 * s, macht=2.2)
    return bm


def hout():
    """Licht beukenhout: fijne nerf (ringen om de lengteas van elk deel, vervormd met ruis), kleur die per plank iets
    verschilt, zachte zijdeglans (laklaag) en de nerf als heel licht reliëf. Kleur in de nodes en in de weergave."""
    m = bpy.data.materials.get("tp_hout") or bpy.data.materials.new("tp_hout")
    m.diffuse_color = FL.srgb(HOUT)
    m.roughness = 0.45
    try:
        m.use_nodes = True
    except Exception:  # noqa: BLE001
        pass
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    N = nt.nodes.new
    uit = N("ShaderNodeOutputMaterial")
    b = N("ShaderNodeBsdfPrincipled")
    nt.links.new(b.outputs[0], uit.inputs["Surface"])
    tc = N("ShaderNodeTexCoord")
    # nerf: ringen om de z-as van het deel (Object), een beetje gekanteld en vervormd: lange strepen langs het lid
    mp = N("ShaderNodeMapping")
    mp.inputs["Location"].default_value = (380.0, -260.0, 0.0)
    mp.inputs["Rotation"].default_value = (0.04, 0.03, 0.0)
    nt.links.new(tc.outputs["Object"], mp.inputs["Vector"])
    golf = N("ShaderNodeTexWave")
    golf.wave_type = "RINGS"
    golf.rings_direction = "Z"
    golf.wave_profile = "SAW"
    golf.inputs["Scale"].default_value = 0.2
    golf.inputs["Distortion"].default_value = 9.0
    golf.inputs["Detail"].default_value = 3.0
    golf.inputs["Detail Scale"].default_value = 0.12
    nt.links.new(mp.outputs[0], golf.inputs["Vector"])
    # fijne poriën: ruis uitgerekt langs z
    mp2 = N("ShaderNodeMapping")
    mp2.inputs["Scale"].default_value = (1.0, 1.0, 0.06)
    nt.links.new(tc.outputs["Object"], mp2.inputs["Vector"])
    ruis = N("ShaderNodeTexNoise")
    ruis.inputs["Scale"].default_value = 2.2
    ruis.inputs["Detail"].default_value = 6.0
    nt.links.new(mp2.outputs[0], ruis.inputs["Vector"])
    # grote vlekken: kleur verschilt iets over het deel
    vlek = N("ShaderNodeTexNoise")
    vlek.inputs["Scale"].default_value = 0.035
    nt.links.new(tc.outputs["Object"], vlek.inputs["Vector"])
    ramp = N("ShaderNodeValToRGB")
    e = ramp.color_ramp.elements
    e[0].position, e[0].color = 0.0, FL.srgb(HOUT)
    e[1].position, e[1].color = 1.0, FL.srgb(NERF)
    e.new(0.55).color = FL.srgb("D6A066")
    mix = N("ShaderNodeMath")
    mix.operation = "MULTIPLY_ADD"
    mix.inputs[1].default_value = 0.75
    pw = N("ShaderNodeMath")
    pw.operation = "POWER"
    pw.inputs[1].default_value = 3.0
    nt.links.new(golf.outputs["Fac"], pw.inputs[0])
    nt.links.new(pw.outputs[0], mix.inputs[0])
    por = N("ShaderNodeMath")
    por.operation = "MULTIPLY"
    por.inputs[1].default_value = 0.22
    nt.links.new(ruis.outputs["Fac"], por.inputs[0])
    nt.links.new(por.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], ramp.inputs["Fac"])
    tint = N("ShaderNodeMix")
    tint.data_type = "RGBA"
    tint.blend_type = "MULTIPLY"
    tint.inputs["Factor"].default_value = 0.18
    nt.links.new(ramp.outputs["Color"], tint.inputs["A"])
    vr = N("ShaderNodeValToRGB")
    vr.color_ramp.elements[0].color = (1.0, 0.86, 0.72, 1)
    vr.color_ramp.elements[1].color = (1, 1, 1, 1)
    nt.links.new(vlek.outputs["Fac"], vr.inputs["Fac"])
    nt.links.new(vr.outputs["Color"], tint.inputs["B"])
    nt.links.new(tint.outputs["Result"], b.inputs["Base Color"])
    for naam, w in (("Roughness", 0.42), ("Coat Weight", 0.35), ("Coat Roughness", 0.16), ("Specular IOR Level", 0.5),
                    ("Subsurface Weight", 0.03)):
        if naam in b.inputs:
            b.inputs[naam].default_value = w
    # nerf als licht reliëf (laathout iets lager)
    bump = N("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.08
    if "Distance" in bump.inputs:
        bump.inputs["Distance"].default_value = 0.02
    nt.links.new(pw.outputs[0], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], b.inputs["Normal"])
    if "Coat Normal" in b.inputs:
        nt.links.new(bump.outputs["Normal"], b.inputs["Coat Normal"])
    return m


def goud(hexkleur=MESSING):
    """Gepoetst messing voor kogel, kom en scharnier (in renders)."""
    m = bpy.data.materials.get("tp_messing") or bpy.data.materials.new("tp_messing")
    m.diffuse_color = FL.srgb(hexkleur)
    try:
        m.use_nodes = True
    except Exception:  # noqa: BLE001
        pass
    nt = m.node_tree
    b = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
    b.inputs["Base Color"].default_value = FL.srgb(hexkleur)
    for naam, w in (("Metallic", 0.85), ("Roughness", 0.26), ("Coat Weight", 0.3), ("Coat Roughness", 0.05)):
        if naam in b.inputs:
            b.inputs[naam].default_value = w
    return m


def materialen(delen, rand_mm=0.35):
    """Na Figure from rig, alleen voor renders: alles wat de add-on aan een gewricht maakt (materialen 'Click Joints'
    en 'pla_grijs') wordt messing; vlakken zonder materiaal en het figuur zelf worden hout. Vlakken die niet op de
    oude buitenkant liggen (verder dan rand_mm; kogel, kom, scharnier) worden ook messing: de add-on kleurt alleen
    een deel van de kogel, en zo zie je het hele gewricht in één tel. rand_mm=None: alleen de kleuren van de add-on."""
    from mathutils.bvhtree import BVHTree
    h, g = hout(), goud()
    huid = bpy.data.meshes.get(HUID)
    bvh = BVHTree.FromPolygons([v.co for v in huid.vertices], [tuple(p.vertices) for p in huid.polygons]) if huid else None
    for o in delen:
        me = o.data
        oud = list(me.materials)
        idx = [pl.material_index for pl in me.polygons]   # clear() zet alle indexen op 0, dus eerst onthouden
        me.materials.clear()
        me.materials.append(h)
        me.materials.append(g)
        cj = {i for i, m in enumerate(oud) if m is not None and (m.name.startswith("Click Joints") or
                                                                 m.name.startswith("pla_grijs"))}
        mw = o.matrix_world
        for f in me.polygons:
            gewricht = idx[f.index] in cj
            if not gewricht and bvh is not None and rand_mm is not None:
                _l, _n, _i, d = bvh.find_nearest(mw @ f.center)
                gewricht = d is None or d > rand_mm
            f.material_index = 1 if gewricht else 0
            f.use_smooth = True
        me.update()


def laad_tekenpop(hoogte_mm=220.0, voxel_mm=0.5, stop_graden=None):
    """Bouwt de tekenpop, maakt er één gesloten mesh van (Make watertight van de add-on) en hangt de rig eraan.
    Geeft (rig, figuur, punten). stop_graden (of CJ_STOP): eindstop van linkerknie en linkerelleboog in de rig
    (Limit Rotation), standaard knie 120 en elleboog 140; Figure from rig leest de stop uit de rig."""
    voxel_mm = float(os.environ.get("CJ_VOXEL", voxel_mm))
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
    f = hoogte_mm / 220.0
    p = punten(hoogte_mm)
    bm = bouw_vormen(p, f)
    me = bpy.data.meshes.new("Figuur")
    bm.to_mesh(me)
    bm.free()
    fig = bpy.data.objects.new("Figuur", me)
    bpy.context.scene.collection.objects.link(fig)
    FL.log(f"tekenpop: {len(me.vertices)} punten voor de remesh, maat {tuple(round(d, 1) for d in fig.dimensions)}")
    bpy.context.scene.click_joints.voxel_mm = voxel_mm
    FL.actief(fig)
    bpy.ops.click_joints.maak_gesloten()
    nieuw = bpy.context.view_layer.objects.active
    if nieuw is not fig:
        bpy.data.objects.remove(fig)
        fig = nieuw
    fig.data.materials.clear()
    fig.data.materials.append(hout())
    for pl in fig.data.polygons:
        pl.material_index = 0
        pl.use_smooth = True
    huid = fig.data.copy()
    huid.name = HUID
    huid.use_fake_user = True
    fig.name = fig.data.name = "Figuur"
    FL.log(f"tekenpop na voxel {voxel_mm}: {len(fig.data.vertices)} punten, {FL.mesh_staat(fig)}")
    M = FL._mens_module(hoogte_mm)
    arm = M["maak_rig"](rig_punten(p, f))
    stop_graden = stop_graden or (float(os.environ["CJ_STOP"]) if os.environ.get("CJ_STOP") else None)
    if stop_graden:
        for pb in arm.pose.bones:
            for c in pb.constraints:
                if c.type == "LIMIT_ROTATION" and c.use_limit_x:
                    c.max_x = math.radians(stop_graden)
                    FL.log(f"stop {pb.name}: {stop_graden} graden")
    arm.data.display_type = "STICK"
    fig.modifiers.new("Armature", "ARMATURE").object = arm
    return arm, fig, p
