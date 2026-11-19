"""Plaatje 20 voor Click Joints Pro: de Fit test strip, schuin van boven (bouwen-in-stappen stap 6, testkaart-ontwerp.md).
    blender -b --factory-startup --python e2e/scherm_testkaart.py -- <map> <betaalde zip>
Maakt met de knop van de add-on (click_joints.testkaart) een set kogels en een set scharnieren in een mm-scene en
rendert met Workbench (geen X-scherm nodig):
  20-testkaart.png         beide sets, schuin van boven, het bovenste deel 14 mm opgetild zodat het gewricht te zien is,
                           scharnierset 30 mm verder naar achteren
  20d-testkaart-getal.png  dichtbij op de getallen van de kogelset
Alleen weergave: optillen gaat met delta_location, kleuren met objectkleur; de delen en de export veranderen niet.
De regel "KAART BEELD OK" is wat de workflow eist (10 + 10 delen, vijf getallen per set, beide plaatjes bestaan)."""
import math
import os
import sys

import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
uitmap, zip_pad = args[0], args[1]
os.makedirs(uitmap, exist_ok=True)
OPTIL_MM = 22.0
ACHTER_MM = 30.0  # scharnierset alleen in beeld verder naar achteren, zodat de kogels hem niet verbergen
KLEUR = {"A": (0.86, 0.62, 0.38, 1.0), "B": (0.32, 0.55, 0.78, 1.0)}  # bovenste deel warm, onderste koel


def log(t):
    print(f"[cj-kaart-scherm] {t}", flush=True)


def leeg():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)


def sets():
    uit = {}
    for c in bpy.data.collections:
        if c.name.startswith("Fit test"):
            uit[c.name] = [o for o in c.objects if o.get("cj_deel")]
    return uit


def kleur_en_optil(delen, achter=0.0):
    """Per staafje: bovenste deel (met getal) warm en opgetild, onderste deel koel."""
    per = {}
    for o in delen:
        per.setdefault(round(o.get("cj_speling_mm", 0), 3), []).append(o)
    for paar in per.values():
        hoog = max(paar, key=lambda o: max((o.matrix_world @ Vector(h)).z for h in o.bound_box))
        for o in paar:
            boven = o is hoog
            o.color = KLEUR["A" if boven else "B"]
            o.delta_location = (0, achter, OPTIL_MM if boven else 0.0)


def camera(doel, afstand, hoogte_graden, draai_graden, lens=50):
    cam = bpy.data.objects.get("Kaartcamera")
    if cam is None:
        cam = bpy.data.objects.new("Kaartcamera", bpy.data.cameras.new("Kaartcamera"))
        bpy.context.scene.collection.objects.link(cam)
    h, d = math.radians(hoogte_graden), math.radians(draai_graden)
    richting = Vector((math.cos(h) * math.sin(d), -math.cos(h) * math.cos(d), math.sin(h)))
    cam.location = doel + richting * afstand
    cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
    cam.data.lens = lens
    cam.data.clip_start, cam.data.clip_end = 1.0, 5000.0
    bpy.context.scene.camera = cam


def render(naam):
    s = bpy.context.scene
    s.render.engine = "BLENDER_WORKBENCH"
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = 1920, 1080, 100
    sh = s.display.shading
    sh.light, sh.color_type = "STUDIO", "OBJECT"
    sh.show_cavity, sh.cavity_type = True, "BOTH"
    sh.show_object_outline = True
    sh.show_shadows = True
    s.display.shadow_focus = 0.3
    s.world = s.world or bpy.data.worlds.new("Wereld")
    s.world.color = (0.017, 0.019, 0.026)  # donker zoals de andere Pro-plaatjes
    s.render.film_transparent = False
    s.view_settings.view_transform = "Standard"
    pad = os.path.join(uitmap, naam)
    s.render.filepath = pad
    bpy.ops.render.render(write_still=True)
    log(f"render {pad} {os.path.exists(pad)}")
    return os.path.exists(pad)


def midden(objs):
    bpy.context.view_layer.update()  # matrix_world neemt delta_location dan mee
    pts = [o.matrix_world @ Vector(h) for o in objs for h in o.bound_box]
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    return (lo + hi) / 2, hi - lo


def main():
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    log(f"Blender {bpy.app.version_string}")
    leeg()
    figuren.mm_scene()
    uitslag = [bpy.ops.click_joints.testkaart(soort=s) for s in ("KOGEL", "SCHARNIER")]
    log(f"knoppen: {uitslag}")
    groepen = sets()
    alle = [o for lijst in groepen.values() for o in lijst]
    ok = len(groepen) == 2 and all(len(v) == 10 for v in groepen.values())
    for naam, lijst in groepen.items():
        getallen = sorted(o.get("cj_kaart_getal") for o in lijst if o.get("cj_kaart_getal"))
        log(f"{naam}: {len(lijst)} delen, getallen {getallen}")
        ok = ok and len(getallen) == 5
        kleur_en_optil(lijst, ACHTER_MM if naam != sorted(groepen)[0] else 0.0)
    for o in bpy.context.scene.objects:
        o.select_set(False)
    m, maat = midden(alle)
    log(f"midden {tuple(round(x, 1) for x in m)} maat {tuple(round(x, 1) for x in maat)}")
    camera(m + Vector((0, 0, 6.0)), 2.6 * max(maat), 48, 18)
    ok = render("20-testkaart.png") and ok
    kogels = groepen[sorted(groepen)[0]]  # eerste klik was KOGEL: collectie "Fit test", de tweede "Fit test.001"
    for naam, lijst in groepen.items():
        for o in lijst:
            o.hide_render = o not in kogels  # dichtbij alleen de kogelset
    boven = [o for o in kogels if o.delta_location.z > 0]
    mb, maat_b = midden(boven)
    camera(Vector((mb.x, mb.y, mb.z + maat_b.z / 4)), 1.75 * maat_b.x, 60, 8, lens=60)
    ok = render("20d-testkaart-getal.png") and ok
    log(f"KAART BEELD {'OK' if ok else 'FOUT'}")


main()
