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
from .lijn import deel_eraf, eraf_hoeken, omdraaien, vlak_uit_lijn
from .eigenschappen import bed, eenheid_per_mm

NAAM = "Free cut"
WAND_TOL_MM = 0.002  # a face this close to a side wall of the box lies on that wall
WAND_OPP_MM2 = 0.05  # more wall area than this on the new piece: the box touched the piece at its side
# keuring #212 K2: after Draw cut the buyer thinks in lines, not in scaling (S)
LIJN_TE_KORT = "Drag the line all the way across the piece: Draw cut again, with the line past both edges"
ERAF_KLEUR = (0.85, 0.35, 0.9)  # the colour of the cut plane: the arrow belongs to the cut
LICHT = (1.0, 1.0, 1.0, 0.5)  # the part that comes off lights up white: pieces have every colour, white none


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
    getekend = bool(snede.get("sj_getekend"))
    if a < 1.0 or b < 1.0:
        report({"ERROR"}, LIJN_TE_KORT if getekend else
               "The free cut is too small: scale it up (S) so it covers the part you want to cut off")
        return None
    alle = uit_elkaar.stukken(scene)
    with uit_elkaar.echte_plek(alle):
        return _snijd(context, scene, inst, u, stuk, snede, R, o, a, b, alle, report, getekend)


def _snijd(context, scene, inst, u, stuk, snede, R, o, a, b, alle, report, getekend=False):
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
        report({"ERROR"}, f"The free cut goes through a {'magnet' if g.get('soort') == 'magneet' else 'pin'} hole of {stuk.name} (to piece {g.get('buur')}). "
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
        report({"ERROR"}, LIJN_TE_KORT if getekend else
               f"The free cut box touches {stuk.name} at its side ({opp:.1f} mm2). Scale the plane "
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


def zet_vlak(context, stuk, R, o, a, b, snede=None):
    """Places the free cut of the piece on the frame (world space, Blender units). Reuses the plane if there is
    one, else makes it. Returns the plane object."""
    if snede is None:
        snede = maak_vrije_snede(context, stuk)
    me = snede.data
    me.clear_geometry()
    me.from_pydata([(-a, -b, 0), (a, -b, 0), (a, b, 0), (-a, b, 0)], [], [(0, 1, 2, 3)])
    me.update()
    m = Matrix(np.asarray(R, dtype=float).tolist()).to_4x4()
    m.translation = Vector(np.asarray(o, dtype=float).tolist())
    snede.matrix_world = m
    return snede


def punten_wereld(stuk):
    """N x 3 points of the piece in world space (Blender units)."""
    me = stuk.data
    co = np.empty(len(me.vertices) * 3)
    me.vertices.foreach_get("co", co)
    co = co.reshape(-1, 3)
    mw = np.array(stuk.matrix_world)
    return co @ mw[:3, :3].T + mw[:3, 3]


def naar_3d(region, rv3d, xy, diepte, ndc_z=None):
    """Pixel of the 3D view region to a point in the world at the depth of `diepte` (or at a fixed ndc_z).
    The exact inverse of what Blender draws (perspective_matrix), for perspective and orthographic views alike.
    Why not bpy_extras region_2d_to_location_3d: in an orthographic view with a far Clip End (100000, common in
    mm scenes) it lands 33 to 113 px off the mouse (measured 26 nov in Blender 4.2.23 and 5.3.0); this one
    lands on the pixel in both kinds of view."""
    pm = rv3d.perspective_matrix
    if ndc_z is None:
        d = pm @ Vector((diepte[0], diepte[1], diepte[2], 1.0))
        ndc_z = d.z / d.w if abs(d.w) > 1e-12 else 0.0
    q = pm.inverted() @ Vector((2.0 * xy[0] / region.width - 1.0, 2.0 * xy[1] / region.height - 1.0, ndc_z, 1.0))
    return Vector((q.x / q.w, q.y / q.w, q.z / q.w))


GEBEURD = []  # last mouse events of Draw cut, read by the screen test (e2e/scherm_paneel.py)


def _teken_lijn(op, _context):
    if op.begin is None or op.eind is None or op.regio is None:
        return
    if bpy.context.region is None or bpy.context.region.as_pointer() != op.regio.as_pointer():
        return  # only in the view where you draw
    try:
        _lijn_op_scherm(op)
    except Exception as e:  # never break the viewport over the helper line
        GEBEURD.append(f"teken fout {e!r}")
        del GEBEURD[:-40]


def _lijn_op_scherm(op):
    import gpu
    from gpu_extras.batch import batch_for_shader
    shader = gpu.shader.from_builtin("UNIFORM_COLOR")
    batch = batch_for_shader(shader, "LINES", {"pos": [tuple(op.begin), tuple(op.eind)]})
    gpu.state.blend_set("ALPHA")
    gpu.state.line_width_set(2.0)
    shader.bind()
    shader.uniform_float("color", (0.85, 0.35, 0.9, 1.0))
    batch.draw(shader)
    gpu.state.line_width_set(1.0)
    gpu.state.blend_set("NONE")


class SPLIT_JOINTS_OT_vrije_snede_tekenen(bpy.types.Operator):
    bl_idname = "split_joints.vrije_snede_tekenen"
    bl_label = "Draw cut"
    bl_description = ("Drag a line across the active piece where you want to cut it. The cut goes along the line, "
                      "straight away from you, and only as wide as the line. Then press Cut piece")
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        stuk, _snede = stuk_van(context)
        return stuk is not None and context.area is not None and context.area.type == "VIEW_3D"

    def invoke(self, context, event):
        # the button sits in the sidebar, so context.region is the sidebar: the line is measured in the 3D view
        # region itself (window coordinates minus its corner), the one under the mouse when you press
        self.begin = None
        self.eind = None
        self.regio = None
        self.rv3d = None
        self.stuk_naam = stuk_van(context)[0].name
        self.handle = bpy.types.SpaceView3D.draw_handler_add(_teken_lijn, (self, context), "WINDOW", "POST_PIXEL")
        context.workspace.status_text_set("Draw cut: click and drag a line across the piece   Esc: cancel")
        context.window.cursor_modal_set("CROSSHAIR")
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def _stop(self, context):
        bpy.types.SpaceView3D.draw_handler_remove(self.handle, "WINDOW")
        context.workspace.status_text_set(None)
        context.window.cursor_modal_restore()
        context.area.tag_redraw()

    def modal(self, context, event):
        if event.type not in {"TIMER", "INBETWEEN_MOUSEMOVE"}:
            GEBEURD.append(f"{event.type} {event.value} {event.mouse_region_x} {event.mouse_region_y}")
            del GEBEURD[:-40]
        if event.type in {"ESC", "RIGHTMOUSE"} and event.value == "PRESS":
            self._stop(context)
            return {"CANCELLED"}
        if event.type == "MOUSEMOVE":
            if self.begin is not None:
                self.eind = self._in_regio(event)
                context.area.tag_redraw()
            return {"RUNNING_MODAL"}
        if event.type == "LEFTMOUSE" and event.value == "PRESS":
            regio = self._regio_onder(context, event)
            if regio is None:  # pressed outside the 3D view (sidebar, header): ignore, keep waiting
                return {"RUNNING_MODAL"}
            self.regio, self.rv3d = regio
            self.begin = self._in_regio(event)
            self.eind = self.begin
            return {"RUNNING_MODAL"}
        if event.type == "LEFTMOUSE" and event.value == "RELEASE" and self.begin is not None:
            self.eind = self._in_regio(event)
            self._stop(context)
            return self.plaats(context)
        if event.type in {"MIDDLEMOUSE", "WHEELUPMOUSE", "WHEELDOWNMOUSE"}:
            return {"PASS_THROUGH"}  # turning and zooming the view still works before you drag
        return {"RUNNING_MODAL"}

    @staticmethod
    def _regio_onder(context, event):
        """(3D view region, its RegionView3D) under the mouse; with quad view each quarter is its own region."""
        regios = [r for r in context.area.regions if r.type == "WINDOW"]
        vlakken = [r for r in regios if r.x <= event.mouse_x < r.x + r.width and r.y <= event.mouse_y < r.y + r.height]
        if not vlakken:
            return None
        r = vlakken[0]
        sp = context.area.spaces.active
        if len(regios) > 1 and getattr(sp, "region_quadviews", None):
            vlakken_rv = list(sp.region_quadviews)
            idx = regios.index(r)
            if idx < len(vlakken_rv):
                return r, vlakken_rv[idx]
        return r, sp.region_3d

    def _in_regio(self, event):
        r = self.regio
        return (event.mouse_x - r.x, event.mouse_y - r.y)

    def plaats(self, context):
        stuk = bpy.data.objects.get(self.stuk_naam)
        if stuk is None:
            return {"CANCELLED"}
        if math.dist(self.begin, self.eind) < 8:
            self.report({"WARNING"}, "Drag a longer line across the piece")
            return {"CANCELLED"}
        region, rv3d = self.regio, self.rv3d
        pts = punten_wereld(stuk)
        midden = Vector(((pts.min(axis=0) + pts.max(axis=0)) / 2.0).tolist())
        p1 = naar_3d(region, rv3d, self.begin, midden)
        p2 = naar_3d(region, rv3d, self.eind, midden)
        mid = ((self.begin[0] + self.eind[0]) / 2.0, (self.begin[1] + self.eind[1]) / 2.0)
        kijk = naar_3d(region, rv3d, mid, midden, ndc_z=0.5) - naar_3d(region, rv3d, mid, midden, ndc_z=-0.5)
        u = eenheid_per_mm(context.scene)
        kader_ = vlak_uit_lijn(p1, p2, kijk, pts, marge=1.0 * u)
        if kader_ is None:
            self.report({"WARNING"}, "Drag a longer line across the piece")
            return {"CANCELLED"}
        _s, oud = stuk_van(context)
        snede = zet_vlak(context, stuk, *kader_, snede=oud if oud is not None and oud.get("sj_vrij") == stuk.name else None)
        for o in context.view_layer.objects:
            o.select_set(False)
        snede.select_set(True)
        context.view_layer.objects.active = snede
        snede["sj_getekend"] = True
        self.report({"INFO"}, "Cut placed: the lit part comes off. Press Cut piece, or Flip side for the other part")
        return {"FINISHED"}


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


class SPLIT_JOINTS_OT_vrije_snede_om(bpy.types.Operator):
    bl_idname = "split_joints.vrije_snede_om"
    bl_label = "Flip side"
    bl_description = "Cut off the other part: turns the free cut half a turn, so the arrow and the lit part change side"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        stuk, snede = stuk_van(context)
        return stuk is not None and snede is not None

    def execute(self, context):
        _stuk, snede = stuk_van(context)
        draai_om(snede)
        for area in context.screen.areas if context.screen else ():
            if area.type == "VIEW_3D":
                area.tag_redraw()
        self.report({"INFO"}, "The other part comes off now. Press Cut piece")
        return {"FINISHED"}


def draai_om(snede):
    """Flip side (keuring #212 K1): half a turn around the local Y through the middle of the rectangle."""
    ps = [Vector(v.co) for v in snede.data.vertices]
    mid = sum(ps, Vector()) / max(len(ps), 1)
    mw = snede.matrix_world
    loc, rot, sca = mw.decompose()
    R = omdraaien(np.array(rot.to_matrix()))
    m_mid = mw @ mid
    nieuw = Matrix(R.tolist()).to_4x4() @ Matrix.Diagonal(sca.to_4d())
    nieuw.translation = m_mid - (nieuw.to_3x3() @ mid)
    snede.matrix_world = nieuw


# keuring #212 M1: before Cut piece the buyer sees what comes off. The part of the piece on the arrow side and
# inside the rectangle is lit in the colour of the cut, and an arrow with "comes off" points to it on the screen.
STAND = {"driehoeken": 0, "pijl": None, "fout": None}  # last drawing, read by the screen test (e2e/scherm_paneel.py)
_CACHE = {"sleutel": None, "tris": None, "midden": None}
_HANDLES = []


def _actief_paar():
    ctx = bpy.context
    try:
        stuk, snede = stuk_van(ctx)
    except (AttributeError, ReferenceError):
        return None, None
    if stuk is None or snede is None or stuk.hide_get() or snede.hide_get():
        return None, None
    return stuk, snede


def _eraf_wereld(stuk, snede):
    """(triangle corners K x 3 in world space, slightly lifted along the normals; middle of the lit part) for the
    pair, cached on the placement of the cut and the piece."""
    sleutel = (stuk.name, len(stuk.data.vertices), len(stuk.data.polygons),
               tuple(round(x, 6) for r in stuk.matrix_world for x in r),
               tuple(round(x, 6) for r in snede.matrix_world for x in r),
               tuple(round(c, 6) for v in snede.data.vertices for c in v.co))
    if _CACHE["sleutel"] == sleutel:
        return _CACHE["tris"], _CACHE["midden"]
    punten, tri = mesh_lokaal_mm(stuk, 1.0)
    R, o, a, b = kader(stuk, snede, 1.0)
    keus = deel_eraf(punten, tri, R, o, a, b)
    tris, midden = None, None
    if keus.any():
        me = stuk.data
        nrm = np.empty(len(me.vertices) * 3)
        me.vertices.foreach_get("normal", nrm)
        grootte = float(np.ptp(punten, axis=0).max()) or 1.0
        opgetild = punten + nrm.reshape(-1, 3) * grootte * 0.002  # above the surface, no flicker with the piece
        mw = np.array(stuk.matrix_world)
        hoeken = eraf_hoeken(punten, tri, R, o, a, b, mee=opgetild).reshape(-1, 3) @ mw[:3, :3].T + mw[:3, 3]
        tris = [tuple(p) for p in hoeken.tolist()]
        mid_l = punten[np.unique(tri[keus].ravel())]
        midden = Vector(((mid_l.min(axis=0) + mid_l.max(axis=0)) / 2.0 @ mw[:3, :3].T + mw[:3, 3]).tolist())
    _CACHE.update(sleutel=sleutel, tris=tris, midden=midden)
    return tris, midden


def _teken_eraf_3d():
    stuk, snede = _actief_paar()
    if stuk is None:
        return
    try:
        import gpu
        from gpu_extras.batch import batch_for_shader
        tris, _m = _eraf_wereld(stuk, snede)
        STAND["driehoeken"] = len(tris) // 3 if tris else 0
        if not tris:
            return
        shader = gpu.shader.from_builtin("UNIFORM_COLOR")
        batch = batch_for_shader(shader, "TRIS", {"pos": tris})
        gpu.state.blend_set("ALPHA")
        gpu.state.depth_test_set("LESS_EQUAL")
        gpu.state.depth_mask_set(False)
        shader.bind()
        shader.uniform_float("color", LICHT)
        batch.draw(shader)
        gpu.state.depth_mask_set(True)
        gpu.state.depth_test_set("NONE")
        gpu.state.blend_set("NONE")
    except Exception as e:  # never break the viewport over the highlight
        STAND["fout"] = repr(e)


def naar_scherm(region, rv3d, p):
    """World point to a pixel of the region with perspective_matrix (the same matrix naar_3d inverts)."""
    q = rv3d.perspective_matrix @ Vector((p[0], p[1], p[2], 1.0))
    if q.w <= 1e-9:
        return None
    return Vector(((q.x / q.w + 1.0) * region.width / 2.0, (q.y / q.w + 1.0) * region.height / 2.0))


PIJL_PX = 70


def _teken_eraf_2d():
    stuk, snede = _actief_paar()
    if stuk is None:
        return
    try:
        region, rv3d = bpy.context.region, bpy.context.region_data
        if region is None or rv3d is None:
            return
        tris, midden = _eraf_wereld(stuk, snede)
        if not tris:
            return
        R, o, a, b = kader(stuk, snede, 1.0)
        mw = np.array(stuk.matrix_world)
        c3 = Vector((np.asarray(o) @ mw[:3, :3].T + mw[:3, 3]).tolist())
        n3 = Vector((R[:, 2] @ mw[:3, :3].T).tolist()).normalized()
        c = naar_scherm(region, rv3d, c3)
        m = naar_scherm(region, rv3d, midden)
        if c is None or m is None:
            return
        # the arrow starts at the cut and points to the lit part; seen face-on the arrow is the way to the middle
        stap_ = naar_scherm(region, rv3d, c3 + n3 * (max(a, b) * 0.05 or 1.0))
        d = (stap_ - c) if stap_ is not None else Vector((0.0, 0.0))
        if d.length < 2.0:
            d = m - c
        if d.length < 2.0:
            return
        d.normalize()
        sc = bpy.context.preferences.system.ui_scale
        begin = c + d * 4.0 * sc
        punt = c + d * PIJL_PX * sc
        zij = Vector((-d.y, d.x))
        kop = [punt, punt - d * 20.0 * sc + zij * 12.0 * sc, punt - d * 20.0 * sc - zij * 12.0 * sc]
        import blf
        import gpu
        from gpu_extras.batch import batch_for_shader
        shader = gpu.shader.from_builtin("UNIFORM_COLOR")
        gpu.state.blend_set("ALPHA")

        def vlak(punten, kleur):
            shader.bind()
            shader.uniform_float("color", kleur)
            batch_for_shader(shader, "TRIS", {"pos": [tuple(p) for p in punten]}).draw(shader)

        def balk(p, q, dik):  # a line as two triangles: line_width is 1 px on some drivers
            z = Vector((-(q - p).y, (q - p).x)).normalized() * dik / 2.0
            return [p + z, p - z, q + z, p - z, q - z, q + z]

        rand = 2.0 * sc
        schacht = (begin, punt - d * 18.0 * sc)
        donker = (0.05, 0.05, 0.05, 0.85)
        vlak(balk(*schacht, 5.0 * sc + 2 * rand), donker)
        vlak([kop[0] + d * rand * 1.8, kop[1] - d * rand + zij * rand * 1.4, kop[2] - d * rand - zij * rand * 1.4], donker)
        vlak(balk(*schacht, 5.0 * sc), (*ERAF_KLEUR, 1.0))
        vlak(kop, (*ERAF_KLEUR, 1.0))
        tekst = "comes off"
        blf.size(0, int(14 * sc))
        breed, hoog = blf.dimensions(0, tekst)
        t = punt + d * 10.0 * sc
        x = t.x if d.x >= -0.3 else t.x - breed
        x = t.x - breed / 2.0 if abs(d.x) < 0.3 else x
        y = t.y - hoog / 2.0 if abs(d.y) < 0.7 else (t.y if d.y > 0 else t.y - hoog)
        m_ = 5.0 * sc  # dark label behind the text, readable on the white light and on every piece colour
        a_, b_ = Vector((x - m_, y - m_)), Vector((x + breed + m_, y + hoog + m_))
        vlak([a_, Vector((b_.x, a_.y)), b_, a_, b_, Vector((a_.x, b_.y))], donker)
        blf.position(0, x, y, 0)
        blf.color(0, 1.0, 1.0, 1.0, 1.0)
        blf.draw(0, tekst)
        gpu.state.blend_set("NONE")
        STAND["pijl"] = (round(c.x), round(c.y), round(punt.x), round(punt.y))
    except Exception as e:
        STAND["fout"] = repr(e)


def koppel():
    if _HANDLES:
        return
    _HANDLES.append((bpy.types.SpaceView3D.draw_handler_add(_teken_eraf_3d, (), "WINDOW", "POST_VIEW"), "WINDOW"))
    _HANDLES.append((bpy.types.SpaceView3D.draw_handler_add(_teken_eraf_2d, (), "WINDOW", "POST_PIXEL"), "WINDOW"))


def ontkoppel():
    while _HANDLES:
        h, soort = _HANDLES.pop()
        try:
            bpy.types.SpaceView3D.draw_handler_remove(h, soort)
        except (ValueError, RuntimeError):
            pass


KLASSEN = (SPLIT_JOINTS_OT_vrije_snede_erbij, SPLIT_JOINTS_OT_vrije_snede_tekenen, SPLIT_JOINTS_OT_vrije_snede_om,
           SPLIT_JOINTS_OT_vrije_snede)
