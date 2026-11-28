"""Pro 1.2.10, issue 410 (kopersreis Iris 28 nov): kogelpreset na Shift + rechtsklik, aangeroepen vanuit test_betaald.

Shift + rechtsklik zet de cursor op de huid met de Z-as naar de kijker. Eerst zei Shoulder daar "Too thin here for a
ball joint" op een arm van 36 mm. Nagespeeld op een staaf (straal 18 mm, lengte 100, lid langs wereld-X), kijk van
voren (+Y). De achtergrond heeft geen 3D-weergave, dus gewricht.kijk_regio geeft hier een vaste kijk terug.
(a) Shoulder, cursor op de voorkant bij x = 20: kogel geplaatst (twee delen, niet rood), as langs de staaf (< 3 graden),
    gericht naar het eind (+X, deel B is het lid), snijpunt in het midden (< 0,5 mm van de as);
(b) Hip op dezelfde manier: geplaatst;
(c) cursor binnen de staaf: punt en as blijven zoals in de kern (kijkrichting), dus niets veranderd voor wie de
    cursor zelf in het lid zet."""
import math
import sys

import bpy
from mathutils import Euler, Vector

import figuren
from hulp_scharnier import cursor as _cursor

KIJK = Vector((0, 1, 0))


class _Kijk:
    view_rotation = Euler((math.pi / 2, 0, 0)).to_quaternion()  # vooraanzicht: kijkt naar +Y, omhoog +Z


def _staaf():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = 0.2
    inst.as_bron = "KIJK"
    inst.kogel_auto = True
    staaf = figuren.staaf("arm", 18.0, 100.0)
    figuren.maak_actief(staaf)
    return staaf


def _huidpunt(x):
    hit = bpy.context.scene.ray_cast(bpy.context.evaluated_depsgraph_get(), Vector((x, -60.0, 0.37)), KIJK)
    return hit[1] if hit[0] else Vector((x, -18.0, 0.37))


def _preset(deel):
    try:
        return bpy.ops.click_joints.plaats_preset(deel=deel)
    except RuntimeError as fout:
        print(f"[cj-betaald] melding: {fout}")
        return {"CANCELLED"}


def toets(stap, eigen):
    gewricht = sys.modules[eigen + ".gewricht"]
    oud = gewricht.kijk_regio
    gewricht.kijk_regio = lambda _context: _Kijk()
    naar_kijker = (Vector((1, 0, 0)), Vector((0, 0, 1)), Vector((0, -1, 0)))  # cursor-Z naar de kijker
    try:
        for deel in ("SHOULDER", "HIP"):
            _staaf()
            p = _huidpunt(20.0)
            _cursor(p, *naar_kijker)
            uitslag = _preset(deel)
            a, b = bpy.data.objects.get("arm_A"), bpy.data.objects.get("arm_B")
            ok = uitslag == {"FINISHED"} and a is not None and b is not None and b.get("cj_passing") != "rood"
            stap(f"kogel {deel} na Shift-klik op de huid: geplaatst", ok,
                 f"{uitslag} punt {tuple(round(c, 2) for c in p)} passing {b.get('cj_passing') if b else None}")
            if not ok:
                continue
            as_ = Vector(b["cj_as"]).normalized()
            hoek = math.degrees(math.acos(min(1.0, as_.x)))
            sp = Vector(b["cj_snijpunt"])
            stap(f"kogel {deel}: as langs het lid naar het eind (< 3 graden van +X)", hoek < 3.0,
                 f"as {tuple(round(c, 3) for c in as_)}, bijgesteld '{b.get('cj_bijgesteld', '')}'")
            stap(f"kogel {deel}: snijpunt in het midden van het lid (< 0.5 mm)", math.hypot(sp.y, sp.z) < 0.5,
                 f"snijpunt {tuple(round(c, 2) for c in sp)}")
            stap(f"kogel {deel}: deel B is het eind van het lid", b.dimensions.x < a.dimensions.x,
                 f"A {tuple(round(c) for c in a.dimensions)} B {tuple(round(c) for c in b.dimensions)}")
        _staaf()
        binnen = Vector((20.0, -4.0, 3.0))
        _cursor(binnen, *naar_kijker)
        uitslag = _preset("SHOULDER")
        b = bpy.data.objects.get("arm_B") or next((o for o in bpy.data.objects if o.name.endswith("_joint_too_thin")), None)
        as_ = Vector(b["cj_as"]).normalized() if b is not None and "cj_as" in b else Vector()
        sp = Vector(b["cj_snijpunt"]) if b is not None and "cj_snijpunt" in b else Vector((1e9, 0, 0))
        stap("kogel met de cursor binnen het lid: punt en as zoals de kern (kijkrichting)",
             b is not None and (as_ - KIJK).length < 1e-6 and (sp - binnen).length < 0.1 and not b.get("cj_bijgesteld"),
             f"{uitslag} as {tuple(round(c, 3) for c in as_)} snijpunt {tuple(round(c, 2) for c in sp)}")
    finally:
        gewricht.kijk_regio = oud
