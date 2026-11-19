"""Toets Pro 1.1 stap 1: figuurpresets zonder rig (ontwerp-1.1.md).

Op een staaf langs X (straal 6 mm, 90 mm lang, mm-scene):
- "Knee" op x = -20: scharnier met stand 135, twee gesloten delen, record Knee / HINGE / herkomst preset,
  gemeten bereik tussen 120 en 136 graden, regel in het paneel "Knee · Hinge · 0–N° · preset";
- "Shoulder" op het deel rechts, x = +20: kogel, nu twee records op de nieuwe delen, de lijst van de figuur
  heeft Knee en Shoulder (in die volgorde), samenvatting "2 joints";
- "Elbow" op dezelfde plek als de knie: geweigerd door het scharnier zelf, lijst blijft 2;
- een open mesh: geweigerd, geen record;
- de zes presets staan in het paneel, met icoon (icon_value > 0) als er een venster is; zonder venster alleen
  dat de iconen geladen zijn.
Gebruik: blender -b --factory-startup --python e2e/toetsen_figuur.py -- <betaalde zip>
"""
import json
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

FOUT = []


def log(t):
    print(f"[cj-figuur] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def cursor(x):
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):
        m.col[i][:3] = v
    m.col[3][:3] = (x, 0.013, 0.021)
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m


def gesloten(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return fout == 0


def main():
    zip_pad = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    import importlib
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    log(f"Blender {bpy.app.version_string}")
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True

    check([p[1] for p in fig.PRESETS] == ["Shoulder", "Elbow", "Hip", "Knee", "Ankle", "Neck"], "zes vaste namen")
    iconen = [fig.icoon(p[0]) for p in fig.PRESETS]
    log(f"iconen {iconen}")
    check(fig._iconen[0] is not None and all(len(fig._iconen[0].get(p[0].lower()).image_size) == 2
                                            for p in fig.PRESETS if p[0].lower() in fig._iconen[0])
          and len(fig._iconen[0]) == 6, "zes iconen geladen")

    staaf = figuren.staaf("pop", 6.0, lengte=90.0)
    figuren.maak_actief(staaf)
    cursor(-20.0)
    r = bpy.ops.click_joints.plaats_preset(deel="KNEE")
    check(r == {"FINISHED"}, f"Knee geplaatst ({r})")
    a, b = bpy.data.objects.get("pop_A"), bpy.data.objects.get("pop_B")
    check(a is not None and b is not None, "twee delen pop_A en pop_B")
    if a is None or b is None:
        log(f"KLAAR {len(FOUT)} FOUT")
        return
    check(gesloten(a) and gesloten(b), "Knee: twee gesloten delen")
    check(b.get("cj_soort") == "SCHARNIER" and int(b.get("cj_stand", 0)) == 135, f"Knee: scharnier stand {b.get('cj_stand')}")
    recs = fig.lees(b)
    check(len(recs) == 1 and recs[0]["naam"] == "Knee" and recs[0]["soort"] == "HINGE"
          and recs[0]["herkomst"] == "preset", f"Knee: record {recs}")
    g = recs[0]["graden"] if recs else None
    check(g is not None and 120.0 <= g <= 136.0, f"Knee: gemeten bereik {g} tussen 120 en 136")
    check(g is not None and abs(g - float(b["cj_bereik_graden"])) < 0.11, "Knee: getal gelijk aan de beweegproef")
    tekst = fig.regel(recs[0]) if recs else ""
    log(f"regel: {tekst}")
    check(tekst == f"Knee · Hinge · 0–{g:.0f}° · preset", "Knee: regel in het paneel")
    check(a.get("cj_figuur") == "pop" and b.get("cj_figuur") == "pop", "Knee: figuurnaam op beide delen")

    rechts = b  # lidas is +X, dus deel B ligt rechts van de knie
    check(rechts is not None, f"deel rechts gevonden ({rechts.name if rechts else None})")
    figuren.maak_actief(rechts)
    cursor(20.0)
    r = bpy.ops.click_joints.plaats_preset(deel="SHOULDER")
    check(r == {"FINISHED"}, f"Shoulder geplaatst ({r})")
    nieuw = [o for o in bpy.context.scene.objects if o.get("cj_naam") == "Shoulder"]
    check(len(nieuw) == 2 and all(gesloten(o) for o in nieuw), f"Shoulder: twee gesloten delen ({len(nieuw)})")
    if nieuw:
        s = nieuw[0]
        check(s.get("cj_soort") == "KOGEL", f"Shoulder: kogel ({s.get('cj_soort')})")
        recs = fig.lees(s)
        check([r_["naam"] for r_ in recs] == ["Knee", "Shoulder"], f"Shoulder: deel kent beide ({recs})")
        check(recs[-1]["soort"] == "BALL" and recs[-1]["graden"] is not None
              and recs[-1]["graden"] == float(importlib.import_module("bl_ext.user_default.click_joints.paneel").buig_graden(s)),
              "Shoulder: ±graden gelijk aan het paneel (Bends ±N°, met beweegproef; sinds 16 nov run 6)")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, "pop")
    check([x["naam"] for x in lijst] == ["Knee", "Shoulder"], f"lijst van de figuur ({[x['naam'] for x in lijst]})")
    check(fig.samenvatting(lijst) == "2 joints", f"samenvatting '{fig.samenvatting(lijst)}'")
    check(fig.samenvatting(lijst + [{"herkomst": "from rig"}]) == "3 joints · 1 rig · 2 preset", "samenvatting met rig")
    # Daan 18 nov moet 1: elk lid één keer geteld, de getallen tellen op tot het totaal.
    _l = [{"herkomst": h} for h in ["from rig"] * 2 + ["mirrored"] * 2 + ["preset"] * 5]
    check(fig.samenvatting(_l) == "9 joints · 2 rig · 2 mirror · 5 preset", f"samenvatting 9 ('{fig.samenvatting(_l)}')")

    links = [o for o in bpy.context.scene.objects if o.get("cj_naam") == "Knee" and o.get("cj_deel") == "A"]
    if links:
        figuren.maak_actief(links[0])
        cursor(-20.0)
        try:
            r = bpy.ops.click_joints.plaats_preset(deel="ELBOW")
        except RuntimeError as e:
            r = f"fout {e}"
        check(r == {"CANCELLED"}, f"Elbow op de knie geweigerd ({r})")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, "pop")
    check(len(lijst) == 2, f"lijst blijft 2 ({len(lijst)})")

    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=4, y_segments=4, size=20)
    me = bpy.data.meshes.new("vlak")
    bm.to_mesh(me)
    bm.free()
    vlak = bpy.data.objects.new("vlak", me)
    bpy.context.scene.collection.objects.link(vlak)
    figuren.maak_actief(vlak)
    try:
        r = bpy.ops.click_joints.plaats_preset(deel="HIP")
    except RuntimeError as e:
        r = f"fout {e}"
    # Een ERROR-melding komt bij bpy.ops als RuntimeError terug: dat is hier de weigering.
    geweigerd = r == {"CANCELLED"} or (isinstance(r, str) and "not watertight" in r)
    check(geweigerd and "cj_gewrichten" not in vlak and not any(o.get("cj_naam") == "Hip" for o in bpy.data.objects),
          f"open mesh geweigerd, geen Hip ({r})")
    log(json.dumps({"lijst": lijst}))
    log(f"KLAAR {len(FOUT)} FOUT")


main()
