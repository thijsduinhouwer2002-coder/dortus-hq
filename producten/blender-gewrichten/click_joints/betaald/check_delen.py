"""Check parts (issue 42): per deel een uitslag in stap 3, en een klik selecteert de foute plek in Edit Mode.

Waarom: 3D Print Toolbox (de grootste print-add-on van Blender) toont elke controle als regel in het paneel en
selecteert met één klik de foute randen of vlakken. Onze "Check mesh" gaf alleen een aantal in de statusbalk.
Per deel (alles met cj_deel, anders de actieve mesh) drie controles:
1. open randen: randen zonder precies 2 vlakken (zoals gesloten.foute_randen);
2. losse stukken: elk stuk naast het grootste (een los stuk valt uit je print);
3. dunne wand rond een kom: vlakken van de kom waar een straal recht de wand in de buitenkant al binnen de
   ingestelde mm raakt (zoals de dikte-controle van 3D Print Toolbox, eigen code). Nu alleen bij een kogel.
De uitslag staat als JSON in scene["cj_check"]; de foute plekken worden bij een klik opnieuw berekend, zodat er
geen grote lijsten in de .blend komen.
Alleen in de betaalde build: het gratis deel blijft gelijk aan de gekeurde stand (e2e/toets_zips.py)."""
import json

import bmesh
import bpy
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

from ..eigenschappen import eenheid_per_mm
from ..passing import GRENS_ORANJE_MM
from ..uit_elkaar import echte_matrix

SLEUTEL = "cj_check"
SOORTEN = ("open", "los", "dun")
MIN_HOEK = 0.3  # de geraakte wand moet de straal tegemoet komen (cos), anders is het een hoek en geen wand


def delen(context):
    """De delen om te controleren: alle meshes met cj_deel in de scene, anders de actieve mesh."""
    lijst = sorted((o for o in context.scene.objects if o.type == "MESH" and o.get("cj_deel")), key=lambda o: o.name)
    if lijst:
        return lijst
    ob = context.active_object
    return [ob] if ob is not None and ob.type == "MESH" else []


def open_randen(me):
    """Indexen van de randen die niet precies 2 vlakken hebben."""
    if not me.edges:
        return []
    idx = np.empty(len(me.loops), dtype=np.int32)
    me.loops.foreach_get("edge_index", idx)
    telling = np.bincount(idx, minlength=len(me.edges))
    return np.flatnonzero(telling != 2).tolist()


def stuk_labels(me):
    """Per vertex het nummer van zijn stuk (kleinste vertex-index in dat stuk)."""
    n = len(me.vertices)
    lab = np.arange(n, dtype=np.int64)
    if n == 0 or not me.edges:
        return lab
    ev = np.empty(len(me.edges) * 2, dtype=np.int64)
    me.edges.foreach_get("vertices", ev)
    a, b = ev[0::2], ev[1::2]
    while True:
        oud = lab.copy()
        m = np.minimum(lab[a], lab[b])
        np.minimum.at(lab, a, m)
        np.minimum.at(lab, b, m)
        lab = lab[lab]  # pointer jumping: snel bij lange ketens
        if np.array_equal(lab, oud):
            return lab


def losse_punten(me):
    """(aantal losse stukken, indexen van hun vertices): alles behalve het grootste stuk."""
    lab = stuk_labels(me)
    if lab.size == 0:
        return 0, []
    soorten, telling = np.unique(lab, return_counts=True)
    if len(soorten) < 2:
        return 0, []
    grootste = soorten[int(np.argmax(telling))]
    return len(soorten) - 1, np.flatnonzero(lab != grootste).tolist()


def gewrichten(objecten, u=1.0):
    """(centrum, kogelstraal, speling) in wereldcoördinaten van elk kogelgewricht op een van de delen.
    Pen en scharnier nog niet: hun kom is geen bol om één punt (ontwerp, Check parts)."""
    uit = []
    for o in objecten:
        if o.get("cj_soort", "KOGEL") == "KOGEL" and "cj_centrum" in o and o.get("cj_kogel_r", 0) > 0:
            uit.append((tuple(round(x, 6) for x in o["cj_centrum"]), round(float(o["cj_kogel_r"]), 6),
                        round(float(o.get("cj_speling_mm", 0.2)) * u, 6)))
    return list(dict.fromkeys(uit))


def dunne_vlakken(ob, grens, gewr):
    """Indexen van de vlakken van een kom met een wand dunner dan grens (in scene-eenheden).

    Net als passing.beoordeel meten we vanaf de kom zelf naar buiten: alleen vlakken op de bol om het centrum
    (straal kogel + speling) met hun normaal naar het centrum (de holte in). Een straal recht de wand in moet de
    buitenkant binnen grens raken. Zo telt de scherpe rand langs de bolnaad niet mee (keurder 26 nov, moet 1)."""
    me = ob.data
    if not gewr or not me.polygons:
        return []
    m = echte_matrix(ob)
    n_v = len(me.polygons)
    mid = np.empty(n_v * 3, dtype=np.float64)
    me.polygons.foreach_get("center", mid)
    mid = mid.reshape(-1, 3) @ np.array(m.to_3x3()).T + np.array(m.translation)
    kans = np.zeros(n_v, dtype=bool)
    for p, r, sp in gewr:
        afst = np.linalg.norm(mid - np.array(p), axis=1)
        kom = r + sp
        kans |= (afst >= 0.9 * kom) & (afst <= kom + sp + 0.05 * r)
    if not kans.any():
        return []
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.transform(m)
    if m.to_3x3().determinant() < 0:
        bmesh.ops.reverse_faces(bm, faces=bm.faces[:])
    bm.normal_update()
    bm.faces.ensure_lookup_table()
    bvh = BVHTree.FromBMesh(bm)
    centra = [Vector(p) for p, _r, _s in gewr]
    eps = grens * 1e-3
    uit = []
    for i_f in np.flatnonzero(kans).tolist():
        f = bm.faces[i_f]
        c, n = f.calc_center_median(), f.normal
        if n.length < 0.5:
            continue
        dichtst = min(centra, key=lambda q: (q - c).length_squared)
        if n.dot(dichtst - c) <= 0:  # normaal van het centrum af: kogel of huid, geen kom
            continue
        hit, hn, i, _d = bvh.ray_cast(c - n * eps, -n, grens)
        if hit is not None and i != f.index and hn.dot(-n) > MIN_HOEK:
            uit.append(f.index)
    bm.free()
    return uit


def controleer(context, grens_mm):
    """Rekent de drie controles voor elk deel uit; geeft de lijst die in scene["cj_check"] komt."""
    objecten = delen(context)
    u = eenheid_per_mm(context.scene)
    grens = grens_mm * u
    gewr = gewrichten(objecten, u)
    uitslag = []
    for o in objecten:
        aantal_los, _p = losse_punten(o.data)
        uitslag.append({"naam": o.name, "open": len(open_randen(o.data)), "los": aantal_los,
                        "dun": len(dunne_vlakken(o, grens, gewr)), "gewricht": bool(gewr)})
    return uitslag


def lees(scene):
    try:
        return json.loads(scene.get(SLEUTEL, "[]"))
    except (TypeError, ValueError):
        return []


class CLICK_JOINTS_OT_check_delen(bpy.types.Operator):
    bl_idname = "click_joints.check_delen"
    bl_label = "Check parts"
    bl_description = ("Check every part before you print: open edges, loose pieces, and socket walls of a ball joint "
                      "thinner than Min wall. Click a result to select it in Edit Mode")

    @classmethod
    def poll(cls, context):
        return bool(delen(context))

    def execute(self, context):
        if context.mode != "OBJECT":
            bpy.ops.object.mode_set(mode="OBJECT")
        grens_mm = context.scene.cj_check_wand_mm
        uitslag = controleer(context, grens_mm)
        context.scene[SLEUTEL] = json.dumps(uitslag)
        fout = sum(1 for d in uitslag if d["open"] or d["los"] or d["dun"])
        if fout:
            self.report({"WARNING"}, f"{fout} of {len(uitslag)} parts need a look. Click a line to select it.")
        else:
            self.report({"INFO"}, f"All {len(uitslag)} parts OK")
        return {"FINISHED"}


class CLICK_JOINTS_OT_check_toon(bpy.types.Operator):
    bl_idname = "click_joints.check_toon"
    bl_label = "Select in Edit Mode"
    bl_description = "Open this part in Edit Mode with exactly these edges, pieces or faces selected"
    bl_options = {"REGISTER", "UNDO"}

    naam: bpy.props.StringProperty()
    soort: bpy.props.EnumProperty(items=[(s, s, "") for s in SOORTEN])

    def execute(self, context):
        ob = context.scene.objects.get(self.naam)
        if ob is None or ob.type != "MESH":
            self.report({"WARNING"}, f"{self.naam} is gone. Click Check parts again.")
            return {"CANCELLED"}
        if ob.name not in context.view_layer.objects or ob.hide_viewport or ob.library is not None:
            self.report({"WARNING"}, f"{ob.name} can't be opened here (hidden, excluded or linked).")
            return {"CANCELLED"}
        if context.mode != "OBJECT":
            bpy.ops.object.mode_set(mode="OBJECT")
        me = ob.data
        if self.soort == "open":
            kies, modus = open_randen(me), (False, True, False)
        elif self.soort == "los":
            kies, modus = losse_punten(me)[1], (True, False, False)
        else:
            u = eenheid_per_mm(context.scene)
            kies = dunne_vlakken(ob, context.scene.cj_check_wand_mm * u, gewrichten(delen(context), u))
            modus = (False, False, True)
        for reeks in (me.vertices, me.edges, me.polygons):
            reeks.foreach_set("select", np.zeros(len(reeks), dtype=bool))
        reeks = (me.vertices, me.edges, me.polygons)[modus.index(True)]
        vlag = np.zeros(len(reeks), dtype=bool)
        vlag[kies] = True
        reeks.foreach_set("select", vlag)
        if self.soort == "open":  # een rand telt in Edit Mode pas als zijn twee punten ook gekozen zijn
            ev = np.empty(len(me.edges) * 2, dtype=np.int64)
            me.edges.foreach_get("vertices", ev)
            pv = np.zeros(len(me.vertices), dtype=bool)
            pv[ev.reshape(-1, 2)[kies].ravel()] = True
            me.vertices.foreach_set("select", pv)
        elif self.soort == "dun":
            pv = np.zeros(len(me.vertices), dtype=bool)
            for i in kies:
                pv[list(me.polygons[i].vertices)] = True
            me.vertices.foreach_set("select", pv)
        me.update()
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(False)
        ob.hide_set(False)
        ob.select_set(True)
        context.view_layer.objects.active = ob
        context.scene.tool_settings.mesh_select_mode = modus
        bpy.ops.object.mode_set(mode="EDIT")
        self.report({"INFO"}, f"{ob.name}: {len(kies)} selected")
        return {"FINISHED"}


TEKST = {"open": "{n} open edges", "los": "{n} loose pieces", "dun": "{n} socket faces with a thin wall"}


def teken(layout, context):
    """In stap 3 boven Export: knop Check parts met de wandgrens, daaronder per deel de uitslag."""
    scene = context.scene
    vak = layout.column(align=True)
    rij = vak.split(factor=0.55, align=True)
    rij.operator(CLICK_JOINTS_OT_check_delen.bl_idname, icon="VIEWZOOM")
    rij.prop(scene, "cj_check_wand_mm", text="Min wall")
    uitslag = [d for d in lees(scene) if d.get("naam") in scene.objects]
    if not uitslag:
        return
    fout = [d for d in uitslag if d["open"] or d["los"] or d["dun"]]
    if not fout:
        vak.label(text=f"All {len(uitslag)} parts OK", icon="CHECKMARK")
        return
    for d in uitslag:
        if not (d["open"] or d["los"] or d["dun"]):
            vak.label(text=f"{d['naam']}: OK", icon="CHECKMARK")
            continue
        vak.label(text=d["naam"], icon="ERROR")
        for s in SOORTEN:
            if d[s]:
                knop = vak.operator(CLICK_JOINTS_OT_check_toon.bl_idname, text=TEKST[s].format(n=d[s]), icon="RESTRICT_SELECT_OFF")
                knop.naam, knop.soort = d["naam"], s


KLASSEN = (CLICK_JOINTS_OT_check_delen, CLICK_JOINTS_OT_check_toon)


def register():
    bpy.types.Scene.cj_check_wand_mm = bpy.props.FloatProperty(
        name="Min wall (mm)", default=GRENS_ORANJE_MM, min=0.1, max=10.0, step=10, precision=2,
        description="Check parts flags ball joint sockets with a wall thinner than this")


def unregister():
    if hasattr(bpy.types.Scene, "cj_check_wand_mm"):
        del bpy.types.Scene.cj_check_wand_mm
