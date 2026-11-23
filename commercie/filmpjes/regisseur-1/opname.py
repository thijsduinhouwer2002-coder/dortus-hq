"""Opname Regisseur reeks 1: de Fit test strip van Click Joints Pro 1.2.0 (23 nov 2026, Regisseur).
Opdracht Thijs 23 nov: mooiere filmpjes met een voice-over die synchroon loopt. Onderwerp nieuw in de laatste 14 dagen:
de Fit test strip (nieuw in 1.2.0, platformen/blender/pro-1.2.0.md).

Draait de opname van reeks 4 (../youtube-shorts-4/opname.py: echte Blender 5.3.0, echte muis, OCR) met drie wijzigingen:
1. Figuur: het aangeklede studio-figuur (../studio/figuur_laden.py, MakeHuman CC0, kleurstelling a) in plaats van de grijze pop.
2. Nieuw deel na de export: "fittest" (echte klik op "Fit test: ball", camera naar de strip) en "fit_scharnier"
   (echte klik op "Fit test: hinge"). Plekken van de knoppen en van "Clearance" komen in film.json (metingen).
3. Renders in de studio (../studio/studio.py): render-1 figuur in pose met beide strips erachter, render-2 de strips
   dichtbij, render-3 alleen het figuur. Losse meshes die niet bij figuur of strip horen gaan voor de render uit beeld.
    CJ_MENS_OBJ=<base.obj> blender --gpu-backend opengl start.blend --python opname.py -- <map> <betaalde zip>
De workflow eist de regels "KORT OK <deel>", ook "KORT OK fittest"."""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.abspath(os.path.join(HIER, "..", "youtube-shorts-4", "opname.py"))
STUDIO = os.path.abspath(os.path.join(HIER, "..", "studio"))
src = open(BRON, encoding="utf-8").read()

FIGUUR = r'''
import sys as _sys
_sys.path.insert(0, STUDIO_MAP)
import figuur_laden as FL  # noqa: E402
import studio as S  # noqa: E402


def figuur():
    arm, ob, punten = FL.laad_mens_kleding(os.environ["CJ_MENS_OBJ"], 220.0)
    arm.data.display_type = "STICK"
    arm.show_in_front = True
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    exportmap = os.path.join(scherm_basis.uitmap, "export")
    os.makedirs(exportmap, exist_ok=True)
    inst.exportmap = exportmap
    log(f"KORT studio-figuur {ob.name} punten {len(ob.data.vertices)}")
    return ob, arm, punten


def strip_delen(soort=None):
    uit = []
    for o in bpy.context.scene.objects:
        if o.type != "MESH":
            continue
        if not any(c.name.startswith("Fit test") for c in o.users_collection):
            continue
        uit.append(o)
    return uit


def strip_midden(obs):
    pts = [o.matrix_world @ Vector(c) for o in obs for c in o.bound_box]
    lo = Vector((min(q.x for q in pts), min(q.y for q in pts), min(q.z for q in pts)))
    hi = Vector((max(q.x for q in pts), max(q.y for q in pts), max(q.z for q in pts)))
    return (lo + hi) / 2, hi - lo


VERBORGEN = []


def deel_fittest(heel, D_HEEL):
    """Fit test: ball en Fit test: hinge met echte klikken; camera naar de strips."""
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = False
    geen_selectie()
    herteken()
    yield 0.6
    cl = ocr("Clearance")
    film["metingen"]["clearance_ocr"] = cl
    vlak("fittest")
    deel("fittest")
    ft = yield from zoek("Fit test ball")
    film["metingen"]["fit_ocr"] = ft
    voor = len(strip_delen())
    if ft:
        yield from muis_naar(ft[0], ft[1], 26)
        neem_m(8)
        klik()
        yield 1.0
    t0 = time.time()
    while len(strip_delen()) == voor and time.time() - t0 < 90:
        yield 0.5
    if len(strip_delen()) == voor:
        log("KORT vangnet fittest: Fit test: ball via script")
        bpy.ops.click_joints.testkaart(soort="KOGEL")
        yield 1.0
    kogel = strip_delen()
    film["metingen"]["fit_kogel_delen"] = len(kogel)
    # rustig beeld op de strip (run 1: bogen en graden van de figuur stonden over de strip heen): bogen uit, figuur
    # even uit beeld; voor het held-deel komt de figuur terug
    try:
        bpy.context.window_manager.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    for o in bpy.context.scene.objects:
        if o.type == "MESH" and o.get("cj_figuur") and o.visible_get():
            o.hide_set(True)
            VERBORGEN.append(o.name)
    herteken()
    getallen = sorted(o.name for o in kogel if o.name.startswith("Fit "))
    film["metingen"]["fit_namen"] = getallen[:20]
    neem_m(10)
    w = rect("WINDOW")
    yield from muis_naar(w[0] + 80, w[1] + w[3] - 120, 14)   # muis uit het paneel (geen tooltip)
    mid, maat = strip_midden(kogel)
    film["metingen"]["fit_kogel_maat"] = [round(x, 1) for x in maat]
    d_strip = max(maat.x, 60.0) * 1.6
    yield from stuk(40, lambda t: cam(-25 + 25 * t, 84.0 - 24 * t, D_HEEL + (d_strip - D_HEEL) * t, mengen(heel, mid, t)))
    yield from stuk(70, lambda t: cam(0 + 18 * t, 60.0, d_strip, mid))
    # dichtbij de getallen bovenop
    boven = Vector((mid.x, mid.y, mid.z + maat.z * 0.45))
    yield from stuk(40, lambda t: cam(18, 60.0 - 15 * t, d_strip + (d_strip * 0.55 - d_strip) * t, mengen(mid, boven, t)))
    neem_m(30)
    log(f"KORT {'OK' if len(kogel) >= 10 else 'FOUT'} fittest {len(kogel)} delen")

    # scharnier: tweede knop, de strip komt achter de eerste
    yield from stuk(24, lambda t: cam(18 - 18 * t, 45.0 + 15 * t, d_strip * 0.55 + (d_strip * 0.45) * t, mengen(boven, mid, t)))
    deel("fit_scharnier")
    fh = yield from zoek("test hinge")
    film["metingen"]["fit_hinge_ocr"] = fh
    voor = len(strip_delen())
    if fh:
        yield from muis_naar(fh[0], fh[1], 24)
        neem_m(6)
        klik()
        yield 1.0
    t0 = time.time()
    while len(strip_delen()) == voor and time.time() - t0 < 90:
        yield 0.5
    if len(strip_delen()) == voor:
        log("KORT vangnet fittest: Fit test: hinge via script")
        bpy.ops.click_joints.testkaart(soort="SCHARNIER")
        yield 1.0
    alles = strip_delen()
    film["metingen"]["fit_alle_delen"] = len(alles)
    neem_m(8)
    yield from muis_naar(w[0] + 80, w[1] + w[3] - 120, 14)
    mid2, maat2 = strip_midden(alles)
    d2 = max(maat2.x, maat2.y, 60.0) * 1.5
    yield from stuk(50, lambda t: cam(18 * (1 - t) - 30 * t, 60.0 - 10 * t, d_strip + (d2 - d_strip) * t, mengen(mid, mid2, t)))
    yield from stuk(70, lambda t: cam(-30 + 40 * t, 50.0, d2, mid2))
    neem_m(20)
    log(f"KORT {'OK' if len(alles) > len(kogel) else 'FOUT'} fit_scharnier {len(alles)} delen")
    for n in VERBORGEN:
        o = bpy.data.objects.get(n)
        if o is not None:
            o.hide_set(False)
    herteken()
    yield from stuk(30, lambda t: cam(10 - 35 * t, 50.0 + 34 * t, d2 + (D_HEEL - d2) * t, mengen(mid2, heel, t)))


def renders_studio(p):
    sc = bpy.context.scene
    inst = sc.click_joints
    wm = bpy.context.window_manager
    try:
        wm.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    inst.uit_elkaar = False
    S.bouw(220.0)
    fig = [o for o in sc.objects if o.type == "MESH" and o.get("cj_figuur") and o.visible_get()]
    strip = strip_delen()
    houd = set(o.name for o in fig + strip)
    weg = []
    for o in sc.objects:
        if o.type == "MESH" and o.name not in houd and not o.name.startswith("studio_") and o.visible_get():
            o.hide_set(True)
            o.hide_render = True
            weg.append(o.name)
    log(f"KORT render uit beeld: {weg[:10]}")
    S.plastic(fig)
    # strips in eigen kleur: kogels oranje, scharnieren blauw (alleen voor de render)
    for o in strip:
        kl = "FF6B3D" if o.get("cj_soort", "") == "KOGEL" or "Ball" in o.name else "2F6BFF"
        m = bpy.data.materials.get("toy_strip_" + kl) or bpy.data.materials.new("toy_strip_" + kl)
        m.diffuse_color = S.srgb(kl)
        o.data.materials.clear()
        o.data.materials.append(m)
    S.plastic(strip, gewricht="contrast")
    cam_ob = S.camera()

    def pose(standen):
        for n, g in standen.items():
            _a, b = paar(n)
            if b is not None:
                buig(b, g)
                bpy.context.view_layer.update()
                yield 0.2
        geen_selectie()
        bpy.context.view_layer.update()
        yield 0.3

    yield from pose({"Left knee": 60.0, "Right knee": 10.0, "Left elbow": 100.0, "Right elbow": 45.0})
    S.richt(cam_ob, fig + strip, "staand", draai=-34, kantel=9, vul=0.72, midden_y=0.55)
    yield 0.3
    S.render(os.path.join(scherm_basis.uitmap, "render-1.png"))
    log("KORT render-1")
    for o in fig:
        o.hide_set(True)
    S.richt(cam_ob, strip, "staand", draai=-18, kantel=48, vul=0.95, midden_y=0.55)
    yield 0.3
    S.render(os.path.join(scherm_basis.uitmap, "render-2.png"))
    for o in fig:
        o.hide_set(False)
    log("KORT render-2")
    for o in strip:
        o.hide_set(True)
        o.hide_render = True
    yield from pose({"Left knee": 95.0, "Right knee": 20.0, "Left elbow": 120.0, "Right elbow": 70.0})
    S.richt(cam_ob, fig, "staand", draai=-30, kantel=7, vul=0.74, midden_y=0.56)
    yield 0.3
    S.render(os.path.join(scherm_basis.uitmap, "render-3.png"))
    log("KORT render-3")


renders = renders_studio
'''

vervang = [
    ("gang = verloop()", FIGUUR.replace("STUDIO_MAP", repr(STUDIO)) + "\ngang = verloop()"),
    # na de export, voor het held-deel: de Fit test strip
    ("    # held: dicht, figuur in pose", "    yield from deel_fittest(heel, D_HEEL)\n\n    # held: dicht, figuur in pose"),
]
for oud, nieuw in vervang:
    assert src.count(oud) == 1, f"niet gevonden of dubbel: {oud}"
    src = src.replace(oud, nieuw)
g = {"__name__": "__main__", "__file__": BRON}
exec(compile(src, BRON, "exec"), g)   # noqa: S102 (eigen code uit de repo)
