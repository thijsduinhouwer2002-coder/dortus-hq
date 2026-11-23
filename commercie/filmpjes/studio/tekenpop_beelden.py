"""Renders van de houten tekenpop met de echte gewrichten van Click Joints Pro (23 nov 2026, tekenpop-agent, opdracht
hoofdchat ±22:35 NL). Release tekenpop-1.

Bouwt de tekenpop uit figuur_tekenpop.py, draait de echte knop Figure from rig van Click Joints Pro 1.2.0, kleurt
alles wat de add-on aan een gewricht maakt messing en het figuur hout, poseert met de Bend-schuif en de kogels van de
add-on (binnen het gemeten bereik) en rendert in Cycles. Hergebruikt de camera, de studio in stijl B (pruim en goud)
en het poseren uit ontwerp/click-joints-pro-v2/bron/pro_beelden.py (dat bestand wordt ingelezen zonder zijn main()).

    blender -b --factory-startup --python tekenpop_beelden.py -- <pro-zip> <uitmap> b <shot> [samples] [schaal%]
shot: staand | uit | pop169 | dyn169 | proef
  staand: staande pose (loophouding), 1600 x 1600
  uit:    rusthouding uit elkaar, 2,3 keer de afstand van de Exploded view, 1600 x 1600
  pop169: cover 2560 x 1440 in de opzet van cover B (pose plus precies de Exploded view van de add-on)
  dyn169: cover 2560 x 1440, onderdelen schuin uit elkaar alsof hij net uiteenspat, groot en deels buiten de rand
  proef:  alleen Figure from rig en de lijst met gewrichten (json), geen render
Wat de add-on meldde staat in b-<shot>.json (gewrichten, pose, graden).
"""
import json
import math
import os
import random
import sys

import bpy
from mathutils import Matrix, Quaternion, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("STUDIO_DIR", HIER)
sys.path.insert(0, HIER)
import figuur_laden as FL  # noqa: E402
import figuur_tekenpop as T  # noqa: E402

PRO = os.path.join(HIER, "..", "..", "..", "ontwerp", "click-joints-pro-v2", "bron", "pro_beelden.py")
M = {"__name__": "pro_beelden", "__file__": os.path.abspath(PRO)}
_bron = open(PRO, encoding="utf-8").read()
assert "\nmain()\n" in _bron
exec(compile(_bron.replace("\nmain()\n", "\n"), PRO, "exec"), M)   # noqa: S102 (eigen code uit de repo)
SHOT, UIT, STIJL = M["SHOT"], M["UIT"], M["STIJL"]
meting = M["meting"]
meting["figuur"] = "tekenpop"

# Loophouding: linkerbeen naar voren, rechterbeen naar achteren met de knie gebogen, armen tegengesteld, kin iets
# omlaag. Scharnieren in graden met de schuif van de add-on; kogels (graden, richting) zoals de add-on ze draait.
VOOR, ACHTER = Vector((0, -1, 0)), Vector((0, 1, 0))
POSES = {
    "loop": ({"Left knee": 8.0, "Right knee": 38.0, "Left elbow": 20.0, "Right elbow": 42.0},
             {"Left hip": (25.0, VOOR), "Right hip": (25.0, ACHTER), "Left shoulder": (30.0, ACHTER),
              "Right shoulder": (30.0, VOOR), "Neck": (8.0, VOOR)}),
    # staande denker: rechterhand onder de kin (schouder 30 naar voren en binnen, elleboog 140), hoofd iets omlaag
    # naar de hand, gewicht op het rechterbeen, linkerknie licht gebogen en naar voren
    "denker": ({"Right elbow": 140.0, "Left elbow": 30.0, "Left knee": 28.0, "Right knee": 4.0},
               {"Right shoulder": (30.0, Vector((0.8, -1, 0))), "Left shoulder": (14.0, Vector((0, 0.6, 0))),
                "Neck": (18.0, Vector((-0.5, -1, 0))), "Left hip": (16.0, Vector((0.3, -1, 0))),
                "Right hip": (6.0, ACHTER)}),
}
POSE_SCHARNIER, POSE_KOGEL = POSES[os.environ.get("TP_POSE", "loop")]
meting["pose_naam"] = os.environ.get("TP_POSE", "loop")


def log(*a):
    print("[tekenpop]", *a, flush=True)


def figuur():
    if "figuur_uit_rig" not in dir(bpy.ops.click_joints):
        bpy.ops.extensions.package_install_files(filepath=M["ZIP"], repo="user_default", enable_on_install=True)
    arm, ob, _p = FL.laad_figuur("tekenpop", M["H"])
    return arm, ob


def spat(objs, seed=7):
    """Alleen voor de dynamische cover: elk deel vliegt verder van de romp weg, een beetje naar de camera toe en
    schuin gedraaid, alsof de pop net uiteenspat. Hoe verder van de romp in de keten, hoe verder en schever."""
    rnd = random.Random(seed)
    bpy.context.view_layer.update()

    def midden(o):
        vs = [o.matrix_world @ Vector(c) for c in o.bound_box]
        return sum(vs, Vector()) / 8
    romp = max(objs, key=lambda o: o.dimensions.x * o.dimensions.y * o.dimensions.z)
    c0 = midden(romp)
    cam_dir = Vector((math.sin(math.radians(34)), -math.cos(math.radians(34)), 0.1)).normalized()
    for o in objs:
        c = midden(o)
        d = c - c0
        if o is romp:
            q = Quaternion(Vector((0.3, 1, 0.2)).normalized(), math.radians(-9))
            o.matrix_world = Matrix.Translation(c) @ q.to_matrix().to_4x4() @ Matrix.Translation(-c) @ o.matrix_world
            continue
        ver = d.length
        r = d.normalized() if ver > 1e-3 else Vector((0, 0, 1))
        stap = r * (2 + 0.11 * ver) + cam_dir * rnd.uniform(-4, 12) + Vector((0, 0, rnd.uniform(-2, 3)))
        as_ = Vector((rnd.uniform(-1, 1), rnd.uniform(-1, 1), rnd.uniform(-0.4, 0.4))).normalized()
        q = Quaternion(as_, math.radians(rnd.uniform(7, 15) * (0.6 + ver / 110)))
        o.matrix_world = (Matrix.Translation(c + stap) @ q.to_matrix().to_4x4() @ Matrix.Translation(-c)
                          @ o.matrix_world)
    bpy.context.view_layer.update()


def main():
    laad = os.environ.get("TP_LAAD", "")
    if laad and os.path.exists(laad):   # alleen om lokaal sneller te proberen: figuur na Figure from rig uit een blend
        if "figuur_uit_rig" not in dir(bpy.ops.click_joints):
            bpy.ops.extensions.package_install_files(filepath=M["ZIP"], repo="user_default", enable_on_install=True)
        bpy.ops.wm.open_mainfile(filepath=laad)
        naam = next(o.get("cj_figuur") for o in bpy.context.scene.objects if o.get("cj_figuur"))
        delen = M["zichtbaar"](naam)
        meting.update(json.loads(bpy.context.scene.get("tp_meting", "{}")))
    else:
        arm, ob = figuur()
        naam, delen = M["maak_gewrichten"](arm, ob)
        if os.environ.get("TP_BEWAAR"):
            bpy.context.scene["tp_meting"] = json.dumps(meting)
            bpy.ops.wm.save_as_mainfile(filepath=os.environ["TP_BEWAAR"])
    meting["aantal_gewrichten"] = len(meting.get("gewrichten", []))
    if SHOT == "proef":
        json.dump(meting, open(os.path.join(UIT, f"{STIJL}-proef.json"), "w"), indent=1, ensure_ascii=False)
        print(f"PROEF tekenpop gewrichten={meting['aantal_gewrichten']} delen={meting['delen']}", flush=True)
        return
    T.materialen(delen, rand_mm=float(os.environ.get("TP_RAND", "0.35")))
    inst = bpy.context.scene.click_joints
    try:
        bpy.context.window_manager.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    inst.uit_elkaar = False
    M["U"]().zet_alle(bpy.context.scene)
    objs = M["zichtbaar"](naam)
    if SHOT in ("staand", "pop169", "dyn169"):
        meting["pose"] = {n: M["buig"](n, g) for n, g in POSE_SCHARNIER.items()}
        meting["kogels"] = M["pose_kogels"](objs, POSE_KOGEL)
    # staand: een fractie (0,45 keer) van de Exploded view van de add-on, zodat je het messing van elk gewricht ziet
    keer = {"staand": 0.45, "uit": 2.3, "pop169": 1.0, "dyn169": 1.1}.get(SHOT, 0.0)
    meting["uit_elkaar_keer"] = keer
    meting["ouders"] = M["pose_en_uiteen"](objs, keer)
    objs = M["zichtbaar"](naam)
    if SHOT == "dyn169":
        spat(objs)
        meting["spat"] = "alleen voor het beeld: delen verder uit elkaar en schuin gedraaid (seed 7)"
    M["studio"](M["laagste"](objs))
    kader = M["kader"]
    if SHOT == "staand":
        M["render_instellingen"](1600, 1600)
        kader(objs, float(os.environ.get("TP_HOEK", "50")), 4, (0.16, 0.84), 0.41, lens=60, ymid=0.46)
    elif SHOT == "uit":
        M["render_instellingen"](1600, 1600)
        kader(objs, 26, 8, (0.12, 0.88), 0.44, lens=60, ymid=0.48)
    elif SHOT == "pop169":
        M["render_instellingen"](2560, 1440)
        kader(objs, 50, 6, (0.55, 0.97), 0.53, lens=70, ymid=0.43)
    elif SHOT == "dyn169":
        M["render_instellingen"](2560, 1440)
        # het kader om romp, hoofd, bovenarmen en dijen; handen en voeten vliegen deels buiten de rand
        kern = [o for o in objs if o.get("cj_naam") in ("Neck", "Left shoulder", "Right shoulder", "Left hip",
                                                        "Right hip") or o.get("cj_deel") != "B"]
        kader(kern or objs, 40, 12, (0.50, 1.02), 0.61, lens=45, ymid=0.36)
    meting["objecten"] = sorted({(o.get("cj_naam") or o.name) for o in objs})[:40]
    M["render"](SHOT)
    json.dump(meting, open(os.path.join(UIT, f"{STIJL}-{SHOT}.json"), "w"), indent=1, ensure_ascii=False)


main()
