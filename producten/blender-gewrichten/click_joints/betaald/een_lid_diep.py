"""Pro 1.1 (run 27): `een_lid.bereid` met een omhulsel dat de hele diepte haalt.

Het gratis deel is gekeurd en blijft gelijk aan de live zip (toets_zips.py), dus de verbetering staat hier: een kopie
van `een_lid.bereid` met één verschil (de bol rond het midden, zie `r_bij`). Pro zet `een_lid.bereid` bij het
registreren op deze functie (zoals snippers.py `gewricht.snij` omhult) en zet hem bij het afmelden terug.
Gevonden op de MakeHuman-mens: beide schouders "blocked" in rechte stand; daarna ±20, en de heupen van ±15 en ±8
naar ±25.
"""
import heapq

import bmesh
from mathutils import Vector
from mathutils.bvhtree import BVHTree

from .. import een_lid as _l


# Pro 1.1 (22 nov, keuring Daan elleboog gedraaid): ook met één lus een omhulsel H, zodat de snede binnen het lid
# blijft. Zonder H lopen wig en stopvlakken over het hele object. Bij een gedraaide elleboog in T-houding die naar
# voren buigt, sneed de wig zo de hele voorkant van romp en hoofd weg (Quaternius Yeti 150 mm: 18 tot 21% van de
# punten kwijt, y van -38 tot 10 mm, GEZIEN). rig.py zet dit alleen aan voor de gedraaide plekken.
ALTIJD_H = [False]


def bereid_diep(werk, frame, vlak_z, diepte, marge, solver, hulp):
    """Zet een_lid.STAND voor de volgende snede. (True, None): snijden mag (met of zonder H). (False, melding): niet."""
    _l.reset()
    _l.LAATSTE.clear()
    bm = bmesh.new()
    bm.from_mesh(werk.data)
    bm.transform(frame.inverted())
    grootte = max(werk.dimensions) or 1.0
    uit = bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], dist=1e-7 * grootte,
                                 plane_co=(0, 0, vlak_z), plane_no=(0, 0, 1))
    bm.verts.index_update()
    bm.faces.index_update()
    tol = 1e-6 * grootte
    vlak = [e for e in bm.edges if all(abs(v.co.z - vlak_z) <= tol for v in e.verts)]
    lussen = _l._groepen(vlak)
    _l.LAATSTE["lussen"] = len(lussen)
    if len(lussen) < 1 or (len(lussen) == 1 and not ALTIJD_H[0]):
        bm.free()
        return True, None
    rond = [l for l in lussen if _l._binnen(l)]
    if not rond:
        bm.free()
        return True, None
    lus0 = min(rond, key=_l._maat)
    eigen = set(lus0)
    ander = set(vlak) - eigen
    # Aan beide kanten tegelijk zoeken vanaf de lus; de kant die het eerst klaar is, is de kleinste.
    stukken, rij, raakt = {"A": set(), "B": set()}, {"A": [], "B": []}, {"A": False, "B": False}
    for e in lus0:
        for f in e.link_faces:
            k = _l._kant(f, vlak_z)
            if f.index not in stukken[k]:
                stukken[k].add(f.index)
                rij[k].append(f)

    def stap(k):
        f = rij[k].pop()
        for e in f.edges:
            if e in ander:
                raakt[k] = True
            for g in e.link_faces:
                if g.index not in stukken[k] and _l._kant(g, vlak_z) == k:
                    stukken[k].add(g.index)
                    rij[k].append(g)
    while rij["A"] and rij["B"]:
        stap("A")
        stap("B")
    klaar = "A" if not rij["A"] else "B"
    lid = None
    if not raakt[klaar]:
        lid = klaar
    else:
        anders = "B" if klaar == "A" else "A"
        while rij[anders]:
            stap(anders)
        if not raakt[anders]:
            lid = anders
    _l.LAATSTE["lid"] = lid
    if lid is None:
        bm.free()
        return False, _l.MELD_VAST
    andere_kant = "B" if lid == "A" else "A"
    # Aan de andere kant: het stuk vanaf de lus tot 2,5 x diepte langs het oppervlak (mag in H), en daarvan wat
    # binnen 1,2 x diepte langs het oppervlak en binnen `diepte` van het vlak ligt (punten van H). Langs het oppervlak, zodat het niet via het kruis
    # naar het andere been loopt.
    bm.faces.ensure_lookup_table()
    afstand = {}
    rij2 = []
    for e in lus0:
        for f in e.link_faces:
            if _l._kant(f, vlak_z) == andere_kant and f.index not in afstand:
                afstand[f.index] = 0.0
                heapq.heappush(rij2, (0.0, f.index))
    while rij2:
        d, i = heapq.heappop(rij2)
        if d > afstand.get(i, 1e30):
            continue
        f = bm.faces[i]
        c = f.calc_center_median()
        for e in f.edges:
            for g in e.link_faces:
                if g.index == i or _l._kant(g, vlak_z) != andere_kant:
                    continue
                nd = d + (g.calc_center_median() - c).length
                if nd <= 2.5 * diepte and nd < afstand.get(g.index, 1e30):
                    afstand[g.index] = nd
                    heapq.heappush(rij2, (nd, g.index))
    # Ronde 2: ook binnen een bol met straal `diepte` rond het midden van het gewricht (verder reikt geen vorm).
    # Zonder bol pakte het omhulsel bij een kort dik been (Meshy man_backpack, diepte 25 mm) het kruis tot ver
    # opzij, en daarmee het andere been.
    # En alleen wat in het vlak dichter bij deze lus ligt dan bij een andere lus (het andere been): anders liep het
    # stuk boven het vlak via het kruis tot op de binnenkant van het andere dijbeen.
    midden = Vector((0.0, 0.0, vlak_z))

    def mid(lus):
        ps = [v.co.xy for e in lus for v in e.verts]
        return sum(ps, Vector((0.0, 0.0))) / len(ps)
    m0 = mid(lus0)
    anderen = [mid(l) for l in lussen if l is not lus0]

    def eigen_kant(co):
        d0 = (co.xy - m0).length
        return all(d0 <= (co.xy - c).length for c in anderen)

    # Run 27 (Pro): de bol om het midden had straal `diepte`. Dan reikt het omhulsel op de huid van het lid (straal
    # rl) maar tot sqrt(diepte^2 - rl^2) diep, bij een platte doorsnede nog minder: op de bovenarm van de
    # MakeHuman-mens tot 5,5 mm, terwijl de bolnaad 6,5 mm diep gaat. Het stuk bolnaad daaronder bleef in deel A,
    # en de schouderkogel zat in rechte stand al vast ("blocked"). Nu reikt het omhulsel op de huid de hele diepte.
    r_bij = (diepte ** 2 + max(v.co.xy.length for e in lus0 for v in e.verts) ** 2) ** 0.5

    def bij(v):
        return (v.co - midden).length <= r_bij and eigen_kant(v.co)
    dicht, punten = set(afstand), set()
    for i in dicht:
        f = bm.faces[i]
        if afstand[i] <= 1.2 * diepte and max(abs(v.co.z - vlak_z) for v in f.verts) <= diepte:
            punten.update(v.index for v in f.verts if bij(v))
    bm.verts.ensure_lookup_table()
    # 0.1.1 ronde 2 (Meshy man_backpack): niet het omhulsel van het hele lid, want een schuin onderbeen met voet
    # gaf een omhulsel dat het andere been raakte. H = (omhulsel van alleen het stuk rond het vlak, tot `diepte`
    # aan beide kanten) samen met (het lid zelf, dichtgemaakt). Beide een fractie groter.
    for i in stukken[lid]:
        f = bm.faces[i]
        if max(abs(v.co.z - vlak_z) for v in f.verts) <= diepte:
            punten.update(v.index for v in f.verts if bij(v))
    punten.update(v.index for e in lus0 for v in e.verts)
    # Convex omhulsel, daarna elke hoek `m` naar buiten.
    rl = max(v.co.xy.length for e in lus0 for v in e.verts)
    m = max(marge, 0.04 * rl)
    hb = bmesh.new()
    nieuw = [hb.verts.new(bm.verts[i].co) for i in punten]
    h_uit = bmesh.ops.convex_hull(hb, input=nieuw)
    weg = [v for v in h_uit["geom_interior"] + h_uit["geom_unused"] if isinstance(v, bmesh.types.BMVert)]
    bmesh.ops.delete(hb, geom=list(set(weg)), context="VERTS")
    bmesh.ops.recalc_face_normals(hb, faces=hb.faces[:])
    hb.normal_update()
    for v in hb.verts:
        v.co += v.normal * m
    hb.normal_update()
    # Het lid zelf: zijn vlakken, het gat bij het snijvlak dicht, `m` naar buiten.
    lb = bmesh.new()
    kaart = {}
    for i in stukken[lid]:
        f = bm.faces[i]
        vs = []
        for v in f.verts:
            if v.index not in kaart:
                kaart[v.index] = lb.verts.new(v.co)
            vs.append(kaart[v.index])
        try:
            lb.faces.new(vs)
        except ValueError:
            pass
    bmesh.ops.holes_fill(lb, edges=lb.edges[:], sides=0)
    bmesh.ops.recalc_face_normals(lb, faces=lb.faces[:])
    lb.normal_update()
    _l.PROEF[:] = [v.co.copy() for v in lb.verts]  # 0.1.3 (#306): _samen kijkt of H het lid zelf bevat
    for v in lb.verts:
        v.co += v.normal * m
    lid_open = sum(1 for e in lb.edges if len(e.link_faces) != 2)
    _l.LAATSTE["lid_open"] = lid_open
    # Raakt H een ander deel van het figuur?
    mag = stukken[lid] | dicht
    bvh_w = BVHTree.FromBMesh(bm)
    vreemde = sorted({j for b in (hb, lb) for _, j in BVHTree.FromBMesh(b).overlap(bvh_w) if j not in mag})
    vreemd = len(vreemde)
    if vreemde:
        _l.LAATSTE["vreemd_voorbeeld"] = [tuple(round(c, 1) for c in bm.faces[j].calc_center_median()) for j in vreemde[:4]]
    _l.LAATSTE["h_doos"] = [tuple(round(f(v.co[i] for v in hb.verts), 1) for i in range(3)) for f in (min, max)]
    _l.LAATSTE.update(diepte=round(diepte, 2), vreemd=vreemd, lid_vlakken=len(stukken[lid]), h_punten=len(hb.verts), marge=m)
    bm.free()
    if vreemd:
        hb.free()
        lb.free()
        return False, _l.MELD_DICHT
    h = _l._samen(hb, lb, frame, hulp, lid_open == 0)
    hb.free()
    lb.free()
    _l.STAND.update(h=h, kant=lid, solver=solver, bronnen={})
    return True, None


_oud = [None]


def origineel():
    """De gratis `een_lid.bereid` (zonder dieper omhulsel). Run 28: in Blender 4.2 (alleen de Exact-solver) liet het
    diepe omhulsel bij een scharnier het andere onderbeen kwijtraken (CI run 44066480759, toetsen_een_lid en plaatje 16);
    daar houdt het scharnier de oude vorm, zoals in de groene run 26."""
    return _oud[0] if _oud[0] is not None else _l.bereid


def register():
    if _oud[0] is None:
        _oud[0] = _l.bereid
        _l.bereid = bereid_diep


def unregister():
    if _oud[0] is not None:
        if _l.bereid is bereid_diep:
            _l.bereid = _oud[0]
        _oud[0] = None
