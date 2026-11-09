"""Klikneuzen van het scharnier (ontwerp betaald v1.1, vorm punt 5, eis 3), alleen in de betaalde build.

Op beide zijkanten van de tong van B (x = +tw en -tw in het frame van scharnier_vorm) een bolkapje met
hoogte h = 0,25 mm en zijn top precies op as H. In de wang van A een kuiltje: een bol met dezelfde
middelpunt en straal + s, dus overal speling s om de neus. Omdat neus en kuiltje allebei rond H draaien,
blijft die speling bij elke buighoek gelijk; de neus houdt het scharnier niet tegen, hij klikt alleen bij
het in elkaar zetten (de wang moet h - s = 0,05 mm verder opzij dan de speling) en houdt B daarna langs H vast.

Rek van de wang bij indrukken (ontwerp, balkformule, GOK van de controleur): eps = 1,5 * t * h / L^2, met
t de dikte van de wang langs H (wx - tw - s) en L de lengte van de buigzame lip: van H tot de bodem van de
zaagsnede, die vanaf de bovenrand van de wang (rn - s/2 boven H) tot 60% van de dikte van het lid (0,6 * 2 wy)
onder H gaat. Is eps groter dan 3%, dan een lagere neus; lager dan H_MIN dan geen scharnier maar de melding
TIGHT (nooit een rood scharnier dat toch geplaatst wordt).
De zaagsnede zelf wordt in deze ronde nog niet gesneden (open punt); de rek is die van de geplande lip."""
import math

import bmesh
import bpy
from mathutils import Matrix

H_MM = 0.25          # hoogte van de neus (ontwerp)
H_MIN_MM = 0.1       # lager klikt niet meer merkbaar: dan de melding
REK_MAX = 0.03       # 3%, PLA breekt rond 3 tot 5%
BASIS = 0.6          # straal van de voet van de neus = BASIS keer de knokkelstraal R
ZAAG = 0.6           # zaagsnede tot 60% van de dikte van het lid onder H
RINGEN = 10
SEGMENTEN = 32
TIGHT = "Tight: cheek too stiff to click. Try a thicker spot."


def rek(t, h, lip):
    """Berekende rek van de lip (balkformule uit het ontwerp)."""
    return 1.5 * t * h / (lip * lip)


def maten_neus(m, u):
    """Vult m aan met de neusmaten (h, voet, bolstraal, wangdikte, lip, rek) of geeft de melding TIGHT terug."""
    s = m["s"]
    t = m["wx"] - m["tw"] - s
    lip = (m["rn"] - s / 2) + ZAAG * 2 * m["wy"]
    h = H_MM * u
    if rek(t, h, lip) > REK_MAX:
        h = REK_MAX * lip * lip / (1.5 * t)
    if h < H_MIN_MM * u or t <= 0:
        return TIGHT
    voet = BASIS * m["r"]
    rho = (voet * voet + h * h) / (2 * h)       # straal van de bol waar het kapje van is
    m.update({"neus_h": h, "neus_voet": voet, "neus_rho": rho, "wang_t": t, "lip": lip,
              "rek": rek(t, h, lip)})
    return ""


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
