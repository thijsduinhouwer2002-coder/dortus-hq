"""Gradenboog en pose-schuif van het scharnier (eis 8, ontwerp betaald v1.1, "Wat je ziet").

Zoals de gradenboog van de kogel (waaier.py en gradenboog.py van het gratis deel, die niet veranderen), maar
met één boog om de scharnieras H: van rechtdoor (0) tot de grens, de grens is het getal van het paneel
("Bends 0° to N°", gemeten, nooit meer dan de stand). Voorbij de grens een rood vlak, een rode pose-lijn en
"+N° past limit". Bovenaan het beeld staat dezelfde regel "Bends 0° to N°" als in het paneel.

De pose-schuif in het paneel draait deel B alleen in de weergave (scharnier_beweeg.pose) en kleurt voorbij de
stop de vlakken van A die B raken rood, net als de pose van de kogel. In achtergrondmodus geen handler."""
import math

import bpy
from mathutils import Vector

from . import scharnier_beweeg as beweeg

WIT = (1.0, 1.0, 1.0)
ROOD = (1.0, 0x4D / 255.0, 0x4D / 255.0)  # zelfde rood als de kogelboog
STRAAL = 3.5        # keer de knokkelstraal: de kleinste straal
DIKTE_X = 2.1       # boogstraal minstens zoveel keer de halve dikte van het lid bij de knie (Daan, Pro punt 6: de boog
                    # buiten het deel, niet door de knokkel; de poster van ronde 1 had 15 mm op een been van 7,2 mm)
_dikte = {}         # (naam A, naam B, aantal hoekpunten) -> halve dikte; in de tekenbeurt mag niets op het object
STREEP = 5          # graden tussen twee streepjes
POSE_LANG = 1.15
ROOD_PX = 24        # "+N° past limit": groot genoeg voor een winkelplaatje (16 was te klein)
_handler = [None]
laatst = {}  # wat de laatste tekenbeurt tekende, voor het bewijs in de schermtest


def grens(a):
    """Getal op de boog: zelfde als het paneel (beweeg.tekst), nooit meer dan de stand."""
    return min(int(round(float(a["cj_bereik_graden"]))), int(a["cj_stand"]))


def tekst(a):
    return beweeg.tekst(float(a["cj_bereik_graden"]), int(a["cj_stand"]))


def paar(scene, ob):
    """(A, B) van het scharnier waar ob bij hoort, of (None, None)."""
    if ob is None or ob.get("cj_soort") != "SCHARNIER":
        return None, None
    a = b = None
    for o in scene.objects:
        if o.get("cj_soort") == "SCHARNIER" and o.get("cj_bron") == ob.get("cj_bron") \
                and list(o.get("cj_snijpunt", [])) == list(ob.get("cj_snijpunt", [])):
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def dikte(a, b):
    """Halve dikte van het lid bij de knie in het buigvlak: de verste afstand langs de buigkant (beide kanten) tot het
    draaipunt van de hoekpunten van A en B binnen 5 knokkelstralen van het draaipunt langs de lidas, rechte stand.
    (2 knokkelstralen was te krap: daar is het lid rond de knokkel weggesneden, run 42794577017 gaf 4,2 mm op een been
    van ±6 mm.)"""
    sleutel = (a.name, b.name, len(a.data.vertices), len(b.data.vertices))
    if sleutel in _dikte:
        return _dikte[sleutel]
    import numpy as np
    from ..uit_elkaar import echte_matrix
    c = np.array(a["cj_scharnier_punt"], dtype=np.float64)
    lid = np.array(Vector(a["cj_as"]).normalized())
    buig = np.array(Vector(a["cj_buigkant"]).normalized())
    k = float(a["cj_knokkel_r"])
    best = k
    for ob in (a, b):
        n = len(ob.data.vertices)
        co = np.empty(n * 3, dtype=np.float64)
        ob.data.vertices.foreach_get("co", co)
        mw = np.array(echte_matrix(ob), dtype=np.float64)
        rel = co.reshape(n, 3) @ mw[:3, :3].T + mw[:3, 3] - c
        dicht = np.abs(rel @ lid) <= 5.0 * k
        if dicht.any():
            best = max(best, float(np.abs(rel[dicht] @ buig).max()))
    _dikte[sleutel] = best
    return best


def straal(a, b):
    """Straal van de boog: buiten het lid (DIKTE_X keer de halve dikte), nooit kleiner dan STRAAL knokkelstralen."""
    return max(STRAAL * float(a["cj_knokkel_r"]), DIKTE_X * dikte(a, b))


def vorm(a, b, pose):
    """De boog in wereldcoördinaten. Beginrichting: de lidas naar de kant van B in rechte stand."""
    c = Vector(a["cj_scharnier_punt"])
    lid = Vector(a["cj_as"]).normalized()
    voor_as = lid.cross(Vector(a["cj_buigkant"])).normalized()
    # Middelpunt van B in rechte stand: de bounding box via de matrix zonder pose en Exploded view.
    from ..uit_elkaar import echte_matrix
    mb = echte_matrix(b)
    hoeken = [mb @ Vector(h) for h in b.bound_box]
    midden_b = sum(hoeken, Vector()) / 8.0
    d = lid if (midden_b - c).dot(lid) >= 0 else -lid
    zij = voor_as.cross(d)  # draaien om voor_as brengt d hierheen
    R = straal(a, b)

    def punt(g, r=R):
        t = math.radians(g)
        return c + r * (d * math.cos(t) + zij * math.sin(t))
    n = grens(a)
    voorbij = pose > n + 1e-6
    rood = []
    if voorbij:
        stappen = max(1, int(math.ceil(pose - n)))
        rood = [punt(n + (pose - n) * i / stappen) for i in range(stappen + 1)]
    return {
        "getal": n, "centrum": c, "normaal": voor_as, "boog": [punt(g) for g in range(n + 1)],
        "as_eind": punt(0), "grens_eind": punt(n), "label": punt(n, R * 1.25), "label_0": punt(0, R * 1.25),
        "streepjes": [(g, punt(g), punt(g, R * 1.1)) for g in range(0, n + 1, STREEP)],
        "pose_eind": punt(pose, R * POSE_LANG) if pose > 0 else None, "voorbij": voorbij, "rood_vlak": rood,
        "voorbij_tekst": f"+{max(1, int(round(pose - n)))}° past limit" if voorbij else None,
    }


def _omhulsel(punten):
    """Convexe omhullende in beeld (monotone keten), tegen de klok in."""
    p = sorted({(round(x.x, 2), round(x.y, 2)) for x in punten if x is not None})
    if len(p) < 3:
        return p

    def kruis(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    onder, boven = [], []
    for rij, uit in ((p, onder), (reversed(p), boven)):
        for x in rij:
            while len(uit) >= 2 and kruis(uit[-2], uit[-1], x) <= 0:
                uit.pop()
            uit.append(x)
    return onder[:-1] + boven[:-1]


def _binnen(hul, x, y):
    n = len(hul)
    return n >= 3 and all((hul[(i + 1) % n][0] - hul[i][0]) * (y - hul[i][1])
                          - (hul[(i + 1) % n][1] - hul[i][1]) * (x - hul[i][0]) >= 0 for i in range(n))


def _rood_plek(regio, rv3d, q, uit, delen, tekst_, px, schaal):
    """Plek van "+N° past limit". Zoals op de kogelboog (winkelplaatje 9) moet rood met donkere rand op de achtergrond
    staan: over een grijs deel is het slecht leesbaar. Kandidaten in ringen rond het eind van de pose-lijn, eerst
    dichtbij en in de richting van de lijn, dan verder en rondom; de eerste waarvan het tekstvak buiten de omhullende
    van A en B (hoekpunten van de bound box, in beeld) en binnen het beeld ligt wint. Alleen langs de pose-lijn zoeken
    (tot run 42668200920) vond bij een schuin scharnier niets vrij: de lijn wijst dan in deel B.
    Geeft (plek, vrij, (breed, hoog)); niets vrij: de oude plek (70 px verder langs de lijn)."""
    import blf
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d
    blf.size(0, px)
    breed, hoog = blf.dimensions(0, tekst_)
    hullen = [_omhulsel([naar2d(regio, rv3d, d.matrix_world @ Vector(h)) for h in d.bound_box]) for d in delen]
    rand = 8.0 * schaal
    hoeken = sorted(range(-180, 180, 15), key=abs)
    for t in [70.0 + 30.0 * i for i in range(40)]:
        for g in hoeken:
            r = math.radians(g)
            richting = Vector((uit.x * math.cos(r) - uit.y * math.sin(r), uit.x * math.sin(r) + uit.y * math.cos(r)))
            m = q["pose_eind"] + richting * (t * schaal)
            x0, x1, y0, y1 = m.x - breed / 2 - rand, m.x + breed / 2 + rand, m.y - hoog / 2 - rand, m.y + hoog / 2 + rand
            if x0 < 0 or y0 < 0 or x1 > regio.width or y1 > regio.height - 100.0 * schaal:
                continue
            proef = [(x, y) for x in (x0, m.x, x1) for y in (y0, m.y, y1)]
            if q["label"] is not None and (m - q["label"]).length < breed / 2 + 40.0 * schaal:
                continue
            if any(_binnen(h, x, y) for h in hullen for x, y in proef):
                continue
            if any(x0 <= hx <= x1 and y0 <= hy <= y1 for h in hullen for hx, hy in h):
                continue
            return m, True, (breed, hoog)
    return q["pose_eind"] + uit * (70.0 * schaal), False, (breed, hoog)


def _tot_vak(van, m, breed, hoog, rand):
    """Punt op de rand van het tekstvak (midden m) op de lijn van van naar m: daar stopt het verwijslijntje."""
    d = m - van
    if d.length == 0:
        return m
    sx = (breed / 2 + rand) / abs(d.x) if d.x else float("inf")
    sy = (hoog / 2 + rand) / abs(d.y) if d.y else float("inf")
    return m - d * min(1.0, sx, sy)


def _teken_een(regio, rv3d, a, b, schaal):
    import gpu
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d

    from .. import waaier  # alleen de tekenhulpjes lezen, het gratis deel verandert niet
    pose = float(b.get("cj_pose_graden", 0.0))
    v = vorm(a, b, pose)

    def p(x):
        return naar2d(regio, rv3d, x) if x is not None else None
    q = {k: p(v[k]) for k in ("centrum", "as_eind", "grens_eind", "label", "pose_eind")}
    boog = [p(x) for x in v["boog"]]
    vlak = gpu.shader.from_builtin("UNIFORM_COLOR")
    dik = gpu.shader.from_builtin("POLYLINE_UNIFORM_COLOR")
    waaier._waaiervlak(vlak, q["centrum"], boog, (*WIT, 0.15))
    waaier._lijn(dik, regio, [q["centrum"], q["as_eind"]], (*WIT, 0.55), 2.0 * schaal)
    waaier._lijn(dik, regio, [q["centrum"], q["grens_eind"]], (*WIT, 0.9), 3.0 * schaal)
    waaier._lijn(dik, regio, boog, (*WIT, 0.9), 3.0 * schaal)
    hoek = waaier.kijkhoek(rv3d, v)
    streep, getal, nul = [], False, False
    if hoek >= waaier.SCHUIN_MIN:
        streep = waaier.streep_lijnen([(g, p(s0), p(s1)) for g, s0, s1 in v["streepjes"]], schaal)
        for _, s0, s1 in streep:
            waaier._lijn(dik, regio, [s0, s1], (*WIT, 0.9), 2.0 * schaal)
        getal = waaier._tekst(0, q["label"], f"{v['getal']}°", WIT, int(20 * schaal))
        # Ook 0° aan het begin (Daan, Pro punt 6): dan lees je de boog als "van 0° tot 115°".
        nul = waaier._tekst(0, p(v["label_0"]), "0°", WIT, int(20 * schaal))
    rood_tekst, vrij = False, None
    if q["pose_eind"] is not None:
        if v["voorbij"]:
            waaier._waaiervlak(vlak, q["centrum"], [p(x) for x in v["rood_vlak"]], (*ROOD, 0.30))
        waaier._lijn(dik, regio, [q["centrum"], q["pose_eind"]], (*(ROOD if v["voorbij"] else WIT), 1.0),
                     4.0 * schaal)
        if v["voorbij"] and hoek >= waaier.SCHUIN_MIN:
            # Verder naar buiten dan het getal van de grens, anders liggen "115°" en "+3° past limit" over elkaar.
            uit = q["pose_eind"] - q["centrum"] if q["centrum"] is not None else Vector((0.0, 1.0))
            uit = uit.normalized() if uit.length > 0 else Vector((0.0, 1.0))
            groot = int(ROOD_PX * schaal)
            plek, vrij, (breed, hoog) = _rood_plek(regio, rv3d, q, uit, (a, b), v["voorbij_tekst"], groot, schaal)
            if vrij:  # dun rood lijntje van het eind van de pose-lijn naar de tekst op de vrije plek
                waaier._lijn(dik, regio, [q["pose_eind"], _tot_vak(q["pose_eind"], plek, breed, hoog, 6.0 * schaal)],
                             (*ROOD, 0.9), 2.0 * schaal)
            rood_tekst = waaier._tekst(0, plek, v["voorbij_tekst"], ROOD, groot)
    # De regel van het paneel ook in beeld (winkelschermen 11 en 12), bovenaan in het midden.
    kop = tekst(a)
    kop_getekend = waaier._tekst(0, Vector((regio.width / 2.0, regio.height - 60.0 * schaal)), kop, WIT,
                                 int(28 * schaal))
    return {"pose": round(pose, 3), "getal": f"{v['getal']}°", "getal_getekend": getal, "nul_getekend": nul,
            "straal": round((v["boog"][0] - v["centrum"]).length, 3),
            "streepjes": len(streep), "kijkhoek": round(hoek, 1), "voorbij": v["voorbij"],
            "voorbij_tekst": v["voorbij_tekst"] if rood_tekst else None,
            "kop": kop if kop_getekend else None, "rood_vrij": vrij}


def teken():
    import gpu
    context = bpy.context
    wm = context.window_manager
    if not getattr(wm, "cj_scharnier_boog", False):
        laatst.clear()
        laatst["bogen"] = []
        return
    regio, rv3d = context.region, context.region_data
    if regio is None or rv3d is None:
        return
    schaal = context.preferences.system.ui_scale
    gpu.state.blend_set("ALPHA")
    gpu.state.depth_test_set("NONE")
    getekend = []
    for b in [o for o in context.scene.objects
              if o.get("cj_soort") == "SCHARNIER" and o.get("cj_deel") == "B" and o.visible_get()]:
        a, _ = paar(context.scene, b)
        if a is None or "cj_bereik_graden" not in a or beweeg.geen_stop(float(a["cj_bereik_graden"])):
            continue
        getekend.append(_teken_een(regio, rv3d, a, b, schaal))
    gpu.state.blend_set("NONE")
    laatst.clear()
    laatst["bogen"] = getekend


def _veilig():
    try:
        teken()
    except Exception as fout:  # noqa: BLE001  tekenen mag Blender nooit laten vallen
        import traceback
        laatst["fout"] = traceback.format_exc()[-600:]
        print(f"Click Joints: hinge range not drawn ({fout})", flush=True)


def herteken(_wm=None, context=None):
    """Alle 3D-weergaven opnieuw tekenen (een eigenschap van de WindowManager doet dat zelf niet)."""
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                gebied.tag_redraw()


def _actief_paar():
    ctx = bpy.context
    ob = getattr(ctx, "active_object", None) or ctx.view_layer.objects.active
    return paar(ctx.scene, ob)


def _pose_lees(_wm):
    """De pose-schuif hoort bij het actieve scharnier: de stand staat op deel B (cj_pose_graden), dus elk scharnier
    houdt zijn eigen stand, ook na heropenen van het bestand (kan-punt controleur eis 8)."""
    try:
        _a, b = _actief_paar()
    except AttributeError:  # bpy.context zonder scene of view_layer (tijdens laden of registreren)
        return 0.0
    return float(b.get("cj_pose_graden", 0.0)) if b is not None else 0.0


def _pose_zet(_wm, waarde):
    from .. import kleur
    a, b = _actief_paar()
    if a is None or b is None:
        return
    beweeg.pose(a, b, float(waarde), kleur.materiaal("rood"))
    herteken()


def teken_paneel(self, context):
    """In het paneel bij een actief scharnierdeel: "Bends 0° to N°", de boog aan of uit en de pose-schuif."""
    ob = context.active_object
    a, b = paar(context.scene, ob)
    if a is None or b is None or "cj_bereik_graden" not in a:
        return
    wm = context.window_manager
    vak = self.layout.box()
    vak.label(text="Hinge", icon="CON_PIVOT")
    if beweeg.geen_stop(float(a["cj_bereik_graden"])):
        vak.label(text="No end stop found", icon="ERROR")
        return
    vak.label(text=tekst(a), icon="BLANK1")
    blok = vak.column(align=True)
    blok.prop(wm, "cj_scharnier_boog", icon="LIGHT_SPOT")
    blok.prop(wm, "cj_scharnier_pose", slider=True)


def register():
    bpy.types.WindowManager.cj_scharnier_boog = bpy.props.BoolProperty(
        name="Show bend range", default=True, description="Draw the measured bend range of the hinge", update=herteken)
    bpy.types.WindowManager.cj_scharnier_pose = bpy.props.FloatProperty(
        name="Bend", default=0.0, min=0.0, max=150.0,
        description="Bend part B in the view only, to check the range. Past the end stop, touching faces turn red",
        get=_pose_lees, set=_pose_zet)
    paneel = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    if paneel is not None:
        paneel.append(teken_paneel)
    if not bpy.app.background and _handler[0] is None:
        _handler[0] = bpy.types.SpaceView3D.draw_handler_add(_veilig, (), "WINDOW", "POST_PIXEL")


def unregister():
    if _handler[0] is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_handler[0], "WINDOW")
        _handler[0] = None
    paneel = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    if paneel is not None:
        paneel.remove(teken_paneel)
    for naam in ("cj_scharnier_pose", "cj_scharnier_boog"):
        if hasattr(bpy.types.WindowManager, naam):
            delattr(bpy.types.WindowManager, naam)
