# Verloop v8 van de sale-Short (issue #159, Regisseur 27 nov 2026). Komt in proces8.py ná verloop7.py, dus de hulpjes
# van v7 (zicht, hoogte_px, maak_toets, schaal_pose, POSES) blijven en alleen verloop_pro is nieuw.
# Thijs 27 nov 11:15 en 11:25: "voelt te sloom", "het moet echt lijken alsof iemand zelf snel met de muis dit doet".
# Dus anders dan v7: het N-paneel van Click Joints Pro staat rechts in beeld, de echte muis (xdotool) gaat snel naar
# de echte knoppen en klikt (Figure from rig, Exploded view, het onderbeen, de Bend-schuif), en de weergave draait niet
# meer door het script maar doordat de muis echt sleept met de middelste knop (Blender draait zelf, view3d.rotate).
# Kleur deel voor deel en de pose zet het script, terwijl de muis de weergave rond sleept (zoals v7, maar sneller).
# De muispijl zelf staat niet in een X-schermafbeelding; muis.txt bewaart per beeld de echte plek en de montage tekent
# daar de pijl, zoals elke schermrecorder doet.
CJ8_LAAG = os.environ.get("CJ_PROEF8", "") == "laag"


def verloop_pro():
    log(f"Blender {bpy.app.version_string}, zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    pr = bpy.context.preferences
    try:
        pr.system.viewport_aa = "OFF"
    except Exception as f:  # noqa: BLE001
        log(f"KORT viewport_aa {f}")
    pr.inputs.use_mouse_continuous = False      # anders verstopt en verplaatst Blender de muis tijdens het draaien
    pr.inputs.use_rotate_around_active = False
    pr.inputs.use_auto_perspective = False
    pr.system.use_region_overlap = False        # paneel naast de weergave, de robot staat midden in de weergave
    ob, arm, p = figuur()
    naam = ob.name
    pr.view.ui_scale = UI
    pr.view.show_tooltips = False
    leeg_beeld()
    venster, g3 = gebied3d()
    ruimte = g3.spaces.active
    ruimte.show_region_header = True
    ruimte.show_region_toolbar = False
    ruimte.show_region_ui = True
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
        gr = pr.themes[0].view_3d.space.gradients
        gr.background_type = "SINGLE_COLOR"
        gr.high_gradient = (0.188, 0.188, 0.188)
    except Exception as f:  # noqa: BLE001
        log(f"KORT thema {f}")
    ruimte.clip_start, ruimte.clip_end = 1.0, 20000.0
    ruimte.lens = 50.0
    for _ in range(16):
        if wiel_naar_tabblad():
            break
        yield 0.2
    arm.hide_set(False)
    geen_selectie()
    A["actief"](ob)                      # de robot is gekozen (oranje rand), zoals vóór de opname
    midden = Vector((0.0, 0.0, 134.0))   # robot iets onder het midden: de hook staat bovenin
    D = 600.0
    for _ in range(3):
        zicht(g3, -40, 80.0, D, midden)
        herteken()
        yield 0.1
        h, hr = hoogte_px(g3, [ob])
        if h > 10:
            D = D * h / (0.71 * hr)
    zicht(g3, -40, 80.0, D, midden)
    film["metingen"]["afstand"] = round(D, 1)
    yield 0.3

    def vind(tekst, keer=3):
        for _ in range(keer):
            herteken()
            r = ocr(tekst)
            if r:
                return r
            yield 0.1
        return None

    knop = yield from vind("Figure from rig")
    if knop is None:                     # 1.2.8: het blok staat onder het hoofdpaneel; hoofdpaneel inklappen
        kop = ocr("Click Joints")
        if kop:
            xdo("mousemove", str(kop[0]), str(kop[1]))
            yield 0.1
            xdo("click", "1")
            yield 0.4
        knop = yield from vind("Figure from rig")
    film["metingen"]["knop_ocr"] = knop
    wv = rect("WINDOW")
    ui = rect("UI")
    film["metingen"]["weergave"] = wv
    film["metingen"]["paneel"] = ui
    log(f"KORT paneel {ui} weergave {wv} knop {knop}")
    if CJ8_LAAG:
        subprocess.run(["import", "-window", "root", os.path.join(scherm_basis.uitmap, "laag.png")])
        log("KORT laag klaar")
        return
    if knop is None:
        knop = (ui[0] + ui[2] // 2, ui[1] + 200)

    rust = (wv[0] + int(wv[2] * 0.62), wv[1] + int(wv[3] * 0.58))
    xdo("mousemove", str(rust[0]), str(rust[1]))
    MUIS["x"], MUIS["y"] = rust
    T = {"t": 0.0}
    _vk = globals().get("_VK")

    def tik():
        T["t"] += 1.0 / FPS7
    if _vk is not None:
        _vk["elke"] = tik

    def tot(sec):
        while T["t"] < sec - 1e-6:
            yield 1.0 / FPS7

    def naar(x, y, duur):
        g = _glij(x, y, duur, 0.8)
        n = max(1, int(round(duur * FPS7)))
        for _ in range(n):
            yield 1.0 / FPS7
        g.wait()
        MUIS["x"], MUIS["y"] = int(x), int(y)

    def klik8():
        xdo("click", "1")
        film["kliks"].append(round(T["t"], 3))

    def sleep_draai(dx, dy, duur, tijdens=None):
        """Echte sleep met de middelste muisknop in de weergave: Blender draait zelf rond (turntable)."""
        x0, y0 = MUIS["x"], MUIS["y"]
        xdo("mousedown", "2")
        yield 1.0 / FPS7
        n = max(2, int(round(duur * FPS7)))
        t0 = T["t"]
        for i in range(1, n + 1):
            e = zacht(i / n)
            xdo("mousemove", str(int(x0 + dx * e)), str(int(y0 + dy * e)))
            if tijdens is not None:
                tijdens(T["t"] - t0)
            yield 1.0 / FPS7
        xdo("mouseup", "2")
        MUIS["x"], MUIS["y"] = int(x0 + dx), int(y0 + dy)
        yield 1.0 / FPS7

    def draai_nu():
        rv = g3.spaces.active.region_3d
        return round(math.degrees(rv.view_rotation.to_euler().z), 1)

    deel("start")
    yield from tot(0.15)
    # 1. Figure from rig: muis snel naar de knop, echte klik
    yield from naar(knop[0], knop[1], 0.42)
    yield from tot(0.62)
    klik8()
    yield 1.0 / FPS7
    for _ in range(60):
        if any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects):
            break
        yield 1.0 / FPS7
    deel("knop")
    vangnet = []
    if not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects):
        vangnet.append("knop")
        log("KORT vangnet knop: Figure from rig via script")
        A["actief"](ob)
        bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    film["metingen"]["gewrichten"] = len(lijst)
    log(f"KORT {'OK' if len(lijst) >= 6 else 'FOUT'} knop {len(lijst)} gewrichten")
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH" and o.visible_get()]
    film["metingen"]["delen"] = len(delen)
    sh.color_type = "RANDOM"
    geen_selectie()
    bpy.context.view_layer.objects.active = max(delen, key=lambda o: len(o.data.vertices))
    # 2. de muis terug de weergave in en echt rond slepen
    yield from naar(rust[0] - 120, rust[1] + 40, 0.28)
    d0 = draai_nu()
    yield from sleep_draai(230, -18, 0.75)
    film["metingen"]["draai_1"] = [d0, draai_nu()]
    log(f"KORT draai 1: {d0} naar {draai_nu()}")
    # 3. Exploded view aan, even rond, weer uit
    ex = ocr("Exploded view")
    film["metingen"]["exploded_ocr"] = ex
    if ex is None:
        ex = (ui[0] + 120, ui[1] + 400)
    yield from naar(ex[0] - 40, ex[1], 0.36)
    inst = bpy.context.scene.click_joints
    klik8()
    yield 1.0 / FPS7
    yield 1.0 / FPS7
    if not inst.uit_elkaar:
        vangnet.append("exploded")
        inst.uit_elkaar = True
    yield from naar(rust[0] + 60, rust[1] - 60, 0.3)
    # v8c (Daan #269 M1): CJ_DX2 kiest de hoek waaronder de knie straks buigt (v8b: -150, been zwaait naar links)
    yield from sleep_draai(int(os.environ.get("CJ_DX2", "-300")), 10, 0.6)
    yield from naar(ex[0] - 40, ex[1], 0.3)
    klik8()
    yield 1.0 / FPS7
    yield 1.0 / FPS7
    if inst.uit_elkaar:
        vangnet.append("exploded_uit")
        inst.uit_elkaar = False

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
    sh.color_type = "MATERIAL"

    # 4. knie: klik op het rechteronderbeen, dan de Bend-schuif echt slepen tot voorbij de stop (rood) en terug
    eerst_knie = os.environ.get("CJ8_KNIE", "Left knee")   # v8c: welke knie (vanaf voren ligt de linker vrij van de rand)
    a, b = paar(eerst_knie)
    if a is None or b is None:
        a, b = paar("Left knee" if eerst_knie == "Right knee" else "Right knee")
    stop = float(a["cj_bereik_graden"]) if a is not None else 120.0
    film["metingen"]["knie_stop"] = stop
    deel("knie")
    # v8c (Daan #269 M1): het label "Right knee" stond op x 19 van 1080. Zoals iemand dat zelf doet: de weergave met
    # Shift en de middelste muisknop echt 140 px naar rechts schuiven (bij 80 stond de rode pil "+N° past limit" nog op x 8) (Blender schuift zelf, view3d.move).
    PAN = int(os.environ.get("CJ_PAN", "0"))

    def schuif_weergave(dx):
        x0, y0 = MUIS["x"], MUIS["y"]
        xdo("keydown", "shift")
        xdo("mousedown", "2")
        yield 1.0 / FPS7
        n = 9
        for i in range(1, n + 1):
            xdo("mousemove", str(int(x0 + dx * zacht(i / n))), str(y0))
            yield 1.0 / FPS7
        xdo("mouseup", "2")
        xdo("keyup", "shift")
        MUIS["x"], MUIS["y"] = x0 + dx, y0
        yield 1.0 / FPS7
    if PAN:
        yield from naar(rust[0] - 150, rust[1] + 120, 0.26)
        yield from schuif_weergave(PAN)
        film["metingen"]["pan_px"] = PAN
    if b is not None:
        bb = [b.matrix_world @ Vector(c) for c in b.bound_box]
        mid = sum(bb, Vector()) / 8.0
        pt = scherm_punt(mid)
        if pt is not None:
            yield from naar(pt[0], pt[1], 0.34)
            geen_selectie()
            klik8()
            yield 1.0 / FPS7
            yield 1.0 / FPS7
        if bpy.context.view_layer.objects.active is not b:
            vangnet.append("onderbeen")
            geen_selectie()
            b.select_set(True)
            bpy.context.view_layer.objects.active = b
        yield 1.0 / FPS7
        wm = bpy.context.window_manager
        schuif = None
        for _ in range(3):
            herteken()
            yield 1.0 / FPS7
            schuif = ocr("Bend")
            if schuif:
                break
        film["metingen"]["bend_ocr"] = schuif
        log(f"KORT bend {schuif}")
        gesleept = False
        if schuif is not None:
            sx = schuif[0] + 30
            yield from naar(sx, schuif[1], 0.32)
            xdo("mousedown", "1")
            film["kliks"].append(round(T["t"], 3))
            yield 1.0 / FPS7
            rechts = ui[0] + ui[2] - 20
            x = sx
            # eerst tot de stop, dan voorbij (rood): de muis gaat rechts tot de waarde er is
            for doel in (stop - 0.5, stop + 15.0):
                k = 0
                while float(wm.cj_scharnier_pose) < doel and k < 40:
                    x = min(rechts + 400, x + 9)
                    xdo("mousemove", str(int(x)), str(schuif[1]))
                    k += 1
                    yield 1.0 / FPS7
                if doel < stop:
                    film["metingen"]["knie_bij_stop"] = round(float(wm.cj_scharnier_pose), 1)
                    for _ in range(5):
                        yield 1.0 / FPS7
            film["metingen"]["knie_rood"] = round(float(wm.cj_scharnier_pose), 1)
            film["metingen"]["knie_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
            deel("knie_rood")
            for _ in range(12):
                yield 1.0 / FPS7
            k = 0
            while float(wm.cj_scharnier_pose) > 0.5 and k < 40:
                x -= 14
                xdo("mousemove", str(int(x)), str(schuif[1]))
                k += 1
                yield 1.0 / FPS7
            xdo("mouseup", "1")
            MUIS["x"], MUIS["y"] = int(x), schuif[1]
            gesleept = film["metingen"]["knie_rood"] > stop
            log(f"KORT knie sleep: stop {stop}, bij stop {film['metingen'].get('knie_bij_stop')}, "
                f"rood {film['metingen']['knie_rood']} ({film['metingen']['knie_rood_vlakken']} vlakken), terug "
                f"{float(wm.cj_scharnier_pose):.1f}")
        if not gesleept:
            vangnet.append("knie")
            log("KORT vangnet knie: script buigt")
            s = math.floor(stop * 10) / 10
            for i in range(1, 16):
                buig(b, (s + 15.0) * zacht(i / 15))
                yield 1.0 / FPS7
            for i in range(1, 10):
                buig(b, (s + 15.0) * (1 - zacht(i / 9)))
                yield 1.0 / FPS7
        buig(b, 0.0)
    inst.toon_bereik = False
    if PAN:   # terugschuiven, anders draait de weergave straks om een punt naast de robot (arm uit beeld)
        yield from naar(rust[0] - 100, rust[1] + 120, 0.26)
        yield from schuif_weergave(-PAN)

    # pose kiezen met de botsingscheck (zoals v7: vaste pose g_zwaai_achter_loop eerst)
    def scharnier(n, gr_):
        _a, bb_ = paar(n)
        if bb_ is not None:
            buig(bb_, gr_)
            bpy.context.view_layer.update()
    R.poseer(delen, {}, scharnier=scharnier)
    raakparen = maak_toets(delen)
    rust_p = raakparen()
    eerst = os.environ.get("CJ_POSE", "g_zwaai_achter_loop")
    lijst_p = [POSES[eerst]] + [v for k, v in POSES.items() if k != eerst] + kandidaten()
    beste, beste_n = None, 99
    for i, kand in enumerate(lijst_p):
        R.poseer(delen, kand, scharnier=scharnier)
        n = len(raakparen() - rust_p)
        if n < beste_n:
            beste, beste_n = kand, n
        if n == 0:
            break
    film["metingen"]["pose_botsingen"] = beste_n
    film["metingen"]["pose_naam"] = next((k for k, v in POSES.items() if v is beste), "reserve")
    log(f"KORT pose {film['metingen']['pose_naam']} met {beste_n} botsingen")
    POSE = beste
    R.poseer(delen, {}, scharnier=scharnier)
    geen_selectie()
    bpy.context.view_layer.objects.active = None

    # 5. muis terug de weergave in; terwijl hij rond sleept krijgt de robot deel voor deel kleur, schaduw, dan de pose
    volg = sorted(delen, key=lambda o: (o.matrix_world @ Vector(o.bound_box[0])).z + o.dimensions.z / 2)
    yield from naar(rust[0] - 160, rust[1] + 80, 0.3)
    deel("kleur")
    gekleurd = {"n": 0}

    def kleur(t):
        k = int(min(len(volg), t / 1.5 * len(volg) + 1))
        while gekleurd["n"] < k:
            o = volg[gekleurd["n"]]
            for m in o.data.materials:
                if m is not None and m.name in echt:
                    m.diffuse_color = echt[m.name]
            gekleurd["n"] += 1
        if t > 1.5:
            sh.show_shadows = True
            sh.show_cavity = True
    # v8c: 150 px extra, zodat de weergave na de kleur weer op dezelfde hoek uitkomt als v8b (CJ_DX2 draaide 150 px minder)
    yield from sleep_draai(int(os.environ.get("CJ_DX3", "450")), -10, 1.7, tijdens=kleur)
    kleur(9.0)
    deel("pose")
    rood_max = {"n": 0}

    def zet(t):
        R.poseer(delen, schaal_pose(POSE, zacht(min(1.0, t / 1.0))), scharnier=scharnier)
        geen_selectie()
        bpy.context.view_layer.objects.active = None
        rood_max["n"] = max(rood_max["n"], sum(len(o.get("cj_rood_vlakken", [])) // 2 for o in delen))
    yield from naar(rust[0] - 200, rust[1] + 20, 0.25)
    yield from sleep_draai(260, -14, 1.3, tijdens=zet)
    zet(9.0)
    film["metingen"]["pose_rood_vlakken"] = rood_max["n"]
    yield from naar(rust[0] + 80, rust[1] - 140, 0.4)
    yield from tot(T["t"] + 0.4)
    film["metingen"]["vangnet"] = vangnet
    film["metingen"]["draai_eind"] = draai_nu()
    film["metingen"]["weergave_sec"] = round(T["t"], 2)
    deel("eind_weergave")
    if _vk is not None:
        _vk["elke"] = None
    log(f"KORT OK weergave {T['t']:.2f} s, vangnet {vangnet}")
