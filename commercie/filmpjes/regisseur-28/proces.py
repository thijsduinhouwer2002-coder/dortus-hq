"""Echte schermopname voor de sale-Short in procesvorm (issue #159, Regisseur 26 nov 2026).

Thijs 26 nov 09:00: "letterlijk zo'n filmpje exact namaken, maar dan met onze robot" (voorbeeld: de procesvideo van
@simonzhang.art, 26 s, elke ±0,7 s een nieuwe stap, van grijs model naar mooie render). Dit script speelt de gebruiker
in de echte Blender 5.3.0 met interface (Xvfb, ffmpeg x11grab neemt op, zie ../regisseur-26/neem_op.sh). Het neemt
alle helpers over van de opname van regisseur-26 (echte muis die glijdt, OCR op knoppen, echte kliks) en vervangt
alleen het verloop door de stappen van het voorbeeld:
  grijs      grijze robot (Solid, één kleur), camera draait mee, muis beweegt al
  rig        het skelet verschijnt
  kies/knop  echte klik op de robot, echte klik op Figure from rig (wachten knipt de montage weg)
  uitelkaar  echte klik op Exploded view, dicht op schouder en heup (kogel in kom), weer dicht
  knie       echte klik op het onderbeen, Bend tot de stop, voorbij de stop rood, terug
  kleur      studio en kleuren: Material Preview met lampen, shader-editor eronder, muis op de nodes
  tijdlijn   tijdlijn eronder, echte sleep van de afspeelkop: de robot loopt door drie poses (sleutelbeelden)
  licht      lamp feller en warmer (de muis sleept in de shader-editor op Roughness als OCR hem vindt)
  render     echte klik op het menu Render, dan Render Animation (2 beelden), resultaat op het scherm, Esc
  eind       daarna (niet in de opname): de eindfilm door de studiocamera, Viewport Render Animation (EEVEE),
             1080x1920, 7 s, langzame camera rond de robot in heldenpose (map eind/)
Elk deel staat met zijn wandkloktijd in film.json ("delen"), zodat de montage de stukken kan knippen.
    blender --gpu-backend opengl start.blend --python proces.py -- <map> <betaalde zip>"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
R26 = os.path.abspath(os.path.join(HIER, "..", "regisseur-26", "echt_opname.py"))
STUDIO = os.path.abspath(os.path.join(HIER, "..", "studio"))
r26 = open(R26, encoding="utf-8").read()

VERLOOP = r'''
import random as _rnd
_rnd.seed(28)
EIND_SEC = float(os.environ.get("CJ_EIND_SEC", "7.0"))
POSE2 = {
    "Right hip": [((1, 0, 0), -20.0)], "Right knee": 70.0,
    "Left hip": [((1, 0, 0), 8.0)], "Left knee": 15.0,
    "Left shoulder": [((1, 0, 0), 25.0)], "Left elbow": 60.0,
    "Right shoulder": [((1, 0, 0), -25.0)], "Right elbow": 110.0,
    "Neck": [((0, 0, 1), 15.0)],
}


def drijf(sec, vak=None):
    """De hand rust nooit: kleine rustige bewegingen binnen vak [x, y, b, h] (standaard de 3D-weergave)."""
    t_eind = time.time() + sec
    vak = vak or rect("WINDOW")
    while time.time() < t_eind - 0.3:
        x = min(max(MUIS["x"] + _rnd.randint(-160, 160), vak[0] + 60), vak[0] + min(vak[2], 1080) - 60)
        y = min(max(MUIS["y"] + _rnd.randint(-120, 120), vak[1] + 80), vak[1] + vak[3] - 80)
        yield from muis_naar(x, y, duur=_rnd.uniform(0.6, 1.0))
        yield _rnd.uniform(0.1, 0.35)


def gebied3d():
    for venster in bpy.context.window_manager.windows:
        for g in venster.screen.areas:
            if g.type == "VIEW_3D":
                return venster, g
    return None, None


def onder_gebied(soort, ui_type=None, deel_=0.36):
    """Splits de 3D-weergave (echte Blender-indeling): onderin een editor van `soort`. Geeft het nieuwe gebied."""
    venster, g = gebied3d()
    voor = set(a.as_pointer() for a in venster.screen.areas)
    regio = next(r for r in g.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=g, region=regio):
        bpy.ops.screen.area_split(direction="HORIZONTAL", factor=deel_)
    nieuw = [a for a in venster.screen.areas if a.as_pointer() not in voor]
    if not nieuw:
        return None
    # het onderste van de twee wordt de nieuwe editor
    paar_ = [a for a in venster.screen.areas if a.type == "VIEW_3D"]
    onder = min(paar_, key=lambda a: a.y)
    onder.type = soort
    if ui_type:
        onder.ui_type = ui_type
    return onder


def gebied_rect(g):
    venster = bpy.context.window_manager.windows[0]
    return [venster.x + g.x, venster.y + venster.height - (g.y + g.height), g.width, g.height]


def sleutels(delen, frame):
    for o in delen:
        o.keyframe_insert("location", frame=frame)
        o.keyframe_insert("rotation_quaternion", frame=frame)


def verloop_pro():
    log(f"Blender {bpy.app.version_string}, zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    ob, arm, p = figuur()
    naam = ob.name
    SM["rustig"]()
    leeg_beeld()
    bpy.context.preferences.view.ui_scale = UI
    bpy.context.preferences.system.use_region_overlap = False
    bpy.context.preferences.view.show_tooltips = False
    bpy.context.preferences.view.render_display_type = "SCREEN"
    kijk_breed()
    venster, g3 = gebied3d()
    ruimte = g3.spaces.active
    ruimte.shading.color_type = "SINGLE"          # grijs model, zoals het begin van het voorbeeld
    ruimte.shading.single_color = (0.62, 0.62, 0.64)
    ruimte.overlay.show_floor = True
    arm.hide_set(True)
    SM["open_paneel"]()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    yield 0.5
    yield from sleep_zijbalk(BREED_ZIJBALK)
    yield 1.0
    MUIS["x"], MUIS["y"] = 700, 1200
    xdo("mousemove", "700", "1200")
    kop = ocr("Click Joints")
    if kop:   # hoofdpaneel dicht: Figure joints met de knop staat dan bovenaan
        xdo("mousemove", str(kop[0]), str(kop[1]))
        time.sleep(0.2)
        xdo("click", "1")
        time.sleep(0.2)
        xdo("mousemove", "700", "1200")
    yield 0.8
    heel = (0.0, 0.0, 112.0)
    D = 330.0
    cam(-60, 84.0, D, heel)
    yield 0.8
    meet_schaal(heel, D)
    cam(-60, 84.0, D, heel)
    yield 0.5

    # grijs: camera draait in één beweging mee, de muis loopt al
    deel("grijs")
    w = rect("WINDOW")
    _rnd.seed(1)
    doelen = [(w[0] + 520, w[1] + 700), (w[0] + 300, w[1] + 1000), (w[0] + 640, w[1] + 900)]
    t0 = time.time()
    duur = 6.0

    def draai():
        t = min(1.0, (time.time() - t0) / duur)
        cam(-60 + 75 * zacht(t), 84.0 - 4 * zacht(t), D - 40 * zacht(t), heel)
    for x, y in doelen:
        yield from muis_naar(x, y, duur=1.2, doe=lambda _t: draai())
    while time.time() - t0 < duur:
        draai()
        yield 0.001
    log("KORT OK grijs")

    # rig: het skelet verschijnt (zoals een gebruiker het oogje aanzet), muis wijst naar de heup
    deel("rig")
    arm.hide_set(False)
    herteken()
    heup = scherm_punt((0.0, -5.0, p["pelvis"].z))
    if heup:
        yield from muis_naar(heup[0] + 30, heup[1], duur=0.8)
    yield from drijf(2.0)
    log("KORT OK rig")

    # kies: echte klik op de robot
    deel("kies")
    arm.hide_select = True
    geen_selectie()
    bpy.context.view_layer.objects.active = None
    buik = scherm_punt((9.0, -8.0, 128.0))
    yield from muis_naar(buik[0], buik[1], duur=0.7)
    klik()
    for _ in range(5):
        yield 0.2
        if bpy.context.view_layer.objects.active == ob:
            break
    if bpy.context.view_layer.objects.active != ob:
        log("KORT vangnet kies: figuur via script actief")
        A["actief"](ob)
    yield 0.6

    # knop: echte klik op Figure from rig
    deel("knop")
    knop = yield from zoek("Figure from rig")
    film["metingen"]["knop_ocr"] = knop
    if knop is None:
        knop = (rect("UI")[0] + rect("UI")[2] // 2, rect("UI")[1] + 160)
    yield from muis_naar(knop[0], knop[1], duur=0.8)
    yield 0.3
    klik()
    yield 0.5
    t0 = time.time()
    while not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects) and time.time() - t0 < 240:
        yield 0.5
    if not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects):
        log("KORT vangnet knop: Figure from rig via script")
        A["actief"](ob)
        bpy.ops.click_joints.figuur_uit_rig()
    deel("knop_klaar")
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    film["metingen"]["gewrichten"] = len(lijst)
    film["metingen"]["regels"] = [fig.regel(r) for r in lijst]
    log(f"KORT knop {len(lijst)} gewrichten")
    geen_selectie()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH"]
    bpy.context.view_layer.objects.active = max(delen, key=lambda o: len(o.data.vertices))
    yield 0.5
    yield from stuk(45, lambda t: cam(15 - 30 * t, 84.0, D - 40, heel))
    log(f"KORT {'OK' if len(lijst) >= 6 else 'FOUT'} knop")

    # uitelkaar: echte klik op Exploded view, dichtbij schouder (kogel in kom) en heup, weer dicht
    deel("uitelkaar")
    inst = bpy.context.scene.click_joints
    ex = yield from zoek("Exploded view")
    if ex:
        yield from muis_naar(ex[0], ex[1], duur=0.7)
        klik()
        yield 0.5
    if not inst.uit_elkaar:
        log("KORT vangnet uitelkaar: Exploded view via script")
        inst.uit_elkaar = True
        herteken()
    deel("uitelkaar_aan")
    w = rect("WINDOW")
    sch = p["l-shoulder"] + (p["l-elbow"] - p["l-shoulder"]) * 0.3
    hp = p["l-upper-leg"]
    D2 = D - 40
    yield from muis_naar(w[0] + 700, w[1] + 1100, duur=0.6)
    yield from stuk(36, lambda t: cam(-15 + 35 * t, 84.0 + 2 * t, D2 + (90.0 - D2) * t, mengen(heel, sch, t)))
    deel("schouder")
    yield from stuk(45, lambda t: cam(20 + 25 * t, 86.0, 90.0, sch))
    yield from stuk(30, lambda t: cam(45, 86.0 - 6 * t, 90.0 + 10 * t, mengen(sch, hp, t)))
    deel("heup")
    yield from stuk(40, lambda t: cam(45 - 25 * t, 80.0, 100.0, hp))
    yield from stuk(30, lambda t: cam(20 - 35 * t, 80.0 + 4 * t, 100.0 + (D2 - 100.0) * t, mengen(hp, heel, t)))
    ex = yield from zoek("Exploded view")
    if ex:
        yield from muis_naar(ex[0], ex[1], duur=0.7)
        klik()
        yield 0.5
    if inst.uit_elkaar:
        inst.uit_elkaar = False
        herteken()
    log("KORT OK uitelkaar")

    # knie: klik op het linkeronderbeen, hoofdpaneel open, Bend tot de stop, voorbij (rood), terug
    a, b = paar("Left knee")
    if a is not None and b is not None:
        stop = float(a["cj_bereik_graden"])
        film["metingen"]["knie_stop"] = stop
        k = p["l-knee"]
        blik = (k.x, k.y, k.z + 5.0)
        yield from stuk(30, lambda t: cam(-15 + 85 * t, 84.0, D2 + (165.0 - D2) * t, mengen(heel, blik, t)))
        deel("knie")
        onder = scherm_punt((p["l-knee"] + p["l-ankle"]) / 2)
        yield from muis_naar(onder[0], onder[1], duur=0.7)
        klik()
        yield 0.3
        geen_selectie()
        b.select_set(True)
        buig(b, 0.0)
        bpy.context.view_layer.objects.active = b
        yield 0.4
        kop = ocr("Click Joints")
        if kop:
            yield from muis_naar(kop[0], kop[1], duur=0.6)
            klik()
            yield 1.0
        schuif = yield from zoek("Bend")
        film["metingen"]["bend_ocr"] = schuif
        wm = bpy.context.window_manager
        z = rect("UI")
        links, midden = z[0] + 70, z[0] + z[2] // 2
        y_s = schuif[1] if schuif else z[1] + 400
        yield from muis_naar(links, y_s, duur=0.6)
        s = math.floor(stop * 10) / 10
        deel("knie_buig")
        yield from sleep_schuif(links + s * 0.5 * (z[2] - 140) / 150.0, 1.1)
        v2 = yield from typ_waarde(s, midden)
        if abs(float(wm.cj_scharnier_pose) - s) > 1.0:
            log("KORT vangnet schuif: script zet de stand")
            buig(b, s)
        deel("knie_stop")
        yield 0.9
        deel("knie_rood")
        yield from typ_waarde(round(stop + 15.0), midden)
        film["metingen"]["knie_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
        yield 1.2
        yield from typ_waarde(0, midden)
        log(f"KORT knie stop {stop} rood {film['metingen']['knie_rood_vlakken']}")
        kop = ocr("Click Joints")
        if kop:
            yield from muis_naar(kop[0], kop[1], duur=0.6)
            klik()
            yield 0.5
    else:
        log("KORT FOUT knie: geen linkerknie")

    # kleur: studio, kleuren en plastic (Material Preview met de lampen van de studio), shader-editor eronder
    geen_selectie()
    for o in delen:
        o.rotation_mode = "QUATERNION"
    R.kleur_herstel(delen)
    S.bouw(220.0)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)

    def scharnier(n, gr):
        _a, bb = paar(n)
        if bb is not None:
            buig(bb, gr)
            bpy.context.view_layer.update()
    sc = bpy.context.scene
    R.poseer(delen, {}, scharnier=scharnier)
    sleutels(delen, 1)
    R.poseer(delen, R.HELD, scharnier=scharnier)
    sleutels(delen, 40)
    R.poseer(delen, POSE2, scharnier=scharnier)
    sleutels(delen, 80)
    R.poseer(delen, R.HELD, scharnier=scharnier)
    sleutels(delen, 120)
    sc.frame_start, sc.frame_end = 1, 120
    sc.frame_set(1)
    cam_ob = S.camera()
    S.richt(cam_ob, delen, "staand", draai=-32, kantel=7, vul=0.74, midden_y=0.56)
    yield 0.5
    sc.frame_set(1)
    venster, g3 = gebied3d()
    ruimte = g3.spaces.active
    ruimte.shading.type = "MATERIAL"
    ruimte.shading.use_scene_world = True
    ruimte.shading.use_scene_lights = True
    ruimte.overlay.show_floor = False
    ruimte.overlay.show_axis_x = ruimte.overlay.show_axis_y = False
    ruimte.overlay.show_extras = False
    D3 = 300.0
    cam(-20, 84.0, D3, heel)
    yield 1.0
    deel("kleur")
    ne = onder_gebied("NODE_EDITOR", "ShaderNodeTree", 0.34)
    romp = max(delen, key=lambda o: len(o.data.vertices))
    bpy.context.view_layer.objects.active = romp
    romp.select_set(True)
    yield 0.6
    if ne is not None:
        with bpy.context.temp_override(window=venster, area=ne, region=next(r for r in ne.regions if r.type == "WINDOW")):
            try:
                bpy.ops.node.view_all()
            except Exception as f:  # noqa: BLE001
                log(f"KORT view_all {f}")
        nr = gebied_rect(ne)
        film["vlakken"]["nodes"] = nr
        yield 0.5
        yield from muis_naar(nr[0] + 300, nr[1] + nr[3] // 2, duur=0.8)
        yield from drijf(1.5, nr)
    yield from stuk(45, lambda t: cam(-20 + 30 * t, 84.0, D3, heel))
    log("KORT OK kleur")

    # licht: Roughness slepen als OCR hem vindt, lamp feller en warmer
    deel("licht")
    lampen = [o for o in sc.objects if o.type == "LIGHT"]
    kracht = {o.name: o.data.energy for o in lampen}
    if ne is not None:
        rv = ocr("Roughness", gebied_rect(ne))
        film["metingen"]["roughness_ocr"] = rv
        if rv:
            yield from muis_naar(rv[0], rv[1], duur=0.6)
            yield from sleep_schuif(rv[0] - 60, 0.8)

    def licht(t):
        for o in lampen:
            o.data.energy = kracht[o.name] * (0.55 + 0.45 * t)
    licht(0.0)
    yield from stuk(40, licht)
    log("KORT OK licht")

    # tijdlijn: de editor onderin wordt de tijdlijn, echte sleep van de afspeelkop door drie poses
    deel("tijdlijn")
    if ne is not None:
        ne.type = "DOPESHEET_EDITOR"
        ne.ui_type = "TIMELINE"
        yield 0.6
        with bpy.context.temp_override(window=venster, area=ne, region=next(r for r in ne.regions if r.type == "WINDOW")):
            try:
                bpy.ops.action.view_all()
            except Exception as f:  # noqa: BLE001
                log(f"KORT tijdlijn view_all {f}")
        yield 0.5
        tr = gebied_rect(ne)
        film["vlakken"]["tijdlijn"] = tr
        reg = next(r for r in ne.regions if r.type == "WINDOW")
        v2d = reg.view2d
        x1, _ = v2d.view_to_region(1, 0, clip=False)
        x120, _ = v2d.view_to_region(120, 0, clip=False)
        vx = venster.x + reg.x
        y_kop = tr[1] + (tr[3] - reg.height) + 28   # bovenrand van het venster van de tijdlijn (de schaal met getallen)
        yield from muis_naar(vx + x1, y_kop, duur=0.7)
        yield 0.3
        xdo("mousedown", "1")
        film["kliks"].append(round(time.time(), 3))
        yield from muis_naar(vx + x120, y_kop, duur=3.6, boog=0.0)
        yield from muis_naar(vx + (x1 + x120) / 2, y_kop, duur=1.2, boog=0.0)
        xdo("mouseup", "1")
        yield 0.3
        film["metingen"]["frame_na_sleep"] = sc.frame_current
        log(f"KORT tijdlijn frame {sc.frame_current}")
        if sc.frame_current in (0, 1):
            log("KORT vangnet tijdlijn: script schuift de afspeelkop")
            yield from stuk(90, lambda t: sc.frame_set(int(1 + 119 * t)))
    sc.frame_set(40)
    log("KORT OK tijdlijn")

    # render: echte klik op het menu Render, dan Render Animation (2 beelden), resultaat op het scherm, Esc
    deel("render")
    sc.frame_start, sc.frame_end = 40, 41
    sc.render.filepath = os.path.join(scherm_basis.uitmap, "proef", "r_")
    sc.render.resolution_percentage = 50
    top = [venster.x, venster.y, venster.width, 70]
    rm = ocr("Render", top)
    film["metingen"]["render_menu_ocr"] = rm
    if rm is None:
        rm = (venster.x + 175, venster.y + 22)
    yield from muis_naar(rm[0], rm[1], duur=0.8)
    yield 0.2
    klik()
    yield 0.6
    ra = ocr("Render Animation", [venster.x, venster.y, 900, 500])
    film["metingen"]["render_anim_ocr"] = ra
    if ra:
        yield from muis_naar(ra[0], ra[1], duur=0.5)
        yield 0.2
        klik()
        deel("render_klik")
        yield 6.0
        xdo("key", "Escape")
        yield 0.8
    else:
        xdo("key", "Escape")
        log("KORT render-menu: Render Animation niet gevonden")
    log("KORT OK render")

    # eind: de eindfilm door de studiocamera (niet in de opname gebruikt)
    deel("eind_render")
    ruimte.region_3d.view_perspective = "CAMERA"
    ruimte.overlay.show_overlays = False
    for o in lampen:
        o.data.energy = kracht[o.name]
    sc.render.resolution_percentage = 100
    R.poseer(delen, R.HELD, scharnier=scharnier)
    for o in delen:
        o.animation_data_clear()
    n = int(EIND_SEC * 30)
    sc.frame_start, sc.frame_end = 1, n
    sc.render.fps = 30
    S.richt(cam_ob, delen, "staand", draai=-40, kantel=7, vul=0.74, midden_y=0.56)
    m0 = cam_ob.matrix_world.copy()
    S.richt(cam_ob, delen, "staand", draai=-18, kantel=9, vul=0.80, midden_y=0.55)
    m1 = cam_ob.matrix_world.copy()
    l0, l1 = m0.to_translation(), m1.to_translation()
    q0, q1 = m0.to_quaternion(), m1.to_quaternion()
    cam_ob.rotation_mode = "QUATERNION"
    for f in (1, n):
        t = 0.0 if f == 1 else 1.0
        cam_ob.location = l0.lerp(l1, t)
        cam_ob.rotation_quaternion = q0.slerp(q1, t)
        cam_ob.keyframe_insert("location", frame=f)
        cam_ob.keyframe_insert("rotation_quaternion", frame=f)
    sc.render.image_settings.file_format = "PNG"
    sc.render.filepath = os.path.join(scherm_basis.uitmap, "eind", "e_")
    g3.spaces.active.shading.type = "MATERIAL"
    with bpy.context.temp_override(window=venster, area=g3, region=next(r for r in g3.regions if r.type == "WINDOW")):
        bpy.ops.render.opengl(animation=True, view_context=True)
    log(f"KORT OK eind {n} beelden")
'''

GEEN_FIGUUR_IMPORT = '''
import sys as _sys2
_sys2.path.insert(0, STUDIO_MAP)
import figuur_robot as R  # noqa: E402
import studio as S  # noqa: E402
'''

MIJN = f'''
_r28 = {{"V": {VERLOOP!r}, "I": {GEEN_FIGUUR_IMPORT.replace("STUDIO_MAP", repr(STUDIO))!r}}}
_i, _j = src.index("def verloop_pro():"), src.index("RENDER_SAMPLES =")
src = src[:_i] + _r28["I"] + _r28["V"] + "\\n\\n" + src[_j:]
'''

_haak = "r14 = r14.replace(_haak, PATCH + _haak)"
assert r26.count(_haak) == 1
r26 = r26.replace(_haak, "r14 = r14.replace(_haak, PATCH + " + repr(MIJN) + " + _haak)")
r26 = r26.replace("HIER = os.path.dirname(os.path.abspath(__file__))", f"HIER = {os.path.dirname(R26)!r}", 1)
exec(compile(r26, R26, "exec"), {"__name__": "__main__", "__file__": R26})   # noqa: S102 (eigen code uit de repo)
