"""Plan cuts: cut planes as objects you can move along their axis (G), plus the model in millimeters.

A cut is a flat object in the collection "Split Joints cuts" with sj_as (0, 1, 2). Its position along
that axis (location) is the cut; the other axes are locked, so dragging it only slides the cut."""
import bpy
import numpy as np
from mathutils import Vector

from . import plan
from .eigenschappen import bed, eenheid_per_mm

COLLECTIE = "Split Joints cuts"
ASNAAM = "XYZ"


def mesh_mm(ob, scene):
    """(points N x 3, triangles M x 3) of the evaluated mesh in world coordinates, in mm."""
    u = eenheid_per_mm(scene)
    ev = ob.evaluated_get(bpy.context.evaluated_depsgraph_get())
    me = ev.to_mesh()
    try:
        me.calc_loop_triangles()
        co = np.empty(len(me.vertices) * 3)
        me.vertices.foreach_get("co", co)
        tri = np.empty(len(me.loop_triangles) * 3, dtype=np.int64)
        me.loop_triangles.foreach_get("vertices", tri)
    finally:
        ev.to_mesh_clear()
    m = np.array(ob.matrix_world)
    p = co.reshape(-1, 3) @ m[:3, :3].T + m[:3, 3]
    return p / u, tri.reshape(-1, 3)


def wereld_kader_mm(ob, scene):
    """(lo, hi) of the object's bounding box in world coordinates, in mm."""
    u = eenheid_per_mm(scene)
    hoeken = np.array([tuple(ob.matrix_world @ Vector(c)) for c in ob.bound_box]) / u
    return tuple(hoeken.min(axis=0)), tuple(hoeken.max(axis=0))


def collectie(scene, maak=True):
    col = bpy.data.collections.get(COLLECTIE)
    if col is None and maak:
        col = bpy.data.collections.new(COLLECTIE)
        scene.collection.children.link(col)
    return col


def snede_objecten(scene):
    col = collectie(scene, maak=False)
    if col is None:
        return []
    return sorted((o for o in col.objects if "sj_as" in o), key=lambda o: (o["sj_as"], o.location[o["sj_as"]]))


def lees(scene):
    """All cuts as (axis, position mm)."""
    u = eenheid_per_mm(scene)
    return [(int(o["sj_as"]), o.location[int(o["sj_as"])] / u) for o in snede_objecten(scene)]


def maak_snede(scene, as_, pos_mm, lo, hi):
    """Adds one cut plane, a bit larger than the model."""
    u = eenheid_per_mm(scene)
    a, b = (as_ + 1) % 3, (as_ + 2) % 3
    rand = 0.08 * max(hi[i] - lo[i] for i in range(3)) + 5.0
    hoeken = []
    for da, db in ((0, 0), (1, 0), (1, 1), (0, 1)):
        p = [0.0, 0.0, 0.0]
        p[a] = (lo[a] - rand if da == 0 else hi[a] + rand) * u
        p[b] = (lo[b] - rand if db == 0 else hi[b] + rand) * u
        hoeken.append(p)
    naam = f"Cut {ASNAAM[as_]}"
    me = bpy.data.meshes.new(naam)
    me.from_pydata(hoeken, [], [(0, 1, 2, 3)])
    ob = bpy.data.objects.new(naam, me)
    collectie(scene).objects.link(ob)
    ob.location[as_] = pos_mm * u
    ob["sj_as"] = as_
    ob.lock_location = [i != as_ for i in range(3)]
    ob.lock_rotation = (True, True, True)
    ob.lock_scale = (True, True, True)
    ob.display_type = "WIRE"
    ob.show_in_front = True
    ob.hide_render = True
    ob.color = (1.0, 0.55, 0.1, 1.0)
    return ob


def wis(scene):
    for o in snede_objecten(scene):
        me = o.data
        bpy.data.objects.remove(o)
        if me and me.users == 0:
            bpy.data.meshes.remove(me)


def model(context):
    """The model to split: the one the cuts belong to, else the active mesh."""
    naam = context.scene.split_joints.bron
    ob = bpy.data.objects.get(naam) if naam else None
    if ob is None or ob.type != "MESH":
        ob = context.active_object if context.active_object and context.active_object.type == "MESH" else None
    return ob


def stand(context):
    """Live check for the panel: (cells, cells that fit, largest cell mm) with the current cuts, or None."""
    ob = model(context)
    if ob is None:
        return None
    lo, hi = wereld_kader_mm(ob, context.scene)
    lijst, _ = plan.cellen(lo, hi, lees(context.scene))
    b = bed(context.scene)
    from .printers import past
    maten = [tuple(y - x for x, y in zip(mn, mx)) for _ijk, mn, mx in lijst]
    goed = sum(1 for m in maten if past(m, b))
    return len(maten), goed, max(maten, key=lambda m: sorted(m, reverse=True)) if maten else (0, 0, 0)


class SPLIT_JOINTS_OT_plan(bpy.types.Operator):
    bl_idname = "split_joints.plan"
    bl_label = "Plan cuts"
    bl_description = "Place cut planes so every piece fits on the bed, with as few pieces as possible"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH" \
            and "sj_as" not in context.active_object

    def execute(self, context):
        ob = context.active_object
        scene = context.scene
        punten, _tri = mesh_mm(ob, scene)
        b = bed(scene)
        uit = plan.maak(punten, b)
        if uit is None:
            self.report({"ERROR"}, "No plan found: the model has no points or is far too large")
            return {"CANCELLED"}
        wis(scene)
        lo, hi = uit["lo"], uit["hi"]
        for as_, pos in uit["snedes"]:
            maak_snede(scene, as_, pos, lo, hi)
        scene.split_joints.bron = ob.name
        scene["sj_plan"] = {"stukken": uit["stukken"], "n": list(uit["n"]), "cel": list(uit["cel"])}
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(False)
        ob.select_set(True)
        context.view_layer.objects.active = ob
        self.report({"INFO"}, f"{uit['stukken']} pieces, {len(uit['snedes'])} cuts. Move a cut with G if you like.")
        return {"FINISHED"}


class SPLIT_JOINTS_OT_snede_erbij(bpy.types.Operator):
    bl_idname = "split_joints.snede_erbij"
    bl_label = "Add cut"
    bl_description = "Add a cut plane through the middle of the model along this axis"
    bl_options = {"REGISTER", "UNDO"}
    as_: bpy.props.IntProperty(default=2, min=0, max=2)

    def execute(self, context):
        ob = model(context)
        if ob is None:
            self.report({"WARNING"}, "Select the model first")
            return {"CANCELLED"}
        lo, hi = wereld_kader_mm(ob, context.scene)
        context.scene.split_joints.bron = ob.name
        maak_snede(context.scene, self.as_, (lo[self.as_] + hi[self.as_]) / 2.0, lo, hi)
        return {"FINISHED"}


class SPLIT_JOINTS_OT_snede_weg(bpy.types.Operator):
    bl_idname = "split_joints.snede_weg"
    bl_label = "Remove cut"
    bl_description = "Remove this cut plane"
    bl_options = {"REGISTER", "UNDO"}
    naam: bpy.props.StringProperty()

    def execute(self, context):
        ob = bpy.data.objects.get(self.naam)
        if ob is None or "sj_as" not in ob:
            return {"CANCELLED"}
        me = ob.data
        bpy.data.objects.remove(ob)
        if me and me.users == 0:
            bpy.data.meshes.remove(me)
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_plan, SPLIT_JOINTS_OT_snede_erbij, SPLIT_JOINTS_OT_snede_weg)
