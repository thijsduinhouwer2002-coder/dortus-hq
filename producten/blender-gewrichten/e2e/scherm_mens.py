"""Plaatje 19 (Pro 1.1, eindbeeld voor Daan): echte mensfiguur na "Figure from rig".

Figuur en rig uit proef_mens.py (MakeHuman base.obj, CC0 1.0, Mixamo-namen op de eigen gewrichtspunten, 220 mm,
linkerknie 120 en linkerelleboog 140 in Limit Rotation, rechts niets). Na de knop: scharnierbogen met getal op knieën
en ellebogen, kogelwaaiers op heupen en nek. Daan 16 nov: "maak het eindbeeld op een echte figuur, niet op de
cilinders". Alleen echte uitkomst van de add-on, niets nagetekend.
Regel "MENS BEELD OK" als minstens 4 bogen (4.2: 2) groen met getal getekend zijn, kogels groen met ±N en 40 px vrij,
de lijst `from rig` en `mirrored` bevat en de uitsnede van het paneel gelukt is.
    CJ_MENS_OBJ=<base.obj> blender --python e2e/scherm_mens.py -- <map> <betaalde zip>
"""
import importlib
import math
import os
import subprocess
import sys

import bpy
from mathutils import Euler, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from scherm_basis import log, open_paneel, schiet, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

os.environ["CJ_HOOGTE"] = os.environ.get("CJ_TOETS_HOOGTE", "220")
_src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
M = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
exec(compile(_src, "proef_mens.py", "exec"), M)
A = M["A"]

staat = {}
BEUK = (0.80, 0.62, 0.43, 1.0)  # matte lichte beukenhoutkleur (Daan 17 nov moet 3)
BUIG = {"Right elbow": 90.0, "Right knee": 60.0}  # Daan 17 nov moet 2: een elleboog ±90, een knie ±60, de rest recht


def etalagepop(ob):
    """Daan 17 nov moet 3: de MakeHuman-figuur als houten tekenpop, niet als kaal mens. Alleen de invoer verandert
    (vorm, kleur, glad), daarna draait de knop zoals altijd; de toets toetsen_mens rekent op de figuur zonder dit.
    Borst plat: punten aan de voorkant tussen z 146 en 172 (220 mm hoog, gemeten run 22) schuiven naar het vlak
    y = -2,5 mm, met een zachte overgang in hoogte en breedte, alleen naar achteren (nooit door de rug)."""
    for v in ob.data.vertices:
        c = v.co
        if c.y >= -2.5 or abs(c.x) < 4.0 or abs(c.x) > 36.0:
            continue
        wz = max(0.0, 1.0 - abs(c.z - 159.0) / 13.0)
        wx = min(1.0, (abs(c.x) - 4.0) / 6.0) * min(1.0, (36.0 - abs(c.x)) / 6.0)
        w = math.sin(wz * math.pi / 2.0) ** 2 * wx
        c.y = c.y + (-2.5 - c.y) * w
    for f in ob.data.polygons:
        f.use_smooth = True
    mat = bpy.data.materials.new("beuk")
    mat.diffuse_color = BEUK
    mat.roughness = 0.9
    ob.data.materials.clear()
    ob.data.materials.append(mat)
    ob.data.update()


def buig():
    """Moet 2: buig met de eigen Bend-schuif van het paneel (zelfde weg als een koper), eindig op de elleboog."""
    wm = bpy.context.window_manager
    delen = {o.get("cj_naam"): o for o in bpy.context.scene.objects
             if o.get("cj_deel") == "B" and o.get("cj_figuur") and o.get("cj_soort") == "SCHARNIER"}
    gebogen = {}
    for naam in ("Right knee", "Right elbow"):  # elleboog aan de kant van de kijker, zijn waaier staat niet achter de hand
        b = delen.get(naam)
        if b is None:
            continue
        A["actief"](b)
        wm.cj_scharnier_pose = BUIG[naam]
        gebogen[naam] = round(float(b.get("cj_pose_graden", 0.0)), 1)
    staat["gebogen"] = gebogen
    log(f"MENS gebogen {gebogen} delen={sorted(k for k in delen if k)}")


def bouw():
    A["leeg"]()  # ook de eenheden op mm: zonder dat is de figuur 220 meter en rekent de passing minuten
    ob, punten = M["laad_mens"](os.environ["CJ_MENS_OBJ"])
    st = A["mesh_staat"](ob)
    log(f"MENS geladen: open randen {st['open_randen']}")
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    if os.environ.get("CJ_POP", "1") == "1":
        etalagepop(ob)
    naam = ob.name
    arm = M["maak_rig"](punten)
    arm.data.display_type = "STICK"
    ob.modifiers.new("Armature", "ARMATURE").object = arm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    log("MENS knop start")
    staat["knop"] = bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    staat["lijst"] = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    staat["regels"] = [fig.regel(r) for r in staat["lijst"]]
    staat["samenvatting"] = fig.samenvatting(staat["lijst"])
    buig()
    log(f"MENS knop {staat['knop']} regels={staat['regels']} samenvatting={staat['samenvatting']}")


def rustig():
    """Moet 1: alleen de 3D-weergave met het paneel (tijdlijn en eigenschappen weg), rasters, assen, 3D-cursor en
    de tekst linksboven uit. Ctrl+Spatie (screen_full_area) houdt kop, gereedschapsbalk en zijbalk."""
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        bpy.ops.screen.screen_full_area()
    venster, gebied, _ = zijbalk()
    ov = gebied.spaces.active.overlay
    for k in ("show_floor", "show_axis_x", "show_axis_y", "show_axis_z", "show_cursor", "show_text", "show_outline_selected"):
        setattr(ov, k, False)


def kijk():
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    rv = ruimte.region_3d
    rv.view_perspective = "ORTHO"
    # Schuin van voren: de knieas ligt langs X (waaier zichtbaar van opzij), de elleboogas niet (zichtbaar van voren).
    rv.view_rotation = Euler((math.radians(float(os.environ.get("CJ_KANTEL", "82"))), 0.0,
                              math.radians(float(os.environ.get("CJ_DRAAI", "-35")))), "XYZ").to_quaternion()
    rv.view_location = (float(os.environ.get("CJ_MIDX", "-12")), 0.0, float(os.environ.get("CJ_MIDZ", "110")))
    rv.view_distance = float(os.environ.get("CJ_AFSTAND", "335"))


def uitsnede():
    venster, _gebied, regio = zijbalk()
    bron = os.path.join(uitmap, "19-mens-x.png")
    doel = os.path.join(uitmap, "19-mens-paneel.png")
    if not (regio and os.path.exists(bron)):
        return False
    x = venster.x + regio.x
    y = venster.y + venster.height - (regio.y + regio.height)
    r = subprocess.run(["convert", bron, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage", doel],
                       capture_output=True, text=True)
    return r.returncode == 0 and os.path.exists(doel)


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        bouw()
        rustig()
        open_paneel()
        kijk()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
    if "geschoten" not in staat:
        staat["geschoten"] = True
        venster, gebied, regio = zijbalk()
        if regio:  # zijbalk omlaag tot het vak Figure joints met de lijst in beeld is
            x = venster.x + regio.x + regio.width // 2
            y = venster.y + venster.height - (regio.y + regio.height // 2)
            subprocess.run(["xdotool", "mousemove", str(x), str(y)])
            for _ in range(25):
                subprocess.run(["xdotool", "click", "5"])
        gebied.tag_redraw()
        return 1.5
    schiet("19-mens.png")
    ok_uit = uitsnede()
    boog = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_boog")
    bogen = [b for b in boog.laatst.get("bogen", []) if b.get("figuur")]
    koppen = [b for b in boog.laatst.get("bogen", []) if b.get("kop")]
    groen = all(b.get("kleur") != boog.WIT for b in bogen)
    getal = all(b.get("getal_getekend") for b in bogen)
    rig_regel = any("from rig" in r for r in staat.get("regels", []))
    act = bpy.context.view_layer.objects.active
    zichtbaar = act is not None and act.visible_get() and bool(act.get("cj_deel"))
    oud = bpy.app.version < (4, 5, 0)  # bekende losse boolean-fout met alleen Exact (toetsen_rig_armen.py)
    # Run 20: zelfde eis als toetsen_rig_armen.py sinds run 19: in 4.2 minstens 4 van 8 gewrichten (de knieën
    # vallen daar eerlijk af met reden), dus minstens 2 scharnierbogen; in 5.x alle 8.
    genoeg = len(bogen) >= (2 if oud else 4)
    acht = any(r.endswith("mirror") for r in staat.get("regels", []))
    # Daan 16 nov ±13:50: kogels van een figuur klein en groen met één getal ±N° (moet 1: nooit binnen 40 px van
    # een ander getal), en stap 3 zegt niet "No joint yet" naast de gewrichten (moet 2).
    ft = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur_teken")
    from mathutils import Vector
    kogels = list(ft.laatst.get("getekend", {}).values())
    schaal = bpy.context.preferences.system.ui_scale
    vakken = [k["vak"] for k in kogels if k.get("getal_getekend")]
    for b in bogen:
        if b.get("label_px"):
            vakken_s = ft.vak(Vector(b["label_px"]), b["getal"], int(boog.FIGUUR_PX * schaal))
            vakken.append(vakken_s)
    gaten = [ft.gat(k["vak"], o) for k in kogels for o in vakken if tuple(o) != tuple(k["vak"])]
    min_gat = round(min(gaten), 1) if gaten else None
    kogel_ok = (len(kogels) >= (1 if oud else 2) and all(k["getal"].startswith("\u00b1") for k in kogels)
                and all(k["kleur"] != boog.WIT for k in kogels) and all(k.get("getal_getekend") for k in kogels)
                and (min_gat is None or min_gat >= 40.0 * schaal - 0.5))
    stap3 = bool(act is not None and act.get("cj_passing"))
    log(f"MENS KOGELS {'OK' if kogel_ok else 'FOUT'} kogels={[(k['naam'], k['getal'], k['label_px']) for k in kogels]} "
        f"kleinste_gat_px={min_gat} stap3_passing={act.get('cj_passing') if act else None} fout={ft.laatst.get('fout')}")
    ok = genoeg and acht and groen and getal and len(koppen) <= 1 and rig_regel and zichtbaar and ok_uit and kogel_ok and stap3
    log(f"MENS BEELD {'OK' if ok else 'FOUT'} samenvatting={staat.get('samenvatting')} bogen={[(b['naam'], b['getal'], b['kijkhoek']) for b in bogen]} "
        f"koppen={len(koppen)} actief={act.name if act else None} zichtbaar={zichtbaar} groen={groen} getal={getal} from_rig={rig_regel} uitsnede={ok_uit} "
        f"fout={boog.laatst.get('fout')}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
