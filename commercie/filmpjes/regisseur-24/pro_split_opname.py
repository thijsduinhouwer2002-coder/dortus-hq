"""Opname Pro-Short "Already split? Add a knee joint" (regisseur-24, Regisseur run 26, 24 nov 2026).
Bouwt op regisseur-23/pro_cursor_opname.py (clip 3), maar met de eigen robot van studio-3 in plaats van blokken,
zodat het eerste beeld een mooi stuk techniek is (besluit Thijs 24 nov: beelden spectaculair).
Verloop, echte Blender 5.3.0 met Click Joints Pro 1.2.7 (main, Shift + rechtsklik werkt sinds b105332):
1. Robot van 440 mm (figuur_robot.py, Make watertight van de add-on), rig weg, dan met een vlak door de dijen in
   losse delen: romp met armen, linkerbeen, rechterbeen. Elk deel is gesloten (zoals na splitsen in een ander programma).
2. Echte muis: klik op het linkerbeen, camera van opzij, Shift + rechtsklik op de knie (3D-cursor), zijbalk naar
   Click Joints, klik "Knee" onder Figure joints, "Show bend range", camera naar de knie.
3. Renders in de studio (studio.py, EEVEE): render-1 robot met de knie gebogen (eerste beeld), render-2 dichtbij de
   knie, render-3 heldenbeeld van de andere kant (eindkaart).
Geen vangnet: lukt een klik niet, dan KORT FOUT. Wat in beeld staat is echt gebeurd.
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl start.blend --python pro_split_opname.py -- <uitmap> <pro zip>"""
import math
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..", "opname"))
sys.path.insert(0, os.path.join(HIER, "..", "studio"))
from blender_opname import *  # noqa: F401,F403,E402
import bmesh  # noqa: E402
from bpy_extras import view3d_utils  # noqa: E402

zet_naam("pro24")
ZIP = sys.argv[sys.argv.index("--") + 2] if len(sys.argv) > sys.argv.index("--") + 2 else "/tmp/click_joints_betaald.zip"
M = film["metingen"]
H = float(os.environ.get("CJ_HOOGTE", "440"))   # 220 gaf een knie van r 11: "Too thin here for a hinge" (run 24 bij r 16)
os.environ.setdefault("CJ_VOXEL", "1.0")        # zelfde fijnheid per lengte als 0,5 bij 220 mm
SNEDE_Z = 100.0 * H / 220.0                      # door de dijen, onder het bekken, boven de knie (57 bij 220)


def zijbalk():
    _, a = gebied("VIEW_3D")
    for r in a.regions:
        if r.type == "UI":
            return a, r
    return a, None


def ui_vak():
    _, a = gebied("VIEW_3D")
    return regio_rect(a, "UI")


def scherm_punt(p):
    _, a = gebied("VIEW_3D")
    r = [x for x in a.regions if x.type == "WINDOW"][0]
    q = view3d_utils.location_3d_to_region_2d(r, a.spaces.active.region_3d, Vector(p))
    v = regio_rect(a)
    return int(v[0] + q.x), int(v[1] + v[3] - q.y)


def naar_tabblad(doel="Click Joints"):
    w = bpy.context.window_manager.windows[0]
    for poging in range(16):
        a, r = zijbalk()
        if r.active_panel_category == doel:
            return True
        x = w.x + r.x + r.width - 8
        y = w.y + w.height - (r.y + r.height // 2)
        xdo("mousemove", str(x), str(y))
        xdo("keydown", "ctrl")
        xdo("click", "5" if poging < 7 else "4")
        xdo("keyup", "ctrl")
        yield 0.4
    return False


def zoek_scroll(tekst, richting="5", keer=10, drempels=("35%", "60%", "75%")):
    vak = ui_vak()
    for _ in range(keer):
        p = knop(tekst, vak, drempels)
        if p:
            return p
        xdo("mousemove", str(vak[0] + vak[2] // 2), str(vak[1] + vak[3] // 2))
        MUIS["x"], MUIS["y"] = vak[0] + vak[2] // 2, vak[1] + vak[3] // 2
        for _k in range(3):
            xdo("click", richting)
            yield 0.05
            neem()
        yield 0.5
        neem(2)
    return None


def splits(fig):
    """Snijdt de robot met een vlak op SNEDE_Z, alleen bij de benen (|x| < 0,2 H: niet door de handen), en vult de
    snijvlakken dicht. Geeft de losse delen als eigen objecten: Body, Leg.L (+x), Leg.R (-x)."""
    me = fig.data
    bm = bmesh.new()
    bm.from_mesh(me)
    grens = 0.2 * H
    geom = [v for v in bm.verts if abs(v.co.x) < grens and v.co.z < SNEDE_Z + 0.2 * H]
    geom = geom + list({e for v in geom for e in v.link_edges}) + list({f for v in geom for f in v.link_faces})
    res = bmesh.ops.bisect_plane(bm, geom=geom, plane_co=(0, 0, SNEDE_Z), plane_no=(0, 0, 1), dist=0.0005)
    snede = [e for e in res["geom_cut"] if isinstance(e, bmesh.types.BMEdge)]
    bmesh.ops.split_edges(bm, edges=snede)
    rand = [e for e in bm.edges if e.is_boundary]
    bmesh.ops.holes_fill(bm, edges=rand, sides=0)
    bm.to_mesh(me)
    bm.free()
    me.update()
    bpy.ops.object.select_all(action="DESELECT")
    fig.select_set(True)
    bpy.context.view_layer.objects.active = fig
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.separate(type="LOOSE")
    bpy.ops.object.mode_set(mode="OBJECT")
    delen = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    groot = sorted(delen, key=lambda o: -len(o.data.vertices))
    hoofd = []
    for o in delen:
        bpy.context.view_layer.update()
        zs = [(o.matrix_world @ v.co) for v in o.data.vertices]
        top = max(q.z for q in zs)
        cx = sum(q.x for q in zs) / len(zs)
        if top < SNEDE_Z + 1.0 and len(o.data.vertices) > 500:
            o.name = o.data.name = "Leg.L" if cx > 0 else "Leg.R"
        elif o is groot[0]:
            o.name = o.data.name = "Body"
        else:
            hoofd.append(o)
    if hoofd:   # losse snippers (bijvoorbeeld een oog-led) horen bij de romp
        body = bpy.data.objects["Body"]
        bpy.ops.object.select_all(action="DESELECT")
        for o in hoofd + [body]:
            o.select_set(True)
        bpy.context.view_layer.objects.active = body
        bpy.ops.object.join()
    uit = {}
    for o in bpy.context.scene.objects:
        if o.type == "MESH":
            bpy.ops.object.select_all(action="DESELECT")
            o.select_set(True)
            bpy.context.view_layer.objects.active = o
            bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
            bm = bmesh.new()
            bm.from_mesh(o.data)
            open_r = sum(1 for e in bm.edges if not e.is_manifold)
            bm.free()
            uit[o.name] = {"punten": len(o.data.vertices), "open_randen": open_r}
    bpy.ops.object.select_all(action="DESELECT")
    return uit


def delen_ab():
    return [o for o in bpy.context.scene.objects if o.get("cj_deel") in ("A", "B")]


def renders():
    """Studio-renders na de opname (EEVEE door de camera, studio.py zoals regisseur-14)."""
    import figuur_robot as R
    import studio as S
    sc = bpy.context.scene
    try:
        bpy.context.window_manager.cj_scharnier_boog = False
    except Exception:  # noqa: BLE001
        pass
    try:
        sc.click_joints.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    S.bouw(H)
    delen = [o for o in sc.objects if o.type == "MESH" and not o.name.startswith("studio_") and o.visible_get()
             and (o.name in ("Body", "Leg.R") or o.get("cj_deel") in ("A", "B"))]
    for o in sc.objects:
        if o.type == "MESH" and o not in delen and not o.name.startswith("studio_"):
            o.hide_set(True)
            o.hide_render = True
    M["render_delen"] = [o.name for o in delen]
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    cam_ob = S.camera()
    a = [o for o in delen if o.get("cj_deel") == "A"]
    b = [o for o in delen if o.get("cj_deel") == "B"]
    M["render_buig"] = None
    if a and b:
        # De add-on draait deel B (de dij) om het scharnier. Voor de render blijft de dij aan de romp en draait het
        # onderbeen (deel A) dezelfde hoek de andere kant op: zelfde stand van de knie, de robot staat op zijn
        # rechterbeen met de linkerknie gebogen.
        try:
            a_oud = a[0].matrix_world.copy()
            b_oud = b[0].matrix_world.copy()
            bpy.context.view_layer.objects.active = b[0]
            graden = min(95.0, max(M.get("buig_graden") or [95.0]))
            bpy.context.window_manager.cj_scharnier_pose = graden
            bpy.context.view_layer.update()
            rot = b[0].matrix_world @ b_oud.inverted()
            bpy.context.window_manager.cj_scharnier_pose = 0.0
            bpy.context.view_layer.update()
            b[0].matrix_world = b_oud
            a[0].matrix_world = rot.inverted() @ a_oud
            bpy.context.view_layer.update()
            M["render_buig"] = graden
        except Exception as e:  # noqa: BLE001
            log(f"buigen voor de render lukte niet: {e}")
    for o in sc.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    bpy.context.view_layer.update()
    yield 0.5
    S.richt(cam_ob, delen, "staand", draai=-38, kantel=8, vul=0.74, midden_y=0.56)
    yield 0.3
    S.render(os.path.join(uitmap, "render-1.png"))
    log("KORT OK render-1")
    S.richt(cam_ob, [o for o in delen if o.get("cj_deel") in ("A", "B")], "staand", draai=-70, kantel=12, vul=0.80, midden_y=0.52)
    yield 0.3
    S.render(os.path.join(uitmap, "render-2.png"))
    log("KORT OK render-2")
    S.richt(cam_ob, delen, "staand", draai=30, kantel=10, vul=0.84, midden_y=0.53)
    yield 0.3
    S.render(os.path.join(uitmap, "render-3.png"))
    log("KORT OK render-3")


def verloop():
    import figuur_laden as FL
    a3 = zet_scherm(mm=True)
    log(f"Blender {bpy.app.version_string}, zip {ZIP}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    sc = bpy.context.scene
    arm, fig, p = FL.laad_figuur("robot", H)
    for m in list(fig.modifiers):
        fig.modifiers.remove(m)
    bpy.data.objects.remove(arm)
    M["delen_na_splitsen"] = splits(fig)
    log(f"KORT delen {M['delen_na_splitsen']}")
    if "Leg.L" not in M["delen_na_splitsen"] or M["delen_na_splitsen"]["Leg.L"]["open_randen"]:
        log("KORT FOUT splitsen: geen gesloten linkerbeen")
        einde()
        return
    log("KORT OK splitsen")
    been = bpy.data.objects["Leg.L"]
    knie = Vector(p["l-knee"])
    M["knie"] = [round(v, 1) for v in knie]
    sc.cursor.location = (0, 0, 0)
    sp = a3.spaces.active
    sp.overlay.show_cursor = True
    bpy.context.preferences.system.use_region_overlap = False
    sp.show_region_ui = True
    sc.click_joints.uit_elkaar = False
    yield 1.0
    ok = yield from naar_tabblad()
    M["tabblad"] = ok
    log(f"KORT tabblad Click Joints {ok}")
    xdo("mousemove", "400", "900")
    MUIS["x"], MUIS["y"] = 400, 900
    midden = (0.0, 0.0, H * 0.5)
    cam(-40, 80.0, H * 2.6, midden)
    yield 1.0

    # Even uit elkaar: zo zie je dat het al losse delen zijn (Blender, echte objecten)
    deel("mooi")
    rust = {o.name: o.location.copy() for o in sc.objects if o.type == "MESH"}
    uit = {"Body": Vector((0, 0, 0.06 * H)), "Leg.L": Vector((0.05 * H, 0, -0.02 * H)), "Leg.R": Vector((-0.05 * H, 0, -0.02 * H))}

    def schuif(t):
        s = math.sin(math.pi * t)
        for n, v in uit.items():
            if n in rust:
                bpy.data.objects[n].location = rust[n] + v * s
        cam(-40 + 25 * t, 80.0 + 4 * t, H * (2.6 - 0.3 * t), midden)
    yield from stuk(90, schuif)
    for n in rust:
        bpy.data.objects[n].location = rust[n]
    herteken()

    deel("kies")
    pk = scherm_punt((knie.x, knie.y - 0.04 * H, knie.z - 0.07 * H))
    yield from muis_naar(pk[0], pk[1], 22)
    klik()
    yield 0.4
    neem(6)
    M["kies_actief"] = bpy.context.view_layer.objects.active.name if bpy.context.view_layer.objects.active else None
    if M["kies_actief"] != been.name:
        log(f"KORT FOUT kies: actief is {M['kies_actief']}")
        einde()
        return
    log("KORT OK kies")
    yield from houd(16)

    # Van opzij kijken (de scharnieras is de kijkrichting, melding Olaf 16:50), dan Shift + rechtsklik op de knie
    deel("opzij")
    yield from stuk(60, lambda t: cam(-15 + 105 * t, 84.0 + 6 * t, H * (2.3 - 1.2 * t), Vector(midden).lerp(knie, t)))
    cam(90, 90.0, H * 1.1, knie)
    yield from houd(10)
    deel("cursor")
    doel_z = knie.z + 12.0 * H / 440.0   # precies op het midden van de knie gaf Tight (korte lip), 12 mm hoger een scharnier (proef run 26)
    pc = scherm_punt((knie.x, knie.y, doel_z))
    yield from muis_naar(pc[0], pc[1], 22)
    yield 0.3
    xdo("keydown", "shift")
    yield 0.2
    xdo("click", "3")
    MUIS["klik"] = 1
    yield 0.2
    xdo("keyup", "shift")
    yield 0.5
    neem(6)
    c = sc.cursor
    M["cursor_plek"] = [round(v, 2) for v in c.location]
    M["cursor_z"] = [round(v, 3) for v in c.matrix.col[2].xyz]
    log(f"KORT cursor {M['cursor_plek']} z-as {M['cursor_z']}")
    if abs(c.location.z - doel_z) > 0.03 * H:
        log("KORT FOUT cursor: niet op de knie")
        einde()
        return
    log("KORT OK cursor")
    yield from houd(30)

    deel("knee")
    kn = yield from zoek_scroll("Knee")
    M["knee_ocr"] = kn
    if not kn:
        log("KORT FOUT knee: knop niet gevonden")
        einde()
        return
    yield 0.6
    kn = knop("Knee", ui_vak()) or kn
    yield from muis_naar(kn[0], kn[1], 22)
    neem(4)
    klik()
    yield 3.0
    neem(6)
    ab = delen_ab()
    M["delen"] = [o.name for o in ab]
    if len(ab) != 2:
        log(f"KORT FOUT knee: {len(ab)} delen, objecten {[o.name for o in sc.objects]}")
        for naam, tekst in (("melding_ocr", "Glue"), ("dun_ocr", "thin"), ("kant_ocr", "side")):
            M[naam] = ocr(tekst, ui_vak(), "35%")
        einde()
        return
    a_deel = [o for o in ab if o.get("cj_deel") == "A"][0]
    M["passing"] = a_deel.get("cj_passing")
    M["melding"] = a_deel.get("cj_melding")
    M["stand"] = a_deel.get("cj_hoek")
    M["buig_graden"] = list(a_deel.get("cj_buig_graden", []))
    M["wand_mm"] = round(float(a_deel.get("cj_wand_mm", -1)), 3)
    log(f"KORT OK knee {M['passing']} {M['melding']} buig {M['buig_graden']} wand {M['wand_mm']}")
    yield from houd(40)
    for naam, tekst in (("fit_ocr", "fit"), ("bends_ocr", "Bends"), ("lijst_ocr", "Knee: hinge")):
        M[naam] = ocr(tekst, ui_vak(), "35%")

    deel("bereik")
    sb = yield from zoek_scroll("Show bend range", "4")
    if not sb:
        sb = yield from zoek_scroll("Show bend range", "5")
    M["bereik_ocr"] = sb
    if not sb:
        log("KORT FOUT bereik: knop niet gevonden")
        einde()
        return
    yield 0.6
    sb = knop("Show bend range", ui_vak()) or sb
    yield from muis_naar(sb[0], sb[1], 22)
    klik()
    yield 0.8
    neem(6)
    M["toon_bereik"] = bool(sc.click_joints.toon_bereik)
    if not M["toon_bereik"]:
        log("KORT FOUT bereik: niet aan")
        einde()
        return
    log("KORT OK bereik")
    xdo("mousemove", "300", "1700")
    MUIS["x"], MUIS["y"] = 300, 1700
    yield from houd(20)
    yield from stuk(110, lambda t: cam(90 + 25 * t, 90.0 - 8 * t, H * (1.1 - 0.35 * t), knie))
    yield from houd(50)

    deel("eind")
    log("KORT OK opname")
    bewaar_film()
    yield from renders()
    log("KORT OK alles")
    einde()


start(verloop)
