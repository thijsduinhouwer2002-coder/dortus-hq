"""Gradenboog in de viewport (Daan, beoordeling 3, moet 1; was de waaier van ronde k).

De vorm staat in gradenboog.py (3D). Hier: één POST_PIXEL-handler die de punten met
`location_3d_to_region_2d` naar pixels brengt en alles tekent: wit vlak (15%), booglijn, aslijn en
grenslijn, streepjes elke 5 graden, het getal (gelijk aan het paneel), de dunne lijn door de grenzen van
alle richtingen, en de pose-lijn (rood voorbij de grens, met rood vlak en "+N° past limit").
Wit, niet de passingkleur: de delen zijn al groen, geel of rood. Pixelmaten maal ui_scale.
Punten achter de kijker slaan we over; kijk je bijna langs het vlak van de boog (onder 15 graden), dan
alleen de lijnen. In achtergrondmodus (blender -b) wordt de handler niet aangemaakt."""
import math

import bpy

from . import beweeg, gradenboog

WIT = (1.0, 1.0, 1.0)
ROOD = (1.0, 0x4D / 255.0, 0x4D / 255.0)  # #FF4D4D
SCHUIN_MIN = 15.0  # graden tussen kijkrichting en vlak van de boog, daaronder geen streepjes en getal
_handler = [None]
laatst = {}  # wat de laatste tekenbeurt tekende, voor het bewijs in de schermtest


def kijkhoek(rv3d, v):
    """Hoek in graden tussen de kijkrichting (naar het kogelmidden) en het vlak van de boog."""
    from mathutils import Vector
    inv = rv3d.view_matrix.inverted()
    if rv3d.is_perspective:
        kijk = (v["centrum"] - inv.translation)
    else:
        kijk = inv.to_3x3() @ Vector((0.0, 0.0, -1.0))
    if kijk.length == 0 or v["normaal"].length == 0:
        return 0.0
    s = abs(kijk.normalized().dot(v["normaal"].normalized()))
    return math.degrees(math.asin(min(1.0, s)))


def plat(regio, rv3d, v):
    """Projecteert de vorm naar pixels. Elke lijst laat punten achter de kijker weg (None)."""
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d

    def p(x):
        return naar2d(regio, rv3d, x) if x is not None else None
    uit = {k: p(v[k]) for k in ("centrum", "as_eind", "grens_eind", "label", "pose_eind")}
    uit["boog"] = [p(x) for x in v["boog"]]
    uit["omtrek"] = [p(x) for x in v["omtrek"]]
    uit["rood_vlak"] = [p(x) for x in v["rood_vlak"]]
    uit["streepjes"] = [(g, p(a), p(b)) for g, a, b in v["streepjes"]]
    return uit


def streep_lijnen(streepjes, schaal):
    """Streepjes naar buiten op de boog: 8 px, om de 10 graden 14 px (maal ui_scale)."""
    lijnen = []
    for g, a, b in streepjes:
        if a is None or b is None or (b - a).length == 0:
            continue
        lang = (14.0 if g % 10 == 0 else 8.0) * schaal
        lijnen.append((g, a, a + (b - a).normalized() * lang))
    return lijnen


def _lijn(shader, regio, punten, kleur, dik, soort="LINE_STRIP"):
    from gpu_extras.batch import batch_for_shader
    pts = [(x.x, x.y, 0.0) for x in punten if x is not None]
    if len(pts) < 2:
        return 0
    shader.uniform_float("viewportSize", (regio.width, regio.height))
    shader.uniform_float("lineWidth", dik)
    shader.uniform_float("color", kleur)
    batch_for_shader(shader, soort, {"pos": pts}).draw(shader)
    return len(pts)


def _waaiervlak(shader, middelpunt, rand, kleur):
    from gpu_extras.batch import batch_for_shader
    if middelpunt is None:
        return
    pts = [x for x in rand if x is not None]
    drie = []
    for i in range(len(pts) - 1):
        drie += [(middelpunt.x, middelpunt.y, 0.0), (pts[i].x, pts[i].y, 0.0), (pts[i + 1].x, pts[i + 1].y, 0.0)]
    if drie:
        shader.uniform_float("color", kleur)
        batch_for_shader(shader, "TRIS", {"pos": drie}).draw(shader)


def _tekst(font, punt, tekst, kleur, px):
    import blf
    if punt is None:
        return False
    blf.size(font, px)
    blf.enable(font, blf.SHADOW)
    blf.shadow(font, 5, 0.0, 0.0, 0.0, 0.8)
    blf.shadow_offset(font, 0, 0)
    blf.color(font, kleur[0], kleur[1], kleur[2], 1.0)
    breed, hoog = blf.dimensions(font, tekst)
    blf.position(font, punt.x - breed / 2.0, punt.y - hoog / 2.0, 0)
    blf.draw(font, tekst)
    blf.disable(font, blf.SHADOW)
    return True


def teken_een(regio, rv3d, a, b, schaal):
    """Tekent de gradenboog voor één gewricht en geeft terug wat er getekend is."""
    import gpu
    k = int(b.get("cj_pose_richting", 0))
    v = gradenboog.vorm(a, k, float(b.get("cj_pose_graden", 0.0)))
    if v is None:
        return None
    q = plat(regio, rv3d, v)
    vlak = gpu.shader.from_builtin("UNIFORM_COLOR")
    dik = gpu.shader.from_builtin("POLYLINE_UNIFORM_COLOR")
    _waaiervlak(vlak, q["centrum"], q["boog"], (*WIT, 0.15))
    _lijn(dik, regio, q["omtrek"] + q["omtrek"][:1], (*WIT, 0.45), 1.5 * schaal)
    _lijn(dik, regio, [q["centrum"], q["as_eind"]], (*WIT, 0.55), 2.0 * schaal)
    _lijn(dik, regio, [q["centrum"], q["grens_eind"]], (*WIT, 0.9), 3.0 * schaal)
    _lijn(dik, regio, q["boog"], (*WIT, 0.9), 3.0 * schaal)
    hoek = kijkhoek(rv3d, v)
    streep, getal = [], False
    if hoek >= SCHUIN_MIN:
        streep = streep_lijnen(q["streepjes"], schaal)
        for _, s0, s1 in streep:
            _lijn(dik, regio, [s0, s1], (*WIT, 0.9), 2.0 * schaal)
        getal = _tekst(0, q["label"], v["tekst"], WIT, int(20 * schaal))
    rood_tekst = False
    if q["pose_eind"] is not None:
        if v["voorbij"]:
            _waaiervlak(vlak, q["centrum"], q["rood_vlak"], (*ROOD, 0.30))
        _lijn(dik, regio, [q["centrum"], q["pose_eind"]], (*(ROOD if v["voorbij"] else WIT), 1.0), 4.0 * schaal)
        if v["voorbij"] and hoek >= SCHUIN_MIN:
            from mathutils import Vector
            plek = q["pose_eind"] + Vector((0.0, 18.0 * schaal))
            rood_tekst = _tekst(0, plek, v["voorbij_tekst"], ROOD, int(16 * schaal))
    return {"pose": round(float(b.get("cj_pose_graden", 0.0)), 3), "richting": k, "getal": v["tekst"], "getal_getekend": getal, "streepjes": len(streep), "kijkhoek": round(hoek, 1),
            "omtrek": sum(1 for x in q["omtrek"] if x is not None), "voorbij": v["voorbij"],
            "voorbij_tekst": v["voorbij_tekst"] if rood_tekst else None, "label_px": tuple(q["label"]) if q["label"] else None}


def teken():
    import gpu
    context = bpy.context
    scene = context.scene
    inst = getattr(scene, "click_joints", None)
    if inst is None or not inst.toon_bereik:
        return
    regio, rv3d = context.region, context.region_data
    if regio is None or rv3d is None:
        return
    schaal = context.preferences.system.ui_scale
    gpu.state.blend_set("ALPHA")
    gpu.state.depth_test_set("NONE")
    getekend = []
    for b in [o for o in scene.objects if o.get("cj_deel") == "B" and "cj_buig_graden" in o and o.visible_get()]:
        a = beweeg.paar(scene, b)
        if a is None or "cj_buig_graden" not in a:
            continue
        uit = teken_een(regio, rv3d, a, b, schaal)
        if uit:
            getekend.append(uit)
    gpu.state.blend_set("NONE")
    laatst.clear()
    laatst.update({"bogen": getekend})


def _veilig():
    try:
        teken()
    except Exception as fout:  # noqa: BLE001  tekenen mag Blender nooit laten vallen
        print(f"Click Joints: bend range not drawn ({fout})")


class CLICK_JOINTS_OT_reset_pose(bpy.types.Operator):
    bl_idname = "click_joints.reset_pose"
    bl_label = "Reset bend"
    bl_description = "Put part B back in the straight position"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        context.scene.click_joints.pose_graden = 0.0  # de update zet alles terug en haalt het rood weg
        return {"FINISHED"}


KLASSEN = (CLICK_JOINTS_OT_reset_pose,)


def koppel():
    if bpy.app.background or _handler[0] is not None:
        return
    _handler[0] = bpy.types.SpaceView3D.draw_handler_add(_veilig, (), "WINDOW", "POST_PIXEL")


def ontkoppel():
    if _handler[0] is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_handler[0], "WINDOW")
        _handler[0] = None
