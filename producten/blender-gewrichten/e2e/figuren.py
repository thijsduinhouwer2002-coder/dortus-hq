"""Testfiguren voor de e2e-test: meestal in een scene waarin 1 Blender-eenheid 1 mm is, één ronde in meters."""
import math

import bmesh
import bpy
from mathutils import Matrix, Vector


def mm_scene():
    us = bpy.context.scene.unit_settings
    us.system = "METRIC"
    us.scale_length = 0.001
    us.length_unit = "MILLIMETERS"


def meter_scene():
    """Standaardscene van Blender: 1 eenheid = 1 m, eenheidschaal 1,0, lengte in meters."""
    us = bpy.context.scene.unit_settings
    us.system = "METRIC"
    us.scale_length = 1.0
    us.length_unit = "METERS"


def _object(naam, bm):
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def arm(naam="arm", u=512, v=256, schaal=1.0):
    """Ellipsoïde arm 40 x 10 x 10 eenheden met lichte sculptgolven (512x256: ±261K driehoeken).
    In de mm-scene is dat 40 x 10 x 10 mm; met schaal 0,002 in de meterscene 0,08 x 0,02 x 0,02 m."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=u, v_segments=v, radius=1.0)
    for p in bm.verts:
        x, y, z = p.co
        golf = 1.0 + 0.03 * math.sin(9 * x) * math.cos(7 * math.atan2(z, y))
        p.co = Vector((x * 20.0, y * 5.0 * golf, z * 5.0 * golf)) * schaal
    return _object(naam, bm)


def open_arm(naam="open_arm"):
    """Arm met één weggehaald vlak in het midden: een klein gat."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=256, v_segments=128, radius=1.0)
    for p in bm.verts:
        p.co = Vector((p.co.x * 20.0, p.co.y * 5.0, p.co.z * 5.0))
    bm.faces.ensure_lookup_table()
    doel = min(bm.faces, key=lambda f: (f.calc_center_median() - Vector((0, 0, 5))).length)
    bmesh.ops.delete(bm, geom=[doel], context="FACES_ONLY")
    return _object(naam, bm)


def _bol(r, c, seg=48):
    tmp = bmesh.new()
    bmesh.ops.create_uvsphere(tmp, u_segments=seg, v_segments=seg // 2, radius=r)
    bmesh.ops.translate(tmp, verts=tmp.verts, vec=c)
    return tmp


def pop(solver, arm_r=2.6):
    """Eenvoudige pop: lijf, hoofd, armen en benen (bollen en cilinders), samengevoegd tot één mesh.
    arm_r: straal van de armen in mm (standaard 2,6; de schermafbeeldingen gebruiken dikkere armen)."""
    delen = []

    def vorm(naam, bm):
        delen.append(_object(naam, bm))

    vorm("lijf", _bol(7.0, (0, 0, 0)))
    vorm("hoofd", _bol(4.5, (0, 0, 10.5)))
    for naam, r, lengte, rot, c in (("armen", arm_r, 34.0, Matrix.Rotation(math.pi / 2, 4, "Y"), (0, 0, 3.0)),
                                    ("been_l", 3.0, 18.0, Matrix(), (-3.2, 0, -10.0)),
                                    ("been_r", 3.0, 18.0, Matrix(), (3.2, 0, -10.0))):
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, segments=48, radius1=r, radius2=r, depth=lengte)
        for i in range(1, int(lengte / 2)):  # lusjes om de 2 mm, zodat de passingring smal blijft op plaatje 2
            z = -lengte / 2 + 2.0 * i + 0.5  # niet precies op de plek van een snede in de tests (x = 11, z = -14)
            geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
            bmesh.ops.bisect_plane(bm, geom=geom, plane_co=(0, 0, z), plane_no=(0, 0, 1))
        bm.transform(Matrix.Translation(c) @ rot)
        vorm(naam, bm)
    basis = delen[0]
    for d in delen[1:]:
        m = basis.modifiers.new(d.name, "BOOLEAN")
        m.operation = "UNION"
        m.object = d
        m.solver = solver
        d.hide_set(True)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(basis.evaluated_get(dg))
    for d in delen:
        bpy.data.objects.remove(d)
    ob = bpy.data.objects.new("pop", me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def staaf(naam, straal, lengte=40.0):
    """Rechte staaf langs X met een vaste straal: de wanddikte rond de kom is dan precies te kiezen."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=128, radius1=straal, radius2=straal, depth=lengte)
    bm.transform(Matrix.Rotation(math.pi / 2, 4, "Y"))
    return _object(naam, bm)


def zet_cursor(punt, as_richting):
    """3D-cursor op het punt, met de Z-as van de cursor langs de gegeven richting."""
    c = bpy.context.scene.cursor
    c.location = punt
    c.rotation_mode = "QUATERNION"
    c.rotation_quaternion = Vector(as_richting).to_track_quat("Z", "Y")


def maak_actief(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        if o is not None:
            o.select_set(False)
    ob.hide_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob
