"""Fit test (must have 1 of concurrentie.md): one button makes a small block with your own pin on four
clearances, the clearance engraved in front of every hole, plus four pins. After printing you click the one
that fits; that clearance is saved per printer and material in the add-on preferences, so it comes back in
every file. Layout and saved values: passing.py (no bpy)."""
import os

import bpy
from bpy.props import FloatProperty, StringProperty
from mathutils import Vector

from . import drie_mf, passing, printers, splitsen
from .eigenschappen import eenheid_per_mm
from .exporteer import exportmap
from .gesloten import is_gesloten
from .verbind_3d import EXTRA_DIEPTE_MM

COLLECTIE = "Click Cuts fit test"
AFSTAND_MM = 15.0  # room between the model and the fit test
_GEHEUGEN = {"json": ""}  # used when the preferences are not there (add-on loaded as a plain module)


class SplitJointsVoorkeuren(bpy.types.AddonPreferences):
    bl_idname = __package__
    spelingen_json: StringProperty(name="Saved clearances", default="{}")

    def draw(self, context):
        d = passing.lees(self.spelingen_json)
        kol = self.layout.column(align=True)
        if not d:
            kol.label(text="No saved clearances yet. Print a fit test (sidebar, step 3).")
        for k, v in sorted(d.items()):
            printer, _, materiaal = k.partition("|")
            kol.label(text=f"{printer_naam(printer)} + {materiaal_naam(materiaal)}: {v:.2f} mm")


def _voorkeuren(context):
    addon = context.preferences.addons.get(__package__)
    return addon.preferences if addon is not None and addon.preferences is not None else None


def lees_json(context):
    vk = _voorkeuren(context)
    return vk.spelingen_json if vk is not None else _GEHEUGEN["json"]


def schrijf_json(context, tekst):
    vk = _voorkeuren(context)
    if vk is not None:
        vk.spelingen_json = tekst
        context.preferences.is_dirty = True  # saved with the preferences (auto save) when Blender closes
    else:
        _GEHEUGEN["json"] = tekst


def printer_naam(sleutel):
    return {k: n for k, n, _m in printers.PRINTERS}.get(sleutel, "Custom size" if sleutel == printers.EIGEN else sleutel)


def materiaal_naam(sleutel):
    return {k: n for k, n, _o in passing.MATERIALEN}.get(sleutel, sleutel)


_BEZIG = [False]  # True while the add-on itself sets the clearance (not the user)


def zet_speling(scene, s):
    _BEZIG[0] = True
    try:
        scene.split_joints.speling_mm = s
    finally:
        _BEZIG[0] = False
    if "sj_speling_eigen" in scene:
        del scene["sj_speling_eigen"]


def speling_gezet(scene):
    """Update of speling_mm: typed by the user means: do not replace it on opening the file."""
    if not _BEZIG[0]:
        scene["sj_speling_eigen"] = True


def pas_toe(context, scene=None, start=False):
    """Printer or material changed (or a file opened): use the saved clearance for that pair, if there is one.
    start=True (material changed): with nothing saved and no clearance typed by the user, use the start clearance
    of the material, so the fit test is around the right value (resin 0.10, TPU 0.30). A printer change without
    a saved value keeps the clearance: a fit test from another printer is a better start than the table."""
    scene = scene or context.scene
    inst = scene.split_joints
    s = passing.opgeslagen(lees_json(context), inst.printer, inst.materiaal)
    if s is None and start and not scene.get("sj_speling_eigen"):
        s = passing.startspeling(inst.materiaal)
    if s is not None and abs(inst.speling_mm - s) > 1e-6:
        zet_speling(scene, s)


@bpy.app.handlers.persistent
def sj_laden(_bestand=None):
    """New or opened file: every scene without a clearance typed by the user gets the saved one (keurder M2)."""
    for scene in bpy.data.scenes:
        if hasattr(scene, "split_joints") and not scene.get("sj_speling_eigen"):
            pas_toe(bpy.context, scene)


def koppel():
    if sj_laden not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(sj_laden)
    bpy.app.timers.register(lambda: sj_laden() and None, first_interval=0.1)


def ontkoppel():
    if sj_laden in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(sj_laden)


def _plek_mm(context, u):
    """Front left corner (mm) for the fit test: behind everything that is visible, on the floor."""
    xs, ys = [], []
    for o in context.scene.objects:
        if o.type != "MESH" or not o.visible_get() or o.get("sj_passing"):
            continue
        for h in o.bound_box:
            p = o.matrix_world @ Vector(h)
            xs.append(p.x / u)
            ys.append(p.y / u)
    if not ys:
        return 0.0, 0.0
    return min(xs), max(ys) + AFSTAND_MM


def ruim_op(context):
    col = bpy.data.collections.get(COLLECTIE)
    if col is not None:
        for ob in list(col.objects):
            splitsen.weg(ob)
        bpy.data.collections.remove(col)


def proef_objecten(context):
    col = bpy.data.collections.get(COLLECTIE)
    return [o for o in col.objects if o.get("sj_passing")] if col is not None else []


class SPLIT_JOINTS_OT_passing_maak(bpy.types.Operator):
    bl_idname = "split_joints.passing_maak"
    bl_label = "Make fit test"
    bl_description = ("A small block with your pin on 4 clearances (engraved) plus 4 pins. Print it and pick the "
                      "clearance where the pin slides in by hand without wobble")
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        scene = context.scene
        inst = scene.split_joints
        u = eenheid_per_mm(scene)
        actief = context.view_layer.objects.active
        if actief is not None and actief.get("sj_passing"):
            actief = None
        ruim_op(context)
        m = passing.maten(inst.pen_mm, inst.pen_lengte_mm, inst.wand_mm, inst.speling_mm, EXTRA_DIEPTE_MM)
        x0, y0 = _plek_mm(context, u)
        schuif = [x0 - m["mn"][0], y0 - m["mn"][1], 0.0]

        def verschoven(lijst):
            uit = []
            for d in lijst:
                d = dict(d)
                d["p"] = [d["p"][i] + schuif[i] for i in range(3)]
                uit.append(d)
            return uit

        gaten = verschoven(m["gaten"])
        nummers = verschoven(m["nummers"])
        col = splitsen.nieuwe_collectie(COLLECTIE, scene)
        hulp = bpy.data.collections.new("sj_passing_hulp")
        scene.collection.children.link(hulp)
        solver = splitsen.solver_naam()
        meldingen = []
        try:
            mn = [m["mn"][i] + schuif[i] for i in range(3)]
            mx = [m["mx"][i] + schuif[i] for i in range(3)]
            doos = splitsen.vormen.doos("sj_passing_doos", mn, mx, u, hulp)
            werk = doos
            lbo = splitsen.label_object("sj_passing_nummers", nummers, passing.GRAVEER_MM, u, hulp, meldingen)
            if lbo is not None:
                werk, _f = splitsen.verschil(werk, lbo, solver, "sj_passing_werk", hulp, u, voxel_mm=0.05)
            gat = splitsen.gat_object("sj_passing_gaten", gaten, u, hulp)
            werk, _f = splitsen.verschil(werk, gat, solver, "sj_passing_werk2", hulp, u)
            blok = splitsen.bak(werk, "Fit test block", col)
            dicht, _ = is_gesloten(blok.data)
            stap = inst.pen_mm + 4.0
            voet = (mx[0] + 6.0 + inst.pen_mm / 2.0, mn[1] + inst.pen_mm / 2.0 + 1.0, 0.0)
            pennen, _breed = splitsen.pennen_object("Fit test pins", inst.pen_mm, passing.AANTAL, inst.pen_lengte_mm,
                                                    voet, u, col)
        finally:
            for ob in list(hulp.objects):
                splitsen.weg(ob)
            bpy.data.collections.remove(hulp)
        import json
        for ob in (blok, pennen):
            ob["sj_passing"] = "blok" if ob is blok else "pennen"
            ob["sj_pen_d"] = inst.pen_mm
            ob["sj_pen_lengte"] = inst.pen_lengte_mm
        blok["sj_gaten"] = json.dumps(gaten)
        blok["sj_spelingen"] = m["spelingen"]
        blok["sj_printer"] = inst.printer
        blok["sj_materiaal"] = inst.materiaal
        blok["sj_gesloten"] = bool(dicht)
        pennen["sj_aantal"] = passing.AANTAL
        # the model stays active and selected (keurder M1): Plan cuts and Split keep working on the model
        blok.select_set(False)
        pennen.select_set(False)
        if actief is not None and actief.name in context.view_layer.objects:
            context.view_layer.objects.active = actief
        if meldingen or not dicht:
            self.report({"WARNING"}, "The fit test block is not watertight" if not dicht else meldingen[0])
        else:
            lijst = ", ".join(passing.tekst(s) for s in m["spelingen"])
            self.report({"INFO"}, f"Fit test made: {inst.pen_mm:g} mm pin, clearances {lijst} mm")
        return {"FINISHED"}


class SPLIT_JOINTS_OT_passing_kies(bpy.types.Operator):
    bl_idname = "split_joints.passing_kies"
    bl_label = "This one fits"
    bl_description = "Use this clearance and remember it for this printer and material"
    bl_options = {"REGISTER", "UNDO"}

    waarde: FloatProperty(name="Clearance (mm)", default=0.2, min=0.0, max=1.0, precision=2)

    def execute(self, context):
        inst = context.scene.split_joints
        zet_speling(context.scene, self.waarde)
        schrijf_json(context, passing.bewaar(lees_json(context), inst.printer, inst.materiaal, self.waarde))
        self.report({"INFO"}, f"Clearance {self.waarde:.2f} mm saved for {printer_naam(inst.printer)} + "
                              f"{materiaal_naam(inst.materiaal)}")
        return {"FINISHED"}


class SPLIT_JOINTS_OT_passing_export(bpy.types.Operator):
    bl_idname = "split_joints.passing_export"
    bl_label = "Export fit test"
    bl_description = "Write the fit test block and its pins as STL or 3MF files in millimeters"

    def execute(self, context):
        lijst = proef_objecten(context)
        if not lijst:
            self.report({"WARNING"}, "Make the fit test first")
            return {"CANCELLED"}
        formaat = context.scene.split_joints.formaat
        if formaat == "STL" and "stl_export" not in dir(bpy.ops.wm):
            self.report({"ERROR"}, "This Blender has no STL export (needs 4.2 or newer)")
            return {"CANCELLED"}
        map_ = exportmap(context.scene)
        os.makedirs(map_, exist_ok=True)
        schaal = 1.0 / eenheid_per_mm(context.scene)
        actief = context.view_layer.objects.active
        geschreven = []
        for ob in lijst:
            naam = "fit_test_block" if ob["sj_passing"] == "blok" else "fit_test_pins"
            pad = os.path.join(map_, naam + (".3mf" if formaat == "3MF" else ".stl"))
            if formaat == "3MF":
                drie_mf.schrijf(ob, pad, schaal)
            else:
                for o in context.view_layer.objects:
                    if o is not None:
                        o.select_set(False)
                ob.select_set(True)
                context.view_layer.objects.active = ob
                bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True, global_scale=schaal,
                                      use_scene_unit=False, ascii_format=False, apply_modifiers=True)
            ob["sj_bestand"] = pad
            geschreven.append(pad)
        context.view_layer.objects.active = actief
        self.report({"INFO"}, f"{len(geschreven)} {formaat} files in {map_}")
        return {"FINISHED"}


def teken(layout, context):
    """Fit test box inside step 3 of the panel."""
    inst = context.scene.split_joints
    vak = layout.box()
    vak.label(text="Fit test: print this first", icon="CHECKBOX_HLT")
    vak.prop(inst, "materiaal")
    opgeslagen = passing.opgeslagen(lees_json(context), inst.printer, inst.materiaal)
    if opgeslagen is not None:
        if abs(opgeslagen - inst.speling_mm) < 1e-6:
            vak.label(text=f"Saved for this printer: {opgeslagen:.2f} mm", icon="CHECKMARK")
        else:
            vak.operator(SPLIT_JOINTS_OT_passing_kies.bl_idname, text=f"Use saved {opgeslagen:.2f} mm",
                         icon="LOOP_BACK").waarde = opgeslagen
    elif not context.scene.get("sj_speling_eigen") and \
            abs(inst.speling_mm - passing.startspeling(inst.materiaal)) < 1e-6:
        vak.label(text=f"Start value for {materiaal_naam(inst.materiaal)}: print the fit test", icon="INFO")
    lijst = passing.spelingen(inst.speling_mm)
    vak.operator(SPLIT_JOINTS_OT_passing_maak.bl_idname,
                 text=f"Make fit test ({passing.tekst(lijst[0])} to {passing.tekst(lijst[-1])} mm)", icon="MESH_CUBE")
    blok = next((o for o in proef_objecten(context) if o["sj_passing"] == "blok"), None)
    if blok is not None:
        vak.operator(SPLIT_JOINTS_OT_passing_export.bl_idname, text=f"Export fit test ({inst.formaat})",
                     icon="EXPORT")
        vak.label(text="Printed? Click the one that fits:")
        rij = vak.row(align=True)
        for s in blok.get("sj_spelingen", []):
            knop = rij.operator(SPLIT_JOINTS_OT_passing_kies.bl_idname, text=passing.tekst(s),
                                depress=abs(s - inst.speling_mm) < 1e-6)
            knop.waarde = s


KLASSEN = (SplitJointsVoorkeuren, SPLIT_JOINTS_OT_passing_maak, SPLIT_JOINTS_OT_passing_kies,
           SPLIT_JOINTS_OT_passing_export)
