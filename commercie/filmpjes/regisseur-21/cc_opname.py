"""Opname cc-nummers (regisseur-21, Regisseur run 20, 24 nov 2026): Click Cuts Short 3 "nummers in elk snijvlak".
Script: commercie/filmpjes/scripts/click-cuts-lancering.md nr. 3 (gekeurd door Daan), hook 3A.
Echte Blender 5.3.0, X-scherm 2160x1920, UI-schaal 2, Click Cuts-zip van main (producten/blender-splitser/e2e/maak_zip.sh).
Model: Lion Head van Poly Haven (CC0), 436 mm hoog, buiten beeld gesplitst op de A1 mini (zoals cc-fit en cc-pas).
Verloop: hoop grijze stukken op tafel (het probleem), Exploded view met de echte objectnamen Piece 01.. van onder naar
boven, klik Export parts, klik More settings en scrollen naar Engrave numbers / Depth, dan close-ups van de echte
gegraveerde nummers (camera loodrecht op het snijvlak, zelfde assenstelsel als vormen.label_frame), twee buren
("a-b" en "b-a"), buitenkant van hetzelfde stuk, een vlak met gaten en het nummer ertussen, het kleinste nummer.
Metingen in film.json: stukken, labels per stuk, gekozen labels, hoogtes, bestanden, OCR-plekken.
    xvfb-run -s "-screen 0 2160x1920x24" blender --gpu-backend opengl --python cc_opname.py -- <uitmap> <zip> <map leeuw>"""
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "opname"))
from blender_opname import *  # noqa: F401,F403,E402
import bmesh  # noqa: E402
from mathutils import Matrix  # noqa: E402

zet_naam("cc21")
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
    return ob


def stukken():
    return sorted((o for o in bpy.context.scene.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])


def doos(obs):
    cs = [o.matrix_world @ Vector(c) for o in obs for c in o.bound_box]
    mn = Vector((min(c.x for c in cs), min(c.y for c in cs), min(c.z for c in cs)))
    mx = Vector((max(c.x for c in cs), max(c.y for c in cs), max(c.z for c in cs)))
    return mn, mx


def muis_weg():
    xdo("mousemove", "300", "1800")
    MUIS["x"], MUIS["y"] = 300, 1800


def frame(as_, teken, richting=None):
    """Zelfde assenstelsel als split_joints/vormen.label_frame: (rechts, op, normaal)."""
    n = Vector((0.0, 0.0, 0.0))
    n[as_] = float(teken)
    op = Vector((0.0, 0.0, 1.0)) if as_ != 2 else Vector((0.0, 1.0, 0.0))
    rechts = op.cross(n)
    if richting is not None:
        r = Vector(richting)
        r = (r - n * r.dot(n)).normalized()
        if r.length > 0.5:
            if r.dot(rechts) < 0:
                r = -r
            rechts = r
            op = n.cross(rechts)
    return rechts, op, n


def kijk_op(lb, ob, afstand, kanteling=0.0, zij=0.0):
    """Camera loodrecht op het label (tekst leesbaar, niet gespiegeld), iets gekanteld voor diepte."""
    rechts, op, n = frame(lb["as"], lb["teken"], lb.get("richting"))
    rot = Matrix((rechts, op, n)).transposed()
    rot = rot @ Matrix.Rotation(math.radians(kanteling), 3, "X") @ Matrix.Rotation(math.radians(zij), 3, "Y")
    _, a = gebied("VIEW_3D")
    r3 = a.spaces.active.region_3d
    r3.view_perspective = "PERSP"
    r3.view_rotation = rot.to_quaternion()
    r3.view_distance = afstand
    r3.view_location = ob.matrix_world @ Vector(lb["p"])
    herteken()


def kijk_richting(d, afstand, punt, extra=0.0):
    d = Vector(d).normalized()
    k = math.degrees(math.acos(max(-1.0, min(1.0, d.z))))
    t = math.degrees(math.atan2(d.x, -d.y))
    cam(t + extra, k, afstand, punt)


def alleen(obs):
    for o in bpy.context.scene.objects:
        if o.type == "MESH":
            o.hide_set(o not in obs)


def gaten_bij(ob, lb):
    """Gaten op hetzelfde snijvlak als dit label (zelfde as, teken en buur)."""
    buur = int(lb["tekst"].split("-")[1])
    uit = []
    for g in json.loads(ob.get("sj_gaten", "[]")):
        if g["as"] == lb["as"] and g["teken"] == lb["teken"] and int(g["buur"]) == buur:
            uit.append(g)
    return uit


def verloop():
    a3 = zet_scherm(mm=True)
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    sc = bpy.context.scene
    inst = sc.split_joints
    ob = laad_leeuw()
    sp = a3.spaces.active
    bpy.context.preferences.system.use_region_overlap = False
    inst.printer = "A1MINI"
    inst.materiaal = "PLA"
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
    M["engrave"] = bool(inst.labels)
    M["diepte_mm"] = round(inst.label_diepte_mm, 2)
    pen = [o for o in sc.objects if o.get("sj_pennen")]
    labels = {int(o["sj_stuk"]): json.loads(o.get("sj_labels", "[]")) for o in st}
    M["labels_per_stuk"] = {k: len(v) for k, v in labels.items()}
    M["label_hoogtes"] = sorted({lb["h"] for v in labels.values() for lb in v})
    log(f"KORT split {M['stukken']} stukken, groen {M['alle_groen']}, labels {sum(M['labels_per_stuk'].values())}, "
        f"hoogtes {M['label_hoogtes']}")
    if M["stukken"] != 12:
        log("KORT FOUT niet 12 stukken: zin 1 zegt twelve")  # script 3: 'Twelve' alleen als het echt 12 is
        einde()
        return
    for o in sc.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    sp.show_region_ui = True
    yield 1.0
    ok = yield from naar_tabblad()
    M["tabblad"] = ok
    log(f"KORT tabblad Click Cuts {ok}")
    muis_weg()
    per_nr = {int(o["sj_stuk"]): o for o in st}

    # ---- hook: hoop losse grijze stukken op tafel ----
    oud = {o.name: (o.matrix_basis.copy(), tuple(o.delta_location)) for o in st}
    kleur = []
    for o in st:
        for m in o.data.materials:
            if m is not None:
                kleur.append((m, tuple(m.diffuse_color)))
                m.diffuse_color = (0.62, 0.62, 0.64, 1)
    for o in pen:
        o.hide_set(True)
    rnd = random.Random(7)
    maten = [max(Vector(o.dimensions)) for o in st]
    stap = max(maten) * 1.05
    volg = list(st)
    rnd.shuffle(volg)
    for i, o in enumerate(volg):
        rij, kol = divmod(i, 4)
        doel = Vector(((kol - 1.5) * stap + rnd.uniform(-0.12, 0.12) * stap,
                       (rij - 1.0) * stap + rnd.uniform(-0.12, 0.12) * stap, 0.0))
        o.delta_location = (0.0, 0.0, 0.0)
        cs = [Vector(c) for c in o.bound_box]
        mid = sum(cs, Vector()) / 8
        laag = min(c.z for c in cs)
        ras = rnd.choice([(0, 0), (90, 0), (0, 90), (180, 0)])
        rot = (Matrix.Rotation(math.radians(rnd.uniform(0, 360)), 4, "Z")
               @ Matrix.Rotation(math.radians(ras[0]), 4, "X") @ Matrix.Rotation(math.radians(ras[1]), 4, "Y"))
        o.matrix_basis = Matrix.Translation(doel) @ rot @ Matrix.Translation(-mid)
        bpy.context.view_layer.update()
        laag = min((o.matrix_world @ Vector(c)).z for c in o.bound_box)
        o.matrix_basis = Matrix.Translation(Vector((0, 0, -laag))) @ o.matrix_basis
    bpy.context.view_layer.update()
    hmn, hmx = doos(st)
    hmid = tuple((hmn + hmx) / 2)
    hgr = max(hmx - hmn)
    deel("hoop")
    yield from stuk(100, lambda t: cam(20 + 22 * t, 55.0, hgr * 1.05 - hgr * 0.15 * t, hmid))
    for o in st:
        mb, dl = oud[o.name]
        o.matrix_basis = mb
        o.delta_location = dl
    for m, kl in kleur:
        m.diffuse_color = kl
    for o in pen:
        o.hide_set(False)
    bpy.context.view_layer.update()

    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    mn, mx = doos(st)
    mid = tuple((mn + mx) / 2)
    gr = max(mx - mn)

    # ---- klik Export parts ----
    deel("export")
    vak = ui_vak()
    M["ui_vak"] = vak
    cam(30, 70.0, gr * 1.9, mid)
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
    M["bestanden"] = sorted(os.path.basename(b) for b in besten)
    log(f"KORT export {len(besten)} bestanden {M['bestanden'][:3]}")
    yield from houd(40)
    muis_weg()

    # ---- More settings, scrollen naar Engrave numbers / Depth ----
    deel("paneel")
    ep = knop("Export parts", vak)
    onder = (vak[0], ep[1] + 20, vak[2], vak[3] - (ep[1] + 20 - vak[1])) if ep else vak
    ms = knop("More settings", onder)
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
    gv = None
    for i in range(30):
        gv = knop("Engrave numbers", vak)
        if gv and gv[1] < vak[1] + vak[3] * 0.55:
            break
        xdo("click", "5")
        yield 0.15
        neem(2)
    M["scroll_stappen"] = i
    yield from houd(14)
    yield 0.8
    gv = knop("Engrave numbers", vak) or gv
    dp = knop("Depth", vak)
    M["engrave_ocr"] = gv
    M["depth_ocr"] = dp
    y = gv[1] + 30 if gv else 960
    M["paneel_plek"] = [1830, int(y)]
    if dp:
        yield from muis_naar(dp[0] + 120, dp[1], 18)
    yield from houd(110)
    muis_weg()

    # ---- close-ups van de echte nummers (andere stukken even verborgen, alleen in de weergave) ----
    sp.overlay.show_overlays = False
    # run 20 les: een verdiept nummer recht van voren in Solid is onzichtbaar (geen schaduw): Cavity aan (echte
    # Blender-weergave) en de camera schuiner, zodat de wanden van de letters donker worden
    sp.shading.show_cavity = True
    sp.shading.cavity_type = "BOTH"
    sp.shading.cavity_valley_factor = 2.0
    sp.shading.cavity_ridge_factor = 1.0
    sp.shading.curvature_valley_factor = 2.0
    sp.shading.curvature_ridge_factor = 1.0
    alle = [(nr, lb) for nr, v in labels.items() for lb in v]
    if not alle:
        log("KORT FOUT geen labels")
        einde()
        return
    # hoofdlabel: grootste tekst, bij gelijk een vlak met minstens 2 gaten, dan het hoogste nummer
    alle.sort(key=lambda x: (x[1]["h"], len(gaten_bij(per_nr[x[0]], x[1])) >= 2, x[0]), reverse=True)
    nr, lb = alle[0]
    p_ob = per_nr[nr]
    buur = int(lb["tekst"].split("-")[1])
    q_ob = per_nr.get(buur)
    tegen = f"{buur}-{nr}"
    lb_q = next((x for x in labels.get(buur, []) if x["tekst"] == tegen), None)
    M["label_hoofd"] = {"stuk": nr, "tekst": lb["tekst"], "h": lb["h"], "as": lb["as"]}
    M["label_buur"] = {"stuk": buur, "tekst": lb_q["tekst"] if lb_q else None}
    M["paar_kop"] = f"{lb['tekst']} meets {tegen}" if lb_q else "Its own number, then the neighbor"
    breed = lb.get("breed") or lb["h"] * 2.2
    log(f"KORT hoofdlabel {lb['tekst']} op stuk {nr} h {lb['h']} buur {M['label_buur']}")

    alleen([p_ob])
    deel("vlak")
    yield from stuk(130, lambda t: kijk_op(lb, p_ob, breed * (9.0 - 5.0 * t), kanteling=38 - 16 * t, zij=-12 + 6 * t))

    deel("buren")
    yield from stuk(70, lambda t: kijk_op(lb, p_ob, breed * (3.8 - 0.5 * t), kanteling=22))
    if q_ob is not None and lb_q is not None:
        alleen([q_ob])
        bq = lb_q.get("breed") or lb_q["h"] * 2.2
        yield from stuk(70, lambda t: kijk_op(lb_q, q_ob, bq * (3.8 - 0.5 * t), kanteling=22))
    else:
        yield from houd(70)

    # buitenkant van hetzelfde stuk: geen tekst
    alleen([p_ob])
    pmn, pmx = doos([p_ob])
    pmid = (pmn + pmx) / 2
    pgr = max(pmx - pmn)
    smid = Vector(sc.get("sj_midden_mm", (0.0, 0.0, HOOGTE / 2)))
    weg = Vector(p_ob.get("sj_midden_mm", tuple(pmid))) - smid
    rechts, op, n = frame(lb["as"], lb["teken"], lb.get("richting"))
    if weg.length < 1.0:
        weg = -n
    weg = weg.normalized() - n * 0.6
    weg.z += 0.35
    M["buiten_richting"] = [round(v, 2) for v in weg.normalized()]
    deel("buiten")
    yield from stuk(130, lambda t: kijk_richting(weg, pgr * (2.3 - 0.3 * t), tuple(pmid), extra=-25 + 50 * t))

    # vlak met gaten: het nummer staat ertussen
    met = [(n_, l_) for n_, l_ in alle if len(gaten_bij(per_nr[n_], l_)) >= 2 and l_['h'] >= 5.0]
    met = [x for x in met if x[1]['tekst'] not in (lb['tekst'], tegen)] or met
    gn, gl = met[0] if met else (nr, lb)
    g_ob = per_nr[gn]
    gg = gaten_bij(g_ob, gl)
    lp = Vector(gl["p"])
    ver = max([(Vector(g["p"]) - lp).length + g["r_gat"] for g in gg] or [gl["h"] * 3])
    ver = min(ver, 90.0)
    M["label_gaten"] = {"stuk": gn, "tekst": gl["tekst"], "gaten": len(gg), "verste_mm": round(ver, 1)}
    log(f"KORT gaten-label {M['label_gaten']}")
    alleen([g_ob])
    deel("gaten")
    gb = gl.get("breed") or gl["h"] * 2.2
    afst = max(gb * 5.0, ver * 3.6)
    yield from stuk(130, lambda t: kijk_op(gl, g_ob, afst * (1.25 - 0.25 * t), kanteling=30 - 12 * t))

    # kleinste nummer
    kl = min(alle, key=lambda x: (x[1]["h"], x[0]))
    kn, kll = kl
    k_ob = per_nr[kn]
    M["label_klein"] = {"stuk": kn, "tekst": kll["tekst"], "h": kll["h"]}
    log(f"KORT klein-label {M['label_klein']}")
    alleen([k_ob])
    deel("klein")
    kb = kll.get("breed") or kll["h"] * 2.2
    yield from stuk(130, lambda t: kijk_op(kll, k_ob, kb * (7.0 - 3.0 * t), kanteling=36 - 14 * t, zij=8 - 6 * t))

    # ---- Exploded view met de echte objectnamen, van onder naar boven ----
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    mn, mx = doos(st)
    mid = tuple((mn + mx) / 2)
    gr = max(mx - mn)
    # run 20 les: alle oorsprongen lagen op 0,0,0, dus alle namen op één kluitje: oorsprong naar het midden van elk stuk
    # (na de close-ups, want sj_labels staan in mesh-coördinaten; de plek in de wereld blijft gelijk)
    alleen(st + pen)
    for o in st:
        o.select_set(True)
    bpy.context.view_layer.objects.active = st[0]
    try:
        with bpy.context.temp_override(selected_editable_objects=st, selected_objects=st, active_object=st[0],
                                       object=st[0]):
            bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
        M["oorsprong_midden"] = True
    except Exception as e:  # noqa: BLE001
        log(f"KORT oorsprong niet gezet: {e}")
        M["oorsprong_midden"] = False
    for o in st:
        o.select_set(False)
    bpy.context.view_layer.objects.active = None
    bpy.context.view_layer.update()
    mn, mx = doos(st)
    mid = tuple((mn + mx) / 2)
    gr = max(mx - mn)
    for o in st:
        o.show_name = True
    sp.overlay.show_overlays = True
    sp.shading.show_cavity = False
    M["namen"] = [o.name for o in st]
    M["z_volgorde"] = [int(o["sj_stuk"]) for o in sorted(st, key=lambda o: o.get("sj_midden_mm", [0, 0, 0])[2])]
    deel("lagen")
    yield from stuk(150, lambda t: cam(-25 + 35 * t, 78.0, gr * 1.55 - gr * 0.12 * t, mid))
    for o in st:
        o.show_name = False

    # ---- in elkaar, kleuren zichtbaar ----
    alleen(st + pen)
    sp.overlay.show_overlays = True
    inst.uit_elkaar = False
    bpy.context.view_layer.update()
    mn2, mx2 = doos(st)
    mid2 = tuple((mn2 + mx2) / 2)
    gr2 = max(mx2 - mn2)
    muis_weg()
    deel("samen")
    yield from stuk(140, lambda t: cam(-30 + 60 * t, 70.0, gr2 * 1.6, mid2))
    yield from houd(10)

    deel("eind")
    ok = (M["stukken"] == 12 and M["engrave"] and lb_q is not None and len(M["bestanden"]) >= 12
          and M["label_hoogtes"] and max(M["label_hoogtes"]) <= 8.0)
    log(f"KORT {'OK' if ok else 'FOUT'} alles")
    einde()


start(verloop)
