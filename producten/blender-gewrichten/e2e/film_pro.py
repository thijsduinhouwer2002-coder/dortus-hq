"""Demofilm Click Joints Pro (opdracht hoofdchat 15 nov 17:55): echte beelden uit de add-on in de echte Blender.
    blender --gpu-backend opengl start.blend --python e2e/film_pro.py -- <map> <betaalde zip>
Maakt <map>/beelden/b00001.png ... (hele X-scherm 1920x1080, één per filmbeeld van 1/30 s) en <map>/film.json met
het eerste beeld van elk deel, voor de onderschriften in maak_film.sh. Het script kleurt niets: groen, rood en de
gradenboog komen van de add-on. Wat het script wel doet (alleen weergave): camera bewegen, de Bend-schuif zetten
zoals een gebruiker hem sleept, B half doorzichtig bij het rode stuk (zoals winkelplaatje 14).
Delen:
  1 plaats   het hele been (één stuk), dan Place hinge met 115° (de knop in de zijbalk), het been is in twee delen
  2 buig     de Bend-schuif van 0° naar 115° met de gradenboog aan
  3 rood     iets voorbij de stop (bereik + 3°): de botsende delen worden rood
  4 kogel    de kogel van Place joint met de groene pasband (gratis deel van de add-on, zit ook in Pro)
Regels "FILM OK <deel>" zijn wat de workflow eist."""
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
from scherm_basis import log, toestand, weergave, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

FPS = 30
UI_SCHAAL = 1.35
AFSTAND = 95.0   # been groter in beeld dan op winkelplaatje 13 (135 liet veel leeg)
beeldmap = os.path.join(scherm_basis.uitmap, "beelden")
os.makedirs(beeldmap, exist_ok=True)
film = {"fps": FPS, "delen": {}, "n": 0}


def neem(houd=1):
    """Pak het hele X-scherm als volgend filmbeeld; houd > 1 herhaalt hetzelfde beeld (stilstaand stuk)."""
    film["n"] += 1
    pad = os.path.join(beeldmap, f"b{film['n']:05d}.png")
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    for _ in range(houd - 1):
        film["n"] += 1
        kopie = os.path.join(beeldmap, f"b{film['n']:05d}.png")
        if os.path.exists(pad):
            os.link(pad, kopie)


def deel(naam):
    film["delen"][naam] = film["n"] + 1
    log(f"FILM deel {naam} vanaf beeld {film['n'] + 1}")


def zacht(t):
    return t * t * (3 - 2 * t)


def zijbalk_aan(aan):
    _, gebied, _ = zijbalk()
    if gebied:
        gebied.spaces.active.show_region_ui = aan
        gebied.tag_redraw()


def leeg_beeld():
    """Alleen de 3D-weergave over het hele scherm, eigen donkere achtergrond, geen raster en assen; zijbalk aan."""
    bpy.context.preferences.view.ui_scale = UI_SCHAAL   # zijbalk leesbaar in de film (alleen deze sessie)
    sp.schoon_beeld()
    zijbalk_aan(True)


def maak_been():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    lid = sp.been()
    figuren.maak_actief(lid)
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):  # H, buigkant, lidas
        m.col[i][:3] = v
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.toon_bereik = sp.SPELING, "CURSOR", False, False
    return lid


def camera(rot, afstand, plek):
    _, gebied, _ = zijbalk()
    rv3d = gebied.spaces.active.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = rot
    rv3d.view_distance = afstand
    rv3d.view_location = plek
    gebied.tag_redraw()


def kijkrot(h, lidas, buig, zij_lidas, hoogte):
    k = (h * math.cos(math.radians(zij_lidas)) + lidas * math.sin(math.radians(zij_lidas))).normalized()
    k = (k * math.cos(math.radians(hoogte)) + buig * math.sin(math.radians(hoogte))).normalized()
    return k.to_track_quat("-Z", "Y")


def verloop():
    """De hele film als reeks stappen; elke yield geeft Blender tijd om te tekenen voor het volgende beeld."""
    wm = bpy.context.window_manager
    log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    lid = maak_been()
    weergave()
    leeg_beeld()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    _, _, regio = zijbalk()
    log(f"FILM tabblad {'OK' if regio and regio.active_panel_category == scherm_basis.DOEL else 'NIET GELUKT'}")
    # Kijkrichting zoals winkelplaatje 13: H, buigkant (Z) en lidas (X) van de cursor hierboven.
    h, buig, lidas = Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0))
    midden = Vector((-4.0, 0, 3.0))   # iets naar links: de zijbalk ligt rechts over de weergave
    # 1 plaats: het hele been draait langzaam (2 s), dan Place hinge met 115°
    deel("plaats")
    for i in range(75):
        camera(kijkrot(h, lidas, buig, 40 - 20 * zacht(i / 74), 15), AFSTAND, midden)
        yield 0.05
        neem()
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("been_A"), bpy.data.objects.get("been_B")
    sp.staat["a"], sp.staat["b"] = a, b
    log(f"FILM plaats: {uitslag} A={a is not None} B={b is not None} "
        f"bereik={a.get('cj_bereik_graden') if a else None} melding={a.get('cj_melding') if a else None}")
    if a is None or b is None:
        bpy.ops.wm.quit_blender()
        return
    sp.deselecteer()
    wm.cj_scharnier_boog = True
    wm.cj_scharnier_pose = 0.0
    sp.deselecteer()
    yield 1.0
    neem(60)
    log(f"FILM OK plaats groen={a.get('cj_band_vlakken', 0)},{b.get('cj_band_vlakken', 0)}")
    # 2 buig: de schuif van 0 naar 115 in 4 s, dan 1 s stil
    deel("buig")
    stop = float(a["cj_bereik_graden"])
    for i in range(121):
        g = min(round(stop * zacht(i / 120), 1), math.floor(stop * 10) / 10)   # nooit voorbij de stop
        sp.zet(g)
        yield 0.05
        neem()
    neem(40)
    log(f"FILM OK buig tot {b.get('cj_pose_graden')} bereik {stop}")
    # 3 rood: camera schuift naar boven op de stop (1 s), B half doorzichtig, dan 3° voorbij de stop
    deel("rood")
    r0 = kijkrot(h, lidas, buig, 20, 15)
    r1 = kijkrot(h, lidas, buig, 20, 50)
    sp.doorzichtig_b()
    for i in range(30):
        camera(r0.slerp(r1, zacht(i / 29)), AFSTAND - 15.0 * zacht(i / 29), midden.lerp(Vector((0, 0, 0)), zacht(i / 29)))
        yield 0.05
        neem()
    rood = 0
    for i in range(16):
        rood = sp.zet(round(stop + 3.0 * i / 15, 2))
        yield 0.05
        neem()
    neem(75)
    log(f"FILM {'OK' if rood > 0 else 'FOUT'} rood rood_vlakken={rood}")
    # 4 kogel: de pop met Place joint, groene pasband, langzaam draaien (3 s)
    deel("kogel")
    wm.cj_scharnier_boog = False
    scherm_basis.maak_pop()
    scherm_basis.plaats()
    weergave()   # niet opnieuw schoon_beeld: screen_full_area zou het volle scherm weer uitzetten
    scherm_basis.close_up()
    _, gebied, _ = zijbalk()
    gebied.spaces.active.region_3d.view_distance = 28.0   # close-up zoals winkelplaatje 4 (24), iets ruimer; 40 toonde het hoofd ervoor
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    yield 1.0
    _, gebied, _ = zijbalk()
    rv3d = gebied.spaces.active.region_3d
    rot0, loc0 = rv3d.view_rotation.copy(), rv3d.view_location.copy()
    groen = sum(1 for o in bpy.context.scene.objects if o.get("cj_passing"))
    for i in range(110):
        hoek = math.radians(-14 + 28 * zacht(i / 109))
        rv3d.view_rotation = Matrix.Rotation(hoek, 3, Vector((0, 0, 1))).to_quaternion() @ rot0
        rv3d.view_location = loc0
        gebied.tag_redraw()
        yield 0.05
        neem()
    log(f"FILM OK kogel delen_met_passing={groen}")
    deel("eind")
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
