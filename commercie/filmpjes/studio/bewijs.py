"""Bewijs van de studio (23 nov 2026): laadt het figuur, bouwt de studio, maakt 3 schermafbeeldingen van het rustige
Blender-scherm met het paneel van Click Joints Pro en 3 renders per figuur (staand in pose, staand uit elkaar met
Exploded view, liggend in pose). Draait in een echte Blender met beeldscherm (xvfb-run), want de renders gaan door de
3D-weergave (Material Preview, EEVEE) en de schermafbeeldingen zijn van het X-scherm.

    xvfb-run -s "-screen 0 1920x1080x24" blender --gpu-backend opengl -p 0 0 1920 1080 \
        --python bewijs.py -- <uitmap> <pro-zip> <base.obj> [naam]
Knoppen (env): CJ_SNEL=<.blend met al gesneden delen> slaat de knop over (alleen om de studio snel te testen);
CJ_STIJL=b geeft de tweede kleurstelling. CJ_FIGUUR=robot (studio-2) laadt de zelfgebouwde robot in plaats van het
mensfiguur; CJ_FIGUUR=<pad.glb> een ander figuur met eigen rig (CJ_HOOGTE, CJ_WEG, CJ_ARMEN zoals bij proef_figuur).
CJ_ALLEEN_STAAND=1: alleen de eerste render (snelle kijk naar een kandidaat). Regels "STUDIO OK <stap>" in het log;
de workflow eist ze.
"""
import importlib
import json
import os
import subprocess
import sys
import time
import traceback

import bpy

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import figuur_laden as FL  # noqa: E402
import studio as S  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
UIT, ZIP, OBJ = args[0], args[1], args[2]
NAAM = args[3] if len(args) > 3 else "figuur"
os.makedirs(UIT, exist_ok=True)
SNEL = os.environ.get("CJ_SNEL", "")
STIJLEN = {
    "a": {},   # oranje shirt, blauwe broek, gele schoenen, bruin haar (FL.STIJL)
    "b": {"shirt": "7B5CFF", "broek": "2B2D42", "schoen": "FF4F79", "haar": "F4B942", "riem": "FF4F79"},
}
FIGUUR = os.environ.get("CJ_FIGUUR", "mens")
HOOGTE = float(os.environ.get("CJ_HOOGTE", "220"))
if FIGUUR == "robot":
    import figuur_robot as R  # noqa: E402
    STIJLEN = {"a": {}, "b": R.STIJL_B}
STIJL = STIJLEN[os.environ.get("CJ_STIJL", "a")]
UI = float(os.environ.get("CJ_UI", "1.35"))
meting = {"naam": NAAM, "stijl": os.environ.get("CJ_STIJL", "a")}


def log(t):
    print(f"[studio] {t}", flush=True)


def xdo(*a):
    subprocess.run(["xdotool", *a], capture_output=True, text=True)


def schiet(naam):
    pad = os.path.join(UIT, naam)
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    log(f"scherm {pad} {os.path.exists(pad)}")


def zijbalk():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                for regio in gebied.regions:
                    if regio.type == "UI":
                        return venster, gebied, regio
    return None, None, None


def naar_tabblad(doel="Click Joints"):
    """Ctrl+wiel boven de tabbladen van de zijbalk tot Click Joints actief is (zoals een gebruiker)."""
    for poging in range(16):
        venster, gebied, regio = zijbalk()
        if regio.active_panel_category == doel:
            return True
        x = venster.x + regio.x + regio.width - 8
        y = venster.y + venster.height - (regio.y + regio.height // 2)
        xdo("mousemove", str(x), str(y))
        xdo("keydown", "ctrl")
        xdo("click", "5" if poging < 7 else "4")
        xdo("keyup", "ctrl")
        yield 0.4
    return False


def wiel(keer, knop="5"):
    """Zijbalk scrollen met het muiswiel (zoals een gebruiker): knop 5 omlaag, 4 omhoog. Een generator: tussen de
    klikken tekent Blender opnieuw, anders blijft het scrollen hangen op de oude lengte van het paneel."""
    venster, gebied, regio = zijbalk()
    xdo("mousemove", str(venster.x + regio.x + regio.width // 2), str(venster.y + venster.height // 2))
    for _ in range(keer):
        xdo("click", knop)
        herteken()
        yield 0.03
    xdo("mousemove", "300", "900")


def herteken():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            gebied.tag_redraw()


def delen_van(naam):
    return [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_figuur") == naam and o.visible_get()]


def paar(naam):
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam and o.get("cj_soort", "") == "SCHARNIER":
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def buig(naam, graden):
    """Scharnier buigen met de schuif van de add-on (zelfde als de gebruiker), binnen het bereik."""
    a, b = paar(naam)
    if b is None:
        log(f"geen scharnier {naam}")
        return None
    stop = float(a.get("cj_bereik_graden", 0) or 0) if a is not None else 0
    g = min(graden, stop) if stop else graden
    bpy.context.view_layer.objects.active = b
    bpy.context.window_manager.cj_scharnier_pose = round(g, 1)
    bpy.context.view_layer.update()
    return round(float(b.get("cj_pose_graden", g)), 1), stop


def geen_selectie():
    for o in bpy.context.view_layer.objects:
        o.select_set(False)


POSE = {"Left knee": 85.0, "Right knee": 15.0, "Left elbow": 45.0, "Right elbow": 80.0}   # stap, binnen het bereik


def verloop():
    log(f"Blender {bpy.app.version_string}")
    if "figuur_uit_rig" not in dir(bpy.ops.click_joints):
        bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    inst = bpy.context.scene.click_joints
    if SNEL:
        for o in list(bpy.data.objects):
            bpy.data.objects.remove(o)
        us = bpy.context.scene.unit_settings
        us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
        with bpy.data.libraries.load(SNEL, link=False) as (van, naar):
            naar.objects = list(van.objects)
        for o in naar.objects:
            if o is not None:
                bpy.context.scene.collection.objects.link(o)
        arm = next(o for o in bpy.context.scene.objects if o.type == "ARMATURE")
        fignaam = next(o.get("cj_figuur") for o in bpy.context.scene.objects if o.get("cj_figuur"))
        ob = None
    else:
        if FIGUUR == "mens":
            arm, ob, _p = FL.laad_mens_kleding(OBJ, HOOGTE, stijl=STIJL)
        else:
            weg = tuple(w for w in os.environ.get("CJ_WEG", "").split(",") if w)
            arm, ob, _p = FL.laad_figuur(FIGUUR, HOOGTE, stijl=STIJL, weg=weg,
                                         armen=float(os.environ.get("CJ_ARMEN", "0")))
        fignaam = ob.name
        meting["figuur"] = FIGUUR
    arm.hide_set(True)
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    S.bouw(HOOGTE)
    log("STUDIO OK bouw")
    venster, gebied = S.rustig_scherm(ui=UI)
    yield 1.0
    S.view3d()[1].spaces.active.show_region_ui = True
    yield from naar_tabblad()
    yield 0.5
    S.kijk_naar((0, 0, 0.49 * HOOGTE), 400 * HOOGTE / 220, draai=-28, kantel=84)
    yield 1.0
    yield from wiel(60)   # zijbalk helemaal omlaag: daar staat Figure joints met de knop en later de lijst
    yield 1.0
    # scherm 1: figuur gekozen, knop Figure from rig in het paneel
    if ob is not None:
        FL.actief(ob)
        herteken()
        yield 1.0
        schiet("scherm-1-figuur-kiezen.png")
        log("STUDIO OK scherm1")
        t0 = time.time()
        r = bpy.ops.click_joints.figuur_uit_rig()
        meting["knop_s"] = round(time.time() - t0, 1)
        log(f"Figure from rig {r} in {meting['knop_s']} s")
        yield 0.5
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, fignaam)
    meting["gewrichten"] = len(lijst)
    meting["regels"] = [fig.regel(x) for x in lijst]
    delen = delen_van(fignaam)
    meting["delen"] = len(delen)
    meting["overgeslagen"] = str(next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), None))
    log(f"gewrichten {len(lijst)}: {meting['regels']}")
    log(f"overgeslagen: {meting['overgeslagen']}")
    # scherm 2: de lijst met gewrichten en graden
    geen_selectie()
    groot = max(delen, key=lambda o: len(o.data.vertices))
    bpy.context.view_layer.objects.active = groot
    groot.select_set(True)
    herteken()
    yield 0.8
    yield from wiel(120)
    yield 1.0
    schiet("scherm-2-lijst.png")
    log("STUDIO OK scherm2")
    # scherm 3: linkerknie gekozen, hoofdpaneel open met de Bend-schuif, boog van de add-on in beeld
    geen_selectie()
    a, b = paar("Left knee")
    if b is not None:
        b.select_set(True)
        bpy.context.view_layer.objects.active = b
        meting["knie_scherm"] = buig("Left knee", 95.0)
        try:
            bpy.context.window_manager.cj_scharnier_boog = True
        except Exception:  # noqa: BLE001
            pass
        yield 0.8
        yield from wiel(60, "4")   # eerst helemaal omhoog, dan omlaag tot het blok Hinge met de Bend-schuif
        yield 0.5
        yield from wiel(int(os.environ.get("CJ_WIEL", "14")))
        yield 0.8
        k = a.get("cj_snijpunt") if a is not None else None
        S.kijk_naar(k if k else (0, 0, 60), 280, draai=38, kantel=80)
        herteken()
        yield 1.5
        schiet("scherm-3-knie.png")
        log("STUDIO OK scherm3")
        buig("Left knee", 0.0)
    # renders: alleen het figuur en de studio, geen bogen of getallen
    try:
        bpy.context.window_manager.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    if FIGUUR == "robot":
        R.kleur_herstel(delen)
        S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)   # gewrichten antraciet, als mechaniek
    else:
        S.plastic(delen)
    cam = S.camera()
    meting["pose"] = {n: buig(n, g) for n, g in POSE.items()}
    geen_selectie()
    bpy.context.view_layer.update()
    yield 0.5
    S.richt(cam, delen, "staand", draai=-32, kantel=7, vul=0.74, midden_y=0.56)
    yield 0.3
    S.render(os.path.join(UIT, f"{NAAM}-1-staand-pose.png"))
    log("STUDIO OK render1")
    if os.environ.get("CJ_ALLEEN_STAAND"):
        json.dump(meting, open(os.path.join(UIT, f"{NAAM}-meting.json"), "w"), indent=1, ensure_ascii=False)
        log("STUDIO OK klaar")
        return
    inst.uit_elkaar = True
    herteken()
    bpy.context.view_layer.update()
    yield 0.5
    # uit elkaar schuiven de onderbenen omlaag, onder z=0: podium, rand en wand gaan even mee omlaag
    lo, _hi = S.kader(delen_van(fignaam))
    zak = min(0.0, lo.z - 0.5)
    studio_obs = [o for o in bpy.context.scene.objects if o.name in ("studio_wand", "studio_podium", "studio_rand")]
    for o in studio_obs:
        o.location.z += zak
    meting["podium_omlaag_mm"] = round(-zak, 1)
    S.richt(cam, delen_van(fignaam), "staand", draai=-24, kantel=6, vul=0.80, midden_y=0.55)
    yield 0.3
    S.render(os.path.join(UIT, f"{NAAM}-2-staand-uit-elkaar.png"))
    for o in studio_obs:
        o.location.z -= zak
    log("STUDIO OK render2")
    inst.uit_elkaar = False
    herteken()
    bpy.context.view_layer.update()
    yield 0.5
    S.richt(cam, delen, "liggend", draai=-38, kantel=8, vul=0.80, midden_y=0.5)
    yield 0.3
    S.render(os.path.join(UIT, f"{NAAM}-3-liggend-pose.png"))
    log("STUDIO OK render3")
    json.dump(meting, open(os.path.join(UIT, f"{NAAM}-meting.json"), "w"), indent=1, ensure_ascii=False)
    if not SNEL and os.environ.get("CJ_BEWAAR"):
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(UIT, f"{NAAM}-studio.blend"))
    log("STUDIO OK klaar")


G = verloop()


def stap():
    try:
        return next(G)
    except StopIteration:
        bpy.ops.wm.quit_blender()
    except Exception as fout:  # noqa: BLE001
        log(f"STUDIO FOUT {fout}\n{traceback.format_exc()}")
        bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=2.0)
