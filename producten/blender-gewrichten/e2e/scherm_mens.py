"""Plaatje 19 (Pro 1.1, eindbeeld voor Daan): echte mensfiguur na "Figure from rig".

Figuur en rig uit proef_mens.py (MakeHuman base.obj, CC0 1.0, Mixamo-namen op de eigen gewrichtspunten, 220 mm,
linkerknie 120 en linkerelleboog 140 in Limit Rotation, rechts niets). Na de knop: scharnierbogen met getal op knieën
en ellebogen, kogelwaaiers op heupen en nek. Daan 16 nov: "maak het eindbeeld op een echte figuur, niet op de
cilinders". Alleen echte uitkomst van de add-on, niets nagetekend.
Regel "MENS BEELD OK" als minstens 4 bogen (4.2: 2) groen met getal getekend zijn, kogels groen met ±N en 40 px vrij,
de lijst `from rig` en `mirrored` bevat en de uitsnede van het paneel gelukt is.
    CJ_MENS_OBJ=<base.obj> blender --python e2e/scherm_mens.py -- <map> <betaalde zip>
"""
import importlib
import math
import os
import subprocess
import sys

import bpy
from mathutils import Euler, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from scherm_basis import klap_hoofdpaneel, log, open_paneel, schiet, toestand, uitmap, wiel_naar_tabblad, zijbalk, zip_pad  # noqa: E402

os.environ["CJ_HOOGTE"] = os.environ.get("CJ_TOETS_HOOGTE", "220")
_src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
M = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
exec(compile(_src, "proef_mens.py", "exec"), M)
A = M["A"]

staat = {}
# Daan 17 nov ±05:30 moet 2: lichtgrijs mat als geprinte PLA, #B9BEC4 (sRGB), hier lineair voor diffuse_color.
PLA = tuple(((c / 255.0 + 0.055) / 1.055) ** 2.4 for c in (0xD2, 0xD6, 0xDB)) + (1.0,)
# Iets lichter dan #B9BEC4 gekozen: het studiolicht van de 3D-weergave maakt het een stap donkerder (run 23 gemeten:
# #B9BEC4 kwam als ±#8A8D90 in beeld). Op het scherm leest het nu als lichtgrijs.
# Daan 17 nov ±05:30 moet 1: een gebogen elleboog toont het blok van de knokkel en open snijvlakken (een klikscharnier
# op een dunne arm van 9 mm is een echt mechaniekje, geen huid die om het gewricht sluit). Zijn uitweg: buig in dit
# beeld alleen de knie, de rest recht. Dan vertellen beeld en paneel hetzelfde (moet 5): het paneel staat op de knie.
BUIG = {"Right knee": 60.0}
if os.environ.get("CJ_BUIG"):  # bijvoorbeeld "Right knee:60" (volgorde telt: het laatste lid staat in het paneel)
    BUIG = {d.split(":")[0]: float(d.split(":")[1]) for d in os.environ["CJ_BUIG"].split(",")}


def etalagepop(ob):
    """Daan 17 nov moet 3: de MakeHuman-figuur als houten tekenpop, niet als kaal mens. Alleen de invoer verandert
    (vorm, kleur, glad), daarna draait de knop zoals altijd; de toets toetsen_mens rekent op de figuur zonder dit.
    Borst plat: punten aan de voorkant tussen z 146 en 172 (220 mm hoog, gemeten run 22) schuiven naar het vlak
    y = -2,5 mm, met een zachte overgang in hoogte en breedte, alleen naar achteren (nooit door de rug)."""
    for v in ob.data.vertices:
        c = v.co
        if c.y >= -2.5 or abs(c.x) < 4.0 or abs(c.x) > 36.0:
            continue
        wz = max(0.0, 1.0 - abs(c.z - 159.0) / 13.0)
        wx = min(1.0, (abs(c.x) - 4.0) / 6.0) * min(1.0, (36.0 - abs(c.x)) / 6.0)
        w = math.sin(wz * math.pi / 2.0) ** 2 * wx
        c.y = c.y + (-2.5 - c.y) * w
    glad_romp(ob)
    for f in ob.data.polygons:
        f.use_smooth = True
    mat = bpy.data.materials.new("pla_grijs")
    mat.diffuse_color = PLA
    mat.roughness = 1.0
    mat.metallic = 0.0
    ob.data.materials.clear()
    ob.data.materials.append(mat)
    ob.data.update()


def glad_romp(ob):
    """Daan 18 nov moet 2 (plaatje 19): geen geslachtskenmerken, glad als een tekenpop. Na het platdrukken van de
    borst waren borsten, navel en billen nog te zien. Hier de romp (heup tot borst, zonder armen en benen) glad
    strijken met Laplace (volume blijft), met een zachte rand naar hals en dijen. Alleen invoer van dit beeld."""
    import bmesh
    lo, hi = float(os.environ.get("CJ_GLAD_LO", "92")), float(os.environ.get("CJ_GLAD_HI", "170"))
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    romp = [v for v in bm.verts if lo < v.co.z < hi and abs(v.co.x) < float(os.environ.get("CJ_GLAD_X", "30"))]
    for _ in range(int(os.environ.get("CJ_GLAD_N", "25"))):
        bmesh.ops.smooth_vert(bm, verts=romp, factor=0.8, use_axis_x=True, use_axis_y=True, use_axis_z=True)
    bm.to_mesh(ob.data)
    bm.free()
    staat["glad_romp"] = len(romp)
    log(f"MENS romp glad: {len(romp)} punten")


def heup_zonder_band(afstand=22.0):
    """Daan 17 nov ±05:30 moet 3, zijn uitweg: de heupband heeft op een figuur een zaagtand (de snede van de kogel
    maakt lange vlakken, en de band kleurt per vlak). In dit beeld de heupen als kogel zonder band; de ±8° en ±15°
    blijven. Alleen kleur in dit schermbeeld (vlakken binnen `afstand` mm van een heupsnede terug naar het materiaal
    van het dichtstbijzijnde vlak buiten de band); de add-on zelf kleurt de band zoals altijd (CJ_HEUPBAND=1)."""
    import numpy as np
    from mathutils.kdtree import KDTree
    obs = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    heup = [Vector(o["cj_snijpunt"]) for o in obs if "hip" in str(o.get("cj_naam", "")).lower() and "cj_snijpunt" in o]
    teruggezet = 0
    for o in obs:
        vak = o.get("cj_ring_vak")
        me = o.data
        if vak is None or not heup or not len(me.polygons):
            continue
        n = len(me.polygons)
        idx = np.empty(n, dtype=np.int32)
        me.polygons.foreach_get("material_index", idx)
        c = np.empty(n * 3)
        me.polygons.foreach_get("center", c)
        c = c.reshape(n, 3)
        mw = np.array(o.matrix_world)
        cw = c @ mw[:3, :3].T + mw[:3, 3]
        dicht = np.zeros(n, dtype=bool)
        for h in heup:
            dicht |= np.linalg.norm(cw - np.array(h), axis=1) <= afstand
        terug = (idx == int(vak)) & dicht
        buiten = np.nonzero(idx != int(vak))[0]
        if not terug.any() or not len(buiten):
            continue
        boom = KDTree(len(buiten))
        for i, j in enumerate(buiten):
            boom.insert(Vector(c[j]), i)
        boom.balance()
        for j in np.nonzero(terug)[0]:
            idx[j] = idx[buiten[boom.find(Vector(c[j]))[1]]]
        me.polygons.foreach_set("material_index", idx)
        me.update()
        teruggezet += int(terug.sum())
    staat["heupband_weg"] = teruggezet
    log(f"MENS heupband weg in dit beeld: {len(heup)} heupen, {teruggezet} vlakken")


def buig():
    """Moet 2: buig met de eigen Bend-schuif van het paneel (zelfde weg als een koper), eindig op de elleboog."""
    wm = bpy.context.window_manager
    delen = {o.get("cj_naam"): o for o in bpy.context.scene.objects
             if o.get("cj_deel") == "B" and o.get("cj_figuur") and o.get("cj_soort") == "SCHARNIER"}
    gebogen = {}
    for naam in BUIG:  # het laatste lid blijft actief en staat in het paneel
        b = delen.get(naam)
        if b is None:
            continue
        A["actief"](b)
        wm.cj_scharnier_pose = BUIG[naam]
        gebogen[naam] = round(float(b.get("cj_pose_graden", 0.0)), 1)
    staat["gebogen"] = gebogen
    if os.environ.get("CJ_HEUPBAND", "0") != "1":
        heup_zonder_band()
    log(f"MENS gebogen {gebogen} delen={sorted(k for k in delen if k)}")


def bouw():
    A["leeg"]()  # ook de eenheden op mm: zonder dat is de figuur 220 meter en rekent de passing minuten
    ob, punten = M["laad_mens"](os.environ["CJ_MENS_OBJ"])
    st = A["mesh_staat"](ob)
    log(f"MENS geladen: open randen {st['open_randen']}")
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    if os.environ.get("CJ_POP", "1") == "1":
        etalagepop(ob)
    naam = ob.name
    arm = M["maak_rig"](punten)
    arm.data.display_type = "STICK"
    ob.modifiers.new("Armature", "ARMATURE").object = arm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    if os.environ.get("CJ_ALLEEN"):  # zoals proef_mens: alleen gewrichten met deze stukjes naam (uitzoeken)
        _rigm = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
        _g = getattr(_rigm, "_cj_echt", _rigm.gewrichten)
        _rigm._cj_echt, _w = _g, os.environ["CJ_ALLEEN"].split(",")
        _rigm.gewrichten = lambda a, meer=False: [x for x in _g(a, meer) if any(w in x[2].lower() for w in _w)]
    log("MENS knop start")
    staat["knop"] = bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    staat["lijst"] = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    staat["regels"] = [fig.regel(r) for r in staat["lijst"]]
    staat["samenvatting"] = fig.samenvatting(staat["lijst"])
    buig()
    log(f"MENS knop {staat['knop']} regels={staat['regels']} samenvatting={staat['samenvatting']}")


def rustig():
    """Moet 1: alleen de 3D-weergave met het paneel (tijdlijn en eigenschappen weg), rasters, assen, 3D-cursor en
    de tekst linksboven uit. Ctrl+Spatie (screen_full_area) houdt kop, gereedschapsbalk en zijbalk."""
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        bpy.ops.screen.screen_full_area()
    venster, gebied, _ = zijbalk()
    ov = gebied.spaces.active.overlay
    for k in ("show_floor", "show_axis_x", "show_axis_y", "show_axis_z", "show_cursor", "show_text", "show_outline_selected",
              "show_object_origins"):
        setattr(ov, k, False)
    # Daan 17 nov ±05:30 moet 4: navigatiegizmo en de knoppen rechtsboven (zoom, hand, camera, raster) uit.
    gebied.spaces.active.show_gizmo_navigate = False


def kijk():
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    rv = ruimte.region_3d
    rv.view_perspective = "ORTHO"
    # Schuin van voren: de knieas ligt langs X (waaier zichtbaar van opzij), de elleboogas niet (zichtbaar van voren).
    rv.view_rotation = Euler((math.radians(float(os.environ.get("CJ_KANTEL", "82"))), 0.0,
                              math.radians(float(os.environ.get("CJ_DRAAI", "-35")))), "XYZ").to_quaternion()
    rv.view_location = (float(os.environ.get("CJ_MIDX", "-12")), 0.0, float(os.environ.get("CJ_MIDZ", "110")))
    rv.view_distance = float(os.environ.get("CJ_AFSTAND", "335"))


def uitsnede():
    venster, _gebied, regio = zijbalk()
    bron = os.path.join(uitmap, "19-mens-x.png")
    doel = os.path.join(uitmap, "19-mens-paneel.png")
    if not (regio and os.path.exists(bron)):
        return False
    x = venster.x + regio.x
    y = venster.y + venster.height - (regio.y + regio.height)
    r = subprocess.run(["convert", bron, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage", doel],
                       capture_output=True, text=True)
    return r.returncode == 0 and os.path.exists(doel)


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        bouw()
        rustig()
        open_paneel()
        kijk()
        return 1.0
    if n < 20 and not wiel_naar_tabblad():
        return 0.5
    if "geschoten" not in staat:
        staat["geschoten"] = True
        venster, gebied, regio = zijbalk()
        if regio:  # paneel Click Joints dicht, zodat Figure joints met teller en lijst in beeld staat (Daan moet 2)
            log(f"MENS hoofdpaneel ingeklapt: {klap_hoofdpaneel()}")
        gebied.tag_redraw()
        return 1.5
    schiet("19-mens.png")
    ok_uit = uitsnede()
    boog = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_boog")
    bogen = [b for b in boog.laatst.get("bogen", []) if b.get("figuur")]
    koppen = [b for b in boog.laatst.get("bogen", []) if b.get("kop")]
    groen = all(b.get("kleur") != boog.WIT for b in bogen)
    getal = all(b.get("getal_getekend") for b in bogen)
    rig_regel = any("from rig" in r for r in staat.get("regels", []))
    act = bpy.context.view_layer.objects.active
    zichtbaar = act is not None and act.visible_get() and bool(act.get("cj_deel"))
    oud = bpy.app.version < (4, 5, 0)  # bekende losse boolean-fout met alleen Exact (toetsen_rig_armen.py)
    # Run 20: zelfde eis als toetsen_rig_armen.py sinds run 19: in 4.2 minstens 4 van 8 gewrichten (de knieën
    # vallen daar eerlijk af met reden), dus minstens 2 scharnierbogen; in 5.x alle 8.
    genoeg = len(bogen) >= (2 if oud else 4)
    acht = any(r.endswith("mirror") for r in staat.get("regels", []))
    # Daan 16 nov ±13:50: kogels van een figuur klein en groen met één getal ±N° (moet 1: nooit binnen 40 px van
    # een ander getal), en stap 3 zegt niet "No joint yet" naast de gewrichten (moet 2).
    ft = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur_teken")
    from mathutils import Vector
    kogels = list(ft.laatst.get("getekend", {}).values())
    schaal = bpy.context.preferences.system.ui_scale
    vakken = [k["vak"] for k in kogels if k.get("getal_getekend")]
    for b in bogen:
        if b.get("label_px"):
            vakken_s = ft.vak(Vector(b["label_px"]), b["getal"], int(boog.FIGUUR_PX * schaal))
            vakken.append(vakken_s)
    gaten = [ft.gat(k["vak"], o) for k in kogels for o in vakken if tuple(o) != tuple(k["vak"])]
    min_gat = round(min(gaten), 1) if gaten else None
    kogel_ok = (len(kogels) >= (1 if oud else 2) and all(k["getal"].startswith("\u00b1") for k in kogels)
                and all(k["kleur"] != boog.WIT for k in kogels) and all(k.get("getal_getekend") for k in kogels)
                and (min_gat is None or min_gat >= 40.0 * schaal - 0.5))
    stap3 = bool(act is not None and act.get("cj_passing"))
    log(f"MENS KOGELS {'OK' if kogel_ok else 'FOUT'} kogels={[(k['naam'], k['getal'], k['label_px']) for k in kogels]} "
        f"kleinste_gat_px={min_gat} stap3_passing={act.get('cj_passing') if act else None} fout={ft.laatst.get('fout')}")
    ok = genoeg and acht and groen and getal and len(koppen) <= 1 and rig_regel and zichtbaar and ok_uit and kogel_ok and stap3
    log(f"MENS BEELD {'OK' if ok else 'FOUT'} samenvatting={staat.get('samenvatting')} bogen={[(b['naam'], b['getal'], b['kijkhoek']) for b in bogen]} "
        f"koppen={len(koppen)} actief={act.name if act else None} zichtbaar={zichtbaar} groen={groen} getal={getal} from_rig={rig_regel} uitsnede={ok_uit} "
        f"fout={boog.laatst.get('fout')}")
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
