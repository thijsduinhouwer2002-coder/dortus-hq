"""Operator split_joints.exporteer: every piece and every pin plate as STL or 3MF, in millimeters.
Same way of writing as Click Joints (exporteer.py and drie_mf.py)."""
import json
import os
import tempfile

import bpy
import numpy as np
from mathutils import Matrix

from . import drie_mf, plat
from .eigenschappen import bed, eenheid_per_mm
from .uit_elkaar import echte_plek

STANDAARD = "//click_cuts/"


def exportmap(scene):
    pad = scene.split_joints.exportmap or STANDAARD
    if pad.startswith("//") and not bpy.data.filepath:
        return os.path.join(tempfile.gettempdir(), "click_cuts")
    return bpy.path.abspath(pad)


def niet_opgeslagen(scene, blend=None):
    """True when Export parts would write to the temp folder of the system (kopersreis #387: on Windows a
    hidden folder, and the main panel did not say so)."""
    pad = scene.split_joints.exportmap or STANDAARD
    return pad.startswith("//") and not (bpy.data.filepath if blend is None else blend)


def hint(scene):
    if scene.split_joints.exportmap:
        return None
    return "Saves next to the .blend" if bpy.data.filepath else "Saves to a temporary folder"


def bestandsnaam(ob):
    if ob.get("sj_stuk"):
        return f"piece_{int(ob['sj_stuk']):02d}"
    return f"pins_{ob['sj_pen_d']:g}mm_x{int(ob['sj_pennen'])}".replace(".", "_")


def onderdelen(context):
    lijst = [o for o in context.view_layer.objects if o is not None and (o.get("sj_stuk") or o.get("sj_pennen"))]
    return sorted(lijst, key=lambda o: (0, o["sj_stuk"]) if o.get("sj_stuk") else (1, o.name))


def snij_punten(ob):
    """(point mm, axis) of every pin hole and number of a piece: they lie in its cut faces (plat.is_snijvlak).
    Free cuts store their normal "n", the straight cuts the axis "as" (0, 1, 2)."""
    uit = []
    for sleutel in ("sj_gaten", "sj_labels"):
        try:
            lijst = json.loads(ob.get(sleutel) or "[]")
        except ValueError:
            continue
        for g in lijst:
            if "n" in g:
                a = [float(x) for x in g["n"]]
            elif g.get("as") in (0, 1, 2):
                a = [1.0 if i == g["as"] else 0.0 for i in range(3)]
            else:
                continue
            uit.append(([float(x) for x in g["p"]], a))
    return uit


def plat_matrix(ob, u, bed_mm):
    """World matrix that lays piece ob flat (plat.kies_stand) with its lowest point on z = 0, x and y of the
    middle kept. None if no flat face fits the bed: then only the height changes (see stand)."""
    deps = bpy.context.evaluated_depsgraph_get()
    oe = ob.evaluated_get(deps)
    me = oe.to_mesh()
    try:
        m = np.array(oe.matrix_world)
        n = len(me.vertices)
        co = np.empty(n * 3)
        me.vertices.foreach_get("co", co)
        co = co.reshape(-1, 3) @ m[:3, :3].T + m[:3, 3]
        k = len(me.polygons)
        nrm, mid, opp = np.empty(k * 3), np.empty(k * 3), np.empty(k)
        me.polygons.foreach_get("normal", nrm)
        me.polygons.foreach_get("center", mid)
        me.polygons.foreach_get("area", opp)
    finally:
        oe.to_mesh_clear()
    inv = np.linalg.inv(m[:3, :3]).T  # normals go with the inverse transpose
    nrm = nrm.reshape(-1, 3) @ inv.T
    nrm /= np.maximum(np.linalg.norm(nrm, axis=1), 1e-12)[:, None]  # unit length again after a scale
    mid = mid.reshape(-1, 3) @ m[:3, :3].T + m[:3, 3]
    schaal = abs(np.linalg.det(m[:3, :3])) ** (1.0 / 3.0)
    opp = opp * schaal * schaal / (u * u)
    snij = snij_punten(ob)
    r, _a, rang, ob["sj_plat_snijvlak"] = plat.kies_stand(nrm, mid / u, opp, co / u, bed_mm, snij)
    if r is None:
        r = np.eye(3)
    w = co @ r.T
    midden = (co.min(axis=0) + co.max(axis=0)) / 2.0
    t = np.array([midden[0] - (w[:, 0].min() + w[:, 0].max()) / 2.0,
                  midden[1] - (w[:, 1].min() + w[:, 1].max()) / 2.0, -w[:, 2].min()])
    d = Matrix.Identity(4)
    for i in range(3):
        for j in range(3):
            d[i][j] = r[i, j]
        d[i][3] = t[i]
    return d @ ob.matrix_world, rang


class SPLIT_JOINTS_OT_exporteer(bpy.types.Operator):
    bl_idname = "split_joints.exporteer"
    bl_label = "Export"
    bl_description = "Write every piece and the pins as STL or 3MF files in millimeters"

    def execute(self, context):
        formaat = context.scene.split_joints.formaat
        if formaat == "STL" and "stl_export" not in dir(bpy.ops.wm):
            self.report({"ERROR"}, "This Blender has no STL export (needs 4.2 or newer)")
            return {"CANCELLED"}
        lijst = onderdelen(context)
        if not lijst:
            self.report({"WARNING"}, "Split the model first")
            return {"CANCELLED"}
        map_ = exportmap(context.scene)
        os.makedirs(map_, exist_ok=True)
        schaal = 1.0 / eenheid_per_mm(context.scene)
        actief = context.view_layer.objects.active
        gekozen = [o for o in context.view_layer.objects if o is not None and o.select_get()]
        geschreven = []
        leg_plat = context.scene.split_joints.plat
        bed_mm = bed(context.scene)
        u = eenheid_per_mm(context.scene)
        with echte_plek([o for o in lijst if o.get("sj_stuk")]):
            for ob in lijst:
                oud = ob.matrix_basis.copy()
                try:
                    if leg_plat and ob.get("sj_stuk"):  # pin plates are already flat on the bed
                        ob.matrix_world, ob["sj_plat_rang"] = plat_matrix(ob, u, bed_mm)
                        context.view_layer.update()
                    pad = os.path.join(map_, bestandsnaam(ob) + (".3mf" if formaat == "3MF" else ".stl"))
                    if formaat == "3MF":
                        ob["sj_3mf_driehoeken"] = drie_mf.schrijf(ob, pad, schaal)
                    else:
                        for o in context.view_layer.objects:
                            if o is not None:
                                o.select_set(False)
                        ob.select_set(True)
                        context.view_layer.objects.active = ob
                        bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True, global_scale=schaal,
                                              use_scene_unit=False, ascii_format=False, apply_modifiers=True)
                finally:
                    if ob.matrix_basis != oud:  # the piece stays where it was in the scene
                        ob.matrix_basis = oud
                        context.view_layer.update()
                ob["sj_bestand"] = pad
                geschreven.append(pad)
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(o in gekozen)
        context.view_layer.objects.active = actief
        context.scene["sj_laatste_export"] = geschreven
        if niet_opgeslagen(context.scene):  # #387: say it where people look, not only in More settings
            self.report({"WARNING"}, f"{len(geschreven)} {formaat} files in a temporary folder: {map_}. "
                                     "Save your .blend (Ctrl+S) and export again to get them next to it")
        else:
            self.report({"INFO"}, f"{len(geschreven)} {formaat} files in {map_}")
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_exporteer,)
