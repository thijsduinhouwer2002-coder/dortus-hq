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
STRAAL = 3.5        # keer de knokkelstraal
STREEP = 5          # graden tussen twee streepjes
POSE_LANG = 1.15
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


def vorm(a, b, pose):
    """De boog in wereldcoördinaten. Beginrichting: de lidas naar de kant van B in rechte stand."""
    c = Vector(a["cj_scharnier_punt"])
    lid = Vector(a["cj_as"]).normalized()
    voor_as = lid.cross(Vector(a["cj_buigkant"])).normalized()
    basis = b.get("cj_pose_basis")
    # Middelpunt van B in rechte stand: de bounding box in lokale coördinaten via de basismatrix.
    from mathutils import Matrix
    mb = Matrix([basis[i * 4:i * 4 + 4] for i in range(4)]) if basis else b.matrix_world
    hoeken = [mb @ Vector(h) for h in b.bound_box]
    midden_b = sum(hoeken, Vector()) / 8.0
    d = lid if (midden_b - c).dot(lid) >= 0 else -lid
    zij = voor_as.cross(d)  # draaien om voor_as brengt d hierheen
    R = STRAAL * float(a["cj_knokkel_r"])

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
        "as_eind": punt(0), "grens_eind": punt(n), "label": punt(n, R * 1.25),
        "streepjes": [(g, punt(g), punt(g, R * 1.1)) for g in range(0, n + 1, STREEP)],
        "pose_eind": punt(pose, R * POSE_LANG) if pose > 0 else None, "voorbij": voorbij, "rood_vlak": rood,
        "voorbij_tekst": f"+{max(1, int(round(pose - n)))}° past limit" if voorbij else None,
    }


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
    streep, getal = [], False
    if hoek >= waaier.SCHUIN_MIN:
        streep = waaier.streep_lijnen([(g, p(s0), p(s1)) for g, s0, s1 in v["streepjes"]], schaal)
        for _, s0, s1 in streep:
            waaier._lijn(dik, regio, [s0, s1], (*WIT, 0.9), 2.0 * schaal)
        getal = waaier._tekst(0, q["label"], f"{v['getal']}°", WIT, int(20 * schaal))
    rood_tekst = False
    if q["pose_eind"] is not None:
        if v["voorbij"]:
            waaier._waaiervlak(vlak, q["centrum"], [p(x) for x in v["rood_vlak"]], (*ROOD, 0.30))
        waaier._lijn(dik, regio, [q["centrum"], q["pose_eind"]], (*(ROOD if v["voorbij"] else WIT), 1.0),
                     4.0 * schaal)
        if v["voorbij"] and hoek >= waaier.SCHUIN_MIN:
            rood_tekst = waaier._tekst(0, q["pose_eind"] + Vector((0.0, 18.0 * schaal)), v["voorbij_tekst"],
                                       ROOD, int(16 * schaal))
    # De regel van het paneel ook in beeld (winkelschermen 11 en 12), bovenaan in het midden.
    kop = tekst(a)
    kop_getekend = waaier._tekst(0, Vector((regio.width / 2.0, regio.height - 60.0 * schaal)), kop, WIT,
                                 int(28 * schaal))
    return {"pose": round(pose, 3), "getal": f"{v['getal']}°", "getal_getekend": getal,
            "streepjes": len(streep), "kijkhoek": round(hoek, 1), "voorbij": v["voorbij"],
            "voorbij_tekst": v["voorbij_tekst"] if rood_tekst else None,
            "kop": kop if kop_getekend else None}


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
        print(f"Click Joints: hinge range not drawn ({fout})")


def bij_pose(wm, context):
    """Pose-schuif: alleen de weergave, net als bij de kogel."""
    from .. import kleur
    ob = getattr(context, "active_object", None) or context.view_layer.objects.active
    a, b = paar(context.scene, ob)
    if a is None or b is None:
        return
    beweeg.pose(a, b, float(wm.cj_scharnier_pose), kleur.materiaal("rood"))


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
        name="Show bend range", default=True, description="Draw the measured bend range of the hinge")
    bpy.types.WindowManager.cj_scharnier_pose = bpy.props.FloatProperty(
        name="Bend", default=0.0, min=0.0, max=150.0,
        description="Bend part B in the view only, to check the range. Past the end stop, touching faces turn red",
        update=bij_pose)
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
