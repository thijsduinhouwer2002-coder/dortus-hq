"""Pro 1.2.3 (Betrouwbaarheid, 23 nov): het omhulsel H van `een_lid` als één schone, gesloten vorm.

Oorzaak van "Figure from rig slaat soms een gewricht over" (meting tak claude/betrouwbaar-rig, run 45253697551,
GEZIEN): H is het lid een fractie groter (elk punt langs zijn normaal naar buiten) samen met een convex omhulsel rond
het snijvlak. Op een voxelfiguur snijdt die verschoven huid zichzelf in elke holte (100 tot 300 paren driehoeken),
en lukt de Exact-vereniging van omhulsel en lid niet, dan blijven het twee losse schillen door elkaar ("los", 4263
paren). Een boolean met zo'n vorm is niet bepaald: Manifold (Blender 4.5+) gaf op de robot een heup waarvan A en B in
rust 9271 paren driehoeken overlappen ("blocked") of één open rand, per processor anders (daarom CI 8 en lokaal 9);
Exact zonder Self Intersection (4.2) gaf lege of open delen. Een vlak dat een fractie verschuift of draait helpt
niet (zelfde meting, alle varianten slecht).

Oplossing: de twee schillen samen door een voxel-remesh (OpenVDB maakt van overlappende of zichzelf snijdende
schillen één gesloten huid zonder zelfdoorsnijding). Daarna controleren dat H het lid en het omhulsel nog bevat
(punten van de huid, `m` naar binnen, moeten binnen H liggen). Lukt dat niet, dan de oude weg (`een_lid._samen`).
Wanneer: met Exact (4.2) altijd, met Manifold alleen als de oude vereniging "los" gaf (zie `samen_schoon`).
Het gratis deel blijft gelijk (toets_zips.py): Pro zet `een_lid._samen` bij het registreren op deze functie.
"""
import math

import bmesh
import bpy
from mathutils import Matrix
from mathutils.bvhtree import BVHTree

from .. import een_lid as _l

AAN = [True]          # voor de meting: False geeft precies de oude weg
MAX_VLAKKEN = 250000  # voxelmaat zo dat H hooguit ±zoveel vlakken krijgt (snelheid van de booleans)
# Issue 14 (25 nov): met Exact (4.2) vroeg de INTERSECT met een H van 214.150 vlakken (voxel 0,14 mm, de ondergrens
# 0,5 m) bij de elleboog van de Rigify-figuur meer dan 15 GB (CI run 45510400380, lokaal meer dan 5 GB in 10 s, GEZIEN).
# Exact rekent met exacte getallen en zijn geheugen groeit met het aantal driehoeken. Daarom voor Exact een eigen grens,
# en die gaat voor de ondergrens 0,5 m: liever een wat grovere H (de controle hieronder kijkt of het lid erin zit) dan
# een Blender die vastloopt. Gemeten op toetsen_rigify in 4.2.23 (lokaal, GEZIEN): 214.150 vlakken meer dan 5 GB en
# gestopt; grens 60.000 piek 4,6 GB, 122 s; grens 30.000 piek 2,5 GB, 85 s, beide KLAAR 0 FOUT.
MAX_VLAKKEN_EXACT = 30000
# Hooguit dit deel van de controlepunten van het lid mag buiten H vallen. Niet 0: in een holte van de figuur vouwt de
# verschoven huid om, en daar ligt het controlepunt (huid min m langs de nieuwe normaal) niet meer op de echte huid
# (run 45255097554: 0,2 tot 1,9 procent, ook waar de snede daarna goed was).
BUITEN_MAX = 0.02
_oud = [None]


def _oppervlak(bm):
    return sum(f.calc_area() for f in bm.faces)


def _binnen_punten(bm, m, n=1500):
    """Punten van de verschoven huid, `m` terug naar binnen: daar lag de echte huid (die moet in H)."""
    bm.normal_update()
    vs = bm.verts[:]
    stap = max(1, len(vs) // n)
    return [v.co - v.normal * m for v in vs[::stap]]


def _buiten_deel(bvh, punten):
    buiten = 0
    for p in punten:
        plek, normaal, _i, _a = bvh.find_nearest(p)
        if plek is None or (p - plek).dot(normaal) > 0:
            buiten += 1
    return buiten / max(1, len(punten))


def voxel_h(hb, lb, frame, hulp, m):
    """(object H, gegevens) of (None, gegevens). hb en lb blijven onaangeroerd (de oude weg kan ze nog nodig hebben)."""
    a, b = hb.copy(), lb.copy()
    a.transform(frame)
    b.transform(frame)
    controle = _binnen_punten(b, m)  # het lid; het omhulsel rond het vlak alleen voor het verslag
    controle_om = _binnen_punten(a, m)
    opp = _oppervlak(a) + _oppervlak(b)
    from ..gewricht import solver_naam
    if solver_naam() == "EXACT":
        v = math.sqrt(opp / MAX_VLAKKEN_EXACT)  # issue 14: geen ondergrens 0,5 m, anders weer ±200.000 vlakken
    else:
        v = max(0.5 * m, math.sqrt(opp / MAX_VLAKKEN))
    kaart = {x: a.verts.new(x.co) for x in b.verts}
    for f in b.faces:
        try:
            a.faces.new([kaart[x] for x in f.verts])
        except ValueError:
            pass
    b.free()
    me = bpy.data.meshes.new("cj_een_lid_bron")
    a.to_mesh(me)
    a.free()
    tmp = bpy.data.objects.new("cj_een_lid_bron", me)
    hulp.objects.link(tmp)
    mod = tmp.modifiers.new("cj_voxel", "REMESH")
    mod.mode, mod.voxel_size, mod.adaptivity = "VOXEL", v, 0.0
    dg = bpy.context.evaluated_depsgraph_get()
    nm = bpy.data.meshes.new_from_object(tmp.evaluated_get(dg))
    bpy.data.objects.remove(tmp)
    bpy.data.meshes.remove(me)
    gegevens = {"h_voxel": round(v, 4), "h_vlakken": len(nm.polygons)}
    from ..gesloten import is_gesloten
    ok, _fout = is_gesloten(nm)
    if ok:
        bm = bmesh.new()
        bm.from_mesh(nm)
        bvh = BVHTree.FromBMesh(bm)
        buiten = _buiten_deel(bvh, controle)
        gegevens["h_buiten_om"] = round(_buiten_deel(bvh, controle_om), 4)
        bm.free()
        gegevens["h_buiten"] = round(buiten, 4)
        ok = buiten <= BUITEN_MAX
    if not ok:
        bpy.data.meshes.remove(nm)
        return None, gegevens
    nm.name = "cj_een_lid"
    h = bpy.data.objects.new("cj_een_lid", nm)
    hulp.objects.link(h)
    h.hide_set(True)
    return h, gegevens


def samen_schoon(hb, lb, frame, hulp, lid_dicht):
    """Vervangt `een_lid._samen`.

    Exact (Blender voor 4.5): altijd eerst H als voxelvorm. Exact zonder Self Intersection kan niets met een H die
    zichzelf snijdt (lege of open delen), en de Exact-vereniging laat die zelfdoorsnijding staan.
    Manifold (4.5+): eerst de oude weg. Alleen als de vereniging mislukt ("los", twee schillen door elkaar) de
    voxelvorm. Reden (run 45264302449, GEZIEN): met voxel-H altijd verloor de rechterknie van de Meshy-knight 8 tot 9%
    van de punten in plaats van 5,6% (de voxelvorm vult holtes en neemt dan wat stof naast het lid mee), en op lichte
    figuren kostte het tijd; met Manifold gaf een "samen"-H in de hele nulmeting geen enkele slechte snede.
    """
    if not AAN[0]:
        return _oud[0](hb, lb, frame, hulp, lid_dicht)
    m = float(_l.LAATSTE.get("marge") or 0.0)
    from ..gewricht import solver_naam
    if solver_naam() == "EXACT":
        h, gegevens = voxel_h(hb, lb, frame, hulp, m) if m > 0 else (None, {})
        _l.LAATSTE.update(gegevens)
        if h is not None:
            _l.LAATSTE["h_soort"] = "voxel"
            return h
        return _oud[0](hb, lb, frame, hulp, lid_dicht)
    h = _oud[0](hb, lb, frame, hulp, lid_dicht)  # zet hb en lb om naar wereldcoordinaten
    if _l.LAATSTE.get("h_soort") != "los" or m <= 0:
        return h
    nieuw, gegevens = voxel_h(hb, lb, Matrix.Identity(4), hulp, m)
    _l.LAATSTE.update(gegevens)
    if nieuw is None:
        return h
    me = h.data
    bpy.data.objects.remove(h)
    if me.users == 0:
        bpy.data.meshes.remove(me)
    _l.LAATSTE["h_soort"] = "voxel"
    return nieuw


def register():
    if _oud[0] is None:
        _oud[0] = _l._samen
        _l._samen = samen_schoon


def unregister():
    if _oud[0] is not None:
        if _l._samen is samen_schoon:
            _l._samen = _oud[0]
        _oud[0] = None
