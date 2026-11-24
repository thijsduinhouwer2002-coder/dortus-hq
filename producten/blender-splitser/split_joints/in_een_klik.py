"""Split to fit: one button that does Make watertight (only when needed), Plan cuts, Split (pins, holes,
numbers) and the check, with the printer and the clearance that are set (the saved one from the fit test
comes in through passingproef). The result is one line in the panel (scene.split_joints.uitslag)."""
import bpy

from . import gesloten, snedes


def _maak_actief(context, ob):
    ob.hide_set(False)
    for o in context.view_layer.objects:
        if o is not None:
            o.select_set(False)
    ob.select_set(True)
    context.view_layer.objects.active = ob


def _doe(op):
    """Runs one of our operators; an ERROR report raises in bpy.ops, that counts as not done."""
    try:
        return op() == {"FINISHED"}
    except RuntimeError as e:
        return str(e).strip()


def kies_model(context):
    """The selected model: the active mesh when it can be split (keuring 24 nov, M1: a second model in the
    scene was ignored), else the model of the cuts (a piece is active after a split)."""
    ob = context.active_object
    if ob is not None and ob.type == "MESH" and "sj_as" not in ob and not ob.get("sj_stuk") \
            and not ob.get("sj_pennen") and not ob.get("sj_passing") and not ob.get("sj_vrij"):
        return ob
    return snedes.model(context)


ZWAAR_VLAKKEN = 1_000_000


def zwaar_tekst(context):
    """One line for the panel when the selected model has a million faces or more, else None. Speed test
    24 nov (e2e/snelheid.py): 1M faces about 40 s, 3M about 2 min for Split to fit on 2 cores in Blender 5.3."""
    ob = kies_model(context)
    if ob is None or ob.type != "MESH":
        return None
    n = len(ob.data.polygons)
    if n < ZWAAR_VLAKKEN:
        return None
    return f"{n / 1e6:.1f}M faces: Split can take a few minutes"


def uitslag_tekst(scene):
    """(main line, detail line, ok) from the pieces in the scene, or None when there are none."""
    stukken = [o for o in scene.objects if o.get("sj_stuk")]
    if not stukken:
        return None
    inst = scene.split_joints
    n = len(stukken)
    niet = [o for o in stukken if o.get("sj_status") != "groen"]
    pennen = sum(int(o["sj_pennen"]) for o in scene.objects if o.get("sj_pennen"))
    if not niet:
        hoofd = f"{n} parts, all fit the bed" if n != 1 else "1 part, it fits the bed"
    else:
        hoofd = f"{n} parts, {len(niet)} need attention"  # "see step 4" is its own line in the panel (cut off)
    detail = f"{pennen} pins, {inst.speling_mm:.2f} mm clearance"
    return hoofd, detail, not niet


class SPLIT_JOINTS_OT_split_to_fit(bpy.types.Operator):
    bl_idname = "split_joints.split_to_fit"
    bl_label = "Split to fit"
    bl_description = ("Cut the selected model into pieces that fit your printer, with pins, holes and numbers, "
                      "in one click (makes a watertight copy first when the model is open)")
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return kies_model(context) is not None

    def execute(self, context):
        scene = context.scene
        inst = scene.split_joints
        ob = kies_model(context)
        if ob is None:
            inst.uitslag = "Select the model first"
            self.report({"ERROR"}, inst.uitslag)
            return {"CANCELLED"}
        _maak_actief(context, ob)
        melding = snedes.te_groot_tekst(ob, scene)
        if melding:
            inst.uitslag = "Wrong unit? Open More settings and use Convert to mm"
            self.report({"ERROR"}, melding)
            return {"CANCELLED"}
        stappen = []
        ok, _fout = gesloten.is_gesloten(ob)
        if not ok:
            if _doe(bpy.ops.split_joints.maak_gesloten) is not True:
                inst.uitslag = "The model is open and could not be made watertight. Try a larger voxel size"
                self.report({"ERROR"}, inst.uitslag)
                return {"CANCELLED"}
            stappen.append("watertight copy made")
            ob = context.active_object
        if _doe(bpy.ops.split_joints.plan) is not True:
            inst.uitslag = "No plan: check the unit or pick a bigger printer"
            self.report({"ERROR"}, inst.uitslag)
            return {"CANCELLED"}
        gelukt = _doe(bpy.ops.split_joints.split)
        if gelukt is not True:
            inst.uitslag = "Split did not work: " + (gelukt.replace("Error: ", "") if gelukt else "see the info log")
            self.report({"ERROR"}, inst.uitslag)
            return {"CANCELLED"}
        uit = uitslag_tekst(scene)
        if uit is None:
            inst.uitslag = "No pieces came out"
            self.report({"ERROR"}, inst.uitslag)
            return {"CANCELLED"}
        hoofd, detail, goed = uit
        inst.uitslag = ""  # the panel shows the live result of the pieces
        scene["sj_klik_stappen"] = ", ".join(stappen)
        self.report({"INFO"} if goed else {"WARNING"}, f"{hoofd}. {detail}")
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_split_to_fit,)
