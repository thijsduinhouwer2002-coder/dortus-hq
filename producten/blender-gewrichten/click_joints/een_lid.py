"""Eén lid snijden, niet het hele figuur (0.1.1, proef met Meshy-figuren 15 nov).

Probleem: de snijvormen (dozen, wig, naadcilinders) lopen over het hele object. Een gewricht in één knie van
een figuur uit één stuk sneed zo ook het andere been door.

Oplossing, alleen als het snijvlak het figuur op meer dan één plek raakt (anders blijft alles zoals het was):
1. Snijvlak door een kopie van het figuur (bisect, in het frame van de snede, vlak z = vlak_z).
2. De lus van het vlak rond de cursor kiezen. Aan elke kant het stuk dat aan die lus vastzit zoeken; het
   stuk dat alleen aan deze lus vastzit is het lid (het onderbeen). Hangt het aan beide kanten aan een andere
   lus vast (twee voeten op één voetstuk), dan niet snijden: melding VAST.
3. H = convex omhulsel van het stuk rond het vlak (tot `diepte` aan beide kanten, aan de andere kant langs het
   oppervlak gemeten; daar zitten kom, naad en wig) samen met het lid zelf (dichtgemaakt), een fractie groter.
   Niet het omhulsel van het hele lid: een schuin onderbeen met voet raakte dan het andere been (ronde 2).
   Raakt H een ander deel van het figuur: melding DICHT.
4. Tijdens de snede (gewricht.bak en gewricht.boolean vragen STAND): de kopie van het figuur aan de kant van
   het lid krijgt eerst INTERSECT H; elk gereedschap dat van de andere kant iets afhaalt krijgt INTERSECT H.
   Buiten H snijdt dus niets: het andere been blijft heel in het deel aan de andere kant.
"""
import heapq

import bmesh
import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

MELD_VAST = ("This limb is joined to another part of the mesh on both sides of the cut (for example both feet on "
             "one base), so one joint would cut both. Pick a spot where the limb is free, or split the model first.")
MELD_DICHT = ("Another part of the mesh is too close to this limb (for example the other leg), so the joint would "
              "cut it too. Pick another spot, or move the parts a little apart first.")

STAND = {"h": None, "kant": None, "solver": None, "bronnen": {}}
LAATSTE = {}  # voor de toetsen: wat bereid de laatste keer besloot
PROEF = []  # 0.1.3 (#306): punten van het lid zelf (zonder marge), in het frame; _samen kijkt of H ze bevat


def reset():
    STAND.update(h=None, kant=None, solver=None, bronnen={})
    PROEF.clear()


def _kant(f, z):
    return "A" if f.calc_center_median().z < z else "B"


def _groepen(randen):
    """Lussen: groepen randen die via punten aan elkaar zitten."""
    ouder = {}

    def zoek(a):
        while ouder.setdefault(a, a) != a:
            ouder[a] = ouder[ouder[a]]
            a = ouder[a]
        return a
    for e in randen:
        a, b = zoek(e.verts[0].index), zoek(e.verts[1].index)
        if a != b:
            ouder[a] = b
    uit = {}
    for e in randen:
        uit.setdefault(zoek(e.verts[0].index), []).append(e)
    return list(uit.values())


def _binnen(lus):
    """Ligt de cursor (0, 0 in het frame) binnen de lus? Straal langs +x, even-oneven."""
    tel = 0
    for e in lus:
        (x1, y1), (x2, y2) = e.verts[0].co.xy, e.verts[1].co.xy
        if (y1 > 0) != (y2 > 0) and x1 + (0 - y1) * (x2 - x1) / (y2 - y1) > 0:
            tel += 1
    return tel % 2 == 1


def _maat(lus):
    xs = [v.co.x for e in lus for v in e.verts]
    ys = [v.co.y for e in lus for v in e.verts]
    return (max(xs) - min(xs)) * (max(ys) - min(ys))


def bereid(werk, frame, vlak_z, diepte, marge, solver, hulp):
    """Zet STAND voor de volgende snede. (True, None): snijden mag (met of zonder H). (False, melding): niet."""
    reset()
    LAATSTE.clear()
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
    lussen = _groepen(vlak)
    LAATSTE["lussen"] = len(lussen)
    if len(lussen) <= 1:
        bm.free()
        return True, None
    rond = [l for l in lussen if _binnen(l)]
    if not rond:
        bm.free()
        return True, None
    lus0 = min(rond, key=_maat)
    eigen = set(lus0)
    ander = set(vlak) - eigen
    # Aan beide kanten tegelijk zoeken vanaf de lus; de kant die het eerst klaar is, is de kleinste.
    stukken, rij, raakt = {"A": set(), "B": set()}, {"A": [], "B": []}, {"A": False, "B": False}
    for e in lus0:
        for f in e.link_faces:
            k = _kant(f, vlak_z)
            if f.index not in stukken[k]:
                stukken[k].add(f.index)
                rij[k].append(f)

    def stap(k):
        f = rij[k].pop()
        for e in f.edges:
            if e in ander:
                raakt[k] = True
            for g in e.link_faces:
                if g.index not in stukken[k] and _kant(g, vlak_z) == k:
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
    LAATSTE["lid"] = lid
    if lid is None:
        bm.free()
        return False, MELD_VAST
    andere_kant = "B" if lid == "A" else "A"
    # Aan de andere kant: het stuk vanaf de lus tot 2,5 x diepte langs het oppervlak (mag in H), en daarvan wat
    # binnen 1,2 x diepte langs het oppervlak en binnen `diepte` van het vlak ligt (punten van H). Langs het oppervlak, zodat het niet via het kruis
    # naar het andere been loopt.
    bm.faces.ensure_lookup_table()
    afstand = {}
    rij2 = []
    for e in lus0:
        for f in e.link_faces:
            if _kant(f, vlak_z) == andere_kant and f.index not in afstand:
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
                if g.index == i or _kant(g, vlak_z) != andere_kant:
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

    def bij(v):
        return (v.co - midden).length <= diepte and eigen_kant(v.co)
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
    PROEF[:] = [v.co.copy() for v in lb.verts]
    for v in lb.verts:
        v.co += v.normal * m
    lid_open = sum(1 for e in lb.edges if len(e.link_faces) != 2)
    LAATSTE["lid_open"] = lid_open
    # Raakt H een ander deel van het figuur?
    mag = stukken[lid] | dicht
    bvh_w = BVHTree.FromBMesh(bm)
    vreemde = sorted({j for b in (hb, lb) for _, j in BVHTree.FromBMesh(b).overlap(bvh_w) if j not in mag})
    vreemd = len(vreemde)
    if vreemde:
        LAATSTE["vreemd_voorbeeld"] = [tuple(round(c, 1) for c in bm.faces[j].calc_center_median()) for j in vreemde[:4]]
    LAATSTE["h_doos"] = [tuple(round(f(v.co[i] for v in hb.verts), 1) for i in range(3)) for f in (min, max)]
    LAATSTE.update(diepte=round(diepte, 2), vreemd=vreemd, lid_vlakken=len(stukken[lid]), h_punten=len(hb.verts), marge=m)
    bm.free()
    if vreemd:
        hb.free()
        lb.free()
        return False, MELD_DICHT
    h = _samen(hb, lb, frame, hulp, lid_open == 0)
    hb.free()
    lb.free()
    STAND.update(h=h, kant=lid, solver=solver, bronnen={})
    return True, None


def _samen(hb, lb, frame, hulp, lid_dicht):
    """H als één gesloten vorm: omhulsel rond het vlak plus het lid (Exact, UNION). Lukt dat niet of is het lid niet
    dicht, dan beide vormen los in één mesh (de booleans rekenen dan met Self Intersection)."""
    hb.transform(frame)
    lb.transform(frame)
    me = bpy.data.meshes.new("cj_een_lid")
    hb.to_mesh(me)
    h = bpy.data.objects.new("cj_een_lid", me)
    hulp.objects.link(h)
    h.hide_set(True)
    me_l = bpy.data.meshes.new("cj_een_lid_l")
    if lid_dicht:
        lb.to_mesh(me_l)
        lo = bpy.data.objects.new("cj_een_lid_l", me_l)
        hulp.objects.link(lo)
        # 0.1.2 (Chris, army_man 16 nov): Exact UNION gaf soms alleen het omhulsel terug en liet het lid weg (gesloten,
        # dus "goed"). Dan bleef alles van het lid buiten het omhulsel (de zool van de schoen) in deel B liggen. Nu
        # telt de uitkomst alleen als hij het lid echt bevat: volume en kader minstens die van omhulsel en lid. Anders
        # nog eens met Self Intersection, en lukt ook dat niet, de terugval "los".
        doel_vol = max(_volume(hb), _volume(lb))
        doel_kader = _kader(lb)
        for zelf in (False, True):
            m = h.modifiers.new("samen", "BOOLEAN")
            m.operation, m.object, m.solver = "UNION", lo, "EXACT"
            m.use_self = zelf
            dg = bpy.context.evaluated_depsgraph_get()
            ev = h.evaluated_get(dg)
            nm = bpy.data.meshes.new_from_object(ev)
            h.modifiers.remove(m)
            bm2 = bmesh.new()
            bm2.from_mesh(nm)
            goed = len(bm2.faces) > 0 and all(len(e.link_faces) == 2 for e in bm2.edges)
            vol = _volume(bm2) if goed else 0.0
            kader = _kader(bm2) if goed else None
            bm2.free()
            tol = 0.02 * max(b - a for a, b in zip(*doel_kader))
            bevat = goed and vol >= 0.98 * doel_vol and all(
                kader[0][i] <= doel_kader[0][i] + tol and kader[1][i] >= doel_kader[1][i] - tol for i in range(3))
            # 0.1.3 (#306): volume en kader zien niet dat kleine stukken van het lid ontbreken. Op Human Base Meshes
            # (tenen dicht op elkaar: de verschoven huid snijdt zichzelf tussen de tenen) liet de vereniging delen
            # van de tenen weg; die stukjes bleven dan in deel A. Nu moet elk punt van het lid zelf in H liggen.
            buiten = _lid_buiten(nm, frame) if goed else -1
            bevat = bevat and buiten == 0
            LAATSTE.setdefault("h_pogingen", []).append((zelf, round(vol, 1), round(doel_vol, 1), buiten, bevat))
            if bevat:
                oud = h.data
                h.data = nm
                bpy.data.meshes.remove(oud)
                LAATSTE["h_soort"] = "samen_zelf" if zelf else "samen"
                break
            bpy.data.meshes.remove(nm)
        bpy.data.objects.remove(lo)
    if lid_dicht and not str(LAATSTE.get("h_soort", "")).startswith("samen"):
        # 0.1.3 (#306): lukt de vereniging niet (of mist ze een stuk van het lid), dan beide vormen door een
        # voxel-remesh: dat maakt van overlappende of zichzelf snijdende schillen één gesloten huid. Alleen als die
        # het hele lid bevat; anders de oude terugval hieronder.
        nieuw = _voxel(hb, lb, hulp, frame)
        if nieuw is not None:
            oud = h.data
            h.data = nieuw
            bpy.data.meshes.remove(oud)
            LAATSTE["h_soort"] = "voxel"
    if not str(LAATSTE.get("h_soort", "")).startswith(("samen", "voxel")):
        # terugval: beide vormen los in één mesh; de booleans rekenen dan met Self Intersection
        alle = bmesh.new()
        alle.from_mesh(h.data)
        kaart = {v: alle.verts.new(v.co) for v in lb.verts}
        for f in lb.faces:
            try:
                alle.faces.new([kaart[v] for v in f.verts])
            except ValueError:
                pass
        alle.to_mesh(h.data)
        alle.free()
        LAATSTE["h_soort"] = "los"
    if me_l.users == 0:
        bpy.data.meshes.remove(me_l)
    return h


def _snijd_met_h(ob):
    if any(m.type == "BOOLEAN" and m.object is STAND["h"] for m in ob.modifiers):
        return
    m = ob.modifiers.new("cj_een_lid", "BOOLEAN")
    m.operation = "INTERSECT"
    m.object = STAND["h"]
    m.solver = STAND["solver"]
    if m.solver == "EXACT":
        m.use_self = LAATSTE.get("h_soort") == "los"
        m.use_hole_tolerant = False


def na_bak(naam, uit):
    """Vanuit gewricht.bak: de kopie van het figuur voor deel A of B."""
    if STAND["h"] is None or naam not in ("cj_a_bron", "cj_b_bron"):
        return
    kant = "A" if naam == "cj_a_bron" else "B"
    STAND["bronnen"][uit.name] = kant
    if kant == STAND["kant"]:
        _snijd_met_h(uit)


def voor_boolean(doel, gereedschap, actie):
    """Vanuit gewricht.boolean: wat de andere kant afhaalt, alleen binnen H."""
    if STAND["h"] is None or actie != "DIFFERENCE":
        return
    kant = STAND["bronnen"].get(doel.name)
    if kant is not None and kant != STAND["kant"]:
        _snijd_met_h(gereedschap)


def _voxel(hb, lb, hulp, frame):
    """Omhulsel en lid (al in wereldmaat) samen door een voxel-remesh. Mesh of None (niet gesloten of lid niet binnen)."""
    import math
    from .gesloten import is_gesloten
    from .gewricht import solver_naam
    m = float(LAATSTE.get("marge") or 0.0)
    if m <= 0:
        return None
    opp = sum(f.calc_area() for f in hb.faces) + sum(f.calc_area() for f in lb.faces)
    # Exact rekent met exacte getallen: daar een grovere vorm, anders loopt het geheugen op (issue 14: bij 214.150 vlakken meer dan 15 GB).
    v = math.sqrt(opp / (30000 if solver_naam() == "EXACT" else 250000))
    v = max(v, 0.5 * m) if solver_naam() != "EXACT" else v
    alle = hb.copy()
    kaart = {x: alle.verts.new(x.co) for x in lb.verts}
    for f in lb.faces:
        try:
            alle.faces.new([kaart[x] for x in f.verts])
        except ValueError:
            pass
    me = bpy.data.meshes.new("cj_een_lid_bron")
    alle.to_mesh(me)
    alle.free()
    tmp = bpy.data.objects.new("cj_een_lid_bron", me)
    hulp.objects.link(tmp)
    mod = tmp.modifiers.new("cj_voxel", "REMESH")
    mod.mode, mod.voxel_size, mod.adaptivity = "VOXEL", v, 0.0
    dg = bpy.context.evaluated_depsgraph_get()
    nm = bpy.data.meshes.new_from_object(tmp.evaluated_get(dg))
    bpy.data.objects.remove(tmp)
    bpy.data.meshes.remove(me)
    ok = is_gesloten(nm)[0]
    buiten = _lid_buiten(nm, frame) if ok else -1
    LAATSTE.update(h_voxel=round(v, 4), h_vlakken=len(nm.polygons), h_voxel_buiten=buiten)
    if not ok or buiten != 0:
        bpy.data.meshes.remove(nm)
        return None
    return nm


def _lid_buiten(me, frame):
    """Hoeveel punten van het lid zelf (PROEF, zonder marge) buiten de gesloten mesh `me` liggen. Een punt telt pas
    als buiten als het meer dan een kwart van de marge buiten de huid ligt (afronding bij scherpe randen)."""
    if not PROEF:
        return 0
    b = bmesh.new()
    b.from_mesh(me)
    b.normal_update()
    bvh = BVHTree.FromBMesh(b)
    b.free()
    speling = 0.25 * float(LAATSTE.get("marge") or 0.0)
    buiten = 0
    for p in PROEF:
        q = p if frame is None else frame @ p
        plek, normaal, _i, _a = bvh.find_nearest(q)
        if plek is None or (q - plek).dot(normaal.normalized()) > speling:
            buiten += 1
    return buiten


def _volume(b):
    return abs(b.calc_volume(signed=True))


def _kader(b):
    """(min, max) van de punten in wereldmaat (na hb/lb.transform(frame) is dat bij beide hetzelfde)."""
    return ([min(v.co[i] for v in b.verts) for i in range(3)], [max(v.co[i] for v in b.verts) for i in range(3)])
