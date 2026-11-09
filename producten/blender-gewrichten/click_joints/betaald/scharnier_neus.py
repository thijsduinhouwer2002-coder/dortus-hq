"""Klikneuzen van het scharnier (ontwerp betaald v1.1, vorm punt 5, eis 3), alleen in de betaalde build.

Op beide zijkanten van de tong van B (x = +tw en -tw in het frame van scharnier_vorm) een bolkapje met zijn
top precies op as H. De klikdiepte k = 0,25 mm is wat telt (besluit manager na de controleur): de neus steekt
k voorbij de speling uit, dus de top ligt op x = tw + s + k en de neus is s + k hoog boven het zijvlak van de
tong. In de wang van A een kuiltje: een bol met hetzelfde middelpunt en straal + s, dus overal speling s om de
neus. Omdat neus en kuiltje allebei rond H draaien, blijft die speling bij elke buighoek gelijk; bij het in
elkaar zetten moet de wang k opzij en daarna houdt de neus B langs H vast.

Rek van de wang bij indrukken (ontwerp, balkformule, GOK van de controleur): eps = 1,5 * t * k / L^2, met
t de dikte van de wang langs H (wx - tw - s), k de klikdiepte en L de lengte van de buigzame lip: van as H tot
de bodem van de zaagsnede (correctie controleur), die ZAAG keer de dikte van het lid (ZAAG * 2 wy) onder H ligt.
De zaagsnede zelf snijdt scharnier_vorm.snij (zaag_maten hieronder). Is eps groter dan 3%, dan een kleinere
klikdiepte; kleiner dan H_MIN dan geen scharnier maar de melding TIGHT (nooit een rood scharnier dat toch
geplaatst wordt)."""
import math

import bmesh
import bpy
from mathutils import Matrix

H_MM = 0.25          # klikdiepte: hoe ver de neus voorbij de speling uitsteekt (ontwerp, besluit manager)
H_MIN_MM = 0.1       # minder klikt niet meer merkbaar: dan de melding
REK_MAX = 0.03       # 3%, PLA breekt rond 3 tot 5%
BASIS = 0.6          # straal van de voet van de neus = BASIS keer de knokkelstraal R
ZAAG = 0.65          # bodem van de zaagsnede op 0,65 keer de dikte van het lid onder H
ZAAG_X = (0.4, 0.8)  # zaagsnede in de wang-voet, van tw + 0,4 s tot tw + 0,8 s (los van alle andere vlakken)
RINGEN = 10
SEGMENTEN = 32
TIGHT = "Tight: cheek too stiff to click. Try a thicker spot."


def rek(t, h, lip):
    """Berekende rek van de lip (balkformule uit het ontwerp)."""
    return 1.5 * t * h / (lip * lip)


def maten_neus(m, u):
    """Vult m aan met de neusmaten of geeft de melding TIGHT terug.
    klik = klikdiepte k, neus_h = hoogte boven het zijvlak van de tong (s + k), lip = L (H tot zaagbodem)."""
    s = m["s"]
    t = m["wx"] - m["tw"] - s
    lip = ZAAG * 2 * m["wy"]
    k = H_MM * u
    if t > 0 and rek(t, k, lip) > REK_MAX:
        k = REK_MAX * lip * lip / (1.5 * t)
    if k < H_MIN_MM * u or t <= 0:
        return TIGHT
    h = s + k
    voet = BASIS * m["r"]
    rho = (voet * voet + h * h) / (2 * h)       # straal van de bol waar het kapje van is
    m.update({"neus_h": h, "neus_klik": k, "neus_voet": voet, "neus_rho": rho, "wang_t": t, "lip": lip,
              "rek": rek(t, k, lip)})
    return ""


def zaag_maten(m):
    """(x0, x1, z_bodem, z_top) van de zaagsnede in het frame (x langs H, z langs de lidas), voor de + kant.
    Een smalle sleuf onder de gleuf, door de hele diepte van het lid (langs de buigkant): zo hangt de wang
    met zijn buitenste derde alleen nog onder de zaagbodem aan deel A en veert hij opzij als een lip."""
    s, tw = m["s"], m["tw"]
    return tw + ZAAG_X[0] * s, tw + ZAAG_X[1] * s, -m["lip"], -s / 4


def _draailichaam(naam, profiel, frame, collectie):
    """Gesloten lichaam rond de lokale X-as: profiel [(x, straal)], eerste en laatste straal 0 (polen)."""
    bm = bmesh.new()
    pool0 = bm.verts.new((profiel[0][0], 0, 0))
    ringen = []
    for x, rr in profiel[1:-1]:
        ringen.append([bm.verts.new((x, rr * math.cos(2 * math.pi * k / SEGMENTEN),
                                     rr * math.sin(2 * math.pi * k / SEGMENTEN))) for k in range(SEGMENTEN)])
    pool1 = bm.verts.new((profiel[-1][0], 0, 0))
    n = SEGMENTEN
    for k in range(n):
        bm.faces.new((pool0, ringen[0][(k + 1) % n], ringen[0][k]))
        bm.faces.new((pool1, ringen[-1][k], ringen[-1][(k + 1) % n]))
    for a, b in zip(ringen, ringen[1:]):
        for k in range(n):
            bm.faces.new((a[k], a[(k + 1) % n], b[(k + 1) % n], b[k]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    bm.transform(frame)
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    collectie.objects.link(ob)
    return ob


def _kap(x_top, rho, x_voet, x_bodem):
    """Profiel van een bolkap met top op x_top, bolstraal rho, vanaf x_bodem (onder de voet) tot de top.
    Geen ring precies op x_voet (het vlak van de tong of de wang), zodat de boolean geen vlak-op-vlak krijgt."""
    cx = x_top - rho
    phi0 = math.acos(max(-1.0, min(1.0, (x_bodem - cx) / rho)))
    profiel = [(x_bodem, 0.0)]
    for i in range(RINGEN + 1):
        phi = phi0 * (1 - i / (RINGEN + 0.5))   # nooit 0 (dat is de pool) en niet op x_voet
        profiel.append((cx + rho * math.cos(phi), rho * math.sin(phi)))
    profiel.append((x_top, 0.0))
    return profiel


def neuzen(frame, m, collectie, kuiltje=False):
    """Twee lichamen (x = +tw en -tw): de neuzen van B, of met kuiltje=True de kuiltjes van A (straal + s)."""
    tw, h, rho, s = m["tw"], m["neus_h"], m["neus_rho"], m["s"]
    extra = s if kuiltje else 0.0
    obs = []
    for k, teken in enumerate((1, -1)):
        # Lokale X langs teken * H; oorsprong op het draaipunt (y = -e), dus de top ligt op H.
        rot = Matrix.Identity(4) if teken > 0 else Matrix.Rotation(math.pi, 4, "Z")
        f = frame @ Matrix.Translation((0, -m["e"], 0)) @ rot
        top = tw + h + extra
        # Bodem iets in het lichaam waar het aan vast zit (tong) of in de gleuf (kuiltje), binnen de knokkel.
        bodem = tw - 0.3 * h if not kuiltje else tw + 0.3 * s
        profiel = _kap(top, rho + extra, tw + extra, bodem)
        naam = f"cj_{'kuiltje' if kuiltje else 'neus'}_{k}"
        obs.append(_draailichaam(naam, profiel, f, collectie))
    return obs
