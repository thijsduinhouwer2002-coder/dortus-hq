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
Regels "FILM OK <deel>" zijn wat de workflow eist.
Staande stand (FILM_STAAND=1, opdracht hoofdchat 15 nov 23:00, voor de korte filmpjes van Chris): zelfde verloop, maar
op een X-scherm van 1080x1920, zonder zijbalk en met de camera dichter op de knie. maak_staand.sh knipt er losse
opnames van per deel uit (zonder tekst; Chris zet de onderschriften)."""
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
AFSTAND = float(os.environ.get("FILM_AFSTAND", "100"))   # v2 (Daan M1): been ±60% van de breedte (v1: 95 gaf ±35%)
HOOGTE = 8.0     # v2: camera iets lager dan v1 (15)
STAAND = os.environ.get("FILM_STAAND") == "1"
if STAAND:
    AFSTAND = float(os.environ.get("FILM_AFSTAND", "68"))
SNEL = int(os.environ.get("FILM_SNEL", "1"))   # proef: alleen elk n-de beeld echt opnemen (sneller kijken)
# Thema-achtergrond als zachte verloop zoals de poster (Daan M1); de add-on zelf blijft ongemoeid.
BOVEN, ONDER = (0x2B / 255, 0x2F / 255, 0x38 / 255), (0x1D / 255, 0x20 / 255, 0x27 / 255)
beeldmap = os.path.join(scherm_basis.uitmap, "beelden")
os.makedirs(beeldmap, exist_ok=True)
film = {"fps": FPS, "delen": {}, "n": 0}


def neem(houd=1):
    """Pak het hele X-scherm als volgend filmbeeld; houd > 1 herhaalt hetzelfde beeld (stilstaand stuk)."""
    film["n"] += 1
    pad = os.path.join(beeldmap, f"b{film['n']:05d}.png")
    if SNEL == 1 or film["n"] % SNEL == 0 or houd > 1:
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


def verloop_achtergrond():
    """Viewport-achtergrond uit het thema: lineaire verloop #2b2f38 boven naar #1d2027 onder (alleen deze sessie)."""
    _, gebied, _ = zijbalk()
    if gebied:
        gebied.spaces.active.shading.background_type = "THEME"
    gr = bpy.context.preferences.themes[0].view_3d.space.gradients
    gr.background_type = "LINEAR"
    gr.high_gradient = BOVEN
    gr.gradient = ONDER


def leeg_beeld():
    """Alleen de 3D-weergave over het hele scherm, verloop als achtergrond, geen raster en assen; zijbalk aan."""
    bpy.context.preferences.view.ui_scale = UI_SCHAAL   # zijbalk leesbaar in de film (alleen deze sessie)
    sp.schoon_beeld()
    verloop_achtergrond()
    zijbalk_aan(True)


def cursor_knie():
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):  # H, buigkant, lidas
        m.col[i][:3] = v
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m


def maak_been():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    lid = sp.been()
    figuren.maak_actief(lid)
    cursor_knie()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.toon_bereik = sp.SPELING, "CURSOR", False, False
    return lid


def scharnier():
    """Place hinge met 115°, zoals de knop in de zijbalk; geeft (A, B) of (None, None)."""
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("been_A"), bpy.data.objects.get("been_B")
    sp.staat["a"], sp.staat["b"] = a, b
    log(f"FILM plaats: {uitslag} A={a is not None} B={b is not None} "
        f"bereik={a.get('cj_bereik_graden') if a else None} melding={a.get('cj_melding') if a else None}")
    return a, b


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


def stopwaarde(stop):
    return math.floor(stop * 10) / 10   # nooit voorbij de stop (115,0 tegen 114,96 is al rood)


def verloop():
    """De hele film als reeks stappen; elke yield geeft Blender tijd om te tekenen voor het volgende beeld."""
    wm = bpy.context.window_manager
    log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    maak_been()
    weergave()
    leeg_beeld()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    _, _, regio = zijbalk()
    log(f"FILM tabblad {'OK' if regio and regio.active_panel_category == scherm_basis.DOEL else 'NIET GELUKT'}")
    if STAAND:
        zijbalk_aan(False)   # staand: geen zijbalk, het gewricht vult de breedte
        yield 0.5
    h, buig, lidas = Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0))
    # Midden van het beeld: iets links van de knie (de zijbalk ligt rechts) en iets omhoog voor de gebogen scheen.
    midden = Vector((8.0, 0, 10.0)) if not STAAND else MIDDEN_STAAND
    kijk_buig = kijkrot(h, lidas, buig, 20, HOOGTE)
    # 0 haak (Daan M4): eerst de knie die door zijn bereik buigt met de boog, zoals de poster (±1,6 s)
    deel("haak")
    a, b = scharnier()
    if a is None or b is None:
        bpy.ops.wm.quit_blender()
        return
    sp.deselecteer()
    wm.cj_scharnier_boog = True
    stop = float(a["cj_bereik_graden"])
    camera(kijk_buig, AFSTAND, midden)
    sp.zet(0.0)
    yield 1.0
    for i in range(48):
        sp.zet(round(stopwaarde(stop) * zacht(i / 47), 1))
        camera(kijkrot(h, lidas, buig, 26 - 6 * zacht(i / 47), HOOGTE), AFSTAND, midden)
        yield 0.05
        neem()
    neem(12)
    log(f"FILM OK haak tot {b.get('cj_pose_graden')}")
    # 1 plaats: weer het hele been als één stuk, draait kort, dan Place hinge met 115°
    wm.cj_scharnier_boog = False
    maak_been()
    yield 1.0
    deel("plaats")
    for i in range(54):
        camera(kijkrot(h, lidas, buig, 40 - 20 * zacht(i / 53), HOOGTE), AFSTAND, midden)
        yield 0.05
        neem()
    a, b = scharnier()
    if a is None or b is None:
        bpy.ops.wm.quit_blender()
        return
    sp.deselecteer()
    wm.cj_scharnier_boog = True
    wm.cj_scharnier_pose = 0.0
    sp.deselecteer()
    yield 1.0
    deel("knop")
    neem(45)
    log(f"FILM OK plaats groen={a.get('cj_band_vlakken', 0)},{b.get('cj_band_vlakken', 0)}")
    # 2 buig: de schuif van 0 naar de stop in 3,5 s, dan 1 s stil
    deel("buig")
    stop = float(a["cj_bereik_graden"])
    for i in range(106):
        sp.zet(round(stopwaarde(stop) * zacht(i / 105), 1))
        yield 0.05
        neem()
    neem(30)
    log(f"FILM OK buig tot {b.get('cj_pose_graden')} bereik {stop}")
    # 3 rood (Daan M3): camera recht op de stop zoals winkelplaatje 14, B half doorzichtig, 7° voorbij, 1,5 s stil
    deel("rood")
    knie = Vector(a["cj_scharnier_punt"])
    r1 = kijkrot(h, lidas, buig, 20, 50)
    sp.doorzichtig_b()
    for i in range(30):
        t = zacht(i / 29)
        camera(kijk_buig.slerp(r1, t), AFSTAND + (ROOD_AFSTAND - AFSTAND) * t, midden.lerp(knie + ROOD_PLEK, t))
        yield 0.05
        neem()
    rood = 0
    for i in range(21):
        rood = sp.zet(round(stop + VOORBIJ * i / 20, 2))
        yield 0.05
        neem()
    yield 0.5
    neem(45)
    log(f"FILM {'OK' if rood > 0 else 'FOUT'} rood rood_vlakken={rood}")
    # 4 kogel (Daan M2): Place joint in hetzelfde been (huidkleur, glad), groene pasband, het hele gewricht in beeld
    deel("kogel")
    wm.cj_scharnier_boog = False
    maak_been()
    inst = bpy.context.scene.click_joints
    inst.kogel_auto = True
    inst.uit_elkaar = True
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
    for d in delen:
        log(f"FILM kogeldeel {d.name} passing={d.get('cj_passing')} wand={d.get('cj_wand_mm')}")
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    groen = sum(1 for o in delen if o.get("cj_passing"))
    log(f"FILM kogel plaats: {uitslag} {len(delen)} delen kogel {inst.kogel_mm} mm")
    deelA = next((d for d in delen if d.get("cj_deel") == "A"), None)
    kmid = Vector(deelA["cj_centrum"]) if deelA else Vector((0, 0, 0))
    if deelA:
        kmid = kmid + Vector(deelA["cj_as"]).normalized() * (1.5 * deelA["cj_kogel_r"])
    yield 1.0
    for i in range(100):
        t = zacht(i / 99)
        camera(kijkrot(h, lidas, buig, KOGEL_ZIJ - 10 + 20 * t, KOGEL_HOOGTE), KOGEL_AFSTAND, kmid + KOGEL_PLEK)
        yield 0.05
        neem()
    log(f"FILM OK kogel delen_met_passing={groen}")
    deel("eind")
    with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"FILM klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


VOORBIJ = 9.5                                   # Daan M3: 6 tot 8° voorbij de stop; v3 (Daan kan 3): 2 tot 3° verder, rood groter
ROOD_AFSTAND = float(os.environ.get("FILM_ROOD_AFSTAND", "40"))
ROOD_PLEK = Vector((-3.0, 0, 2.0))              # beeldmidden iets links van de knie (zijbalk rechts)
KOGEL_AFSTAND = float(os.environ.get("FILM_KOGEL_AFSTAND", "60"))
KOGEL_ZIJ, KOGEL_HOOGTE = 25.0, 15.0
KOGEL_PLEK = Vector((6.0, 0, 0))
MIDDEN_STAAND = Vector([float(x) for x in os.environ.get("FILM_MIDDEN", "-4,0,14").split(",")])
if STAAND:   # geen zijbalk rechts, dus niets naar links schuiven; het rood en de kogel iets dichterbij
    ROOD_PLEK = Vector((5.0, 0, 3.0))   # gradenboog loopt naar rechts: beeldmidden iets rechts van de knie
    ROOD_AFSTAND = float(os.environ.get("FILM_ROOD_AFSTAND", "46"))
    KOGEL_PLEK = Vector((0.0, 0, 0))
    KOGEL_AFSTAND = float(os.environ.get("FILM_KOGEL_AFSTAND", "45"))


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
