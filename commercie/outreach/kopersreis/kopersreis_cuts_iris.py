# Kopersreis Click Cuts als mailontvanger (issue #424, Iris, 28 nov 2026).
# Draaien: blender -b --factory-startup --python kopersreis_cuts_iris.py -- <zip> <uitmap>
# Volgt de belofte uit de mail en de snelstart van dortus.com/click-cuts/ met een eigen te groot model.
import bpy, sys, os, json, glob, struct, traceback, tempfile

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


def kies(obj):
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    obj.hide_set(False)
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def stukken():
    return [o for o in bpy.context.view_layer.objects if o.get("sj_stuk")]


def pennen():
    return [o for o in bpy.context.view_layer.objects if o.get("sj_pennen")]


def stand():
    st = stukken()
    kleur = {}
    for o in st:
        kleur[o.get("sj_status", "?")] = kleur.get(o.get("sj_status", "?"), 0) + 1
    gaten = sum(len(json.loads(o.get("sj_gaten") or "[]")) for o in st)
    labels = sum(len(json.loads(o.get("sj_labels") or "[]")) for o in st)
    return "uitslag=%r stukken=%d kleuren=%s gaten=%d nummers=%d pennen=%s meldingen=%r" % (
        sj().uitslag, len(st), kleur, gaten, labels,
        [int(p["sj_pennen"]) for p in pennen()], sj().meldingen[:200])


def stl_maat(pad):
    with open(pad, "rb") as f:
        f.read(80)
        n = struct.unpack("<I", f.read(4))[0]
        lo = [1e9] * 3; hi = [-1e9] * 3
        for _ in range(n):
            d = struct.unpack("<12fH", f.read(50))
            for v in range(3):
                for a in range(3):
                    x = d[3 + v * 3 + a]
                    lo[a] = min(lo[a], x); hi[a] = max(hi[a], x)
    return tuple(round(hi[a] - lo[a], 1) for a in range(3)), n


def importeer(pad):
    if hasattr(bpy.ops.wm, "stl_import"):
        bpy.ops.wm.stl_import(filepath=pad)
    else:
        bpy.ops.import_mesh.stl(filepath=pad)
    m = bpy.context.selected_objects[0]
    kies(m)
    return m


# 0. Installeren zoals Install from Disk of slepen
def installeer():
    r = bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    pt = getattr(bpy.types, "SPLIT_JOINTS_PT_paneel", None)
    return "%s tab=%s" % (r, getattr(pt, "bl_category", None)) if pt and hasattr(bpy.types.Scene, "split_joints") else False
stap("1 installeren", installeer)

# Eigen te groot model: buste (Suzanne, 2x onderverdeeld) van 420 mm, als STL in mm, zoals van een modelsite
MODEL = os.path.join(UIT, "buste_420mm.stl")
def maak_model():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete()
    bpy.ops.mesh.primitive_monkey_add(size=1)
    m = bpy.context.active_object
    bpy.ops.object.modifier_add(type="SUBSURF"); m.modifiers[0].levels = 2
    bpy.ops.object.modifier_apply(modifier=m.modifiers[0].name)
    bpy.ops.object.modifier_add(type="SOLIDIFY"); m.modifiers[0].thickness = 0.06
    bpy.ops.object.modifier_apply(modifier=m.modifiers[0].name)
    f = 420.0 / max(m.dimensions)
    m.scale = (f, f, f); bpy.ops.object.transform_apply(scale=True)
    if hasattr(bpy.ops.wm, "stl_export"):
        bpy.ops.wm.stl_export(filepath=MODEL)
    else:
        bpy.ops.export_mesh.stl(filepath=MODEL)
    return "maat=%s vlakken=%d" % (tuple(round(d) for d in m.dimensions), len(m.data.polygons))
stap("model maken (buiten de reis)", maak_model)

# 2. Snelstart stap 1 tot 3: nieuwe scene, STL importeren, printer kiezen, Split to fit
def eerste_split():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete()
    m = importeer(MODEL)
    sj().printer = "A1"
    r = bpy.ops.split_joints.split_to_fit()
    return "%s dims=%s %s" % (r, tuple(round(d) for d in m.dimensions), stand())
stap("2 STL 420 mm importeren, A1, Split to fit", eerste_split)

def omzetten():
    r = bpy.ops.split_joints.zet_om_mm()
    m = [o for o in bpy.data.objects if o.type == "MESH" and not o.get("sj_stuk") and not o.get("sj_pennen")][0]
    kies(m)
    r2 = bpy.ops.split_joints.split_to_fit()
    return "%s unit=%s; daarna %s %s" % (r, bpy.context.scene.unit_settings.length_unit, r2, stand())
stap("3 Convert to mm en opnieuw Split to fit", omzetten)

def kleur_check():
    sj().kleur = "CHECK"
    st = stukken()
    alle = all(o.get("sj_status") in ("groen", "oranje", "rood") for o in st)
    return ("ieder stuk heeft een kleur: %s" % stand()) if st and alle else False
stap("4 belofte: elk stuk groen, oranje of rood", kleur_check)

# 5. Opslaan en exporteren naar STL
def exporteer_stl():
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(UIT, "buste.blend"))
    sj().formaat = "STL"
    r = bpy.ops.split_joints.exporteer()
    map_ = os.path.join(UIT, "click_cuts")
    fs = sorted(os.listdir(map_))
    bed = 256 - 2 * sj().marge_mm
    maten = {f: stl_maat(os.path.join(map_, f))[0] for f in fs if f.endswith(".stl")}
    te_groot = [f for f, d in maten.items() if max(d) > 256.0]
    return ("%s bestanden=%s grootste=%s te_groot_voor_A1=%s" % (
        r, fs, max((max(d) for d in maten.values()), default=0), te_groot)) if fs and not te_groot else False
stap("5 opslaan, Export parts (STL), maat van elk bestand", exporteer_stl)

# 6. Magneten in plaats van pinnen (belofte mail 2)
def magneten():
    m = bpy.data.objects.get(sj().bron) or [o for o in bpy.data.objects if o.type == "MESH" and not o.get("sj_stuk") and not o.get("sj_pennen")][0]
    kies(m)
    sj().verbinder = "MAGNET"
    sj().magneet = "6x3"
    r = bpy.ops.split_joints.split_to_fit()
    st = stukken()
    soorten = set()
    for o in st:
        for g in json.loads(o.get("sj_gaten") or "[]"):
            soorten.add(str(g.get("soort", g.get("d", "?"))))
    return "%s gatsoorten=%s %s" % (r, sorted(soorten)[:6], stand())
stap("6 Joint op Magnets (6x3), Split to fit", magneten)

def exporteer_3mf():
    import shutil
    shutil.rmtree(os.path.join(UIT, "click_cuts"), ignore_errors=True)
    sj().formaat = "3MF"
    r = bpy.ops.split_joints.exporteer()
    fs = sorted(os.listdir(os.path.join(UIT, "click_cuts")))
    return ("%s %s" % (r, fs)) if any(f.endswith(".3mf") for f in fs) else False
stap("7 Export parts (3MF)", exporteer_3mf)

def fittest():
    sj().verbinder = "PIN"
    sj().formaat = "STL"
    r = bpy.ops.split_joints.passing_maak()
    r2 = bpy.ops.split_joints.passing_export()
    fs = sorted(f for f in os.listdir(os.path.join(UIT, "click_cuts")) if "fit" in f)
    return ("%s %s speling=%.2f %s" % (r, r2, sj().speling_mm, fs)) if fs else False
stap("8 belofte: fit test block maken en exporteren", fittest)

# 9. Tweede soort ontvanger: modelleert zelf in Blender (meters), buste 0,42 m, opslaan vergeten
def zelf_gemaakt():
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete()
    bpy.ops.mesh.primitive_monkey_add(size=1)
    m = bpy.context.active_object
    bpy.ops.object.modifier_add(type="SUBSURF"); m.modifiers[0].levels = 2
    bpy.ops.object.modifier_apply(modifier=m.modifiers[0].name)
    f = 0.42 / max(m.dimensions); m.scale = (f, f, f); bpy.ops.object.transform_apply(scale=True)
    sj().printer = "A1"
    r = bpy.ops.split_joints.split_to_fit()
    r2 = bpy.ops.split_joints.exporteer() if stukken() else None
    t = os.path.join(tempfile.gettempdir(), "click_cuts")
    return "%s %s; export zonder opslaan: %s naar %s (%d bestanden)" % (
        r, stand(), r2, t, len(os.listdir(t)) if os.path.isdir(t) else 0)
stap("9 eigen Blender-model 0,42 m, Split to fit, export zonder opslaan", zelf_gemaakt)

log("KLAAR", bpy.app.version_string)
