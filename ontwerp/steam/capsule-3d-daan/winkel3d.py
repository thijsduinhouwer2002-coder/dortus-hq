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
elif soort == "logo":
    # alleen de titel, doorzichtig, recht van voren
    src = src[:cam_begin] + '''# ---------- logo: alles behalve de titel onzichtbaar ----------
for o in list(sc.objects):
    if o.type in ("MESH", "CURVE", "FONT") and not o.name.startswith("titel"):
        o.hide_render = True
for o in sc.objects:
    if o.name.startswith("titel"):
        o.location.x += 4.55; o.location.z -= 1.4
cam = bpy.data.cameras.new("cam"); cam.type = "ORTHO"; cam.ortho_scale = float(os.environ.get("LOGO_SCHAAL", "6.4"))
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
