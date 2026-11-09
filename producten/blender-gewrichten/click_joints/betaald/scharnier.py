"""Operator click_joints.plaats_scharnier ("Place hinge") en de knoppen in het paneel (alleen betaalde build).

Lidas L: de Z-as van de 3D-cursor (de snede staat daar dwars op, zoals bij as-bron Cursor van de kogel).
Scharnieras H (ontwerp betaald v1.1, invoer b): bij as-bron View direction de kijkrichting geprojecteerd
loodrecht op L; maakt die minder dan 30 graden met L, dan een melding en geen scharnier. Bij as-bron Cursor
de X-as van de cursor. Buigkant: omhoog op het scherm (bij Cursor de Y-as van de cursor).
De vorm zelf staat in scharnier_vorm.py, de beweegproef (eis 2) in scharnier_beweeg.py. Nog niet in deze ronde:
passingkleur, Exploded view.
Klikneuzen (eis 3) en de maten van de zaagsnede (vorm punt 5) in scharnier_neus.py.
Flip bend (eigenschap flip_bend, ontwerp punt 4): keert H en de buigkant samen om, dus de stop en de
achterstop komen aan de andere kant van het lid; in het Redo-paneel snijdt omzetten het scharnier opnieuw."""
import math
import time

import bmesh
import bpy
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty
from mathutils import Vector
from mathutils.bvhtree import BVHTree

from ..eigenschappen import eenheid_per_mm
from ..gesloten import gespiegeld, is_gesloten
from ..gewricht import kijk_regio, ruim_op, solver_naam, verhuis
from ..uit_elkaar import echte_matrix
from . import scharnier_beweeg as beweeg
from . import scharnier_neus as neus
from . import scharnier_vorm as vorm

STAND_KEUZES = [(str(n), f"{n}°", f"Bends up to {n}°") for n in vorm.STANDEN]


def kijk_en_omhoog(context, kijk=None, omhoog=None):
    """(kijkrichting, omhoog) in wereldcoordinaten, of None zonder 3D-weergave.

    Een meegegeven kijkrichting (eigenschap kijk_richting van de operator, lengte groter dan 0) gaat voor;
    zo kan de toets in Blender zonder venster de echte operator met een kijkrichting draaien."""
    if kijk is not None and Vector(kijk).length > 1e-9:
        om = Vector(omhoog) if omhoog is not None and Vector(omhoog).length > 1e-9 else None
        return Vector(kijk).normalized(), om
    rv3d = kijk_regio(context)
    if rv3d is None:
        return None
    return (rv3d.view_rotation @ Vector((0, 0, -1))).normalized(), rv3d.view_rotation @ Vector((0, 1, 0))


def assen(context, inst, kijk=None, omhoog=None, omdraaien=False):
    """(punt, H, buigkant, L, as-bron, terugval) of None als de kijkrichting te dicht bij de lidas ligt."""
    cursor = context.scene.cursor
    m = cursor.matrix
    lid = m.col[2].xyz.normalized()
    if inst.as_bron == "KIJK":
        ko = kijk_en_omhoog(context, kijk, omhoog)
        if ko is not None:
            uit = vorm.scharnier_assen(lid, kijk=ko[0], omhoog=ko[1], omdraaien=omdraaien)
            return None if uit is None else (cursor.location.copy(),) + uit[:3] + ("KIJK", False)
    uit = vorm.scharnier_assen(lid, cursor_x=m.col[0].xyz, cursor_y=m.col[1].xyz, omdraaien=omdraaien)
    return (cursor.location.copy(),) + uit[:3] + ("CURSOR", inst.as_bron == "KIJK")


class CLICK_JOINTS_OT_plaats_scharnier(bpy.types.Operator):
    bl_idname = "click_joints.plaats_scharnier"
    bl_label = "Place hinge"
    bl_description = "Cut the mesh at the 3D cursor into two watertight parts with a hinge and an end stop"
    bl_options = {"REGISTER", "UNDO"}

    stand: EnumProperty(name="Bends up to", items=STAND_KEUZES, default=str(vorm.STAND_STANDAARD))
    flip_bend: BoolProperty(name="Flip bend", default=False,
                            description="Bend the other way: the end stop moves to the other side of the part")
    # Leeg (0, 0, 0) = kijkrichting uit de 3D-weergave. Alleen voor scripts en de toets zonder venster.
    kijk_richting: FloatVectorProperty(size=3, default=(0.0, 0.0, 0.0), options={"HIDDEN", "SKIP_SAVE"})
    kijk_omhoog: FloatVectorProperty(size=3, default=(0.0, 0.0, 0.0), options={"HIDDEN", "SKIP_SAVE"})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        t0 = time.perf_counter()
        bron = context.active_object
        inst = context.scene.click_joints
        dg = context.evaluated_depsgraph_get()
        ok, fout = is_gesloten(bron, dg)
        if not ok:
            self.report({"ERROR"}, f"The mesh {bron.name} is not watertight ({fout} edges without exactly "
                                   "2 faces). Click Make watertight first.")
            return {"CANCELLED"}
        uit = assen(context, inst, kijk=self.kijk_richting, omhoog=self.kijk_omhoog, omdraaien=self.flip_bend)
        if uit is None:
            self.report({"WARNING"}, vorm.KIJK_LANGS)
            return {"CANCELLED"}
        punt, h, buig, lid, as_bron, terugval = uit
        # Controleur (d), punt 1: niet opnieuw snijden op dezelfde plek van een bestaand scharnier (bijvoorbeeld na
        # het omzetten van Flip bend in het paneel). Een tweede gewricht elders op het deel mag wel.
        if bron.get("cj_soort") == "SCHARNIER" and "cj_snijpunt" in bron:
            vorige = Vector(bron["cj_snijpunt"])
            if (Vector(punt) - vorige).length < 2.0 * float(bron.get("cj_knokkel_r", 0.0)) + 1e-9:
                self.report({"WARNING"}, "There is already a hinge here. Undo first, or use Flip bend in the "
                                         "Redo panel right after placing.")
                return {"CANCELLED"}
        if terugval:
            self.report({"WARNING"}, "No 3D viewport found for the view direction; the hinge axis now follows "
                                     "the X axis of the 3D cursor.")
        u = eenheid_per_mm(context.scene)
        s = inst.speling_mm * u
        frame = vorm.frame_scharnier(punt, h, buig, lid)

        me = bpy.data.meshes.new_from_object(bron.evaluated_get(dg))
        me.transform(echte_matrix(bron))
        bm = bmesh.new()
        bm.from_mesh(me)
        if gespiegeld(bron):
            bmesh.ops.reverse_faces(bm, faces=bm.faces[:])
            bm.to_mesh(me)
        bvh = BVHTree.FromBMesh(bm)
        bm.free()
        maat, reden = vorm.maten(bvh, frame, s, int(self.stand), u)
        if maat is not None:
            # Eis 3: klikneus en rek, of Tight (dan geen scharnier); de sleuf nooit door de onderkant van A.
            reden = neus.maten_neus(maat, u, neus.zaag_diepte(bvh, frame, maat))
            maat = None if reden else maat
        if maat is None:
            bpy.data.meshes.remove(me)
            self.report({"WARNING"}, reden)
            return {"CANCELLED"}
        hulp = bpy.data.collections.new("cj_hulp")
        context.scene.collection.children.link(hulp)
        werk = bpy.data.objects.new("cj_werk", me)
        hulp.objects.link(werk)
        solver = solver_naam()
        try:
            deel_a, deel_b = vorm.snij(hulp, werk, frame, maat, solver)
        except RuntimeError as e:  # controleur (d), punt 4: geen hulpobjecten achterlaten
            ruim_op(hulp)
            self.report({"ERROR"}, f"The cut failed ({e}); the mesh is unchanged.")
            return {"CANCELLED"}
        uitslag = [is_gesloten(d.data) for d in (deel_a, deel_b)]
        if not all(ok for ok, _ in uitslag):
            ruim_op(hulp)
            self.report({"ERROR"}, "The cut gave no watertight parts (bad edges: part A "
                                   f"{uitslag[0][1]}, part B {uitslag[1][1]}); the mesh is unchanged.")
            return {"CANCELLED"}
        draaipunt = frame @ Vector((0, -maat["e"], 0))
        gegevens = {"cj_bron": bron.name, "cj_soort": "SCHARNIER", "cj_speling_mm": inst.speling_mm,
                    "cj_as": list(lid), "cj_scharnier_as": list(h), "cj_buigkant": list(buig),
                    "cj_scharnier_punt": list(draaipunt), "cj_snijpunt": list(punt), "cj_as_bron": as_bron,
                    "cj_as_terugval": terugval, "cj_knokkel_r": maat["r"], "cj_naad_r": maat["rn"],
                    "cj_tong_half": maat["tw"], "cj_stand": maat["stand"], "cj_solver": solver,
                    "cj_wig_graden": round(math.degrees(maat["alfa"]), 3), "cj_theta_s": maat["theta_s"], "cj_t_vlak": maat["t_vlak"], "cj_gespiegeld": gespiegeld(bron),
                    "cj_flip_bend": bool(self.flip_bend), "cj_neus_h": maat["neus_h"],
                    "cj_neus_klik": maat["neus_klik"],
                    "cj_neus_voet": maat["neus_voet"], "cj_wang_t": maat["wang_t"], "cj_lip": maat["lip"],
                    "cj_rek": maat["rek"], "cj_zaag_diepte": maat.get("zaag_diepte", -1.0)}
        # Beweegproef om H (eis 2) op de delen in wereldcoordinaten, voor ze verhuizen.
        voor, achter = beweeg.bereik(deel_a, deel_b, draaipunt, h, buig, lid,
                                     1.5 * math.hypot(maat["wx"], maat["wy"]) + maat["rn"])
        if voor is None:
            ruim_op(hulp)
            self.report({"ERROR"}, "The parts overlap before they move; the mesh is unchanged.")
            return {"CANCELLED"}
        gegevens["cj_bereik_graden"] = round(voor, 2)
        gegevens["cj_achter_graden"] = round(achter, 2)
        gegevens["cj_r_lip"] = maat["r_lip"]
        for deel, letter in ((deel_a, "A"), (deel_b, "B")):
            verhuis(deel, f"{bron.name}_{letter}", bron)
            deel["cj_deel"] = letter
        ruim_op(hulp)
        gegevens["cj_duur_s"] = round(time.perf_counter() - t0, 3)
        for deel in (deel_a, deel_b):
            for k, v in gegevens.items():
                deel[k] = v
        bron.hide_set(True)
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(False)
        context.view_layer.objects.active = deel_a
        kop = "Hinge placed, bend flipped" if self.flip_bend else "Hinge placed"
        melding = f"{kop}. {beweeg.tekst(voor, maat['stand'])}."
        if beweeg.geen_stop(voor):
            melding = f"{kop}, but no end stop was found. Check the shape near the joint."
        for deel in (deel_a, deel_b):
            deel["cj_melding"] = melding
        self.report({"WARNING"} if beweeg.geen_stop(voor) else {"INFO"}, f"{melding} {gegevens['cj_duur_s']} s.")
        return {"FINISHED"}


def teken_knop(self, context):
    """Kleine knoppen onder het paneel van de kern: drie standen als knoppen, dan Place hinge."""
    if context.active_object is None:
        return
    vak = self.layout.box()
    vak.label(text="Place hinge, bends up to:")
    rij = vak.row(align=True)
    wm = context.window_manager
    flip = bool(getattr(wm, "cj_flip_bend", False))
    for n in vorm.STANDEN:
        op = rij.operator(CLICK_JOINTS_OT_plaats_scharnier.bl_idname, text=f"{n}°")
        op.stand = str(n)
        op.flip_bend = flip
    if hasattr(wm, "cj_flip_bend"):
        vak.prop(wm, "cj_flip_bend", toggle=True)


KLASSEN = (CLICK_JOINTS_OT_plaats_scharnier,)
