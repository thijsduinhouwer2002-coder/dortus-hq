# Kopersreis Click Joints Pro als mailontvanger (issue #404, Iris 28 nov 2026).
# Volgt de Gumroad-tekst letterlijk: Install from Disk, N-paneel tab Click Joints, Fit test strip eerst,
# eigen figuur zonder rig als STL in mm, 3D-cursor op de huid (Shift + rechtsklik), Shoulder (kogel) en Knee
# (scharnier), export STL zonder en met opslaan. Daarna dezelfde figuur met een eenvoudige rig: Figure from rig.
# Gebruik: blender -b --factory-startup --python kopersreis_pro_iris.py -- <zip> <uitmap>
import bpy, sys, os, glob, math, traceback

import bmesh
from mathutils import Matrix, Vector

args = sys.argv[sys.argv.index("--") + 1:]
ZIP, UIT = args[0], args[1]
os.makedirs(UIT, exist_ok=True)
F = 7.0  # pop van ±30 mm naar ±210 mm, zoals de Gumroad-tekst aanraadt ("about 200 mm tall or more")


def log(*a):
    print("[reis]", *a, flush=True)


def stap(naam, f):
    try:
        r = f()
        log("GOED" if r is not False else "DREMPEL", naam, "" if r in (None, True, False) else r)
        return r
    except Exception as e:
        log("FOUT", naam, repr(e)[:400])
        traceback.print_exc()
        return False


def kies(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    ob.hide_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob


def cursor(p, richting=(0, 0, 1)):
    c = bpy.context.scene.cursor
    c.location = p
    c.rotation_mode = "QUATERNION"
    c.rotation_quaternion = Vector(richting).to_track_quat("Z", "Y")


def delen():
    return [o.name for o in bpy.context.view_layer.objects if o.get("cj_deel")]


def stand(ob=None):
    uit = []
    for o in bpy.context.view_layer.objects:
        if o.get("cj_deel") and o.get("cj_passing"):
            uit.append("%s:%s" % (o.name, o.get("cj_passing")))
    return "delen=%d %s" % (len(delen()), " ".join(uit[:8]))


# Figuur bouwen in een mm-scene en als STL wegschrijven: zo krijgt een maker hem uit ZBrush of een modelsite.
def maak_figuur_stl():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    stukken = []

    def obj(naam, bm):
        me = bpy.data.meshes.new(naam)
        bm.to_mesh(me)
        bm.free()
        o = bpy.data.objects.new(naam, me)
        bpy.context.scene.collection.objects.link(o)
        stukken.append(o)

    def bol(r, c):
        b = bmesh.new()
        bmesh.ops.create_uvsphere(b, u_segments=48, v_segments=24, radius=r * F)
        bmesh.ops.translate(b, verts=b.verts, vec=Vector(c) * F)
        return b

    obj("lijf", bol(7.0, (0, 0, 0)))
    obj("hoofd", bol(4.5, (0, 0, 10.5)))
    for naam, r, lengte, rot, c in (("armen", 2.6, 34.0, Matrix.Rotation(math.pi / 2, 4, "Y"), (0, 0, 3.0)),
                                    ("been_l", 3.0, 18.0, Matrix(), (-3.2, 0, -10.0)),
                                    ("been_r", 3.0, 18.0, Matrix(), (3.2, 0, -10.0))):
        b = bmesh.new()
        bmesh.ops.create_cone(b, cap_ends=True, segments=48, radius1=r * F, radius2=r * F, depth=lengte * F)
        for i in range(1, int(lengte * F / 6)):
            z = -lengte * F / 2 + 6.0 * i + 1.5
            bmesh.ops.bisect_plane(b, geom=b.verts[:] + b.edges[:] + b.faces[:], plane_co=(0, 0, z), plane_no=(0, 0, 1))
        b.transform(Matrix.Translation(Vector(c) * F) @ rot)
        obj(naam, b)
    basis = stukken[0]
    for d in stukken[1:]:
        m = basis.modifiers.new(d.name, "BOOLEAN")
        m.operation = "UNION"
        m.object = d
        m.solver = "EXACT"
        d.hide_set(True)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(basis.evaluated_get(dg))
    for d in stukken:
        bpy.data.objects.remove(d)
    ob = bpy.data.objects.new("my_figure", me)
    bpy.context.scene.collection.objects.link(ob)
    kies(ob)
    pad = os.path.join(UIT, "my_figure.stl")
    bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True, global_scale=1.0, use_scene_unit=False)
    d = ob.dimensions
    return "%s %.0f x %.0f x %.0f (eenheden = mm)" % (os.path.basename(pad), d.x, d.y, d.z)


# 1. Installeren zoals Install from Disk
def installeer():
    r = bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    pt = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    fig = getattr(bpy.types, "CLICK_JOINTS_PT_figuur", None)
    if not (pt and fig and hasattr(bpy.types.Scene, "click_joints")):
        return False
    return "%s tab=%s figuurpaneel=%s" % (r, pt.bl_category, fig.bl_label)


stap("installeren", installeer)
stap("figuur maken (STL in mm, 210 mm hoog)", maak_figuur_stl)


# 2. Nieuw bestand, STL importeren zoals een maker dat doet (File > Import > STL, standaardinstellingen)
def importeer():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    bpy.ops.wm.stl_import(filepath=os.path.join(UIT, "my_figure.stl"))
    ob = bpy.context.view_layer.objects.active
    from importlib import import_module
    mods = [m for m in sys.modules if m.endswith("click_joints.schaal")]
    schaal = sys.modules[mods[0]]
    mm = schaal.maat_mm(ob, bpy.context.scene)
    buiten = not (5 <= mm <= 500)
    return "%s maat=%.4g mm paneelwaarschuwing=%s" % (ob.name, mm, buiten)


stap("STL importeren in een nieuwe scene (meters)", importeer)


def omzetten():
    ob = bpy.context.view_layer.objects.active
    kies(ob)
    r = bpy.ops.click_joints.zet_om_mm()
    ob = bpy.context.view_layer.objects.active
    mods = [m for m in sys.modules if m.endswith("click_joints.schaal")]
    mm = sys.modules[mods[0]].maat_mm(ob, bpy.context.scene)
    us = bpy.context.scene.unit_settings
    return "%s maat=%.4g mm scale_length=%s dim=%s" % (r, mm, us.scale_length, tuple(round(x, 1) for x in ob.dimensions))


stap("Convert to mm", omzetten)
FIG = bpy.context.view_layer.objects.active.name


# 3. Fit test strip eerst (mail en Gumroad: "Print the Fit test strip first")
def strip():
    kies(bpy.data.objects[FIG])
    voor = set(o.name for o in bpy.data.objects)
    r = bpy.ops.click_joints.testkaart(soort="KOGEL")
    nieuw = sorted(set(o.name for o in bpy.data.objects) - voor)
    return "%s nieuw=%s" % (r, nieuw[:6])


stap("Fit test: ball", strip)


def strip_export():
    bpy.context.scene.click_joints.formaat = "STL"
    r = bpy.ops.click_joints.exporteer()
    lijst = bpy.context.scene.get("cj_laatste_export", [])
    return "%s %d bestanden: %s" % (r, len(lijst), [os.path.relpath(p, "/tmp") if p.startswith("/tmp") else p for p in list(lijst)[:6]])


stap("Fit test strip exporteren (niet opgeslagen)", strip_export)


def strip_weg():
    for o in list(bpy.data.objects):
        if o.name != FIG and o.type == "MESH":
            bpy.data.objects.remove(o)
    return "over: %s" % [o.name for o in bpy.data.objects]


stap("strip weghalen, terug naar de figuur", strip_weg)


# 4. Eerste kogelgewricht: Shoulder, cursor op de huid bovenop de linkerarm vlak naast het lijf
def schouder():
    ob = bpy.data.objects[FIG]
    kies(ob)
    # Midden van de arm net naast het lijf, cursor-Z langs de arm (zoals de e2e). Shift + rechtsklik op de huid
    # schuift alleen met een echte 3D-viewport naar het midden (cursor_lid.py); die is er in de achtergrond niet.
    cursor((-8.0 * F, 0, 3.0 * F), (1, 0, 0))
    r = bpy.ops.click_joints.plaats_preset(deel="SHOULDER")
    return "%s %s" % (r, stand())


stap("Shoulder, cursor midden in de arm", schouder)


def knie():
    ob = bpy.data.objects.get(FIG)
    kandidaten = [o for o in bpy.context.view_layer.objects if o.type == "MESH" and (o.name == FIG or o.name.startswith(FIG))]
    # pak het deel dat het linkerbeen bevat
    doel = None
    for o in kandidaten:
        bb = [o.matrix_world @ Vector(c) for c in o.bound_box]
        if min(v.x for v in bb) < -4 * F and min(v.z for v in bb) < -15 * F:
            doel = o
    if doel is None:
        return False
    kies(doel)
    cursor((-3.2 * F, 0, -12.0 * F), (0, 0, 1))  # midden van de knie, cursor-Z langs het been
    r = bpy.ops.click_joints.plaats_preset(deel="KNEE")
    return "%s op %s %s" % (r, doel.name, stand())


stap("Knee, cursor midden in het been", knie)


def export_temp():
    bpy.context.scene.click_joints.formaat = "STL"
    mods = [m for m in sys.modules if m.endswith("click_joints.exporteer")]
    hint = sys.modules[mods[0]].hint(bpy.context.scene)
    r = bpy.ops.click_joints.exporteer()
    lijst = list(bpy.context.scene.get("cj_laatste_export", []))
    return "%s hint=%r %d bestanden, map=%s" % (r, hint, len(lijst), os.path.dirname(lijst[0]) if lijst else None)


stap("Export STL zonder opslaan", export_temp)


def export_opgeslagen():
    pad = os.path.join(UIT, "my_figure.blend")
    bpy.ops.wm.save_as_mainfile(filepath=pad)
    r = bpy.ops.click_joints.exporteer()
    lijst = list(bpy.context.scene.get("cj_laatste_export", []))
    groot = [(os.path.basename(p), os.path.getsize(p)) for p in lijst]
    return "%s %d bestanden naast de .blend: %s" % (r, len(lijst), groot)


stap("Export STL na opslaan", export_opgeslagen)


def stl_maat():
    lijst = list(bpy.context.scene.get("cj_laatste_export", []))
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    uit = []
    for p in lijst:
        bpy.ops.wm.stl_import(filepath=p)
        o = bpy.context.view_layer.objects.active
        uit.append("%s %.1f mm" % (o.name, max(o.dimensions)))
    return "; ".join(uit)


stap("STL terug inlezen: maat in mm", stl_maat)


# 5. Zelfde figuur met een eenvoudige rig (Mixamo-namen), zoals een maker die al riggede
def met_rig():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    bpy.ops.wm.stl_import(filepath=os.path.join(UIT, "my_figure.stl"))
    ob = bpy.context.view_layer.objects.active
    bpy.ops.click_joints.zet_om_mm()
    ob = bpy.context.view_layer.objects.active
    s = 1.0  # na Convert to mm: 1 eenheid = 1 mm
    arm_d = bpy.data.armatures.new("rig")
    arm = bpy.data.objects.new("rig", arm_d)
    bpy.context.scene.collection.objects.link(arm)
    kies(arm)
    bpy.ops.object.mode_set(mode="EDIT")
    eb = arm_d.edit_bones

    def bot(naam, kop, staart, ouder=None):
        b = eb.new(naam)
        b.head = Vector(kop) * F
        b.tail = Vector(staart) * F
        if ouder:
            b.parent = eb[ouder]
            b.use_connect = (b.head - eb[ouder].tail).length < 1e-3
        return b

    bot("mixamorig:Hips", (0, 0, -4), (0, 0, 0))
    bot("mixamorig:Spine", (0, 0, 0), (0, 0, 3), "mixamorig:Hips")
    bot("mixamorig:Neck", (0, 0, 6), (0, 0, 8), "mixamorig:Spine")
    bot("mixamorig:Head", (0, 0, 8), (0, 0, 14), "mixamorig:Neck")
    for kant, sx in (("Left", -1), ("Right", 1)):
        bot(f"mixamorig:{kant}Arm", (sx * 6, 0, 3), (sx * 11, 0, 3), "mixamorig:Spine")
        bot(f"mixamorig:{kant}ForeArm", (sx * 11, 0, 3), (sx * 17, 0, 3), f"mixamorig:{kant}Arm")
        bot(f"mixamorig:{kant}UpLeg", (sx * 3.2, 0, -4), (sx * 3.2, 0, -11), "mixamorig:Hips")
        bot(f"mixamorig:{kant}Leg", (sx * 3.2, 0, -11), (sx * 3.2, 0, -19), f"mixamorig:{kant}UpLeg")
    bpy.ops.object.mode_set(mode="OBJECT")
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    ob.select_set(True)
    arm.select_set(True)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.parent_set(type="ARMATURE_AUTO")
    kies(ob)
    r = bpy.ops.click_joints.figuur_uit_rig(meer=False)
    return "%s %s" % (r, stand())


stap("Figure from rig (Mixamo-namen, 210 mm)", met_rig)


def rig_export():
    pad = os.path.join(UIT, "my_figure_rig.blend")
    bpy.ops.wm.save_as_mainfile(filepath=pad)
    bpy.context.scene.click_joints.formaat = "STL"
    r = bpy.ops.click_joints.exporteer()
    lijst = list(bpy.context.scene.get("cj_laatste_export", []))
    return "%s %d bestanden" % (r, len(lijst))


stap("Export STL na Figure from rig", rig_export)
log("KLAAR")
