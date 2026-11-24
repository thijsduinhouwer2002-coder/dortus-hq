"""Heldenbeelden voor Click Joints Pro (tekenpop-agent, 24 nov 2026, opdracht hoofdchat 16:45 NL: "spectaculairder,
een mooi stuk techniek"). Zelfde studio, licht en materialen als cover-pop-dynamisch (release tekenpop-1).

    blender -b --factory-startup --python helden.py -- <pro-zip> <uitmap> b <shot> [samples] [schaal%]
shot:
  knie     macro van het linkerkniescharnier, half weggesneden (vlak loodrecht op de scharnieras door het midden):
           je ziet de knokkel in zijn gleuf, de wig van de eindstop en de speling. Groen gloeit alleen waar lucht is
           rond de knokkel (een dun vlak net achter de snede, alleen zichtbaar door de spleten). Ondiepe scherptediepte.
  spiraal  alle 10 delen in een spiraal uit elkaar, met bewegingsonscherpte, en een dunne gradenboog bij elleboog en
           knie over het bereik dat de add-on meldt (0 tot 115).
  voor     het figuur vóór de knop: grijs model met oranje botten zoals in Blender
  na       zelfde camera: het figuur na de knop, hout en messing, in dezelfde houding
  strip    de echte knop "Fit test: ball" van Pro: vijf staafjes met elk een kogel bij 0.10 tot 0.30 mm speling en het
           getal van de add-on in reliëf, bovenste helft iets opgetild zodat je de kogel ziet.
Elk figuurshot draait de echte knop Figure from rig van Click Joints Pro (stops 115 in de rig, CJ_STOP) en schrijft in
b-<shot>.json wat de add-on meldde.
"""
import importlib
import json
import math
import os
import random
import sys

import bpy
from mathutils import Matrix, Quaternion, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.abspath(os.path.join(HIER, "..", "..", "..", "commercie", "filmpjes", "studio"))
os.environ.setdefault("CJ_STOP", "115")
_pad = os.path.join(STUDIO, "tekenpop_beelden.py")
TB = {"__name__": "tekenpop_beelden", "__file__": _pad}
_bron = open(_pad, encoding="utf-8").read()
assert "\nmain()\n" in _bron
exec(compile(_bron.replace("\nmain()\n", "\n"), _pad, "exec"), TB)   # noqa: S102 (eigen code uit de repo)
M, T, FL = TB["M"], TB["T"], TB["FL"]
S = M["S"]
SHOT, UIT, STIJL, H = M["SHOT"], M["UIT"], M["STIJL"], M["H"]
meting = M["meting"]
meting["figuur"] = "tekenpop" if SHOT != "strip" else "fit test strip"
GROEN = "4DFF9A"


def log(*a):
    print("[helden]", *a, flush=True)


def zip_aan():
    if "figuur_uit_rig" not in dir(bpy.ops.click_joints):
        bpy.ops.extensions.package_install_files(filepath=M["ZIP"], repo="user_default", enable_on_install=True)


def figuur_klaar():
    """Figuur, Figure from rig (of uit TP_LAAD), materialen. Geeft (naam, delen)."""
    laad = os.environ.get("TP_LAAD", "")
    if laad and os.path.exists(laad):
        zip_aan()
        bpy.ops.wm.open_mainfile(filepath=laad)
        naam = next(o.get("cj_figuur") for o in bpy.context.scene.objects if o.get("cj_figuur"))
        meting.update(json.loads(bpy.context.scene.get("tp_meting", "{}")))
    else:
        arm, ob = TB["figuur"]()
        naam, _d = M["maak_gewrichten"](arm, ob)
        if os.environ.get("TP_BEWAAR"):
            bpy.context.scene["tp_meting"] = json.dumps(meting)
            bpy.ops.wm.save_as_mainfile(filepath=os.environ["TP_BEWAAR"])
    meting["aantal_gewrichten"] = len(meting.get("gewrichten", []))
    delen = M["zichtbaar"](naam)
    T.materialen(delen)
    inst = bpy.context.scene.click_joints
    try:
        bpy.context.window_manager.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    inst.uit_elkaar = False
    M["U"]().zet_alle(bpy.context.scene)
    return naam, M["zichtbaar"](naam)


def deel_b(naam):
    return next((o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_naam") == naam
                 and o.get("cj_deel") == "B" and o.visible_get()), None)


def eigen(o, k):
    v = o.get(k)
    return Vector(v) if v is not None else None


def mat_emissie(naam, hexkleur, kracht):
    m = bpy.data.materials.get(naam) or bpy.data.materials.new(naam)
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = S.srgb(hexkleur)
    e.inputs["Strength"].default_value = kracht
    nt.links.new(e.outputs[0], o.inputs[0])
    m.diffuse_color = S.srgb(hexkleur)
    return m


def kops():
    """Doorsnede van het hout: dezelfde houtkleur, iets donkerder en matter (kopshout)."""
    m = T.hout().copy()
    m.name = "tp_kops"
    nt = m.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    for naam, w in (("Roughness", 0.7), ("Coat Weight", 0.0)):
        if naam in b.inputs:
            b.inputs[naam].default_value = w
    # vers gezaagd: lichter en vlakker dan de gelakte buitenkant, de nerf maar half zo sterk
    ramp = next(n for n in nt.nodes if n.type == "VALTORGB")
    els = ramp.color_ramp.elements
    els[0].color = S.srgb("F2D3A6")
    els[-1].color = S.srgb("D9AE7A")
    for e in els[1:-1]:
        e.color = S.srgb("E8C291")
    return m


def snij_weg(o, punt, normaal, cap_mat, maat=400.0, tweede=None):
    """Haalt alles aan de kant van `normaal` van het vlak door `punt` weg (Boolean Exact). Met `tweede` (een normaal
    loodrecht op de eerste) alleen het kwart dat aan beide kanten ligt: een opengewerkt kwart, zoals een technische
    tekening. Nieuwe vlakken krijgen cap_mat."""
    bpy.ops.mesh.primitive_cube_add(size=1.0)
    doos = bpy.context.active_object
    doos.name = "snij_doos"
    n = normaal.normalized()
    if tweede is None:
        doos.matrix_world = (Matrix.Translation(punt + n * maat / 2) @ n.to_track_quat("Z", "Y").to_matrix().to_4x4()
                             @ Matrix.Diagonal((maat, maat, maat, 1)))
    else:
        t = (tweede - n * tweede.dot(n)).normalized()
        z = n.cross(t)
        rot = Matrix((n, t, z)).transposed().to_4x4()
        doos.matrix_world = (Matrix.Translation(punt + (n + t) * maat / 2) @ rot
                             @ Matrix.Diagonal((maat, maat, maat, 1)))
    doos.data.materials.append(cap_mat)
    if cap_mat.name not in [m.name for m in o.data.materials if m]:
        o.data.materials.append(cap_mat)
    md = o.modifiers.new("snede", "BOOLEAN")
    md.operation, md.object, md.solver = "DIFFERENCE", doos, "EXACT"
    try:
        md.material_mode = "TRANSFER"
    except Exception:  # noqa: BLE001
        pass
    FL.actief(o)
    bpy.ops.object.modifier_apply(modifier="snede")
    bpy.data.objects.remove(doos)


def gloed_schijf(punt, normaal, r, diep, mat):
    """Dunne schijf in het snijvlak, `diep` mm achter de snede: zichtbaar alleen door de spleten van het gewricht."""
    bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=r, depth=0.01)
    s = bpy.context.active_object
    s.name = "speling_gloed"
    n = normaal.normalized()
    s.matrix_world = Matrix.Translation(punt - n * diep) @ n.to_track_quat("Z", "Y").to_matrix().to_4x4()
    s.data.materials.append(mat)
    s.visible_shadow = False
    return s


def speling_lijnen(delen, mat, cap_naam="tp_kops", dicht=0.45, dik=0.05):
    """Dunne groene gloeiende lijnen precies waar de speling zit: de randen van het snijvlak van elk deel die binnen
    `dicht` mm van het andere deel liggen (de spleet tussen knokkel en gleuf, tussen tong en wang). De wig van de
    eindstop is breder en gloeit dus niet. Alleen voor het beeld."""
    import bmesh
    from mathutils.bvhtree import BVHTree
    dg = bpy.context.evaluated_depsgraph_get()
    bvh = {}
    for o in delen:
        bm = bmesh.new()
        bm.from_object(o, dg)
        bm.transform(o.matrix_world)
        bvh[o.name] = BVHTree.FromBMesh(bm)
        bm.free()
    punten, randen = [], []
    for o in delen:
        idx = next((i for i, m in enumerate(o.data.materials) if m and m.name == cap_naam), None)
        if idx is None:
            continue
        ander = [bvh[x.name] for x in delen if x is not o]
        me, mw = o.data, o.matrix_world
        rand_vlakken = {}
        for pl in me.polygons:
            for ek in pl.edge_keys:
                rand_vlakken.setdefault(ek, []).append(pl.material_index == idx)
        for (i, j), soorten in rand_vlakken.items():
            if len(soorten) != 2 or soorten[0] == soorten[1]:
                continue
            a, b = mw @ me.vertices[i].co, mw @ me.vertices[j].co
            mid = (a + b) / 2
            if any((t.find_nearest(mid)[3] or 1e9) <= dicht for t in ander):
                k = len(punten)
                punten += [a, b]
                randen.append((k, k + 1))
    if not randen:
        log("speling_lijnen: geen randen gevonden")
        return None
    me = bpy.data.meshes.new("speling_lijnen")
    me.from_pydata([tuple(p) for p in punten], randen, [])
    ob = bpy.data.objects.new("speling_lijnen", me)
    bpy.context.scene.collection.objects.link(ob)
    FL.actief(ob)
    bpy.ops.object.convert(target="CURVE")
    ob = bpy.context.active_object
    ob.data.bevel_depth = dik
    ob.data.bevel_resolution = 2
    ob.data.materials.append(mat)
    ob.visible_shadow = False
    log("speling_lijnen:", len(randen), "randen")
    return ob


def lamp(naam, plek, doel, maat_, kracht, kleur, vorm="DISK"):
    ld = bpy.data.lights.new(naam, "AREA")
    ld.shape, ld.size, ld.energy = vorm, maat_, kracht
    ld.color = S.srgb(kleur)[:3]
    ob = bpy.data.objects.new(naam, ld)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = Vector(plek)
    ob.rotation_euler = (Vector(doel) - ob.location).to_track_quat("-Z", "Y").to_euler()
    return ob


def scherpte(cam, punt, f):
    """f als op een echte camera; de scene is in mm (schaal 0,001) en Blender rekent het diafragma in meters,
    dus delen door 1000 voor dezelfde scherptediepte."""
    cam.data.dof.use_dof = f > 0
    cam.data.dof.focus_distance = (cam.location - punt).length
    cam.data.dof.aperture_fstop = f * bpy.context.scene.unit_settings.scale_length


# ------------------------------------------------------------------ shot knie
def shot_knie():
    naam, objs = figuur_klaar()
    meting["pose"] = {"Left knee": M["buig"]("Left knee", float(os.environ.get("KNIE_BUIG", "35")))}
    M["pose_en_uiteen"](objs, 0.0)
    b = deel_b("Left knee")
    hp = eigen(b, "cj_scharnier_punt")
    ax = eigen(b, "cj_scharnier_as").normalized()
    if hp.x * ax.x < 0:   # snijvlak met de normaal naar buiten (linkerbeen: +x), daar staat de camera
        ax = -ax
    # dij: het zichtbare deel dat het dichtst bij het scharnierpunt ligt, naast deel B
    dg = bpy.context.evaluated_depsgraph_get()

    def afstand(o):
        m = o.matrix_world
        ok, loc, _n, _i = o.evaluated_get(dg).closest_point_on_mesh(m.inverted() @ hp)
        return (m @ loc - hp).length if ok else 1e9
    dij = min((o for o in objs if o is not b), key=afstand)
    log("knie: deel B", b.name, "dij", dij.name, "punt", tuple(round(c, 2) for c in hp))
    for o in objs:
        if o not in (b, dij):
            o.hide_render = True
            o.hide_set(True)
    cap = kops()
    voor = -eigen(b, "cj_buigkant").normalized()   # knie buigt naar achteren: de voorkant gaat open
    for o in (b, dij):
        snij_weg(o, hp, ax, cap, tweede=voor)
    groen = mat_emissie("speling_groen", GROEN, float(os.environ.get("KNIE_GLOED", "12")))
    r = 0.0
    speling_lijnen([b, dij], groen)
    meting["snede"] = {"punt": [round(c, 3) for c in hp], "normaal": [round(c, 4) for c in ax],
                       "gloed_straal_mm": round(r, 2), "speling_mm": float(b.get("cj_speling_mm", 0))}
    zichtbaar = [b, dij]
    M["studio"](M["laagste"](zichtbaar) - 30)
    M["render_instellingen"](2400, 1200)
    sc = bpy.context.scene
    sc.cycles.max_bounces = 8
    # camera van buiten (kant van de snede), iets van voren en boven, lange lens
    kijk = (ax * 1.0 + voor * float(os.environ.get("KNIE_VOOR", "0.18")) + Vector((0, 0, 0.3))).normalized()
    cd = bpy.data.cameras.new("cam")
    cd.lens, cd.clip_start, cd.clip_end, cd.sensor_fit = 105, 1, 100000, "HORIZONTAL"
    cam = bpy.data.objects.new("cam", cd)
    sc.collection.objects.link(cam)
    afst = float(os.environ.get("KNIE_AFSTAND", "180"))
    doel = hp + Vector((0, 0, -2.0)) - (ax.cross(Vector((0, 0, 1)))).normalized() * float(os.environ.get("KNIE_X", "-9"))
    cam.location = doel + kijk * afst
    rol = Quaternion((doel - cam.location).normalized(), math.radians(float(os.environ.get("KNIE_ROL", "20"))))
    cam.rotation_euler = (rol @ (doel - cam.location).to_track_quat("-Z", "Y")).to_euler()
    sc.camera = cam
    scherpte(cam, hp, float(os.environ.get("KNIE_F", "7")))
    # randlicht van achter, warm sleutellicht, koel tegenlicht
    for o in list(sc.objects):   # eigen licht voor de macro: het studiolicht is voor een heel figuur
        if o.type == "LIGHT":
            bpy.data.objects.remove(o)
    zij = kijk.cross(Vector((0, 0, 1))).normalized()
    lamp("macro_sleutel", hp + kijk * 110 + zij * 70 + Vector((0, 0, 90)), hp, 50, 2.8e5, "FFD7A8")
    lamp("macro_vul", hp + kijk * 120 - zij * 110 + Vector((0, 0, -10)), hp, 90, 2.0e4, "FFD9B0")
    lamp("macro_rand", hp - kijk * 110 + zij * 40 + Vector((0, 0, 60)), hp, 30, 2.5e5, "FFD25C")
    lamp("macro_rand2", hp - kijk * 100 - zij * 60 + Vector((0, 0, 20)), hp, 30, 1.5e5, "FFFFFF")
    # zachte pruimen gloed op de wand achter het scharnier, zodat het niet in zwart zweeft
    ld = bpy.data.lights.new("macro_gloed", "POINT")
    ld.energy, ld.shadow_soft_size = float(os.environ.get("KNIE_GLOED_WAND", "6e5")), 40
    ld.color = S.srgb("8A5BC2")[:3]
    og = bpy.data.objects.new("macro_gloed", ld)
    sc.collection.objects.link(og)
    og.location = hp - kijk * 160 + Vector((0, 0, 20))
    if sc.world:
        bg = next((n for n in sc.world.node_tree.nodes if n.type == "BACKGROUND"), None)
        if bg is not None:
            bg.inputs[1].default_value = 0.02
    meting["camera"] = {"lens": 105, "fstop": cam.data.dof.aperture_fstop, "afstand": afst}
    M["render"]("knie")


# ------------------------------------------------------------------ gedeeld voor spiraal, voor en na
def deel_a(naam, objs):
    """Het zichtbare deel aan de andere kant van gewricht `naam` (het dichtst bij het gewrichtspunt, niet deel B)."""
    b = deel_b(naam)
    p = eigen(b, "cj_scharnier_punt") or eigen(b, "cj_centrum") or eigen(b, "cj_snijpunt")
    dg = bpy.context.evaluated_depsgraph_get()

    def afstand(o):
        m = o.matrix_world
        ok, loc, _n, _i = o.evaluated_get(dg).closest_point_on_mesh(m.inverted() @ p)
        return (m @ loc - p).length if ok else 1e9
    return min((o for o in objs if o is not b), key=afstand)


def tekst_obj(tekst, plek, maat, mat, cam=None):
    cu = bpy.data.curves.new("t_" + tekst, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = tekst, maat, "CENTER", "CENTER"
    cu.extrude = maat * 0.04
    ob = bpy.data.objects.new("t_" + tekst, cu)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = plek
    cu.materials.append(mat)
    ob.visible_shadow = False
    return ob


def gradenboog(naam, objs, straal, mat, mat_tekst, dik=0.32):
    """Dunne boog om de scharnieras van `naam`, van gestrekt (0) tot de eindstop die de add-on meldt
    (cj_bereik_graden), in het vlak waarin het lid buigt. Hangt aan deel A, zodat hij blijft staan als deel B buigt.
    Met kleine streepjes aan beide einden en het getal bij de stop."""
    b = deel_b(naam)
    a = deel_a(naam, objs)
    hp = eigen(b, "cj_scharnier_punt")
    lid = eigen(b, "cj_as").normalized()
    buig = eigen(b, "cj_buigkant").normalized()
    buig = (buig - lid * buig.dot(lid)).normalized()
    stop = float(b.get("cj_bereik_graden", 0) or 0)
    n = 96
    pts = [hp + (lid * math.cos(math.radians(stop * i / n)) + buig * math.sin(math.radians(stop * i / n))) * straal
           for i in range(n + 1)]
    cu = bpy.data.curves.new("boog_" + naam, "CURVE")
    cu.dimensions = "3D"
    sp = cu.splines.new("POLY")
    sp.points.add(len(pts) - 1)
    for p_, q in zip(sp.points, pts):
        p_.co = (q.x, q.y, q.z, 1.0)
    cu.bevel_depth, cu.bevel_resolution = dik, 3
    ob = bpy.data.objects.new("boog_" + naam, cu)
    bpy.context.scene.collection.objects.link(ob)
    cu.materials.append(mat)
    ob.visible_shadow = False
    delen = [ob]
    for t in (0.0, stop):   # streepjes
        r = lid * math.cos(math.radians(t)) + buig * math.sin(math.radians(t))
        c2 = bpy.data.curves.new("streep", "CURVE")
        c2.dimensions = "3D"
        s2 = c2.splines.new("POLY")
        s2.points.add(1)
        q0, q1 = hp + r * (straal - 1.8), hp + r * (straal + 1.8)
        s2.points[0].co, s2.points[1].co = (*q0, 1.0), (*q1, 1.0)
        c2.bevel_depth = dik
        o2 = bpy.data.objects.new("streep", c2)
        bpy.context.scene.collection.objects.link(o2)
        c2.materials.append(mat)
        o2.visible_shadow = False
        delen.append(o2)
    r = lid * math.cos(math.radians(stop)) + buig * math.sin(math.radians(stop))
    delen.append(tekst_obj(f"{round(stop):d}°", hp + r * (straal + 6.0), 4.2, mat_tekst))
    delen.append(tekst_obj("0°", hp + lid * (straal + 5.0), 4.2, mat_tekst))
    bpy.context.view_layer.update()
    for o in delen:
        o.parent = a
        o.matrix_parent_inverse = a.matrix_world.inverted()
    meting.setdefault("bogen", {})[naam] = {"graden": round(stop, 1), "straal_mm": straal, "aan": a.name}
    return delen


def naar_camera(delen, cam):
    for o in delen:
        if o.type == "FONT":
            c = o.constraints.new("TRACK_TO")
            c.target, c.track_axis, c.up_axis = cam, "TRACK_Z", "UP_Y"


# ------------------------------------------------------------------ shot spiraal
def shot_spiraal():
    naam, objs = figuur_klaar()
    goud_licht = mat_emissie("boog_goud", "FFD25C", 5.0)
    bogen = []
    for n_, r_ in (("Left elbow", 17.0), ("Right elbow", 17.0), ("Left knee", 24.0), ("Right knee", 24.0)):
        if deel_b(n_) is not None:
            bogen += gradenboog(n_, objs, r_, goud_licht, goud_licht)
    meting["pose"] = {n: M["buig"](n, g) for n, g in TB["POSE_SCHARNIER"].items()}
    meting["kogels"] = M["pose_kogels"](objs, TB["POSE_KOGEL"])
    keer = float(os.environ.get("SPIRAAL_KEER", "1.8"))
    M["pose_en_uiteen"](objs, keer)
    eind = {o.name: o.matrix_world.copy() for o in objs}
    romp = max(objs, key=lambda o: o.dimensions.x * o.dimensions.y * o.dimensions.z)

    def midden(o, m=None):
        m = m or o.matrix_world
        vs = [m @ Vector(c) for c in o.bound_box]
        return sum(vs, Vector()) / 8
    c0 = midden(romp)
    draai = float(os.environ.get("SPIRAAL_DRAAI", "0.55"))   # graden per mm hoogte
    rnd = random.Random(11)

    hh = math.radians(float(os.environ.get("SPIRAAL_HOEK", "32")))
    kijkas = Vector((math.sin(hh), -math.cos(hh), 0))
    kantel = (Matrix.Translation(c0) @ Matrix.Rotation(math.radians(float(os.environ.get("SPIRAAL_KANTEL", "0"))), 4,
                                                       kijkas) @ Matrix.Translation(-c0))

    def spiraal(f):
        """f = 1: eindstand. Elk deel draait om de verticale as door de romp, verder naarmate het hoger of lager
        zit, en schuift wat naar buiten: een spiraal. Alleen voor het beeld."""
        for o in objs:
            m = eind[o.name]
            c = midden(o, m)
            d = (c - c0).length
            # draaikolk: elk deel draait om de kijkas door de romp, verder naarmate het verder van de romp zit
            hoek = math.radians(draai * d * f)
            rad = (c - c0)
            uit = rad.normalized() * (6.0 + 0.12 * d) * f if rad.length > 1e-3 else Vector()
            R = Matrix.Translation(c0) @ Matrix.Rotation(hoek, 4, kijkas) @ Matrix.Translation(-c0)
            q = Quaternion(Vector((rnd.uniform(-1, 1), rnd.uniform(-1, 1), 0.3)).normalized(),
                           math.radians(rnd.uniform(4, 12) * f)) if o is not romp else Quaternion()
            cc = R @ c
            o.matrix_world = (kantel @ Matrix.Translation(uit) @ Matrix.Translation(cc) @ q.to_matrix().to_4x4()
                              @ Matrix.Translation(-cc) @ R @ m)
    sc = bpy.context.scene
    # bewegingsonscherpte: frame 1 iets minder gedraaid en minder uit elkaar, frame 2 de eindstand
    for frame, f in ((1, 0.80), (2, 1.0)):
        rnd.seed(11)
        spiraal(f)
        bpy.context.view_layer.update()
        for o in objs:
            o.keyframe_insert("location", frame=frame)
            o.rotation_mode = "QUATERNION"
            o.rotation_quaternion = o.matrix_world.to_quaternion()
            o.keyframe_insert("rotation_quaternion", frame=frame)
            o.keyframe_insert("scale", frame=frame)
    sc.frame_set(2)
    meting["spiraal"] = {"graden_per_mm_van_de_romp": draai, "uit_elkaar_keer": keer,
                         "let_op": "spiraal, draai en bewegingsonscherpte alleen voor het beeld"}
    M["studio"](M["laagste"](objs) - 20)
    M["render_instellingen"](2400, 1200)
    sc.render.use_motion_blur = True
    sc.render.motion_blur_shutter = float(os.environ.get("SPIRAAL_SLUITER", "0.4"))
    cam = M["kader"](objs, float(os.environ.get("SPIRAAL_HOEK", "32")), 10, (0.50, 0.97), 0.42, lens=60, ymid=0.47)
    naar_camera(bogen, cam)
    M["render"]("spiraal")


# ------------------------------------------------------------------ shot voor en na
OSTEO = "FF8A1F"   # oranje van een gekozen bot in Blender


def bot_mesh(a, b, mat, dikte=0.1):
    """Achtvlak-bot zoals Blender ze tekent (kop bij a, staart bij b), plus bolletjes op kop en staart."""
    import bmesh
    L = (b - a).length
    if L < 1e-3:
        return []
    z = (b - a).normalized()
    x = z.orthogonal().normalized()
    y = z.cross(x)
    w = L * dikte
    m = a + z * L * 0.1
    bm = bmesh.new()
    v = [bm.verts.new(a), bm.verts.new(b)] + [bm.verts.new(m + (x * cx + y * cy) * w) for cx, cy in
                                              ((1, 1), (-1, 1), (-1, -1), (1, -1))]
    for i in range(4):
        r0, r1 = v[2 + i], v[2 + (i + 1) % 4]
        bm.faces.new((v[0], r1, r0))
        bm.faces.new((v[1], r0, r1))
    me = bpy.data.meshes.new("bot")
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("bot", me)
    bpy.context.scene.collection.objects.link(ob)
    me.materials.append(mat)
    uit = [ob]
    for q, r in ((a, w * 0.75), (b, w * 0.55)):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=q, segments=16, ring_count=8)
        s = bpy.context.active_object
        s.data.materials.append(mat)
        uit.append(s)
    return uit


def gewrichtpunt(naam):
    b = deel_b(naam)
    if b is None:
        return None, None
    p = eigen(b, "cj_scharnier_punt") or eigen(b, "cj_centrum") or eigen(b, "cj_snijpunt")
    return p, b


def shot_voor_na(soort):
    naam, objs = figuur_klaar()
    meting["pose"] = {n: M["buig"](n, g) for n, g in TB["POSE_SCHARNIER"].items()}
    meting["kogels"] = M["pose_kogels"](objs, TB["POSE_KOGEL"])
    keer = 0.35 if soort == "na" else 0.0
    M["pose_en_uiteen"](objs, keer)
    heel = M["HEEL"]
    sc = bpy.context.scene
    if soort == "voor":
        # vóór de knop: het hele figuur grijs (zoals de Solid-weergave), half doorzichtig zodat de botten zichtbaar
        # zijn, zoals X-ray in Blender. Zelfde houding: elk rustpunt van de rig gaat mee met het deel waar het in zit.
        grijs = bpy.data.materials.new("voor_grijs")
        bsdf = next(n for n in grijs.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        bsdf.inputs["Base Color"].default_value = S.srgb("8F96A3")
        bsdf.inputs["Roughness"].default_value = 0.55
        bsdf.inputs["Alpha"].default_value = float(os.environ.get("VOOR_ALPHA", "0.42"))
        for o in objs:
            o.data.materials.clear()
            o.data.materials.append(grijs)
        bot = mat_emissie("voor_bot", OSTEO, 2.2)
        rp = T.rig_punten(T.punten(H), H / 220.0)

        def via(sleutel, gewricht):
            p = rp[sleutel]
            if gewricht is None:
                return p
            _q, b = gewrichtpunt(gewricht)
            return (heel.get(b.name, Matrix.Identity(4)) @ p) if b is not None else p
        ketens = [(("pelvis", None), ("spine-2", None)), (("spine-2", None), ("spine-1", None)),
                  (("spine-1", None), ("neck", None)), (("neck", None), ("head", "Neck")),
                  (("head", "Neck"), ("head-2", "Neck"))]
        for k, kant in (("l", "Left"), ("r", "Right")):
            ketens += [((f"{k}-clavicle", None), (f"{k}-shoulder", None)),
                       ((f"{k}-shoulder", None), (f"{k}-elbow", f"{kant} shoulder")),
                       ((f"{k}-elbow", f"{kant} shoulder"), (f"{k}-hand", f"{kant} elbow")),
                       ((f"{k}-hand", f"{kant} elbow"), (f"{k}-hand-2", f"{kant} elbow")),
                       ((f"{k}-upper-leg", None), (f"{k}-knee", f"{kant} hip")),
                       ((f"{k}-knee", f"{kant} hip"), (f"{k}-ankle", f"{kant} knee")),
                       ((f"{k}-ankle", f"{kant} knee"), (f"{k}-foot-1", f"{kant} knee"))]
        for (a, ga), (b_, gb) in ketens:
            bot_mesh(via(a, ga), via(b_, gb), bot)
        meting["voor"] = "grijs figuur (alpha %.2f) met oranje botten in dezelfde houding" % \
            bsdf.inputs["Alpha"].default_value
    M["studio"](M["laagste"](objs))
    M["render_instellingen"](2400, 1200)
    # zelfde kader voor voor en na: rond het figuur in rust in deze houding, keer 0
    vak = (0.07, 0.45) if soort == "voor" else (0.55, 0.93)
    M["kader"](objs, float(os.environ.get("VN_HOEK", "40")), 6, vak, 0.44, lens=60, ymid=0.48)
    M["render"](soort)


# ------------------------------------------------------------------ shot strip
def shot_strip():
    zip_aan()
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = False
    r = bpy.ops.click_joints.testkaart(soort=os.environ.get("STRIP_SOORT", "KOGEL"))
    delen = [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_deel")]
    meting["uitslag"] = str(r)
    meting["delen"] = len(delen)
    meting["getallen"] = sorted(str(o.get("cj_kaart_getal")) for o in delen if o.get("cj_kaart_getal"))
    log("Fit test", r, len(delen), "delen, getallen", meting["getallen"])
    # materialen: hout, en messing voor wat de add-on aan het gewricht kleurt en voor het getal
    h, g = T.hout(), T.goud()
    for o in delen:
        me = o.data
        oud = list(me.materials)
        idx = [pl.material_index for pl in me.polygons]
        cj = {i for i, m in enumerate(oud) if m is not None and (m.name.startswith("Click Joints") or
                                                                 m.name.startswith("pla_grijs"))}
        zs = [v.co.z for v in me.vertices]
        top = None
        if o.get("cj_kaart_getal"):
            # het getal staat 0,6 mm op de bovenkant: alles hoger dan de bovenkant van de staaf
            from collections import Counter
            hoog = Counter(round(z, 2) for z in zs)
            top = max(z for z, n in hoog.items() if n > 40 and z < max(zs) - 0.3)
        me.materials.clear()
        me.materials.append(h)
        me.materials.append(g)
        for pl in me.polygons:
            gew = idx[pl.index] in cj
            if top is not None and pl.center.z > top + 0.05:
                gew = True
            pl.material_index = 1 if gew else 0
            pl.use_smooth = pl.area < 2.0
        me.update()
    # bovenste helft iets opgetild en een fractie gedraaid, zodat je de kogel in de kom ziet (alleen voor het beeld)
    til = float(os.environ.get("STRIP_TIL", "11"))
    rnd = random.Random(3)
    for o in delen:
        if o.get("cj_kaart_getal"):
            c = sum((o.matrix_world @ Vector(b) for b in o.bound_box), Vector()) / 8
            q = Matrix.Rotation(math.radians(rnd.uniform(-7, 7)), 4, "Z")
            o.matrix_world = Matrix.Translation((0, 0, til)) @ Matrix.Translation(c) @ q @ Matrix.Translation(-c) \
                @ o.matrix_world
    bpy.context.view_layer.update()
    meting["opgetild_mm"] = til
    lo = M["laagste"](delen)
    # het getal van elk staafje nog eens groot en plat op de vloer ervoor, in messing (het reliëf van de add-on is
    # 3,6 mm en op een productfoto te klein om te lezen)
    fpad = os.environ.get("STRIP_FONT", "")
    fnt = bpy.data.fonts.load(fpad) if fpad and os.path.exists(fpad) else None
    vloer = []
    for o in delen:
        g_ = o.get("cj_kaart_getal")
        if not g_:
            continue
        c = sum((o.matrix_world @ Vector(b_) for b_ in o.bound_box), Vector()) / 8
        cu = bpy.data.curves.new("vloer_" + g_, "FONT")
        cu.body, cu.size, cu.align_x, cu.align_y = g_, float(os.environ.get("STRIP_LETTER", "7.5")), "CENTER", "CENTER"
        cu.extrude = 0.25
        if fnt is not None:
            cu.font = fnt
        t = bpy.data.objects.new("vloer_" + g_, cu)
        bpy.context.scene.collection.objects.link(t)
        t.location = (c.x, c.y - float(os.environ.get("STRIP_VOOR", "19")), lo + 0.25)
        cu.materials.append(g)
        vloer.append(t)
    meting["vloergetallen"] = sorted(t.data.body for t in vloer)
    M["studio"](lo)
    M["render_instellingen"](2400, 1200)
    cam = M["kader"](delen + vloer, float(os.environ.get("STRIP_HOEK", "18")),
                     float(os.environ.get("STRIP_KANTEL", "38")), (0.1, 0.9), 0.40, lens=85, ymid=0.5)
    c = sum((o.matrix_world @ Vector(b) for o in delen for b in o.bound_box), Vector()) / (8 * len(delen))
    scherpte(cam, c, float(os.environ.get("STRIP_F", "8")))
    M["render"]("strip")


# ------------------------------------------------------------------ hoofd
def main():
    {"knie": shot_knie, "spiraal": shot_spiraal, "voor": lambda: shot_voor_na("voor"),
     "na": lambda: shot_voor_na("na"), "strip": shot_strip}[SHOT]()
    json.dump(meting, open(os.path.join(UIT, f"{STIJL}-{SHOT}.json"), "w"), indent=1, ensure_ascii=False)


main()
