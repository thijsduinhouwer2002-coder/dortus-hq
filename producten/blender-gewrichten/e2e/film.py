"""Filmpje Click Joints (draaiboek Daan, ontwerp/click-joints/film.md): beeld voor beeld opnemen in de echte Blender.
Draait met de interface onder Xvfb: blender /tmp/start.blend --python e2e/film.py -- <map> <zip>
Maakt <map>/scene1..4/0001.png enzovoort (hele X-scherm met `import -window root`) en <map>/draaiboek.json
voor ontwerp/click-joints/film/bron/maak_film.py. Alleen gratis functies in beeld.

Per beeld twee timerstappen: (1) toestand zetten (camera, Bend, verschuiving van deel B) en hertekenen vragen,
(2) hertekenen afdwingen en het X-scherm vastleggen. Zo staat er nooit een half getekend beeld op de opname."""
import importlib
import json
import math
import os
import subprocess
import sys

import bmesh
import bpy
from mathutils import Matrix, Quaternion, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
from scherm_basis import DOEL, log, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

FPS = 30
# Scènes 1 tot 4 (eindkaart maakt maak_film.py). Duur in seconden, gelijk aan het draaiboek.
DUUR = {1: 3.0, 2: 3.5, 3: 5.0, 4: 3.5}
KLIK_T = 2.0
HOUT = "#D9C2A0"
ACHTERGROND = "#2B2E35"
staat = {"fase": "start", "scene": 1, "beeld": 0, "klik": None}


def srgb_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def kleur(hexa, lineair=True):
    rgb = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    return [srgb_lin(c) for c in rgb] if lineair else rgb


def glad(a):
    a = min(max(a, 0.0), 1.0)
    return a * a * (3 - 2 * a)


def mod(naam):
    m = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    return importlib.import_module(f"{m}.{naam}")


# ---------- de tekenpop (versie 2 van de plaatjes): eenvoudige vormen, samengevoegd tot één gesloten mesh ----------

def _bol(r, c, schaal=(1, 1, 1), seg=48):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg // 2, radius=1.0)
    bm.transform(Matrix.Translation(c) @ Matrix.Diagonal((r * schaal[0], r * schaal[1], r * schaal[2], 1.0)))
    return bm


def _staaf(p0, p1, r0, r1, lus=0.0):
    """Taps toelopende cilinder van p0 naar p1 (straal r0 naar r1); lus > 0: extra lusjes, zodat de passingring smal blijft."""
    p0, p1 = Vector(p0), Vector(p1)
    d = p1 - p0
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=48, radius1=r0, radius2=r1, depth=d.length)
    if lus > 0:
        n = int(d.length / lus)
        for i in range(1, n):
            z = -d.length / 2 + lus * i + 0.37
            bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, z), plane_no=(0, 0, 1))
    rot = d.normalized().to_track_quat("Z", "Y").to_matrix().to_4x4()
    bm.transform(Matrix.Translation((p0 + p1) / 2) @ rot)
    return bm


# Maten in mm (1 eenheid = 1 mm), voeten op z = 0, ±117 mm hoog. Rechterarm (−X) van het lijf, elleboog gebogen,
# onderarm naar buiten en iets naar voren: zo ligt het snijvlak van het gewricht (loodrecht op de onderarm) vrij van
# lijf, hoofd en benen (nagerekend: alle andere delen liggen minstens 6 mm aan één kant van dat vlak).
SCHOUDER_R = Vector((-15, 0, 92))
ELLEBOOG = Vector((-31, -2, 80))
ONDERARM = Vector((-0.85, -0.45, 0.2)).normalized()
SNEDE = 11.0  # mm van de elleboog: plek van het gewricht op de onderarm


def tekenpop(solver):
    delen = []
    hand = ELLEBOOG + ONDERARM * 30.0
    vormen = [
        _bol(1.0, (0, 0, 108), (6.5, 7.0, 8.5)),             # hoofd (ei)
        _staaf((0, 0, 95), (0, 0, 101), 2.8, 2.6),           # nek
        _bol(1.0, (0, 0, 84), (13.0, 8.0, 13.5)),            # borst
        _bol(5.5, (0, 0, 70)),                               # taille (bolletje)
        _bol(1.0, (0, 0, 60), (11.0, 7.5, 8.0)),             # bekken
        _bol(4.6, SCHOUDER_R), _bol(4.6, (15, 0, 92)),       # schouders
        _staaf(SCHOUDER_R, ELLEBOOG, 4.4, 4.2),              # rechterbovenarm
        _bol(4.6, ELLEBOOG),                                 # rechterelleboog
        _staaf(ELLEBOOG, hand, 4.2, 3.8, lus=1.5),           # rechteronderarm (hier komt het gewricht)
        _bol(1.0, hand + ONDERARM * 3.0, (3.0, 3.6, 4.0)),   # rechterhand
        _staaf((15, 0, 92), (18, 0, 70), 4.2, 3.6),          # linkerbovenarm, hangt langs het lijf
        _bol(4.0, (18, 0, 70)),
        _staaf((18, 0, 70), (19, -1, 49), 3.6, 3.0),
        _bol(1.0, (19.3, -1, 44), (2.6, 3.2, 5.0)),          # linkerhand
        _bol(5.2, (6, 0, 53)), _staaf((6, 0, 53), (6.5, 0, 29), 5.4, 4.3), _bol(4.4, (6.5, 0, 29)),
        _staaf((6.5, 0, 29), (6.5, 0, 6), 4.1, 3.1), _bol(1.0, (6.5, -3, 3), (3.6, 7.0, 3.0)),       # standbeen
        _bol(5.2, (-6, 0, 53)), _staaf((-6, 0, 53), (-9, -3, 30), 5.4, 4.3), _bol(4.4, (-9, -3, 30)),
        _staaf((-9, -3, 30), (-9.5, 1, 6.5), 4.1, 3.1), _bol(1.0, (-9.8, -2, 3), (3.6, 7.0, 3.0)),  # speelbeen
    ]
    for i, bm in enumerate(vormen):
        me = bpy.data.meshes.new(f"deel{i}")
        bm.to_mesh(me)
        bm.free()
        ob = bpy.data.objects.new(f"deel{i}", me)
        bpy.context.scene.collection.objects.link(ob)
        delen.append(ob)
    basis = delen[0]
    for d in delen[1:]:
        m = basis.modifiers.new(d.name, "BOOLEAN")
        m.operation, m.object, m.solver = "UNION", d, solver
        d.hide_set(True)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(basis.evaluated_get(dg))
    for d in delen:
        bpy.data.objects.remove(d)
    try:
        me.shade_smooth()
        me.set_sharp_from_angle(angle=math.radians(35))
    except Exception as e:  # noqa: BLE001
        log(f"glad maken lukte niet: {e}")
    hout = bpy.data.materials.new("Wood")
    hout.diffuse_color = (*kleur(HOUT), 1.0)
    me.materials.append(hout)
    ob = bpy.data.objects.new("Mannequin", me)
    bpy.context.scene.collection.objects.link(ob)
    ob.color = (*kleur(HOUT), 1.0)
    ob.active_material = hout
    return ob


def gesloten(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = bm.calc_volume(signed=True)
    bm.free()
    return fout, vol


# ---------- weergave ----------

def ruimte_regio():
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    return venster, gebied, gebied.spaces.active, regio


def schoon_beeld():
    venster, gebied, ruimte, _ = ruimte_regio()
    with bpy.context.temp_override(window=venster, area=gebied):
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
    venster, gebied, ruimte, _ = ruimte_regio()
    ruimte.show_region_toolbar = False
    ruimte.show_region_header = False
    ruimte.show_region_ui = True
    try:
        ruimte.show_region_tool_header = False
    except AttributeError:
        pass
    ruimte.show_gizmo_navigate = False
    sh = ruimte.shading
    sh.type, sh.light, sh.color_type = "SOLID", "STUDIO", "MATERIAL"
    sh.background_type = "VIEWPORT"
    sub = type(sh).bl_rna.properties["background_color"].subtype
    sh.background_color = kleur(ACHTERGROND, lineair=(sub != "COLOR_GAMMA"))
    ov = ruimte.overlay
    for k in ("show_floor", "show_axis_x", "show_axis_y", "show_axis_z", "show_cursor", "show_text", "show_stats",
              "show_object_origins", "show_ortho_grid", "show_extras", "show_relationship_lines"):
        if hasattr(ov, k):
            setattr(ov, k, False)
    ruimte.clip_start, ruimte.clip_end = 0.5, 10000
    bpy.context.scene.view_settings.view_transform = "Standard"
    gebied.tag_redraw()
    log(f"FILM beeld: gebied {gebied.width}x{gebied.height}, achtergrond subtype {sub}, ui_scale "
        f"{bpy.context.preferences.view.ui_scale}")


def zet_kijk(richting, doel, afstand, rechts_frac):
    """Kijk langs `richting` naar `doel`; het doel schuift naar links (rechts zit de zijbalk), rechts_frac x afstand."""
    _, gebied, ruimte, _ = ruimte_regio()
    rv3d = ruimte.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = Vector(richting).normalized().to_track_quat("-Z", "Y")
    rv3d.view_distance = afstand
    rechts = rv3d.view_rotation @ Vector((1.0, 0, 0))
    rv3d.view_location = Vector(doel) + rechts * (rechts_frac * afstand)
    gebied.tag_redraw()


def meng(a, b, t):
    return a.lerp(b, t) if isinstance(a, Vector) else a + (b - a) * t


# ---------- de scènes ----------

POP_MIDDEN = Vector((-6, 0, 58))
POP_AFSTAND = 250.0
BASIS_RICHTING = Vector((-0.4, 1.0, -0.18)).normalized()


def draai_z(v, graden):
    return Quaternion((0, 0, 1), math.radians(graden)) @ v


def deel(letter):
    return next((o for o in bpy.context.scene.objects if o.get("cj_deel") == letter), None)


def plaats_gewricht():
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = False  # Exploded view staat standaard aan; in scène 1 tot 3 uit (draaiboek)
    inst.toon_bereik = False
    inst.pose_graden = 0.0
    inst.speling_mm, inst.as_bron, inst.kogel_auto = 0.2, "CURSOR", True
    figuren.zet_cursor(tuple(ELLEBOOG + ONDERARM * SNEDE), tuple(ONDERARM))
    figuren.maak_actief(staat["pop"])
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    a, b = deel("A"), deel("B")
    for o in bpy.context.selected_objects:
        o.select_set(False)
    if a:
        bpy.context.view_layer.objects.active = a
    paneel = mod("paneel")
    log(f"FILM plaats: {uitslag}, kogel {inst.kogel_mm} mm, passing {a.get('cj_passing') if a else None}, "
        f"wand {a.get('cj_wand_mm') if a else None}, tekst {paneel.buig_tekst(a) if a else None}, "
        f"bereik {list(a.get('cj_buig_graden', [])) if a else None}")
    for d in (a, b):
        if d:
            fout, vol = gesloten(d)
            log(f"FILM deel {d.get('cj_deel')}: foute randen {fout}, volume {vol:.1f}")
    # Richting van de buiging: van de 8 richtingen de meest omhoog wijzende, zodat de onderarm omhoog zwaait.
    as_ = Vector(a["cj_as"]).normalized()
    rich = mod("uit_elkaar").richtingen(as_)
    k = max(range(len(rich)), key=lambda i: rich[i].z)
    inst.pose_richting = str(k)
    staat.update(as_=as_, rich=rich[k], c=Vector(a["cj_centrum"]), r=float(a["cj_kogel_r"]), richting=k)
    log(f"FILM richting {k} ({k * 45} graden), grens {paneel.richting_graden(a, k)}")


def kijk_buig():
    """Scène 3: loodrecht op het buigvlak, het gewricht iets links van het midden."""
    kijk_r = staat["as_"].cross(staat["rich"]).normalized()
    if kijk_r.dot(BASIS_RICHTING) < 0:
        kijk_r = -kijk_r  # van de voorkant van de pop, niet van achteren
    # ronde 2: verder weg (was 16 r), zodat je de hele arm met hand en schouder ziet buigen
    return kijk_r, staat["c"] + staat["as_"] * 4.0, 36.0 * staat["r"]


def zet_beeld(sc, i):
    """Toestand van beeld i (vanaf 0) in scène sc."""
    t = i / FPS
    a = t / DUUR[sc]
    inst = bpy.context.scene.click_joints
    if sc == 1:
        zet_kijk(draai_z(BASIS_RICHTING, -5 + 10 * a), POP_MIDDEN, POP_AFSTAND, 0.17)
        return
    if sc == 2:
        if i == 0:
            plaats_gewricht()
        kijk_r, doel, afst = kijk_buig()
        # rustig van de hele pop naar de elleboog (en het paneel rechts): klaar op 2,5 s, dan stil
        z = glad(t / 2.5)
        rich = BASIS_RICHTING.slerp(kijk_r, z) if hasattr(Vector, "slerp") else BASIS_RICHTING.lerp(kijk_r, z)
        zet_kijk(rich, meng(POP_MIDDEN, doel, z), meng(POP_AFSTAND, afst, z), 0.17)
        return
    if sc == 3:
        if i == 0:
            inst.toon_bereik = True
        kijk_r, doel, afst = kijk_buig()
        zet_kijk(kijk_r, doel, afst, 0.17)
        # 0 -> 15 (1,5 s), stil 0,5 s, 15 -> 28 (1,2 s), stil 0,8 s, terug naar 15 (1,0 s)
        if t < 1.5:
            g = 15 * glad(t / 1.5)
        elif t < 2.0:
            g = 15
        elif t < 3.2:
            g = 15 + 13 * glad((t - 2.0) / 1.2)
        elif t < 4.0:
            g = 28
        else:
            g = 28 - 13 * glad((t - 4.0) / 1.0)
        inst.pose_graden = round(g, 2)
        return
    if sc == 4:
        b = deel("B")
        if i == 0:
            inst.pose_graden = 0.0
            inst.toon_bereik = False
            staat["los"] = Vector(b["cj_as"]).normalized() * mod("uit_elkaar").afstand(b)
        kijk_r, doel, afst = kijk_buig()
        schuin = (kijk_r * math.cos(math.radians(35)) + staat["as_"] * math.sin(math.radians(35))).normalized()
        zet_kijk(kijk_r.lerp(schuin, glad(t / 1.0)), doel, afst * 1.05, 0.17)
        b.delta_location = staat["los"] * glad(t / 1.0)  # deel B schuift in 1 s van de kogel af
        if i == 45:
            rol_paneel()  # draaiboek: daarna kort het paneel met STL / 3MF en "Export STL"


def rol_paneel():
    """Rol de zijbalk omlaag (gewoon muiswiel, zonder Ctrl) zodat stap 3 met STL / 3MF en Export STL in beeld komt."""
    from scherm_basis import xdo
    venster, _, regio = zijbalk()
    x = venster.x + regio.x + regio.width // 2
    y = venster.y + venster.height - (regio.y + regio.height // 2)
    xdo("mousemove", str(x), str(y))
    for _ in range(12):
        xdo("click", "5")
    xdo("mousemove", "5", "5")
    log(f"FILM paneel gerold bij ({x}, {y})")


def kleur_verslag(naam):
    _, _, ruimte, _ = ruimte_regio()
    pop = staat.get("pop")
    a = deel("A")
    ob = a or pop
    mats = [(m.name, tuple(round(c, 3) for c in m.diffuse_color)) if m else None for m in ob.data.materials] if ob else []
    idx = sorted({p.material_index for p in ob.data.polygons}) if ob else []
    log(f"FILM kleur {naam}: color_type={ruimte.shading.color_type} light={ruimte.shading.light} "
        f"object={ob.name if ob else None} materialen={mats} indexen={idx[:8]}")


def klik_plek():
    """Schermplek (X-pixels, y van boven) van de elleboog-snede, voor het pijltje en de ring in maak_film.py."""
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    venster, gebied, ruimte, regio = ruimte_regio()
    p = location_3d_to_region_2d(regio, ruimte.region_3d, ELLEBOOG + ONDERARM * SNEDE)
    if p is None:
        return None
    x = venster.x + regio.x + p.x
    y = venster.height - (regio.y + p.y)
    return [round(x), round(y)]


def leg_vast():
    sc, i = staat["scene"], staat["beeld"]
    venster = bpy.context.window_manager.windows[0]
    try:
        with bpy.context.temp_override(window=venster):
            bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)
    except Exception as e:  # noqa: BLE001
        if i == 0:
            log(f"redraw_timer lukte niet: {e}")
    d = os.path.join(uitmap, f"scene{sc}")
    os.makedirs(d, exist_ok=True)
    pad = os.path.join(d, f"{i + 1:04d}.png")
    r = subprocess.run(["import", "-window", "root", pad], capture_output=True, text=True)
    if r.returncode or not os.path.exists(pad):
        log(f"FILM FOUT vastleggen {pad}: {r.stderr.strip()}")
    if i == 0:
        kleur_verslag(f"scene{sc}")
    if sc == 1 and i == int(KLIK_T * FPS):
        staat["klik"] = klik_plek()
        log(f"FILM klik op {staat['klik']}")
    if sc == 3 and i in (int(1.9 * FPS), int(3.9 * FPS)):
        a = deel("A")
        waaier = mod("waaier")
        log(f"FILM boog bij {bpy.context.scene.click_joints.pose_graden}: {waaier.laatst.get('bogen', [])} "
            f"rood {len(a.get('cj_rood_vlakken', [])) // 2 if a else None}")


def draaiboek():
    lagen = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../ontwerp/click-joints/film"))
    uit = [0, 98, 1920, 983]  # 1920 x 885, zelfde verhouding als de kaart (1700 x 784)
    klik = staat["klik"] or [700, 500]
    boek = {"fps": FPS, "lagen": lagen, "scenes": [
        {"beeld": "scene1", "duur": DUUR[1], "kop": "kop1", "uitsnede": uit, "klik": [klik[0], klik[1], KLIK_T]},
        {"beeld": "scene2", "duur": DUUR[2], "kop": "kop2", "uitsnede": uit},
        {"beeld": "scene3", "duur": DUUR[3], "kop": "kop3", "uitsnede": uit},
        {"beeld": "scene4", "duur": DUUR[4], "kop": "kop4", "uitsnede": uit},
        {"eind": True, "duur": 3.5}]}
    with open(os.path.join(uitmap, "draaiboek.json"), "w") as f:
        json.dump(boek, f, indent=1)
    log(f"FILM draaiboek geschreven, klik {klik}")


def stap():
    f = staat["fase"]
    if f == "start":
        log(f"Blender {bpy.app.version_string}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        bpy.context.preferences.view.ui_scale = 1.6  # paneeltekst groot en scherp (draaiboek Daan)
        for ob in list(bpy.data.objects):
            bpy.data.objects.remove(ob)
        figuren.mm_scene()
        solver = mod("gewricht").solver_naam()
        pop = tekenpop(solver)
        staat["pop"] = pop
        fout, vol = gesloten(pop)
        log(f"FILM pop: {len(pop.data.polygons)} vlakken, foute randen {fout}, volume {vol:.0f} mm3, solver {solver}")
        figuren.maak_actief(pop)
        schoon_beeld()
        staat["fase"] = "tabblad"
        return 1.5
    if f == "tabblad":
        if not wiel_naar_tabblad() and toestand["pogingen"] < 14:
            return 0.6
        _, _, regio = zijbalk()
        log(f"FILM TABBLAD {'OK' if regio and regio.active_panel_category == DOEL else 'NIET GELUKT'}")
        for o in bpy.context.selected_objects:
            o.select_set(False)
        staat["fase"] = "zet"
        return 1.0
    if f == "zet":
        zet_beeld(staat["scene"], staat["beeld"])
        staat["fase"] = "vast"
        return 0.3 if staat["beeld"] == 0 else 0.05
    if f == "vast":
        leg_vast()
        staat["beeld"] += 1
        if staat["beeld"] >= int(round(DUUR[staat["scene"]] * FPS)):
            log(f"FILM scene {staat['scene']} klaar, {staat['beeld']} beelden")
            staat["scene"] += 1
            staat["beeld"] = 0
        if staat["scene"] > 4:
            draaiboek()
            log("FILM KLAAR")
            bpy.ops.wm.quit_blender()
            return None
        staat["fase"] = "zet"
        return 0.02
    return None


bpy.app.timers.register(stap, first_interval=3.0)
