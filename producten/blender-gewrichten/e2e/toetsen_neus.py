"""Toets klikneus en zaagsnede van het scharnier (ontwerp betaald v1.1, eis 3 en vorm punt 5), aangeroepen
vanuit toetsen_scharnier.py.

Alles gemeten in de mesh, tegen een eigen rekensom; de as H komt uit de 3D-cursor (X-as van de cursor, door
de cursor min e = 0,15 keer de dikte langs de Y-as van de cursor), niet uit opgeslagen cj-waarden.
- Zijvlak van de tong: de rand van de knokkel van B (0,7 R tot R van H) op de grootste |x|.
- Neus: punten van B dichter dan 0,7 R bij H; hoogte = top min zijvlak van de tong; top tot H.
- Wang: binnenvlak van A (punten boven H, binnen de wangstraal) op de kleinste |x|.
- Klikdiepte = top van de neus min binnenvlak van de wang: 0,25 mm (besluit manager), bij speling 0,2 en 0,3.
- Rek 1,5 t k / L^2 met L van H tot de bodem van de zaagsnede (correctie controleur), hoogstens 3%.
- Staaf van 9 mm: de rek-eis geeft een lagere klikdiepte (eigen rekensom), het scharnier wordt wel geplaatst.
- Zaagsnede: een straal uit het midden van A langs H stuit vlak naast de tong op de sleuf, tot de zaagbodem.
- Breedte van de sleuf in de mesh (stralen uit het midden van de sleuf naar beide wanden): minstens s - 0,01,
  want smaller smelt bij het printen dicht; de wand aan de wangkant ligt op of net binnen tw + s (lip t dik).
- Korte staaf (onderkant van A dichter bij H dan L + rest): de sleuf wordt korter (L = diepte - max(t, 0,8)),
  deel A blijft één stuk en de sleuf eindigt boven de onderkant; nog korter geeft Tight en geen objecten.
- Dunne staaf van 5 mm: CANCELLED met de te-dun- of Tight-melding en geen nieuwe objecten."""
import math
import sys

import bpy
from mathutils import Matrix, Vector

import figuren
from hulp_scharnier import bvh as _bvh

TOL_MM = 0.01
KNOKKEL, WANG, ACHTER, ZAAG = 0.35, 0.20, 0.15, 0.65   # eigen rekensom (ontwerp v1.1, staaf rond)


def _plaats(straal, cursor, s=0.2, onder=None):
    """Staaf langs X met de cursor in de oorsprong; onder = afstand van de cursor tot het uiteinde aan de kant
    van deel A (-X), anders de gewone 20 mm."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = s
    inst.as_bron = "CURSOR"
    staaf = figuren.staaf("staaf", straal)
    if onder is not None:
        staaf.data.transform(Matrix.Translation((20.0 - onder, 0, 0)))
    figuren.maak_actief(staaf)
    cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    return staaf


def _as_uit_cursor(straal, u):
    """(punt op H, H, buigkant, lidas) uit de 3D-cursor: H = X-as, buigkant = Y-as, lidas = Z-as."""
    m = bpy.context.scene.cursor.matrix
    h, buig, lid = (m.col[i].xyz.normalized() for i in range(3))
    return m.to_translation() - buig * (ACHTER * 2 * straal * u), h, buig, lid


def meet_neus(a, b, straal, s, u):
    """Per kant (+H, -H): dict met tong, top, rho_top, wang (afstanden langs H in mm) en het toppunt."""
    p, h, buig, lid = _as_uit_cursor(straal, u)
    r = KNOKKEL * straal * u
    rn = r + s * u + WANG * straal * u
    uit = {}
    for teken, kant in ((1, "+H"), (-1, "-H")):
        tong, top, beste = None, None, -1.0
        for v in b.data.vertices:
            d = b.matrix_world @ v.co - p
            x = d.dot(h) * teken
            if x <= 0:
                continue
            rho = (d - h * d.dot(h)).length
            if 0.7 * r < rho < r + 1e-4 * u:
                tong = x if tong is None else max(tong, x)
            elif rho <= 0.7 * r and x > beste:
                beste, top = x, d
        wang = None
        for v in a.data.vertices:
            d = a.matrix_world @ v.co - p
            x = d.dot(h) * teken
            rho = (d - h * d.dot(h)).length
            if x > 0 and d.dot(lid) > s * u and rho < rn - s * u / 2 + 1e-3 * u:
                wang = x if wang is None else min(wang, x)
        if tong is None or top is None or wang is None:
            uit[kant] = None
            continue
        uit[kant] = {"tong": tong / u, "top": beste / u, "wang": wang / u, "punt": p + top,
                     "rho_top": (top - h * top.dot(h)).length / u}
    return uit


def _klik(stap, naam, a, b, straal, s, u, klik_verwacht, lip=None):
    """Meet en toetst neus, klikdiepte, speling en rek op één geplaatst scharnier; geeft de klikdiepte.
    lip: eigen L als de sleuf korter is (korte staaf), anders ZAAG keer de dikte."""
    bvh_a = _bvh(a)
    gemeten = meet_neus(a, b, straal, s, u)
    kliks = []
    for kant, m in gemeten.items():
        if m is None:
            stap(f"{naam} {kant}: tong, neus en wang gevonden in de mesh", False)
            continue
        hoogte, klik, gleuf = m["top"] - m["tong"], m["top"] - m["wang"], m["wang"] - m["tong"]
        hit = bvh_a.find_nearest(m["punt"])
        boven = hit[3] / u if hit[0] is not None else -1
        print(f"[cj-betaald] METING {naam} {kant}: neushoogte tegen zijvlak tong {hoogte:.4f} mm, klikdiepte "
              f"{klik:.4f} mm, gleuf {gleuf:.4f} mm, top tot H (cursor) {m['rho_top']:.4f} mm, "
              f"top neus tot A {boven:.4f} mm, tong op {m['tong']:.4f} mm")
        stap(f"{naam} {kant}: neushoogte = speling + klikdiepte ({s + klik_verwacht:.4f}) binnen {TOL_MM}",
             abs(hoogte - (s + klik_verwacht)) <= TOL_MM, f"{hoogte:.4f} mm")
        stap(f"{naam} {kant}: klikdiepte {klik_verwacht:.4f} mm binnen {TOL_MM} mm", abs(klik - klik_verwacht)
             <= TOL_MM, f"{klik:.4f} mm")
        stap(f"{naam} {kant}: gleuf tong-wang {s} mm binnen {TOL_MM}", abs(gleuf - s) <= TOL_MM, f"{gleuf:.4f}")
        stap(f"{naam} {kant}: top op H uit de cursor binnen {TOL_MM} mm", m["rho_top"] <= TOL_MM,
             f"{m['rho_top']:.4f} mm")
        stap(f"{naam} {kant}: kuiltje, speling boven de neus {s} mm binnen {TOL_MM}", abs(boven - s) <= TOL_MM,
             f"{boven:.4f} mm")
        kliks.append((klik, m["tong"]))
    if not kliks:
        return None
    klik, tw = min(kliks)
    t = straal - tw - s
    lip = ZAAG * 2 * straal if lip is None else lip
    eigen_rek = 1.5 * t * klik / (lip * lip)
    rek = float(b.get("cj_rek", -1))
    print(f"[cj-betaald] METING {naam} rek: add-on {rek * 100:.3f}% eigen {eigen_rek * 100:.3f}% t {t:.3f} mm "
          f"L (H tot zaagbodem) {lip:.3f} mm klikdiepte {klik:.4f} mm; add-on L {float(b.get('cj_lip', -1)) / u:.3f}")
    stap(f"{naam}: rek hoogstens 3% en gelijk aan de eigen rekensom met de gemeten klikdiepte",
         0 < rek <= 0.03 + 1e-6 and abs(rek - eigen_rek) < 1e-4, f"{rek * 100:.3f}% (eigen {eigen_rek * 100:.3f}%)")
    return klik


def _zaag(stap, a, straal, s, u, tw, lip=None, naam="zaagsnede"):
    """Vorm punt 5: de sleuf naast de tong is er, aan beide kanten, tot de zaagbodem L onder H, en is
    minstens s breed (correctie controleur eis 3)."""
    p, h, buig, lid = _as_uit_cursor(straal, u)
    bvh_a = _bvh(a)
    lip = ZAAG * 2 * straal if lip is None else lip
    for teken, kant in ((1, "+H"), (-1, "-H")):
        bodem = None
        # Van 2,5 mm onder H (buiten het knokkelgat) tot 1 mm onder de verwachte zaagbodem, stap 0,05 mm.
        for i in range(int((lip - 1.5) / 0.05) + 1):
            z = 2.5 + 0.05 * i
            o = p - buig * (1.0 * u) - lid * (z * u)
            hit = bvh_a.ray_cast(o, h * teken)
            # De sleuf begint sinds de correctie van de controleur net binnen tw (minstens s breed), dus de
            # binnenwand ligt tussen tw - s en tw + s (was tussen tw en tw + s).
            if hit[0] is not None and tw - s < hit[3] / u < tw + s:
                bodem = z
        print(f"[cj-betaald] METING {naam} {kant}: sleuf naast de tong tot {bodem} mm onder H "
              f"(eigen L {lip:.3f} mm)")
        stap(f"{naam} {kant}: sleuf naast de tong tot de zaagbodem L binnen 0.06 mm",
             bodem is not None and abs(bodem - lip) <= 0.06, f"bodem {bodem} eigen {lip:.3f}")
        _breedte(stap, bvh_a, p, h * teken, buig, lid, s, u, tw, lip, f"{naam} {kant}")


def _breedte(stap, bvh_a, p, h, buig, lid, s, u, tw, lip, naam):
    """Breedte van de sleuf in de mesh: uit het midden van de gleuf (tw + s/2, zeker in de sleuf) een straal
    naar de wang (+h) en een naar de tong (-h). Beide moeten een wand van A van de luchtkant raken (normaal
    tegen de straal in), anders zit het punt in het materiaal en is er geen sleuf."""
    smalst, buiten = None, None
    for i in range(int((lip - 2.6) / 0.25) + 1):
        z = 2.5 + 0.25 * i
        o = p - buig * (1.0 * u) - lid * (z * u) + h * ((tw + s / 2) * u)
        uit, terug = bvh_a.ray_cast(o, h), bvh_a.ray_cast(o, -h)
        if uit[0] is None or terug[0] is None or uit[1].dot(h) >= 0 or terug[1].dot(-h) >= 0:
            smalst = -1.0
            break
        b = (uit[3] + terug[3]) / u
        smalst = b if smalst is None else min(smalst, b)
        w = tw + s / 2 + uit[3] / u
        buiten = w if buiten is None else max(buiten, w)
    print(f"[cj-betaald] METING {naam}: sleufbreedte smalst {smalst} mm (s {s}), wand aan de wangkant op "
          f"{buiten} mm (tw + s = {tw + s:.4f})")
    stap(f"{naam}: sleuf overal minstens s - 0.01 = {s - 0.01:.2f} mm breed", smalst is not None and
         smalst >= s - 0.01, f"{smalst} mm")
    stap(f"{naam}: wand aan de wangkant tussen tw + s - 0.05 en tw + s (lip t dik)", buiten is not None and
         tw + s - 0.05 <= buiten <= tw + s + 0.002, f"{buiten} mm")


def _eilanden(ob):
    """Aantal losse stukken in de mesh (hoekpunten verbonden via randen)."""
    ouder = list(range(len(ob.data.vertices)))

    def wortel(i):
        while ouder[i] != i:
            ouder[i] = ouder[ouder[i]]
            i = ouder[i]
        return i
    for e in ob.data.edges:
        a, b = wortel(e.vertices[0]), wortel(e.vertices[1])
        if a != b:
            ouder[a] = b
    return len({wortel(i) for i in range(len(ouder))})


def _kort(stap, cursor, eig, neus, vorm, ops):
    """Eis 3 en controleur punt 4: de zaagbodem snijdt nooit door de onderkant van deel A.
    Staaf 10 mm, onderkant 8,5 mm onder de cursor: eigen L = 8,5 - max(t, 0,8) (korter dan 0,65 * 10 = 6,5),
    dus een lagere klikdiepte; onderkant 6 mm onder de cursor: L te kort, Tight en geen nieuwe objecten."""
    straal, s, onder = 5.0, 0.2, 8.5
    _plaats(straal, cursor, s, onder=onder)
    u = eig.eenheid_per_mm(bpy.context.scene)
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    stap("korte staaf (onderkant 8.5 mm onder H): scharnier geplaatst", uitslag == {"FINISHED"} and a and b,
         str(uitslag))
    if not (a and b):
        return
    tw = meet_neus(a, b, straal, s, u)["+H"]["tong"]
    t = straal - tw - s
    p, h, buig, lid = _as_uit_cursor(straal, u)
    diepte = onder   # H ligt in het vlak van de cursor (z = 0), de onderkant van A op onder mm daaronder
    lip = min(ZAAG * 2 * straal, diepte - max(t, 0.8))
    k_eigen = min(neus.H_MM, 0.03 * lip * lip / (1.5 * t))
    print(f"[cj-betaald] METING korte staaf: diepte {diepte:.3f} mm, eigen L {lip:.3f} mm, add-on L "
          f"{float(b.get('cj_lip', -1)) / u:.3f} mm, eigen klikdiepte {k_eigen:.4f} mm, delen A {_eilanden(a)} stuk")
    stap("korte staaf: L korter dan 0.65 keer de dikte en gelijk aan diepte - max(t, 0.8) binnen 0.01",
         lip < ZAAG * 2 * straal and abs(float(b.get("cj_lip", -1)) / u - lip) <= TOL_MM,
         f"{float(b.get('cj_lip', -1)) / u:.4f} eigen {lip:.4f}")
    _klik(stap, "korte staaf", a, b, straal, s, u, k_eigen, lip=lip)
    _zaag(stap, a, straal, s, u, tw, lip=lip, naam="korte staaf zaagsnede")
    stap("korte staaf: deel A is één stuk (de wang hangt nog aan A)", _eilanden(a) == 1, str(_eilanden(a)))
    # Onderkant van A onder de sleuf: een straal langs -L midden in de sleuf raakt de bodem van de sleuf en
    # daaronder zit nog minstens max(t, 0,8) materiaal tot de onderkant.
    bvh_a = _bvh(a)
    o = p - buig * (1.0 * u) + h * ((tw + s / 2) * u)
    hit = bvh_a.ray_cast(o, -lid)
    zaag_bodem = hit[3] / u if hit[0] is not None else -1
    stap("korte staaf: sleuf eindigt boven de onderkant van A, met minstens max(t, 0.8) mm eronder",
         hit[0] is not None and abs(zaag_bodem - lip) <= 0.06 and diepte - zaag_bodem >= max(t, 0.8) - TOL_MM,
         f"sleufbodem {zaag_bodem:.3f} mm, onderkant {diepte:.3f} mm")
    staaf = _plaats(straal, cursor, s, onder=6.0)
    voor = sorted(o.name for o in bpy.data.objects)
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError:
        uitslag = {"CANCELLED"}
    na = sorted(o.name for o in bpy.data.objects)
    reden = _reden(ops, vorm, neus, staaf, u)
    print(f"[cj-betaald] METING korte staaf 6 mm: {uitslag}, melding \"{reden}\"")
    stap("korte staaf (onderkant 6 mm onder H): Tight, CANCELLED, geen nieuwe objecten",
         uitslag == {"CANCELLED"} and voor == na and reden == neus.TIGHT, f"{uitslag} {reden}")


def toets(stap, eigen, cursor):
    eig = sys.modules[eigen + ".eigenschappen"]
    neus = sys.modules[eigen + ".betaald.scharnier_neus"]
    vorm = sys.modules[eigen + ".betaald.scharnier_vorm"]
    for straal, s in ((5.0, 0.2), (6.0, 0.3)):
        naam = f"neus staaf {2 * straal:g} mm speling {s}"
        _plaats(straal, cursor, s)
        u = eig.eenheid_per_mm(bpy.context.scene)
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
        a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
        stap(f"{naam}: scharnier geplaatst", uitslag == {"FINISHED"} and a and b, str(uitslag))
        if not (a and b):
            continue
        p, h = _as_uit_cursor(straal, u)[:2]
        stap(f"{naam}: as van de add-on is de as uit de cursor", (Vector(b["cj_scharnier_punt"]) - p).length
             < 1e-6 and abs(Vector(b["cj_scharnier_as"]).dot(h)) > 1 - 1e-9)
        klik = _klik(stap, naam, a, b, straal, s, u, neus.H_MM)
        if straal == 5.0 and klik is not None:
            tw = meet_neus(a, b, straal, s, u)["+H"]["tong"]
            _zaag(stap, a, straal, s, u, tw)
            print(f"[cj-betaald] METING tijd met neuzen en zaagsnede {b.get('cj_duur_s')} s "
                  f"solver {b.get('cj_solver')}")
    # Echte staafmaat op de lagere neus: 9 mm. Eigen rekensom: tw = 4,5/3 - s/2, t = 4,5 - tw - s,
    # L = 0,65 * 9 = 5,85; bij k = 0,25 is de rek boven 3%, dus k = 0,03 L^2 / (1,5 t).
    straal, s = 4.5, 0.2
    tw = straal / 3 - s / 2
    t, lip = straal - tw - s, ZAAG * 2 * straal
    k_eigen = min(neus.H_MM, 0.03 * lip * lip / (1.5 * t))
    rek_vol = 1.5 * t * neus.H_MM / (lip * lip)
    _plaats(straal, cursor, s)
    u = eig.eenheid_per_mm(bpy.context.scene)
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    print(f"[cj-betaald] METING staaf 9 mm: {uitslag}, rek bij 0,25 zou {rek_vol * 100:.3f}% zijn, eigen "
          f"klikdiepte {k_eigen:.4f} mm")
    stap("staaf 9 mm: rek bij klikdiepte 0.25 boven 3% (eigen rekensom)", rek_vol > 0.03, f"{rek_vol * 100:.3f}%")
    stap("staaf 9 mm: scharnier geplaatst met de lagere neus", uitslag == {"FINISHED"} and a and b, str(uitslag))
    if a and b:
        klik = _klik(stap, "neus staaf 9 mm (lagere neus)", a, b, straal, s, u, k_eigen)
        stap("staaf 9 mm: klikdiepte lager dan 0.25 en rek precies 3%", klik is not None and klik < neus.H_MM - 0.005
             and abs(float(b.get("cj_rek", -1)) - 0.03) < 1e-6, f"{klik} rek {float(b.get('cj_rek', -1)) * 100:.4f}%")
    # Dunne staaf 5 mm: nooit een scharnier dat toch geplaatst wordt.
    staaf = _plaats(2.5, cursor)
    voor = sorted(o.name for o in bpy.data.objects)
    tekst = ""
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as fout:
        uitslag, tekst = {"CANCELLED"}, str(fout)
    na = sorted(o.name for o in bpy.data.objects)
    ops = sys.modules[eigen + ".betaald.scharnier"]
    # De melding zelf: maten en neus opnieuw rekenen zoals de operator (zonder venster komt report niet terug).
    reden = _reden(ops, vorm, neus, staaf, u)
    print(f"[cj-betaald] METING dunne staaf 5 mm: {uitslag}, melding \"{reden}\", objecten {na}")
    stap("dunne staaf 5 mm: CANCELLED, geen nieuwe objecten", uitslag == {"CANCELLED"} and voor == na
         and not staaf.hide_get(), f"{uitslag} {na}")
    stap("dunne staaf 5 mm: melding te dun of Tight", reden in (vorm.TE_DUN, neus.TIGHT) and
         (not tekst or reden in tekst), reden)
    stap("Tight-rekensom: hoge neus op een korte lip geeft Tight", neus.maten_neus(
        {"s": 0.2, "wx": 5.0, "tw": 1.0, "rn": 0.3, "wy": 0.2, "r": 1.0}, 1.0) == neus.TIGHT)
    stap("rekensom: L is de afstand van H tot de zaagbodem", math.isclose(neus.ZAAG, ZAAG))
    _kort(stap, cursor, eig, neus, vorm, ops)


def _reden(ops, vorm, neus, staaf, u):
    """Melding zoals de operator: maten, dan neus met de diepte tot de onderkant (zaag_diepte)."""
    from mathutils.bvhtree import BVHTree as _B
    import bmesh
    inst = bpy.context.scene.click_joints
    punt, h, buig, lid = ops.assen(bpy.context, inst)[:4]
    frame = vorm.frame_scharnier(punt, h, buig, lid)
    bm = bmesh.new()
    bm.from_mesh(staaf.data)
    bm.transform(staaf.matrix_world)
    bvh = _B.FromBMesh(bm)
    bm.free()
    maat, reden = vorm.maten(bvh, frame, inst.speling_mm * u, 115, u)
    if maat is not None:
        reden = neus.maten_neus(maat, u, neus.zaag_diepte(bvh, frame, maat))
    return reden
