"""Split to fit: one button that does Make watertight (only when needed), Plan cuts, Split (pins, holes,
numbers) and the check, with the printer and the clearance that are set (the saved one from the fit test
comes in through passingproef). The result is one line in the panel (scene.split_joints.uitslag)."""
import math

import bpy

from . import gesloten, snedes
from .eigenschappen import magneten


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


WATERDICHT_ACHTERVOEGSEL = "_watertight"  # name Make watertight gives the copy (gesloten.py)


def model_tekst(naam, n):
    """Panel line that names the model Split to fit will cut, like Cleave shows "TV_robot · 1,982,604 faces"
    (issue #69: the buyer sees what will be cut before the click)."""
    if naam.endswith(WATERDICHT_ACHTERVOEGSEL):  # keuring #74 K1: the suffix is internal, a buyer reads words
        naam = naam[:-len(WATERDICHT_ACHTERVOEGSEL)] + " (closed)"  # short: "(watertight copy)" was cut off at the default width
    return f"{naam}: {n:,} faces"


GEEN_MODEL = "Click your model in the viewport"


ZWAAR_VLAKKEN = 1_000_000
# Seconds per million faces for Split to fit, from the speed test on the 1M face skull scan (e2e/snelheid.py):
# Manifold (4.5+) 44 s on GitHub (run 45349335526) and 42 s on 2 cores; Exact (4.2) 106 s on GitHub but
# 186 s on 2 cores (24 nov). The slowest measure counts, rounded up, so the panel never promises less.
SEC_PER_MILJOEN = {"MANIFOLD": 45, "EXACT": 190}


def schatting_tekst(n, solver):
    """Panel line for a model of n faces with this solver, or None below ZWAAR_VLAKKEN."""
    if n < ZWAAR_VLAKKEN:
        return None
    sec = SEC_PER_MILJOEN.get(solver, SEC_PER_MILJOEN["EXACT"]) * n / 1e6
    minuten = max(1, math.ceil(sec / 60))
    return f"{n / 1e6:.1f}M faces: Split takes about {minuten} min"


# Peak memory per million faces during Split to fit, from the same speed test: Manifold 4.7 GB at 3M (2 cores,
# 24 nov), Exact 9.2 GB at 3M (run 45367520845). Rounded up. Warn from 8 GB: a laptop with 8 GB runs out.
GB_PER_MILJOEN = {"MANIFOLD": 1.6, "EXACT": 3.1}
GEHEUGEN_GRENS_GB = 8


def geheugen_tekst(n, solver):
    """Second panel line when Split to fit needs GEHEUGEN_GRENS_GB of memory or more, else None (Daan K, 24 nov)."""
    gb = GB_PER_MILJOEN.get(solver, GB_PER_MILJOEN["EXACT"]) * n / 1e6
    if gb < GEHEUGEN_GRENS_GB:
        return None
    return f"Needs about {math.ceil(gb)} GB of memory"


def zwaar_tekst(context):
    """One line for the panel when the selected model has a million faces or more, else None."""
    ob = kies_model(context)
    if ob is None or ob.type != "MESH":
        return None
    from .splitsen import solver_naam
    return schatting_tekst(len(ob.data.polygons), solver_naam())


def geheugen_regel(context):
    """The memory line for the selected model, or None."""
    ob = kies_model(context)
    if ob is None or ob.type != "MESH":
        return None
    from .splitsen import solver_naam
    return geheugen_tekst(len(ob.data.polygons), solver_naam())


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
    mag = magneten(scene)
    if mag:
        detail = ", ".join(f"{n} magnets {k} mm" for k, n in sorted(mag.items()))
        detail += f", {inst.speling_mm:.2f} mm clearance"
    else:
        detail = f"{pennen} pins, {inst.speling_mm:.2f} mm clearance"
    return hoofd, detail, not niet


def noten_regel(meldingen, meer_open):
    """Line for the result box when Split left notes (glue this joint, ...) and More settings is closed, so the
    buyer knows they are there (keuring winkeltekst K1: the notes hid under the closed More settings)."""
    n = len([r for r in (meldingen or "").split("\n") if r.strip()])
    if n == 0 or meer_open:
        return None
    return f"{n} note{'s' if n != 1 else ''}: see More settings"


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
        # keuring K5 (oranje-k5-k6): cuts moved by hand on this same model are kept, not planned again
        eigen_snedes = snedes.verschoven(scene) and scene.get("sj_gesneden_model") == ob.name
        if eigen_snedes:
            stappen.append("kept your moved cuts")
        elif _doe(bpy.ops.split_joints.plan) is not True:
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
