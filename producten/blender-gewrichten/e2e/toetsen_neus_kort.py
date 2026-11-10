"""Toetsen van de sleuf bij een onderkant dicht bij H (eis 3, controleur punt 4 en 5), aangeroepen vanuit
toetsen_scharnier.py na toetsen_neus.py.
- Korte staaf: de sleuf wordt korter (L = diepte - max(t, 0,8)), deel A blijft één stuk, A en B gesloten en de
  sleuf eindigt boven de onderkant; nog korter geeft Tight en geen objecten.
- Schuine onderkant (figuren.balk met ronde randen langs H, profile 0,5): de add-on meet de diepte ook vlak bij
  de randen van de buigkant (eigen rekensom rond_diepte, 5,603 in plaats van 8); deel A één stuk en zonder open
  randen, en bij de achterrand en de voorrand eindigt de sleuf op L met minstens max(t, 0,8) materiaal eronder.
  Dezelfde balk met de onderkant 6,5 mm onder H geeft Tight (midden alleen zou nog een scharnier geven).
- Taps lid (toetsen_neus_taps.py): geen Tight."""
import math
import sys

import bpy
from mathutils import Matrix, Vector

import figuren
from hulp_neus import TOL_MM, ZAAG, eilanden, meet_neus
from hulp_neus import as_uit_cursor as _as_uit_cursor
from hulp_neus import plaats as _plaats
from hulp_neus import reden as _reden
from hulp_scharnier import bvh as _bvh
from toetsen_neus import _klik, _zaag
import toetsen_neus_taps


def toets(stap, eigen, cursor):
    eig = sys.modules[eigen + ".eigenschappen"]
    neus = sys.modules[eigen + ".betaald.scharnier_neus"]
    vorm = sys.modules[eigen + ".betaald.scharnier_vorm"]
    ops = sys.modules[eigen + ".betaald.scharnier"]
    gesloten = sys.modules[eigen + ".gesloten"]
    _kort(stap, cursor, eig, neus, vorm, ops, gesloten)
    _schuin(stap, cursor, eig, gesloten)
    _schuin_tight(stap, cursor, eig, neus, vorm, ops)
    toetsen_neus_taps.toets(stap, cursor, eig, neus, gesloten)


def _kort(stap, cursor, eig, neus, vorm, ops, gesloten):
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
          f"{float(b.get('cj_lip', -1)) / u:.3f} mm, eigen klikdiepte {k_eigen:.4f} mm, delen A {eilanden(a)} stuk")
    stap("korte staaf: L korter dan 0.65 keer de dikte en gelijk aan diepte - max(t, 0.8) binnen 0.01",
         lip < ZAAG * 2 * straal and abs(float(b.get("cj_lip", -1)) / u - lip) <= TOL_MM,
         f"{float(b.get('cj_lip', -1)) / u:.4f} eigen {lip:.4f}")
    _klik(stap, "korte staaf", a, b, straal, s, u, k_eigen, lip=lip)
    _zaag(stap, a, straal, s, u, tw, lip=lip, naam="korte staaf zaagsnede")
    stap("korte staaf: deel A is één stuk (de wang hangt nog aan A)", eilanden(a) == 1, str(eilanden(a)))
    ga, gb = gesloten.is_gesloten(a), gesloten.is_gesloten(b)
    stap("korte staaf: A en B gesloten (0 open randen)", ga[0] and gb[0], f"A {ga[1]} B {gb[1]} foute randen")
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


BREED, DIK, LENGTE, SCHUIN = 40.0, 10.0, 6.0, 3.0


def rond_diepte(y, onder, half=DIK / 2, r=SCHUIN):
    """Eigen rekensom: diepte van de onderkant van de balk op afstand y van het midden (langs de buigkant).
    Ronde hoek in twee stukken (profile 0,5): punten (half, onder - r), (half - r + r cos 45, onder - r + r sin 45)
    en (half - r, onder); daartussen rechte stukken, binnen half - r de vlakke onderkant."""
    y = abs(y)
    c = r * math.cos(math.pi / 4)
    pts = [(half, onder - r), (half - r + c, onder - r + c), (half - r, onder)]
    for (y0, d0), (y1, d1) in zip(pts, pts[1:]):
        if y1 <= y <= y0:
            return d0 + (y0 - y) / (y0 - y1) * (d1 - d0)
    return onder


def _balk(cursor, eig, onder, s=0.2):
    """Balk 6 mm langs H, 10 mm dik langs de buigkant, randen langs H rond met straal 3 mm, onderkant van A
    onder mm onder de cursor; plaatst het scharnier. (uitslag, A, B, u)."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = s
    inst.as_bron = "CURSOR"
    balk = figuren.balk("balk", BREED, DIK, lengte=LENGTE, schuin=SCHUIN)
    # Lengte langs wereld-Y (H), breedte langs wereld-X (lidas), dikte langs Z (buigkant).
    balk.data.transform(Matrix.Translation((BREED / 2 - onder, 0, 0)) @ Matrix.Rotation(math.pi / 2, 4, "Z"))
    figuren.maak_actief(balk)
    cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as fout:
        uitslag = f"fout: {fout}"
    return uitslag, bpy.data.objects.get("balk_A"), bpy.data.objects.get("balk_B"), eig.eenheid_per_mm(
        bpy.context.scene)


def _schuin(stap, cursor, eig, gesloten):
    """Onderkant van A 8 mm onder de cursor. Midden gemeten zou L = min(6,5, 8 - t) = 6,1 zijn; de ronde hoek
    komt aan de rand dichter bij H. Eigen rekensom: wx 3, tw = 0,9, t = 1,9; zijmaat 5, dus de add-on meet op
    0,95 x 5 = 4,75 van het midden: diepte rond_diepte(4,75, 8) = 5,603 (vlak op 67,5 graden van de lidas)."""
    onder, s = 8.0, 0.2
    uitslag, a, b, u = _balk(cursor, eig, onder, s)
    stap("schuine onderkant: scharnier geplaatst", uitslag == {"FINISHED"} and a and b, str(uitslag))
    if not (a and b):
        return
    tw = LENGTE / 2 / 3 - s / 2
    t = LENGTE / 2 - tw - s
    eigen = min(rond_diepte(f * DIK / 2, onder) for f in (0.0, 0.5, 0.95))
    diepte, lip = float(b.get("cj_zaag_diepte", -1)) / u, float(b.get("cj_lip", -1)) / u
    stuk, ga = eilanden(a), gesloten.is_gesloten(a)
    print(f"[cj-betaald] METING schuine onderkant: diepte add-on {diepte:.3f} mm, eigen {eigen:.3f} (midden "
          f"{onder}), L {lip:.3f} mm, t {t:.3f} mm, delen A {stuk} stuk, A {ga[1]} foute randen")
    stap("schuine onderkant: diepte bij de rand gelijk aan de eigen rekensom (ronde hoek) en L = diepte - max(t, 0.8)",
         abs(diepte - eigen) <= TOL_MM and abs(lip - (eigen - max(t, 0.8))) <= TOL_MM,
         f"diepte {diepte:.3f} eigen {eigen:.3f} L {lip:.3f}")
    stap("schuine onderkant: deel A is één stuk", stuk == 1, str(stuk))
    stap("schuine onderkant: deel A gesloten (0 open randen)", ga[0], f"{ga[1]} foute randen")
    _randen(stap, a, tw, t, s, lip, u)


def _randen(stap, a, tw, t, s, lip, u):
    """Sleufbodem bij de achterrand (0,95 van de halve dikte) en bij de voorrand, per wang: de sleuf ligt recht
    en even lang onder beide wangen. De voorkant van A zakt door de wig weg; voorrand = 0,95 van waar A net
    onder de sleufbodem ophoudt (straal langs +buig op L + 0,02)."""
    m = bpy.context.scene.cursor.matrix
    c, h, buig, lid = m.to_translation(), m.col[0].xyz.normalized(), m.col[1].xyz.normalized(), m.col[2].xyz
    lid = lid.normalized()
    bvh_a = _bvh(a)
    for teken, kant in ((1, "+H"), (-1, "-H")):
        x = c + h * (teken * (tw + s / 2) * u)
        voor = bvh_a.ray_cast(x - lid * ((lip + 0.02) * u), buig)
        y_voor = 0.95 * voor[3] / u if voor[0] is not None else 0.0
        for rand, y in (("achterrand", -0.95 * DIK / 2), ("voorrand", y_voor)):
            o = x + buig * (y * u) - lid * ((lip - 0.2) * u)
            hit = bvh_a.ray_cast(o, -lid)
            bodem = rest = -1.0
            if hit[0] is not None and hit[1].dot(lid) > 0.5:
                bodem = lip - 0.2 + hit[3] / u
                onderkant = bvh_a.ray_cast(hit[0] - lid * (1e-4 * u), -lid)
                rest = onderkant[3] / u if onderkant[0] is not None else -1.0
            print(f"[cj-betaald] METING schuine onderkant {kant} bij de {rand} (buig {y:.3f} mm): sleufbodem "
                  f"{bodem:.3f} mm onder H, materiaal eronder {rest:.3f} mm")
            stap(f"schuine onderkant {kant}: bij de {rand} eindigt de sleuf op L met minstens max(t, 0.8) eronder",
                 abs(bodem - lip) <= 0.06 and rest >= max(t, 0.8) - 0.06, f"bodem {bodem:.3f} rest {rest:.3f}")


def _schuin_tight(stap, cursor, eig, neus, vorm, ops):
    """Echt dunne onderkant: onderkant 6,5 mm onder H. Alleen midden gemeten: L = 6,5 - 1,9 = 4,6, klikdiepte
    min(0,25, 0,03 x 4,6^2 / (1,5 x 1,9)) = 0,223, dus wel een scharnier. Met de rand: diepte rond_diepte(4,75,
    6,5) = 4,103, L = 2,203, klikdiepte 0,051 onder 0,1: Tight, CANCELLED en geen objecten. De reden moet
    neus.TIGHT zijn (zoals bij de korte staaf), niet zomaar een andere weigering."""
    onder, t = 6.5, 1.9
    lip = rond_diepte(0.95 * DIK / 2, onder) - t
    k = 0.03 * lip * lip / (1.5 * t)
    uitslag, a, b, u = _balk(cursor, eig, onder)
    tight = uitslag == {"CANCELLED"} or (isinstance(uitslag, str) and "Tight" in uitslag)
    balk = bpy.data.objects.get("balk")
    reden = _reden(ops, vorm, neus, balk, u) if balk else None
    print(f"[cj-betaald] METING dunne ronde onderkant 6.5 mm: {uitslag}, melding \"{reden}\", eigen L {lip:.3f} "
          f"klikdiepte {k:.4f}")
    stap("dunne ronde onderkant (6.5 mm onder H, rand 4.1 mm): eigen klikdiepte onder 0.1 en Tight (CANCELLED, "
         "melding Tight, geen delen)", k < 0.1 and tight and reden == neus.TIGHT and a is None and b is None
         and len(bpy.data.objects) == 1, f"{uitslag} {reden} k {k:.4f}")
