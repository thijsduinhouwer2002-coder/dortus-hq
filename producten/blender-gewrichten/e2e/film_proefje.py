"""Staande opname voor tip 9 van de reeks (Chris, 16 nov): een klein proefje met een paar spelingen.
    xvfb-run -s "-screen 0 1080x1920x24" blender --gpu-backend opengl start.blend --python e2e/film_proefje.py -- <map> <gratis zip>
Drie staafjes van 10 mm naast elkaar, elk met een kogelgewricht van 5 mm uit de gratis add-on (Place joint), speling
0,1 / 0,2 / 0,3 mm, opengewerkt (uit elkaar) met de groene pasband. De camera begint op alle drie, gaat langs elk staafje
en eindigt weer op alle drie. Het script kleurt niets; wat in beeld staat komt van de add-on. Geen tekst in beeld:
Chris zet de spelingen erbij, de tijden staan in <map>/film.json en de gemeten speling per staafje in het log
("FILM staafje ...")."""
import json
import math
import os
import subprocess
import sys

import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
import scherm_basis  # noqa: E402
import scherm_pro as sp  # noqa: E402
from scherm_basis import log, weergave, zijbalk, zip_pad  # noqa: E402

FPS = 30
SPELINGEN = (0.1, 0.2, 0.3)
AFSTAND_X = 15.0
BOVEN, ONDER = (0x2B / 255, 0x2F / 255, 0x38 / 255), (0x1D / 255, 0x20 / 255, 0x27 / 255)
beeldmap = os.path.join(scherm_basis.uitmap, "beelden")
os.makedirs(beeldmap, exist_ok=True)
film = {"fps": FPS, "delen": {}, "n": 0, "spelingen": {}}


def neem(houd=1):
    film["n"] += 1
    pad = os.path.join(beeldmap, f"b{film['n']:05d}.png")
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    for _ in range(houd - 1):
        film["n"] += 1
        if os.path.exists(pad):
            os.link(pad, os.path.join(beeldmap, f"b{film['n']:05d}.png"))


def deel(naam):
    film["delen"][naam] = film["n"] + 1
    log(f"FILM deel {naam} vanaf beeld {film['n'] + 1}")


def zacht(t):
    return t * t * (3 - 2 * t)


def camera(rot, afstand, plek):
    _, gebied, _ = zijbalk()
    rv3d = gebied.spaces.active.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = rot
    rv3d.view_distance = afstand
    rv3d.view_location = plek
    gebied.tag_redraw()


def kijk(zij, hoogte):
    """Kijkrichting: van voren (-Y), zij graden om Z, hoogte graden omhoog."""
    k = Vector((math.sin(math.radians(zij)), -math.cos(math.radians(zij)), 0))
    k = (k * math.cos(math.radians(hoogte)) + Vector((0, 0, 1)) * math.sin(math.radians(hoogte))).normalized()
    return (-k).to_track_quat("-Z", "Y")


def staafje(i, s):
    st = figuren.staaf(f"proef_{s:.1f}mm", 5.0, lengte=30.0)
    st.data.transform(Matrix.Rotation(math.pi / 2, 4, "Y"))   # rechtop langs Z
    st.location = ((i - 1) * AFSTAND_X, 0, 0)
    bpy.context.view_layer.update()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.kogel_mm, inst.soort, inst.as_bron = s, 5.0, "KOGEL", "CURSOR"
    inst.kogel_auto = False
    inst.uit_elkaar = True
    inst.toon_bereik = False   # geen gradenboog: het gaat hier om de speling, niet om het bereik
    figuren.zet_cursor(st.location, (0, 0, 1))
    figuren.maak_actief(st)
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel") and abs(o.get("cj_speling_mm", -1) - s) < 1e-4]
    a = next((d for d in delen if d.get("cj_deel") == "A"), None)
    gemeten = a.get("cj_speling_gemeten_mm") if a else None
    film["spelingen"][f"{s:.1f}"] = gemeten
    log(f"FILM staafje {s} mm: {uitslag} delen={len(delen)} passing={a.get('cj_passing') if a else None} "
        f"wand={a.get('cj_wand_mm') if a else None} gemeten={gemeten}")
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    return len(delen) == 2 and a.get("cj_passing") == "groen"


def verloop():
    log(f"Blender {bpy.app.version_string}, gratis zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    goed = [staafje(i, s) for i, s in enumerate(SPELINGEN)]
    log(f"FILM {'OK' if all(goed) else 'FOUT'} drie staafjes groen: {goed}")
    weergave()
    bpy.context.preferences.view.ui_scale = 1.35
    sp.schoon_beeld()
    _, gebied, _ = zijbalk()
    gebied.spaces.active.shading.background_type = "THEME"
    gr = bpy.context.preferences.themes[0].view_3d.space.gradients
    gr.background_type, gr.high_gradient, gr.gradient = "LINEAR", BOVEN, ONDER
    midden = Vector((0, 0, 0.0))
    yield 1.0
    # 1 alle drie (3 s): langzaam iets dichterbij
    deel("alle")
    for i in range(90):
        t = zacht(i / 89)
        camera(kijk(-12 + 6 * t, 14), 58 - 6 * t, midden)
        yield 0.04
        neem()
    # 2 tot 4 elk staafje (2,5 s): camera naar het staafje, licht draaien
    for j, s in enumerate(SPELINGEN):
        deel(f"speling_{s:.1f}")
        doel = Vector(((j - 1) * AFSTAND_X, 0, 0.0))
        van = midden if j == 0 else Vector(((j - 2) * AFSTAND_X, 0, 0.0))
        for i in range(75):
            t = zacht(min(i / 30, 1.0))
            plek = van.lerp(doel, t)
            afst = (52 if j == 0 else 30) * (1 - t) + 30 * t
            camera(kijk(-6 + 12 * i / 74, 12), afst, plek)
            yield 0.04
            neem()
    # 5 terug naar alle drie (2 s)
    deel("eind")
    laatst = Vector((AFSTAND_X, 0, 0.0))
    for i in range(60):
        t = zacht(i / 59)
        camera(kijk(6 - 12 * t, 12 + 2 * t), 30 + 24 * t, laatst.lerp(midden, t))
        yield 0.04
        neem()
    neem(15)
    with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"FILM klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
