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
- Dunne staaf van 5 mm: CANCELLED met de te-dun- of Tight-melding en geen nieuwe objecten.
- Rekensom zonder mesh: wang dunner dan 0,8 mm, dan is de rest onder de zaagbodem 0,8 mm (L = diepte - 0,8).
Korte staaf en schuine onderkant staan in toetsen_neus_kort.py, de gedeelde hulp in hulp_neus.py."""
import math
import sys

import bpy
from mathutils import Vector

from hulp_neus import TOL_MM, ZAAG
from hulp_neus import as_uit_cursor as _as_uit_cursor
from hulp_neus import meet_neus
from hulp_neus import plaats as _plaats
from hulp_neus import reden as _reden
from hulp_scharnier import bvh as _bvh


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
    # Controleur punt 4: wang dunner dan 0,8 mm (t = 1,5 - 0,9 - 0,2 = 0,4), dan is de rest 0,8 en L = diepte - 0,8.
    m08 = {"s": 0.2, "wx": 1.5, "tw": 0.9, "rn": 1.0, "wy": 5.0, "r": 1.0}
    uit08 = neus.maten_neus(m08, 1.0, 4.0)
    print(f"[cj-betaald] METING rekensom t {m08.get('wang_t')} mm, diepte 4.0 mm: L {m08.get('lip')} mm")
    stap("rekensom: wang dunner dan 0.8 mm (t 0.4), dan L = diepte - 0.8 = 3.2",
         uit08 == "" and m08.get("wang_t", 9) < 0.8 and math.isclose(m08.get("lip", -1), 4.0 - 0.8, abs_tol=1e-9),
         f"{uit08!r} L {m08.get('lip')}")
