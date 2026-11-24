"""Pro 1.2.7: scharnier na Shift + rechtsklik (melding Regisseur 24 nov, clip 3), aangeroepen vanuit toetsen_scharnier.

Shift + rechtsklik zet de cursor op de huid met de Z-as naar de kijker (keymap orientation VIEW). Nagespeeld op de
staaf (straal 5 mm, lid langs wereld-X), kijk van voren (+Y), omhoog +Z:
(a) cursor-Z naar de kijker: scharnier geplaatst, lidas uit het figuur (binnen 3 graden van X), snijpunt in het
    midden van de staaf (binnen 0,3 mm van de X-as);
(b) cursor recht (Z langs het lid) maar op de huid: geplaatst en gecentreerd;
(c) zelfde cursor als (a) maar binnen de staaf: oude weigering blijft (zie toetsen_kijk)."""
import math

import bpy
from mathutils import Vector

import figuren
from hulp_scharnier import cursor as _cursor

KIJK, OMHOOG = Vector((0, 1, 0)), Vector((0, 0, 1))


def _staaf():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = 0.2
    inst.as_bron = "KIJK"
    staaf = figuren.staaf("staaf", 5.0)
    figuren.maak_actief(staaf)
    return staaf


def _huidpunt(staaf):
    """Punt op de voorkant van de staaf (zoals Shift + rechtsklik), niet precies op een hoekpunt."""
    hit = bpy.context.scene.ray_cast(bpy.context.evaluated_depsgraph_get(), Vector((2.0, -20.0, 0.37)), KIJK)
    return hit[1] if hit[0] else Vector((2.0, -5.0, 0.37))


def _plaats():
    try:
        return bpy.ops.click_joints.plaats_scharnier(stand="115", kijk_richting=tuple(KIJK), kijk_omhoog=tuple(OMHOOG))
    except RuntimeError as fout:
        print(f"[cj-betaald] melding: {fout}")
        return {"CANCELLED"}


def toets(stap, eigen):
    naar_kijker = (Vector((1, 0, 0)), Vector((0, 0, 1)), Vector((0, -1, 0)))  # X, Y, Z van de cursor (Z naar ons)
    recht = (Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))         # Z langs het lid
    for naam, assen in (("cursor-Z naar de kijker", naar_kijker), ("cursor recht op de huid", recht)):
        staaf = _staaf()
        p = _huidpunt(staaf)
        _cursor(p, *assen)
        uitslag = _plaats()
        b = bpy.data.objects.get("staaf_B")
        ok = uitslag == {"FINISHED"} and b is not None and bpy.data.objects.get("staaf_A") is not None
        stap(f"Shift-klik {naam}: scharnier geplaatst", ok, f"{uitslag} punt {tuple(round(c, 3) for c in p)}")
        if not ok:
            continue
        lid = Vector(b["cj_as"]).normalized()
        hoek = math.degrees(math.acos(min(1.0, abs(lid.x))))
        sp = Vector(b["cj_snijpunt"])
        midden = math.hypot(sp.y, sp.z)
        stap(f"Shift-klik {naam}: lidas langs de staaf (< 3 graden)", hoek < 3.0, f"hoek {hoek:.2f}")
        stap(f"Shift-klik {naam}: snijpunt in het midden (< 0.3 mm)", midden < 0.3,
             f"afstand tot de as {midden:.3f} mm, bijgesteld '{b.get('cj_bijgesteld', '')}'")
    staaf = _staaf()
    n_v = len(staaf.data.vertices)
    _cursor(Vector((2.0, -1.0, 0.37)), *naar_kijker)
    uitslag = _plaats()
    stap("cursor-Z naar de kijker binnen de staaf: weigering blijft", uitslag == {"CANCELLED"}
         and len(staaf.data.vertices) == n_v and bpy.data.objects.get("staaf_B") is None, str(uitslag))
