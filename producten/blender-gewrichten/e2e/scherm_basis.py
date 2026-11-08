"""Gedeelde onderdelen van de schermtest (schermen.py): zijbalk vinden, tabblad kiezen met xdotool,
schermafbeelding, weergave, de pop met gewricht, de close-up en de kijkrichtingstoets.
Opgesplitst uit schermen.py (opruimen 8 nov, regel: bestanden onder ±400 regels)."""
import os
import subprocess
import sys
import bpy
from mathutils import Vector

import figuren  # noqa: E402  (schermen.py zet de map e2e vooraan in sys.path)

args = sys.argv[sys.argv.index("--") + 1:]
uitmap, zip_pad = args[0], args[1]
os.makedirs(uitmap, exist_ok=True)
toestand = {"n": 0, "pogingen": 0}
DOEL = "Click Joints"
staat = {}


def log(tekst):
    print(f"[cj-scherm] {tekst}", flush=True)


def zijbalk():
    """Geeft (venster, gebied, regio) van de zijbalk (N-paneel) in de 3D-weergave."""
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                for regio in gebied.regions:
                    if regio.type == "UI":
                        return venster, gebied, regio
    return None, None, None


def open_paneel():
    venster, gebied, regio = zijbalk()
    if gebied:
        gebied.spaces.active.show_region_ui = True
        gebied.tag_redraw()


def xdo(*a):
    r = subprocess.run(["xdotool", *a], capture_output=True, text=True)
    if r.returncode:
        log(f"xdotool {' '.join(a)} faalde: {r.stderr.strip()}")


def wiel_naar_tabblad():
    """Eén stap Ctrl+wiel boven de tabbladen. Geeft True als Click Joints actief is."""
    venster, gebied, regio = zijbalk()
    if not regio:
        log("geen zijbalk gevonden")
        return False
    huidig = regio.active_panel_category
    log(f"actief tabblad: {huidig} (poging {toestand['pogingen']})")
    if huidig == DOEL:
        return True
    # Blender telt y van onder; X telt van boven. Tabbladen staan aan de rechterrand van de zijbalk.
    x = venster.x + regio.x + regio.width - 8
    y = venster.y + venster.height - (regio.y + regio.height // 2)
    knop = "5" if toestand["pogingen"] < 5 else "4"  # eerst omlaag, daarna omhoog
    xdo("mousemove", str(x), str(y))
    xdo("keydown", "ctrl")
    xdo("click", knop)
    xdo("keyup", "ctrl")
    toestand["pogingen"] += 1
    return False


def schiet(naam):
    pad = os.path.join(uitmap, naam)
    venster = bpy.context.window_manager.windows[0]
    with bpy.context.temp_override(window=venster):
        bpy.ops.screen.screenshot(filepath=pad)
    log(f"schermafbeelding {pad} {os.path.exists(pad)}")
    # Blender leest onder Xvfb met software-OpenGL een zwart beeld uit; pak daarom ook het hele X-scherm.
    x_pad = pad.replace(".png", "-x.png")
    r = subprocess.run(["import", "-window", "root", x_pad], capture_output=True, text=True)
    log(f"X-scherm {x_pad} {os.path.exists(x_pad)} {r.stderr.strip()}")


def weergave():
    """Zet de 3D-weergave in objectkleur en zoomt in op alles wat zichtbaar is."""
    venster, gebied, _ = zijbalk()
    if not gebied:
        return
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"  # standaard Solid: de passingkleur moet hier al te zien zijn
    ruimte.clip_start = 0.1
    ruimte.clip_end = 10000
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        bpy.ops.view3d.view_all()


def maak_pop():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    bpy.context.view_layer.update()
    figuren.mm_scene()
    import importlib
    naam = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    solver = importlib.import_module(naam + ".gewricht").solver_naam()
    # Armen 8 mm dik: het hoofdplaatje toont een Good fit (Daan, tussenreactie 2, punt 3).
    # De dunne armen (5,2 mm) geven altijd Tight; die staan in de achtergrondtest.
    # Armen 40 mm lang: bij 34 mm lag het eind van de arm vlak achter de kom, waardoor Auto maar 3,0 mm koos
    # (wand naar de vlakke kop van de arm). Nu krijgt het plaatje een kogel van ±4,5 mm.
    pop = figuren.pop(solver, arm_r=4.0, arm_lengte=40.0)
    pop.color = (0.8, 0.8, 0.8, 1.0)
    figuren.maak_actief(pop)
    figuren.zet_cursor((11, 0, 3), (1, 0, 0))
    staat["pop"] = pop
    log(f"pop gemaakt met solver {solver}, {len(pop.data.polygons)} vlakken")


def plaats():
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron = 0.2, "CURSOR"
    inst.kogel_auto = True  # plaatje toont de automatische kogelmaat (grootste met Good fit), punt 2 en 3 van Daan
    inst.uit_elkaar = True  # opengewerkt beeld van de add-on zelf (standaard aan), zo is de kogel te zien
    figuren.maak_actief(staat["pop"])
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
    for d in delen:
        log(f"deel {d.name} passing={d.get('cj_passing')} wand={d.get('cj_wand_mm')} ring={d.get('cj_ring_deel')} "
            f"weergaveverschuiving={tuple(round(x, 3) for x in d.delta_location)} location={tuple(d.location)}")
    log(f"plaats: {uitslag}, {len(delen)} delen, kogel {inst.kogel_mm} mm (auto={inst.kogel_auto})")
    a = next((d for d in delen if d.get("cj_deel") == "A"), None)
    log(f"HOOFDPLAATJE passing={a.get('cj_passing') if a else None} keuze={a.get('cj_auto_keuze') if a else None} "
        f"breedte={a.get('cj_breedte_mm') if a else None}mm")


def close_up():
    """Kijk driekwart van voren op het gewricht, schuin langs de as, zodat je in de kom van deel B kijkt
    en de kogel op deel A ernaast ziet (punt 4 van Daan, ronde e). Het midden schuift wat naar rechts,
    want de zijbalk ligt over het rechterdeel van de weergave."""
    venster, gebied, _ = zijbalk()
    a = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "A"), None)
    if not gebied or a is None:
        log("close-up: geen weergave of geen deel A")
        return
    rv3d = gebied.spaces.active.region_3d
    as_ = Vector(a["cj_as"]).normalized()
    midden = Vector(a["cj_centrum"]) + as_ * (1.5 * a["cj_kogel_r"])  # half de verschuiving van de add-on
    richting = Vector((0.8, 0.6, -0.3)).normalized()  # kijkt langs +X (de as) de kom in, van voren en iets van boven
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = richting.to_track_quat("-Z", "Y")
    rv3d.view_distance = 24.0
    rechts = rv3d.view_rotation @ Vector((1.0, 0, 0))
    rv3d.view_location = midden + rechts * 2.5
    gebied.tag_redraw()
    log(f"close-up: midden={tuple(round(x, 2) for x in midden)} afstand=24 kogel_r={a.get('cj_kogel_r')}")


def gesloten(ob):
    """Elke rand precies 2 vlakken en volume groter dan 0."""
    import bmesh
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = bm.calc_volume(signed=True)
    bm.free()
    return fout == 0 and vol > 0, fout, vol


def kijk():
    """As langs de kijkrichting, aangeroepen zoals de knop in de zijbalk (context van de UI-regio).
    Plek: het rechterbeen (straal 3 mm). De cursor-as ligt dwars (X), dus een terugval op de cursor
    zou uit het been steken en rood geven."""
    for o in [o for o in bpy.data.objects if o.get("cj_deel")]:
        bpy.data.objects.remove(o)
    venster, gebied, regio_ui = zijbalk()
    rv3d = gebied.spaces.active.region_3d
    doel = Vector((0.03, 0.02, -1.0)).normalized()  # bijna recht omlaag, langs het rechterbeen
    rv3d.view_rotation = doel.to_track_quat("-Z", "Y")
    gebied.tag_redraw()
    verwacht = (rv3d.view_rotation @ Vector((0, 0, -1))).normalized()
    figuren.zet_cursor((3.2, 0, -12), (1, 0, 0))  # ronde g: 2 mm hoger, het gewricht is bij 3 mm langer
    inst = bpy.context.scene.click_joints
    inst.kogel_mm, inst.speling_mm, inst.as_bron = 3.0, 0.2, "KIJK"
    figuren.maak_actief(staat["pop"])
    with bpy.context.temp_override(window=venster, area=gebied, region=regio_ui):
        log(f"kijk: context regio={bpy.context.region.type} region_data={bpy.context.region_data}")
        uitslag = bpy.ops.click_joints.plaats()
    for o in bpy.context.scene.objects:
        if o.get("cj_passing") == "rood" and "cj_as" in o:
            log(f"kijk: rood teken, as={tuple(round(x, 4) for x in o['cj_as'])} as_bron={o.get('cj_as_bron')}")
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
    ok = len(delen) == 2
    hoek = None
    for d in delen:
        dicht, fout, vol = gesloten(d)
        hoek = Vector(d["cj_as"]).normalized().angle(verwacht)
        log(f"KIJK deel {d.name}: gesloten={dicht} foute_randen={fout} volume={vol:.2f} as_bron={d.get('cj_as_bron')} "
            f"as={tuple(round(x, 4) for x in d['cj_as'])} kijkrichting={tuple(round(x, 4) for x in verwacht)} "
            f"hoek={hoek:.6f}rad passing={d.get('cj_passing')}")
        ok = ok and dicht and d.get("cj_as_bron") == "KIJK" and hoek < 0.01
    log(f"kijk: {uitslag}, {len(delen)} delen")
    log(f"KIJK {'OK' if ok else 'FOUT'} (hoek {hoek} rad, marge 0,01)")
