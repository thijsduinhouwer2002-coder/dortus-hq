"""Opname voor YouTube-video 1 van Click Joints Pro (Chris, 19 nov 2026, opdracht hoofdchat 09:20 NL).
    blender --gpu-backend opengl start.blend --python commercie/filmpjes/youtube-pro/opname.py -- <map> <betaalde zip>
Echte beelden: de betaalde add-on in de echte Blender, het hele X-scherm per filmbeeld (1920x1080, 30 fps).
De hulpjes (neem, deel, camera, maak_been ...) komen ongewijzigd uit producten/blender-gewrichten/e2e/film_pro.py
(alles vóór 'def verloop'), zodat beeld en instellingen gelijk zijn aan de demofilm die Daan keurde.
Het script kleurt niets: groen, rood en de gradenboog komen van de add-on. Het zet alleen de camera en de
Bend-schuif zoals een gebruiker hem sleept, en roept de knop Place hinge aan met 90, 115 of 135 graden.
Uit: <map>/beelden/b00001.png ... en <map>/film.json (eerste beeld per deel en gemeten bereik per stand).
Regels "UITLEG OK <deel>" eist de workflow."""
import json
import math
import os
import sys

E2E = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "producten", "blender-gewrichten", "e2e")
E2E = os.path.abspath(E2E)
sys.path.insert(0, E2E)
_bron = open(os.path.join(E2E, "film_pro.py"), encoding="utf-8").read()
_bron = _bron[:_bron.index("def verloop():")].replace(
    "sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))", "")
exec(compile(_bron, "film_pro_hulp", "exec"), globals())   # noqa: S102 (eigen code uit de repo)

VOORBIJ = 9.5
ROOD_AFSTAND = 40.0
ROOD_PLEK = Vector((-3.0, 0, 2.0))
film["standen"] = {}
film["metingen"] = {}


def scharnier_stand(stand):
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand=str(stand))
    a, b = bpy.data.objects.get("been_A"), bpy.data.objects.get("been_B")
    sp.staat["a"], sp.staat["b"] = a, b
    log(f"UITLEG plaats {stand}: {uitslag} A={a is not None} B={b is not None} "
        f"bereik={a.get('cj_bereik_graden') if a else None} melding={a.get('cj_melding') if a else None}")
    if a is not None:
        film["standen"][str(stand)] = float(a["cj_bereik_graden"])
    return a, b


def stuk(stappen, doe):
    """stappen beelden, elk na een tekenmoment; doe(t) met t van 0 tot 1 (zacht)."""
    for i in range(stappen):
        doe(zacht(i / max(1, stappen - 1)))
        yield 0.05
        neem()


def verloop():
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
    h, buig, lidas = Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0))
    midden = Vector((8.0, 0, 10.0))
    kijk = lambda zij, hoog=HOOGTE: kijkrot(h, lidas, buig, zij, hoog)  # noqa: E731

    # 0 haak: de knie buigt tot de stop, met de boog (zoals de poster)
    deel("haak")
    a, b = scharnier_stand(115)
    if a is None:
        bpy.ops.wm.quit_blender()
        return
    sp.deselecteer()
    wm.cj_scharnier_boog = True
    stop = float(a["cj_bereik_graden"])
    camera(kijk(20), AFSTAND, midden)
    sp.zet(0.0)
    yield 1.0
    yield from stuk(60, lambda t: (sp.zet(round(stopwaarde(stop) * t, 1)), camera(kijk(26 - 6 * t), AFSTAND, midden)))
    neem(45)
    log("UITLEG OK haak")

    # 1 heel: één stuk, rustig rond, de zijbalk met het paneel staat rechts
    wm.cj_scharnier_boog = False
    maak_been()
    yield 1.0
    deel("heel")
    yield from stuk(180, lambda t: camera(kijk(50 - 30 * t), AFSTAND, midden))
    neem(90)
    log("UITLEG OK heel")

    # 2 knop: Place hinge 115 (de knop in de zijbalk), dan stil op het paneel
    a, b = scharnier_stand(115)
    if a is None:
        bpy.ops.wm.quit_blender()
        return
    sp.deselecteer()
    wm.cj_scharnier_boog = True
    wm.cj_scharnier_pose = 0.0
    yield 1.0
    deel("knop")
    neem(210)
    log("UITLEG OK knop")

    # 3 rond: het gesneden scharnier op 0 graden van twee kanten
    deel("rond")
    yield from stuk(150, lambda t: camera(kijk(20 + 40 * math.sin(math.pi * t)), AFSTAND, midden))
    neem(30)
    log("UITLEG OK rond")

    # 4 buig: de schuif van 0 naar de stop in 6 s, dan stil
    deel("buig")
    stop = float(a["cj_bereik_graden"])
    yield from stuk(180, lambda t: sp.zet(round(stopwaarde(stop) * t, 1)))
    neem(150)
    film["metingen"]["buig_stop"] = stop
    log(f"UITLEG OK buig tot {a.get('cj_pose_graden')} bereik {stop}")

    # 5 rood: recht op de stop, B half doorzichtig, 9,5 graden voorbij, lang stil
    deel("rood")
    knie = Vector(a["cj_scharnier_punt"])
    r0, r1 = kijk(20), kijk(20, 50)
    sp.doorzichtig_b()
    yield from stuk(45, lambda t: camera(r0.slerp(r1, t), AFSTAND + (ROOD_AFSTAND - AFSTAND) * t,
                                        midden.lerp(knie + ROOD_PLEK, t)))
    rood = [0]
    yield from stuk(60, lambda t: rood.__setitem__(0, sp.zet(round(stop + VOORBIJ * t, 2))))
    yield 0.5
    neem(150)
    film["metingen"]["rood_vlakken"] = rood[0]
    log(f"UITLEG {'OK' if rood[0] > 0 else 'FOUT'} rood rood_vlakken={rood[0]}")

    # 6 terug: binnen het bereik is het rood weg
    deel("terug")
    na = [0]
    yield from stuk(60, lambda t: na.__setitem__(0, sp.zet(round(stop + VOORBIJ - (VOORBIJ + 15) * t, 2))))
    neem(120)
    film["metingen"]["rood_na_terug"] = na[0]
    log(f"UITLEG {'OK' if na[0] == 0 else 'FOUT'} terug rood_vlakken={na[0]}")

    # 7 en 8: dezelfde knie met 90 en 135 graden
    for stand in (90, 135):
        wm.cj_scharnier_boog = False
        maak_been()
        camera(kijk(20), AFSTAND, midden)
        yield 1.0
        a, b = scharnier_stand(stand)
        if a is None:
            bpy.ops.wm.quit_blender()
            return
        sp.deselecteer()
        wm.cj_scharnier_boog = True
        sp.zet(0.0)
        yield 1.0
        deel(f"stand{stand}")
        neem(45)
        s = float(a["cj_bereik_graden"])
        yield from stuk(150, lambda t, s=s: sp.zet(round(stopwaarde(s) * t, 1)))
        neem(90)
        r = [0]
        yield from stuk(30, lambda t, s=s: r.__setitem__(0, sp.zet(round(s + VOORBIJ * t, 2))))
        neem(75)
        film["metingen"][f"rood_{stand}"] = r[0]
        log(f"UITLEG {'OK' if r[0] > 0 else 'FOUT'} stand{stand} bereik {s} rood_vlakken={r[0]}")

    # 9 kogel: Place joint uit de gratis versie (zit ook in Pro), groene pasband, rustig rond
    deel("kogel")
    wm.cj_scharnier_boog = False
    maak_been()
    inst = bpy.context.scene.click_joints
    inst.kogel_auto = True
    inst.uit_elkaar = True
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    groen = sum(1 for o in delen if o.get("cj_passing"))
    film["metingen"]["kogel_passing"] = groen
    log(f"UITLEG kogel plaats: {uitslag} {len(delen)} delen, passing {groen}")
    deelA = next((d for d in delen if d.get("cj_deel") == "A"), None)
    kmid = Vector(deelA["cj_centrum"]) + Vector(deelA["cj_as"]).normalized() * (1.5 * deelA["cj_kogel_r"]) if deelA else Vector()
    yield 1.0
    yield from stuk(180, lambda t: camera(kijk(15 + 20 * t, 15.0), 60.0, kmid + Vector((6.0, 0, 0))))
    neem(30)
    log(f"UITLEG {'OK' if groen > 0 else 'FOUT'} kogel delen_met_passing={groen}")
    deel("eind")
    with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"UITLEG klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
