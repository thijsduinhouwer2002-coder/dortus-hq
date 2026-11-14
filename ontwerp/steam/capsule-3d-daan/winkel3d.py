"""Daan, 14 nov: hero 3840x1240 en logo 1280 voor de Steam-bibliotheek, uit Mila's capsule3d.py.
Leest haar script, vervangt alleen titel, camera en de breedte van de wand, en voert het uit.
Gebruik (venv met bpy 5.2.4):
  python winkel3d.py hero.png 3840 1240 24 hero
  python winkel3d.py logo.png 2560 1410 32 logo
"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.normpath(os.path.join(HIER, "..", "capsule-3d", "capsule3d.py"))
soort = sys.argv[5]
src = open(BRON, encoding="utf-8").read()
sys.argv = sys.argv[:5] + ["header"]

def vervang(oud, nieuw):
    global src
    assert oud in src, oud[:60]
    src = src.replace(oud, nieuw, 1)

titel_begin = src.index("if KLEIN:\n    tekst(\"HATS\"")
titel_eind = src.rindex("# ---------- licht")
cam_begin = src.rindex("# ---------- camera")
cam_eind = src.rindex("sc.render.engine")

if soort == "hero":
    # geen titel (Steam legt het logo erover), wand en rotsen breder, twee fakkels extra
    src = src[:titel_begin] + src[titel_eind:]
    cam_begin = src.rindex("# ---------- camera"); cam_eind = src.rindex("sc.render.engine")
    src = src[:cam_begin] + '''# ---------- camera (hero) ----------
cam = bpy.data.cameras.new("cam"); cam.lens = float(os.environ.get("HERO_LENS", "26")); cam.sensor_fit = "HORIZONTAL"; cam.sensor_width = 36
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
doel = Vector((float(os.environ.get("HERO_X", "2.2")), 0.6, float(os.environ.get("HERO_Z", "2.3"))))
co.location = (doel.x, -13.5, 3.7)
co.rotation_euler = (doel - Vector(co.location)).to_track_quat("-Z", "Y").to_euler()
''' + src[cam_eind:]
    vervang("for i in range(40):\n    x = -7.5 + i * 0.4", "for i in range(75):\n    x = -12.5 + i * 0.4")
    vervang("for i in range(26):\n    x = random.uniform(-7, 7)", "for i in range(50):\n    x = random.uniform(-11, 15)")
    # ronde 2: geen behang van vier gelijke fakkels; links een zwakke boven het logo (Steam zet het logo linksonder), rechts een hogere verder weg
    vervang("    fakkel(GX + 3.4, 3.1)\n", "    fakkel(GX + 3.4, 3.1)\n    fakkel(GX + 7.9, 3.6, kracht=150)\n    fakkel(GX - 7.6, 3.3, kracht=140)\n")
    # ronde 2: hoeden op de berg iets groter dan de hoge hoed, schuiven iets naar voren (weg van de wand)
    vervang("    hoeden.bouw(nr, plek=(x, y, z), schaal=0.85, kantel=k, draai=d)", "    hoeden.bouw(nr, plek=(x, y - (0.5 if nr != 7 else 0), z), schaal=0.85 if nr == 7 else 1.05, kantel=k, draai=d)")
    # ronde 2: de berg hoeden van gevallen helden rechts naast Gloop (zoals in het spel), in plaats van één hoge hoed
    vervang("BERG = [(7, GX + 2.2, -0.3, 0.62, 12, -20)]",
            "BERG = [(7, GX + 2.3, -0.4, 0.55, 12, -20), (8, GX + 3.5, 0.3, 0.0, -10, 30), (6, GX + 4.3, 0.4, 0.0, 6, -20), (2, GX + 5.1, 0.3, 0.0, 15, -10),"
            " (5, GX + 3.9, 0.5, 0.42, -12, 10), (9, GX + 4.7, 0.55, 0.48, 14, 25), (3, GX + 4.3, 0.6, 0.9, -6, 0)]")
    # ronde 3 (kan van de frisse kijker): de ridder kijkt omhoog naar zijn helm op Gloop, niet recht vooruit.
    # Alleen in de hero: pupillen en glimstip iets hoger (HERO_BLIK, in hoofdmaat). Mila's capsule blijft gelijk.
    blik = float(os.environ.get("HERO_BLIK", "0.035"))
    # ronde 3 (kan): de rand van de muntenplas is een harde ellips; losse munten over de rand heen maken hem rafelig.
    # Eigen random, zodat de rest van de scène (stenen, munten) op dezelfde plek blijft.
    if os.environ.get("HERO_RAND", "1") == "1":
        vervang("# beker\n", '''_rr = random.Random(5)
for _i in range(int(os.environ.get("HERO_RANDMUNTEN", "90"))):
    _a = _rr.uniform(0, 2 * math.pi); _f = _rr.uniform(0.9, 1.18)
    _x = GX + 3.25 * _f * math.cos(_a); _y = 0.5 + 2.15 * _f * math.sin(_a)
    if _y > 1.6 or (_x < GX - 2.4 and _y < 0.6):   # niet bij de voeten en het schild van de ridder (frisse kijker)
        continue
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=_rr.uniform(0.12, 0.18), depth=0.05, location=(_x, _y, 0.03 + max(0, 1.0 - _f) * 0.6),
                                        rotation=(math.radians(_rr.uniform(-12, 12)), math.radians(_rr.uniform(-12, 12)), _rr.uniform(0, 6)))
    _m = bpy.context.object; _m.name = "munt"; bpy.ops.object.shade_smooth(); kies(_m, GOUD)
# beker
''')
    vervang('                   gloed=30, rand=float(os.environ.get("RIDDER_RAND", "25")))\n',
            '                   gloed=30, rand=float(os.environ.get("RIDDER_RAND", "25")))\n'
            'for _o in ridder.children:\n'
            '    if _o.type == "MESH" and _o.data.materials and _o.data.materials[0].name.startswith(("hpupil", "hglim")):\n'
            '        _o.location.z += %f\n' % blik)
elif soort == "logo":
    # alleen de titel, doorzichtig, recht van voren
    src = src[:cam_begin] + '''# ---------- logo: alles behalve de titel onzichtbaar ----------
for o in list(sc.objects):
    if o.type in ("MESH", "CURVE", "FONT", "META", "SURFACE") and not o.name.startswith("titel"):
        o.hide_render = True
for o in sc.objects:
    if o.name.startswith("titel"):
        o.location.x += 4.55; o.location.z -= 1.4
        if o.type == "FONT" and o.data.body == "OF THE FALLEN":
            # logo ronde 2: ondertitel dichter onder HATS en eronder gecentreerd (in de capsule mag hij uitsteken, los niet)
            o.location.x += float(os.environ.get("LOGO_OX", "-0.28")); o.location.z += float(os.environ.get("LOGO_OZ", "0.23"))
sc.view_settings.exposure = float(os.environ.get("LOGO_BELICHTING", "-0.6"))   # zonder muur en Gloop eromheen werd HATS bijna wit
# ronde 1 logo (Daan, 14 nov 17:40): op elke letter van HATS een hoed uit het spel, zoals het pixellogo deed
# (kroon, heksenhoed, pan, veermuts). LOGO_HOEDEN=0 zet ze uit, LOGO_HS is de maat van de hoeden.
if os.environ.get("LOGO_HOEDEN", "1") == "1":
    import hoeden
    bpy.context.view_layer.update()
    hats = [o for o in sc.objects if o.type == "FONT" and o.name.startswith("titel") and not o.name.startswith("titelrand") and o.data.body == "HATS"][0]
    def breedte(woord):
        cu = hats.data.copy(); cu.body = woord; cu.extrude = 0; cu.bevel_depth = 0
        t = bpy.data.objects.new("maat", cu); sc.collection.objects.link(t); bpy.context.view_layer.update()
        bb = [Vector(v) for v in t.bound_box]; xs = [v.x for v in bb]; ys = [v.y for v in bb]
        bpy.data.objects.remove(t)
        return min(xs), max(xs), max(ys)
    KEUZE = [(4, -4, 0), (1, 6, 0), (5, 5, 10), (9, -10, -15)]   # ronde 3: pan las als zwart potje, helm los als serveerdeksel met worm (frisse kijker); koksmuts leest wel, kroon minder scheef   # (hoed, kantel, draai) per letter
    hs = float(os.environ.get("LOGO_HS", "0.68"))
    vorig = 0.0
    for i, (nr, k, d) in enumerate(KEUZE):
        x0, x1, top = breedte("HATS"[:i + 1])
        lx0, lx1, ltop = breedte("HATS"[i])
        links = x1 - (lx1 - lx0)
        midden = (links + x1) / 2
        p = hats.matrix_world @ Vector((midden, ltop + 0.04, 0.0))
        hoeden.bouw(nr, plek=(p.x, p.y, p.z), schaal=hs, kantel=k, draai=d)
    # ronde 3b: koksmuts was egaal wit en plat (frisse kijker); in het logo iets grijzer, dan tonen de plooien
    for m in bpy.data.materials:
        if m.name.startswith("koks") and m.use_nodes:
            for n in m.node_tree.nodes:
                if n.type == "BSDF_PRINCIPLED":
                    n.inputs["Base Color"].default_value = (0.52, 0.53, 0.58, 1)
cam =bpy.data.cameras.new("cam"); cam.type = "ORTHO"; cam.ortho_scale = float(os.environ.get("LOGO_SCHAAL", "6.4"))
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
doel = Vector((float(os.environ.get("LOGO_X", "2.4")), -0.6, float(os.environ.get("LOGO_Z", "1.85"))))
co.location = (doel.x, -13.5, doel.z + 1.2)
co.rotation_euler = (doel - Vector(co.location)).to_track_quat("-Z", "Y").to_euler()
''' + src[cam_eind:]
    vervang("sc.render.film_transparent = False", "sc.render.film_transparent = True; sc.render.image_settings.color_mode = 'RGBA'")
else:
    raise SystemExit("soort: hero of logo")

__file__ = BRON
exec(compile(src, BRON, "exec"))
