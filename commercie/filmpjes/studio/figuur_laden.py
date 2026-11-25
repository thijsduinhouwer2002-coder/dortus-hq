"""Studio voor de filmpjes van Click Joints Pro (23 nov 2026, opdracht hoofdchat ±11:45 NL): een figuur met eigen rig
inladen als één mesh die Figure from rig kan lezen, met de kleuren van het model behouden.

Gebruik in Blender (na het installeren van de Pro-zip):
    import figuur_laden as FL
    arm, body = FL.laad("/pad/model.glb", hoogte_mm=240, weg=("Backpack",))
Keuze per figuur (studio-2, 23 nov): `laad_figuur("robot")` (zelfgebouwde robot, figuur_robot.py, de standaard
voor filmpjes), `laad_figuur("mens")` (MakeHuman met kleding, studio-1) of `laad_figuur("/pad/model.glb")`.

Stappen van laad(): glb inladen, animatie en pose weg (rusthouding), alle meshes van de rig samen tot één object (ook delen die
aan een bot hangen, zoals bij de robot), schaal naar `hoogte_mm` met de voeten op z=0, Make watertight van de add-on
als de mesh open is of uit losse stukken bestaat, en daarna de kleuren per vlak terug van het origineel (de
voxel-remesh gooit de materialen weg). Alleen invoer: de knop Figure from rig doet daarna alles zelf.
"""
import os

import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree


def log(t):
    print(f"[studio] {t}", flush=True)


def actief(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob


def kader(obs):
    pts = [o.matrix_world @ Vector(c) for o in obs for c in o.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return lo, hi


def mesh_staat(ob):
    import bmesh
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    open_r = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    gezien, stukken = set(), 0
    for v in bm.verts:
        if v.index in gezien:
            continue
        stukken += 1
        rij = [v]
        gezien.add(v.index)
        while rij:
            w = rij.pop()
            for e in w.link_edges:
                o = e.other_vert(w)
                if o.index not in gezien:
                    gezien.add(o.index)
                    rij.append(o)
    bm.free()
    return {"open_randen": open_r, "stukken": stukken}


def rust(arm):
    if arm.animation_data:
        for t in list(arm.animation_data.nla_tracks):
            arm.animation_data.nla_tracks.remove(t)
        arm.animation_data_clear()
    for pb in arm.pose.bones:
        pb.location = (0, 0, 0)
        pb.rotation_quaternion = (1, 0, 0, 0)
        pb.rotation_euler = (0, 0, 0)
        pb.scale = (1, 1, 1)
    bpy.context.view_layer.update()


def staarten(arm):
    """glTF kent geen botstaarten: de import maakt piepkleine botten. Zet de staart van elk bot op de kop van zijn
    kind in de keten (UpperArm naar LowerArm, LowerArm naar Hand, enzovoort), zodat lengte en richting kloppen."""
    actief(arm)
    bpy.ops.object.mode_set(mode="EDIT")
    voorkeur = ("lowerarm", "hand", "palm", "lowerleg", "foot", "head", "neck", "torso", "chest", "abdomen", "spine")
    for eb in arm.data.edit_bones:
        kids = [c for c in eb.children]
        if not kids:
            continue
        kies = None
        for v in voorkeur:
            kies = next((c for c in kids if v in c.name.lower().replace("_", "").replace(".", "")), None)
            if kies:
                break
        if kies is None and len(kids) == 1:
            kies = kids[0]
        if kies is not None and (kies.head - eb.head).length > 1e-6:
            eb.tail = kies.head.copy()
    # botten zonder kind: zelfde richting, lengte van de ouder of een kwart daarvan
    for eb in arm.data.edit_bones:
        if not eb.children and eb.parent is not None and eb.length < 0.3 * eb.parent.length:
            r = (eb.head - eb.parent.head).normalized() if (eb.head - eb.parent.head).length > 1e-6 else (eb.tail - eb.head).normalized()
            eb.tail = eb.head + r * 0.5 * eb.parent.length
    bpy.ops.object.mode_set(mode="OBJECT")


def armen_omlaag(arm, graden):
    """Rusthouding met de armen `graden` lager (T-pose naar A-pose): de schouders zijn kogels van ±20°, dus de
    houding waarin de knop snijdt bepaalt hoe de armen er in elke pose bij hangen. Alleen invoer, voor de knop."""
    import math
    from mathutils import Matrix
    mw = arm.matrix_world
    for pb in arm.pose.bones:
        n = pb.name.lower().replace("_", "").replace(".", "")
        if "upperarm" not in n:
            continue
        kop = mw @ pb.head
        teken = 1.0 if kop.x > 0 else -1.0
        r = Matrix.Translation(kop) @ Matrix.Rotation(math.radians(graden) * teken, 4, "Y") @ Matrix.Translation(-kop)
        pb.matrix = mw.inverted() @ r @ mw @ pb.matrix
        bpy.context.view_layer.update()
    log(f"armen {graden} graden omlaag")


def kleur_terug(bron_me, bron_mw, doel):
    """Elk vlak van `doel` krijgt het materiaal van het dichtstbijzijnde vlak van de bron (zelfde wereld)."""
    bvh = BVHTree.FromPolygons([bron_mw @ v.co for v in bron_me.vertices], [tuple(p.vertices) for p in bron_me.polygons])
    mats = [p.material_index for p in bron_me.polygons]
    doel.data.materials.clear()
    for m in bron_me.materials:
        doel.data.materials.append(m)
    mw = doel.matrix_world
    for f in doel.data.polygons:
        _p, _n, i, _d = bvh.find_nearest(mw @ f.center)
        f.material_index = mats[i] if i is not None else 0
        f.use_smooth = True
    doel.data.update()


def laad(pad, hoogte_mm=240.0, weg=(), watertight="auto", armen=0.0, voxel_mm=0.6):
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
    if pad.endswith(".blend"):
        with bpy.data.libraries.load(pad, link=False) as (van, naar):
            naar.objects = list(van.objects)
        for o in naar.objects:
            if o is not None:
                bpy.context.scene.collection.objects.link(o)
    else:
        bpy.ops.import_scene.gltf(filepath=pad)
    arm = next(o for o in bpy.context.scene.objects if o.type == "ARMATURE")
    rust(arm)
    meshes = []
    for o in list(bpy.context.scene.objects):
        if o.type != "MESH":
            continue
        hoort = o.parent == arm or any(m.type == "ARMATURE" for m in o.modifiers)
        if not hoort or any(w.lower() in o.name.lower() for w in weg):
            bpy.data.objects.remove(o)
            continue
        meshes.append(o)
    log(f"meshes {[o.name for o in meshes]}")
    staarten(arm)
    if armen:
        armen_omlaag(arm, armen)
    # Vervorming van de rig vastzetten (ook de A-pose), alles los van de rig, samen tot één mesh
    dg = bpy.context.evaluated_depsgraph_get()
    for o in meshes:
        me = bpy.data.meshes.new_from_object(o.evaluated_get(dg), preserve_all_data_layers=False, depsgraph=dg)
        mw = o.matrix_world.copy()
        for m in list(o.modifiers):
            o.modifiers.remove(m)
        o.parent = None
        o.matrix_world = mw
        oud = o.data
        o.data = me
        if oud.users == 0:
            bpy.data.meshes.remove(oud)
    if armen:
        actief(arm)
        bpy.ops.object.mode_set(mode="POSE")
        bpy.ops.pose.select_all(action="SELECT")
        bpy.ops.pose.armature_apply(selected=False)
        bpy.ops.object.mode_set(mode="OBJECT")
    for o in bpy.context.view_layer.objects:
        o.select_set(o in meshes)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    if len(meshes) > 1:
        bpy.ops.object.join()
    body = bpy.context.view_layer.objects.active
    # rig: los van de lege ouder, transformaties vast
    mw = arm.matrix_world.copy()
    arm.parent = None
    arm.matrix_world = mw
    for o in list(bpy.context.scene.objects):
        if o not in (arm, body):
            bpy.data.objects.remove(o)
    # kijkrichting: de add-on rekent met voorkant -y (zoals Blenders vooraanzicht), dan zit links op +x
    links = [arm.matrix_world @ b.head_local for b in arm.data.bones
             if "upperarm" in b.name.lower().replace("_", "") and (b.name.lower().endswith((".l", "_l")) or "left" in b.name.lower())]
    if links and links[0].x < 0:
        from mathutils import Matrix
        import math
        rz = Matrix.Rotation(math.pi, 4, "Z")
        for o in (arm, body):
            o.matrix_world = rz @ o.matrix_world
        bpy.context.view_layer.update()
        log("figuur keek naar +y: 180 graden gedraaid")
    # schaal en plek: lichaam `hoogte_mm` hoog, voeten op 0, midden op x=y=0
    lo, hi = kader([body])
    f = hoogte_mm / (hi.z - lo.z)
    for o in (arm, body):
        o.matrix_world = o.matrix_world.copy()
        o.scale = o.scale * f
        o.location = o.location * f
    bpy.context.view_layer.update()
    lo, hi = kader([body])
    sch = Vector(((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, lo.z))
    for o in (arm, body):
        o.location -= sch
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        o.select_set(o in (arm, body))
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    body.name = body.data.name = "Figuur"
    st = mesh_staat(body)
    log(f"lichaam {len(body.data.vertices)} punten, {st}, maat {tuple(round(d, 1) for d in body.dimensions)}")
    if watertight == "ja" or (watertight == "auto" and (st["open_randen"] or st["stukken"] > 1)):
        bpy.context.scene.click_joints.voxel_mm = voxel_mm
        bron_me = body.data.copy()
        bron_mw = body.matrix_world.copy()
        actief(body)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not body:
            bpy.data.objects.remove(body)
            body = nieuw
        kleur_terug(bron_me, bron_mw, body)
        bpy.data.meshes.remove(bron_me)
        log(f"na watertight: {len(body.data.vertices)} punten, {mesh_staat(body)}")
    body.modifiers.new("Armature", "ARMATURE").object = arm
    return arm, body


# ---------- MakeHuman met kleding (alles uit base.obj, CC0 1.0) ----------
E2E = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
                                   "producten", "blender-gewrichten", "e2e"))


def _mens_module(hoogte_mm):
    os.environ["CJ_HOOGTE"] = str(hoogte_mm)
    pad = os.path.join(E2E, "proef_mens.py")
    src = open(pad, encoding="utf-8").read().replace("\nmain()\n", "\n")
    M = {"__name__": "proef_mens", "__file__": pad}
    exec(compile(src, pad, "exec"), M)   # noqa: S102 (eigen code uit de repo)
    return M


def _midden(o):
    vs = [o.matrix_world @ v.co for v in o.data.vertices]
    return sum(vs, Vector()) / len(vs)


# Speelgoedkleuren (sRGB hex): elk stuk kleding een eigen heldere kleur, zoals een gekleurde print
STIJL = {
    "huid": "F2C29B", "haar": "4A2C1D", "shirt": "FF6B3D", "broek": "2F6BFF", "schoen": "FFD23F",
    "pupil": "1B1B2F", "riem": "1B1B2F",
}


def srgb(h):
    c = tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    return tuple((x / 12.92) if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


def toy_mat(naam, hexkleur):
    """Materiaal met de kleur in zowel de weergave (Solid) als de nodes (Material Preview en renders)."""
    m = bpy.data.materials.new("toy_" + naam)
    m.diffuse_color = srgb(hexkleur)
    m.roughness = 0.45
    try:
        m.use_nodes = True
    except Exception:  # noqa: BLE001
        pass
    b = next((n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None) if m.node_tree else None
    if b is not None:
        b.inputs["Base Color"].default_value = srgb(hexkleur)
        b.inputs["Roughness"].default_value = 0.45
    return m


def _seg_afstand(p, a, b):
    ab = b - a
    t = max(0.0, min(1.0, (p - a).dot(ab) / max(ab.length_squared, 1e-9)))
    return (p - (a + ab * t)).length, t


def laad_mens_kleding(obj_pad, hoogte_mm=220.0, stijl=None, voxel_mm=0.5, dikte=None):
    """MakeHuman base.obj (CC0 1.0) als aangekleed speelgoedfiguur. Alleen invoer voor de knop, zoals een koper zijn
    figuur zelf aankleedt: borst plat en romp glad (zoals e2e/scherm_mens.py), dan per stuk kleding het oppervlak een
    fractie naar buiten (shirt met korte mouwen, broek, riem, schoenen, haar), zodat zomen en randen echt in de vorm
    zitten; ogen, wenkbrauwen en mond als kleur. Daarna Make watertight van de add-on en de kleuren terug, en de rig uit
    e2e/proef_mens.py (Mixamo-namen, linkerknie 120 en linkerelleboog 140 in Limit Rotation). Geeft (rig, figuur, punten)."""
    import bmesh
    stijl = dict(STIJL, **(stijl or {}))
    voxel_mm = float(os.environ.get("CJ_VOXEL", voxel_mm))
    dikte = dict({"shirt": 0.45, "broek": 0.45, "riem": 0.9, "schoen": 0.6, "haar": 2.2}, **(dikte or {}))
    M = _mens_module(hoogte_mm)
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
    body, p = M["laad_mens"](obj_pad)
    me = body.data
    f = hoogte_mm / 220.0
    # borst plat en romp glad (zelfde getallen als scherm_mens.etalagepop en glad_romp, op 220 mm gemeten)
    import math
    for v in me.vertices:
        c = v.co
        if c.y >= -2.5 * f or abs(c.x) < 4.0 * f or abs(c.x) > 36.0 * f:
            continue
        wz = max(0.0, 1.0 - abs(c.z - 159.0 * f) / (13.0 * f))
        wx = min(1.0, (abs(c.x) - 4.0 * f) / (6.0 * f)) * min(1.0, (36.0 * f - abs(c.x)) / (6.0 * f))
        w = math.sin(wz * math.pi / 2.0) ** 2 * wx
        c.y = c.y + (-2.5 * f - c.y) * w
    bm = bmesh.new()
    bm.from_mesh(me)
    romp = [v for v in bm.verts if 92 * f < v.co.z < 170 * f and abs(v.co.x) < 30 * f]
    for _ in range(25):
        bmesh.ops.smooth_vert(bm, verts=romp, factor=0.8, use_axis_x=True, use_axis_y=True, use_axis_z=True)
    bm.to_mesh(me)
    bm.free()
    me.update()
    top = max(v.co.z for v in me.vertices)
    oog = (p["l-eye"] + p["r-eye"]) / 2
    taille = p["pelvis"].z + 0.45 * (p["spine-3"].z - p["pelvis"].z)
    log(f"punten: oog z {oog.z:.1f}, mond {p['mouth'].z:.1f}, nek {p['neck'].z:.1f}, bekken {p['pelvis'].z:.1f}, "
        f"taille {taille:.1f}, top {top:.1f}")
    segs = {"romp": ("pelvis", "neck"), "hoofd": ("neck", "head-2")}
    for k in "lr":
        segs.update({f"{k}-boven": (f"{k}-shoulder", f"{k}-elbow"), f"{k}-onder": (f"{k}-elbow", f"{k}-hand"),
                     f"{k}-hand": (f"{k}-hand", f"{k}-finger-3-4"), f"{k}-dij": (f"{k}-upper-leg", f"{k}-knee"),
                     f"{k}-scheen": (f"{k}-knee", f"{k}-ankle"), f"{k}-voet": (f"{k}-ankle", f"{k}-toe-3-1")})
    hoofd_vs = [v.co for v in me.vertices if v.co.z > p["neck"].z + 4 * f]
    hy0, hy1 = min(c.y for c in hoofd_vs), max(c.y for c in hoofd_vs)

    def rol_van(c, n=None):
        """Welk stuk kleding (of huid, haar) op plek c hoort; met normaal n ook ogen, wenkbrauwen en mond."""
        best, bt = None, (1e9, 0)
        for naam, (a, b) in segs.items():
            d, t = _seg_afstand(c, p[a], p[b])
            if d < bt[0]:
                best, bt = naam, (d, t)
        t = bt[1]
        if best == "hoofd" or (best == "romp" and c.z > p["neck"].z + 2 * f):
            ty = (c.y - hy0) / max(hy1 - hy0, 1e-6)   # 0 = voorkant gezicht, 1 = achterhoofd
            if c.z > oog.z + 0.42 * (top - oog.z) or (ty > 0.55 and c.z > p["mouth"].z + 1.0 * f) or \
                    (ty > 0.40 and c.z > oog.z + 0.5 * f and abs(c.x) > abs(p["l-eye"].x) + 4.5 * f):
                return "haar"
            if n is not None and n.y < -0.2:
                for e in (p["l-eye"], p["r-eye"]):
                    dx, dz = c.x - e.x, c.z - e.z
                    if (dx / (1.15 * f)) ** 2 + (dz / (1.45 * f)) ** 2 < 1.0:
                        return "pupil"
                    bx = dx + (0.5 * f if e.x > 0 else -0.5 * f)
                    if abs(bx) < 2.3 * f and 2.4 * f + 0.25 * f * (bx / (2.3 * f)) ** 2 * -2 < dz < 3.1 * f:
                        return "haar"   # wenkbrauw
                dm = c - p["mouth"]
                u = dm.x / (2.0 * f)
                if abs(u) < 1.0 and abs(dm.z - 0.5 * f * u * u + 0.3 * f) < 0.3 * f:
                    return "mond"
            return "huid"
        if best == "romp":
            if os.environ.get("CJ_HALS") == "rond":
                # ronde hals (Beeldmaker #101, keuring #113): een smalle boog rond de nek, geen vierkante lap
                u = c.x / (7.0 * f)
                if abs(u) < 1.0 and c.z > p["neck"].z + 1.0 * f - 4.0 * f * math.sqrt(1.0 - u * u):
                    return "huid"
            elif c.z > p["neck"].z - 6.5 * f and abs(c.x) < 9.5 * f:
                return "huid"   # halsopening van het shirt
            if abs(c.z - taille) < 1.6 * f:
                return "riem"
            return "broek" if c.z < taille else "shirt"
        if best.endswith("boven"):
            return "shirt" if t < 0.42 else "huid"
        if best.endswith(("onder", "hand")):
            return "huid"
        if best.endswith("dij"):
            if abs(c.z - taille) < 1.6 * f:
                return "riem"
            return "shirt" if c.z > taille else "broek"
        if best.endswith("scheen"):
            return "schoen" if t > 0.86 else "broek"
        return "schoen"

    rol = [rol_van(v.co) for v in me.vertices]
    buren = [[] for _ in me.vertices]
    for e in me.edges:
        a, b = e.vertices
        buren[a].append(b)
        buren[b].append(a)
    # schoenen glad (geen tenen), borst nog wat gladder onder het shirt
    for ronde in range(15):
        nieuw_co = {}
        for i, v in enumerate(me.vertices):
            if rol[i] == "shirt" and ronde < 10 and 145 * f < v.co.z < 170 * f and abs(v.co.x) < 15 * f:
                if buren[i]:
                    nieuw_co[i] = v.co * 0.2 + sum((me.vertices[j].co for j in buren[i]), Vector()) * (0.8 / len(buren[i]))
        for i, c in nieuw_co.items():
            me.vertices[i].co = c
    me.update()
    # naar buiten per stuk kleding (zomen en randen in de vorm), haar met een zachte rand. Niet waar huid tegen huid
    # zit (binnenkant dij, oksel): daar moet de spleet blijven, anders kan de kogel van heup of schouder niet bewegen.
    off = []
    for i, v in enumerate(me.vertices):
        d = dikte.get(rol[i], 0.0) * f
        nx = v.normal.x * (1 if v.co.x > 0 else -1)
        if rol[i] == "broek" and nx < -0.25 and v.co.z < taille - 4 * f:
            d = 0.0
        if rol[i] == "shirt" and abs(v.co.x) > 13 * f:
            d = 0.0   # mouwen en schouders alleen kleur: daar komt de kogel van de schouder
        off.append(d)
    for _ in range(2):
        off = [sum(off[j] for j in buren[i]) / len(buren[i]) if buren[i] and (rol[i] == "haar" or off[i] == 0.0) else off[i]
               for i in range(len(off))]
    for v, d in zip(me.vertices, off):
        v.co = v.co + v.normal * d
        if v.co.z < 0.0:
            v.co.z = 0.0   # platte zool op de grond
    me.update()
    # kleuren: eerst grof per vlak, na de remesh nog eens fijn per nieuw vlak (strakke zomen, ronde ogen)
    volgorde = list(stijl) + ["mond"]
    stijl = dict(stijl, mond=stijl.get("mond", "B5384B"))
    me.materials.clear()
    for k in volgorde:
        me.materials.append(toy_mat(k, stijl[k]))
    import collections
    for poly in me.polygons:
        poly.material_index = volgorde.index(collections.Counter(rol[i] for i in poly.vertices).most_common(1)[0][0])
        poly.use_smooth = True
    me.update()
    # schoenen: per voet de bolle schil (convex hull) van de voet onder de enkel, iets ruimer, samen met het lichaam
    # in de remesh. Zo verdwijnen de tenen in een gladde schoen met een platte zool.
    schoen_i = volgorde.index("schoen")
    bm = bmesh.new()
    bm.from_mesh(me)
    for k in "lr":
        enk = p[f"{k}-ankle"]
        vs = [v.co.copy() for v in me.vertices if v.co.z < enk.z + 1.0 * f and (v.co.x > 0) == (enk.x > 0)
              and (v.co - Vector((enk.x, enk.y, v.co.z))).length < 40 * f]
        if len(vs) < 8:
            continue
        nieuw_v = [bm.verts.new(c) for c in vs]
        res = bmesh.ops.convex_hull(bm, input=nieuw_v)
        weg = list({g for g in res["geom_interior"] + res["geom_unused"] if isinstance(g, bmesh.types.BMVert)})
        bmesh.ops.delete(bm, geom=weg, context="VERTS")
        schil_v = [g for g in res["geom"] if isinstance(g, bmesh.types.BMVert) and g.is_valid]
        midden = sum((v.co for v in schil_v), Vector()) / max(1, len(schil_v))
        for v in schil_v:
            d = v.co - midden
            v.co = midden + Vector((d.x * 1.08, d.y * 1.04, d.z * 1.06))
            v.co.z = max(v.co.z, 0.0)
        for g in res["geom"]:
            if isinstance(g, bmesh.types.BMFace) and g.is_valid:
                g.material_index = schoen_i
        log(f"schoen {k}: schil van {len(schil_v)} punten")
    bm.to_mesh(me)
    bm.free()
    me.update()
    fig = body
    fig.name = fig.data.name = "Figuur"
    bron_me = fig.data.copy()
    bron_mw = fig.matrix_world.copy()
    bpy.context.scene.click_joints.voxel_mm = voxel_mm
    actief(fig)
    bpy.ops.click_joints.maak_gesloten()
    nieuw = bpy.context.view_layer.objects.active
    if nieuw is not fig:
        bpy.data.objects.remove(fig)
        fig = nieuw
    kleur_terug(bron_me, bron_mw, fig)
    bpy.data.meshes.remove(bron_me)
    mw = fig.matrix_world
    for poly in fig.data.polygons:
        poly.material_index = volgorde.index(rol_van(mw @ poly.center, poly.normal))
    fig.data.update()
    log(f"na watertight: {len(fig.data.vertices)} punten, {mesh_staat(fig)}")
    arm = M["maak_rig"](p)
    arm.data.display_type = "STICK"
    fig.modifiers.new("Armature", "ARMATURE").object = arm
    return arm, fig, p


def voorproef(pad, samples=16):
    """Snel plaatje van alles wat zichtbaar is (Cycles op de CPU, drie zonnen, camera schuin voor), alleen om te kijken."""
    import math
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.samples = samples
    sc.cycles.use_denoising = False
    sc.render.resolution_x, sc.render.resolution_y = 540, 960
    obs = [o for o in sc.objects if o.type == "MESH" and o.visible_get()]
    lo, hi = kader(obs)
    mid = (lo + hi) / 2
    h = hi.z - lo.z
    cd = bpy.data.cameras.new("vp")
    cd.lens = 60
    cd.sensor_fit = "VERTICAL"
    cam = bpy.data.objects.new("vp", cd)
    sc.collection.objects.link(cam)
    sc.camera = cam
    d = h * 1.15 / (2 * math.tan(math.atan(12 / 60)))
    r = Vector((math.sin(math.radians(-25)), -math.cos(math.radians(-25)), 0.12)).normalized()
    cam.location = mid + r * d
    cam.rotation_euler = (-r).to_track_quat("-Z", "Y").to_euler()
    cd.clip_end = d * 4
    for i, (rx, rz, e) in enumerate(((50, -35, 3.0), (60, 60, 1.2), (70, 170, 2.0))):
        ld = bpy.data.lights.new(f"vp{i}", "SUN")
        ld.energy = e
        lo_ = bpy.data.objects.new(f"vp{i}", ld)
        sc.collection.objects.link(lo_)
        lo_.rotation_euler = (math.radians(rx), 0, math.radians(rz))
    if sc.world is None:
        sc.world = bpy.data.worlds.new("w")
    sc.world.color = (0.6, 0.65, 0.75)
    for o in obs:
        for m in o.data.materials:
            if m is not None:
                m.use_nodes = True
                b = next((n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
                if b:
                    b.inputs["Base Color"].default_value = m.diffuse_color
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cam)


# ---------- keuze per figuur (studio-2) ----------
HIER = os.path.dirname(os.path.abspath(__file__))
MENS_OBJ = os.path.join(HIER, "modellen", "makehuman-base.obj")


def laad_figuur(keuze="robot", hoogte_mm=220.0, stijl=None, weg=(), armen=0.0):
    """Eén ingang voor elk figuur. keuze: "robot" (figuur_robot.py, standaard), "tekenpop" (figuur_tekenpop.py), "mens" (MakeHuman met kleding) of
    een pad naar een .glb/.blend met eigen rig. Geeft (rig, figuur, punten); punten is None bij een eigen glb."""
    if keuze == "robot":
        import figuur_robot as R
        return R.laad_robot(hoogte_mm, stijl=stijl)
    if keuze == "tekenpop":   # houten tekenpop (figuur_tekenpop.py, 23 nov ±22:35), één materiaal: hout
        import figuur_tekenpop as T
        return T.laad_tekenpop(hoogte_mm)
    if keuze == "mens" or keuze.endswith(".obj"):
        return laad_mens_kleding(MENS_OBJ if keuze == "mens" else keuze, hoogte_mm, stijl=stijl)
    arm, body = laad(keuze, hoogte_mm, weg, armen=armen)
    return arm, body, None
