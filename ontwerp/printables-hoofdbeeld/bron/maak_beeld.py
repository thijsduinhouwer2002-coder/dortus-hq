"""Printables-hoofdbeeld van de gratis Click Joints (issue #297, Beeldmaker, 27 nov 2026).

Figuur: Blender Human Base Meshes v1.4.1, object GEO-body_male_stylized met zijn twee ogen (CC0 1.0, Blender Studio), hoogte PR_HOOGTE (standaard 180 mm, beeld r1: 200 mm).
De gewrichten maakt de echte knop Place joint van de gratis add-on (click_joints_direct-0.1.2.zip), Ball, Auto-maat,
as langs de 3D-cursor. Niets is nagetekend; alleen de afstand van Exploded view is voor het beeld groter gezet
(alleen weergave, de STL heeft de echte plek). Ook de STL's van de delen worden weggeschreven (Export van de add-on).

    blender -b --factory-startup --python maak_beeld.py -- <bundle.blend> <add-on-zip> <uitmap> [samples] [schaal%]
"""
import json, math, os, sys
import bpy
from mathutils import Matrix, Vector

a = sys.argv[sys.argv.index("--") + 1:]
BRON, ZIP, UIT = a[0], a[1], a[2]
SAMPLES = int(a[3]) if len(a) > 3 else 64
SCHAAL = int(a[4]) if len(a) > 4 else 100
E = os.environ.get
os.makedirs(UIT, exist_ok=True)
log = lambda t: print(f"[printables] {t}", flush=True)

bpy.ops.wm.open_mainfile(filepath=BRON)
ob = bpy.data.objects["GEO-body_male_stylized"]
ogen = [bpy.data.objects[n] for n in ("GEO-body_male_stylized.eye.L", "GEO-body_male_stylized.eye.R")]
for o in list(bpy.data.objects):
    if o is not ob and o not in ogen:
        bpy.data.objects.remove(o)
for c in list(bpy.data.collections):
    bpy.data.collections.remove(c)
sc = bpy.context.scene
if ob.name not in sc.collection.objects:
    sc.collection.objects.link(ob)
ob.hide_set(False); ob.hide_viewport = False; ob.hide_render = False
ob.name = "Figure"; ob.data.name = "Figure"
OOG = []  # (midden, straal) in wereldmaat vóór het schalen
for o in [ob] + ogen:
    for m in list(o.modifiers):
        o.modifiers.remove(m)
    o.data.materials.clear()
    if o.name not in sc.collection.objects:
        sc.collection.objects.link(o)
for o in ogen:
    pts = [o.matrix_world @ v.co for v in o.data.vertices]
    c = sum(pts, Vector()) / len(pts)
    OOG.append((c, max((p - c).length for p in pts)))
if E("PR_OGEN", "1") == "1":
    ob.data.materials.append(bpy.data.materials.new("lijf"))
    for o in ogen:
        o.data.materials.append(bpy.data.materials.new("oog"))
    for o in bpy.data.objects:
        o.select_set(o is ob or o in ogen)
    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.join()  # ogen zijn gesloten bollen: het figuur blijft gesloten
else:
    for o in ogen:
        bpy.data.objects.remove(o)
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
# 1 eenheid = 1 mm, figuur PR_HOOGTE mm hoog, midden op x=0, voeten op z=0
sc.unit_settings.system = "METRIC"; sc.unit_settings.scale_length = 0.001; sc.unit_settings.length_unit = "MILLIMETERS"
V = [ob.matrix_world @ v.co for v in ob.data.vertices]
lo = Vector([min(v[i] for v in V) for i in range(3)]); hi = Vector([max(v[i] for v in V) for i in range(3)])
HOOG = float(E("PR_HOOGTE", "180"))
S = HOOG / 180.0  # maten hieronder staan voor 180 mm
f = HOOG / (hi.z - lo.z)
mid = Vector(((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, lo.z))
T = Matrix.Scale(f, 4) @ Matrix.Translation(-mid)
ob.matrix_world = T @ ob.matrix_world
OOG = [(T @ c, r * f) for c, r in OOG]
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
import bmesh as _bm
_b = _bm.new(); _b.from_mesh(ob.data)
_vol0 = _b.calc_volume(signed=True)
_bm.ops.recalc_face_normals(_b, faces=_b.faces[:])  # zoals Recalculate Outside in Blender
log(f"normalen: volume voor {_vol0:.0f}, na {_b.calc_volume(signed=True):.0f} mm3")
_b.to_mesh(ob.data); _b.free()
V = [v.co.copy() for v in ob.data.vertices]
log(f"figuur {len(V)} punten, hoogte {max(v.z for v in V) - min(v.z for v in V):.1f} mm")

bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
inst = sc.click_joints
inst.soort = "KOGEL"; inst.as_bron = "CURSOR"; inst.kogel_auto = True; inst.uit_elkaar = True


def centrum(zone):
    """Midden van de punten in een doos (xmin, xmax, zmin, zmax)."""
    p = [v for v in V if zone[0] <= v.x <= zone[1] and zone[2] <= v.z <= zone[3]]
    return sum(p, Vector()) / len(p)


def plaats(doel, punt, as_, naam, mm=0.0):
    if mm > 0:
        inst.kogel_auto = False; inst.kogel_mm = mm
    else:
        inst.kogel_auto = True
    as_ = as_.normalized()
    rot = as_.to_track_quat("Z", "Y").to_matrix().to_4x4()
    sc.cursor.matrix = Matrix.Translation(punt) @ rot
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = doel
    doel.select_set(True)
    voor = set(o.name for o in bpy.data.objects)
    r = bpy.ops.click_joints.plaats()
    nieuw = [bpy.data.objects[n] for n in set(o.name for o in bpy.data.objects) - voor if n in bpy.data.objects]
    delen = {o.get("cj_deel"): o for o in nieuw if o.get("cj_deel")}
    log(f"{naam}: {r} delen {[(k, v.name) for k, v in delen.items()]} passing "
        f"{[v.get('cj_passing') for v in delen.values()]} kogel {2 * delen['A']['cj_kogel_r']:.2f} mm" if delen else f"{naam}: {r} GEEN DELEN")
    return delen


uitslag = {}
cj = lambda o: {k2: (list(v) if hasattr(v, "__len__") and not isinstance(v, str) else v) for k2, v in o.items() if k2.startswith("cj_")}
# Gewrichten langs een lid: punt = midden van de doorsnede op hoogte z (x tussen x0 en x1, maten voor 180 mm),
# as langs het lid naar beneden ("neer"): deel A = lijf met de kogel, deel B = het losse stuk met de kom.
GEW = json.loads(E("PR_GEWRICHTEN", '[{"naam": "rechterknie", "x0": 1, "x1": 30, "z": 61, "richting": "neer"},'
                                    ' {"naam": "linkerknie", "x0": -30, "x1": -1, "z": 61, "richting": "neer"}]'))
lijf = ob; losse = []
for g in GEW:
    z = g["z"] * S
    c = lambda zz: centrum((g["x0"] * S, g["x1"] * S, zz - 1.5, zz + 1.5))
    p, q = c(z), c(z - 4 * S)
    as_ = (q - p) if g["richting"] == "neer" else (p - q)
    d = plaats(lijf, p, as_, g["naam"], float(g.get("mm", 0)))
    if not d:
        continue
    lijf = d["A"]; losse.append(d["B"])
    uitslag[g["naam"]] = cj(d["A"])
romp = lijf; benen = None; kop = None

# Losse stukjes: bij een snede in het been houdt deel A kleine losse stukjes van de tenen (die steken buiten het lid
# uit; dezelfde tenen zitten ook heel in deel B). Voor beeld en STL halen we schillen onder 2% van deel A weg (gemeld).
import bmesh
def losse_weg(o, deel=0.02):
    bm = bmesh.new(); bm.from_mesh(o.data); bm.verts.ensure_lookup_table()
    gezien, schillen = set(), []
    for v in bm.verts:
        if v.index in gezien:
            continue
        st, c = [v], []
        gezien.add(v.index)
        while st:
            x = st.pop(); c.append(x)
            for e in x.link_edges:
                y = e.other_vert(x)
                if y.index not in gezien:
                    gezien.add(y.index); st.append(y)
        schillen.append(c)
    groot = max(len(c) for c in schillen)
    weg = [v for c in schillen if len(c) < deel * groot and not any((o.matrix_world @ v.co - oc).length < r * 1.2
                                                                       for oc, r in OOG for v in c[:1])
           for v in c]
    n = sum(1 for c in schillen if len(c) < deel * groot) - (len(OOG) if E("PR_OGEN", "1") == "1" and o is romp else 0)
    if weg:
        bmesh.ops.delete(bm, geom=weg, context="VERTS")
    bm.to_mesh(o.data); bm.free(); o.data.update()
    log(f"losse stukjes uit {o.name}: {len(weg)} punten weg ({n} schillen, ogen blijven)")
    return n
uitslag["losse_stukjes_weg"] = losse_weg(romp)

# Export van de add-on (STL in mm)
inst.exportmap = os.path.join(UIT, "stl") + os.sep
os.makedirs(inst.exportmap, exist_ok=True)
try:
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = romp
    romp.select_set(True)
    log(f"export: {bpy.ops.click_joints.exporteer()} {sorted(os.listdir(inst.exportmap))}")
except Exception as e:
    log(f"export FOUT {e}")


# Exploded view: afstand voor het beeld groter (alleen weergave). Het lijf gaat omhoog, de onderbenen blijven op de vloer.
VER = float(E("PR_VER", "2.2"))
op = 0.0
for d in losse:
    v = Vector(d["cj_as"]).normalized() * VER * 2 * float(d["cj_kogel_r"])
    op = max(op, -v.z)
    d.delta_location = Vector((v.x, v.y, 0.0))
romp.delta_location = Vector((0, 0, op))

# ---------- studio ----------
def mat(naam, hexkleur, ruw=0.42, glans=0.0):
    m = bpy.data.materials.new(naam); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    c = [int(hexkleur[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c]
    b.inputs["Base Color"].default_value = (*c, 1)
    b.inputs["Roughness"].default_value = ruw
    if "Coat Weight" in b.inputs:
        b.inputs["Coat Weight"].default_value = glans
    return m


K_ROMP = E("PR_KLEUR_ROMP", "F2A541"); K_DEEL = E("PR_KLEUR_DEEL", "2F9C95")
m_romp = mat("romp", K_ROMP, 0.38, 0.15); m_deel = mat("deel", K_DEEL, 0.38, 0.15)
rest = [o for o in bpy.data.objects if o.type == "MESH" and o.visible_get() and o is not romp and o not in losse]
m_oog = mat("oog", E("PR_KLEUR_OOG", "2A2230"), 0.2, 0.8)
for o, m in [(romp, m_romp)] + [(o, m_deel) for o in losse] + [(o, m_romp) for o in rest]:
    if o is None:
        continue
    for i, slot in enumerate(o.data.materials):
        o.data.materials[i] = m_oog if (slot and slot.name.startswith("oog")) else m
    if len(o.data.materials) == 0:
        o.data.materials.append(m)
    for p in o.data.polygons:
        p.use_smooth = True
    log(f"kleur {o.name} {m.name}")
for o in bpy.data.objects:
    if o.type == "MESH" and not o.visible_get():
        o.hide_render = True
# alles wat de add-on tekent (waaier, gradenboog) niet in de render
for o in bpy.data.objects:
    if o.type != "MESH" or o.name.startswith("cj_") or "range" in o.name.lower():
        if o.type != "MESH":
            o.hide_render = True

bpy.ops.mesh.primitive_plane_add(size=4000, location=(0, 0, 0))
vloer = bpy.context.active_object
bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="DESELECT"); bpy.ops.object.mode_set(mode="OBJECT")
# hoek naar achtergrond: buig de achterkant omhoog (cyclorama)
bpy.ops.object.mode_set(mode="OBJECT")
vloer.data.materials.append(mat("vloer", E("PR_KLEUR_VLOER", "EFEAE2"), 0.9))
ach = bpy.data.objects.new("achter", bpy.data.meshes.new("achter"))
import bmesh
bm = bmesh.new()
R = 260.0; N = 24
rij = []
for i in range(N + 1):
    h = math.pi / 2 * i / N
    y = 160 + R * math.sin(h); z = R - R * math.cos(h)
    rij.append((y, z))
vs = [[bm.verts.new((x, y, z)) for (y, z) in rij] for x in (-2000, 2000)]
for i in range(N):
    bm.faces.new((vs[0][i], vs[1][i], vs[1][i + 1], vs[0][i + 1]))
top = [bm.verts.new((x, 160 + R, 2000)) for x in (-2000, 2000)]
bm.faces.new((vs[0][N], vs[1][N], top[1], top[0]))
bm.to_mesh(ach.data); bm.free()
sc.collection.objects.link(ach)
ach.data.materials.append(vloer.data.materials[0])
for p in ach.data.polygons:
    p.use_smooth = True

def licht(naam, soort, plek, energie, maat=100, doel=Vector((0, 0, 80)), kleur=(1, 1, 1)):
    l = bpy.data.lights.new(naam, soort); l.energy = energie; l.color = kleur
    if soort == "AREA":
        l.size = maat
    o = bpy.data.objects.new(naam, l); sc.collection.objects.link(o)
    o.location = plek
    o.rotation_euler = (Vector(doel) - Vector(plek)).to_track_quat("-Z", "Y").to_euler()
    return o

L = float(E("PR_LICHT", "1.0"))
licht("key", "AREA", (-260, -300, 330), 2.2e6 * L, 220, kleur=(1, 0.97, 0.92))
licht("vul", "AREA", (320, -220, 160), 0.7e6 * L, 260, kleur=(0.92, 0.96, 1))
licht("rand", "AREA", (120, 260, 300), 1.3e6 * L, 160)
sc.world = bpy.data.worlds.new("w"); sc.world.use_nodes = True
sc.world.node_tree.nodes["Background"].inputs[0].default_value = (0.9, 0.9, 0.92, 1)
sc.world.node_tree.nodes["Background"].inputs[1].default_value = 0.25

cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam)
sc.camera = cam
cam.data.lens = float(E("PR_LENS", "70"))
DRAAI = math.radians(float(E("PR_DRAAI", "-24"))); KANTEL = math.radians(float(E("PR_KANTEL", "6")))
AF = float(E("PR_AFSTAND", "620"))
doel = Vector([float(x) for x in E("PR_DOEL", "6,0,92").split(",")])
cam.location = doel + Vector((math.sin(DRAAI) * math.cos(KANTEL), -math.cos(DRAAI) * math.cos(KANTEL), math.sin(KANTEL))) * AF
cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
cam.data.shift_x = float(E("PR_SHIFT_X", "0")); cam.data.shift_y = float(E("PR_SHIFT_Y", "0"))
cam.data.clip_start = 1; cam.data.clip_end = 10000

sc.render.engine = "CYCLES"; sc.cycles.samples = SAMPLES; sc.cycles.use_denoising = True
sc.cycles.device = "CPU"
sc.render.resolution_x = 2000; sc.render.resolution_y = 1500; sc.render.resolution_percentage = SCHAAL
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = E("PR_LOOK", "AgX - Medium High Contrast")
sc.render.filepath = os.path.join(UIT, E("PR_NAAM", "beeld") + ".png")
sc.render.image_settings.file_format = "PNG"

# 2D-plek van de gewrichten voor labels
from bpy_extras.object_utils import world_to_camera_view
bpy.context.view_layer.update()
def pix(p):
    c = world_to_camera_view(sc, cam, Vector(p))
    return [round(c.x * 2000), round((1 - c.y) * 1500)]
uitslag["pix"] = {g["naam"]: pix(Vector(uitslag[g["naam"]]["cj_centrum"]) + romp.delta_location) for g in GEW if g["naam"] in uitslag}
json.dump(uitslag, open(os.path.join(UIT, E("PR_NAAM", "beeld") + ".json"), "w"), indent=1, default=str)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(UIT, "scene.blend"))
bpy.ops.render.render(write_still=True)
log("klaar " + sc.render.filepath)
if E("PR_INZET"):
    g = E("PR_INZET")
    c = Vector(uitslag[g]["cj_centrum"]) + Vector((0, 0, op * 0.5))
    DR = math.radians(float(E("PR_IZ_DRAAI", "-30"))); KA = math.radians(float(E("PR_IZ_KANTEL", "22")))
    AFZ = float(E("PR_IZ_AFSTAND", "120"))
    cam.location = c + Vector((math.sin(DR) * math.cos(KA), -math.cos(DR) * math.cos(KA), math.sin(KA))) * AFZ
    cam.rotation_euler = (c - cam.location).to_track_quat("-Z", "Y").to_euler()
    cam.data.shift_x = cam.data.shift_y = 0
    sc.render.resolution_x = sc.render.resolution_y = 1000
    sc.render.filepath = os.path.join(UIT, "inzet.png")
    bpy.ops.render.render(write_still=True)
    log("klaar inzet")
