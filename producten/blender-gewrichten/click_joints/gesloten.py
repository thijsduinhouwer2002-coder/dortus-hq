"""Manifold-check (elke rand precies 2 vlakken) en Maak gesloten (voxel-remesh op een kopie)."""
import bmesh
import bpy
import numpy as np

from .eigenschappen import eenheid_per_mm


def foute_randen(me):
    """Aantal randen dat niet precies 2 vlakken heeft (open of niet-manifold)."""
    if not me.edges:
        return 0
    idx = np.empty(len(me.loops), dtype=np.int32)
    me.loops.foreach_get("edge_index", idx)
    telling = np.bincount(idx, minlength=len(me.edges))
    return int(np.count_nonzero(telling != 2))


def volume(me):
    bm = bmesh.new()
    bm.from_mesh(me)
    v = bm.calc_volume(signed=True)
    bm.free()
    return v


def is_gesloten(me):
    fout = foute_randen(me)
    return fout == 0 and len(me.polygons) > 0 and volume(me) > 0, fout


class CLICK_JOINTS_OT_controleer(bpy.types.Operator):
    bl_idname = "click_joints.controleer"
    bl_label = "Controleer figuur"
    bl_description = "Kijk of het figuur gesloten is (elke rand precies 2 vlakken)"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        ob = context.active_object
        ok, fout = is_gesloten(ob.data)
        ob["cj_gesloten"] = ok
        if ok:
            self.report({"INFO"}, f"{ob.name} is gesloten")
        else:
            self.report({"WARNING"}, f"{ob.name} is niet gesloten: {fout} randen zonder precies 2 vlakken. "
                                     "Gebruik Maak gesloten.")
        return {"FINISHED"}


class CLICK_JOINTS_OT_maak_gesloten(bpy.types.Operator):
    bl_idname = "click_joints.maak_gesloten"
    bl_label = "Maak gesloten"
    bl_description = "Maak een gesloten kopie met een voxel-remesh. Het origineel blijft verborgen bewaard"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        bron = context.active_object
        inst = context.scene.click_joints
        tijdelijk = bpy.data.objects.new(bron.name + "_cj_tmp", bron.data)
        context.scene.collection.objects.link(tijdelijk)
        tijdelijk.matrix_world = bron.matrix_world
        mod = tijdelijk.modifiers.new("cj_remesh", "REMESH")
        mod.mode = "VOXEL"
        mod.voxel_size = inst.voxel_mm * eenheid_per_mm(context.scene)
        dg = context.evaluated_depsgraph_get()
        me = bpy.data.meshes.new_from_object(tijdelijk.evaluated_get(dg))
        bpy.data.objects.remove(tijdelijk)
        me.name = bron.name + "_gesloten"
        kopie = bpy.data.objects.new(bron.name + "_gesloten", me)
        for c in bron.users_collection:
            c.objects.link(kopie)
        kopie.matrix_world = bron.matrix_world
        ok, fout = is_gesloten(me)
        if not ok:
            bpy.data.objects.remove(kopie)
            bpy.data.meshes.remove(me)
            self.report({"ERROR"}, f"Maak gesloten lukte niet ({fout} foute randen). Probeer een grotere voxel.")
            return {"CANCELLED"}
        kopie["cj_gesloten"] = True
        kopie["cj_bron"] = bron.name
        bron.hide_set(True)
        context.view_layer.update()
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(False)
        kopie.select_set(True)
        context.view_layer.objects.active = kopie
        self.report({"INFO"}, f"Gesloten kopie {kopie.name} gemaakt ({len(me.polygons)} vlakken)")
        return {"FINISHED"}


KLASSEN = (CLICK_JOINTS_OT_controleer, CLICK_JOINTS_OT_maak_gesloten)
