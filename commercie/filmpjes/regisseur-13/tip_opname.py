"""Opname tip-dubbel (regisseur-13, Regisseur run 13, 24 nov 2026): een vaas die stiekem uit twee losse stukken bestaat
(dubbele punten op de naad). Echte Blender 5.3.0, X-scherm 2160x1920, UI-schaal 2, geen add-on.
Verloop met de echte muis en toetsen: Tab, 3, muis op de bovenkant, L (alleen de bovenkant licht op), A, M, By Distance
(Blender meldt Removed N vertices), Alt A, L opnieuw (nu de hele vaas). Metingen in film.json: punten, losse randen
(boundary) en geselecteerde vlakken voor en na.
Hulpcode: ../opname/blender_opname.py (LEESMIJ daar).
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python tip_opname.py -- <uitmap>"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403,E402
from bpy_extras import view3d_utils  # noqa: E402

zet_naam("tip13")
MAP = "/tmp/tip13"
SEG, RINGEN, STAP, NAAD = 48, 13, 5.0, 6      # 48 punten per ring, z van 0 tot 60 mm, naad op ring 6 (z 30 mm)


def straal(z):
    return 15.0 + 7.0 * math.sin(math.pi * z / 60.0) - 3.0 * math.sin(math.pi * z / 30.0) * (z > 40)


def maak_vaas():
    """Vaas van 60 mm hoog, gesloten, glad gekleurd. Ring 6 bestaat twee keer: onderdeel en bovendeel delen geen punten."""
    me = bpy.data.meshes.new("vaas")
    ob = bpy.data.objects.new("Vase", me)
    bpy.context.scene.collection.objects.link(ob)
    bm = bmesh.new()
    ringen = []
    for i in range(RINGEN):
        z = i * STAP
        kopie = 2 if i == NAAD else 1
        for _ in range(kopie):
            r = straal(z)
            ringen.append((i, [bm.verts.new((r * math.cos(2 * math.pi * k / SEG), r * math.sin(2 * math.pi * k / SEG), z))
                               for k in range(SEG)]))
    # volgorde: ring 0..5, 6a, 6b, 7..12; onderdeel gebruikt 6a, bovendeel 6b
    lijst = [v for _, v in ringen]
    onder = lijst[:NAAD + 1]
    boven = lijst[NAAD + 1:]
    for deelringen in (onder, boven):
        for a, b in zip(deelringen, deelringen[1:]):
            for k in range(SEG):
                bm.faces.new((a[k], a[(k + 1) % SEG], b[(k + 1) % SEG], b[k]))
    bm.faces.new(list(reversed(lijst[0])))
    bm.faces.new(lijst[-1])
    for f in bm.faces:
        f.smooth = True
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()
    m = bpy.data.materials.new("vaas")
    m.diffuse_color = (0.42, 0.68, 0.92, 1)
    m.roughness = 0.45
    me.materials.append(m)
    selecteer(ob)
    return ob


def tel(ob):
    """Punten, losse randen en geselecteerde vlakken (in Edit Mode uit de bmesh, anders uit de mesh)."""
    if ob.mode == "EDIT":
        bm = bmesh.from_edit_mesh(ob.data)
        return {"punten": len(bm.verts), "losse_randen": sum(1 for e in bm.edges if e.is_boundary),
                "vlakken": len(bm.faces), "gekozen": sum(1 for f in bm.faces if f.select)}
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    d = {"punten": len(bm.verts), "losse_randen": sum(1 for e in bm.edges if e.is_boundary), "vlakken": len(bm.faces)}
    bm.free()
    return d


def scherm_punt(a, co):
    """Schermpixel (x, y van boven) van een 3D-punt in de 3D-weergave."""
    reg = [r for r in a.regions if r.type == "WINDOW"][0]
    p = view3d_utils.location_3d_to_region_2d(reg, a.spaces.active.region_3d, Vector(co))
    rx, ry, _, rh = regio_rect(a)
    return int(rx + p.x), int(ry + rh - p.y)


def voorkant(a, z):
    """Punt op het vaasoppervlak op hoogte z, aan de kant naar de kijker."""
    kijk = a.spaces.active.region_3d.view_rotation @ Vector((0, 0, 1))
    hoek = math.atan2(kijk.y, kijk.x)
    r = straal(z) - 0.5
    return (r * math.cos(hoek), r * math.sin(hoek), z)


def verloop():
    a = zet_scherm()
    os.makedirs(MAP, exist_ok=True)
    sp = a.spaces.active
    sp.clip_start, sp.clip_end = 0.5, 20000.0
    yield 1.0
    film["metingen"]["weergave"] = regio_rect(a)
    w = bpy.context.window_manager.windows[0]
    reg = [x for x in a.regions if x.type == "WINDOW"][0]
    with bpy.context.temp_override(window=w, area=a, region=reg):
        ob = maak_vaas()
    film["metingen"]["d_maat_mm"] = maat_mm(ob, 1)
    film["metingen"]["d_voor"] = tel(ob)
    log(f"KORT meting vaas {film['metingen']['d_maat_mm']} mm, {film['metingen']['d_voor']}")
    herteken()
    yield 0.8
    kop = regio_rect(a, "HEADER")
    film["metingen"]["kop"] = kop
    mid = Vector((0, 0, 30))
    cam(20, 66, 190, mid)
    yield 0.5
    if os.environ.get("CJ_KIJK"):
        subprocess.run(["import", "-window", "root", os.path.join(uitmap, "kijk.png")])
        bpy.ops.wm.quit_blender()
        return
    yield from muis_naar(*zachte_muis_in_beeld(), 4)

    deel("d_mooi")      # haakbeeld: de vaas draait langzaam, licht op de naad
    yield from stuk(120, lambda t: cam(20 + 50 * t, 66 + 8 * t, 190 - 40 * t, mid))
    log("KORT OK d_mooi")

    deel("d_l1")        # Tab, 3, muis op de bovenkant, L: alleen de bovenkant licht op
    toets("Tab")
    yield 0.6
    neem(8)
    toets("3")
    yield 0.4
    neem(6)
    film["metingen"]["d_edit"] = ob.mode == "EDIT"
    p = scherm_punt(a, voorkant(a, 46))
    film["metingen"]["d_muis_boven"] = p
    yield from muis_naar(*p, 16)
    yield from houd(10)
    toets("l")
    yield 0.5
    neem(6)
    t1 = tel(ob) if ob.mode == "EDIT" else {}
    film["metingen"]["d_l1"] = t1
    if not t1 or not t1.get("gekozen"):
        log("KORT vangnet d_l1: niets gekozen met L")
    log(f"KORT meting na L: {t1}")
    yield from houd(110)
    log("KORT OK d_l1")

    deel("d_merge")     # A, M, By Distance
    toets("a")
    yield 0.4
    neem(6)
    yield from houd(24)
    voor = tel(ob)
    mx, my = MUIS["x"], MUIS["y"]
    toets("m")
    q = yield from wacht_ocr("By Distance", [max(0, mx - 700), max(0, my - 900), 1400, 1500], (mx, my))
    film["metingen"]["d_menu_item"] = q
    via_menu = False
    if q:
        yield from muis_naar(q[0], q[1], 14)
        neem(6)
        klik()
        yield 0.8
        neem(6)
        via_menu = tel(ob)["punten"] < voor["punten"]
    film["metingen"]["d_via_menu"] = via_menu
    if not via_menu:
        log("KORT vangnet d_merge: Merge by Distance via script")
        toets("Escape")
        with bpy.context.temp_override(window=w, area=a, region=reg):
            bpy.ops.mesh.remove_doubles(threshold=0.0001)
        herteken()
    na = tel(ob)
    film["metingen"]["d_merge_voor"], film["metingen"]["d_merge_na"] = voor, na
    film["metingen"]["d_weg"] = voor["punten"] - na["punten"]
    yield 0.3
    neem(4)
    onder = [0, 1700, 2160, 220]
    film["metingen"]["d_removed_ocr"] = ocr("Removed", onder, "35%") or ocr("Removed", onder, "60%")
    log(f"KORT meting merge: weg {film['metingen']['d_weg']}, voor {voor}, na {na}")
    yield from houd(90)
    log("KORT OK d_merge")

    deel("d_l2")        # Alt A, muis op de bovenkant, L: nu licht de hele vaas op
    toets("alt+a")
    yield 0.4
    neem(6)
    yield from houd(16)
    p2 = scherm_punt(a, voorkant(a, 46))
    film["metingen"]["d_muis_boven_2"] = p2
    yield from muis_naar(p2[0] + 6, p2[1] + 4, 8)
    toets("l")
    yield 0.5
    neem(6)
    t2 = tel(ob)
    film["metingen"]["d_l2"] = t2
    log(f"KORT meting na merge en L: {t2}")
    yield from houd(110)
    log("KORT OK d_l2")

    deel("d_klaar")     # Tab terug, rustig eindbeeld, de naad is weg
    toets("Tab")
    yield 0.5
    neem(4)
    film["metingen"]["d_na_object"] = tel(ob)
    yield from muis_naar(*zachte_muis_in_beeld(), 8)
    yield from stuk(150, lambda t: cam(70 + 60 * t, 74 - 8 * t, 150 + 10 * t, mid))
    yield from houd(30)
    log("KORT OK d_klaar")

    deel("eind")
    einde()


start(verloop)
