"""Robot-actiefiguur voor de filmpjes van Click Joints Pro (23 nov 2026, opdracht hoofdchat ±14:35 NL: "het mensfiguur
is super nep, een robot of actiefiguur, maar dan goed gedaan").

Helemaal door ons gemaakt met dit script (geen download, geen AI-model, geen merk of bekend personage): strakke vormen
met afgeronde randen, wit pantser met oranje en blauw, metalen gewrichten, een helm met een donker vizier en
twee lichtblauwe oog-leds. De ledematen hebben de lengtes van het MakeHuman-figuur dat 8 tot 9 gewrichten gaf
(bovenarm, dij en scheen lang genoeg voor kogel plus scharnier), met een spleet tussen de dijen en tussen arm en romp.
Bij de gewrichten blijft het lid een gladde metalen buis; het pantser zit alleen in het midden van elk lid, zodat de
kogel of het scharnier van de add-on vrij kan draaien.

Gebruik (na het installeren van de Pro-zip, want Make watertight van de add-on maakt er één gesloten mesh van):
    import figuur_robot as R
    arm, fig, punten = R.laad_robot(220.0)              # stijl={"wit": "...", ...} mag
De rig heeft Mixamo-namen (zelfde rig als e2e/proef_mens.py: linkerknie 120 en linkerelleboog 140 in Limit Rotation).
Kijkt naar -y, links is +x, voeten op z=0, maten in mm (bij 220 mm hoog).
"""
import math
import os

import bpy
import bmesh
from mathutils import Matrix, Vector

import figuur_laden as FL

# Kleuren (sRGB hex). wit: pantser, oranje en blauw: accenten, metaal: gewrichten en handen, vizier en led: gezicht.
STIJL = {
    "wit": "F3F1EA", "oranje": "FF6A1F", "blauw": "1F44B0", "metaal": "8E95A3",
    "donker": "3A404D", "vizier": "15171E", "led": "4DF0FF",
}
STIJL_B = {"wit": "FFD23F", "oranje": "E8364F", "blauw": "1B1F3B", "metaal": "8A909C", "led": "7CFF6B"}
METAAL = ("metaal",)
LICHT = ("led",)


def punten(h=220.0):
    """Gewrichtspunten in mm bij hoogte h (zelfde sleutels als de MakeHuman-punten, voor maak_rig)."""
    f = h / 220.0
    p = {
        "pelvis": (0, 0, 118), "spine-4": (0, 0, 124), "spine-2": (0, 0, 145), "spine-1": (0, 0, 163),
        "neck": (0, 0, 180), "head": (0, 0, 192), "head-2": (0, 0, 219),
    }
    for k, s in (("l", 1), ("r", -1)):
        p.update({
            f"{k}-upper-leg": (15 * s, 0, 116), f"{k}-knee": (17 * s, -1, 57), f"{k}-ankle": (18 * s, 1, 14),
            f"{k}-foot-1": (18 * s, -17, 3),
            f"{k}-clavicle": (4 * s, 0, 174), f"{k}-shoulder": (29 * s, 0, 174), f"{k}-elbow": (48 * s, -1, 136),
            f"{k}-hand": (59 * s, -3, 108), f"{k}-hand-2": (62 * s, -4, 100),
        })
    return {n: Vector(c) * f for n, c in p.items()}


def rig_punten(p, f=1.0):
    """Punten voor de rig: als die van de vormen, maar elleboog en knie dicht bij de huid aan de buigkant (4,4 mm),
    zoals bij een echte arm. Het scharnier van de add-on meet zijn stopvlakken vanaf het bot naar de buigkant; met het
    bot in het midden van een dikke buis reikt het ver langs het lid (elleboog 35 mm, proef 23 nov) en is er geen plek
    meer voor de kogel van schouder of heup. Elleboog buigt naar voren (-y), knie naar achteren (+y)."""
    q = dict(p)
    for k in "lr":
        q[f"{k}-elbow"] = p[f"{k}-elbow"] + Vector((0, -3.0, 0)) * f
        q[f"{k}-knee"] = p[f"{k}-knee"] + Vector((0, 3.0, 0)) * f
    return q


class Bouwer:
    """Verzamelt gesloten vormen in één bmesh, elk vlak met een materiaal-index."""

    def __init__(self, namen):
        self.bm = bmesh.new()
        self.namen = list(namen)

    def _klaar(self, geom, mat, m):
        vs = [g for g in geom if isinstance(g, bmesh.types.BMVert)]
        bmesh.ops.transform(self.bm, matrix=m, verts=vs)
        fs = {f for v in vs for f in v.link_faces}
        i = self.namen.index(mat)
        for fc in fs:
            fc.material_index = i
            fc.smooth = True

    def doos(self, mid, maat, mat, rond=2.0, draai=None, seg=3, taps=None):
        """Afgeronde doos: maat (b, d, h) in mm, rond = straal van de randen. taps=(fx, fy): onderkant smaller."""
        bm = self.bm
        oud = set(bm.verts)
        r = bmesh.ops.create_cube(bm, size=1.0)
        vs = r["verts"]
        bmesh.ops.scale(bm, vec=Vector(maat), verts=vs)
        if taps:
            for v in vs:
                if v.co.z < 0:
                    v.co.x *= taps[0]
                    v.co.y *= taps[1]
        es = list({e for v in vs for e in v.link_edges})
        rond = min(rond, 0.49 * min(maat))
        if rond > 0.05:
            bmesh.ops.bevel(bm, geom=list(vs) + es, offset=rond, segments=seg, affect="EDGES", profile=0.5)
        nieuw = [v for v in bm.verts if v not in oud]
        m = Matrix.Translation(Vector(mid)) @ (draai.to_4x4() if draai is not None else Matrix.Identity(4))
        self._klaar(nieuw, mat, m)

    def bol(self, mid, r, mat, schaal=(1, 1, 1)):
        bm = self.bm
        oud = set(bm.verts)
        bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=r)
        nieuw = [v for v in bm.verts if v not in oud]
        self._klaar(nieuw, mat, Matrix.Translation(Vector(mid)) @ Matrix.Diagonal(Vector(schaal)).to_4x4())

    def buis(self, a, b, r1, r2, mat, bollen=True, seg=32):
        """Kegelbuis van a naar b (straal r1 bij a, r2 bij b), met bollen op de einden als bollen=True."""
        a, b = Vector(a), Vector(b)
        bm = self.bm
        oud = set(bm.verts)
        L = (b - a).length
        bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r1, radius2=r2, depth=L)
        nieuw = [v for v in bm.verts if v not in oud]
        q = (b - a).normalized().to_track_quat("Z", "Y")
        self._klaar(nieuw, mat, Matrix.Translation((a + b) / 2) @ q.to_matrix().to_4x4())
        if bollen:
            self.bol(a, r1, mat)
            self.bol(b, r2, mat)

    def schaal_langs(self, a, b, t0, t1, r0, r1, mat, rond=2.0, ovaal=(1.0, 1.0)):
        """Pantserschaal om een lid: stuk t0..t1 van a naar b, straal r0 naar r1, afgeronde randen."""
        a, b = Vector(a), Vector(b)
        p0, p1 = a.lerp(b, t0), a.lerp(b, t1)
        bm = self.bm
        oud = set(bm.verts)
        L = (p1 - p0).length
        bmesh.ops.create_cone(bm, cap_ends=True, segments=40, radius1=r0, radius2=r1, depth=L)
        nieuw = [v for v in bm.verts if v not in oud]
        es = list({e for v in nieuw for e in v.link_edges if len(e.link_faces) == 2 and
                   e.calc_face_angle(0) > 0.6})
        if es and rond > 0.05:
            bmesh.ops.bevel(bm, geom=es, offset=min(rond, 0.45 * L, 0.45 * min(r0, r1)), segments=3,
                            affect="EDGES", profile=0.5)
            nieuw = [v for v in bm.verts if v not in oud]
        for v in nieuw:
            v.co.x *= ovaal[0]
            v.co.y *= ovaal[1]
        self._klaar(nieuw, mat, Matrix.Translation((p0 + p1) / 2) @ _richting(p0, p1).to_4x4())


def _richting(a, b, op=Vector((0, -1, 0))):
    """Draaiing die z naar (b - a) zet en y zo veel mogelijk naar `op`."""
    z = (Vector(b) - Vector(a)).normalized()
    x = op.cross(z).normalized()
    y = z.cross(x).normalized()
    return Matrix((x, y, z)).transposed()


def bouw_vormen(p, f=1.0):
    """Alle vormen van de robot (maten in mm bij 220 mm, f schaalt mee). Geeft (bmesh, namen)."""
    namen = ["wit", "oranje", "blauw", "metaal", "donker", "vizier", "led"]
    B = Bouwer(namen)
    s = f

    def P(*c):
        return Vector(c) * s

    # ---- romp ----
    B.doos(P(0, 0.5, 163), P(50, 27, 33), "wit", rond=7.5 * s, taps=(0.64, 0.86))   # borstkas, smal naar de taille
    B.doos(P(0, -11.6, 164), P(30, 8, 19), "oranje", rond=3.6 * s, taps=(0.78, 1.0))    # borstplaat
    B.buis(P(0, -14.8, 164), P(0, -16.6, 164), 7.0 * s, 6.6 * s, "donker", bollen=False)   # ring om de kern
    B.buis(P(0, -15.4, 164), P(0, -17.6, 164), 4.8 * s, 4.6 * s, "led", bollen=False)      # kern
    for k in (1, -1):
        B.doos(P(13 * k, 0.5, 174.5), P(13, 22, 5), "blauw", rond=2.2 * s)    # schouderranden op de borst
    B.doos(P(0, 0.5, 149.2), P(35, 27.6, 4.0), "blauw", rond=1.8 * s)          # band onder de borst
    B.doos(P(0, 1, 141.5), P(27, 19, 23), "metaal", rond=4 * s)                # buik, van bekken tot borst
    for z in (138.5, 143, 147.5):
        B.doos(P(0, 1, z), P(30, 21, 2.6), "donker", rond=1.2 * s)           # ribbels
    B.doos(P(0, 0.5, 126.5), P(40, 23, 12), "blauw", rond=4.5 * s, taps=(0.86, 0.95))   # bekken
    B.doos(P(0, -10.6, 127.5), P(11, 3, 7), "oranje", rond=1.5 * s)            # gesp
    B.doos(P(0, 1, 179), P(14, 12, 5), "metaal", rond=2 * s)                 # kraag
    # ---- nek en hoofd ----
    B.buis(p["neck"] - P(0, 0, 2), p["head"] - P(0, 0, 1), 5.6 * s, 5.2 * s, "metaal")
    B.doos(P(0, 0.5, 204), P(34, 31, 31), "wit", rond=10 * s)                 # helm
    B.doos(P(0, -12.9, 202.5), P(27, 6, 11), "vizier", rond=3.4 * s)         # vizier
    for k in (1, -1):
        B.doos(P(6.4 * k, -15.8, 203.0), P(6.4, 1.4, 3.2), "led", rond=0.6 * s)   # oog-leds
        B.buis(P(15.2 * k, 1, 203.5), P(17.6 * k, 1, 203.5), 5.4 * s, 4.8 * s, "blauw", bollen=False)   # oren
        B.buis(P(17.4 * k, 1, 203.5), P(18.4 * k, 1, 203.5), 2.7 * s, 2.7 * s, "oranje", bollen=False)
    B.doos(P(0, 1.5, 218.2), P(5, 18, 4.4), "oranje", rond=2.0 * s)            # kam
    B.doos(P(0, -14.6, 211.2), P(9, 3, 2.4), "blauw", rond=1.0 * s)          # voorhoofd
    B.doos(P(0, -12.9, 193.6), P(14, 4, 3.2), "donker", rond=1.2 * s)        # mondrooster
    # ---- armen ----
    for k in "lr":
        sx = 1 if k == "l" else -1
        sh, el, ha, h2 = p[f"{k}-shoulder"], p[f"{k}-elbow"], p[f"{k}-hand"], p[f"{k}-hand-2"]
        B.buis(sh, el, 7.6 * s, 7.4 * s, "donker")
        B.schaal_langs(sh, el, 0.40, 0.66, 9.4 * s, 9.0 * s, "wit", rond=2.2 * s, ovaal=(1.0, 0.92))
        B.schaal_langs(sh, el, 0.36, 0.42, 9.0 * s, 9.0 * s, "blauw", rond=0.6 * s, ovaal=(1.0, 0.92))
        B.buis(el, ha, 7.4 * s, 7.0 * s, "donker")
        B.schaal_langs(el, ha, 0.44, 0.96, 9.6 * s, 11.2 * s, "oranje", rond=2.6 * s, ovaal=(0.92, 1.0))
        B.schaal_langs(el, ha, 0.54, 0.61, 10.4 * s, 10.6 * s, "blauw", rond=0.5 * s, ovaal=(0.92, 1.0))
        # vuist: afgeronde doos langs de onderarm, duim als kleine doos naar voren
        dr = _richting(ha, h2)
        mid = ha + (h2 - ha).normalized() * 7.5 * s
        B.doos(mid, P(14, 15, 15), "metaal", rond=5.0 * s, draai=dr)
        B.doos(mid + dr @ P(0, -7.0, -2.0), P(5.5, 5, 8), "metaal", rond=2.4 * s, draai=dr)
        B.doos(mid + dr @ P(0, 0, 3.5), P(15, 16, 3.0), "blauw", rond=1.2 * s, draai=dr)   # pols
        # ---- benen ----
        hp, kn, an = p[f"{k}-upper-leg"], p[f"{k}-knee"], p[f"{k}-ankle"]
        B.buis(hp, kn, 10.4 * s, 9.6 * s, "donker")
        B.schaal_langs(hp, kn, 0.28, 0.64, 13.0 * s, 11.6 * s, "wit", rond=2.6 * s, ovaal=(0.92, 1.0))
        B.schaal_langs(hp, kn, 0.56, 0.62, 12.2 * s, 12.0 * s, "blauw", rond=0.6 * s, ovaal=(0.92, 1.0))
        # kniestuk aan de voorkant (-y): de knie buigt naar achteren
        B.doos(kn + P(0, -8.8, -3.0), P(16, 6, 16), "oranje", rond=2.8 * s, draai=_richting(hp, an))
        B.buis(kn, an, 9.6 * s, 8.2 * s, "donker")
        # scheen: pantser dat overloopt in een stevige laars
        B.schaal_langs(kn, an, 0.40, 0.62, 11.6 * s, 12.2 * s, "wit", rond=2.6 * s, ovaal=(0.95, 1.0))
        B.schaal_langs(kn, an, 0.58, 1.04, 12.5 * s, 13.0 * s, "blauw", rond=2.6 * s, ovaal=(0.95, 1.0))
        B.schaal_langs(kn, an, 0.56, 0.62, 12.8 * s, 12.8 * s, "oranje", rond=0.6 * s, ovaal=(0.95, 1.0))
        B.doos(P(18 * sx, -5, 8.5), P(23, 38, 15), "blauw", rond=5.5 * s)          # voet
        B.doos(P(18 * sx, -5.5, 2.0), P(24.4, 39.5, 4.0), "donker", rond=1.6 * s)   # zool
        B.doos(P(18 * sx, -20, 8.5), P(20, 9, 9.5), "oranje", rond=3.8 * s)         # neus
    return B.bm, namen


def laad_robot(hoogte_mm=220.0, stijl=None, voxel_mm=0.5):
    """Bouwt de robot, maakt er met Make watertight van de add-on één gesloten mesh van, zet de kleuren terug en
    hangt de rig eraan. Geeft (rig, figuur, punten)."""
    stijl = dict(STIJL, **(stijl or {}))
    voxel_mm = float(os.environ.get("CJ_VOXEL", voxel_mm))
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
    f = hoogte_mm / 220.0
    p = punten(hoogte_mm)
    bm, namen = bouw_vormen(p, f)
    me = bpy.data.meshes.new("Figuur")
    bm.to_mesh(me)
    bm.free()
    for n in namen:
        m = FL.toy_mat(n, stijl[n])
        if n in METAAL:
            m["cj_metaal"] = 1
        if n in LICHT:
            m["cj_licht"] = 1
        me.materials.append(m)
    fig = bpy.data.objects.new("Figuur", me)
    bpy.context.scene.collection.objects.link(fig)
    FL.log(f"robot: {len(me.vertices)} punten voor de remesh, maat {tuple(round(d, 1) for d in fig.dimensions)}")
    bron_me = fig.data.copy()
    bron_mw = fig.matrix_world.copy()
    bpy.context.scene.click_joints.voxel_mm = voxel_mm
    FL.actief(fig)
    bpy.ops.click_joints.maak_gesloten()
    nieuw = bpy.context.view_layer.objects.active
    if nieuw is not fig:
        bpy.data.objects.remove(fig)
        fig = nieuw
    FL.kleur_terug(bron_me, bron_mw, fig)
    bpy.data.meshes.remove(bron_me)
    fig.name = fig.data.name = "Figuur"
    FL.log(f"robot na watertight: {len(fig.data.vertices)} punten, {FL.mesh_staat(fig)}")
    M = FL._mens_module(hoogte_mm)
    arm = M["maak_rig"](rig_punten(p, f))
    arm.data.display_type = "STICK"
    fig.modifiers.new("Armature", "ARMATURE").object = arm
    return arm, fig, p
