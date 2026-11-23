"""Testset betrouwbaarheid Figure from rig (Betrouwbaarheid, 23 nov 2026).

Draait de knop Figure from rig op één figuur uit een vaste testset en schrijft per figuur op: hoeveel gewrichten,
welke overgeslagen en waarom (de echte melding van de add-on), en per snede wat er gebeurde (meet_diag.py).
Figuren (allemaal eigen werk of vrije licentie, niets gedownload):
- robot-a, robot-b: de robot-actiefiguur van de studio (eigen werk, commercie/filmpjes/studio/figuur_robot.py), beide
  kleurstellingen, voxel 0,5 mm (zoals in de filmpjes).
- robot-fijn: dezelfde robot met voxel 0,35 mm (LEESMIJ studio: daar viel lokaal de linkerheup weg).
- kleding: MakeHuman base.obj (CC0 1.0, staat in de repo) aangekleed, zoals in studio-1 (figuur_laden.py).
- mens: dezelfde MakeHuman base.obj kaal, met de rig van e2e/proef_mens.py (zoals toetsen_mens.py), 220 mm.
- rigify: de echte Rigify-metarig van Blender met buizen (e2e/proef_rigify.py).
- armen: buizenfiguur met armen en benen uit één stuk (e2e/toetsen_rig_armen.py, B = 90).
Gebruik: blender -b --factory-startup --python e2e/meet_rig.py -- <pro-zip> <figuur> <uit.json>
Laatste regel: "MEET <figuur> gewrichten=<n> overgeslagen=<n>".
"""
import importlib
import json
import os
import sys
import time

import bpy

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
STUDIO = os.path.join(REPO, "commercie", "filmpjes", "studio")
MH_OBJ = os.path.join(STUDIO, "modellen", "makehuman-base.obj")
sys.path.insert(0, HIER)
sys.path.insert(0, STUDIO)

args = sys.argv[sys.argv.index("--") + 1:]
ZIP, FIGUUR, UIT = args[0], args[1], args[2]
STANDAARD = ["Left shoulder", "Right shoulder", "Left elbow", "Right elbow", "Left hip", "Right hip",
             "Left knee", "Right knee", "Neck"]


def log(t):
    print(f"[meet] {t}", flush=True)


def installeer():
    if "figuur_uit_rig" not in dir(bpy.ops.click_joints):
        bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)


def actief(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob


def standaard_inst():
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True


def bouw_robot(stijl=None, voxel=0.5):
    import figuur_robot as R
    _arm, ob, _p = R.laad_robot(220.0, stijl=stijl, voxel_mm=voxel)
    return ob


def bouw_kleding():
    import figuur_laden as FL
    _arm, ob, _p = FL.laad_mens_kleding(MH_OBJ, 220.0)
    return ob


def bouw_mens():
    os.environ["CJ_HOOGTE"] = "220"
    src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
    M = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
    exec(compile(src, "proef_mens.py", "exec"), M)
    A = M["A"]
    A["leeg"]()
    ob, punten = M["laad_mens"](MH_OBJ)
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        actief(ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    rig = M["maak_rig"](punten)
    ob.modifiers.new("Armature", "ARMATURE").object = rig
    return ob


def bouw_armen():
    src = open(os.path.join(HIER, "toetsen_rig_armen.py"), encoding="utf-8").read()
    M = {"__name__": "toetsen_rig_armen", "__file__": os.path.join(HIER, "toetsen_rig_armen.py")}
    exec(compile(src, "toetsen_rig_armen.py", "exec"), M)
    mesh, _arm = M["figuur"](90.0)
    return mesh


def bouw_meshy():
    """Alleen voor onderzoek, niet in de testset (licentie van de Meshy-set niet zelf nagelezen): een Meshy-figuur
    zoals toetsen_meshy_rig.py (150 mm, Make watertight, rig uit doorsneden, alleen heupen en knieën). Pad in CJ_GLB."""
    os.environ["CJ_ALLEEN"] = "hip,knee"
    os.environ["CJ_HEUP_PCT"] = "52"
    src = open(os.path.join(HIER, "proef_meshy_rig.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
    P = {"__name__": "proef_meshy_rig", "__file__": os.path.join(HIER, "proef_meshy_rig.py")}
    exec(compile(src, "proef_meshy_rig.py", "exec"), P)
    A = P["A"]
    A["leeg"]()
    ob = A["laad"](os.environ["CJ_GLB"])
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        actief(ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    rig = P["maak_rig"](ob)
    ob.modifiers.new("Armature", "ARMATURE").object = rig
    rigm = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
    echt = rigm.gewrichten
    rigm.gewrichten = lambda a, meer=False: [x for x in echt(a, meer) if "hip" in x[2].lower() or "knee" in x[2].lower()]
    return ob


def zelf_overlap_bron(ob):
    import meet_diag
    try:
        return meet_diag.zelf_overlap(ob)
    except Exception as e:
        return f"fout {e}"


def verslag(naam, t0, extra=None):
    import meet_diag
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
    alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
    over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), "") or ""
    namen = [x["naam"] for x in alle]
    uit = {"figuur": FIGUUR, "blender": bpy.app.version_string, "gewrichten": len(alle), "namen": namen,
           "regels": [fig.regel(x) for x in alle], "overgeslagen": over,
           "ontbreekt": [n for n in STANDAARD if n not in namen],
           "delen": len(delen), "open_delen": [o.name for o in delen if not ges.is_gesloten(o)[0]],
           "knop_s": round(time.perf_counter() - t0, 1), "pogingen": meet_diag.POGINGEN, "sneden": meet_diag.SNEDEN,
           # Vingerafdruk voor herhalingen (hoofdchat 23 nov: zelfde mesh, wisselende uitkomst): de regels met bereik en
           # het aantal punten per deel. Twee runs met dezelfde vingerafdruk gaven precies hetzelfde figuur.
           "vinger": {"regels": sorted(fig.regel(x) for x in alle), "punten": sorted(len(o.data.vertices) for o in delen)},
           "threads": os.environ.get("CJ_THREADS", "")}
    uit.update(extra or {})
    os.makedirs(os.path.dirname(os.path.abspath(UIT)), exist_ok=True)
    json.dump(uit, open(UIT, "w"), indent=1, default=str)
    slecht = [s for s in meet_diag.SNEDEN if not s.get("goed", True)]
    log(f"Blender {bpy.app.version_string} figuur {FIGUUR}: {len(alle)} gewrichten {namen}")
    log(f"ontbreekt: {uit['ontbreekt']}; overgeslagen: {over}")
    log(f"pogingen {len(meet_diag.POGINGEN)}, sneden {len(meet_diag.SNEDEN)}, slechte sneden {len(slecht)}")
    for s in slecht:
        log(f"  SLECHT {json.dumps(s, default=str)[:1500]}")
    print(f"MEET {FIGUUR} gewrichten={len(alle)} overgeslagen={len(uit['ontbreekt'])} slechte_sneden={len(slecht)}",
          flush=True)


def main():
    import meet_diag
    if FIGUUR == "rigify":
        # proef_rigify.py bouwt de figuur en drukt zelf op de knop; CJ_HOOK zet vlak ervoor de meetregels aan.
        haak = "/tmp/cj_meet_haak.py"
        open(haak, "w").write("import meet_diag as _md\n_md.instrumenteer()\n_MEET_T0 = __import__('time').perf_counter()\n")
        os.environ["CJ_HOOK"] = haak
        os.environ.pop("CJ_NA", None)
        os.environ.pop("CJ_ALLEEN", None)
        G = {"__name__": "proef_rigify", "__file__": os.path.join(HIER, "proef_rigify.py")}
        sys.argv = [sys.argv[0], "--", ZIP]
        exec(compile(open(os.path.join(HIER, "proef_rigify.py")).read(), "proef_rigify.py", "exec"), G)
        verslag("held", G.get("_MEET_T0", time.perf_counter()))
        return
    installeer()
    bouwers = {"robot-a": lambda: bouw_robot(), "robot-b": lambda: bouw_robot(_stijl_b()),
               "robot-fijn": lambda: bouw_robot(voxel=0.35), "kleding": bouw_kleding, "mens": bouw_mens,
               "armen": bouw_armen, "meshy": bouw_meshy}
    ob = bouwers[FIGUUR]()
    standaard_inst()
    naam = ob.name
    extra = {"bron_punten": len(ob.data.vertices), "bron_zelf_overlap": zelf_overlap_bron(ob)}
    log(f"figuur {FIGUUR}: {naam}, {extra}")
    meet_diag.instrumenteer()
    actief(ob)
    t0 = time.perf_counter()
    try:
        r = bpy.ops.click_joints.figuur_uit_rig()
    except RuntimeError as e:
        r = f"fout {str(e).strip()[:300]}"
    extra["uitslag"] = str(r)
    verslag(naam, t0, extra)


def _stijl_b():
    import figuur_robot as R
    return R.STIJL_B


main()
