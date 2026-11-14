"""Staande winkelbeelden van Hats of the Fallen in 3D (Mila, 14 nov 2026).
Bibliotheek 600x900 (Steam-bibliotheek) en staand 748x896 (vertical capsule), uit capsule3d.py.
Leest capsule3d.py, vervangt titel, camera en de hoogte van de wand, en voert het uit (zelfde aanpak als
Daans winkel3d.py, zodat Gloop, ridder en hoeden overal gelijk blijven).

Het idee: staand is het formaat van de toren. Gloop zit onderaan op zijn goud met de volle toren van vier
hoeden (zoveel draagt hij in het spel), de ridder staat klein linksonder en kijkt omhoog naar zijn eigen
helm onderaan de toren. Bovenaan de titel met op elke letter een hoed uit het spel, zoals Daans logo.

Gebruik (venv met bpy 5.2.4), render op dubbele maat en verklein:
  python staand3d.py b.png 1200 1800 32 bibliotheek
  python staand3d.py s.png 1496 1792 32 staand
"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.join(HIER, "capsule3d.py")
soort = sys.argv[5] if len(sys.argv) > 5 else "bibliotheek"
src = open(BRON, encoding="utf-8").read()
sys.argv = sys.argv[:5] + ["header"]
os.environ.setdefault("HEADER_HOEDEN", "4")   # de hele toren: helm, kroon, heksenhoed, rode muts

def vervang(oud, nieuw):
    global src
    assert oud in src, oud[:60]
    src = src.replace(oud, nieuw, 1)

E = lambda k, d: float(os.environ.get(k, d))

# wand en kiezels hoger: staand kijken we tot ver boven Gloop
vervang("o.scale = (30, 14, 1); o.rotation_euler = (math.radians(90), 0, 0); kies(o, WAND)",
        "o.scale = (30, 30, 1); o.rotation_euler = (math.radians(90), 0, 0); kies(o, WAND)")
vervang("for i in range(26):\n    x = random.uniform(-7, 7); z = random.uniform(0.3, 6.5)",
        "for i in range(46):\n    x = random.uniform(-7, 7); z = random.uniform(0.3, 11.5)")
# fakkels: links een hogere boven de ridder, rechts zoals in de header
vervang("    fakkel(GX - 3.4 + 0.2, 3.1)", "    fakkel(GX - 3.4 + 0.2, " + os.environ.get("ST_FAKKEL_L", "3.6") + ")")
# Gloop iets groter: hij is staand de hele onderkant
vervang("GROOT = 1.1 if not KLEIN else 1.3", "GROOT = " + os.environ.get("ST_GROOT", "1.28"))
# ridder: dichter bij Gloop, zodat beide in de smalle beeldbreedte passen
vervang('RX = float(os.environ.get("HEADER_RX", "-0.1"))', 'RX = float(os.environ.get("ST_RX", "0.15"))')
vervang("RS = 1.2 if not KLEIN else 1.5", 'RS = float(os.environ.get("ST_RS", "1.45"))')   # ronde 2 (frisse kijker moet): ridder groter
vervang('RY = float(os.environ.get("HEADER_RY", "-1.95"))', 'RY = float(os.environ.get("ST_RY", "-2.3"))')
# hoedenberg rechts naast Gloop zoals in het spel (zelfde berg als Daans hero)
vervang("BERG = [(7, GX + 2.2, -0.3, 0.62, 12, -20)]",
        os.environ.get("ST_BERG", "BERG = [(8, GX + 2.3, 0.9, 0.3, -10, 30)]"))

titel_begin = src.index("if KLEIN:\n    tekst(\"HATS\"")
titel_eind = src.rindex("# ---------- licht")
src = src[:titel_begin] + '''# ---------- titel staand: gecentreerd bovenaan, met een hoed op elke letter (zoals Daans logo) ----------
CX = float(os.environ.get("ST_CX", "1.55")); TZ = float(os.environ.get("ST_TZ", "6.05"))
def midden_op(o, cx):
    bpy.context.view_layer.update()
    xs = [v[0] for v in o.bound_box]
    dx = cx - (min(xs) + max(xs)) / 2 * 1.0 - o.location.x
    for t in [o] + [r for r in sc.objects if r.name.startswith("titelrand") and abs(r.location.z - o.location.z) < 0.2 * o.data.size + 0.1 and r.data.body == o.data.body]:
        t.location.x += dx
hats = tekst("HATS", (0.0, -0.6, TZ), float(os.environ.get("ST_HS", "1.75")), kantel=-3)
midden_op(hats, CX)
sub = tekst("OF THE FALLEN", (0.0, -0.6, TZ - float(os.environ.get("ST_SUBZ", "0.7"))), float(os.environ.get("ST_SS", "0.78")), kantel=-3)
midden_op(sub, CX)
if os.environ.get("ST_LETTERHOEDEN", "1") == "1":
    bpy.context.view_layer.update()
    def breedte(woord):
        cu = hats.data.copy(); cu.body = woord; cu.extrude = 0; cu.bevel_depth = 0
        t = bpy.data.objects.new("maat", cu); sc.collection.objects.link(t); bpy.context.view_layer.update()
        bb = [Vector(v) for v in t.bound_box]; xs = [v.x for v in bb]; ys = [v.y for v in bb]
        bpy.data.objects.remove(t)
        return min(xs), max(xs), max(ys)
    KEUZE = [(4, -4, 0), (1, 6, 0), (5, 5, 10), (9, -10, -15)]   # kroon, heksenhoed, koksmuts, veermuts (Daans logo ronde 3)
    hs = float(os.environ.get("ST_LHS", "0.74"))
    for i, (nr, k, d) in enumerate(KEUZE):
        x0, x1, top = breedte("HATS"[:i + 1])
        lx0, lx1, ltop = breedte("HATS"[i])
        p = hats.matrix_world @ Vector(((x1 - (lx1 - lx0) + x1) / 2, ltop + 0.04, 0.0))
        hoeden.bouw(nr, plek=(p.x, p.y, p.z), schaal=hs, kantel=k, draai=d)
    for m in bpy.data.materials:
        if m.name.startswith("koks") and m.use_nodes:
            for n in m.node_tree.nodes:
                if n.type == "BSDF_PRINCIPLED":
                    n.inputs["Base Color"].default_value = (0.62, 0.63, 0.68, 1)
''' + src[titel_eind:]
vervang('lamp("titellamp", "AREA", (-3.0, -4.0, 4.5), (1.0, 0.95, 0.85), 500, 3.0, (-3.0, -0.6, 2.4))',
        'lamp("titellamp", "AREA", (CX, -4.5, TZ + 1.5), (1.0, 0.95, 0.85), 550, 4.0, (CX, -0.6, TZ))')

cam_begin = src.rindex("# ---------- camera")
cam_eind = src.rindex("sc.render.engine")
src = src[:cam_begin] + '''# ---------- camera staand ----------
cam = bpy.data.cameras.new("cam"); cam.lens = float(os.environ.get("ST_LENS", "52")); cam.sensor_fit = "VERTICAL"; cam.sensor_height = 36; cam.sensor_width = 36
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
doel = Vector((CX, 0.6, float(os.environ.get("ST_Z", "3.75"))))
co.location = (CX, -14.5, float(os.environ.get("ST_CAMZ", "3.3")))
co.rotation_euler = (doel - Vector(co.location)).to_track_quat("-Z", "Y").to_euler()
''' + src[cam_eind:]

__file__ = BRON
exec(compile(src, BRON, "exec"))
