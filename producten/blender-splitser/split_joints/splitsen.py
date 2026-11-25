"""Operator split_joints.split: cuts the model along the cut planes into pieces with pin holes and numbers.

Order: watertight check, one piece per grid cell (Boolean Intersect with a box), number the pieces
(bottom layer first), plan pins and labels on every shared face (verbind_3d.py), cut the holes and
the numbers (Boolean Difference), make the pins, check every piece (controle.py).
Booleans: Manifold solver on Blender 4.5+, else Exact, as in Click Joints."""
import json
import time

import bmesh
import bpy
from mathutils import Vector

from . import controle, kleuren, plan, snedes, uit_elkaar, verbind_3d, vormen
from .eigenschappen import bed, eenheid_per_mm, verbind_opties
from .gesloten import foute_randen, is_gesloten

STUKKEN = "Click Cuts pieces"
BUITEN_MM = 10.0  # outer boxes reach this far past the model
# The cut lies this far past the plane you set: a cut exactly through existing points gave open edges in
# Blender 4.2 (lesson from Click Joints, gewricht.py). Far below anything a printer can show.
SCHUIF_MM = 0.0137


def solver_naam():
    solvers = {s.identifier for s in bpy.types.BooleanModifier.bl_rna.properties["solver"].enum_items}
    if bpy.app.version >= (4, 5, 0) and "MANIFOLD" in solvers:
        return "MANIFOLD"
    return "EXACT"


def boolean(doel, gereedschap, actie, solver):
    m = doel.modifiers.new(f"sj_{actie}", "BOOLEAN")
    m.operation = actie
    m.object = gereedschap
    m.solver = solver
    if solver == "EXACT":
        m.use_self = False
        m.use_hole_tolerant = False
    gereedschap.hide_set(True)


def bak(ob, naam, collectie):
    """New object with the evaluated mesh of ob in world coordinates (identity matrix)."""
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    me.transform(ob.matrix_world)
    me.name = naam
    uit = bpy.data.objects.new(naam, me)
    collectie.objects.link(uit)
    return uit


def splits_vierkant(bm):
    """Edges with 4 (or 6, ...) faces: two parts of the model touch each other exactly on a line in the cut
    plane (seen with Exact in 4.2 on the 1M face skull scan, ontwerp 14b). Not a hole, so merging points does
    not help. Every point of such an edge gets one copy per fan of faces around it (faces that are joined by
    an edge with exactly 2 faces), so each part gets its own edge with 2 faces. The shape does not change.
    Returns the number of points that were split."""
    bm.edges.ensure_lookup_table()
    punten = {v for e in bm.edges if len(e.link_faces) >= 4 and len(e.link_faces) % 2 == 0 for v in e.verts}
    vervang = {}  # face -> {old vert: new vert}
    gesplitst = 0
    for v in punten:
        vlakken = list(v.link_faces)
        ouder = {f: f for f in vlakken}

        def wortel(f):
            while ouder[f] is not f:
                ouder[f] = ouder[ouder[f]]
                f = ouder[f]
            return f

        for e in v.link_edges:
            if len(e.link_faces) == 2:
                a, b = (wortel(f) for f in e.link_faces)
                if a is not b:
                    ouder[a] = b
        groepen = {}
        for f in vlakken:
            groepen.setdefault(wortel(f), []).append(f)
        if len(groepen) < 2:
            continue
        for groep in list(groepen.values())[1:]:
            kopie = bm.verts.new(v.co)
            gesplitst += 1
            for f in groep:
                vervang.setdefault(f, {})[v] = kopie
    if not vervang:
        return 0
    oud = []
    for f, kaart in vervang.items():
        punten_f = [kaart.get(l.vert, l.vert) for l in f.loops]
        try:
            bm.faces.new(punten_f, f)
        except ValueError:
            continue
        oud.append(f)
    bmesh.ops.delete(bm, geom=oud, context="FACES_ONLY")
    los = [e for e in bm.edges if not e.link_faces]
    if los:
        bmesh.ops.delete(bm, geom=los, context="EDGES")
    los = [v for v in bm.verts if not v.link_edges]
    if los:
        bmesh.ops.delete(bm, geom=los, context="VERTS")
    return gesplitst


def herstel(ob, u):
    """Repair after a Boolean that left a few bad edges (seen with Exact in 4.2): merge points that lie on top
    of each other and dissolve slivers. Returns the number of bad edges after the repair."""
    fout = foute_randen(ob.data)
    if fout == 0:
        return 0
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0005 * u)
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=0.0005 * u)
    bm.to_mesh(ob.data)
    ob.data.update()
    fout = foute_randen(ob.data)
    if fout and splits_vierkant(bm):
        # only keep the split when it leaves fewer bad edges (a sliver can turn into open edges instead)
        me = bpy.data.meshes.new("sj_herstel")
        bm.to_mesh(me)
        if foute_randen(me) < fout:
            ob.data.clear_geometry()
            bm.to_mesh(ob.data)
            ob.data.update()
            fout = foute_randen(ob.data)
        bpy.data.meshes.remove(me)
    bm.free()
    return fout


POGINGEN = ("gewoon", "driehoeken", "zelf", "gaten", "schuif")


def verschil(doel, gereedschap, solver, naam, collectie, u, voxel_mm=None, actie="DIFFERENCE"):
    """Boolean (Difference unless told otherwise), baked. Exact (4.2) sometimes leaves a few open edges around small shapes such as
    the numbers (every "4" of the built-in font gave 4 open edges, run 45212458120); then we try again: the
    tool as a fine voxel copy (voxel_mm, only for the numbers), target in triangles, Self Intersection on,
    Hole Tolerant on, and the tool shifted 0.002 mm. Returns (new object, bad edges per try); the first try
    without bad edges wins."""
    telling, beste = [], None
    pogingen = POGINGEN if solver == "EXACT" else POGINGEN[:1]
    if solver == "EXACT" and voxel_mm:
        pogingen = ("gewoon", "voxel") + POGINGEN[1:]
    for poging in pogingen:
        remesh = None
        if poging == "voxel":
            remesh = gereedschap.modifiers.new("sj_voxel", "REMESH")
            remesh.mode = "VOXEL"
            remesh.voxel_size = voxel_mm * u
        werk = bak(doel, naam, collectie)
        if poging == "driehoeken":
            bm = bmesh.new()
            bm.from_mesh(werk.data)
            bmesh.ops.triangulate(bm, faces=bm.faces)
            bm.to_mesh(werk.data)
            bm.free()
        oud = gereedschap.location.copy()
        if poging == "schuif":
            gereedschap.location = oud + Vector((0.0013, 0.0017, 0.0011)) * u
        boolean(werk, gereedschap, actie, solver)
        m = werk.modifiers[-1]
        if poging == "zelf":
            m.use_self = True
        if poging == "gaten":
            m.use_hole_tolerant = True
        uit = bak(werk, naam, collectie)
        gereedschap.location = oud
        if remesh is not None:
            gereedschap.modifiers.remove(remesh)
        weg(werk)
        fout = herstel(uit, u)
        telling.append(fout)
        if beste is None or fout < beste[0]:
            if beste is not None:
                weg(beste[1])
            beste = (fout, uit)
        else:
            weg(uit)
        if fout == 0:
            break
    return beste[1], telling


def weg(ob):
    me = ob.data
    bpy.data.objects.remove(ob)
    if me is not None and me.users == 0:
        bpy.data.meshes.remove(me)


def ruim_oud_op(scene):
    col = bpy.data.collections.get(STUKKEN)
    if col is not None:
        for ob in list(col.objects):
            weg(ob)
        bpy.data.collections.remove(col)


def cel_doos(ijk, cel, n_ijk, u, collectie):
    """Box of one cell; at the outside of the grid it reaches BUITEN_MM past the model."""
    mn, mx = cel
    bmn = [mn[a] - (BUITEN_MM if ijk[a] == 0 else 0.0) for a in range(3)]
    bmx = [mx[a] + (BUITEN_MM if ijk[a] == n_ijk[a] - 1 else 0.0) for a in range(3)]
    return vormen.doos("sj_doos", bmn, bmx, u, collectie)


def nieuwe_collectie(naam, scene):
    col = bpy.data.collections.new(naam)
    scene.collection.children.link(col)
    return col


def gat_object(naam, gaten, u, col):
    bm = bmesh.new()
    for g in gaten:
        vormen.gat_bmesh(bm, g["p"], g["as"], g["r_gat"], g["diepte"], u)
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    col.objects.link(ob)
    return ob


def label_object(naam, labels, diepte, u, col, meldingen):
    bm = bmesh.new()
    for lb in labels:
        me, _breedte = vormen.label_mesh(lb["tekst"], lb["h"], diepte, lb["p"], lb["as"], lb["teken"], u,
                                         max_breedte=lb.get("breed"), richting=lb.get("richting"))
        if me is None or foute_randen(me):
            meldingen.append(f"Piece {lb['tekst'].split('-')[0]}: the number {lb['tekst']} could not be made "
                             "as a closed shape and was left out")
            lb["weg"] = True
            if me is not None:
                bpy.data.meshes.remove(me)
            continue
        bm.from_mesh(me)
        bpy.data.meshes.remove(me)
    if not bm.verts:
        bm.free()
        return None
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    col.objects.link(ob)
    return ob


def pennen_object(naam, d, aantal, lengte, voet_mm, u, col):
    """All pins of one diameter standing on a small grid, ready to print in one go."""
    bm = bmesh.new()
    kol = max(1, int(aantal ** 0.5 + 0.999))
    stap = d + 4.0
    for k in range(aantal):
        x = voet_mm[0] + (k % kol) * stap
        y = voet_mm[1] + (k // kol) * stap
        vormen.pen_bmesh(bm, (x, y, voet_mm[2]), d, lengte, u)
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    col.objects.link(ob)
    return ob, kol * stap


class SPLIT_JOINTS_OT_split(bpy.types.Operator):
    bl_idname = "split_joints.split"
    bl_label = "Split"
    bl_description = "Cut the model along the cut planes into pieces with pin holes and engraved numbers"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        t0 = time.time()
        scene = context.scene
        inst = scene.split_joints
        ob = snedes.model(context)
        if ob is None:
            self.report({"ERROR"}, "Select the model first")
            return {"CANCELLED"}
        melding = snedes.te_groot_tekst(ob, scene)
        if melding:
            self.report({"ERROR"}, melding)
            return {"CANCELLED"}
        ok, fout = is_gesloten(ob)
        if not ok:
            scene["sj_geweigerd"] = f"open:{fout}"
            self.report({"ERROR"}, f"{ob.name} is not watertight ({fout} bad edges). Use Make watertight first.")
            return {"CANCELLED"}
        u = eenheid_per_mm(scene)
        punten, tri = snedes.mesh_mm(ob, scene)
        lo, hi = tuple(punten.min(axis=0)), tuple(punten.max(axis=0))
        sn = [(a, pos + SCHUIF_MM) for a, pos in snedes.lees(scene)]
        n_cellen = plan.aantal_cellen(lo, hi, sn)
        if n_cellen > plan.MAX_CELLEN:
            scene["sj_geweigerd"] = f"cellen:{n_cellen}"
            self.report({"ERROR"}, f"These cuts make {n_cellen} cells (limit {plan.MAX_CELLEN}). Remove cuts or plan again")
            return {"CANCELLED"}
        scene["sj_geweigerd"] = ""
        inst.uitslag = ""
        lijst, grenzen = plan.cellen(lo, hi, sn)
        # keuring K5: a model split before that is not this one comes back into view (its pieces go)
        vorig = bpy.data.objects.get(scene.get("sj_gesneden_model", ""))
        if vorig is not None and vorig is not ob:
            eigen = bpy.data.objects.get(vorig.get("sj_bron", ""))  # a watertight copy: show the own model
            if eigen is not None and eigen is not ob and eigen.name in context.view_layer.objects:
                vorig = eigen
            if vorig.name in context.view_layer.objects:
                vorig.hide_set(False)
        ruim_oud_op(scene)
        col = nieuwe_collectie(STUKKEN, scene)
        hulp = nieuwe_collectie("sj_hulp", scene)
        solver = solver_naam()
        meldingen = []
        ruw, cellen = {}, {}
        n_ijk = [len(g) - 1 for g in grenzen]
        for ijk, mn, mx in lijst:
            doos = cel_doos(ijk, (mn, mx), n_ijk, u, hulp)
            kopie = bak(ob, "sj_kopie", hulp)
            boolean(kopie, doos, "INTERSECT", solver)
            stuk = bak(kopie, "sj_ruw", hulp)
            weg(kopie)
            weg(doos)
            if len(stuk.data.polygons) == 0:
                weg(stuk)
                continue
            stuk["sj_fout"] = [foute_randen(stuk.data), herstel(stuk, u)]
            ruw[ijk], cellen[ijk] = stuk, (mn, mx)
        volgorde = sorted(ruw, key=lambda t: (t[2], t[1], t[0]))
        nummers = {ijk: i + 1 for i, ijk in enumerate(volgorde)}
        opties = verbind_opties(inst)
        gaten, labels, pennen, m2 = verbind_3d.plan_alles(punten, tri, cellen, nummers, grenzen, opties, inst.labels)
        meldingen += m2
        b = bed(scene)
        stukken = []
        for ijk in volgorde:
            nr = nummers[ijk]
            stuk = ruw[ijk]
            fout = list(stuk["sj_fout"])
            lbo = label_object("sj_labels", labels.get(ijk, []), inst.label_diepte_mm, u, hulp, meldingen) \
                if labels.get(ijk) else None
            if lbo is not None:
                # Numbers first, in the box: box minus the numbers (simple shapes), then model times that box.
                # Subtracting the numbers from the finished piece left open edges with Exact in 4.2
                # (run 45213448129), even with a voxel copy of the text.
                kleinste = min(lb["h"] for lb in labels[ijk])
                doos = cel_doos(ijk, cellen[ijk], n_ijk, u, hulp)
                gesneden, f1 = verschil(doos, lbo, solver, "sj_doos_nummers", hulp, u, voxel_mm=max(0.05, kleinste / 40.0))
                # Manifold (4.5+) handles the coplanar cut faces, so the rough piece is enough (speed test
                # 24 nov: the whole model a second time per piece was a third of the time on 1M polygons).
                bron = stuk if solver == "MANIFOLD" else ob
                werk, f2 = verschil(bak(bron, "sj_kopie", hulp), gesneden, solver, "sj_werk", hulp, u, actie="INTERSECT")
                fout += f1 + f2
            else:
                werk = bak(stuk, "sj_werk", hulp)
            if gaten.get(ijk):
                vorig = werk
                werk, f = verschil(werk, gat_object("sj_gaten", gaten[ijk], u, hulp), solver, "sj_werk2", hulp, u)
                weg(vorig)
                fout += f
            af = bak(werk, f"Piece {nr:02d}", col)
            af["sj_fout_stappen"] = fout  # bad edges per step and per try (cut, holes, numbers)
            af["sj_stuk"] = nr
            af["sj_cel"] = list(ijk)
            mn, mx = cellen[ijk]
            af["sj_midden_mm"] = [(mn[a] + mx[a]) / 2.0 for a in range(3)]
            af["sj_gaten"] = json.dumps(gaten.get(ijk, []))
            af["sj_labels"] = json.dumps([lb for lb in labels.get(ijk, []) if not lb.get("weg")])
            af["sj_label_diepte_mm"] = inst.label_diepte_mm
            af["sj_solver"] = solver
            controle.keur(af, stuk, b, u, opties["wand"])
            stukken.append(af)
        ruw_vol = {nummers[ijk]: controle.volume_mm3(ruw[ijk], u) for ijk in volgorde}
        for af in stukken:
            af["sj_volume_ruw_mm3"] = ruw_vol[af["sj_stuk"]]
        for o in list(hulp.objects):
            weg(o)
        bpy.data.collections.remove(hulp)
        x = hi[0] + 20.0
        for d, aantal in pennen:
            pob, breed = pennen_object(f"Pins {d:g} mm x{aantal}", d, aantal, inst.pen_lengte_mm, (x, lo[1], lo[2]), u, col)
            pob["sj_pennen"] = aantal
            pob["sj_pen_d"] = d
            pob["sj_pen_lengte"] = inst.pen_lengte_mm
            controle.kleur(pob, "groen")
            x += breed + 10.0
        ob.hide_set(True)
        scene["sj_gesneden_model"] = ob.name
        scene["sj_snedes_bij_split"] = json.dumps(snedes.handtekening(scene))
        for s in snedes.snede_objecten(scene):
            s.hide_set(True)
        scene["sj_midden_mm"] = [(lo[a] + hi[a]) / 2.0 for a in range(3)]
        uit_elkaar.zet(scene)
        kleuren.zet(scene)
        inst.meldingen = "\n".join(meldingen)
        context.view_layer.update()
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(False)
        if stukken:
            context.view_layer.objects.active = stukken[0]
        rood = sum(1 for s in stukken if s.get("sj_status") == "rood")
        scene["sj_duur_s"] = round(time.time() - t0, 2)
        if opties.get("soort") == "magneet":
            n_mag = sum(len(gaten.get(ijk, [])) for ijk in volgorde)
            tekst = f"{len(stukken)} pieces, holes for {n_mag} magnets of {inst.magneet} mm"
        else:
            tekst = f"{len(stukken)} pieces, {sum(a for _d, a in pennen)} pins"
        tekst += f", {rood} need attention" if rood else ", all fit"
        if meldingen:
            tekst += f". {len(meldingen)} notes in the panel"
        self.report({"WARNING"} if rood or meldingen else {"INFO"}, tekst)
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_split,)
