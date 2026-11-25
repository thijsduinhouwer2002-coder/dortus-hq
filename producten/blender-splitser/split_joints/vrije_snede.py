"""Free cut: a plane you move, turn and scale yourself, that cuts one piece in two, only inside its rectangle.

Why: the grid cuts go straight through the whole model. A free cut takes off an arm at the shoulder, at any
angle, and leaves the rest of the piece alone. How (ontwerp.md deel 12):
- the plane is an object "Free cut" (sj_vrij = name of the piece), its local Z is the cut direction;
- everything of the piece on the +Z side of the plane and inside the rectangle becomes a new piece: the piece
  times a box over the rectangle that reaches past the piece on that side;
- if that box touches the piece with one of its side walls, the rectangle is too small (or something else of
  the piece sits on that side): we refuse and say so, instead of making a cut nobody asked for;
- a cut through an existing pin hole is refused too;
- pins and numbers come from the same planner as the grid cuts (verbind_3d.plan_alles): the piece is turned so
  the plane lies flat at z = 0, planned as two cells along Z, and the holes and numbers are turned back."""
import json
import math

import bpy
import numpy as np
from mathutils import Matrix, Vector

from . import controle, eigenschappen, kleuren, splitsen, uit_elkaar, verbind_3d, vormen
from .eigenschappen import bed, eenheid_per_mm

NAAM = "Free cut"
WAND_TOL_MM = 0.002  # a face this close to a side wall of the box lies on that wall
WAND_OPP_MM2 = 0.05  # more wall area than this on the new piece: the box touched the piece at its side


def stuk_van(context):
    """(piece, free cut object) for the active object, or (None, None)."""
    ob = context.active_object
    if ob is None:
        return None, None
    if ob.get("sj_vrij"):
        stuk = bpy.data.objects.get(ob["sj_vrij"])
        return (stuk, ob) if stuk is not None and stuk.get("sj_stuk") else (None, ob)
    if ob.get("sj_stuk"):
        for o in context.scene.objects:
            if o.get("sj_vrij") == ob.name:
                return ob, o
        return ob, None
    return None, None


def mesh_lokaal_mm(ob, u):
    """(points N x 3 in mm, triangles) of the mesh data itself (pieces have an identity matrix)."""
    me = ob.data
    me.calc_loop_triangles()
    co = np.empty(len(me.vertices) * 3)
    me.vertices.foreach_get("co", co)
    tri = np.empty(len(me.loop_triangles) * 3, dtype=np.int64)
    me.loop_triangles.foreach_get("vertices", tri)
    return co.reshape(-1, 3) / u, tri.reshape(-1, 3)


def kader(stuk, snede, u):
    """Frame of the free cut in the mesh space of the piece, in mm: (R 3x3 numpy with columns e1 e2 n,
    origin o, half width a, half height b). Works with the exploded view on (matrix of the piece)."""
    m = stuk.matrix_world.inverted() @ snede.matrix_world
    loc, rot, sca = m.decompose()
    ps = [Vector(v.co) for v in snede.data.vertices]
    mn = Vector([min(p[i] for p in ps) for i in range(3)])
    mx = Vector([max(p[i] for p in ps) for i in range(3)])
    midden = (mn + mx) / 2.0
    o = m @ midden
    R = np.array(rot.to_matrix())
    a = (mx.x - mn.x) / 2.0 * abs(sca.x) / u
    b = (mx.y - mn.y) / 2.0 * abs(sca.y) / u
    return R, np.array(o) / u, a, b


def door_gat(gaten, R, o, a, b, wand):
    """First existing hole that the free cut goes through (or comes closer to than the wall), else None.
    Measured on points around the hole wall and at both ends, in the frame of the cut."""
    for g in gaten:
        n, e1, e2 = controle.gat_assen(g)
        p = Vector(g["p"])
        lok = []
        for z in (-g["diepte"], 0.0, g["diepte"]):
            for k in range(16):
                h = 2 * math.pi * k / 16
                q = p + n * z + (e1 * math.cos(h) + e2 * math.sin(h)) * g["r_gat"]
                lok.append((np.array(q) - o) @ R)
        lok = np.array(lok)
        binnen = (np.abs(lok[:, 0]) <= a + wand) & (np.abs(lok[:, 1]) <= b + wand)
        if binnen.any() and lok[binnen, 2].min() < wand and lok[binnen, 2].max() > -wand:
            return g
    return None


def wand_vlak(stuk_ruw, R, o, a, b, u):
    """Area (mm2) of the faces of the new piece that lie on a side wall of the box (|x| = a or |y| = b)."""
    co = np.array([tuple(v.co) for v in stuk_ruw.data.vertices]) / u
    lok = (co - o) @ R
    opp = 0.0
    for f in stuk_ruw.data.polygons:
        idx = list(f.vertices)
        x, y = lok[idx, 0], lok[idx, 1]
        if np.all(np.abs(np.abs(x) - a) < WAND_TOL_MM) or np.all(np.abs(np.abs(y) - b) < WAND_TOL_MM):
            opp += f.area / (u * u)
    return opp


def _getal(x):
    """numpy numbers (float32 in Blender 5.3) to plain Python for json."""
    if hasattr(x, "tolist"):
        return x.tolist()
    raise TypeError(f"Object of type {type(x).__name__} is not JSON serializable")


def _json(obj):
    return json.dumps(obj, default=_getal)


def naar_wereld(item, R, o):
    """A hole or label planned in the frame of the cut, back in the mesh space of the piece."""
    uit = dict(item)
    uit["p"] = [float(x) for x in R @ np.array(item["p"], dtype=float) + o]
    uit["n"] = [float(x) for x in R[:, 2]]
    uit["as"] = -1
    uit["vrij"] = True
    if item.get("richting") is not None:
        uit["richting"] = [float(x) for x in R @ np.array(item["richting"], dtype=float)]
    return uit


def maak_vrije_snede(context, stuk):
    """Adds a free cut plane through the middle of the piece, a bit larger than the piece, lying flat."""
    scene = context.scene
    u = eenheid_per_mm(scene)
    pts = np.array([tuple(stuk.matrix_world @ v.co) for v in stuk.data.vertices]) / u
    lo, hi = pts.min(axis=0), pts.max(axis=0)
    half = 0.6 * max(hi[0] - lo[0], hi[1] - lo[1]) + 2.0
    me = bpy.data.meshes.new(NAAM)
    me.from_pydata([(-half * u, -half * u, 0), (half * u, -half * u, 0), (half * u, half * u, 0),
                    (-half * u, half * u, 0)], [], [(0, 1, 2, 3)])
    ob = bpy.data.objects.new(NAAM, me)
    from .snedes import collectie
    collectie(scene).objects.link(ob)
    ob.location = Vector((lo + hi) / 2.0) * u
    ob["sj_vrij"] = stuk.name
    ob.display_type = "WIRE"
    ob.show_in_front = True
    ob.hide_render = True
    ob.color = (0.85, 0.35, 0.9, 1.0)
    return ob


def snijd(context, stuk, snede, report):
    """Cuts the piece along the free cut. Returns (piece A, new piece B, new pins object) or None."""
    scene = context.scene
    inst = scene.split_joints
    u = eenheid_per_mm(scene)
    R, o, a, b = kader(stuk, snede, u)
    if a < 1.0 or b < 1.0:
        report({"ERROR"}, "The free cut is too small: scale it up (S) so it covers the part you want to cut off")
        return None
    alle = uit_elkaar.stukken(scene)
    with uit_elkaar.echte_plek(alle):
        return _snijd(context, scene, inst, u, stuk, snede, R, o, a, b, alle, report)


def _snijd(context, scene, inst, u, stuk, snede, R, o, a, b, alle, report):
    punten, tri = mesh_lokaal_mm(stuk, u)
    lok = (punten - o) @ R
    c = splitsen.SCHUIF_MM
    binnen = (np.abs(lok[:, 0]) < a) & (np.abs(lok[:, 1]) < b)
    if not (binnen & (lok[:, 2] > c)).any() or not (lok[:, 2] < c).any():
        report({"ERROR"}, f"The free cut does not go through {stuk.name}. Move it (G) so it crosses the piece")
        return None
    oude_gaten = json.loads(stuk.get("sj_gaten", "[]"))
    g = door_gat(oude_gaten, R, o, a, b, inst.wand_mm)
    if g is not None:
        report({"ERROR"}, f"The free cut goes through a hole of {stuk.name} (to piece {g.get('buur')}). "
                          f"Move it at least {inst.wand_mm:.1f} mm away from the hole")
        return None
    lo, hi = lok.min(axis=0), lok.max(axis=0)
    x0, x1, y0, y1 = max(lo[0], -a), min(hi[0], a), max(lo[1], -b), min(hi[1], b)
    nr_a = int(stuk["sj_stuk"])
    nr_b = max(int(s["sj_stuk"]) for s in alle) + 1
    cellen = {(0, 0, 0): ((x0, y0, lo[2]), (x1, y1, c)), (0, 0, 1): ((x0, y0, c), (x1, y1, hi[2]))}
    grenzen = [[x0, x1], [y0, y1], [lo[2], c, hi[2]]]
    nummers = {(0, 0, 0): nr_a, (0, 0, 1): nr_b}
    opties = eigenschappen.verbind_opties(inst)
    gaten, labels, pennen, meldingen = verbind_3d.plan_alles(lok, tri, cellen, nummers, grenzen, opties, inst.labels)

    solver = splitsen.solver_naam()
    hulp = splitsen.nieuwe_collectie("sj_hulp", scene)
    m_snede = Matrix.Translation(Vector(o) * u) @ Matrix(R.tolist()).to_4x4()

    def in_kader(ob):
        ob.matrix_world = m_snede
        return ob

    def opruimen():
        for x in list(hulp.objects):
            splitsen.weg(x)
        bpy.data.collections.remove(hulp)

    doos = in_kader(vormen.doos("sj_vrij_doos", (-a, -b, c), (a, b, hi[2] + splitsen.BUITEN_MM), u, hulp))
    ruw_b, f_b = splitsen.verschil(stuk, doos, solver, "sj_ruw_b", hulp, u, actie="INTERSECT")
    opp = wand_vlak(ruw_b, R, o, a, b, u)
    if opp > WAND_OPP_MM2 or len(ruw_b.data.polygons) == 0:
        opruimen()
        report({"ERROR"}, f"The free cut box touches {stuk.name} at its side ({opp:.1f} mm2). Scale the plane "
                          "up (S) so it goes around the whole part, or turn it")
        return None
    ruw_a, f_a = splitsen.verschil(stuk, doos, solver, "sj_ruw_a", hulp, u)
    fout_a, fout_b = list(f_a), list(f_b)

    def werk_uit(ruw, ijk, naam, fout, met_doos):
        werk = splitsen.bak(ruw, naam, hulp)
        lbl = labels.get(ijk, [])
        if lbl:
            lbo = splitsen.label_object("sj_labels", lbl, inst.label_diepte_mm, u, hulp, meldingen)
            if lbo is not None:
                in_kader(lbo)
                kleinste = min(lb["h"] for lb in lbl)
                if met_doos:  # numbers first in the box, then piece times that box (as in splitsen.py)
                    gesneden, f1 = splitsen.verschil(doos, lbo, solver, "sj_doos_nummers", hulp, u,
                                                     voxel_mm=max(0.05, kleinste / 40.0))
                    nieuw, f2 = splitsen.verschil(stuk, gesneden, solver, naam, hulp, u, actie="INTERSECT")
                    fout += f1 + f2
                else:
                    nieuw, f1 = splitsen.verschil(werk, lbo, solver, naam, hulp, u, voxel_mm=max(0.05, kleinste / 40.0))
                    fout += f1
                splitsen.weg(werk)
                werk = nieuw
        if gaten.get(ijk):
            go = in_kader(splitsen.gat_object("sj_gaten", gaten[ijk], u, hulp))
            nieuw, f = splitsen.verschil(werk, go, solver, naam, hulp, u)
            splitsen.weg(werk)
            werk = nieuw
            fout += f
        return werk

    werk_a = werk_uit(ruw_a, (0, 0, 0), "sj_werk_a", fout_a, False)
    werk_b = werk_uit(ruw_b, (0, 0, 1), "sj_werk_b", fout_b, True)

    col = stuk.users_collection[0]
    oud = {k: stuk.get(k) for k in ("sj_cel", "sj_wand_mm", "sj_vrij_buren", "sj_labels", "sj_label_diepte_mm")}
    oude_labels = json.loads(oud["sj_labels"] or "[]")
    b_bed = bed(scene)
    uit = []
    for werk, ruw, ijk, nr, buur, fout in ((werk_a, ruw_a, (0, 0, 0), nr_a, nr_b, fout_a),
                                          (werk_b, ruw_b, (0, 0, 1), nr_b, nr_a, fout_b)):
        af = splitsen.bak(werk, f"Piece {nr:02d}", col)
        kant = 1 if ijk == (0, 0, 1) else -1

        def op_kant(p):
            z = float((np.array(p) - o) @ R[:, 2])
            binnen_rect = abs(float((np.array(p) - o) @ R[:, 0])) <= a and abs(float((np.array(p) - o) @ R[:, 1])) <= b
            return (z > c and binnen_rect) == (kant == 1)

        mijn_oud = [g for g in oude_gaten if op_kant(g["p"])]
        nieuw = [naar_wereld(g, R, o) for g in gaten.get(ijk, [])]
        af["sj_fout_stappen"] = fout
        af["sj_stuk"] = nr
        af["sj_cel"] = list(oud["sj_cel"]) if oud["sj_cel"] is not None else [nr, 0, 0]
        af["sj_vrij_buren"] = sorted(set(int(x) for x in (oud["sj_vrij_buren"] or [])) | {buur})
        af["sj_label_diepte_mm"] = oud["sj_label_diepte_mm"] or inst.label_diepte_mm
        af["sj_labels"] = _json([lb for lb in oude_labels if op_kant(lb["p"])] +
                                     [naar_wereld(lb, R, o) for lb in labels.get(ijk, []) if not lb.get("weg")])
        af["sj_solver"] = solver
        # wall check: the new holes against this piece before its holes; the old holes kept their measured wall
        af["sj_gaten"] = _json(nieuw)
        controle.keur(af, ruw, b_bed, u, inst.wand_mm)
        wanden = [w for w in (af["sj_wand_mm"], oud["sj_wand_mm"] if mijn_oud else None) if w is not None and w >= 0]
        wand = min(wanden) if wanden else None
        af["sj_wand_mm"] = round(wand, 3) if wand is not None else -1.0
        af["sj_gaten"] = _json(mijn_oud + nieuw)
        status = controle.status_uit(af["sj_past"], af["sj_gesloten"], wand, inst.wand_mm)
        controle.kleur(af, status)
        af["sj_volume_ruw_mm3"] = controle.volume_mm3(ruw, u)
        co = np.array([tuple(v.co) for v in af.data.vertices]) / u
        af["sj_midden_mm"] = list((co.min(axis=0) + co.max(axis=0)) / 2.0)
        uit.append(af)
    opruimen()
    for s in alle:  # pieces that had the old piece as a free-cut neighbor touch both halves now
        if s is not stuk and nr_a in [int(x) for x in s.get("sj_vrij_buren", [])]:
            s["sj_vrij_buren"] = sorted(set(int(x) for x in s["sj_vrij_buren"]) | {nr_b})
    pob = None
    if pennen:
        pts = np.array([tuple(v.co) for s in alle for v in s.data.vertices]) / u
        x = float(pts[:, 0].max()) + 20.0
        for d, aantal in pennen:
            pob, breed = splitsen.pennen_object(f"Pins {d:g} mm x{aantal} (free cut {nr_a}-{nr_b})", d, aantal,
                                                inst.pen_lengte_mm, (x, float(pts[:, 1].max()) + 20.0,
                                                                     float(pts[:, 2].min())), u, col)
            pob["sj_pennen"] = aantal
            pob["sj_pen_d"] = d
            pob["sj_pen_lengte"] = inst.pen_lengte_mm
            x += breed + 10.0
    splitsen.weg(stuk)
    me = snede.data
    bpy.data.objects.remove(snede)
    if me is not None and me.users == 0:
        bpy.data.meshes.remove(me)
    a_ob, b_ob = uit
    a_ob.name = f"Piece {nr_a:02d}"
    if meldingen:
        inst.meldingen = "\n".join(([inst.meldingen] if inst.meldingen else []) + meldingen)
    return a_ob, b_ob, pob, sum(n for _d, n in pennen)


class SPLIT_JOINTS_OT_vrije_snede_erbij(bpy.types.Operator):
    bl_idname = "split_joints.vrije_snede_erbij"
    bl_label = "Add free cut"
    bl_description = ("Add a cut plane for the active piece that you can move (G), turn (R) and scale (S). "
                      "It only cuts what lies inside its rectangle, on the side its arrow (local Z) points to")
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob is not None and bool(ob.get("sj_stuk"))

    def execute(self, context):
        stuk, oud = stuk_van(context)
        if oud is not None:
            context.view_layer.objects.active = oud
            for o in context.view_layer.objects:
                o.select_set(o is oud)
            return {"FINISHED"}
        ob = maak_vrije_snede(context, stuk)
        for o in context.view_layer.objects:
            o.select_set(False)
        ob.select_set(True)
        context.view_layer.objects.active = ob
        self.report({"INFO"}, "Move (G), turn (R) and scale (S) the free cut, then Cut piece")
        return {"FINISHED"}


class SPLIT_JOINTS_OT_vrije_snede(bpy.types.Operator):
    bl_idname = "split_joints.vrije_snede"
    bl_label = "Cut piece"
    bl_description = "Cut the piece in two along the free cut, with pins and numbers, only inside the rectangle"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        stuk, snede = stuk_van(context)
        return stuk is not None and snede is not None

    def execute(self, context):
        stuk, snede = stuk_van(context)
        uitslag = snijd(context, stuk, snede, self.report)
        if uitslag is None:
            return {"CANCELLED"}
        a_ob, b_ob, _pob, n_pen = uitslag
        scene = context.scene
        uit_elkaar.zet(scene)
        kleuren.zet(scene)
        for o in context.view_layer.objects:
            o.select_set(False)
        b_ob.select_set(True)
        context.view_layer.objects.active = b_ob
        rood = [s for s in (a_ob, b_ob) if s.get("sj_status") == "rood"]
        inst = scene.split_joints
        if inst.verbinder == "MAGNET":
            n_mag = sum(1 for s_ in (a_ob, b_ob) for g in json.loads(s_.get("sj_gaten", "[]"))
                        if g.get("vrij") and g.get("soort") == "magneet")
            wat = f"holes for {n_mag} magnets"
        else:
            wat = f"{n_pen} pins"
        tekst = f"Piece {int(a_ob['sj_stuk'])} and new piece {int(b_ob['sj_stuk'])}, {wat}"
        self.report({"WARNING"} if rood else {"INFO"}, tekst + (", check the red piece" if rood else ""))
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_vrije_snede_erbij, SPLIT_JOINTS_OT_vrije_snede)
