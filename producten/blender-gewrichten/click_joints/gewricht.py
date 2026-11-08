"""Operator click_joints.plaats: snijdt het actieve figuur in twee gesloten delen met een gewricht.

Werkt op kopieën in wereldcoördinaten; het origineel blijft verborgen staan zodat het terug te halen is.
Booleans: Manifold-solver op Blender 4.5+, anders Exact. Het snijvlak ligt een fractie naast de
3D-cursor, want een snijvlak precies door bestaande punten gaf in 4.2 open randen.
"""
import time

import bmesh
import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

from . import passing, vormen
from .eigenschappen import eenheid_per_mm
from .gesloten import is_gesloten

SCHUIF_MM = 0.0137


def solver_naam():
    solvers = {s.identifier for s in bpy.types.BooleanModifier.bl_rna.properties["solver"].enum_items}
    if bpy.app.version >= (4, 5, 0) and "MANIFOLD" in solvers:
        return "MANIFOLD"
    return "EXACT"


def maten(inst, u):
    r = inst.kogel_mm / 2 * u
    maat = {"r": r, "s": inst.speling_mm * u, "nek_r": 0.48 * r, "schuif": SCHUIF_MM * u,
            "onder_z": -0.4 * r, "midden_z": 1.2 * r, "top_z": 2.2 * r}
    if inst.soort == "PEN":
        maat["midden_z"] = maat["top_z"] / 2
    return maat


def as_en_punt(context, inst):
    cursor = context.scene.cursor
    rv3d = getattr(context, "region_data", None)
    if inst.as_bron == "KIJK" and rv3d is not None and hasattr(rv3d, "view_rotation"):
        richting = rv3d.view_rotation @ Vector((0, 0, -1))
    else:
        richting = cursor.matrix.col[2].xyz
    return cursor.location.copy(), richting.normalized()


def boolean(doel, gereedschap, actie, solver):
    m = doel.modifiers.new(f"{actie}_{gereedschap.name}", "BOOLEAN")
    m.operation = actie
    m.object = gereedschap
    m.solver = solver
    if solver == "EXACT":
        m.use_self = False
        m.use_hole_tolerant = False
    gereedschap.hide_set(True)


def bak(ob, naam, collectie):
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    me.name = naam
    uit = bpy.data.objects.new(naam, me)
    collectie.objects.link(uit)
    return uit


def ruim_op(collectie):
    for ob in list(collectie.objects):
        me = ob.data
        bpy.data.objects.remove(ob)
        if me is not None and me.users == 0:
            bpy.data.meshes.remove(me)
    bpy.data.collections.remove(collectie)


def snij(hulp, werk, frame, maat, soort, solver):
    """Maakt deel A (met kogel of pen) en deel B (met kom of gat) in de hulpcollectie."""
    groot = max(werk.dimensions) * 2 + 20 * maat["r"]
    s = maat["s"]
    boven = vormen.doos("cj_boven", groot, maat["schuif"], groot, frame, hulp)
    onder = vormen.doos("cj_onder", groot, -groot, maat["schuif"], frame, hulp)
    if soort == "KOGEL":
        kogel = vormen.bol("cj_kogel", maat["r"], maat["midden_z"], frame, hulp)
        nek = vormen.cilinder("cj_nek", maat["nek_r"], maat["onder_z"], maat["midden_z"], frame, hulp)
        kom = vormen.bol("cj_kom", maat["r"] + s, maat["midden_z"], frame, hulp)
        gat = vormen.cilinder("cj_nekgat", maat["nek_r"] + s, maat["onder_z"], maat["midden_z"], frame, hulp)
        uitsteek = [kogel, nek]
    else:
        pen = vormen.cilinder("cj_pen", maat["r"], maat["onder_z"], maat["top_z"], frame, hulp)
        kom = vormen.cilinder("cj_gat", maat["r"] + s, maat["onder_z"] - s, maat["top_z"] + s, frame, hulp)
        gat = None
        uitsteek = [pen]
    a = bak(werk, "cj_a_bron", hulp)
    boolean(a, boven, "DIFFERENCE", solver)
    for vorm in uitsteek:
        boolean(a, vorm, "UNION", solver)
    deel_a = bak(a, "cj_deel_a", hulp)
    if gat is not None:
        # Kom en nekgat eerst samen tot één gesloten snijvorm (les uit de bouwproef op 4.2).
        boolean(kom, gat, "UNION", solver)
        kom = bak(kom, "cj_snijvorm", hulp)
        kom.hide_set(True)
    b = bak(werk, "cj_b_bron", hulp)
    boolean(b, onder, "DIFFERENCE", solver)
    boolean(b, kom, "DIFFERENCE", solver)
    deel_b = bak(b, "cj_deel_b", hulp)
    return deel_a, deel_b


def verhuis(ob, naam, bron):
    for c in list(ob.users_collection):
        c.objects.unlink(ob)
    for c in bron.users_collection:
        c.objects.link(ob)
    ob.name = naam
    ob.data.name = naam


def markeer(ob, kleur, gegevens):
    ob["cj_passing"] = kleur
    for k, v in gegevens.items():
        ob[k] = v
    ob.color = passing.KLEUREN[kleur]


class CLICK_JOINTS_OT_plaats(bpy.types.Operator):
    bl_idname = "click_joints.plaats"
    bl_label = "Plaats gewricht"
    bl_description = "Snijd het figuur op de 3D-cursor in twee gesloten delen met een gewricht"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        t0 = time.perf_counter()
        bron = context.active_object
        inst = context.scene.click_joints
        ok, fout = is_gesloten(bron.data)
        if not ok:
            self.report({"ERROR"}, f"Het figuur {bron.name} is niet gesloten ({fout} randen zonder precies "
                                   "2 vlakken). Klik eerst op Maak gesloten.")
            return {"CANCELLED"}
        u = eenheid_per_mm(context.scene)
        maat = maten(inst, u)
        punt, richting = as_en_punt(context, inst)
        frame = vormen.frame_voor(punt, richting)
        solver = solver_naam()

        hulp = bpy.data.collections.new("cj_hulp")
        context.scene.collection.children.link(hulp)
        dg = context.evaluated_depsgraph_get()
        me = bpy.data.meshes.new_from_object(bron.evaluated_get(dg))
        me.transform(bron.matrix_world)
        werk = bpy.data.objects.new("cj_werk", me)
        hulp.objects.link(werk)
        bm = bmesh.new()
        bm.from_mesh(me)
        bvh = BVHTree.FromBMesh(bm)
        bm.free()
        kleur, wand, uitleg = passing.beoordeel(bvh, frame, maat, inst.soort, u)
        centrum = frame @ Vector((0, 0, maat["midden_z"]))
        gegevens = {"cj_bron": bron.name, "cj_soort": inst.soort, "cj_speling_mm": inst.speling_mm,
                    "cj_wand_mm": round(wand, 3), "cj_centrum": list(centrum), "cj_as": list(richting),
                    "cj_kogel_r": maat["r"], "cj_solver": solver}

        if kleur == "rood":
            ruim_op(hulp)
            teken = vormen.bol(f"{bron.name}_gewricht_rood", maat["r"] + maat["s"], maat["midden_z"], frame,
                               bron.users_collection[0])
            markeer(teken, kleur, gegevens)
            teken.display_type = "WIRE"
            self.report({"WARNING"}, f"Rood: {uitleg}. Er is niet gesneden; kies een dikkere plek of een "
                                     "kleinere diameter.")
            return {"FINISHED"}

        deel_a, deel_b = snij(hulp, werk, frame, maat, inst.soort, solver)
        goed = all(is_gesloten(d.data)[0] for d in (deel_a, deel_b))
        if not goed:
            ruim_op(hulp)
            self.report({"ERROR"}, "Het snijden gaf geen gesloten delen; het figuur is niet veranderd.")
            return {"CANCELLED"}
        for deel, letter in ((deel_a, "A"), (deel_b, "B")):
            verhuis(deel, f"{bron.name}_{letter}", bron)
            deel["cj_deel"] = letter
        if inst.soort == "KOGEL":
            bm = bmesh.new()
            bm.from_mesh(deel_b.data)
            bvh_b = BVHTree.FromBMesh(bm)
            bm.free()
            afst = passing.meet_speling(deel_a, bvh_b, centrum, maat["r"], richting, 1e-3 * maat["r"])
            if afst:
                gegevens["cj_speling_gemeten_mm"] = round(sum(afst) / len(afst) / u, 4)
        ruim_op(hulp)
        gegevens["cj_duur_s"] = round(time.perf_counter() - t0, 3)
        for deel in (deel_a, deel_b):
            markeer(deel, kleur, gegevens)
        bron.hide_set(True)
        for o in context.view_layer.objects:
            o.select_set(False)
        deel_a.select_set(True)
        deel_b.select_set(True)
        context.view_layer.objects.active = deel_a
        ruimte = getattr(context, "space_data", None)
        if ruimte is not None and ruimte.type == "VIEW_3D":
            ruimte.shading.color_type = "OBJECT"
        self.report({"INFO"}, f"Gewricht geplaatst, passing {kleur} ({uitleg}), {gegevens['cj_duur_s']} s")
        return {"FINISHED"}


KLASSEN = (CLICK_JOINTS_OT_plaats,)
