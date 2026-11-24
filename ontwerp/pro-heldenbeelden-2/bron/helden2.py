"""Heldenbeelden ronde 2 voor Click Joints Pro (heldenbeelden-maker, 24 nov 2026, opdracht hoofdchat). Twee nieuwe
renders; beeld 3 (voor en na) en 4 (Fit test strip) uit ronde 1 blijven.

Leest ontwerp/pro-heldenbeelden-1/bron/helden.py in zonder zijn main(), dus dezelfde tekenpop, studio, licht,
materialen en de echte knop Figure from rig van Click Joints Pro 1.2.6 (stops 115 in de rig, CJ_STOP).

    blender -b --factory-startup --python helden2.py -- <pro-zip> <uitmap> b <shot> [samples] [schaal%]
shot:
  knie     het linkerbeen van opzij: dij, knie en onderbeen met voet, het onderbeen 60 graden gebogen met de schuif van
           de add-on, het hele been 30 graden gekanteld (een pas). Rond de knie een rond venster weggesneden (straal
           12,5 mm, alleen de helft naar de camera), zodat je de knokkel in zijn gleuf, de wig van de eindstop en de
           speling (groen) ziet. Gouden gradenboog van 0 tot de stop die de add-on meldt (115), streepjes per 15 graden,
           een zachte ring van 0 tot 60 en een gouden schim van het onderbeen bij de stop. Schrijft ook
           b-knie-inzet.png: een scherpe close-up van het venster, voor de inzet (maak2.py).
  spiraal  alle 10 delen in een sprong uit elkaar, van opzij gezien zodat de bogen naar de camera kijken: benen in
           spagaat, armen voor en achter, het geheel 12 graden gekanteld; grote gouden gradenbogen 0 tot 115 bij
           ellebogen en knieën.
Alles wat na de knop gebeurt (venster, boog, schim, ster, kanteling) is alleen voor het beeld; de vorm van de delen en
het bereik komen van de add-on. Elke waarde is met een omgevingsvariabele te veranderen (zie E(...) hieronder).
"""
import json
import math
import os
import random

import bpy
from mathutils import Matrix, Quaternion, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
_pad = os.path.abspath(os.path.join(HIER, "..", "..", "pro-heldenbeelden-1", "bron", "helden.py"))
HD = {"__name__": "helden", "__file__": _pad}
_bron = open(_pad, encoding="utf-8").read()
assert _bron.rstrip().endswith("main()")
exec(compile(_bron.rstrip()[:-len("main()")], _pad, "exec"), HD)   # noqa: S102 (eigen code uit de repo)
M, T, FL, TB = HD["M"], HD["T"], HD["FL"], HD["TB"]
S = M["S"]
SHOT, UIT, STIJL = M["SHOT"], M["UIT"], M["STIJL"]
meting = M["meting"]
meting["ronde"] = 2
E = os.environ.get


def log(*a):
    print("[helden2]", *a, flush=True)


def lettertype():
    p = E("STRIP_FONT", "")
    return bpy.data.fonts.load(p) if p and os.path.exists(p) else None


def buis(naam, pts, dik, mat, dicht=False):
    cu = bpy.data.curves.new(naam, "CURVE")
    cu.dimensions = "3D"
    sp = cu.splines.new("POLY")
    sp.points.add(len(pts) - 1)
    for p_, q in zip(sp.points, pts):
        p_.co = (q.x, q.y, q.z, 1.0)
    sp.use_cyclic_u = dicht
    cu.bevel_depth, cu.bevel_resolution = dik, 3
    cu.use_fill_caps = True
    ob = bpy.data.objects.new(naam, cu)
    bpy.context.scene.collection.objects.link(ob)
    cu.materials.append(mat)
    ob.visible_shadow = False
    return ob


def tekst(body, plek, maat, mat, fnt, rot=None, uitlijn="CENTER"):
    cu = bpy.data.curves.new("t_" + body, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = body, maat, uitlijn, "CENTER"
    cu.extrude = maat * 0.03
    if fnt is not None:
        cu.font = fnt
    ob = bpy.data.objects.new("t_" + body, cu)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = plek
    if rot is not None:
        ob.rotation_euler = rot
    cu.materials.append(mat)
    ob.visible_shadow = False
    return ob


def mat_glas(naam, hexkleur, alpha, emis=0.0):
    """Vage schim: half doorzichtig, een beetje gloed."""
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = S.srgb(hexkleur)
    b.inputs["Alpha"].default_value = alpha
    b.inputs["Roughness"].default_value = 0.5
    if emis:
        b.inputs["Emission Color"].default_value = S.srgb(hexkleur)
        b.inputs["Emission Strength"].default_value = emis
    return m


def mat_schim(mix, kracht):
    """Schim van het onderbeen bij de stop: bijna doorzichtig, zacht gouden gloed (alleen voor het beeld)."""
    m = bpy.data.materials.new("schim")
    m.use_nodes = True
    nt = m.node_tree
    for n_ in list(nt.nodes):
        nt.nodes.remove(n_)
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    t = nt.nodes.new("ShaderNodeBsdfTransparent")
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = S.srgb("FFD25C")
    e.inputs["Strength"].default_value = kracht
    fr = nt.nodes.new("ShaderNodeLayerWeight")      # randen sterker dan het midden: een omtrek
    fr.inputs["Blend"].default_value = 0.35
    mu = nt.nodes.new("ShaderNodeMath")
    mu.operation = "MULTIPLY"
    mu.inputs[1].default_value = mix * 4
    nt.links.new(fr.outputs["Facing"], mu.inputs[0])
    cl = nt.nodes.new("ShaderNodeClamp")
    nt.links.new(mu.outputs[0], cl.inputs[0])
    mx = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(cl.outputs[0], mx.inputs[0])
    nt.links.new(t.outputs[0], mx.inputs[1])
    nt.links.new(e.outputs[0], mx.inputs[2])
    nt.links.new(mx.outputs[0], o.inputs[0])
    return m


def snij_venster(o, punt, n, as_venster, straal, cap_mat):
    """Haalt binnen een cilinder (straal, as `as_venster` door `punt`) alles weg wat aan de kant van `n` van het vlak
    door `punt` ligt: een rond venster in de helft naar de camera. Nieuwe vlakken krijgen cap_mat."""
    diep = 200.0
    bpy.ops.mesh.primitive_cylinder_add(vertices=160, radius=straal, depth=diep)
    c = bpy.context.active_object
    c.name = "venster"
    nn = n.normalized()
    c.matrix_world = Matrix.Translation(punt + nn * diep / 2) @ nn.to_track_quat("Z", "Y").to_matrix().to_4x4()
    c.data.materials.append(cap_mat)
    if cap_mat.name not in [m.name for m in o.data.materials if m]:
        o.data.materials.append(cap_mat)
    md = o.modifiers.new("venster", "BOOLEAN")
    md.operation, md.object, md.solver = "DIFFERENCE", c, "EXACT"
    try:
        md.material_mode = "TRANSFER"
    except Exception:  # noqa: BLE001
        pass
    FL.actief(o)
    bpy.ops.object.modifier_apply(modifier="venster")
    bpy.data.objects.remove(c)


def camera_op(punten, kijk, rol, xb, yb, lens, naam="cam", omhoog=Vector((0, 0, 1))):
    """Camera die vanuit richting `kijk` naar de punten kijkt, gerold over `rol` graden, en ze precies in het vak
    xb x yb (fracties van het beeld) zet."""
    from bpy_extras.object_utils import world_to_camera_view
    sc = bpy.context.scene
    c = sum(punten, Vector()) / len(punten)
    straal = max((p - c).length for p in punten)
    cd = bpy.data.cameras.new(naam)
    cd.lens, cd.clip_start, cd.clip_end, cd.sensor_fit = lens, 1, 100000, "HORIZONTAL"
    cam = bpy.data.objects.new(naam, cd)
    sc.collection.objects.link(cam)
    k = kijk.normalized()
    cam.location = c + k * straal * 5
    q = (-k).to_track_quat("-Z", "Y")
    q = Quaternion(-k, math.radians(rol)) @ q
    cam.rotation_euler = q.to_euler()
    sc.camera = cam
    for _ in range(100):
        bpy.context.view_layer.update()
        pts = [world_to_camera_view(sc, cam, p) for p in punten]
        x0, x1 = min(p.x for p in pts), max(p.x for p in pts)
        y0, y1 = min(p.y for p in pts), max(p.y for p in pts)
        schaal = max((x1 - x0) / (xb[1] - xb[0]), (y1 - y0) / (yb[1] - yb[0]))
        m = cam.matrix_world.to_3x3()
        d = (cam.location - c).length
        mx_ = (x0 + x1) / 2 - (xb[0] + xb[1]) / 2
        my_ = (y0 + y1) / 2 - (yb[0] + yb[1]) / 2
        bw = 2 * d * math.tan(cam.data.angle_x / 2)
        bh = bw * sc.render.resolution_y / sc.render.resolution_x
        cam.location += m @ Vector((mx_ * bw, my_ * bh, 0))
        cam.location += (m @ Vector((0, 0, 1))) * d * (schaal - 1) * 0.7
        if abs(schaal - 1) < 0.005 and abs(mx_) < 0.003 and abs(my_) < 0.003:
            break
    log("camera", naam, "schaal", round(schaal, 3), "x", round(x0, 3), round(x1, 3), "y", round(y0, 3), round(y1, 3))
    return cam


def draai_studio(c, hoek, lichten=True):
    """De studio (gebogen wand en, als lichten=True, de lampen) om een verticale as door c draaien, zodat de wand
    achter het figuur staat gezien vanaf een camera die niet van voren kijkt."""
    D = Matrix.Translation((c.x, c.y, 0)) @ Matrix.Rotation(math.radians(hoek), 4, "Z") @ \
        Matrix.Translation((-c.x, -c.y, 0))
    bpy.context.view_layer.update()
    for o in bpy.context.scene.objects:
        if o.name.startswith("studio_wand") or (lichten and o.type == "LIGHT"):
            o.matrix_world = D @ o.matrix_world
    bpy.context.view_layer.update()


def hoeken(objs, filt=None):
    uit = []
    for o in objs:
        if o.type == "MESH":
            dg = bpy.context.evaluated_depsgraph_get()
            me = o.evaluated_get(dg).data
            mw = o.matrix_world
            for i in range(0, len(me.vertices), 7):
                p = mw @ me.vertices[i].co
                if filt is None or filt(p):
                    uit.append(p)
        else:
            uit += [o.matrix_world @ Vector(c) for c in o.bound_box]
    return uit


# ------------------------------------------------------------------ shot knie
def shot_knie():
    naam, objs = HD["figuur_klaar"]()
    buig_g = float(E("KNIE_BUIG", "60"))
    meting["pose"] = {"Left knee": M["buig"]("Left knee", buig_g)}
    M["pose_en_uiteen"](objs, 0.0)
    b = HD["deel_b"]("Left knee")
    dij = HD["deel_a"]("Left knee", objs)
    hp = HD["eigen"](b, "cj_scharnier_punt")
    ax = HD["eigen"](b, "cj_scharnier_as").normalized()
    if hp.x * ax.x < 0:          # naar buiten (linkerbeen: +x), daar staat de camera
        ax = -ax
    lid = HD["eigen"](b, "cj_as").normalized()
    bk = HD["eigen"](b, "cj_buigkant").normalized()
    bk = (bk - lid * bk.dot(lid)).normalized()
    if lid.z > 0:                # 0 graden = rechtdoor naar beneden (het onderbeen in rust)
        log("let op: lidas wijst omhoog", tuple(lid))
    stop = float(b.get("cj_bereik_graden", 0) or 0)
    teken = 1.0 if ax.cross(lid).dot(bk) > 0 else -1.0
    log("knie: B", b.name, "dij", dij.name, "punt", tuple(round(c, 2) for c in hp), "stop", stop, "teken", teken)
    for o in objs:
        if o not in (b, dij):
            o.hide_render = True
            o.hide_set(True)
    cap = HD["kops"]()
    vr = float(E("KNIE_VENSTER", "12.5"))
    for o in (b, dij):
        snij_venster(o, hp, ax, ax, vr, cap)
    groen = HD["mat_emissie"]("speling_groen", HD["GROEN"], float(E("KNIE_GLOED", "14")))
    HD["speling_lijnen"]([b, dij], groen, dik=float(E("KNIE_LIJN", "0.1")))
    meting["venster"] = {"punt": [round(c, 3) for c in hp], "as": [round(c, 4) for c in ax], "straal_mm": vr,
                         "speling_mm": float(b.get("cj_speling_mm", 0)),
                         "let_op": "venster en groene lijnen alleen voor het beeld"}

    # gradenboog in een vlak voor het been (naar de camera), om de scharnieras
    goud = HD["mat_emissie"]("boog_goud", "FFD25C", float(E("BOOG_GLOED", "6")))
    creme = HD["mat_emissie"]("boog_creme", "FFF4E0", 5.0)
    zacht = mat_glas("boog_vlak", "FFD25C", float(E("VLAK_ALPHA", "0.10")), emis=1.2)
    voor_x = float(E("BOOG_X", "11"))      # mm voor het snijvlak, zodat de boog voor het been zweeft
    R = float(E("BOOG_R", "38"))
    dik = float(E("BOOG_DIK", "0.55"))
    o0 = hp + ax * voor_x

    def richting(g):
        t = math.radians(g)
        return lid * math.cos(t) + bk * math.sin(t)
    extra = []
    n = 160
    extra.append(buis("boog", [o0 + richting(stop * i / n) * R for i in range(n + 1)], dik, goud))
    # streepjes per 15 graden, lang bij 0, 60 en de stop
    for g in list(range(0, int(stop) + 1, 15)) + [stop]:
        lang = 4.5 if g in (0, stop) else 2.4
        extra.append(buis("streep", [o0 + richting(g) * (R - lang * 0.5), o0 + richting(g) * (R + lang)],
                          dik * 0.75, goud))
    # zacht vlak (taartpunt) van 0 tot de huidige stand
    import bmesh
    bm = bmesh.new()
    r_in = float(E("TAART_BINNEN", "0.45")) * R     # ring, zodat het venster in de knie vrij blijft
    rand = [bm.verts.new(o0 + richting(buig_g * i / 60) * (R - 0.6)) for i in range(61)]
    binnen = [bm.verts.new(o0 + richting(buig_g * i / 60) * r_in) for i in range(61)]
    for i in range(60):
        bm.faces.new((binnen[i], rand[i], rand[i + 1], binnen[i + 1]))
    me = bpy.data.meshes.new("taart")
    bm.to_mesh(me)
    bm.free()
    taart = bpy.data.objects.new("taart", me)
    bpy.context.scene.collection.objects.link(taart)
    me.materials.append(zacht)
    taart.visible_shadow = False
    extra.append(taart)
    # eindstop: dikke balk op de boog bij de stop
    extra.append(buis("stopbalk", [o0 + richting(stop) * (R - 5), o0 + richting(stop) * (R + 6)], dik * 2.2, goud))
    # schim van het onderbeen bij de stop
    schim = None
    if E("KNIE_SCHIM", "1") == "1":
        dg = bpy.context.evaluated_depsgraph_get()
        me2 = bpy.data.meshes.new_from_object(b.evaluated_get(dg))
        schim = bpy.data.objects.new("schim", me2)
        bpy.context.scene.collection.objects.link(schim)
        me2.materials.clear()
        me2.materials.append(mat_schim(float(E("SCHIM_MIX", "0.06")), float(E("SCHIM_GLOED", "1.5"))))
        rot = (Matrix.Translation(hp) @ Matrix.Rotation(math.radians(teken * (stop - buig_g)), 4, ax)
               @ Matrix.Translation(-hp))
        schim.matrix_world = rot @ b.matrix_world
        schim.visible_shadow = False

    zwaai = float(E("KNIE_ZWAAI", "-30"))   # het hele been (dij, onderbeen, boog, schim) gekanteld, alleen voor het beeld
    if zwaai:
        Z = Matrix.Translation(hp) @ Matrix.Rotation(math.radians(zwaai), 4, ax) @ Matrix.Translation(-hp)
        for o in [b, dij] + extra + ([schim] if schim else []):
            o.matrix_world = Z @ o.matrix_world
        Z3 = Z.to_3x3()
        lid, bk = (Z3 @ lid).normalized(), (Z3 @ bk).normalized()
        bpy.context.view_layer.update()
    meting["zwaai_graden"] = zwaai
    sc = bpy.context.scene
    M["render_instellingen"](2400, 1200)
    sc.cycles.max_bounces = 8
    # camera: van buiten (kant van het venster), iets van voren en boven
    voor = -bk
    kijk = (ax + voor * float(E("KNIE_VOOR", "0.10")) + Vector((0, 0, float(E("KNIE_OP", "0.12"))))).normalized()
    reik = float(E("KNIE_DIJ", "32"))
    pts = hoeken([b], None) + hoeken([dij], lambda p: (p - hp).length < reik)
    pts += [o0 + richting(g) * (R + 9) for g in range(0, int(stop) + 1, 5)]
    xb = (float(E("KNIE_X0", "0.38")), float(E("KNIE_X1", "0.97")))
    yb = (float(E("KNIE_Y0", "0.06")), float(E("KNIE_Y1", "0.98")))
    cam = camera_op(pts, kijk, float(E("KNIE_ROL", "0")), xb, yb, float(E("KNIE_LENS", "85")))
    fnt = lettertype()
    crot = cam.rotation_euler.copy()
    lm = float(E("LABEL_MAAT", "6.2"))
    labels = [tekst("0°", o0 + richting(0) * (R + 9.5), lm, creme, fnt, crot),
              tekst(f"{round(stop):d}°", o0 + richting(stop) * (R + float(E("LABEL_STOP_AF", "13"))), lm * 1.25, goud, fnt, crot),
              tekst(f"{round(buig_g):d}°", o0 + richting(buig_g * 0.5) * (R * 0.62), lm * 0.9, creme, fnt, crot)]
    extra += labels
    meting["boog"] = {"graden": round(stop, 2), "straal_mm": R, "stand": buig_g,
                      "let_op": "boog, streepjes, taartpunt en schim alleen voor het beeld; 115 is wat de add-on meldt"}
    M["studio"](M["laagste"]([b, dij]) - float(E("KNIE_VLOER", "40")))
    draai_studio(hp, math.degrees(math.atan2(kijk.x, -kijk.y)), lichten=False)
    # eigen licht: warm sleutellicht van voren boven, gouden randlicht van achter, pruim op de wand
    for o in list(sc.objects):
        if o.type == "LIGHT":
            bpy.data.objects.remove(o)
    zij = kijk.cross(Vector((0, 0, 1))).normalized()
    L = HD["lamp"]
    k = float(E("KNIE_LICHT", "1.0"))
    L("sleutel", hp + kijk * 220 + zij * 120 + Vector((0, 0, 170)), hp, 110, 1.1e6 * k, "FFD7A8")
    L("vul", hp + kijk * 240 - zij * 200 + Vector((0, 0, -20)), hp, 160, 1.2e5 * k, "C9B6FF")
    L("rand", hp - kijk * 200 + zij * 80 + Vector((0, 0, 120)), hp, 60, 9e5 * k, "FFD25C")
    L("rand2", hp - kijk * 180 - zij * 120 + Vector((0, 0, 30)), hp, 60, 5e5 * k, "FFFFFF")
    L("venster", hp + kijk * 90 + Vector((0, 0, 40)), hp, 30, 6e4 * k, "FFF0DC")
    ld = bpy.data.lights.new("gloed", "POINT")
    ld.energy, ld.shadow_soft_size = float(E("KNIE_GLOED_WAND", "2.5e6")), 80
    ld.color = S.srgb("8A5BC2")[:3]
    og = bpy.data.objects.new("gloed", ld)
    sc.collection.objects.link(og)
    og.location = hp - kijk * 260 + Vector((0, 0, 30))
    if sc.world:
        bg = next((n_ for n_ in sc.world.node_tree.nodes if n_.type == "BACKGROUND"), None)
        if bg is not None:
            bg.inputs[1].default_value = 0.03
    HD["scherpte"](cam, hp, float(E("KNIE_F", "0")))
    from bpy_extras.object_utils import world_to_camera_view
    bpy.context.view_layer.update()
    sp = world_to_camera_view(sc, cam, hp)
    meting["knie_in_beeld"] = [round(sp.x, 4), round(1 - sp.y, 4)]   # fractie van links en van boven
    meting["camera"] = {"lens": cam.data.lens, "rol": float(E("KNIE_ROL", "0"))}
    M["render"]("knie")

    # inzet: scherpe close-up van het venster, zonder boog en schim
    if E("KNIE_INZET", "1") == "1":
        for o in extra + ([schim] if schim else []):
            o.hide_render = True
        ip = int(E("INZET_PX", "1000"))
        sc.render.resolution_x = sc.render.resolution_y = ip
        kijk2 = (ax + voor * float(E("INZET_VOOR", "0.05")) + Vector((0, 0, float(E("INZET_OP", "0.08"))))).normalized()
        ir = float(E("INZET_R", "10"))
        pts2 = [hp + (Vector((math.cos(t), math.sin(t), 0)) * ir) for t in [i * math.pi / 8 for i in range(16)]]
        # cirkel in het snijvlak
        u = ax.cross(Vector((0, 0, 1))).normalized()
        v = ax.cross(u).normalized()
        pts2 = [hp + (u * math.cos(t) + v * math.sin(t)) * ir for t in [i * math.pi / 12 for i in range(24)]]
        cam2 = camera_op(pts2, kijk2, float(E("INZET_ROL", "0")), (0.04, 0.96), (0.04, 0.96),
                         float(E("INZET_LENS", "100")), naam="cam_inzet")
        HD["scherpte"](cam2, hp, float(E("INZET_F", "0")))
        sc.render.filepath = os.path.join(UIT, f"{STIJL}-knie-inzet.png")
        bpy.ops.render.render(write_still=True)
        log("render", sc.render.filepath)


# ------------------------------------------------------------------ shot spiraal
def shot_spiraal():
    naam, objs = HD["figuur_klaar"]()
    goud = HD["mat_emissie"]("boog_goud", E("BOOG_KLEUR", "FFB938"), float(E("BOOG_GLOED", "2.6")))
    bogen = []
    rb, rk = float(E("BOOG_ARM", "30")), float(E("BOOG_BEEN", "38"))
    dk = float(E("SPIRAAL_BOOG_DIK", "1.6"))
    for n_, r_ in (("Left elbow", rb), ("Right elbow", rb), ("Left knee", rk), ("Right knee", rk)):
        if HD["deel_b"](n_) is not None:
            bogen += boog_groot(n_, objs, r_, goud, dk)
    sprong = {"Left knee": float(E("SP_LKNIE", "10")), "Right knee": float(E("SP_RKNIE", "60")),
              "Left elbow": float(E("SP_LELL", "70")), "Right elbow": float(E("SP_RELL", "45"))}
    meting["pose"] = {n: M["buig"](n, g) for n, g in sprong.items()}
    meting["kogels"] = M["pose_kogels"](objs, TB["POSE_KOGEL"]) if E("SP_KOGELS", "0") == "1" else {}
    keer = float(E("SPIRAAL_KEER", "1.0"))
    M["pose_en_uiteen"](objs, keer)
    bpy.context.view_layer.update()

    def midden(o):
        vs = [o.matrix_world @ Vector(c) for c in o.bound_box]
        return sum(vs, Vector()) / 8
    romp = max(objs, key=lambda o: o.dimensions.x * o.dimensions.y * o.dimensions.z)
    c0 = midden(romp)
    hh = math.radians(float(E("SPIRAAL_HOEK", "80")))
    rechts = Vector((math.cos(hh), math.sin(hh), 0))
    naar_cam = Vector((math.sin(hh), -math.cos(hh), 0))
    op = Vector((0, 0, 1))
    kx, kz = float(E("SPIRAAL_KX", "1.15")), float(E("SPIRAAL_KZ", "1.1"))
    draai = float(E("SPIRAAL_DRAAI", "0.08"))   # graden per mm van de romp, om de kijkas (draaikolk)
    rnd = random.Random(int(E("SPIRAAL_SEED", "5")))
    # ster: armen en benen als geheel om hun schouder of heup naar buiten gedraaid (om de kijkas), zodat de delen een
    # brede X vormen in plaats van een smalle staande figuur. Alleen voor het beeld (verder dan de kogels kunnen).
    pt = T.punten(M["H"])
    stuk = {(o.get("cj_naam"), o.get("cj_deel")): o for o in objs}
    VOOR_ = Vector((0, -1, 0))
    ketens = [("l-shoulder", ["Left shoulder", "Left elbow"], float(E("STER_LARM", "130")), -1.0),
              ("r-shoulder", ["Right shoulder", "Right elbow"], float(E("STER_RARM", "60")), 1.0),
              ("l-upper-leg", ["Left hip", "Left knee"], float(E("STER_LBEEN", "80")), 1.0),
              ("r-upper-leg", ["Right hip", "Right knee"], float(E("STER_RBEEN", "80")), -1.0)]
    for sleutel, namen, hoek, waar in ketens:
        wortel = pt[sleutel]
        delen_k = [stuk[(n_, "B")] for n_ in namen if (n_, "B") in stuk]
        if not delen_k:
            continue
        eind = midden(delen_k[-1])
        # teken zo dat het uiteinde naar voren (waar = 1) of naar achteren (waar = -1) zwaait
        beste = None
        for tk in (1.0, -1.0):
            Rk = Matrix.Rotation(math.radians(tk * hoek), 3, naar_cam)
            nieuw = wortel + Rk @ (eind - wortel)
            score = (nieuw - eind).dot(VOOR_) * waar
            if beste is None or score > beste[0]:
                beste = (score, tk)
        tk = beste[1]
        Rk = Matrix.Translation(wortel) @ Matrix.Rotation(math.radians(tk * hoek), 4, naar_cam) \
            @ Matrix.Translation(-wortel)
        for o in delen_k:
            o.matrix_world = Rk @ o.matrix_world
        meting.setdefault("ster", {})[sleutel] = round(tk * hoek, 1)
    bpy.context.view_layer.update()
    for o in objs:
        c = midden(o)
        d = c - c0
        dr, dz = d.dot(rechts), d.dot(op)
        stap = rechts * dr * (kx - 1) + op * dz * (kz - 1) + naar_cam * rnd.uniform(-3, 9) * (d.length / 80)
        R = Matrix.Translation(c0) @ Matrix.Rotation(math.radians(draai * d.length), 4, naar_cam) \
            @ Matrix.Translation(-c0)
        if o is romp:
            q = Quaternion(Vector((0.3, 1, 0.2)).normalized(), math.radians(-6))
            o.matrix_world = Matrix.Translation(c) @ q.to_matrix().to_4x4() @ Matrix.Translation(-c) @ o.matrix_world
            continue
        as_ = Vector((rnd.uniform(-1, 1), rnd.uniform(-1, 1), rnd.uniform(-0.4, 0.4))).normalized()
        q = Quaternion(as_, math.radians(rnd.uniform(5, 13)))
        cc = R @ (c + stap)
        o.matrix_world = (Matrix.Translation(cc) @ q.to_matrix().to_4x4() @ R.to_3x3().to_4x4()
                          @ Matrix.Translation(-c) @ o.matrix_world)
    bpy.context.view_layer.update()
    kantel = float(E("SPIRAAL_KANTEL", "-12"))   # het hele figuur gekanteld om de kijkas (duikend), alleen voor het beeld
    if kantel:
        K = Matrix.Translation(c0) @ Matrix.Rotation(math.radians(kantel), 4, naar_cam) @ Matrix.Translation(-c0)
        for o in objs:
            o.matrix_world = K @ o.matrix_world
        bpy.context.view_layer.update()
    meting["explosie"] = {"uit_elkaar_keer": keer, "breder_keer": kx, "hoger_keer": kz, "draai_graden_per_mm": draai,
                          "kantel_graden": kantel,
                          "let_op": "explosie en draaiing alleen voor het beeld"}
    sc = bpy.context.scene
    M["studio"](M["laagste"](objs) - float(E("SPIRAAL_VLOER", "40")))
    draai_studio(c0, math.degrees(hh), lichten=E("SPIRAAL_LICHT_MEE", "1") == "1")
    # zachte pruimen gloed op de wand achter het midden, zodat de delen niet in zwart zweven
    gl = float(E("SPIRAAL_GLOED", "0"))
    if gl > 0:
        ld = bpy.data.lights.new("gloed2", "POINT")
        ld.energy, ld.shadow_soft_size = gl, 120
        ld.color = S.srgb("8A5BC2")[:3]
        og = bpy.data.objects.new("gloed2", ld)
        sc.collection.objects.link(og)
        og.location = c0 - naar_cam * float(E("SPIRAAL_GLOED_AF", "260")) + Vector((0, 0, -40))
    M["render_instellingen"](2400, 1200)
    xb = (float(E("SPIRAAL_X0", "0.30")), float(E("SPIRAAL_X1", "0.97")))
    cam = M["kader"](objs + [o for o in bogen if o.type == "CURVE"], math.degrees(hh), float(E("SPIRAAL_HV", "3")),
                     xb, float(E("SPIRAAL_YHALF", "0.45")), lens=float(E("SPIRAAL_LENS", "50")),
                     ymid=float(E("SPIRAAL_YMID", "0.5")))
    HD["naar_camera"](bogen, cam)
    from bpy_extras.object_utils import world_to_camera_view
    bpy.context.view_layer.update()
    xs = [world_to_camera_view(sc, cam, o.matrix_world @ Vector(c)).x for o in objs for c in o.bound_box]
    meting["breedte_delen"] = [round(min(xs), 3), round(max(xs), 3)]
    M["render"]("spiraal")


def boog_groot(naam, objs, straal, mat, dik):
    """Grote gouden boog om de scharnieras (0 tot de stop die de add-on meldt), streepjes per 15 graden, een dikke
    balk bij de stop en de getallen 0° en 115°. Hangt aan deel A."""
    b = HD["deel_b"](naam)
    a = HD["deel_a"](naam, objs)
    hp = HD["eigen"](b, "cj_scharnier_punt")
    lid = HD["eigen"](b, "cj_as").normalized()
    bk = HD["eigen"](b, "cj_buigkant").normalized()
    bk = (bk - lid * bk.dot(lid)).normalized()
    stop = float(b.get("cj_bereik_graden", 0) or 0)

    def r(g):
        t = math.radians(g)
        return lid * math.cos(t) + bk * math.sin(t)
    n = 120
    delen = [buis("boog_" + naam, [hp + r(stop * i / n) * straal for i in range(n + 1)], dik, mat)]
    for g in list(range(15, int(stop), 15)):
        delen.append(buis("streep", [hp + r(g) * (straal - 1.0), hp + r(g) * (straal + 2.2)], dik * 0.7, mat))
    delen.append(buis("nul", [hp + r(0) * (straal - 2.5), hp + r(0) * (straal + 3.5)], dik, mat))
    delen.append(buis("stop", [hp + r(stop) * (straal - 4), hp + r(stop) * (straal + 5)], dik * 2.0, mat))
    fnt = lettertype()
    lm = float(E("BOOG_LETTER", "11"))
    delen.append(tekst(f"{round(stop):d}°", hp + r(stop) * (straal + 10), lm, mat, fnt))
    delen.append(tekst("0°", hp + r(0) * (straal + 8), lm * 0.8, mat, fnt))
    bpy.context.view_layer.update()
    for o in delen:
        o.parent = a
        o.matrix_parent_inverse = a.matrix_world.inverted()
    meting.setdefault("bogen", {})[naam] = {"graden": round(stop, 1), "straal_mm": straal, "aan": a.name}
    return delen


def main():
    {"knie": shot_knie, "spiraal": shot_spiraal}[SHOT]()
    json.dump(meting, open(os.path.join(UIT, f"{STIJL}-{SHOT}.json"), "w"), indent=1, ensure_ascii=False)


main()
