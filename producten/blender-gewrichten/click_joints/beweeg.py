"""Beweegproef (ontwerp v0.2, ronde k): hoe ver buigt het kogelgewricht, gemeten in de echte vorm.

Na een geslaagde kogelplaatsing draait deel B om het kogelmidden in 8 richtingen loodrecht op de as, tot het
eerste raakpunt met deel A. Aanpak uit de bouwproef (`proef/proef_beweeg.py`): een kleine uitsnede (alleen de
vlakken rond nek en klikrand, kogel en kom tellen niet), BVH-overlap, en het kleinste deel draaien.
Grof in stappen van 2,5 graden, dan bisectie tot 0,1 graad, zodat een kort raakmoment niet gemist wordt.
Naast overlap een binnen-of-buiten-toets: zakt een punt van de klikrand helemaal in deel A, dan telt dat ook.

Ook hier: de pose (deel B alleen in de weergave gedraaid, zie `uit_elkaar.zet`) en de botsende vlakken van
deel A in het rode passingmateriaal."""
import math
import time

import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

from . import kleur as kleuren
from . import uit_elkaar

GROF = 2.5         # graden
FIJN = 0.1         # graden, nauwkeurigheid van de bisectie
MAX_HOEK = 60.0    # graden; een klikkogel komt nooit zo ver (standen 30, 25, 20)
BEREIK = 1.6       # keer (kogelstraal + speling): uitsnede rond nek en klikrand
MARGE_IN = 0.05    # keer de kogelstraal boven r + s: wat daarbinnen ligt is kogel of kom


def mesh_np(ob):
    """Punten in wereldmaat (echte plek, zonder Exploded view en pose), loop_start, loop_total, hoekpunten."""
    me = ob.data
    co = np.empty(len(me.vertices) * 3, dtype=np.float32)
    me.vertices.foreach_get("co", co)
    m = np.array(uit_elkaar.echte_matrix(ob))
    ls = np.empty(len(me.polygons), dtype=np.int32)
    lt = np.empty(len(me.polygons), dtype=np.int32)
    me.polygons.foreach_get("loop_start", ls)
    me.polygons.foreach_get("loop_total", lt)
    lv = np.empty(len(me.loops), dtype=np.int32)
    me.loops.foreach_get("vertex_index", lv)
    co = co.reshape(-1, 3).astype(np.float64) @ m[:3, :3].T + m[:3, 3]
    return co, ls, lt, lv


def uitsnede(mesh, c, r_uit, r_in):
    """Vlakken met minstens één hoekpunt binnen r_uit van c, zonder vlakken die helemaal binnen r_in liggen
    (kogel en kom). Geeft (punten, vlakken met hernummerde punten, oorspronkelijke vlaknummers)."""
    co, ls, lt, lv = mesh
    d = np.linalg.norm(co - c, axis=1)
    order = np.argsort(ls)
    ls_o = ls[order]
    dl = d[lv]
    houd = np.zeros(len(ls), dtype=bool)
    houd[order] = (np.minimum.reduceat(dl, ls_o) <= r_uit) & (np.maximum.reduceat(dl, ls_o) > r_in)
    gekozen = np.nonzero(houd)[0]
    if not len(gekozen):
        return np.zeros((0, 3)), [], gekozen
    idx = np.concatenate([lv[ls[i]:ls[i] + lt[i]] for i in gekozen])
    punten = np.unique(idx)
    nieuw = np.searchsorted(punten, idx).tolist()
    vlakken, k = [], 0
    for n in lt[gekozen].tolist():
        vlakken.append(nieuw[k:k + n])
        k += n
    return co[punten], vlakken, gekozen


def straal_in(a):
    return a["cj_kogel_r"] + a["cj_speling_mm"] * _u(a) + MARGE_IN * a["cj_kogel_r"]


def _u(a):
    """Eenheden per mm voor dit deel: kogel_r staat in eenheden, cj_speling_mm in mm; de verhouding staat in
    cj_speling_eenheid (bij het meten gezet), anders 1 (scene in mm)."""
    return a.get("cj_eenheid_per_mm", 1.0)


class Meter:
    def __init__(self, a, b):
        self.c = np.array(a["cj_centrum"])
        self.as_ = Vector(a["cj_as"]).normalized()
        r_in = straal_in(a)
        r_uit = BEREIK * (a["cj_kogel_r"] + a["cj_speling_mm"] * _u(a))
        self.a = uitsnede(mesh_np(a), self.c, r_uit, r_in)
        self.b = uitsnede(mesh_np(b), self.c, r_uit, r_in)
        self.bvh_a = BVHTree.FromPolygons(self.a[0].tolist(), self.a[1]) if self.a[1] else None
        self.richtingen = uit_elkaar.richtingen(self.as_)
        self.toetsen = 0
        rk = a["cj_kogel_r"] + a["cj_speling_mm"] * _u(a)
        afst = np.linalg.norm(self.b[0] - self.c, axis=1) if len(self.b[0]) else np.zeros(0)
        self.rand = np.nonzero(afst < 1.15 * rk)[0]  # klikrand: alleen die punten voor de binnen-toets
        self.zoek = 0.5 * a["cj_kogel_r"]

    def draai(self, k, hoek):
        m = np.array(Matrix.Rotation(math.radians(hoek), 3, self.as_.cross(self.richtingen[k])))
        return (self.b[0] - self.c) @ m.T + self.c

    def raakt(self, k, hoek, paren=False):
        """Raakt deel B (gedraaid over hoek graden richting k) deel A? Met paren: de lijst botsende paren."""
        self.toetsen += 1
        if self.bvh_a is None or not self.b[1]:
            return [] if paren else False
        pb = self.draai(k, hoek)
        bvh_b = BVHTree.FromPolygons(pb.tolist(), self.b[1])
        over = self.bvh_a.overlap(bvh_b)
        if paren:
            return over
        return bool(over) or self.binnen(pb)

    def binnen(self, pb):
        """Binnen-of-buiten: een punt van B dat dicht bij A ligt, maar aan de binnenkant van het dichtste vlak."""
        for p in pb[self.rand]:
            hit = self.bvh_a.find_nearest(Vector(p), self.zoek)
            if hit[0] is not None and (Vector(p) - hit[0]).dot(hit[1]) < -1e-9:
                return True
        return False

    def grens(self, k):
        if self.raakt(k, 0.0):
            return 0.0
        hoek = GROF
        while hoek <= MAX_HOEK + 1e-9:
            if self.raakt(k, hoek):
                vrij, raak = hoek - GROF, hoek
                while raak - vrij > FIJN + 1e-9:
                    mid = (vrij + raak) / 2
                    if self.raakt(k, mid):
                        raak = mid
                    else:
                        vrij = mid
                return math.floor(vrij / FIJN + 1e-6) * FIJN
            hoek += GROF
        return MAX_HOEK


def paar(scene, b):
    """Deel A dat bij deel B hoort (zelfde bron en kogelmidden)."""
    for o in scene.objects:
        if o.get("cj_deel") == "A" and o.get("cj_bron") == b.get("cj_bron") and \
                list(o.get("cj_centrum", [])) == list(b.get("cj_centrum", [])):
            return o
    return None


def meet(a, b, u):
    """Meet het bereik in 8 richtingen en zet cj_buig_graden en cj_buig_duur_s op beide delen."""
    t0 = time.perf_counter()
    for d in (a, b):
        d["cj_eenheid_per_mm"] = u
    meter = Meter(a, b)
    grenzen = [round(meter.grens(k), 2) for k in range(len(meter.richtingen))]
    duur = round(time.perf_counter() - t0, 3)
    for d in (a, b):
        d["cj_buig_graden"] = grenzen
        d["cj_buig_duur_s"] = duur
        d["cj_buig_toetsen"] = meter.toetsen
        d["cj_buig_vlakken"] = [len(meter.a[1]), len(meter.b[1])]
    return grenzen


def kleur_botsing(scene, b):
    """Na een pose: botsende vlakken van deel A krijgen het rode materiaal (eigen vak); de vorige weer terug.
    Geeft het aantal rode vlakken."""
    a = paar(scene, b)
    if a is None:
        return 0
    me = a.data
    oud = list(a.get("cj_rood_vlakken", []))
    for i in range(0, len(oud), 2):  # paren (vlak, oud vak)
        if oud[i] < len(me.polygons):
            me.polygons[oud[i]].material_index = oud[i + 1]
    a["cj_rood_vlakken"] = []
    g = float(b.get("cj_pose_graden", 0.0))
    if g <= 0.0 or "cj_buig_graden" not in a:
        me.update()
        return 0
    meter = Meter(a, b)
    paren = meter.raakt(int(b.get("cj_pose_richting", 0)), g, paren=True)
    vlakken = sorted({int(meter.a[2][i]) for i, _ in paren})
    if vlakken:
        mat = kleuren.materiaal("rood")
        namen = [m.name if m else None for m in me.materials]
        if len(me.materials) == 0:
            me.materials.append(None)
            namen = [None]
        if mat.name in namen:
            vak = namen.index(mat.name)
        else:
            me.materials.append(mat)
            vak = len(me.materials) - 1
        lijst = []
        for v in vlakken:
            lijst += [v, me.polygons[v].material_index]
            me.polygons[v].material_index = vak
        a["cj_rood_vlakken"] = lijst
    me.update()
    return len(vlakken)


def zet_pose(scene):
    """Update van Pose en richting: alle kogeldelen B draaien mee in de weergave, botsingen worden rood."""
    inst = scene.click_joints
    for b in [o for o in scene.objects if o.get("cj_deel") == "B" and "cj_buig_graden" in o]:
        b["cj_pose_graden"] = float(inst.pose_graden)
        b["cj_pose_richting"] = int(inst.pose_richting)
        uit_elkaar.zet(b, inst.uit_elkaar)
        kleur_botsing(scene, b)


def bij_pose(inst, context):
    zet_pose(context.scene)
