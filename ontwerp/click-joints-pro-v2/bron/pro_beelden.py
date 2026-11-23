"""Nieuwe winkelbeelden voor Click Joints Pro (Dortus, merk-agent, 23 nov 2026, opdracht hoofdchat ±20:35).

Laadt de robot-actiefiguur uit commercie/filmpjes/studio/figuur_robot.py (stijl A), draait de echte knop
Figure from rig van Click Joints Pro 1.2.0 (geen nagemaakte gewrichten), kleurt de gewrichten goud zodat je ze ziet,
buigt ellebogen en knieen met de schuif van de add-on (cj_scharnier_pose, binnen het bereik) en rendert in Cycles.

    blender -b --factory-startup --python pro_beelden.py -- <pro-zip> <uitmap> <stijl a|b> <shot> [samples] [schaal%]
shot: cover169 | cover21 | pose | uit | knie | kogel | voor
Stijl a = Pop (kobaltblauwe studio, familie van Click Cuts A), b = Nacht (pruim en goud, familie van Click Cuts B).
STUDIO_DIR wijst naar commercie/filmpjes/studio.
"""
import importlib
import json
import math
import os
import sys

import bpy
from mathutils import Matrix, Vector

argv = sys.argv[sys.argv.index("--") + 1:]
ZIP, UIT = argv[0], argv[1]
STIJL = argv[2] if len(argv) > 2 else "b"
SHOT = argv[3] if len(argv) > 3 else "pose"
SAMPLES = int(argv[4]) if len(argv) > 4 else 32
SCHAAL = int(argv[5]) if len(argv) > 5 else 50
STUDIO = os.environ.get("STUDIO_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
                                                    "commercie", "filmpjes", "studio"))
sys.path.insert(0, os.path.abspath(STUDIO))
import figuur_laden as FL  # noqa: E402
import figuur_robot as R  # noqa: E402
import studio as S  # noqa: E402

os.makedirs(UIT, exist_ok=True)
H = 220.0
GOUD = "FFD25C"
STIJLEN = {
    "a": {"vloer": "7F95FF", "wand": "2443E6", "lucht": "C9D3FF", "gewricht": GOUD},
    "b": {"vloer": "2E1F3A", "wand": "4A2E57", "lucht": "1D1426", "gewricht": GOUD},
}
ST = STIJLEN[STIJL]
# pose met de schuif van de add-on (graden, binnen het bereik: knie 0 tot 120, elleboog 0 tot 140, uit pro-1.2.0 en de meting)
POSES = {
    "stoer": {"Left knee": 70.0, "Right knee": 25.0, "Left elbow": 105.0, "Right elbow": 60.0},
    "knie": {"Left knee": 120.0, "Right knee": 10.0, "Left elbow": 40.0, "Right elbow": 40.0},
}
meting = {"stijl": STIJL, "shot": SHOT}


def log(*a):
    print("[pro]", *a, flush=True)


# ------------------------------------------------------------------ add-on en figuur
def figuur():
    if "figuur_uit_rig" not in dir(bpy.ops.click_joints):
        bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    arm, ob, _p = R.laad_robot(H)
    return arm, ob


def maak_gewrichten(arm, ob):
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    naam = ob.name
    FL.actief(ob)
    r = bpy.ops.click_joints.figuur_uit_rig()
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    meting["uitslag"] = str(r)
    meting["gewrichten"] = [fig.regel(x) for x in lijst]
    delen = [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_figuur") == naam and o.visible_get()]
    meting["delen"] = len(delen)
    log("Figure from rig", r, len(lijst), "gewrichten", len(delen), "delen")
    for x in meting["gewrichten"]:
        log("  ", x)
    arm.hide_set(True)
    arm.hide_render = True
    # wat de add-on in de weergave verbergt (het oude figuur en de tussenstukken) ook uit de render halen
    for o in bpy.context.scene.objects:
        if (o.get("cj_figuur") or o is ob) and not o.visible_get():
            o.hide_render = True
    return naam, delen


def paar(naam):
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam and o.get("cj_soort", "") == "SCHARNIER":
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def buig(naam, graden):
    """Zelfde als bewijs.py: de Bend-schuif van de add-on, nooit verder dan het bereik."""
    a, b = paar(naam)
    if b is None:
        return None
    stop = float(a.get("cj_bereik_graden", 0) or 0) if a is not None else 0
    g = min(graden, stop) if stop else graden
    bpy.context.view_layer.objects.active = b
    bpy.context.window_manager.cj_scharnier_pose = round(g, 1)
    bpy.context.view_layer.update()
    return [round(float(b.get("cj_pose_graden", g)), 1), stop]


def U():
    return importlib.import_module("bl_ext.user_default.click_joints.uit_elkaar")


def stukken_b(objs):
    return {o.get("cj_naam"): o for o in objs if o.get("cj_deel") == "B" and "cj_as" in o}


def pose_kogels(objs, wens):
    """Kogels poseren zoals de add-on dat doet (cj_pose_graden en cj_pose_richting op deel B, uit_elkaar.zet), binnen
    het gemeten bereik. wens: naam -> (graden, Vector richting waarheen het uiteinde moet). De richting (0 tot 7)
    kies ik zo dat het uiteinde van het deel zo ver mogelijk die kant op gaat."""
    from mathutils import Quaternion
    bs = stukken_b(objs)
    gezet = {}
    for naam, (graden, waarheen) in wens.items():
        b = bs.get(naam)
        if b is None or "cj_centrum" not in b:
            continue
        bereik = float(b.get("cj_bereik_graden", 0) or 0)
        a = next((o for o in bpy.context.scene.objects if o.get("cj_naam") == naam and o.get("cj_deel") == "A"), None)
        if a is not None and not bereik:
            bereik = float(a.get("cj_bereik_graden", 0) or 0)
        g = min(graden, bereik) if bereik else graden
        c = Vector(b["cj_centrum"])
        verst = max((b.matrix_world @ Vector(v) for v in b.bound_box), key=lambda q: (q - c).length)
        as_ = Vector(b["cj_as"]).normalized()
        beste = max(range(8), key=lambda r: (Quaternion(as_.cross(U().richtingen(as_)[r]), math.radians(g)) @ (verst - c)
                                             - (verst - c)).dot(waarheen))
        b["cj_pose_graden"], b["cj_pose_richting"] = g, beste
        U().zet(b, bpy.context.scene.click_joints.uit_elkaar)
        gezet[naam] = [round(g, 1), beste, bereik]
    bpy.context.view_layer.update()
    return gezet


HEEL = {}


def graaf(objs):
    """Welk deel zit aan welk deel: gewricht j verbindt deel B_j met het deel dat het dichtst bij zijn midden ligt."""
    bs = stukken_b(objs)
    ouder = {}
    dg = bpy.context.evaluated_depsgraph_get()
    for naam, b in bs.items():
        a = next((o for o in bpy.context.scene.objects if o.get("cj_naam") == naam and o.get("cj_deel") == "A"), None)
        punt = b.get("cj_centrum") or b.get("cj_snijpunt") or (a.get("cj_snijpunt") if a is not None else None) \
            or (a.get("cj_centrum") if a is not None else None)
        c = Vector(punt) if punt is not None else b.matrix_world.translation
        best = None
        for o in objs:
            if o is b:
                continue
            m = U().echte_matrix(o)
            ok, loc, _n, _i = o.evaluated_get(dg).closest_point_on_mesh(m.inverted() @ c)
            if ok:
                d = (m @ loc - c).length
                if best is None or d < best[0]:
                    best = (d, o)
        ouder[b.name] = best[1].name if best else None
    return bs, ouder


def pose_en_uiteen(objs, keer=0.0):
    """Zet elk deel op zijn plek: de pose die de add-on per gewricht geeft (deel B gedraaid om zijn eigen midden) wordt
    doorgegeven aan alles wat eraan vastzit (de onderarm draait mee met de schouder), en elk gewricht schuift keer x de
    afstand van de Exploded view van de add-on (1,5 kogeldiameter) uit elkaar langs zijn as. keer=1 is precies de
    Exploded view van de add-on. Alleen voor het beeld; de mesh verandert niet."""
    bpy.context.view_layer.update()
    bs, ouder = graaf(objs)
    eigen_pose = {b.name: b.matrix_world @ U().echte_matrix(b).inverted() for b in bs.values()}
    rust = {o.name: U().echte_matrix(o) for o in objs}
    schuif = {b.name: Matrix.Translation(Vector(b["cj_as"]).normalized() * U().afstand(b) * keer) for b in bs.values()}
    randen = {}
    for bn, nn in ouder.items():
        if nn is None:
            continue
        stap = schuif[bn] @ eigen_pose[bn]
        randen.setdefault(nn, []).append((bn, stap))
        randen.setdefault(bn, []).append((nn, stap.inverted()))
    romp = [o.name for o in objs if o.get("cj_deel") != "B"]
    heel = {r: Matrix.Identity(4) for r in romp}
    rij = list(romp)
    while rij:
        x = rij.pop(0)
        for y, stap in randen.get(x, []):
            if y not in heel:
                # het pose-deel van y is in wereldmaat om zijn eigen midden; eerst de ouder, dan y
                heel[y] = heel[x] @ stap
                rij.append(y)
    HEEL.clear()
    HEEL.update(heel)
    for nm, m in heel.items():
        o = bpy.data.objects[nm]
        o.delta_location = (0, 0, 0)
        o.delta_rotation_euler = (0, 0, 0)
        o.delta_rotation_quaternion = (1, 0, 0, 0)
        o.matrix_world = m @ rust[nm]
    bpy.context.view_layer.update()
    return {bpy.data.objects[k].get("cj_naam"): v for k, v in ouder.items()}


def punt_van(naam):
    for o in bpy.context.scene.objects:
        if o.get("cj_naam") == naam:
            p = o.get("cj_centrum") or o.get("cj_snijpunt")
            if p is not None:
                v = Vector(p)
                b = next((x for x in bpy.context.scene.objects if x.get("cj_naam") == naam and x.get("cj_deel") == "B"),
                         None)
                if b is not None:
                    v = v + Vector(b.delta_location) * 0.5
                return v
    return Vector((0, 0, H / 2))


def punt_via(naam, drager):
    """Rustpunt van gewricht naam, meebewogen met het deel waar het aan vastzit (drager = naam van dat gewricht, deel B)."""
    p = None
    for o in bpy.context.scene.objects:
        if o.get("cj_naam") == naam and (o.get("cj_centrum") or o.get("cj_snijpunt")):
            p = Vector(o.get("cj_centrum") or o.get("cj_snijpunt"))
            break
    d = next((x for x in bpy.context.scene.objects if x.get("cj_naam") == drager and x.get("cj_deel") == "B"), None)
    if p is None or d is None:
        return p or Vector((0, 0, H / 2))
    bpy.context.view_layer.update()
    return d.matrix_world @ (U().echte_matrix(d).inverted() @ p)


def midden_gewricht(naam, drager):
    """Midden tussen de twee helften van een gewricht na pose_en_uiteen (drager: het gewricht van het deel aan de
    andere kant, leeg voor de romp)."""
    p = None
    for o in bpy.context.scene.objects:
        if o.get("cj_naam") == naam and (o.get("cj_centrum") or o.get("cj_snijpunt")):
            p = Vector(o.get("cj_centrum") or o.get("cj_snijpunt"))
            break
    p = p or Vector((0, 0, H / 2))
    b = next((x for x in bpy.context.scene.objects if x.get("cj_naam") == naam and x.get("cj_deel") == "B"), None)
    d = next((x for x in bpy.context.scene.objects if x.get("cj_naam") == drager and x.get("cj_deel") == "B"), None)
    mb = HEEL.get(b.name, Matrix.Identity(4)) if b is not None else Matrix.Identity(4)
    md = HEEL.get(d.name, Matrix.Identity(4)) if d is not None else Matrix.Identity(4)
    return ((mb @ p) + (md @ p)) / 2


def doos_om(c, r):
    """Onzichtbare doos om een punt, alleen om de camera op een gewricht te richten."""
    bpy.ops.mesh.primitive_cube_add(size=2 * r, location=c)
    d = bpy.context.active_object
    d.hide_render = True
    d.name = "kader_doos"
    return d


def zichtbaar(naam):
    return [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_figuur") == naam and o.visible_get()]


def goud_gewricht():
    m = bpy.data.materials.get("studio_gewricht")
    if m is None:
        return
    nt = m.node_tree
    b = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if b is None:
        return
    b.inputs["Base Color"].default_value = S.srgb(ST["gewricht"])
    S._zet(b, "Metallic", 0.75)
    S._zet(b, "Roughness", 0.24)
    S._zet(b, "Coat Weight", 0.3)


# ------------------------------------------------------------------ voor: gewone rig (doorzichtig figuur met botten)
def toon_rig(arm, ob):
    glas = bpy.data.materials.new("voor_glas")
    nt = glas.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = S.srgb("E9ECF5" if STIJL == "a" else "C9B9FF")
    b.inputs["Alpha"].default_value = 0.22
    b.inputs["Roughness"].default_value = 0.3
    try:
        glas.surface_render_method = "BLENDED"
    except Exception:  # noqa: BLE001
        pass
    ob.data.materials.clear()
    ob.data.materials.append(glas)
    gloed = bpy.data.materials.new("voor_bot")
    nt = gloed.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = S.srgb("FFFFFF" if STIJL == "a" else GOUD)
    e.inputs["Strength"].default_value = 4.0
    nt.links.new(e.outputs[0], o.inputs[0])
    mw = arm.matrix_world
    for bn in arm.data.bones:
        kop, staart = mw @ bn.head_local, mw @ bn.tail_local
        lengte = (staart - kop).length
        if lengte < 1e-3:
            continue
        bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=1.1, depth=lengte, location=(kop + staart) / 2)
        c = bpy.context.active_object
        c.rotation_euler = (staart - kop).to_track_quat("Z", "Y").to_euler()
        c.data.materials.append(gloed)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2.4, location=kop, segments=16, ring_count=8)
        bpy.context.active_object.data.materials.append(gloed)


# ------------------------------------------------------------------ studio, licht, camera
def studio(lo_z):
    S.KLEUR["vloer"] = ST["vloer"]
    S.KLEUR["wand"] = ST["wand"]
    S.achterwand(H * 1.1, z0=lo_z)
    sc = bpy.context.scene
    if sc.world is None:
        sc.world = bpy.data.worlds.new("w")
    bg = next((n for n in sc.world.node_tree.nodes if n.type == "BACKGROUND"), None)
    if bg is not None:
        bg.inputs[0].default_value = S.srgb(ST["lucht"])
        bg.inputs[1].default_value = 0.4 if STIJL == "a" else 0.08
    mid = Vector((0, 0, H * 0.5))

    def lamp(naam, plek, maat_, kracht, kleur):
        ld = bpy.data.lights.new(naam, "AREA")
        ld.shape, ld.size, ld.energy = "DISK", maat_, kracht
        ld.color = S.srgb(kleur)[:3]
        ob = bpy.data.objects.new(naam, ld)
        sc.collection.objects.link(ob)
        ob.location = Vector(plek)
        ob.rotation_euler = (mid - ob.location).to_track_quat("-Z", "Y").to_euler()
    k = (H / 436.0) ** 2
    if STIJL == "a":
        lamp("sleutel", (1.5 * H, -1.6 * H, 1.9 * H), 1.2 * H, 2.2e7 * k, "FFF3E4")
        lamp("vul", (-1.9 * H, -1.3 * H, 0.7 * H), 1.8 * H, 4.0e6 * k, "DDE6FF")
        lamp("rand", (-0.9 * H, 1.3 * H, 2.0 * H), 0.8 * H, 1.2e7 * k, "FFFFFF")
    else:
        lamp("sleutel", (1.4 * H, -1.5 * H, 1.8 * H), 1.0 * H, 2.0e7 * k, "FFE2B0")
        lamp("vul", (-1.8 * H, -1.2 * H, 0.6 * H), 1.6 * H, 4.0e6 * k, "B9A6FF")
        lamp("rand", (-1.0 * H, 1.4 * H, 1.9 * H), 0.7 * H, 1.6e7 * k, "FFD25C")
        lamp("rand2", (1.2 * H, 1.2 * H, 1.4 * H), 0.7 * H, 9.0e6 * k, "A58CFF")
        ld = bpy.data.lights.new("gloed", "POINT")
        ld.energy, ld.shadow_soft_size = 1.2e7 * k, 0.3 * H
        ld.color = S.srgb("7A4FB0")[:3]
        ob = bpy.data.objects.new("gloed", ld)
        sc.collection.objects.link(ob)
        ob.location = (0, 1.3 * H, 0.45 * H)


def render_instellingen(bx, by):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = SAMPLES
    sc.cycles.use_denoising = True
    sc.cycles.max_bounces = 6
    sc.render.resolution_x, sc.render.resolution_y = bx, by
    sc.render.resolution_percentage = SCHAAL
    sc.render.film_transparent = False
    sc.view_settings.view_transform = "AgX"
    try:
        sc.view_settings.look = "AgX - Punchy"
    except Exception:  # noqa: BLE001
        pass
    sc.render.image_settings.file_format = "PNG"


def kader(objs, hh, hv, xbereik, yhalf, lens=60, ymid=0.5, doel=None):
    """Camera zo zetten dat de objecten precies in het vak vallen (zelfde aanpak als de Click Cuts-beelden)."""
    from bpy_extras.object_utils import world_to_camera_view
    sc = bpy.context.scene
    bpy.context.view_layer.update()
    hoeken = []
    for o in objs:
        for c in o.bound_box:
            hoeken.append(o.matrix_world @ Vector(c))
    c = doel or sum(hoeken, Vector()) / len(hoeken)
    straal = max((p - c).length for p in hoeken)
    cd = bpy.data.cameras.new("cam")
    cd.lens, cd.clip_start, cd.clip_end = lens, 1, 100000
    cd.sensor_fit = "HORIZONTAL"   # anders klopt angle_x niet bij staande beelden (de camera schoot weg: zwart beeld)
    cam = bpy.data.objects.new("cam", cd)
    sc.collection.objects.link(cam)
    a, e = math.radians(hh), math.radians(hv)
    cam.location = c + Vector((math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e))) * straal * 4
    cam.rotation_euler = (c - cam.location).to_track_quat("-Z", "Y").to_euler()
    sc.camera = cam
    for _ in range(80):
        bpy.context.view_layer.update()
        pts = [world_to_camera_view(sc, cam, p) for p in hoeken]
        x0, x1 = min(p.x for p in pts), max(p.x for p in pts)
        y0, y1 = min(p.y for p in pts), max(p.y for p in pts)
        schaal = max((x1 - x0) / (xbereik[1] - xbereik[0]), (y1 - y0) / (2 * yhalf))
        m = cam.matrix_world.to_3x3()
        d = (cam.location - c).length
        mx_ = (x0 + x1) / 2 - (xbereik[0] + xbereik[1]) / 2
        my_ = (y0 + y1) / 2 - ymid
        bw = 2 * d * math.tan(cam.data.angle_x / 2)
        bh = bw * sc.render.resolution_y / sc.render.resolution_x
        cam.location += m @ Vector((mx_ * bw, my_ * bh, 0))
        cam.location += (m @ Vector((0, 0, 1))) * d * (schaal - 1) * 0.7
        if abs(schaal - 1) < 0.01 and abs(mx_) < 0.005 and abs(my_) < 0.005:
            break
    log("kader", len(objs), "objecten, straal", round(straal, 1), "afstand", round((cam.location - c).length, 1),
        "schaal", round(schaal, 3), "x", round(x0, 2), round(x1, 2), "y", round(y0, 2), round(y1, 2))
    return cam


def laagste(objs):
    bpy.context.view_layer.update()
    return min((o.matrix_world @ Vector(c)).z for o in objs for c in o.bound_box)


def render(naam):
    bpy.context.scene.render.filepath = os.path.join(UIT, f"{STIJL}-{naam}.png")
    bpy.ops.render.render(write_still=True)
    log("render", bpy.context.scene.render.filepath)


# ------------------------------------------------------------------ hoofd
def main():
    arm, ob = figuur()
    if SHOT == "voor":
        toon_rig(arm, ob)
        objs = [ob]
        studio(laagste(objs))
        render_instellingen(800, 1600)
        kader(objs, 28, 8, (0.08, 0.92), 0.36, ymid=0.46)
        render("voor")
        return
    naam, delen = maak_gewrichten(arm, ob)
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=ST["gewricht"])
    goud_gewricht()
    inst = bpy.context.scene.click_joints
    try:
        bpy.context.window_manager.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    pose = POSES["knie"] if SHOT == "knie" else POSES["stoer"]
    inst.uit_elkaar = False
    U().zet_alle(bpy.context.scene)
    objs = zichtbaar(naam)
    if SHOT not in ("uit", "uitp", "kogel", "knie"):
        meting["pose"] = {n: buig(n, g) for n, g in pose.items()}
        voor, achter = Vector((0, -1, 0)), Vector((0, 1, 0))
        meting["kogels"] = pose_kogels(objs, {
            "Left shoulder": (30.0, voor), "Right shoulder": (30.0, achter + Vector((0.6, 0, 0))),
            "Left hip": (27.0, voor), "Right hip": (27.0, achter), "Neck": (15.0, Vector((-0.5, -0.3, 0))),
        })
    keer = {"uit": 2.3, "uitp": 2.3, "knie": 2.0, "kogel": 2.0, "cover169": 1.0, "cover21": 1.0}.get(SHOT, 0.0)
    meting["uit_elkaar_keer"] = keer
    meting["ouders"] = pose_en_uiteen(objs, keer)
    objs = zichtbaar(naam)
    studio(laagste(objs))
    if SHOT == "cover169":
        render_instellingen(2560, 1440)
        kader(objs, 34, 6, (0.55, 0.98), 0.62, lens=70, ymid=0.35)
    elif SHOT == "cover21":
        render_instellingen(2400, 1200)
        kader(objs, 34, 6, (0.57, 0.98), 0.62, lens=70, ymid=0.35)
    elif SHOT == "pose":
        render_instellingen(1600, 1600)
        kader(objs, 30, 2, (0.14, 0.86), 0.40, lens=60, ymid=0.43)
    elif SHOT == "uit":
        render_instellingen(1600, 1600)
        kader(objs, 26, 8, (0.1, 0.9), 0.385, lens=60, ymid=0.42)
    elif SHOT == "uitp":
        render_instellingen(800, 1600)
        kader(objs, 26, 8, (0.08, 0.92), 0.36, lens=60, ymid=0.46)
    elif SHOT == "knie":
        render_instellingen(800, 1600)
        kader([doos_om(midden_gewricht("Left knee", "Left hip"), 24)], float(os.environ.get("KNIE_HOEK", "38")), 8, (0.1, 0.9), 0.36, lens=100, ymid=0.43)
    elif SHOT == "kogel":
        render_instellingen(800, 1600)
        kader([doos_om(midden_gewricht("Left shoulder", ""), 24)], 34, 12, (0.06, 0.94), 0.38, lens=100,
              ymid=0.43)
    meting["objecten"] = sorted({(o.get("cj_naam") or o.name) for o in objs})[:40]
    render(SHOT)
    json.dump(meting, open(os.path.join(UIT, f"{STIJL}-{SHOT}.json"), "w"), indent=1, ensure_ascii=False)


main()
