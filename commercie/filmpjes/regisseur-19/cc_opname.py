"""Opname cc-fit (regisseur-19, Regisseur run 18, 24 nov 2026; run 21: lijmmeldingen gemeten en noot-regel langer in beeld, keuring Iris M1): Click Cuts Short 1 "Split to fit".
Script: commercie/filmpjes/scripts/click-cuts-lancering.md nr. 1 (gekeurd door Daan), hook 1A.
Echte Blender 5.3.0, X-scherm 2160x1920, UI-schaal 2, Click Cuts-zip van main (producten/blender-splitser/e2e/maak_zip.sh).
Model: Lion Head van Poly Haven (CC0), 436 mm hoog, zoals splitser-merk-1.
Verloop met de echte muis: leeuw met een draadkader van het bed van de A1 mini (180 mm, eigen hulpvorm, alleen in beeld),
zijbalk naar Click Cuts (Ctrl+wiel), klik op de leeuw, keuzelijst Your printer open, klik "Bambu Lab A1 mini",
klik "Split to fit", uitslagregel, Exploded view (staat standaard aan) met kleur per stuk, close-up van pennen en gaten,
klik "Export parts", camera rond de stukken.
Metingen in film.json: printer, stukken, pennen, status per stuk, bestanden, plekken van de knoppen (OCR).
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python cc_opname.py -- <uitmap> <zip> <map leeuw>"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403,E402
from bpy_extras import view3d_utils  # noqa: E402
import bmesh  # noqa: E402
from mathutils import Matrix  # noqa: E402

zet_naam("cc19")
_A = sys.argv[sys.argv.index("--") + 1:]
ZIP = _A[1] if len(_A) > 1 else "/tmp/click_cuts.zip"
LEEUW = _A[2] if len(_A) > 2 else "/tmp/mod/lion_head"
HOOGTE = 436.0
M = film["metingen"]


def zijbalk():
    _, a = gebied("VIEW_3D")
    for r in a.regions:
        if r.type == "UI":
            return a, r
    return a, None


def ui_vak():
    _, a = gebied("VIEW_3D")
    return regio_rect(a, "UI")


def scherm_punt(p):
    _, a = gebied("VIEW_3D")
    r = [x for x in a.regions if x.type == "WINDOW"][0]
    q = view3d_utils.location_3d_to_region_2d(r, a.spaces.active.region_3d, Vector(p))
    v = regio_rect(a)
    return int(v[0] + q.x), int(v[1] + v[3] - q.y)


def naar_tabblad(doel="Click Cuts"):
    w = bpy.context.window_manager.windows[0]
    for poging in range(16):
        a, r = zijbalk()
        if r.active_panel_category == doel:
            return True
        x = w.x + r.x + r.width - 8
        y = w.y + w.height - (r.y + r.height // 2)
        xdo("mousemove", str(x), str(y))
        xdo("keydown", "ctrl")
        xdo("click", "5" if poging < 7 else "4")
        xdo("keyup", "ctrl")
        yield 0.4
    return False


def laad_leeuw():
    sc = bpy.context.scene
    bpy.ops.import_scene.gltf(filepath=os.path.join(LEEUW, "lion_head_1k.gltf"))
    ob = [o for o in sc.objects if o.type == "MESH"][0]
    for o in list(sc.objects):
        if o is not ob:
            bpy.data.objects.remove(o)
    ob.name = "Lion Head"
    ob.data.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)
    zs = [v.co.z for v in ob.data.vertices]
    ob.data.transform(Matrix.Scale(HOOGTE / (max(zs) - min(zs)), 4))
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.05)
    bm.to_mesh(ob.data)
    bm.free()
    cs = [v.co for v in ob.data.vertices]
    mn = Vector((min(c.x for c in cs), min(c.y for c in cs), min(c.z for c in cs)))
    mx = Vector((max(c.x for c in cs), max(c.y for c in cs), max(c.z for c in cs)))
    ob.data.transform(Matrix.Translation(Vector((-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z))))
    for p in ob.data.polygons:
        p.use_smooth = True
    ob.data.materials.clear()
    m = bpy.data.materials.new("leeuw")
    m.diffuse_color = (0.85, 0.80, 0.72, 1)
    m.roughness = 0.6
    ob.data.materials.append(m)
    M["leeuw_mm"] = [round(v, 1) for v in (mx - mn)]
    M["leeuw_vlakken"] = len(ob.data.polygons)
    return ob, mx - mn


def maak_bed(b=180.0):
    """Draadkader van het printbed (A1 mini 180 mm), alleen voor de kijker; geen deel van het model."""
    bpy.ops.mesh.primitive_cube_add(size=b, location=(0, 0, b / 2))
    k = bpy.context.active_object
    k.name = "Print bed A1 mini"
    # proef 24 nov: display WIRE was bijna onzichtbaar; nu een dikke rode draadrand als echte vorm (6 mm; 2,5 mm was in de tweede proef nog te dun)
    md = k.modifiers.new("rand", "WIREFRAME")
    md.thickness = 6.0
    m = bpy.data.materials.new("bed_rood")
    m.diffuse_color = (1.0, 0.04, 0.02, 1)
    k.data.materials.append(m)
    k.hide_select = True
    return k


def stukken():
    return sorted((o for o in bpy.context.scene.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])


def verloop():
    a3 = zet_scherm(mm=True)
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    sc = bpy.context.scene
    ob, maat = laad_leeuw()
    log(f"KORT leeuw {M['leeuw_mm']} vlakken {M['leeuw_vlakken']}")
    bed_ob = maak_bed()
    sp = a3.spaces.active
    bpy.context.preferences.system.use_region_overlap = False
    for o in sc.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    sc.split_joints.printer = "A1"      # standaard; de kijker kiest zelf de A1 mini
    sp.show_region_ui = True
    yield 1.0
    ok = yield from naar_tabblad()
    M["tabblad"] = ok
    log(f"KORT tabblad Click Cuts {ok}")
    xdo("mousemove", "300", "1700")
    MUIS["x"], MUIS["y"] = 300, 1700
    midden = (0.0, 0.0, maat.z * 0.5)
    cam(-35, 72.0, 1150.0, midden)
    yield 1.0

    # te groot: de kop steekt boven het bed uit
    deel("mooi")
    yield from stuk(70, lambda t: cam(-35 + 25 * t, 72.0, 1150.0 - 120 * t, midden))

    # klik op de leeuw (echte muis)
    deel("kies")
    p = scherm_punt((0, -maat.y * 0.3, maat.z * 0.45))
    yield from muis_naar(p[0], p[1], 22)
    klik()
    yield 0.4
    neem(6)
    if bpy.context.view_layer.objects.active is not ob:
        log("KORT vangnet kies: leeuw via script actief")
        selecteer(ob)
    yield from houd(10)

    # keuzelijst Your printer
    deel("printer")
    vak = ui_vak()
    M["ui_vak"] = vak
    yp = ocr("printer", vak, "35%")
    M["your_printer_ocr"] = yp
    lijst = (yp[0] + 60, yp[1] + 62) if yp else None
    M["lijst_ocr"] = lijst
    gekozen = False
    if lijst:
        yield from muis_naar(lijst[0], lijst[1], 20)
        klik()
        yield 0.8
        neem(4)
        mini = None
        for _ in range(3):
            mini = ocr("mini", (vak[0] - 900, 0, vak[2] + 900, 1920), "35%")
            if mini:
                break
            yield 0.4
        M["mini_ocr"] = mini
        if mini:
            yield from muis_naar(mini[0], mini[1], 22)
            neem(6)
            klik()
            yield 0.6
            neem(6)
        else:
            toets("Escape")
            yield 0.3
    gekozen = sc.split_joints.printer == "A1MINI"
    M["printer_via_lijst"] = gekozen
    if not gekozen:
        log("KORT vangnet printer: A1 mini via script")
        sc.split_joints.printer = "A1MINI"
    yield from houd(24)

    # Split to fit
    deel("split")
    sf = knop("Split to fit", vak)
    M["split_ocr"] = sf
    if sf:
        yield from muis_naar(sf[0], sf[1], 20)
        neem(8)
        bed_ob.hide_set(True)   # het kader zou de stukken in Exploded view bedekken
        klik()
        yield 2.0
        neem(4)
    st = stukken()
    for _ in range(40):
        if st:
            break
        yield 1.0
        st = stukken()
    if not st:
        log("KORT vangnet split: Split to fit via script")
        bed_ob.hide_set(True)
        selecteer(ob)
        bpy.ops.split_joints.split_to_fit()
        yield 1.0
        st = stukken()
    if not st:
        log("KORT FOUT split: geen stukken")
        einde()
        return
    M["stukken"] = len(st)
    M["status"] = [o.get("sj_status") for o in st]
    M["pennen"] = sum(int(o["sj_pennen"]) for o in sc.objects if o.get("sj_pennen"))
    M["speling_mm"] = round(sc.split_joints.speling_mm, 3)
    M["alle_groen"] = all(s == "groen" for s in M["status"])
    M["uit_elkaar"] = bool(sc.split_joints.uit_elkaar)
    log(f"KORT split {M['stukken']} stukken, groen {M['alle_groen']}, pennen {M['pennen']}")
    xdo("mousemove", str(vak[0] + 60), "1800")
    MUIS["x"], MUIS["y"] = vak[0] + 60, 1800
    yield 0.6

    # uitslag in het paneel en de stukken
    deel("uitslag")
    M["uitslag_ocr"] = ocr("fit the bed", vak, "35%")
    # keuring Iris 24 nov M1: de lijmmeldingen meten en de noot-regel in het paneel vinden (nieuwe zip, 8de5e36)
    meld = [r for r in (getattr(sc.split_joints, "meldingen", "") or "").split("\n") if r.strip()]
    M["meldingen"] = meld
    M["noot_ocr"] = ocr("glue joints", vak, "35%") if meld else None
    log(f"KORT meldingen {len(meld)} noot {M['noot_ocr']}")
    yield from houd(80)
    cs = [o.matrix_world @ Vector(c) for o in st for c in o.bound_box]
    mn = Vector((min(c.x for c in cs), min(c.y for c in cs), min(c.z for c in cs)))
    mx = Vector((max(c.x for c in cs), max(c.y for c in cs), max(c.z for c in cs)))
    mid2 = tuple((mn + mx) / 2)
    gr = max(mx - mn)
    deel("uit")
    yield from stuk(110, lambda t: cam(-10 + 50 * t, 70.0, gr * 2.4 - gr * 0.3 * t, mid2))

    # pennen en gaten van dichtbij: het penplaatje of het midden van een stuk
    deel("pen")
    pen = [o for o in sc.objects if o.get("sj_pennen")]
    if pen:
        pc = [pen[0].matrix_world @ Vector(c) for c in pen[0].bound_box]
        doel = tuple(sum(pc, Vector()) / 8)
    else:
        doel = tuple(st[0].matrix_world.translation)
    M["pen_doel"] = [round(v, 1) for v in doel]
    yield from stuk(90, lambda t: cam(20 + 30 * t, 55.0, 260.0 - 40 * t, doel))

    # Export parts
    deel("export")
    cam(30, 70.0, gr * 2.2, mid2)
    yield 0.4
    ex = knop("Export parts", vak)
    M["export_ocr"] = ex
    if ex:
        yield from muis_naar(ex[0], ex[1], 20)
        neem(6)
        klik()
        yield 2.0
        neem(6)
    besten = [o.get("sj_bestand") for o in sc.objects if o.get("sj_bestand")]
    if not besten:
        log("KORT vangnet export: via script")
        bpy.ops.split_joints.exporteer()
        yield 1.0
        besten = [o.get("sj_bestand") for o in sc.objects if o.get("sj_bestand")]
    M["bestanden"] = len(besten)
    M["bestand_voorbeeld"] = [os.path.basename(b) for b in sorted(besten)[:3]]
    log(f"KORT export {len(besten)} bestanden {M['bestand_voorbeeld']}")
    yield from houd(30)

    # weer in elkaar, kleuren zichtbaar
    deel("samen")
    sc.split_joints.uit_elkaar = False
    xdo("mousemove", "300", "1800")
    MUIS["x"], MUIS["y"] = 300, 1800
    yield 0.6
    yield from stuk(110, lambda t: cam(-30 + 60 * t, 74.0, 1000.0 - 100 * t, midden))
    yield from houd(20)

    deel("eind")
    log("KORT OK alles")
    einde()


start(verloop)
