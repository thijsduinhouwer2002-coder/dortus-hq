"""Eis 5 van het scharnier (ontwerp betaald v1.1): printbaar zonder steun. Aangeroepen vanuit toetsen_scharnier.py.

Staaf van 10 mm en testarm (261K), stand 115, speling 0,2, cursor als as-bron (H = wereld-Y, lidas = X).

(a) Vlakke kant langs H om op te leggen, per deel. Het ontwerp noemt geen vaste printrichting, alleen "een vlakke
kant langs H". Rekenregel: groepeer de vlakken op dezelfde normaal (binnen 0,001) en hetzelfde vlak (n . p binnen
0,01 mm); een groep telt als oplegvlak als de normaal loodrecht op H staat (|n . H| < 0,01, dus H ligt plat op het
bed) en het hele deel aan één kant van dat vlak ligt (geen hoekpunt meer dan 0,01 mm voorbij het vlak, anders
steekt er iets door het bed). De grootste zo'n groep is het oplegvlak; de printrichting "omlaag" is zijn normaal.
Oppervlak en richting staan in de METING-regel. Op de staaf zijn dat de eindvlakken (pi x 25 = 78,5 mm2, deel A op
-L, deel B op +L). De testarm is een gebeeldhouwde ellipsoïde zonder enig vlak stuk: daar hoort (a) bij het figuur,
niet bij de add-on. Daar loggen we de grootste groep en printen we zoals de staaf, rechtop op het uiteinde van het
lid (omlaag = -L voor A, +L voor B), en toetsen we alleen (b).

(b) Overhang bij neus, kuiltje en sleuf. Rekenregel per vlak met eenheidsnormaal n en omlaag d: hoek met recht
omlaag a = acos(n . d). Een vlak kijkt naar onder als n . d > 0; de overhang is dan 90 - a (0 = verticale wand,
90 = plafond). Eis: overhang hoogstens 45 graden, dus a minstens 45 graden voor elk vlak dat naar onder kijkt.
Vlakken op het bed (n . d > 0,9999 en in het oplegvlak) tellen niet.
Welke vlakken "bij" neus, kuiltje en sleuf horen (frame: x langs H vanaf het draaipunt, rho afstand tot H,
z langs de lidas): een vlak telt als zijn middelpunt of een van zijn hoekpunten ligt in
- neus en kuiltje: tw - m <= |x| <= tw + 2s + k + m en rho <= max(voet, rand kuiltje) + m, met de rand van het
  kuiltje sqrt(h (2 rho_bol + 2s - h)) (bol met straal rho_bol + s door de wang op x = tw + s);
- sleuf (alleen deel A): tw - 0,1 s - m <= |x| <= tw + 0,95 s + m en -L - m <= z <= -s/4 + m, elke y;
met marge m = s/2 = 0,1 mm. Reden: binnen een halve speling van de vorm hoort een vlak nog bij neus, kuiltje of
sleuf (de randen waar ze in tong en wang overgaan); verder weg begint de knokkel (holle cilinder R + s, knokkel R),
die bij de neus op 0,5 mm of meer ligt en niet onder eis 5 valt. Hoekpunten tellen mee zodat lange driehoeken van
de boolean die tot in de neus reiken niet wegvallen."""
import math
import sys

import bpy
import numpy as np
from mathutils import Vector

import figuren

MARGE_S = 0.5      # marge m = 0,5 s
MAX_OVERHANG = 45.0


def _mesh(ob):
    """(hoekpunten wereld, middelpunten, normalen, oppervlakken, (hoekpunt per lus, eerste lus per vlak))."""
    me = ob.data
    n_v, n_f = len(me.vertices), len(me.polygons)
    co = np.empty(n_v * 3)
    me.vertices.foreach_get("co", co)
    mw = np.array(ob.matrix_world)
    v = co.reshape(-1, 3) @ mw[:3, :3].T + mw[:3, 3]
    nr = np.empty(n_f * 3)
    me.polygons.foreach_get("normal", nr)
    nrm = nr.reshape(-1, 3) @ np.linalg.inv(mw[:3, :3])   # normalen met de inverse-transpose
    nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    tot = np.empty(n_f, dtype=np.int32)
    me.polygons.foreach_get("loop_total", tot)
    lv = np.empty(len(me.loops), dtype=np.int32)
    me.loops.foreach_get("vertex_index", lv)
    start = np.concatenate(([0], np.cumsum(tot)[:-1])).astype(np.int64)
    mid = np.add.reduceat(v[lv], start, axis=0) / tot[:, None]
    # Oppervlak via een waaier van driehoeken per vlak (lus-index start, start + i, start + i + 1).
    eigen = np.repeat(np.arange(n_f), tot - 2)
    i = np.arange(len(eigen)) - np.repeat(np.cumsum(tot - 2) - (tot - 2), tot - 2) + 1
    p0, p1, p2 = v[lv[start[eigen]]], v[lv[start[eigen] + i]], v[lv[start[eigen] + i + 1]]
    opp = np.zeros(n_f)
    np.add.at(opp, eigen, 0.5 * np.linalg.norm(np.cross(p1 - p0, p2 - p0), axis=1))
    vlakken = (lv, start)
    return v, mid, nrm, opp, vlakken


def oplegvlak(ob, h, u):
    """(omlaag, oppervlak mm2, aantal vlakken, vlak n . p) van de grootste vlakke groep langs H die het hele deel
    draagt, of None. Zie (a) in de docstring."""
    v, mid, nrm, opp, _ = _mesh(ob)
    tol = 0.01 * u
    groepen = {}
    for j in range(len(nrm)):
        n = nrm[j]
        if abs(float(np.dot(n, h))) >= 0.01:
            continue
        sleutel = (tuple(np.round(n, 3)), round(float(np.dot(n, mid[j])) / tol))
        g = groepen.setdefault(sleutel, [0.0, 0, n, float(np.dot(n, mid[j]))])
        g[0] += opp[j]
        g[1] += 1
    for (_, _), (a, k, n, d) in sorted(groepen.items(), key=lambda kv: -kv[1][0]):
        if float((v @ n).max()) <= d + tol:
            return Vector(n.tolist()), a / (u * u), k, d
    return None


def overhang(ob, b, omlaag, bed, deel, u):
    """(grootste overhang in graden, kleinste hoek met omlaag, aantal vlakken in de buurt, slechtste vlak:
    (x, rho, z) in mm, of None) over de vlakken bij neus, kuiltje en (deel A) sleuf. Zie (b) in de docstring."""
    v, mid, nrm, opp, vlakken = _mesh(ob)
    p = np.array(list(b["cj_scharnier_punt"]))
    h, lid = (np.array(list(Vector(b[k]).normalized())) for k in ("cj_scharnier_as", "cj_as"))
    s, tw = float(b["cj_speling_mm"]) * u, float(b["cj_tong_half"])
    nh, voet, klik, lip = (float(b[k]) for k in ("cj_neus_h", "cj_neus_voet", "cj_neus_klik", "cj_lip"))
    bol = (voet * voet + nh * nh) / (2 * nh)
    rand_kuil = math.sqrt(nh * (2 * bol + 2 * s - nh))
    m = MARGE_S * s

    def frame(q):
        d = q - p
        x = d @ h
        rho = np.linalg.norm(d - np.outer(x, h), axis=1)
        return np.abs(x), x, rho, d @ lid

    def binnen(q):
        ax, _, rho, z = frame(q)
        ok = (ax >= tw - m) & (ax <= tw + 2 * s + klik + m) & (rho <= max(voet, rand_kuil) + m)
        if deel == "A":
            ok |= (ax >= tw - 0.1 * s - m) & (ax <= tw + 0.95 * s + m) & (z >= -lip - m) & (z <= -s / 4 + m)
        return ok
    in_v = binnen(v)
    lv, start = vlakken
    kies = binnen(mid) | np.logical_or.reduceat(in_v[lv], start)
    d = np.array(omlaag)
    c = nrm @ d
    op_bed = (c > 0.9999) & (np.abs(mid @ d - bed) <= 0.01 * u)
    telt = kies & ~op_bed
    if not telt.any():
        return None
    c_t = np.where(telt & (c > 0), c, -1.0)
    j = int(np.argmax(c_t))
    if c_t[j] <= 0:
        return 0.0, 90.0, int(telt.sum()), None
    a = math.degrees(math.acos(min(1.0, float(c_t[j]))))
    ax, x, rho, z = frame(mid[j:j + 1])
    return 90.0 - a, a, int(telt.sum()), (float(x[0]) / u, float(rho[0]) / u, float(z[0]) / u)


def _plaats(maak, cursor, s=0.2):
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = s
    inst.as_bron = "CURSOR"
    ob = maak()
    figuren.maak_actief(ob)
    cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    return bpy.ops.click_joints.plaats_scharnier(stand="115")


def toets(stap, eigen, cursor):
    eig = sys.modules[eigen + ".eigenschappen"]
    for naam, maak, plat in (("staaf", lambda: figuren.staaf("staaf", 5.0), True),
                             ("arm", lambda: figuren.arm("arm"), False)):
        uitslag = _plaats(maak, cursor)
        u = eig.eenheid_per_mm(bpy.context.scene)
        a, b = bpy.data.objects.get(f"{naam}_A"), bpy.data.objects.get(f"{naam}_B")
        if uitslag != {"FINISHED"} or a is None or b is None or "cj_neus_h" not in b:
            stap(f"print {naam}: scharnier geplaatst", False, str(uitslag))
            continue
        h, lid = Vector(b["cj_scharnier_as"]).normalized(), Vector(b["cj_as"]).normalized()
        for deel, ob, eind in (("A", a, -lid), ("B", b, lid)):
            vlak = oplegvlak(ob, np.array(h), u)
            if vlak is not None:
                omlaag, opp, aantal, bed = vlak
                print(f"[cj-betaald] METING print {naam} deel {deel}: oplegvlak langs H {opp:.2f} mm2 in {aantal} "
                      f"vlakken, omlaag {tuple(round(c, 3) for c in omlaag)}, |n.H| {abs(omlaag.dot(h)):.4f}")
            else:
                print(f"[cj-betaald] METING print {naam} deel {deel}: geen vlakke kant langs H die het deel draagt")
            if plat:
                stap(f"print {naam} deel {deel}: vlakke kant langs H om op te leggen (eindvlak, minstens 70 mm2)",
                     vlak is not None and vlak[1] >= 70.0 and abs(vlak[0].dot(h)) < 0.01,
                     f"{vlak[1]:.2f} mm2" if vlak else "geen")
            if vlak is None or not plat:
                # Arm zonder vlak stuk: rechtop op het uiteinde van het lid, zoals de staaf.
                omlaag = eind
                bed = max(float((ob.matrix_world @ w.co).dot(eind)) for w in ob.data.vertices)
            uit = overhang(ob, b, omlaag, bed, deel, u)
            if uit is None:
                stap(f"print {naam} deel {deel}: vlakken bij neus en kuiltje gevonden", False)
                continue
            oh, hoek, aantal, plek = uit
            plek_t = f"(x {plek[0]:.3f}, rho {plek[1]:.3f}, z {plek[2]:.3f} mm)" if plek else "geen vlak naar onder"
            print(f"[cj-betaald] METING print {naam} deel {deel}: grootste overhang bij neus, kuiltje"
                  f"{' en sleuf' if deel == 'A' else ''} {oh:.2f} graden (hoek met omlaag {hoek:.2f}) over {aantal} "
                  f"vlakken, slechtste vlak {plek_t}, omlaag {tuple(round(c, 3) for c in omlaag)}")
            stap(f"print {naam} deel {deel}: geen overhang boven {MAX_OVERHANG:.0f} graden bij neus, kuiltje"
                 f"{' en sleuf' if deel == 'A' else ''}", oh <= MAX_OVERHANG, f"{oh:.2f} graden {plek_t}")
