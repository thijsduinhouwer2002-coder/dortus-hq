# Kopersreis Click Cuts: snelstart letterlijk volgen in de achtergrond.
import bpy, sys, os, glob, traceback, time

args = sys.argv[sys.argv.index("--") + 1:]
ZIP, UIT = args[0], args[1]
os.makedirs(UIT, exist_ok=True)

def log(*a):
    print("[reis]", *a, flush=True)

def sj():
    return bpy.context.scene.split_joints

def stap(naam, f):
    try:
        r = f()
        log("GOED" if r is not False else "DREMPEL", naam, "" if r in (None, True, False) else r)
        return r
    except Exception as e:
        log("FOUT", naam, repr(e))
        traceback.print_exc()
        return False

def doe(op, **kw):
    r = op(**kw)
    return r

def kies(obj):
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    obj.hide_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

def stand():
    s = sj()
    stukken = [o for o in bpy.data.objects if o.name.startswith("piece") or (o.users_collection and o.users_collection[0].name == "Click Cuts pieces")]
    return "uitslag=%r meldingen=%r stukken=%d" % (s.uitslag, s.meldingen[:300], len(stukken))

# 1. Installeren zoals Install from Disk / slepen
def installeer():
    r = bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    ok = hasattr(bpy.types.Scene, "split_joints") and hasattr(bpy.types, "SPLIT_JOINTS_PT_paneel")
    pt = getattr(bpy.types, "SPLIT_JOINTS_PT_paneel", None)
    return "%s paneel=%s tab=%s" % (r, ok, getattr(pt, "bl_category", None)) if ok else False
stap("installeren", installeer)

# 2. Eenvoudig model: de standaard kubus van een nieuwe scene (2 m)
def kubus():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    c = bpy.data.objects.get("Cube")
    kies(c)
    sj().printer = "A1"
    r = bpy.ops.split_joints.split_to_fit()
    return "%s %s" % (r, stand())
stap("standaardkubus 2 m, A1, Split to fit", kubus)

# 3. Een model in mm geïmporteerd als STL (zoals een download van Printables)
def stl_mm():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete()
    bpy.ops.mesh.primitive_monkey_add(size=300)  # 300 eenheden: een mm-model
    m = bpy.context.active_object
    bpy.ops.object.modifier_add(type="SUBSURF"); m.modifiers[0].levels = 2
    bpy.ops.object.modifier_apply(modifier=m.modifiers[0].name)
    pad = os.path.join(UIT, "aap_mm.stl")
    if hasattr(bpy.ops.wm, "stl_export"):
        bpy.ops.wm.stl_export(filepath=pad)
    else:
        bpy.ops.export_mesh.stl(filepath=pad)
    bpy.ops.object.delete()
    if hasattr(bpy.ops.wm, "stl_import"):
        bpy.ops.wm.stl_import(filepath=pad)
    else:
        bpy.ops.import_mesh.stl(filepath=pad)
    m = bpy.context.selected_objects[0]
    kies(m)
    sj().printer = "A1"
    r = bpy.ops.split_joints.split_to_fit()
    return "%s dims=%s %s" % (r, tuple(round(d) for d in m.dimensions), stand())
stap("aap 300 mm als STL, A1, Split to fit", stl_mm)

def omzetten():
    r = bpy.ops.split_joints.zet_om_mm()
    s = bpy.context.scene.unit_settings
    m = bpy.data.objects.get("aap_mm") or [o for o in bpy.data.objects if o.type == "MESH"][0]
    kies(m)
    r2 = bpy.ops.split_joints.split_to_fit()
    return "%s unit=%s scale=%s; daarna %s %s" % (r, s.length_unit, s.scale_length, r2, stand())
stap("Convert to mm en opnieuw Split to fit", omzetten)

def exporteer():
    r = bpy.ops.split_joints.exporteer()
    import tempfile
    kand = glob.glob(os.path.join(tempfile.gettempdir(), "**", "click_cuts", "*.*"), recursive=True)
    kand += glob.glob(os.path.join(bpy.app.tempdir, "**", "*.stl"), recursive=True)
    return "%s map=%r bestanden=%s" % (r, sj().exportmap, sorted(os.path.basename(k) for k in kand)[:20])
stap("Export parts (STL), .blend niet bewaard", exporteer)

def exporteer_bewaard():
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(UIT, "mijn.blend"))
    r = bpy.ops.split_joints.exporteer()
    fs = sorted(os.listdir(os.path.join(UIT, "click_cuts"))) if os.path.isdir(os.path.join(UIT, "click_cuts")) else None
    return ("%s %s" % (r, fs)) if fs else False
stap("Export parts (STL), .blend bewaard", exporteer_bewaard)

def fittest():
    s = sj()
    s.materiaal = "PLA" if "PLA" in [i.identifier for i in s.bl_rna.properties["materiaal"].enum_items] else s.materiaal
    r = bpy.ops.split_joints.passing_maak()
    r2 = bpy.ops.split_joints.passing_export()
    fs = sorted(os.listdir(os.path.join(UIT, "click_cuts")))
    return "%s %s speling=%.2f materialen=%s bestanden=%s" % (r, r2, s.speling_mm, [i.identifier for i in s.bl_rna.properties["materiaal"].enum_items], fs)
stap("fit test maken en exporteren", fittest)

def vrije():
    stukken = [o for o in bpy.data.objects if o.users_collection and o.users_collection[0].name == "Click Cuts pieces" and o.type == "MESH" and not o.name.lower().startswith("pin")]
    if not stukken:
        return False
    kies(stukken[0]); n0 = len(stukken)
    r = bpy.ops.split_joints.vrije_snede_erbij()
    r2 = bpy.ops.split_joints.vrije_snede()
    return "%s %s %s" % (r, r2, stand())
stap("Add free cut en Cut piece", vrije)

log("KLAAR", bpy.app.version_string)
