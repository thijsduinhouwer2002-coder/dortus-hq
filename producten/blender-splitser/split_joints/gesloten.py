"""Watertight check (every edge has exactly 2 faces) and Make watertight (voxel remesh on a copy).
Taken over from Click Joints (click_joints/gesloten.py), without the exploded view of the joints."""
import bmesh
import bpy
import numpy as np

from .eigenschappen import eenheid_per_mm

MAX_VOXELS = 3000


def foute_randen(me):
    """Number of edges that do not have exactly 2 faces (open or non-manifold)."""
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


def is_gesloten(bron):
    """(watertight, bad edges) of a mesh or of an object (evaluated, with its modifiers)."""
    if not isinstance(bron, bpy.types.Object):
        fout = foute_randen(bron)
        return fout == 0 and len(bron.polygons) > 0 and volume(bron) > 0, fout
    ob_e = bron.evaluated_get(bpy.context.evaluated_depsgraph_get())
    me = ob_e.to_mesh()
    try:
        fout = foute_randen(me)
        return fout == 0 and len(me.polygons) > 0 and volume(me) > 0, fout
    finally:
        ob_e.to_mesh_clear()


class SPLIT_JOINTS_OT_maak_gesloten(bpy.types.Operator):
    bl_idname = "split_joints.maak_gesloten"
    bl_label = "Make watertight"
    bl_description = "Make a watertight copy with a voxel remesh. The original is kept, hidden"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        bron = context.active_object
        inst = context.scene.split_joints
        stappen = max(bron.dimensions) / (inst.voxel_mm * eenheid_per_mm(context.scene))
        if stappen > MAX_VOXELS:  # a model in mm in a scene in meters would hang Blender here
            self.report({"ERROR"}, f"{bron.name} would need {stappen:.0f} voxels across (limit {MAX_VOXELS}). "
                                   "Check the unit of the scene (Convert to mm) or use a bigger voxel size")
            return {"CANCELLED"}
        dg = context.evaluated_depsgraph_get()
        basis = bpy.data.meshes.new_from_object(bron.evaluated_get(dg))
        tijdelijk = bpy.data.objects.new(bron.name + "_sj_tmp", basis)
        context.scene.collection.objects.link(tijdelijk)
        tijdelijk.matrix_world = bron.matrix_world
        mod = tijdelijk.modifiers.new("sj_remesh", "REMESH")
        mod.mode = "VOXEL"
        mod.voxel_size = inst.voxel_mm * eenheid_per_mm(context.scene)
        dg = context.evaluated_depsgraph_get()
        me = bpy.data.meshes.new_from_object(tijdelijk.evaluated_get(dg))
        bpy.data.objects.remove(tijdelijk)
        bpy.data.meshes.remove(basis)
        me.name = bron.name + "_watertight"
        kopie = bpy.data.objects.new(bron.name + "_watertight", me)
        for c in bron.users_collection:
            c.objects.link(kopie)
        kopie.matrix_world = bron.matrix_world
        kopie["sj_bron"] = bron.name  # keuring K2 (oranje-k5-k6): the own model comes back, not this copy
        ok, fout = is_gesloten(me)
        if not ok:
            bpy.data.objects.remove(kopie)
            bpy.data.meshes.remove(me)
            self.report({"ERROR"}, f"Make watertight failed ({fout} bad edges). Try a larger voxel size.")
            return {"CANCELLED"}
        bron.hide_set(True)
        context.view_layer.update()
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(False)
        kopie.select_set(True)
        context.view_layer.objects.active = kopie
        self.report({"INFO"}, f"Watertight copy {kopie.name} made ({len(me.polygons)} faces)")
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_maak_gesloten,)
