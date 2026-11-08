"""Beweegproef (ontwerp v0.2, ronde k): hoe ver buigt het kogelgewricht, gemeten in de echte vorm.

Na een geslaagde kogelplaatsing draait deel B om het kogelmidden in 8 richtingen loodrecht op de as, tot het
eerste raakpunt met deel A. Aanpak uit de bouwproef (`proef/proef_beweeg.py`): een kleine uitsnede (alleen de
vlakken rond nek en klikrand, kogel en kom tellen niet), BVH-overlap, en het kleinste deel draaien.
Grof in stappen van 2,5 graden, dan bisectie tot 0,1 graad. Eerlijk: een raakmoment dat korter is dan één grove
stap (botsen en weer los tussen twee stappen) kan gemist worden.
Naast overlap een binnen-of-buiten-toets: zakt een punt van de klikrand helemaal in deel A, dan telt dat ook.
De kleine uitsnede ziet alleen nek en klikrand, niet de rest van het figuur (controleur ronde k). Daarom per
richting op de gevonden grens één controle met een grote uitsnede (BEREIK_GROOT keer de kogelstraal, zonder
kogel en kom); botst het daar, dan opnieuw zoeken met de grote uitsnede.

Ook hier: de pose (deel B alleen in de weergave gedraaid, zie `uit_elkaar.zet`) en de botsende vlakken van
deel A in het rode passingmateriaal, gezocht in de grote uitsnede (ronde l).
Ronde n (sneller, zelfde uitkomst): de grote uitsnede laat vlakken weg die bij de geteste hoek bewijsbaar nooit
kunnen botsen (`snoei_maskers`, met bewijs), en `cj_buig_tijden` toont waar de tijd zit."""
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
BEREIK_GROOT = 6.0  # keer de kogelstraal (3 kogeldiameters): controle op de grens met de rest van het figuur
MARGE_IN = 0.05    # keer de kogelstraal boven r + s: wat daarbinnen ligt is kogel of kom
SNOEI = True       # ronde n: grote uitsnede snoeien op de geteste hoek (de toets zet hem uit om te vergelijken)


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


def uitsnede(mesh, c, r_uit, r_in, weg=None):
    """Vlakken met minstens één hoekpunt binnen r_uit van c, zonder vlakken die helemaal binnen r_in liggen
    (kogel en kom), en zonder de vlakken in `weg` (snoei, zie `snoei_maskers`).
    Geeft (punten, vlakken met hernummerde punten, oorspronkelijke vlaknummers)."""
    co, ls, lt, lv = mesh
    d = np.linalg.norm(co - c, axis=1)
    order = np.argsort(ls)
    ls_o = ls[order]
    dl = d[lv]
    houd = np.zeros(len(ls), dtype=bool)
    houd[order] = (np.minimum.reduceat(dl, ls_o) <= r_uit) & (np.maximum.reduceat(dl, ls_o) > r_in)
    if weg is not None:
        houd &= ~weg
    gekozen = np.nonzero(houd)[0]
    if not len(gekozen):
        return np.zeros((0, 3)), [], gekozen
    # Snel (ronde n): de hoekpunten van de gekozen vlakken in één keer, zonder lus per vlak.
    aantal = lt[gekozen]
    voor = np.concatenate(([0], np.cumsum(aantal)[:-1]))
    lussen = np.repeat(ls[gekozen] - voor, aantal) + np.arange(int(aantal.sum()))
    idx = lv[lussen]
    punten, nieuw = np.unique(idx, return_inverse=True)
    nieuw = nieuw.reshape(-1)
    if np.all(aantal == 3):
        vlakken = nieuw.reshape(-1, 3).tolist()
    else:
        vlakken = [v.tolist() for v in np.split(nieuw, np.cumsum(aantal)[:-1])]
    return co[punten], vlakken, gekozen


def vlak_maten(mesh, c, as_np, kant):
    """Per vlak (oorspronkelijke volgorde): kleinste en grootste hoogte h langs as * kant, grootste afstand w tot
    de as, een ondergrens en de grootste waarde van de afstand tot c. h is lineair en w en de afstand tot c zijn
    bol (convex), dus hun grootste waarde op een vlak ligt op een hoekpunt; alleen de kleinste afstand tot c
    kan binnen het vlak liggen: daarvoor (kleinste hoekpunt min de vlakgrootte) of h zelf."""
    co, ls, lt, lv = mesh
    order = np.argsort(ls)
    ls_o, lt_o = ls[order], lt[order]
    p = co[lv]
    h = ((p - c) @ as_np) * kant
    rho = np.linalg.norm(p - c, axis=1)
    w = np.sqrt(np.maximum(rho * rho - h * h, 0.0))
    def kl(x):
        return np.minimum.reduceat(x, ls_o)

    def gr(x):
        return np.maximum.reduceat(x, ls_o)
    midden = np.add.reduceat(p, ls_o, axis=0) / lt_o[:, None]
    grootte = 2.0 * gr(np.linalg.norm(p - np.repeat(midden, lt_o, axis=0), axis=1))
    uit = [np.empty(len(ls)) for _ in range(5)]
    h_min = kl(h)
    uit[0][order] = h_min
    uit[1][order] = gr(h)
    uit[2][order] = gr(w)
    uit[3][order] = np.maximum(kl(rho) - grootte, h_min)
    uit[4][order] = gr(rho)
    return uit


def snoei_maskers(ma, mb, c, as_np, kant_b, g_rad, marge, r_houd):
    """Welke vlakken van A en van B kunnen bij een draaiing tot g_rad om c nooit botsen? (masker A, masker B)

    Waarom het klopt. Gebied S_B: verder dan r_houd van c en hoger dan marge aan de kant van B; S_A hetzelfde aan
    de kant van A. Draai je om een lijn L door c in het snijvlak (loodrecht op de as) over hoogstens G, dan
    verandert de hoek van een punt tot dat vlak (om L gezien) hoogstens G. Die hoek is minstens atan(h / w), en de
    afstand tot L is minstens h, dus na de draaiing is de hoogte minstens h * sin(atan(h / w) - G). Is dat meer
    dan de marge voor elk punt van een vlak van B (kleinste h en grootste w van het vlak), en ligt het hele vlak
    verder dan r_houd (blijft zo, want draaien verandert de afstand tot c niet), dan blijft het vlak in S_B.
    Heeft A geen enkel punt in S_B, dan kan dat vlak nooit botsen. Voor A net zo (draai A terug).
    Of A punten in S_B heeft, wordt per vlak nagekeken (grootste h en grootste afstand: als beide erover gaan
    telt het vlak als indringer, voorzichtig); is er één, dan wordt aan die kant niets gesnoeid. Zo blijft het
    juist voor elke vorm, ook als iemand iets aan een deel vastmaakt (zoals het blok in de toets)."""
    ha_min, ha_max, wa, ra_min, ra_max = vlak_maten(ma, c, as_np, -kant_b)
    hb_min, hb_max, wb, rb_min, rb_max = vlak_maten(mb, c, as_np, kant_b)

    def weg(h_min, w_max, r_min):
        hoek = np.arctan2(h_min, w_max) - g_rad
        return (r_min > r_houd) & (h_min > 0) & (hoek > 0) & (h_min * np.sin(np.clip(hoek, 0.0, None)) > marge)

    # Indringers: punten van A aan de kant van B (hoogte -h_A > marge) buiten r_houd, en omgekeerd.
    a_in_b = np.any((-ha_min > marge) & (ra_max > r_houd))
    b_in_a = np.any((-hb_min > marge) & (rb_max > r_houd))
    leeg_a, leeg_b = np.zeros(len(ha_min), dtype=bool), np.zeros(len(hb_min), dtype=bool)
    weg_b = leeg_b if a_in_b else weg(hb_min, wb, rb_min)
    weg_a = leeg_a if b_in_a else weg(ha_min, wa, ra_min)
    return weg_a, weg_b


def straal_in(a):
    return a["cj_kogel_r"] + a["cj_speling_mm"] * _u(a) + MARGE_IN * a["cj_kogel_r"]


def _u(a):
    """Eenheden per mm voor dit deel: kogel_r staat in eenheden, cj_speling_mm in mm; de verhouding staat in
    cj_speling_eenheid (bij het meten gezet), anders 1 (scene in mm)."""
    return a.get("cj_eenheid_per_mm", 1.0)


class Meter:
    def __init__(self, a, b, groot=False, meshes=None, hoek=None):
        """Met hoek (graden): deze meter toetst nooit verder dan die hoek, dus vlakken die daar nooit kunnen
        botsen vallen weg (`snoei_maskers`). Alleen voor de grote uitsnede; zonder hoek alles zoals eerst."""
        self.c = np.array(a["cj_centrum"])
        self.as_ = Vector(a["cj_as"]).normalized()
        self.hoek = hoek
        r_in = straal_in(a)
        r_uit = BEREIK_GROOT * a["cj_kogel_r"] if groot else BEREIK * (a["cj_kogel_r"] + a["cj_speling_mm"] * _u(a))
        ma, mb = meshes if meshes else (mesh_np(a), mesh_np(b))
        wa, wb = self.snoei(a, ma, mb) if (SNOEI and groot and hoek is not None) else (None, None)
        self.gesnoeid = wa is not None
        self._vol = None
        self._maak_vol = lambda: Meter(a, b, groot=groot, meshes=(ma, mb))  # zonder snoei, voor verder dan hoek
        self.a = uitsnede(ma, self.c, r_uit, r_in, wa)
        self.b = uitsnede(mb, self.c, r_uit, r_in, wb)
        self.bvh_a = BVHTree.FromPolygons(self.a[0].tolist(), self.a[1]) if self.a[1] else None
        self.richtingen = uit_elkaar.richtingen(self.as_)
        self.toetsen = 0
        rk = a["cj_kogel_r"] + a["cj_speling_mm"] * _u(a)
        afst = np.linalg.norm(self.b[0] - self.c, axis=1) if len(self.b[0]) else np.zeros(0)
        self.rand = np.nonzero(afst < 1.15 * rk)[0]  # klikrand: alleen die punten voor de binnen-toets
        self.zoek = 0.5 * a["cj_kogel_r"]

    def snoei(self, a, ma, mb):
        """Snoeimaskers voor A en B, of (None, None) als het niet kan (geen bolnaad bekend)."""
        naad = a.get("cj_naad_r", -1.0)
        if naad is None or naad <= 0:
            return None, None
        r, s = a["cj_kogel_r"], a["cj_speling_mm"] * _u(a)
        # Binnen deze bol niets snoeien: bolnaad plus speling, en alles wat de binnen-toets ziet (klikrand plus
        # zoekafstand), met wat ruimte.
        r_houd = max(naad + s, 1.15 * (r + s) + 0.5 * r) + 0.1 * r
        as_np = np.array(self.as_)
        co_b = mb[0]
        buiten = np.linalg.norm(co_b - self.c, axis=1) > r_houd
        if not np.any(buiten):
            return None, None
        kant_b = 1.0 if float(np.mean((co_b[buiten] - self.c) @ as_np)) > 0 else -1.0
        g = math.radians(max(0.0, self.hoek) + 0.5)
        # Marge: ruim boven de verschuiving van het snijvlak naast het kogelmidden (0,0137 mm).
        marge = 0.05 * r
        return snoei_maskers(ma, mb, self.c, as_np, kant_b, g, marge, r_houd)

    def draai(self, k, hoek):
        m = np.array(Matrix.Rotation(math.radians(hoek), 3, self.as_.cross(self.richtingen[k])))
        return (self.b[0] - self.c) @ m.T + self.c

    def raakt(self, k, hoek, paren=False):
        """Raakt deel B (gedraaid over hoek graden richting k) deel A? Met paren: de lijst botsende paren.
        Let op: voorbij de snoeihoek komen de paren uit de volle meter (`self._vol.a`), niet uit `self.a`;
        vraag paren dus alleen op tot de snoeihoek (zoals kleur_botsing doet)."""
        self.toetsen += 1
        if self.gesnoeid and hoek > self.hoek + 1e-9:
            # Verder dan de snoeihoek (controleur ronde n): dan geldt het snoeien niet, dus de volle uitsnede.
            if self._vol is None:
                self._vol = self._maak_vol()
            return self._vol.raakt(k, hoek, paren)
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
    """Meet het bereik in 8 richtingen en zet cj_buig_graden en cj_buig_duur_s op beide delen.

    Ronde n (sneller, zelfde meting): eerst alle grenzen met de kleine uitsnede; de grote uitsnede snoeit daarna
    wat tot de grootste daarvan plus één grove stap nooit kan botsen (`snoei_maskers`), met de volle uitsnede als
    terugval voorbij die hoek. Zelfde zoektocht als zonder snoei, dus dezelfde grenzen."""
    t0 = time.perf_counter()
    for d in (a, b):
        d["cj_eenheid_per_mm"] = u
    meshes = (mesh_np(a), mesh_np(b))
    t1 = time.perf_counter()
    meter = Meter(a, b, meshes=meshes)
    klein = [meter.grens(k) for k in range(len(meter.richtingen))]
    t2 = time.perf_counter()
    # De grote meter zoekt zo nodig tot de volgende grove stap (zelfde zoektocht als altijd): snoeien tot daar;
    # komt hij toch verder, dan neemt hij vanzelf de volle uitsnede (Meter.raakt).
    groot = Meter(a, b, groot=True, meshes=meshes, hoek=min(MAX_HOEK, max(klein) + GROF))
    t3 = time.perf_counter()
    grenzen, opnieuw = [], 0
    for k, g in enumerate(klein):
        if groot.raakt(k, g):  # de rest van het figuur botst eerder: opnieuw zoeken met de grote uitsnede
            g = groot.grens(k)
            opnieuw += 1
        grenzen.append(round(g, 2))
    t4 = time.perf_counter()
    duur = round(t4 - t0, 3)
    for d in (a, b):
        d["cj_buig_graden"] = grenzen
        d["cj_buig_duur_s"] = duur
        d["cj_buig_toetsen"] = meter.toetsen + groot.toetsen
        d["cj_buig_vlakken"] = [len(meter.a[1]), len(meter.b[1]), len(groot.a[1]), len(groot.b[1])]
        d["cj_buig_opnieuw"] = opnieuw
        # Waar de tijd zit: punten lezen, kleine uitsnede met zoeken, grote uitsnede bouwen, grote toetsen.
        d["cj_buig_tijden"] = [round(t1 - t0, 3), round(t2 - t1, 3), round(t3 - t2, 3), round(t4 - t3, 3)]
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
    k = int(b.get("cj_pose_richting", 0))
    grenzen = list(a.get("cj_buig_graden", []))
    # Binnen de gemeten grens kan niets botsen (zo is de grens gemeten): niet meten, de schuif blijft vlot.
    if g <= 0.0 or k >= len(grenzen) or g <= grenzen[k]:
        me.update()
        return 0
    # Grote uitsnede (controleur ronde k): ook een botsing met de rest van het figuur (schouder, kraag) wordt rood,
    # niet alleen nek en klikrand. De grote uitsnede bevat de kleine (6r > 1,6 (r + s)).
    meter = Meter(a, b, groot=True, hoek=g)
    paren = meter.raakt(k, g, paren=True)
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
