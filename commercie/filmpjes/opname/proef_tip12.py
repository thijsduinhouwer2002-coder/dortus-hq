"""Proef (Olaf, 24 nov 2026): de opname van ../regisseur-12/tip_opname.py op de gedeelde hulpcode blender_opname.py.
Zelfde verloop; File > Export > STL nu via menu_pad, de Export-knop via knop(). Doel: laten zien dat een tip-opname
met de gedeelde code ±300 regels korter is en hetzelfde doet (zelfde delen, metingen en KORT OK in CI).
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python proef_tip12.py -- <uitmap>"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blender_opname import *  # noqa: F401,F403,E402

zet_naam("tip12p")
MAP = "/tmp/tip12p"


def maak_label():
    """Label van 60 x 30 x 4 mm met afgeronde hoeken en een gat (intern 0,06 x 0,03 x 0,004)."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.002))
    ob = bpy.context.view_layer.objects.active
    ob.name = "Label"
    ob.scale = (0.06, 0.03, 0.004)
    bpy.ops.object.transform_apply(scale=True)
    bv = ob.modifiers.new("hoek", "BEVEL")
    bv.width, bv.segments, bv.affect = 0.006, 6, "EDGES"
    bv.limit_method = "ANGLE"
    bpy.ops.mesh.primitive_cylinder_add(radius=0.0045, depth=0.02, location=(-0.021, 0, 0.002), vertices=48)
    gat = bpy.context.view_layer.objects.active
    selecteer(ob)
    bo = ob.modifiers.new("gat", "BOOLEAN")
    bo.object, bo.operation = gat, "DIFFERENCE"
    with bpy.context.temp_override(object=ob, active_object=ob):
        bpy.ops.object.modifier_apply(modifier="hoek")
        bpy.ops.object.modifier_apply(modifier="gat")
    bpy.data.objects.remove(gat, do_unlink=True)
    selecteer(ob)
    try:
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(35))
    except Exception as f:  # noqa: BLE001
        log(f"glad kleuren lukte niet: {f}")
    m = bpy.data.materials.new("label")
    m.diffuse_color = (0.96, 0.62, 0.18, 1)
    ob.data.materials.append(m)
    selecteer(ob)
    return ob



def verloop():
    zet_scherm()
    os.makedirs(MAP, exist_ok=True)
    sc = bpy.context.scene
    # de valkuil: Unit Scale 1 (Blender rekent in meter), lengte getoond in millimeter
    sc.unit_settings.system = "METRIC"
    sc.unit_settings.scale_length = 1.0
    sc.unit_settings.length_unit = "MILLIMETERS"
    _, a = gebied("VIEW_3D")
    sp = a.spaces.active
    sp.overlay.grid_scale = 1.0
    sp.clip_start, sp.clip_end = 0.0005, 50.0
    yield 1.0
    film["metingen"]["weergave"] = regio_rect(a)
    w = bpy.context.window_manager.windows[0]
    reg = [x for x in a.regions if x.type == "WINDOW"][0]
    with bpy.context.temp_override(window=w, area=a, region=reg):
        ob = maak_label()
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(MAP, "label.blend"))
    film["metingen"]["j_maat_blender_mm"] = maat_mm(ob)
    film["metingen"]["j_unit_scale"] = sc.unit_settings.scale_length
    # wat de gewone export schrijft (Scale 1): onzichtbaar, alleen om na te meten
    exporteer_stl(os.path.join(MAP, "zonder.stl"), 1.0)
    film["metingen"]["j_stl_zonder"] = stl_maat(os.path.join(MAP, "zonder.stl"))
    log(f"KORT meting blender {film['metingen']['j_maat_blender_mm']} mm, stl zonder schaal {film['metingen']['j_stl_zonder']}")
    herteken()
    yield 0.8
    kop = regio_rect(a, "HEADER")
    balk = bovenbalk()
    film["metingen"]["kop"], film["metingen"]["bovenbalk"] = kop, balk
    mid = Vector((0, 0, 0.002))
    cam(25, 58, 0.16, mid)
    yield 0.5
    if os.environ.get("CJ_KIJK"):
        subprocess.run(["import", "-window", "root", os.path.join(uitmap, "kijk.png")])
        bpy.ops.wm.quit_blender()
        return
    yield from muis_naar(*zachte_muis_in_beeld(), 4)

    deel("j_mooi")      # haakbeeld: label draait langzaam, dichtbij
    yield from stuk(120, lambda t: cam(25 + 40 * t, 58 - 6 * t, 0.16 - 0.03 * t, mid))
    log("KORT OK j_mooi")

    deel("j_maat")      # N: Dimensions 60 x 30 x 4 mm
    toets("n")
    yield 0.8
    if not sp.show_region_ui:
        log("KORT vangnet j_maat: zijbalk via script")
        sp.show_region_ui = True
        herteken()
        yield 0.5
    neem(6)
    zb = regio_rect(a, "UI")
    film["metingen"]["j_zijbalk"] = zb
    film["metingen"]["j_dim_scherm"] = ocr("Dimensions", zb, "35%") if zb else None
    yield from houd(100)
    toets("n")
    yield 0.5
    sp.show_region_ui = False
    yield from stuk(40, lambda t: cam(65 - 30 * t, 52 + 4 * t, 0.13 + 0.03 * t, mid))
    log("KORT OK j_maat")

    deel("j_menu")      # File > Export > STL
    neem(6)
    voor = len(bpy.context.window_manager.windows)
    r = yield from menu_pad(balk, ["File", "Export", "STL"], "j_menu", klik_wacht=1.5)
    neem(10)
    if not r:
        log("KORT vangnet j_menu: menu niet gevonden")
    yield 0.3
    film["metingen"]["j_venster_open"] = (len(bpy.context.window_manager.windows) > voor or any(
        a.type == "FILE_BROWSER" for w in bpy.context.window_manager.windows for a in w.screen.areas))
    log("KORT OK j_menu")

    deel("j_venster")   # Scale 1000, Export STL
    via_venster = False
    doel = os.path.join(MAP, "label.stl")
    if os.path.exists(doel):
        os.remove(doel)
    if r and film["metingen"]["j_venster_open"]:
        yield from houd(12)
        s = None
        for _ in range(6):
            s = ocr("Scale", [0, 0, 2160, 1920], "35%")
            if s:
                break
            yield 0.5
            neem(2)
        film["metingen"]["j_scale_label"] = s
        if s:
            veld = (s[0] + 260, s[1])
            yield from muis_naar(*veld, 16)
            neem(6)
            dubbelklik()
            yield 0.4
            neem(6)
            toets("ctrl+a")
            for c in "1000":
                toets(c)
                yield 0.15
                neem(5)
            yield from houd(14)
            toets("Return")
            yield 0.4
            neem(10)
            # run 12: witte tekst op de blauwe knop leest tesseract slecht; onderste strook, drie drempels, dan Cancel + 280
            onder = [1000, 1700, 1160, 220]
            e = knop("Export STL", onder)
            if not e:
                c = ocr("Cancel", onder, "35%") or ocr("Cancel", onder, "60%")
                if c:
                    e = (c[0] + 280, c[1])
            film["metingen"]["j_knop"] = e
            if e:
                yield from muis_naar(e[0], e[1], 16)
                neem(6)
                klik()
                yield 1.0
                neem(4)
                if not os.path.exists(doel) and any(
                        a.type == "FILE_BROWSER" for a in bpy.context.window_manager.windows[0].screen.areas):
                    klik()      # eerste klik sloot alleen het tekstveld af
            yield 1.5
            neem(8)
    if os.path.exists(doel):
        film["metingen"]["j_stl_met"] = stl_maat(doel)
        via_venster = abs(film["metingen"]["j_stl_met"][0] - 60) < 0.5
    film["metingen"]["j_via_venster"] = via_venster
    if not via_venster:
        log(f"KORT vangnet j_venster: export via script (bestand {os.path.exists(doel)})")
        for _ in range(3):
            if len(bpy.context.window_manager.windows) > 1 or any(
                    a.type == "FILE_BROWSER" for a in bpy.context.window_manager.windows[0].screen.areas):
                toets("Escape")
                yield 0.4
        exporteer_stl(doel, 1000.0)
        film["metingen"]["j_stl_met"] = stl_maat(doel)
    log(f"KORT meting stl met schaal 1000 {film['metingen']['j_stl_met']}")
    yield from houd(10)
    log("KORT OK j_venster")

    deel("j_klaar")     # rustig eindbeeld
    yield from muis_naar(*zachte_muis_in_beeld(), 8)
    yield from stuk(150, lambda t: cam(35 + 50 * t, 56 - 8 * t, 0.16 - 0.035 * t, mid))
    yield from houd(30)
    log("KORT OK j_klaar")
    deel("eind")
    einde()



start(verloop)
