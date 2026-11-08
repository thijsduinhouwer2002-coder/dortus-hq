"""Draait met de interface onder Xvfb: blender --python e2e/schermen.py -- <map> <zip>
Zet het Click Joints-paneel open met een pop, plaatst een gewricht, maakt schermafbeeldingen en sluit af.

Tabblad kiezen: `active_panel_category` is alleen-lezen, daarom draait de test met
xdotool Ctrl+muiswiel boven de zijbalk (zo wisselt Blender van tabblad) tot het
tabblad Click Joints actief is. Dat lezen we wel uit, dus het bewijs staat in het log."""
import os
import subprocess
import sys
import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

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
    ruimte.shading.color_type = "OBJECT"
    ruimte.clip_start = 0.1
    ruimte.clip_end = 10000
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        bpy.ops.view3d.view_all()


def maak_pop():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    import importlib
    naam = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    solver = importlib.import_module(naam + ".gewricht").solver_naam()
    pop = figuren.pop(solver)
    pop.color = (0.8, 0.8, 0.8, 1.0)
    figuren.maak_actief(pop)
    figuren.zet_cursor((11, 0, 3), (1, 0, 0))
    staat["pop"] = pop
    log(f"pop gemaakt met solver {solver}, {len(pop.data.polygons)} vlakken")


def plaats():
    inst = bpy.context.scene.click_joints
    inst.kogel_mm, inst.speling_mm, inst.as_bron = 3.0, 0.2, "CURSOR"
    figuren.maak_actief(staat["pop"])
    uitslag = bpy.ops.click_joints.plaats()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
    for d in delen:
        if d["cj_deel"] == "B":
            d.location += Vector(d["cj_as"]) * 4.0  # een beetje uit elkaar, zodat je de kogel ziet
        log(f"deel {d.name} passing={d.get('cj_passing')} wand={d.get('cj_wand_mm')} kleur={tuple(d.color)}")
    log(f"plaats: {uitslag}, {len(delen)} delen")


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, splash in voorkeuren: {bpy.context.preferences.view.show_splash}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        maak_pop()
        open_paneel()
        weergave()
        return 1.5
    if n == 2:
        if not wiel_naar_tabblad() and toestand["pogingen"] < 14:
            toestand["n"] = 1  # deze stap nog eens
            return 0.6
        _, _, regio = zijbalk()
        log(f"TABBLAD {'OK' if regio and regio.active_panel_category == DOEL else 'NIET GELUKT'}")
        return 0.8
    if n == 3:
        schiet("1-paneel.png")
        return 0.5
    if n == 4:
        plaats()
        weergave()
        return 1.5
    if n == 5:
        schiet("2-gewricht.png")
        return 0.5
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
