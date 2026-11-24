"""Toets (Pro 1.2.8, issue 14): het scharnier levert nooit een deel met een los stuk af.

CI 4.2.23 op army_man (run 45488637167, GEZIEN): de Exact-boolean gaf een gesloten maar half gelukt scharnier,
deel B in twee stukken (voet los) en "no end stop was found". Die boolean is niet elke keer gelijk, dus hier wordt
de fout nagebootst: vorm.snij geeft deel B een extra los blok. Eisen:
1. los blok van 4 mm in B: geweigerd ("loose piece"), de staaf onveranderd, geen delen.
2. dun kruimeltje van 0,05 mm in B (zoals de boolean soms achterlaat): opgeruimd, scharnier geplaatst, A en B elk één stuk.
3. bron met een eigen los onderdeel (een oog ver van de snede): scharnier geplaatst, samen precies één stuk meer.
Aangeroepen vanuit toetsen_scharnier.py.
"""
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

import figuren
from hulp_scharnier import cursor as _cursor


def _blok(ob, midden, maat):
    """Voeg een gesloten blok (maat = (x, y, z) in mm) als los stuk aan de mesh van ob toe."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    m = Matrix.Translation(ob.matrix_world.inverted() @ Vector(midden)) @ Matrix.Diagonal((*maat, 1.0))
    bmesh.ops.create_cube(bm, size=1.0, matrix=m)
    bm.to_mesh(ob.data)
    bm.free()
    ob.data.update()


def _scene(oog=False):
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = 0.2
    inst.as_bron = "CURSOR"
    staaf = figuren.staaf("staaf", 5.0)
    if oog:
        _blok(staaf, (17.0, 0.0, 9.0), (3.0, 3.0, 3.0))
    figuren.maak_actief(staaf)
    _cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    return staaf


def toets(stap, eigen):
    vorm = sys.modules[eigen + ".betaald.scharnier_vorm"]
    zwaai = sys.modules[eigen + ".betaald.scharnier_zwaai"]
    orig = vorm.snij

    def met_extra(midden, maat):
        def snij(*a, **k):
            deel_a, deel_b = orig(*a, **k)
            _blok(deel_b, midden, maat)
            return deel_a, deel_b
        return snij

    # 1. Een echt los stuk (zoals de voet van army_man): weigeren, niets veranderd.
    staaf = _scene()
    n_voor = len(staaf.data.vertices)
    vorm.snij = met_extra((14.0, 0.0, 12.0), (4.0, 4.0, 4.0))
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    finally:
        vorm.snij = orig
    staaf = bpy.data.objects.get("staaf")
    reden = str(staaf.get("cj_weigering", "")) if staaf else ""
    stap("los stuk in B: geweigerd", uitslag == {"CANCELLED"} and "loose piece" in reden.lower(), f"{uitslag} {reden!r}")
    stap("los stuk in B: staaf onveranderd en zichtbaar, geen delen",
         staaf is not None and len(staaf.data.vertices) == n_voor and staaf.visible_get()
         and not any(o.get("cj_deel") for o in bpy.data.objects), f"{n_voor} punten")

    # 2. Een dun kruimeltje mag geen scharnier kosten.
    _scene()
    vorm.snij = met_extra((14.0, 0.0, 12.0), (2.0, 2.0, 0.05))
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    finally:
        vorm.snij = orig
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    st = (zwaai.stukken(a.data), zwaai.stukken(b.data)) if a and b else None
    stap("dun kruimeltje in B: opgeruimd, scharnier geplaatst, A en B elk één stuk",
         uitslag == {"FINISHED"} and st == (1, 1), f"{uitslag} stukken {st}")

    # 3. Een bron met een eigen los onderdeel blijft gewoon werken.
    staaf = _scene(oog=True)
    n_bron = zwaai.stukken(staaf.data)
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    st = (zwaai.stukken(a.data), zwaai.stukken(b.data)) if a and b else None
    stap("bron met een los oog: scharnier geplaatst, samen één stuk meer dan de bron",
         uitslag == {"FINISHED"} and st is not None and sum(st) == n_bron + 1, f"{uitslag} bron {n_bron} stukken {st}")
