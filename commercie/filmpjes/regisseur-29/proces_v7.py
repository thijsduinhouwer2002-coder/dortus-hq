"""Sale-Short v7 in procesvorm (issue #159, Regisseur 26 nov 2026 avond).

Thijs keurde v6b af (26 nov 18:10): "niet van beeld wisselen, alles in één beeld", "niet ingezoomd maar dynamisch",
"maak exact die tiktok na". Het voorbeeld (@simonzhang.art) is één doorlopende opname van één project: het model vult
het beeld, de camera van de weergave draait steeds rond, en het model zelf verandert elke ±0,7 s.

Dit script gebruikt alle machinerie van ../regisseur-28/proces.py (echte Blender 5.3.0 met interface onder Xvfb,
Click Joints Pro 1.2.8, beeld voor beeld op een eigen klok van 1/30 s met echte muis en echte kliks) en vervangt
alleen het verloop:
  grijs      grijze robot, camera draait doorlopend rond (dat blijft zo tot de klik op Render)
  rig        het skelet verschijnt
  kies/knop  echte klik op de robot, echte klik op Figure from rig
  delen      Blender kleurt de nieuwe delen kort willekeurig (Solid, Random), dan weer grijs
  uitelkaar  echte klik op Exploded view, rondje, echte klik terug
  knie       camera zakt naar de knie, Bend tot de stop, voorbij de stop rood, terug
  kleur      deel voor deel krijgt de robot zijn kleur (van boven naar beneden, elke ±0,6 s)
  pose       de robot gaat in een pose zonder botsing (eigen toets: geen twee delen door elkaar die in rust los zijn)
  licht      achtergrond van grijs naar groenblauw, het studiolicht draait mee
  render     echte klik op Render, dan Render Animation
  eind       (niet in de opname) eind.blend: Cycles, camera vliegt langzaam om de hele robot heen, 6,5 s
    blender --gpu-backend opengl start.blend --python proces_v7.py -- <map> <betaalde zip>"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
P28 = os.path.abspath(os.path.join(HIER, "..", "regisseur-28", "proces.py"))

VERLOOP7 = r'''
import random as _rnd
_rnd.seed(29)
EIND_SEC = float(os.environ.get("CJ_EIND_SEC", "6.5"))


def ocr2(tekst, vak=None, drempels=("65%", "45%", "30%")):
    vak = vak or rect("UI")
    x0, y0, b, h = vak
    subprocess.run(["import", "-window", "root", "/tmp/cj_ocr2.png"], capture_output=True)
    doel = tekst.lower().split()
    for dr in drempels:
        subprocess.run(["convert", "/tmp/cj_ocr2.png", "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray",
                        "-resize", "200%", "-threshold", dr, "-negate", "/tmp/cj_ocr2_v.png"], capture_output=True)
        r = subprocess.run(["tesseract", "/tmp/cj_ocr2_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True,
                           text=True)
        regels = {}
        for regel in r.stdout.splitlines()[1:]:
            d = regel.split("\t")
            if len(d) == 12 and d[11].strip():
                w = (d[11].strip().lower().strip(".,:;(){}[]'\"|"), int(d[6]) // 2, int(d[7]) // 2, int(d[8]) // 2,
                     int(d[9]) // 2)
                regels.setdefault((d[2], d[3], d[4]), []).append(w)
        for ws in regels.values():
            ws.sort(key=lambda w: w[1])
            for i in range(len(ws) - len(doel) + 1):
                if all(ws[i + j][0] == doel[j] for j in range(len(doel))):
                    s_ = ws[i:i + len(doel)]
                    return (x0 + (min(w[1] for w in s_) + max(w[1] + w[3] for w in s_)) // 2,
                            y0 + (min(w[2] for w in s_) + max(w[2] + w[4] for w in s_)) // 2)
    log(f"KORT ocr2 niet gevonden: {tekst!r}")
    return None


def drijf(sec):
    """De hand rust nooit: kleine rustige bewegingen in het zichtbare deel van de weergave (links, 1080 breed)."""
    t_eind = time.time() + sec
    w = rect("WINDOW")
    while time.time() < t_eind - 0.25:
        x = min(max(MUIS["x"] + _rnd.randint(-140, 140), w[0] + 120), w[0] + 960)
        y = min(max(MUIS["y"] + _rnd.randint(-110, 110), w[1] + 500), w[1] + 1500)
        yield from muis_naar(x, y, duur=min(_rnd.uniform(0.5, 0.8), max(0.2, t_eind - time.time() - 0.1)))
        yield _rnd.uniform(0.05, 0.2)
    while time.time() < t_eind:
        yield 1.0 / 30


def gebied3d():
    for venster in bpy.context.window_manager.windows:
        for g in venster.screen.areas:
            if g.type == "VIEW_3D":
                return venster, g
    return None, None


def wereld_bvh(o):
    import bmesh
    from mathutils.bvhtree import BVHTree
    bm = bmesh.new()
    bm.from_mesh(o.data)
    bm.transform(o.matrix_world)
    t = BVHTree.FromBMesh(bm)
    bm.free()
    return t


def raak_paren(delen):
    bomen = {o.name: wereld_bvh(o) for o in delen}
    namen = sorted(bomen)
    paren = set()
    for i, a in enumerate(namen):
        for b in namen[i + 1:]:
            if bomen[a].overlap(bomen[b]):
                paren.add((a, b))
    return paren


def geschaald(pose, f):
    uit = {}
    for k, v in pose.items():
        uit[k] = [(a, g * f) for a, g in v] if isinstance(v, list) else v * f
    return uit


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
    SM["rustig"]()
    leeg_beeld()
    bpy.context.preferences.view.ui_scale = UI
    bpy.context.preferences.system.use_region_overlap = False
    bpy.context.preferences.view.show_tooltips = False
    bpy.context.preferences.view.render_display_type = "SCREEN"
    kijk_breed()
    venster, g3 = gebied3d()
    ruimte = g3.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "SINGLE"
    ruimte.shading.single_color = (0.62, 0.62, 0.64)
    ruimte.shading.show_cavity = False
    ruimte.overlay.show_floor = True
    arm.hide_set(True)
    SM["open_paneel"]()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    yield 0.5
    yield from sleep_zijbalk(BREED_ZIJBALK)
    yield 1.0
    MUIS["x"], MUIS["y"] = 640, 1100
    xdo("mousemove", "640", "1100")
    heel = Vector((0.0, 0.0, 112.0))
    D = 300.0
    cam(-70, 84.0, D, tuple(heel))
    yield 0.8
    meet_schaal(tuple(heel), D)

    # De camera van de weergave draait vanaf nu elke tik rond (16 graden per seconde) en glijdt zacht naar het doel
    # (afstand, punt, kanteling) dat de stappen hieronder zetten. Zo is het één doorlopende opname.
    CAM = {"a": -70.0, "k": 84.0, "d": D, "p": heel.copy(), "dk": 84.0, "dd": D, "dp": heel.copy(), "v": 16.0}

    def elke():
        CAM["a"] += CAM["v"] / 30.0
        f = 0.075
        CAM["k"] += (CAM["dk"] - CAM["k"]) * f
        CAM["d"] += (CAM["dd"] - CAM["d"]) * f
        CAM["p"] = CAM["p"].lerp(CAM["dp"], f)
        cam(CAM["a"], CAM["k"], CAM["d"], tuple(CAM["p"]))
    _vk = globals().get("_VK")
    if _vk is not None:
        _vk["elke"] = elke
    else:
        log("KORT FOUT geen eigen klok (CJ_BEELD=1 nodig)")
    elke()
    yield 0.4

    # grijs
    deel("grijs")
    yield from drijf(1.4)
    log("KORT OK grijs")

    # rig
    deel("rig")
    arm.hide_set(False)
    herteken()
    yield from drijf(0.7)

    # kies: echte klik op de robot
    deel("kies")
    arm.hide_select = True
    geen_selectie()
    bpy.context.view_layer.objects.active = None
    buik = scherm_punt((9.0, -8.0, 128.0))
    if buik:
        yield from muis_naar(buik[0], buik[1], duur=0.5)
    klik()
    for _ in range(4):
        yield 0.1
        if bpy.context.view_layer.objects.active == ob:
            break
    if bpy.context.view_layer.objects.active != ob:
        log("KORT vangnet kies")
        A["actief"](ob)
    yield 0.2

    # knop: echte klik op Figure from rig (paneel rechts, buiten de staande uitsnede)
    deel("knop")
    knop = yield from zoek("Figure from rig")
    film["metingen"]["knop_ocr"] = knop
    if knop is None:
        knop = (rect("UI")[0] + rect("UI")[2] // 2, rect("UI")[1] + 160)
    yield from muis_naar(knop[0], knop[1], duur=0.6)
    for poging in range(3):
        yield 0.1
        tk = time.time()
        klik()
        yield 0.2
        heeft = any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects)
        if heeft:
            break
        knop2 = ocr("Figure from rig")
        if knop2:
            yield from muis_naar(knop2[0] + 25 * (poging + 1), knop2[1], duur=0.3)
    t0 = time.time()
    while not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects) and time.time() - t0 < 10:
        yield 0.2
    if not any(o.get("cj_figuur") and o.get("cj_deel") for o in bpy.context.scene.objects):
        log("KORT vangnet knop: Figure from rig via script")
        A["actief"](ob)
        bpy.ops.click_joints.figuur_uit_rig()
    deel("knop_klaar")
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    film["metingen"]["gewrichten"] = len(lijst)
    log(f"KORT knop {len(lijst)} gewrichten")
    geen_selectie()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") and o.type == "MESH"]
    film["metingen"]["delen"] = len(delen)
    # delen: Blender laat de losse delen kort elk in een eigen kleur zien (Solid, Random), dan weer grijs
    deel("delen")
    ruimte.shading.color_type = "RANDOM"
    w = rect("WINDOW")
    yield from muis_naar(w[0] + 760, w[1] + 1250, duur=0.6)
    yield 0.3
    ruimte.shading.color_type = "SINGLE"
    yield 0.1

    # uitelkaar: echte klik op Exploded view, een stuk rond, echte klik terug
    deel("uitelkaar")
    inst = bpy.context.scene.click_joints
    ex = yield from zoek("Exploded view", 3)
    if ex:
        yield from muis_naar(ex[0], ex[1], duur=0.5)
        klik()
        yield 0.1
    if not inst.uit_elkaar:
        log("KORT vangnet uitelkaar aan")
        inst.uit_elkaar = True
        herteken()
    deel("uitelkaar_aan")
    CAM["dd"] = D + 20
    yield from muis_naar(w[0] + 700, w[1] + 1150, duur=0.6)
    yield from drijf(0.8)
    if ex:
        yield from muis_naar(ex[0], ex[1], duur=0.5)
        klik()
        yield 0.1
    if inst.uit_elkaar:
        log("KORT vangnet uitelkaar uit")
        inst.uit_elkaar = False
        herteken()
    CAM["dd"] = D
    log("KORT OK uitelkaar")

    # knie: camera zakt naar de linkerknie, klik op het onderbeen, Bend tot de stop, voorbij (rood), terug
    a, b = paar("Left knee")
    if a is not None and b is not None:
        stop = float(a["cj_bereik_graden"])
        film["metingen"]["knie_stop"] = stop
        k = p["l-knee"]
        CAM["dp"], CAM["dd"], CAM["dk"] = Vector((k.x, k.y, k.z + 8.0)), 170.0, 80.0
        deel("knie")
        yield from drijf(0.5)
        onder = scherm_punt((p["l-knee"] + p["l-ankle"]) / 2)
        if onder:
            yield from muis_naar(onder[0], onder[1], duur=0.4)
        klik()
        yield 0.1
        geen_selectie()
        b.select_set(True)
        buig(b, 0.0)
        bpy.context.view_layer.objects.active = b
        s = math.floor(stop * 10) / 10
        deel("knie_buig")
        yield from stuk(27, lambda t: buig(b, s * t))
        deel("knie_stop")
        yield 0.3
        deel("knie_rood")
        yield from stuk(12, lambda t: buig(b, s + 15.0 * t))
        film["metingen"]["knie_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
        yield 0.4
        yield from stuk(15, lambda t: buig(b, (s + 15.0) * (1 - t)))
        buig(b, 0.0)
        log(f"KORT knie stop {stop} rood {film['metingen']['knie_rood_vlakken']}")
    else:
        log("KORT FOUT knie: geen linkerknie")
    geen_selectie()
    CAM["dp"], CAM["dd"], CAM["dk"] = heel.copy(), D, 84.0

    # kleur: de echte kleuren (zoals in de eindfilm) eerst klaarzetten maar grijs laten, dan deel voor deel tonen
    for o in delen:
        o.rotation_mode = "QUATERNION"
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    grijs = bpy.data.materials.new("cj_v7_grijs")
    grijs.diffuse_color = (0.62, 0.62, 0.64, 1.0)
    echt = {}
    for o in delen:
        echt[o.name] = [s_.material for s_ in o.material_slots]
        for s_ in o.material_slots:
            s_.material = grijs
    ruimte.shading.color_type = "MATERIAL"
    ruimte.shading.light = "STUDIO"
    deel("kleur")
    yield from muis_naar(w[0] + 520, w[1] + 900, duur=0.6)
    volg = sorted(delen, key=lambda o: -sum((o.matrix_world @ Vector(c)).z for c in o.bound_box) / 8.0)
    groepen = 7
    per = max(1, math.ceil(len(volg) / groepen))
    for gi in range(0, len(volg), per):
        for o in volg[gi:gi + per]:
            for s_, m in zip(o.material_slots, echt[o.name]):
                s_.material = m
        herteken()
        yield from drijf(0.6)
    log("KORT OK kleur")

    # pose zonder botsing: kies de eerste pose waarin geen twee delen elkaar raken die in rust los zijn
    def scharnier(n, gr):
        _a, bb = paar(n)
        if bb is not None:
            buig(bb, gr)
            bpy.context.view_layer.update()
    R.poseer(delen, {}, scharnier=scharnier)
    rust = raak_paren(delen)
    H = R.HELD
    kandidaten = [("HELD", H)]
    for sg in (1, -1):
        kandidaten.append((f"armen_wijd_{sg}", {
            "Left hip": [((0, 1, 0), -9.0)], "Right hip": [((0, 1, 0), 9.0)], "Left knee": 6.0, "Right knee": 6.0,
            "Left shoulder": [((0, 1, 0), 24.0 * sg), ((1, 0, 0), -20.0)], "Left elbow": 110.0,
            "Right shoulder": [((0, 1, 0), -24.0 * sg), ((1, 0, 0), 10.0)], "Right elbow": 60.0,
            "Neck": [((0, 0, 1), -14.0), ((1, 0, 0), -6.0)]}))
        kandidaten.append((f"armen_wijd_recht_{sg}", {
            "Left hip": [((0, 1, 0), -8.0)], "Right hip": [((0, 1, 0), 8.0)], "Left knee": 4.0, "Right knee": 4.0,
            "Left shoulder": [((0, 1, 0), 28.0 * sg)], "Left elbow": 30.0,
            "Right shoulder": [((0, 1, 0), -28.0 * sg)], "Right elbow": 30.0,
            "Neck": [((0, 0, 1), 12.0)]}))
    beste, uitslag = None, {}
    for kn, kp in kandidaten:
        R.poseer(delen, kp, scharnier=scharnier)
        nieuw = sorted(raak_paren(delen) - rust)
        uitslag[kn] = [list(x) for x in nieuw]
        log(f"KORT botsing {kn}: {len(nieuw)} {nieuw[:6]}")
        if beste is None or len(nieuw) < len(uitslag[beste[0]]):
            beste = (kn, kp)
        if not nieuw:
            break
    film["metingen"]["botsing"] = uitslag
    film["metingen"]["pose"] = beste[0]
    POSE = beste[1]
    log(f"KORT {'OK' if not uitslag[beste[0]] else 'FOUT'} pose {beste[0]} botsingen {len(uitslag[beste[0]])}")
    R.poseer(delen, {}, scharnier=scharnier)
    deel("pose")
    yield from stuk(42, lambda t: R.poseer(delen, geschaald(POSE, t), scharnier=scharnier))
    yield from drijf(0.5)

    # licht: achtergrond van grijs naar groenblauw, het studiolicht draait mee
    deel("licht")
    ruimte.shading.background_type = "VIEWPORT"
    try:
        ruimte.shading.use_world_space_lighting = True
    except Exception as f:  # noqa: BLE001
        log(f"KORT licht {f}")
    van_k, naar_k = Vector((0.19, 0.19, 0.20)), Vector((0.30, 0.48, 0.45))

    def licht(t):
        ruimte.shading.background_color = tuple(van_k.lerp(naar_k, t))
        try:
            ruimte.shading.studiolight_rotate_z = math.radians(-120 + 160 * t)
        except Exception:  # noqa: BLE001
            pass
    licht(0.0)
    yield from stuk(36, licht)
    log("KORT OK licht")

    # render: echte klik op het menu Render, dan Render Animation (2 kleine beelden), dan Esc
    deel("render")
    sc = bpy.context.scene
    sc.frame_start, sc.frame_end = 1, 2
    sc.render.filepath = os.path.join(scherm_basis.uitmap, "proef", "r_")
    sc.render.resolution_percentage = 10
    try:
        sc.eevee.taa_render_samples = 1
    except Exception:  # noqa: BLE001
        pass
    top = [venster.x, venster.y, venster.width, 70]
    rm = ocr("Render", top) or ocr2("Render", top)
    film["metingen"]["render_menu_ocr"] = rm
    if rm is None:
        rm = (venster.x + 175, venster.y + 22)
    yield from muis_naar(rm[0], rm[1], duur=0.6)
    klik()
    yield 0.4
    ra = ocr("Render Animation", [venster.x, venster.y, 900, 500]) or ocr2("Render Animation", [venster.x, venster.y, 900, 500])
    film["metingen"]["render_anim_ocr"] = ra
    if ra:
        yield from muis_naar(ra[0], ra[1], duur=0.4)
        klik()
        deel("render_klik")
        yield 0.5
        if _vk is not None:
            _vk["elke"] = None
        yield 2.0
        xdo("key", "Escape")
        yield 1.0
    else:
        deel("render_klik")
        xdo("key", "Escape")
        log("KORT render-menu: Render Animation niet gevonden")
    if _vk is not None:
        _vk["elke"] = None
    log("KORT OK render")

    # eind (niet in de opname): Cycles, camera vliegt langzaam om de hele robot heen
    deel("eind_render")
    for o in delen:
        for s_, m in zip(o.material_slots, echt[o.name]):
            s_.material = m
        o.animation_data_clear()
    S.bouw(220.0)
    R.poseer(delen, POSE, scharnier=scharnier)
    cam_ob = S.camera()
    n = int(EIND_SEC * 30)
    sc.frame_start, sc.frame_end = 1, n
    sc.render.fps = 30
    sc.render.resolution_percentage = 100
    cam_ob.rotation_mode = "QUATERNION"
    sleutel = [(1, -62, 9, 0.66), (n * 0.25, -44, 8, 0.67), (n * 0.5, -26, 7, 0.68), (n * 0.75, -10, 6, 0.69), (n, 4, 6, 0.70)]
    for f, dr, kt, vul in sleutel:
        S.richt(cam_ob, delen, "staand", draai=dr, kantel=kt, vul=vul, midden_y=0.55)
        cam_ob.keyframe_insert("location", frame=int(round(f)))
        cam_ob.keyframe_insert("rotation_quaternion", frame=int(round(f)))
    sc.render.image_settings.file_format = "PNG"
    sc.render.filepath = "//e_"
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = int(os.environ.get("CJ_EIND_SAMPLES", "32"))
    sc.cycles.use_denoising = True
    sc.render.use_persistent_data = True
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(scherm_basis.uitmap, "eind.blend"), copy=True)
    log(f"KORT OK eind {n} beelden (eind.blend), pose {beste[0]}")
'''

src = open(P28, encoding="utf-8").read()
_i = src.index("VERLOOP = r'''")
_j = src.index("'''\n\nGEEN_FIGUUR_IMPORT")
src = src[:_i] + "VERLOOP = " + repr(VERLOOP7) + src[_j + 3:]
exec(compile(src, P28, "exec"), {"__name__": "__main__", "__file__": P28})   # noqa: S102 (eigen code uit de repo)
