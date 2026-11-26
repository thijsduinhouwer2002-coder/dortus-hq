# Verloop v7 van de sale-Short (issue #159, Regisseur 26 nov 2026). Wordt door proces7.py in de opname van regisseur-28
# gezet (zelfde echte Blender, zelfde beeld-voor-beeld-klok). Thijs 26 nov 18:14: "niet van beeld wisselen, alles in
# één beeld", "niet ingezoomd maar dynamisch", "maak exact die tiktok na". Dus: één doorlopende opname van de
# weergave, de robot vult het staande scherm, de camera van de weergave draait de hele tijd rustig rond, en in
# hetzelfde beeld verandert de robot elke ±0,7 s: grijs met rig, Figure from rig (delen in willekeurige kleuren),
# Exploded view, knie tot de stop en voorbij (rood), deel voor deel kleur, schaduw, pose. Daarna eind.blend voor de
# Cycles-eindfilm met een bewegende camera. De pose wordt gekozen met een botsingscheck (geen deel door een ander).
import random as _rnd
_rnd.seed(29)
FPS7 = 30
EIND_SEC = float(os.environ.get("CJ_EIND_SEC", "6.5"))
GRIJS = (0.62, 0.62, 0.64, 1.0)


def zacht(t):
    t = min(1.0, max(0.0, t))
    return t * t * (3 - 2 * t)


def gebied3d():
    for venster in bpy.context.window_manager.windows:
        for g in venster.screen.areas:
            if g.type == "VIEW_3D":
                return venster, g
    return None, None


def zicht(g, draai, kantel, afstand, punt):
    rv = g.spaces.active.region_3d
    rv.view_perspective = "PERSP"
    rv.view_rotation = Euler((math.radians(kantel), 0.0, math.radians(draai)), "XYZ").to_quaternion()
    rv.view_distance = afstand
    rv.view_location = Vector(punt)


def hoogte_px(g, objs):
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    regio = next(r for r in g.regions if r.type == "WINDOW")
    rv = g.spaces.active.region_3d
    ys, xs = [], []
    for o in objs:
        for c in o.bound_box:
            q = location_3d_to_region_2d(regio, rv, o.matrix_world @ Vector(c))
            if q is not None:
                ys.append(q.y)
                xs.append(q.x)
    if not ys:
        return 0.0, regio.height
    return max(ys) - min(ys), regio.height


def sleutels(delen, frame):
    for o in delen:
        o.keyframe_insert("location", frame=frame)
        o.keyframe_insert("rotation_quaternion", frame=frame)


def maak_toets(delen, per_deel=500):
    """Snelle botsingscheck: per deel één BVH in eigen ruimte (één keer), en per deel ±500 punten van het oppervlak.
    Een punt van deel X zit in deel Y als het meer dan 0,6 mm van het oppervlak van Y ligt en een straal in twee
    richtingen Y een oneven aantal keer raakt; vanaf 3 zulke punten telt het paar als botsing. Geeft een functie die de paren (X, Y) teruggeeft waarvan punten in elkaar zitten."""
    from mathutils.bvhtree import BVHTree
    dg = bpy.context.evaluated_depsgraph_get()
    bomen, punten = {}, {}
    for o in delen:
        bomen[o.name] = BVHTree.FromObject(o, dg)
        vs = o.data.vertices
        stap = max(1, len(vs) // per_deel)
        punten[o.name] = [vs[i].co.copy() for i in range(0, len(vs), stap)]

    def binnen(boom, lp):
        """Echt binnen: een straal in twee richtingen raakt het oppervlak een oneven aantal keer."""
        for r in (Vector((0.013, 0.007, 1.0)).normalized(), Vector((1.0, 0.011, 0.017)).normalized()):
            o_, k = lp.copy(), 0
            while k < 40:
                hit, _n, _i, _d = boom.ray_cast(o_, r)
                if hit is None:
                    break
                k += 1
                o_ = hit + r * 0.01
            if k % 2 == 0:
                return False
        return True

    def paren():
        uit = set()
        mw = {o.name: o.matrix_world.copy() for o in delen}
        inv = {k: m.inverted() for k, m in mw.items()}
        for x in delen:
            wereld = [mw[x.name] @ c for c in punten[x.name]]
            for y in delen:
                if y is x:
                    continue
                boom, iv = bomen[y.name], inv[y.name]
                diep = 0
                for wp in wereld:
                    lp = iv @ wp
                    loc, nor, _i, d = boom.find_nearest(lp, 60.0)
                    if loc is None or d < 0.6:
                        continue
                    if binnen(boom, lp):
                        diep += 1
                        if diep >= 3:
                            uit.add(tuple(sorted((x.name, y.name))))
                            break
        return uit
    return paren


def schaal_pose(pose, t):
    uit = {}
    for k, v in pose.items():
        uit[k] = [(a, g * t) for a, g in v] if isinstance(v, list) else v * t
    return uit


def kandidaten():
    lijst = []
    for sy in (1, -1):
        for el in ((95.0, 55.0), (70.0, 35.0), (45.0, 20.0)):
            for sx in (-18.0, 0.0):
                lijst.append({
                    "Left hip": [((0, 1, 0), -9.0)], "Right hip": [((0, 1, 0), 9.0)],
                    "Left knee": 8.0, "Right knee": 8.0,
                    "Left shoulder": [((1, 0, 0), sx), ((0, 1, 0), sy * 28.0)], "Left elbow": el[0],
                    "Right shoulder": [((1, 0, 0), -sx * 0.6), ((0, 1, 0), -sy * 28.0)], "Right elbow": el[1],
                    "Neck": [((0, 0, 1), -14.0), ((1, 0, 0), -5.0)],
                })
    return lijst


def verloop_pro():
    log(f"Blender {bpy.app.version_string}, zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    try:
        bpy.context.preferences.system.viewport_aa = "OFF"
        for sc_ in bpy.data.scenes:
            sc_.display.viewport_aa = "OFF"
    except Exception as f:  # noqa: BLE001
        log(f"KORT viewport_aa {f}")
    ob, arm, p = figuur()
    naam = ob.name
    bpy.context.preferences.view.ui_scale = UI
    bpy.context.preferences.view.show_tooltips = False
    leeg_beeld()
    venster, g3 = gebied3d()
    ruimte = g3.spaces.active
    # gewone Blender: kop van de weergave, assenkruis rechtsboven, vloerraster, standaard donkergrijze achtergrond
    ruimte.show_region_header = True
    ruimte.show_region_toolbar = False
    ruimte.show_region_ui = False
    ruimte.show_gizmo_navigate = True
    ov = ruimte.overlay
    ov.show_floor = ov.show_axis_x = ov.show_axis_y = True
    ov.show_text = False
    ov.show_cursor = False
    ov.show_outline_selected = True
    sh = ruimte.shading
    sh.type = "SOLID"
    sh.light = "STUDIO"
    sh.color_type = "SINGLE"
    sh.single_color = GRIJS[:3]
    sh.background_type = "THEME"
    try:
        gr = bpy.context.preferences.themes[0].view_3d.space.gradients
        gr.background_type = "SINGLE_COLOR"
        gr.high_gradient = (0.188, 0.188, 0.188)
    except Exception as f:  # noqa: BLE001
        log(f"KORT thema {f}")
    ruimte.clip_start, ruimte.clip_end = 1.0, 20000.0
    ruimte.lens = 50.0
    arm.hide_set(False)
    geen_selectie()
    bpy.context.view_layer.objects.active = None
    midden = Vector((0.0, 0.0, 112.0))

    # afstand meten zodat de robot ±72% van de hoogte vult (twee keer bijstellen; deze beelden knipt de montage weg)
    D = 600.0
    for _ in range(3):
        zicht(g3, -50, 80.0, D, midden)
        herteken()
        yield 0.1
        h, hr = hoogte_px(g3, [ob])
        if h > 10:
            D = D * h / (0.80 * hr)
    log(f"KORT afstand {D:.0f}")
    film["metingen"]["afstand"] = round(D, 1)

    def camera(t):
        # doorlopend rustig rond: 7 graden per seconde, licht kantelen. v7b (Daan #217 M2): niet meer uitzoomen bij de
        # pose; de camera komt over de hele opname heel langzaam 8% dichterbij, zodat de robot het beeld blijft vullen.
        # v7c (Daan #228 K2): eerst zacht naar de zijkant (draai -85) zodat de knieboog als echte beweging van het
        # onderbeen te zien is (van voren klapte het onderbeen weg), dan rustig terug rond naar schuin rechts (55) voor
        # kleur en pose. Beeld 0 blijft gelijk aan v7 (draai -55, zelfde kantel en afstand).
        draai = -55.0 - 30.0 * zacht(t / 4.0) + 140.0 * zacht((t - 3.0) / 10.5)
        kantel = 81.0 - 5.0 * zacht(t / 13.0)
        d = D * (1.0 - 0.08 * zacht(t / 13.5))
        punt = midden + Vector((0.0, 0.0, 4.0 * zacht((t - 10.2) / 1.5)))   # bij de pose gaat de arm omhoog
        zicht(g3, draai, kantel, d, punt)

    T = {"t": 0.0}
    _vk = globals().get("_VK")

    def tik():
        camera(T["t"])
        T["t"] += 1.0 / FPS7
    if _vk is not None:
        _vk["elke"] = tik

    def tot(sec):
        """Laat de film lopen tot filmtijd sec (camera draait elke tik)."""
        while T["t"] < sec - 1e-6:
            yield 1.0 / FPS7

    def doe_tot(sec, f):
        t0 = T["t"]
        while T["t"] < sec - 1e-6:
            f((T["t"] - t0) / max(1e-6, sec - t0))
            yield 1.0 / FPS7
        f(1.0)

    deel("start")
    camera(0.0)
    yield from tot(0.6)

    # Figure from rig (de echte knop van Pro; blokkeert Blender, kost in de film 0 s)
    deel("knop")
    A["actief"](ob)
    tk = time.time()
    bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    film["metingen"]["gewrichten"] = len(lijst)
    film["metingen"]["regels"] = [fig.regel(r) for r in lijst]
    log(f"KORT {'OK' if len(lijst) >= 6 else 'FOUT'} knop {len(lijst)} gewrichten")
    geen_selectie()
    bpy.context.view_layer.objects.active = None
    # alleen de zichtbare delen: de add-on bewaart de tussenstappen van het snijden verborgen (proef 1)
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH" and o.visible_get()]
    film["metingen"]["delen"] = len(delen)
    sh.color_type = "RANDOM"
    yield from tot(1.3)

    deel("uitelkaar")
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = True
    yield from tot(2.1)
    inst.uit_elkaar = False
    yield from tot(2.4)

    # materialen: per deel een eigen kopie (voor deel voor deel kleur), eerst alles grijs
    for o in delen:
        o.rotation_mode = "QUATERNION"
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    echt = {}
    for o in delen:
        for i, m in enumerate(o.data.materials):
            if m is None:
                continue
            c = m.copy()
            o.data.materials[i] = c
            echt[c.name] = tuple(c.diffuse_color)
            c.diffuse_color = GRIJS
    deel("grijs_mat")
    sh.color_type = "MATERIAL"

    # knie tot de stop, voorbij de stop rood, terug
    # v7c: de rechterknie, want die staat aan de kant waar de camera nu kijkt (anders staat het andere been ervoor)
    a, b = paar("Right knee")
    if a is None or b is None:
        a, b = paar("Left knee")
    if a is not None and b is not None:
        stop = float(a["cj_bereik_graden"])
        film["metingen"]["knie_stop"] = stop
        s = math.floor(stop * 10) / 10
        deel("knie")
        # v7d (Daan #232 K1): het label "Right knee 0-120°" en "+N° past limit" van Pro anderhalf keer zo groot,
        # zodat ze op een telefoon leesbaar zijn. Alleen de tekstmaat van de echte overlay, verder niets.
        import sys as _sys
        _sb = [m for n, m in list(_sys.modules.items()) if n.endswith(".betaald.scharnier_boog")]
        _oud = [(m, m.FIGUUR_PX, m.ROOD_PX) for m in _sb]
        for m in _sb:
            m.FIGUUR_PX, m.ROOD_PX = int(m.FIGUUR_PX * 1.5), int(m.ROOD_PX * 1.5)
        log(f"KORT labels groter: {len(_sb)} module(s)")
        yield from tot(2.5)
        yield from doe_tot(3.6, lambda t: buig(b, s * zacht(t)))
        yield from tot(3.9)
        deel("knie_rood")
        yield from doe_tot(4.2, lambda t: buig(b, s + 15.0 * zacht(t)))
        film["metingen"]["knie_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
        log(f"KORT knie stop {stop} rood {film['metingen']['knie_rood_vlakken']}")
        # v7d (Daan #232 K2): rood 0,2 s langer vasthouden (tot 4,7 s), terug in 0,4 s; lengte blijft gelijk
        yield from tot(4.7)
        yield from doe_tot(5.1, lambda t: buig(b, (s + 15.0) * (1 - zacht(t))))
        buig(b, 0.0)
        for m, f_, r_ in _oud:
            m.FIGUUR_PX, m.ROOD_PX = f_, r_
    else:
        log("KORT FOUT knie: geen linkerknie")
    geen_selectie()
    bpy.context.view_layer.objects.active = None
    inst.toon_bereik = False   # proef 1: de waaier en "Right knee 0-120°" bleven anders tot het eind in beeld

    def scharnier(n, gr_):
        _a, bb = paar(n)
        if bb is not None:
            buig(bb, gr_)
            bpy.context.view_layer.update()

    # pose kiezen met de botsingscheck: in de rusthouding rakende paren (gewrichten) mogen, nieuwe niet;
    # onderarmen (deel B van de ellebogen) mogen niets raken behalve hun eigen bovenarm
    R.poseer(delen, {}, scharnier=scharnier)
    raakparen = maak_toets(delen)
    rust = raakparen()
    onder = [x for x in (paar("Left elbow")[1], paar("Right elbow")[1]) if x is not None]
    eigen = {x.name: (paar(x["cj_naam"])[0].name if paar(x["cj_naam"])[0] else "") for x in onder}
    beste, beste_n, uitslag = None, 99, []
    # v7b (Daan #217 M3): eerst de vaste open pose uit poses7.py (CJ_POSE), daarna de andere; de oude lijst alleen als
    # reserve. Dezelfde pose gaat naar de weergave en naar eind.blend (Cycles).
    eerst = os.environ.get("CJ_POSE", "g_zwaai_achter_loop")
    lijst = [POSES[eerst]] + [v for k, v in POSES.items() if k != eerst] + kandidaten()
    for i, kand in enumerate(lijst):
        R.poseer(delen, kand, scharnier=scharnier)
        nu = raakparen()
        nieuw = nu - rust
        arm_hits = [pr for pr in nu if any(n in pr for n in eigen) and not any(set(pr) == {k, v} for k, v in eigen.items())]
        n = len(nieuw) + len(arm_hits)
        uitslag.append({"nr": i, "nieuw": sorted(nieuw), "onderarm": sorted(arm_hits)})
        if n < beste_n:
            beste, beste_n = kand, n
        log(f"KORT pose kandidaat {i}: {n}")
        if n == 0:
            break
    film["metingen"]["pose_check"] = uitslag
    film["metingen"]["pose_botsingen"] = beste_n
    log(f"KORT pose gekozen met {beste_n} botsingen ({len(uitslag)} geprobeerd)")
    POSE = beste
    film["metingen"]["pose"] = {k: v for k, v in POSE.items()}
    film["metingen"]["pose_naam"] = next((k for k, v in POSES.items() if v is POSE), "reserve")
    R.poseer(delen, {}, scharnier=scharnier)
    geen_selectie()
    bpy.context.view_layer.objects.active = None

    # deel voor deel kleur (van de voeten naar het hoofd), elke ±0,3 s een deel
    volg = sorted(delen, key=lambda o: (o.matrix_world @ Vector(o.bound_box[0])).z + o.dimensions.z / 2)
    deel("kleur")
    t0, t1 = 5.2, 9.4
    for k, o in enumerate(volg):
        yield from tot(t0 + (t1 - t0) * k / max(1, len(volg)))
        for m in o.data.materials:
            if m is not None and m.name in echt:
                m.diffuse_color = echt[m.name]
    for o in delen:
        for m in o.data.materials:
            if m is not None and m.name in echt:
                m.diffuse_color = echt[m.name]
    yield from tot(9.6)
    deel("schaduw")
    sh.show_shadows = True
    sh.show_cavity = True
    ov.show_floor = True
    yield from tot(10.2)

    # pose: van rechtop naar de gekozen pose
    deel("pose")
    rood_max = {"n": 0}

    def zet(t):
        R.poseer(delen, schaal_pose(POSE, zacht(t)), scharnier=scharnier)
        geen_selectie()
        bpy.context.view_layer.objects.active = None   # proef 2: anders tekent Pro de waaier van de laatste knie
        rood_max["n"] = max(rood_max["n"], sum(len(o.get("cj_rood_vlakken", [])) // 2 for o in delen))
    yield from doe_tot(11.7, zet)
    film["metingen"]["pose_rood_vlakken"] = rood_max["n"]
    log(f"KORT pose rood {rood_max['n']}")
    yield from tot(13.5)
    deel("eind_weergave")
    if _vk is not None:
        _vk["elke"] = None
    log("KORT OK weergave")

    # eind.blend: Cycles-film, camera vliegt langzaam om de geposeerde robot, hele figuur met lucht erom
    sc = bpy.context.scene
    for o in delen:
        o.animation_data_clear()
    S.bouw(220.0)
    cam_ob = S.camera()
    cam_ob.rotation_mode = "XYZ"
    n = int(EIND_SEC * 30)
    sc.frame_start, sc.frame_end = 1, n
    sc.render.fps = 30
    # proef 1 (GEZIEN): matrix_world is pas na een update bijgewerkt, dus de sleutels stonden alle op 0 (camera in de
    # wand). Daarom location en rotatie zelf overnemen.
    # v7b (Daan #217 K1): meer draai, 60 graden over de eindfilm, aan dezelfde kant als waar de weergave eindigt
    # (draai ±57 graden), van schuin rechts van de robot naar voren
    S.richt(cam_ob, delen, "staand", draai=62, kantel=6, vul=0.82, midden_y=0.52)
    l0, q0 = cam_ob.location.copy(), cam_ob.rotation_euler.to_quaternion()
    S.richt(cam_ob, delen, "staand", draai=2, kantel=9, vul=0.84, midden_y=0.52)
    l1, q1 = cam_ob.location.copy(), cam_ob.rotation_euler.to_quaternion()
    film["metingen"]["eind_camera"] = [list(l0), list(l1)]
    cam_ob.rotation_mode = "QUATERNION"
    for f in range(1, n + 1, 6):
        t = zacht((f - 1) / (n - 1))
        cam_ob.location = l0.lerp(l1, t)
        cam_ob.rotation_quaternion = q0.slerp(q1, t)
        cam_ob.keyframe_insert("location", frame=f)
        cam_ob.keyframe_insert("rotation_quaternion", frame=f)
    sc.render.image_settings.file_format = "PNG"
    sc.render.filepath = "//e_"
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = int(os.environ.get("CJ_EIND_SAMPLES", "40"))
    sc.cycles.use_denoising = True
    sc.render.use_persistent_data = True
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1080, 1920, 100
    for o in bpy.data.objects:   # v7b: verborgen tussenstappen van het snijden ook uit de render (zie eind_fix.py)
        if o.type == "MESH" and not o.visible_get():
            o.hide_render = True
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(scherm_basis.uitmap, "eind.blend"), copy=True)
    log(f"KORT OK eind {n} beelden (eind.blend)")
