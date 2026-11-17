"""Zwaairuimte van een scharnier (Pro 1.1, run 25): haal uit deel A weg waar deel B doorheen zwaait.

Waarom: op een echte figuur botst het vlees van de onderarm op dat van de bovenarm voor de eindstop bereikt is.
Op de MakeHuman-elleboog gaf rig-stop 115 maar 82 graden (rig-stop 90 gaf 55). Dan klopt de belofte "elk
gewricht stopt waar je rig stopt" niet.

Hoe: deel B wordt in stappen gedraaid (van het gemeten bereik tot net onder de stand) en telkens van A
afgetrokken. Twee details, beide gemeten op de MakeHuman-elleboog (e2e/proef_zwaai.py):
- Een bol rond het draaipunt (naadstraal plus 1 mm) blijft buiten de uitsnede, zodat het klikmechaniek
  (knokkel, tong, wangen, eindstop) heel blijft.
- B wordt eerst iets dikker gemaakt (OPZET, kleiner dan de speling). Zonder dat liggen de nieuwe snijvlakken
  van A precies op B en telt de beweegproef dat als botsing (bleef op 100 hangen). Met 0,15 mm: 115.
  Met meer dan de speling (0,3 bij speling 0,2) snijdt de dikkere tong in de wangen en breekt A.

Veilig: lukt het niet (A niet meer gesloten, A in stukken, of het bereik wordt niet groter), dan krijgt A zijn
oude vorm terug en blijft het eerlijk gemeten bereik staan."""
import math

import bmesh
import bpy
import numpy as np
from mathutils import Matrix, Vector

from ..gesloten import is_gesloten
from . import scharnier_beweeg as beweeg

STAP = 10.0        # graden tussen twee uitsneden
MARGE = 2.0        # pas iets doen als het gemeten bereik meer dan dit onder de stand ligt
OPZET_MM = 0.15    # hoeveel B dikker wordt, nooit meer dan 3/4 van de speling
KERN_MM = 1.0      # bol rond het draaipunt: naadstraal plus dit


def hoeken(voor, stand):
    """De standen van B waarop uitgesneden wordt: vanaf het gemeten bereik in stappen tot net onder de stand."""
    uit, g = [], math.floor(voor)
    while g < stand - 0.5:
        uit.append(float(g))
        g += STAP
    uit.append(stand - 0.5)
    return uit


def stukken(me):
    """Aantal losse stukken in een mesh (vertices die via randen samenhangen)."""
    n = len(me.vertices)
    if n == 0:
        return 0
    ouder = list(range(n))

    def wortel(i):
        while ouder[i] != i:
            ouder[i] = ouder[ouder[i]]
            i = ouder[i]
        return i
    for e in me.edges:
        a, b = wortel(e.vertices[0]), wortel(e.vertices[1])
        if a != b:
            ouder[a] = b
    return len({wortel(i) for i in range(n)})


def _gebakken(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    return bpy.data.meshes.new_from_object(ob.evaluated_get(dg))


def _aftrekken(doel, gereedschap, solver):
    """doel = doel min gereedschap (Boolean-modifier, gebakken); geeft de oude mesh terug om op te ruimen."""
    m = doel.modifiers.new("cj_zwaai", "BOOLEAN")
    m.operation, m.object, m.solver = "DIFFERENCE", gereedschap, solver
    me = _gebakken(doel)
    doel.modifiers.remove(m)
    oud = doel.data
    doel.data = me
    return oud


def uitsnijden(a, b, punt, h, buig, lid, bol, stand, voor, achter, rn, s, u, solver, hulp):
    """Snijdt de zwaairuimte van B uit A. Geeft (voor, achter, gedaan) terug: het nieuwe gemeten bereik, of
    het oude als er niets te doen was of als het niet lukte (dan is A ongewijzigd)."""
    if voor is None or beweeg.geen_stop(voor) or voor >= stand - MARGE:
        return voor, achter, False
    punt = Vector(punt)
    voor_as = Vector(lid).cross(Vector(buig)).normalized()
    opzet = min(OPZET_MM * u, 0.75 * s)
    # B dikker (langs de normaal) en zonder de kern rond het draaipunt; de kern is rond, dus dit hoeft maar
    # één keer, daarna alleen draaien.
    bm = bmesh.new()
    bm.from_mesh(b.data)
    bm.transform(b.matrix_world)
    bm.normal_update()
    for v in bm.verts:
        v.co += v.normal * opzet
    me_t = bpy.data.meshes.new("cj_zwaai_b")
    bm.to_mesh(me_t)
    bm.free()
    t = bpy.data.objects.new("cj_zwaai_b", me_t)
    hulp.objects.link(t)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=48, v_segments=24, radius=rn + KERN_MM * u,
                              matrix=Matrix.Translation(punt))
    me_k = bpy.data.meshes.new("cj_zwaai_kern")
    bm.to_mesh(me_k)
    bm.free()
    kern = bpy.data.objects.new("cj_zwaai_kern", me_k)
    hulp.objects.link(kern)
    oud_t = _aftrekken(t, kern, solver)
    bpy.data.meshes.remove(oud_t)
    kern.hide_set(True)
    t.hide_set(True)

    reserve = a.data.copy()
    oude_meshes = []
    try:
        for g in hoeken(voor, stand):
            t.matrix_world = (Matrix.Translation(punt) @ Matrix.Rotation(math.radians(g), 4, voor_as)
                              @ Matrix.Translation(-punt))
            oude_meshes.append(_aftrekken(a, t, solver))
    except RuntimeError:
        a.data = reserve
        return voor, achter, False
    finally:
        for me in oude_meshes:
            if me is not reserve and me.users == 0:
                bpy.data.meshes.remove(me)
    nieuw_voor, nieuw_achter = beweeg.bereik(a, b, punt, h, buig, lid, bol)
    goed = (is_gesloten(a.data)[0] and stukken(a.data) == stukken(reserve) and nieuw_voor is not None
            and nieuw_voor > voor + 0.5 and abs((nieuw_achter or 0) - (achter or 0)) < 0.5)
    if not goed:
        kapot = a.data
        a.data = reserve
        if kapot.users == 0:
            bpy.data.meshes.remove(kapot)
        return voor, achter, False
    if reserve.users == 0:
        bpy.data.meshes.remove(reserve)
    return nieuw_voor, nieuw_achter, True
