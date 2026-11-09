"""Vorm van het scharnier (ontwerp betaald v1.1, punt "Vorm"): maten en snijden, zonder operator.

Frame van het scharnier: oorsprong op de 3D-cursor, X = scharnieras H, Y = buigkant (de knie buigt naar +Y),
Z = lidas L (deel A onder, deel B boven, zoals bij de kogel). De as H zelf ligt e = 0,15 keer de dikte naar
achteren (-Y), dat punt heet hier het draaipunt (y = -e, z = 0).

Vlakken tussen A en B (doorsnede loodrecht op H):
- achter het draaipunt: B begint op z = +s/2, A houdt op bij z = -s/2. Dat is de achterstop: doorknikken gaat
  hoogstens ongeveer atan(s / r_lip) voorbij rechtdoor.
- voor het draaipunt de wig (eindstop): het stopvlak van B staat op hoek +a, dat van A op -a, elk evenwijdig
  op s/2 van een vlak door H. Bij een draai van 2a lopen de twee vlakken evenwijdig, maar aan weerszijden van
  H, dus nog met een spleet s; de rand van B (afstand r van H) raakt pas na nog ongeveer s/r. De echte stop
  is dus 2a + s/r (exact 2a + 2 atan(s / (2 sqrt(r^2 - s^2/4))), minder dan 0,001 graad verschil). Daarom
  a = (N - s/r_buiten) / 2, zodat de stop op de stand N ligt (ontwerp v1.1; controleur ronde t2 rekende de
  zuivere doorsnede na: 90,0 / 115,0 / 135,0 bij r 6,5 mm en s 0,2 mm).
Zijwaarts drie derden langs H: de tong van B (|x| < tw) met de knokkel (cilinder straal R om H), en de
wangen van A (|x| > tw + s), elk een cilinder met straal Rn - s/2 om H. B houdt buiten de tong afstand
(cilinder Rn + s/2), dus B draait langs de wangen zonder te botsen (zelfde truc als de bolnaad).
A heeft in de gleuf (|x| < tw + s) de holle cilinder R + s om H. Overal tussen A en B zit dus de speling s.
"""
import math

import bmesh
import bpy
from mathutils import Matrix, Vector

from .. import vormen
from ..gewricht import bak, boolean

STANDEN = (90, 115, 135)
STAND_STANDAARD = 115
ACHTER = 0.15     # e = ACHTER keer de dikte langs de buigkant
KNOKKEL = 0.35    # R = KNOKKEL keer de halve dikte
WANG = 0.20       # Rn = R + s + WANG keer de halve dikte
MARGE = 0.6       # graden: de stop mikt zoveel onder de stand, zodat hij er nooit voorbij ligt (eis 2)
TE_DUN = "Too thin here for a hinge. Try a thicker spot."
KIJK_LANGS = "Look at the joint from the side to place a hinge."


def frame_scharnier(punt, h, buig, lid):
    """Matrix met oorsprong op het punt, X = H, Y = buigkant, Z = lidas (rechtshandig)."""
    m = Matrix.Identity(4)
    for i, v in enumerate((h, buig, lid)):
        m.col[i][:3] = v
    m.col[3][:3] = punt
    return m


def scharnier_assen(lid, kijk=None, omhoog=None, cursor_x=None, cursor_y=None):
    """(H, buigkant, lidas, hoek tussen kijkrichting en lidas in graden) of None als de kijkhoek te klein is.

    Met een kijkrichting: H is de kijkrichting geprojecteerd loodrecht op L, de buigkant is de omhoog-richting
    van de kijker loodrecht op H en L. Zonder kijkrichting (as-bron Cursor): H = X-as en buigkant = Y-as van
    de cursor, ook loodrecht op L gemaakt."""
    lid = lid.normalized()
    if kijk is not None:
        hoek = math.degrees(lid.angle(kijk)) if kijk.length > 0 else 0.0
        hoek = min(hoek, 180.0 - hoek)
        if hoek < 30.0:
            return None
        h = (kijk - lid * kijk.dot(lid)).normalized()
        voorkeur = omhoog
    else:
        hoek = 90.0
        h = (cursor_x - lid * cursor_x.dot(lid)).normalized()
        voorkeur = cursor_y
    buig = lid.cross(h).normalized()
    if voorkeur is not None and buig.dot(voorkeur) < 0:
        # Buigkant naar de voorkeur: H omdraaien houdt het frame rechtshandig (de as zelf blijft dezelfde lijn).
        h, buig = -h, -buig
    return h, buig, lid, hoek


def straal_tot_huid(bvh, frame, richting):
    """Afstand van de oorsprong van het frame tot de huid langs een richting in het frame, of None."""
    oorsprong = frame.to_translation()
    w = (frame.to_3x3() @ Vector(richting)).normalized()
    hit = bvh.ray_cast(oorsprong, w)
    return None if hit[0] is None else hit[3]


def maten(bvh, frame, s, stand, u):
    """Maten van het scharnier, of (None, reden) als het lid te dun is of de cursor buiten het figuur ligt."""
    zij = [straal_tot_huid(bvh, frame, r) for r in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0))]
    if any(z is None for z in zij):
        return None, "Put the 3D cursor inside the mesh to place a hinge."
    wx = min(zij[0], zij[1])          # halve breedte langs H
    wy = min(zij[2], zij[3])          # halve dikte langs de buigkant
    e = ACHTER * 2 * wy
    r = KNOKKEL * wy
    rn = r + s + WANG * wy
    tw = wx / 3 - s / 2
    if tw < 0.6 * u or (wy - e) - (rn + s / 2) < 0.3 * u or r < 0.6 * u:
        return None, TE_DUN
    r_buiten = zij[2] + e             # van H tot de voorkant van het lid
    theta_s = s / r_buiten
    # Marge (run 28): gemeten in de mesh lag de stop op de staaf van 128 hoeken bij stand 90 op 90,55, dus
    # 0,55 voorbij de stand (bij 115 en 135 op -0,8 en -1,1). Mikken op stand - 0,6 houdt alle drie binnen 2 onder.
    alfa = (math.radians(stand - MARGE) - theta_s) / 2
    r_lip = zij[3] - e                # van H tot de achterkant van het lid (raakpunt achterstop)
    return {"s": s, "e": e, "r_lip": r_lip, "r": r, "rn": rn, "tw": tw, "wx": wx, "wy": wy, "stand": stand,
            "alfa": alfa, "theta_s": theta_s, "r_buiten": r_buiten}, ""


def stop_graden(alfa, theta_s):
    """De echte eindstop in graden: 2a + s/r (zie boven)."""
    return math.degrees(2 * alfa + theta_s)


def prisma(naam, punten, x0, x1, frame, collectie):
    """Gesloten prisma: veelhoek (y, z) in het frame, langs X van x0 tot x1."""
    bm = bmesh.new()
    onder = [bm.verts.new((x0, y, z)) for y, z in punten]
    boven = [bm.verts.new((x1, y, z)) for y, z in punten]
    bm.faces.new(list(reversed(onder)))
    bm.faces.new(boven)
    n = len(punten)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((onder[i], onder[j], boven[j], boven[i]))
    bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts) > 4])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    bm.transform(frame)
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    collectie.objects.link(ob)
    return ob


def onder_b(m, g):
    """Doorsnede van alles onder deel B (achterstop op +s/2, wig op hoek +a)."""
    yp, s, ta = -m["e"], m["s"], math.tan(m["alfa"])
    c = s / (2 * math.cos(m["alfa"]))
    y_top = yp + (g - c) / ta
    return [(-g, -g), (g, -g), (g, g), (min(y_top, g - 1e-3), g), (yp, c), (yp, s / 2), (-g, s / 2)]


def boven_a(m, g):
    """Doorsnede van alles boven deel A (achterstop op -s/2, wig op hoek -a)."""
    yp, s, ta = -m["e"], m["s"], math.tan(m["alfa"])
    c = s / (2 * math.cos(m["alfa"]))
    y_bodem = yp + (g - c) / ta
    return [(-g, -s / 2), (yp, -s / 2), (yp, -c), (min(y_bodem, g - 1e-3), -g), (g, -g), (g, g), (-g, g)]


def as_cilinder(naam, r, x0, x1, frame, m, collectie):
    """Cilinder om H (de X-as door het draaipunt) van x0 tot x1."""
    f = frame @ Matrix.Translation((0, -m["e"], 0)) @ Matrix.Rotation(math.pi / 2, 4, "Y")
    # Na een kwartslag om Y wijst de lokale Z langs +X van het frame.
    return vormen.cilinder(naam, r, x0, x1, f, collectie)


def snij(hulp, werk, frame, m, solver):
    """(deel A, deel B) in de hulpcollectie. Booleans zoals gewricht.py: gereedschap eerst los tot één
    gesloten vorm, daarna één verschil per stap op een gebakken kopie van het figuur."""
    g = max(werk.dimensions) * 2 + 20 * m["rn"]
    s, tw, rn = m["s"], m["tw"], m["rn"]
    # Deel A = figuur zonder (boven A, plus de holle cilinder R + s, min de twee wangen).
    gereed_a = prisma("cj_boven_a", boven_a(m, g), -g, g, frame, hulp)
    gat = as_cilinder("cj_knokkel_gat", m["r"] + s, -g, g, frame, m, hulp)
    boolean(gereed_a, gat, "UNION", solver)
    for k, (x0, x1) in enumerate(((tw + s, g * 1.1), (-g * 1.1, -(tw + s)))):
        wang = as_cilinder(f"cj_wang_{k}", rn - s / 2, x0, x1, frame, m, hulp)
        boolean(gereed_a, wang, "DIFFERENCE", solver)
    gereed_a = bak(gereed_a, "cj_snij_a", hulp)
    gereed_a.hide_set(True)
    a = bak(werk, "cj_a_bron", hulp)
    boolean(a, gereed_a, "DIFFERENCE", solver)
    deel_a = bak(a, "cj_deel_a", hulp)
    # Deel B = figuur zonder (onder B min de knokkel), dan zonder de naad Rn + s/2 naast de tong.
    gereed_b = prisma("cj_onder_b", onder_b(m, g), -g, g, frame, hulp)
    knokkel = as_cilinder("cj_knokkel", m["r"], -tw, tw, frame, m, hulp)
    boolean(gereed_b, knokkel, "DIFFERENCE", solver)
    gereed_b = bak(gereed_b, "cj_snij_b", hulp)
    gereed_b.hide_set(True)
    b = bak(werk, "cj_b_bron", hulp)
    boolean(b, gereed_b, "DIFFERENCE", solver)
    for k, (x0, x1) in enumerate(((tw, g * 1.1), (-g * 1.1, -tw))):
        naad = as_cilinder(f"cj_naad_{k}", rn + s / 2, x0, x1, frame, m, hulp)
        boolean(b, naad, "DIFFERENCE", solver)
    deel_b = bak(b, "cj_deel_b", hulp)
    return deel_a, deel_b
