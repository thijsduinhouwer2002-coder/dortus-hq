"""Opname Regisseur run 14: de robot-actiefiguur door Figure from rig van Click Joints Pro (24 nov 2026, Regisseur).
Script: week 49 nr. 1 (commercie/filmpjes/scripts/week-49-click-joints.md, ja Daan), Pro-lijst nr. 1 in
scripts/volgorde-stem.md. De eerste Pro-Short met de robot van studio-3 (Thijs vond het mensfiguur "super nep").

Draait de opname van reeks 4 (../youtube-shorts-4/opname.py: echte Blender 5.3.0, echte muis, OCR) met twee wijzigingen:
1. Figuur: de robot (../studio/figuur_robot.py via figuur_laden.laad_figuur("robot")), zelfde punt-sleutels als het
   mensfiguur, dus de klikken op onderbeen en schouder van reeks 4 werken ongewijzigd.
2. Renders in de studio (../studio/studio.py) zoals studio-3: kleur_herstel, gewrichten antraciet;
   render-1 heldenpose, render-2 uit elkaar (26 mm per gewricht), render-3 heldenpose dichterbij van de andere kant.
    blender --gpu-backend opengl start.blend --python opname.py -- <map> <betaalde zip>
De workflow eist de regels "KORT OK <deel>"."""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.abspath(os.path.join(HIER, "..", "youtube-shorts-4", "opname.py"))
STUDIO = os.path.abspath(os.path.join(HIER, "..", "studio"))
src = open(BRON, encoding="utf-8").read()

FIGUUR = r'''
import sys as _sys
_sys.path.insert(0, STUDIO_MAP)
import figuur_laden as FL  # noqa: E402
import figuur_robot as R  # noqa: E402
import studio as S  # noqa: E402


def figuur():
    arm, ob, punten = FL.laad_figuur("robot", 220.0)
    arm.data.display_type = "STICK"
    arm.show_in_front = True
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    exportmap = os.path.join(scherm_basis.uitmap, "export")
    os.makedirs(exportmap, exist_ok=True)
    inst.exportmap = exportmap
    log(f"KORT robot {ob.name} punten {len(ob.data.vertices)}")
    return ob, arm, punten


def renders_robot(p):
    sc = bpy.context.scene
    inst = sc.click_joints
    wm = bpy.context.window_manager
    try:
        wm.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    inst.uit_elkaar = False
    S.bouw(220.0)
    delen = [o for o in sc.objects if o.type == "MESH" and o.get("cj_figuur")]
    houd = set(o.name for o in delen)
    weg = []
    for o in sc.objects:
        if o.type == "MESH" and o.name not in houd and not o.name.startswith("studio_") and o.visible_get():
            o.hide_set(True)
            o.hide_render = True
            weg.append(o.name)
    log(f"KORT render uit beeld: {weg[:10]}")
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    cam_ob = S.camera()

    def scharnier(n, g):
        _a, b = paar(n)
        if b is not None:
            buig(b, g)
            bpy.context.view_layer.update()

    film["metingen"]["render_pose"] = R.poseer(delen, R.HELD, scharnier=scharnier)
    geen_selectie()
    bpy.context.view_layer.update()
    yield 0.5
    S.richt(cam_ob, delen, "staand", draai=-32, kantel=7, vul=0.74, midden_y=0.56)
    yield 0.3
    S.render(os.path.join(scherm_basis.uitmap, "render-1.png"))
    log("KORT render-1")

    R.poseer(delen, {}, uit=26.0)
    bpy.context.view_layer.update()
    yield 0.5
    lo, _hi = S.kader(delen)
    zak = min(0.0, lo.z - 0.5)
    studio_obs = [o for o in sc.objects if o.name in ("studio_wand", "studio_podium", "studio_rand")]
    for o in studio_obs:
        o.location.z += zak
    S.richt(cam_ob, delen, "staand", draai=-24, kantel=6, vul=0.80, midden_y=0.55)
    yield 0.3
    S.render(os.path.join(scherm_basis.uitmap, "render-2.png"))
    for o in studio_obs:
        o.location.z -= zak
    log("KORT render-2")

    R.poseer(delen, R.HELD, scharnier=scharnier)
    geen_selectie()
    bpy.context.view_layer.update()
    yield 0.5
    S.richt(cam_ob, delen, "staand", draai=28, kantel=10, vul=0.86, midden_y=0.52)
    yield 0.3
    S.render(os.path.join(scherm_basis.uitmap, "render-3.png"))
    log("KORT render-3")


renders = renders_robot
'''

vervang = [
    ("gang = verloop()", FIGUUR.replace("STUDIO_MAP", repr(STUDIO)) + "\ngang = verloop()"),
]
for oud, nieuw in vervang:
    assert src.count(oud) == 1, f"niet gevonden of dubbel: {oud}"
    src = src.replace(oud, nieuw)
g = {"__name__": "__main__", "__file__": BRON}
exec(compile(src, BRON, "exec"), g)   # noqa: S102 (eigen code uit de repo)
