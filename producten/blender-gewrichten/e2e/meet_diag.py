"""Meting betrouwbaarheid Figure from rig (Betrouwbaarheid, 23 nov 2026): meetregels rond elke snede.

Wordt vanuit meet_rig.py geladen nadat de Pro-zip aan staat. Verandert niets aan de uitkomst van de knop: de omhulsels
roepen het echte werk aan en schrijven alleen op wat er gebeurde.
- `figuur.plaats_gewricht`: per poging het gewricht, de plek, ok en de melding.
- `gewricht.snij` (buitenom, dus ook om de terugval van Pro): per snede de solver, wat een_lid besloot (lussen,
  soort H), gesloten of niet, en bij open randen waar die liggen in het frame van de snede (hoogte boven het
  snijvlak, afstand tot de as, afstand tot het kogelmidden). Ook de overlap van deel A en B in rust (driehoeken die
  elkaar snijden, zonder de paren die allebei op het snijvlak liggen): een kapotte snede die wel gesloten is.
- Met CJ_PROEVEN=1: na een slechte snede dezelfde snede nog eens op andere manieren (Exact, vlak verschoven, vlak
  een fractie gedraaid), alleen om te meten; de uitkomst van de knop blijft die van de eerste snede.
"""
import importlib
import math
import os
import time

import bpy
import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

POGINGEN, SNEDEN = [], []
KEUS = ("lussen", "lid", "h_soort", "lid_open", "vreemd", "marge", "h_voxel", "h_vlakken", "h_buiten", "h_buiten_om", "h_pogingen")
_HUIDIG = {}


def mod(naam):
    return importlib.import_module(f"bl_ext.user_default.click_joints.{naam}")


def bvh_van(ob):
    me = ob.data
    mw = ob.matrix_world
    return BVHTree.FromPolygons([mw @ v.co for v in me.vertices], [tuple(p.vertices) for p in me.polygons])


def zelf_overlap(ob):
    """Paren driehoeken van één mesh die elkaar snijden (zonder gedeelde punten): zelfdoorsnijding."""
    me = ob.data
    vlakken = [set(p.vertices) for p in me.polygons]
    bvh = bvh_van(ob)
    return sum(1 for i, j in bvh.overlap(bvh) if i < j and not (vlakken[i] & vlakken[j]))


def foute_randen(me):
    """[(rand, aantal vlakken)] voor elke rand met een ander aantal vlakken dan 2."""
    idx = np.empty(len(me.loops), dtype=np.int32)
    me.loops.foreach_get("edge_index", idx)
    tel = np.bincount(idx, minlength=len(me.edges))
    return [(int(i), int(tel[i])) for i in np.nonzero(tel != 2)[0]]


def open_plekken(ob, frame, maat, n=8):
    """Waar liggen de foute randen? Hoogte boven het snijvlak, straal tot de as, afstand tot het kogelmidden."""
    me = ob.data
    fout = foute_randen(me)
    if not fout:
        return {"aantal": 0}
    inv = frame.inverted()
    mz = maat.get("midden_z", 0.0)
    vlak = maat.get("schuif", 0.0) + (mz if "naad_r" in maat else 0.0)
    uit = {"aantal": len(fout), "vlakken_per_rand": sorted({k for _i, k in fout}), "plekken": []}
    for i, k in fout[:n]:
        e = me.edges[i]
        a, b = (inv @ (ob.matrix_world @ me.vertices[v].co) for v in e.vertices)
        p = (a + b) / 2
        d = (p - Vector((0, 0, mz))).length
        uit["plekken"].append({"vlakken": k, "z_vlak": round(p.z - vlak, 4), "rho": round(p.xy.length, 3),
                               "d_mid": round(d, 3), "d_naad": round(d - maat.get("naad_r", 0.0), 4),
                               "d_kogel": round(d - maat["r"], 4), "lengte": round((a - b).length, 5)})
    return uit


def overlap_ab(deel_a, deel_b, frame, maat):
    """Paren driehoeken van A en B die elkaar snijden, zonder paren die allebei het snijvlak raken (daar liggen A en B
    vlak tegen elkaar, dat is goed)."""
    inv = frame.inverted()
    mz = maat.get("midden_z", 0.0)
    vlak = maat.get("schuif", 0.0) + (mz if "naad_r" in maat else 0.0)
    tol = 2e-3 * maat["r"]

    def raakt_vlak(ob):
        me = ob.data
        zs = [(inv @ (ob.matrix_world @ v.co)).z for v in me.vertices]
        return [any(abs(zs[v] - vlak) < tol for v in p.vertices) for p in me.polygons]
    ra, rb = raakt_vlak(deel_a), raakt_vlak(deel_b)
    paren = bvh_van(deel_a).overlap(bvh_van(deel_b))
    return sum(1 for i, j in paren if not (ra[i] and rb[j]))


def herstel_proef(ob):
    """Alleen meten: wordt een deel met randen van 4 vlakken gesloten als je die randen splitst?"""
    import bmesh
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    vier = [e for e in bm.edges if len(e.link_faces) == 4]
    if not vier:
        bm.free()
        return None
    bmesh.ops.split_edges(bm, edges=vier)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return {"vier": len(vier), "fout_na": fout}


def staat(deel_a, deel_b, frame, maat, zelf=False):
    ges = mod("gesloten")
    uit = {}
    for letter, d in (("A", deel_a), ("B", deel_b)):
        ok, fout = ges.is_gesloten(d.data)
        uit[letter] = {"gesloten": ok, "fout": fout, "punten": len(d.data.vertices)}
        if zelf:
            uit[letter]["zelf"] = zelf_overlap(d)
        if not ok:
            uit[letter]["open"] = open_plekken(d, frame, maat)
            uit[letter]["herstel"] = herstel_proef(d)
    uit["overlap_ab"] = overlap_ab(deel_a, deel_b, frame, maat)
    uit["goed"] = uit["A"]["gesloten"] and uit["B"]["gesloten"] and uit["overlap_ab"] == 0
    return uit


def _ruim(hulp, houd):
    for ob in [o for o in hulp.objects if o.name not in houd]:
        me = ob.data
        bpy.data.objects.remove(ob)
        if me is not None and me.users == 0:
            bpy.data.meshes.remove(me)


def proeven(oud, hulp, werk, frame, maat, soort, solver):
    """Dezelfde snede op andere manieren, alleen meten. Geeft {naam: goed/fout-tekst}."""
    een_lid = mod("een_lid")
    bewaar = {k: (dict(v) if isinstance(v, dict) else v) for k, v in een_lid.STAND.items()}
    uit = {}
    u = maat["s"] / 0.2 if maat.get("s") else 1.0
    varianten = [
        ("exact", frame, "EXACT"),
        ("exact_zelf", frame, "EXACT"),
        ("schuif_0.05", frame @ Matrix.Translation((0, 0, 0.05 * u)), solver),
        ("draai_0.3", frame @ Matrix.Rotation(math.radians(0.3), 4, "X"), solver),
        ("draai_1.0", frame @ Matrix.Rotation(math.radians(1.0), 4, "X"), solver),
    ]
    for naam, f, sv in varianten:
        voor = {o.name for o in hulp.objects}
        een_lid.STAND.update({k: (dict(v) if isinstance(v, dict) else v) for k, v in bewaar.items()})
        if een_lid.STAND.get("h") is not None:
            een_lid.STAND["solver"] = sv
            een_lid.STAND["bronnen"] = {}
        t0 = time.perf_counter()
        gw = mod("gewricht")
        zelf_oud = gw.EXACT_ZELF
        gw.EXACT_ZELF = naam == "exact_zelf"
        try:
            a, b = oud(hulp, werk, f, maat, soort, sv)
            st = staat(a, b, f, maat)
            uit[naam] = {"goed": st["goed"], "A": st["A"]["fout"], "B": st["B"]["fout"], "overlap": st["overlap_ab"],
                         "s": round(time.perf_counter() - t0, 2)}
        except Exception as e:  # meten mag de knop nooit breken
            uit[naam] = {"fout": str(e)[:200]}
        gw.EXACT_ZELF = zelf_oud
        _ruim(hulp, voor)
    een_lid.STAND.update(bewaar)
    return uit


def instrumenteer():
    gw = mod("gewricht")
    fig = mod("betaald.figuur")
    rig = mod("betaald.rig")
    een_lid = mod("een_lid")
    oud_snij, oud_plaats, oud_vast = gw.snij, fig.plaats_gewricht, rig.kogel_vast
    oud_verloren = rig.verloren_stuk

    def snij(hulp, werk, frame, maat, soort, solver):
        t0 = time.perf_counter()
        a, b = oud_snij(hulp, werk, frame, maat, soort, solver)
        rec = {"poging": len(POGINGEN), "gewricht": _HUIDIG.get("naam"), "soort": soort, "solver": solver,
               "terugval": bool(a.get("cj_solver_terugval")), "s": round(time.perf_counter() - t0, 2),
               "r_mm": round(maat["r"], 3), "naad_r": round(maat.get("naad_r", -1.0), 3),
               "een_lid": {k: een_lid.LAATSTE.get(k) for k in KEUS}}
        try:
            rec.update(staat(a, b, frame, maat, zelf=True))
            rec["werk_zelf"] = zelf_overlap(werk)
            if een_lid.STAND.get("h") is not None:
                rec["h_zelf_overlap"] = zelf_overlap(een_lid.STAND["h"])
            if not rec["goed"] and os.environ.get("CJ_PROEVEN"):
                rec["proeven"] = proeven(oud_snij, hulp, werk, frame, maat, soort, solver)
        except Exception as e:
            rec["meetfout"] = str(e)[:200]
        SNEDEN.append(rec)
        return a, b

    def plaats(context, sleutel, naam=None, graden_vrij=0, herkomst="preset"):
        _HUIDIG["naam"] = naam
        bron = context.active_object
        t0 = time.perf_counter()
        ok, melding, nieuw = oud_plaats(context, sleutel, naam, graden_vrij, herkomst)
        rec = {"gewricht": naam, "ok": ok, "melding": melding, "s": round(time.perf_counter() - t0, 2),
               "plek": [round(c, 3) for c in context.scene.cursor.location]}
        if ok and nieuw and sleutel in ("SHOULDER", "HIP", "NECK"):
            # Keuring A, M1: verlies ook bij elke kogelsnede, in nulstand en tak op dezelfde manier gemeten
            # (rig.verloren_stuk, bol van 15 mm rond de cursor overgeslagen).
            try:
                u = mod("eigenschappen").eenheid_per_mm(context.scene)
                rec["verloren_diag"] = round(oud_verloren(context, bron, nieuw, context.scene.cursor.location.copy(),
                                                          15 * u), 4)
            except Exception as e:
                rec["verloren_diag"] = f"fout {e}"[:120]
        POGINGEN.append(rec)
        return ok, melding, nieuw

    def vast(nieuw):
        uit = oud_vast(nieuw)
        if POGINGEN:
            POGINGEN[-1]["blocked"] = uit
            g = [list(d.get("cj_buig_graden", [])) for d in nieuw or [] if d.get("cj_deel") == "B"]
            POGINGEN[-1]["buig"] = [round(x, 1) for x in g[0]] if g else None
        return uit

    def verloren(context, bron, nieuw, centrum, straal, n=400):
        uit = oud_verloren(context, bron, nieuw, centrum, straal, n)
        if POGINGEN is not None:
            _HUIDIG["verloren"] = round(uit, 4)
            SNEDEN[-1]["verloren"] = round(uit, 4) if SNEDEN else None
        return uit

    rig.verloren_stuk = verloren
    if os.environ.get("CJ_OMHULSEL_UIT"):
        mod("betaald.omhulsel").AAN[0] = False
    gw.snij, fig.plaats_gewricht, rig.kogel_vast = snij, plaats, vast
    sv = mod("betaald.scharnier_vorm")
    oud_scharnier = sv.snij

    def snij_scharnier(hulp, werk, frame, m, solver):
        a, b = oud_scharnier(hulp, werk, frame, m, solver)
        ges = mod("gesloten")
        rec = {"poging": len(POGINGEN), "gewricht": _HUIDIG.get("naam"), "soort": "SCHARNIER", "solver": solver,
               "een_lid": {k: een_lid.LAATSTE.get(k) for k in KEUS}}
        for letter, d in (("A", a), ("B", b)):
            ok, fout = ges.is_gesloten(d.data)
            rec[letter] = {"gesloten": ok, "fout": fout, "punten": len(d.data.vertices)}
            try:
                rec[letter]["zelf"] = zelf_overlap(d)
                if not ok:
                    rec[letter]["herstel"] = herstel_proef(d)
            except Exception as e:
                rec["meetfout"] = str(e)[:200]
        rec["goed"] = rec["A"]["gesloten"] and rec["B"]["gesloten"]
        if not rec["goed"] and solver == "EXACT" and os.environ.get("CJ_PROEVEN"):
            rec["proeven"] = proeven_scharnier(oud_scharnier, hulp, werk, frame, m, solver)
        SNEDEN.append(rec)
        return a, b

    sv.snij = snij_scharnier


def proeven_scharnier(oud, hulp, werk, frame, m, solver):
    """Alleen meten: dezelfde scharniersnede met Exact en Self Intersection aan, en een fractie verschoven."""
    een_lid = mod("een_lid")
    gw = mod("gewricht")
    ges = mod("gesloten")
    bewaar = {k: (dict(v) if isinstance(v, dict) else v) for k, v in een_lid.STAND.items()}
    uit = {}
    for naam, f, zelf in (("exact_zelf", frame, True), ("schuif_0.05", frame @ Matrix.Translation((0, 0, 0.05)), False)):
        voor = {o.name for o in hulp.objects}
        een_lid.STAND.update({k: (dict(v) if isinstance(v, dict) else v) for k, v in bewaar.items()})
        if een_lid.STAND.get("h") is not None:
            een_lid.STAND["bronnen"] = {}
        zelf_oud = gw.EXACT_ZELF
        gw.EXACT_ZELF = zelf
        try:
            a, b = oud(hulp, werk, f, m, solver)
            uit[naam] = {"A": ges.is_gesloten(a.data)[1], "B": ges.is_gesloten(b.data)[1],
                         "goed": ges.is_gesloten(a.data)[0] and ges.is_gesloten(b.data)[0],
                         "punten": [len(a.data.vertices), len(b.data.vertices)]}
        except Exception as e:
            uit[naam] = {"fout": str(e)[:200]}
        gw.EXACT_ZELF = zelf_oud
        _ruim(hulp, voor)
    een_lid.STAND.update(bewaar)
    return uit
