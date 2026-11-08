"""Waaier in de viewport (ronde k): per richting een taartpunt van de as tot de gemeten grens, rond het
kogelmidden, in de passingkleur, plus een dikke rand en een witte lijn voor de huidige pose.
Groot en dik genoeg voor een lijstplaatje op 1280 breed (kan-punt Daan): straal 2 keer de kogeldiameter.
In achtergrondmodus (blender -b) wordt de handler niet aangemaakt."""
import math

import bpy

from . import beweeg, passing, uit_elkaar

STRAAL = 4.0     # keer de kogelstraal (2 keer de diameter)
STUKJES = 12     # boogstukjes per taartpunt
DIK = 4.0        # lijndikte in pixels
_handler = [None]


def punten(a):
    """(taartpunten als driehoeken, randlijnen) voor deel A, in wereldcoördinaten."""
    from mathutils import Vector
    c = Vector(a["cj_centrum"])
    as_ = Vector(a["cj_as"]).normalized()
    R = STRAAL * a["cj_kogel_r"]
    rich = uit_elkaar.richtingen(as_)
    drie, lijn = [], []
    tips = []
    for k, g in enumerate(a["cj_buig_graden"]):
        boog = [c + R * (as_ * math.cos(math.radians(g * i / STUKJES)) +
                         rich[k] * math.sin(math.radians(g * i / STUKJES))) for i in range(STUKJES + 1)]
        for i in range(STUKJES):
            drie += [tuple(c), tuple(boog[i]), tuple(boog[i + 1])]
        lijn += [tuple(c), tuple(boog[-1])]
        for i in range(STUKJES):
            lijn += [tuple(boog[i]), tuple(boog[i + 1])]
        tips.append(boog[-1])
    for k in range(len(tips)):  # kegelrand door de grenzen
        lijn += [tuple(tips[k]), tuple(tips[(k + 1) % len(tips)])]
    return drie, lijn


def pose_lijn(a, b):
    from mathutils import Vector
    g = float(b.get("cj_pose_graden", 0.0))
    if g <= 0:
        return []
    c = Vector(a["cj_centrum"])
    as_ = Vector(a["cj_as"]).normalized()
    q = uit_elkaar.pose_q(b)
    return [tuple(c), tuple(c + (q @ as_) * (STRAAL * 1.15 * a["cj_kogel_r"]))]


def teken():
    import gpu
    from gpu_extras.batch import batch_for_shader
    context = bpy.context
    scene = context.scene
    inst = getattr(scene, "click_joints", None)
    if inst is None or not inst.toon_bereik:
        return
    vlak = gpu.shader.from_builtin("UNIFORM_COLOR")
    dik = gpu.shader.from_builtin("POLYLINE_UNIFORM_COLOR")
    regio = context.region
    gpu.state.blend_set("ALPHA")
    gpu.state.depth_test_set("NONE")
    for b in [o for o in scene.objects if o.get("cj_deel") == "B" and "cj_buig_graden" in o and o.visible_get()]:
        a = beweeg.paar(scene, b)
        if a is None or "cj_buig_graden" not in a:
            continue
        rgba = passing.KLEUREN.get(a.get("cj_passing", "groen"), (1, 1, 1, 1))
        drie, lijn = punten(a)
        vlak.uniform_float("color", (rgba[0], rgba[1], rgba[2], 0.28))
        batch_for_shader(vlak, "TRIS", {"pos": drie}).draw(vlak)
        dik.uniform_float("viewportSize", (regio.width, regio.height))
        dik.uniform_float("lineWidth", DIK)
        dik.uniform_float("color", (rgba[0], rgba[1], rgba[2], 1.0))
        batch_for_shader(dik, "LINES", {"pos": lijn}).draw(dik)
        pl = pose_lijn(a, b)
        if pl:
            dik.uniform_float("lineWidth", DIK + 1.0)
            dik.uniform_float("color", (1.0, 1.0, 1.0, 1.0))
            batch_for_shader(dik, "LINES", {"pos": pl}).draw(dik)
    gpu.state.blend_set("NONE")


def _veilig():
    try:
        teken()
    except Exception as fout:  # noqa: BLE001  tekenen mag Blender nooit laten vallen
        print(f"Click Joints: fan not drawn ({fout})")


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
    _handler[0] = bpy.types.SpaceView3D.draw_handler_add(_veilig, (), "WINDOW", "POST_VIEW")


def ontkoppel():
    if _handler[0] is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_handler[0], "WINDOW")
        _handler[0] = None
