"""Opname cc-pas (regisseur-20, Regisseur run 19, 24 nov 2026): Click Cuts Short 2 "fit test".
Script: commercie/filmpjes/scripts/click-cuts-lancering.md nr. 2 (gekeurd door Daan), hook 2A.
Echte Blender 5.3.0, X-scherm 2160x1920, UI-schaal 2, Click Cuts-zip van main (producten/blender-splitser/e2e/maak_zip.sh).
Model: Lion Head van Poly Haven (CC0), 436 mm hoog, buiten beeld gesplitst op de A1 mini (zoals cc-fit).
Verloop met de echte muis: pennen in rood (het probleem), snijvlakken met gaten, zijbalk Click Cuts, klik More settings,
scrollen naar stap 3, klik Make fit test, blok van dichtbij en van boven (gegraveerde spelingen), klik 0.25
("This one fits"), regel "Saved for this printer", keuzelijst Material naar PETG (eerder bewaard 0.30, buiten beeld gezet
in de voorkeuren) en terug naar PLA (speling springt terug naar 0.25), klik Export fit test.
Metingen in film.json: spelingen van het blok, bewaarde JSON, speling na elke wissel, bestanden, OCR-plekken.
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python cc_opname.py -- <uitmap> <zip> <map leeuw>"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403,E402
from bpy_extras import view3d_utils  # noqa: E402
import bmesh  # noqa: E402
from mathutils import Matrix  # noqa: E402

zet_naam("cc20")
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


def stukken():
    return sorted((o for o in bpy.context.scene.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])




def voorkeuren():
    for k, ad in bpy.context.preferences.addons.items():
        if k.endswith("split_joints") and ad.preferences is not None:
            return ad.preferences
    return None


def doos(obs):
    cs = [o.matrix_world @ Vector(c) for o in obs for c in o.bound_box]
    mn = Vector((min(c.x for c in cs), min(c.y for c in cs), min(c.z for c in cs)))
    mx = Vector((max(c.x for c in cs), max(c.y for c in cs), max(c.z for c in cs)))
    return mn, mx


def muis_weg():
    xdo("mousemove", "300", "1800")
    MUIS["x"], MUIS["y"] = 300, 1800


def kies_lijst(vak, label, item, waarde_ok):
    """Keuzelijst naast `label` (OCR) openen en `item` klikken met de echte muis. True als waarde_ok() daarna klopt."""
    lp = knop(label, vak)
    if not lp:
        return False, None
    veld = (vak[0] + int(vak[2] * 0.72), lp[1])
    yield from muis_naar(veld[0], veld[1], 16)
    klik()
    yield 0.8
    neem(4)
    p = None
    for _ in range(3):
        p = knop(item, (max(0, vak[0] - 900), 0, min(2160 - max(0, vak[0] - 900), vak[2] + 900), 1920))
        if p:
            break
        yield 0.4
    if p:
        yield from muis_naar(p[0], p[1], 16)
        neem(4)
        klik()
        yield 0.6
        neem(4)
    else:
        toets("Escape")
        yield 0.3
    return waarde_ok(), (lp, p)


def verloop():
    a3 = zet_scherm(mm=True)
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    sc = bpy.context.scene
    inst = sc.split_joints
    ob, maat = laad_leeuw()
    log(f"KORT leeuw {M['leeuw_mm']} vlakken {M['leeuw_vlakken']}")
    sp = a3.spaces.active
    bpy.context.preferences.system.use_region_overlap = False
    inst.printer = "A1MINI"
    inst.materiaal = "PLA"
    # eerder bewaard (buiten beeld): PETG op deze printer 0.30 mm, zodat de wissel in zin 9 iets laat terugkomen
    vk = voorkeuren()
    if vk is None:
        log("KORT FOUT geen voorkeuren van Click Cuts")
        einde()
        return
    vk.spelingen_json = json.dumps({"A1MINI|PETG": 0.3})
    inst.speling_mm = 0.2
    M["voor_json"] = vk.spelingen_json
    # buiten beeld splitsen (dat liet cc-fit al zien)
    selecteer(ob)
    bpy.ops.split_joints.split_to_fit()
    yield 1.0
    st = stukken()
    if not st:
        log("KORT FOUT split: geen stukken")
        einde()
        return
    M["stukken"] = len(st)
    M["alle_groen"] = all(o.get("sj_status") == "groen" for o in st)
    pen = [o for o in sc.objects if o.get("sj_pennen")]
    M["pennen"] = sum(int(o["sj_pennen"]) for o in pen)
    log(f"KORT split {M['stukken']} stukken, groen {M['alle_groen']}, pennen {M['pennen']}")
    for o in sc.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    sp.show_region_ui = True
    yield 1.0
    ok = yield from naar_tabblad()
    M["tabblad"] = ok
    log(f"KORT tabblad Click Cuts {ok}")
    muis_weg()
    mn, mx = doos(st)
    mid = tuple((mn + mx) / 2)
    gr = max(mx - mn)

    # hook: de pennen in rood (het probleem: past niet)
    goud = []
    for o in pen:
        for m in o.data.materials:
            if m is not None:
                goud.append((m, tuple(m.diffuse_color)))
                m.diffuse_color = (1.0, 0.05, 0.03, 1)
    if pen:
        pc = [pen[0].matrix_world @ Vector(c) for c in pen[0].bound_box]
        doel = tuple(sum(pc, Vector()) / 8)
    else:
        doel = mid
    M["pen_doel"] = [round(v, 1) for v in doel]
    cam(15, 58.0, 230.0, doel)
    yield 1.0
    deel("mooi")
    yield from stuk(80, lambda t: cam(15 + 25 * t, 58.0, 230.0 - 35 * t, doel))
    for m, kl in goud:
        m.diffuse_color = kl

    # snijvlakken met gaten van boven
    deel("gaten")
    yield from stuk(110, lambda t: cam(-30 + 40 * t, 38.0, gr * 1.5 - gr * 0.25 * t, mid))

    # More settings openen en naar stap 3 scrollen
    deel("meer")
    vak = ui_vak()
    M["ui_vak"] = vak
    ms = knop("More settings", vak)
    M["meer_ocr"] = ms
    if ms:
        yield from muis_naar(ms[0], ms[1], 18)
        neem(4)
        klik()
        yield 0.6
        neem(6)
    if not inst.meer:
        log("KORT vangnet meer: More settings via script")
        inst.meer = True
        yield 0.5
    xdo("mousemove", str(vak[0] + vak[2] // 2), str(vak[1] + vak[3] // 2))
    MUIS["x"], MUIS["y"] = vak[0] + vak[2] // 2, vak[1] + vak[3] // 2
    mf = None
    for i in range(30):
        mf = knop("Make fit test", vak)
        if mf and mf[1] < vak[1] + vak[3] * 0.62:
            break
        xdo("click", "5")
        yield 0.15
        neem(2)
    M["scroll_stappen"] = i
    M["maak_ocr"] = mf
    yield from houd(10)

    # Make fit test
    deel("maak")
    if mf:
        yield from muis_naar(mf[0], mf[1], 20)
        neem(6)
        klik()
        yield 2.0
        neem(6)
    blok = [o for o in sc.objects if o.get("sj_passing") == "blok"]
    if not blok:
        log("KORT vangnet maak: Make fit test via script")
        bpy.ops.split_joints.passing_maak()
        yield 1.0
        blok = [o for o in sc.objects if o.get("sj_passing") == "blok"]
    if not blok:
        log("KORT FOUT geen fit test")
        einde()
        return
    blok = blok[0]
    pp = [o for o in sc.objects if o.get("sj_passing") == "pennen"]
    M["spelingen"] = [round(float(s), 3) for s in blok.get("sj_spelingen", [])]
    M["blok_dicht"] = bool(blok.get("sj_gesloten"))
    M["proef_pennen"] = int(pp[0].get("sj_aantal", 0)) if pp else 0
    log(f"KORT blok spelingen {M['spelingen']} dicht {M['blok_dicht']} pennen {M['proef_pennen']}")
    yield from houd(16)
    muis_weg()

    # blok van dichtbij (leeuw even verborgen, alleen in de weergave)
    for o in st + pen:
        o.hide_set(True)
    bmn, bmx = doos([blok] + pp)
    bmid = tuple((bmn + bmx) / 2)
    bgr = max(bmx - bmn)
    M["blok_mm"] = [round(v, 1) for v in (bmx - bmn)]
    deel("blok")
    yield from stuk(90, lambda t: cam(-25 + 25 * t, 62.0 - 10 * t, bgr * 2.4 - bgr * 0.5 * t, bmid))

    # van boven: spelingen leesbaar
    kmn, kmx = doos([blok])
    kmid = tuple((kmn + kmx) / 2)
    kgr = max(kmx - kmn)
    deel("boven")
    yield from stuk(100, lambda t: cam(0, 30.0 - 12 * t, kgr * 1.9 - kgr * 0.3 * t, kmid))

    # klik op 0.25: This one fits
    deel("kies")
    vak = ui_vak()
    k25 = knop("0.25", vak)
    M["k25_ocr"] = k25
    pr = knop("Printed?", vak)
    M["printed_ocr"] = pr
    if k25:
        yield from muis_naar(k25[0], k25[1], 20)
        neem(8)
        klik()
        yield 0.6
        neem(6)
    if abs(inst.speling_mm - 0.25) > 1e-6:
        log("KORT vangnet kies: 0.25 via script")
        bpy.ops.split_joints.passing_kies(waarde=0.25)
        yield 0.4
    M["na_kies_speling"] = round(inst.speling_mm, 3)
    M["na_kies_json"] = vk.spelingen_json
    yield from houd(20)

    # Saved for this printer
    deel("bewaard")
    M["saved_ocr"] = knop("Saved for this printer", vak)
    yield from houd(50)

    # Material wisselen: PETG (bewaard 0.30) en terug naar PLA (0.25)
    deel("wissel")
    goed, plek = yield from kies_lijst(vak, "Material", "PETG", lambda: inst.materiaal == "PETG")
    M["petg_via_lijst"] = goed
    M["material_ocr"] = plek
    if not goed:
        log("KORT vangnet wissel: PETG via script")
        inst.materiaal = "PETG"
        yield 0.4
    M["petg_speling"] = round(inst.speling_mm, 3)
    yield from houd(24)
    deel("terug")
    goed, plek = yield from kies_lijst(vak, "Material", "PLA", lambda: inst.materiaal == "PLA")
    M["pla_via_lijst"] = goed
    if not goed:
        log("KORT vangnet terug: PLA via script")
        inst.materiaal = "PLA"
        yield 0.4
    M["pla_speling"] = round(inst.speling_mm, 3)
    log(f"KORT wissel PETG {M['petg_speling']} PLA {M['pla_speling']}")
    yield from houd(24)

    # Export fit test, daarna blok en pennen
    deel("export")
    ex = knop("Export fit test", vak)
    M["export_ocr"] = ex
    if ex:
        yield from muis_naar(ex[0], ex[1], 20)
        neem(6)
        klik()
        yield 1.5
        neem(6)
    besten = [o.get("sj_bestand") for o in sc.objects if o.get("sj_passing") and o.get("sj_bestand")]
    if not besten:
        log("KORT vangnet export: via script")
        bpy.ops.split_joints.passing_export()
        yield 1.0
        besten = [o.get("sj_bestand") for o in sc.objects if o.get("sj_passing") and o.get("sj_bestand")]
    M["bestanden"] = sorted(os.path.basename(b) for b in besten)
    log(f"KORT export {M['bestanden']}")
    muis_weg()
    yield from houd(10)
    deel("samen")
    yield from stuk(130, lambda t: cam(-35 + 70 * t, 60.0, bgr * 2.2, bmid))
    yield from houd(10)

    deel("eind")
    ok = (M["na_kies_speling"] == 0.25 and M["petg_speling"] == 0.3 and M["pla_speling"] == 0.25
          and M["spelingen"] == [0.15, 0.2, 0.25, 0.3] and len(M["bestanden"]) == 2)
    log(f"KORT {'OK' if ok else 'FOUT'} alles")
    einde()


start(verloop)
