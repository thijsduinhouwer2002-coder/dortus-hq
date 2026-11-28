"""Pro 1.2.7: scharnier na Shift + rechtsklik (melding Regisseur 24 nov, opname clip 3).

Shift + rechtsklik zet de 3D-cursor op de huid, met de standaard keymap gedraaid naar de kijker (orientation VIEW):
de Z-as van de cursor wijst dan langs de kijkrichting. Met as-bron View direction gaf dat "Look at the joint from
the side" (lidas langs de kijkrichting) en met een rechte cursor "Too thin" (punt op de huid, breedte bijna 0).

Hier twee stappen, alleen voor die gevallen:
1. lid_uit_vorm: ligt de cursor-Z binnen 30 graden van de kijkrichting, dan schatten we de lidas uit het figuur.
   In het vlak van het scherm door het punt meten we de breedte in 36 richtingen; het lid loopt dwars op de
   smalste. De smalste richting is plaatselijk (de doorsnede van de knie); de langste kan een voet of romp raken.
2. naar_midden: ligt het punt op de huid (binnen RAND_MM), dan schuift het naar het midden van de doorsnede
   loodrecht op het lid: eerst langs de kijkrichting (voorkant en achterkant), dan dwars daarop.
Alleen als het punt op de huid ligt (het kenmerk van Shift + rechtsklik). Een cursor binnen het figuur blijft zoals
hij was, ook de weigering bij een lidas langs de kijkrichting (toetsen_kijk): rig.py, de presets uit scripts en de
e2e zetten de cursor zelf binnen het lid. Met as-bron Cursor verandert er niets."""
import math

from mathutils import Vector

RAND_MM = 0.5     # dichter bij de huid dan dit: het punt telt als "op de huid"
STAPPEN = 36      # richtingen in het schermvlak (elke 5 graden over 180)
KIJK_MIN = 30.0   # zelfde grens als scharnier_vorm.scharnier_assen


def _straal(bvh, oorsprong, richting):
    hit = bvh.ray_cast(oorsprong, richting)
    return None if hit[0] is None else hit[3]


def _breedte(bvh, punt, d):
    """(breedte, verschuiving naar het midden) langs richting d vanuit punt, of None."""
    a, b = _straal(bvh, punt, d), _straal(bvh, punt, -d)
    if a is None or b is None:
        return None
    return a + b, (a - b) / 2.0


def _basis(n):
    """Twee eenheidsvectoren loodrecht op n en op elkaar."""
    hulp = Vector((0, 0, 1)) if abs(n.z) < 0.9 else Vector((1, 0, 0))
    e1 = n.cross(hulp).normalized()
    return e1, n.cross(e1).normalized()


def langs_kijk(lid, kijk):
    """True als de lidas binnen KIJK_MIN graden van de kijkrichting ligt (dan weigert scharnier_assen)."""
    hoek = math.degrees(lid.angle(kijk)) if lid.length > 0 and kijk.length > 0 else 0.0
    return min(hoek, 180.0 - hoek) < KIJK_MIN


def op_huid(bvh, punt, u):
    near = bvh.find_nearest(punt)
    return near[0] is not None and near[3] <= RAND_MM * u


def diepte_midden(bvh, punt, kijk, u):
    """Midden tussen voorkant en achterkant van het figuur langs de kijkrichting, door punt. None bij mis."""
    k = kijk.normalized()
    start = punt - k * (2.0 * RAND_MM * u)
    voor = _straal(bvh, start, k)
    if voor is None:
        return None
    p_voor = start + k * voor
    achter = _straal(bvh, p_voor + k * (0.01 * u), k)
    if achter is None:
        return None
    return p_voor + k * ((achter + 0.01 * u) / 2.0)


def lid_uit_vorm(bvh, punt, kijk):
    """(lidas, smalste richting) in het vlak loodrecht op de kijkrichting, of None als stralen missen."""
    k = kijk.normalized()
    e1, e2 = _basis(k)
    beste = None
    for i in range(STAPPEN):
        a = math.pi * i / STAPPEN
        d = (e1 * math.cos(a) + e2 * math.sin(a)).normalized()
        b = _breedte(bvh, punt, d)
        if b is not None and (beste is None or b[0] < beste[0]):
            beste = (b[0], d)
    if beste is None:
        return None
    return k.cross(beste[1]).normalized(), beste[1]


def naar_midden(bvh, punt, lid, kijk, u):
    """Punt naar het midden van de doorsnede loodrecht op lid: langs de kijkrichting (op het lid geprojecteerd),
    dan dwars daarop in het snijvlak. Geeft het oude punt terug als een straal mist."""
    l = lid.normalized()
    h = kijk - l * kijk.dot(l)
    if h.length < 1e-6:
        return punt
    h.normalize()
    p = diepte_midden(bvh, punt, h, u)
    if p is None:
        return punt
    dwars = l.cross(h).normalized()
    for _ in range(2):
        b = _breedte(bvh, p, dwars)
        if b is None:
            break
        p = p + dwars * b[1]
        b = _breedte(bvh, p, h)
        if b is None:
            break
        p = p + h * b[1]
    return p


def bijstellen(bvh, punt, lid, kijk, u):
    """(punt, lid, wat) na Shift + rechtsklik. wat: lege tekst als er niets veranderde, anders een korte uitleg
    voor de melding. kijk None (as-bron Cursor of geen 3D-weergave): niets aanpassen."""
    if kijk is None:
        return punt, lid, ""
    punt, lid, kijk = Vector(punt), Vector(lid).normalized(), Vector(kijk).normalized()
    if not op_huid(bvh, punt, u):
        return punt, lid, ""
    wat = []
    if langs_kijk(lid, kijk):
        start = diepte_midden(bvh, punt, kijk, u)
        if start is None:
            return punt, lid, ""
        uit = lid_uit_vorm(bvh, start, kijk)
        if uit is None:
            return punt, lid, ""
        lid = uit[0]
        wat.append("limb axis from the mesh")
    nieuw = naar_midden(bvh, punt, lid, kijk, u)
    if (nieuw - punt).length > 1e-9:
        punt = nieuw
        wat.append("centred in the limb")
    return punt, lid, " and ".join(wat)


ROND = 1.5  # breedste / smalste doorsnede in het schermvlak onder dit getal: je kijkt langs het lid


def kogel_bijstellen(bvh, punt, kijk, u, centrum=None):
    """Issue 410 (kopersreis Iris 28 nov): (punt, as, wat) voor een kogel met as-bron View direction na Shift + rechtsklik.

    Shift + rechtsklik zet de cursor op de huid. De kogelpresets (Shoulder, Hip, Neck) zeiden daar "Too thin" op een
    arm van 36 mm. Erger: met de cursor midden in de arm en een vooraanzicht liep de as van de kogel langs de
    kijkrichting, dus dwars door de arm, en sneed hij het hele figuur in een voor- en achterhelft (GEZIEN, delen
    238 x 65 x 238 en 238 x 49 x 238 mm, toch Good fit). Een kogel hoort dwars op het lid te staan.
    Daarom, alleen als het punt op de huid ligt:
    1. naar het midden tussen voorkant en achterkant langs de kijkrichting;
    2. ligt het lid in het schermvlak (breedste doorsnede minstens ROND keer de smalste), dan wordt de as de lidas
       uit het figuur, gericht van centrum (midden van het figuur) naar het punt, zodat deel B het lid is (arm, been,
       hoofd) en de kogel aan de kant van het lijf zit; anders (je kijkt langs het lid) blijft de kijkrichting;
    3. dwars op het lid naar het midden van de doorsnede.
    Een cursor binnen het figuur blijft precies zoals hij was. wat: lege tekst als er niets veranderde."""
    if kijk is None:
        return punt, kijk, ""
    punt, kijk = Vector(punt), Vector(kijk).normalized()
    if not op_huid(bvh, punt, u):
        return punt, kijk, ""
    start = diepte_midden(bvh, punt, kijk, u)
    if start is None:
        return punt, kijk, ""
    e1, e2 = _basis(kijk)
    breedtes = []
    for i in range(STAPPEN):
        a = math.pi * i / STAPPEN
        d = (e1 * math.cos(a) + e2 * math.sin(a)).normalized()
        b = _breedte(bvh, start, d)
        if b is not None:
            breedtes.append((b[0], d))
    if not breedtes:
        return punt, kijk, ""
    smal, breed = min(breedtes, key=lambda b: b[0]), max(breedtes, key=lambda b: b[0])
    wat = []
    if breed[0] >= ROND * smal[0]:
        lid = kijk.cross(smal[1]).normalized()
        if centrum is not None and lid.dot(start - Vector(centrum)) < 0:
            lid = -lid
        nieuw = naar_midden(bvh, punt, lid, kijk, u)
        wat.append("joint axis along the limb")
        as_ = lid
    else:
        nieuw = start
        for d in (e1, e2):
            b = _breedte(bvh, nieuw, d)
            if b is not None:
                nieuw = nieuw + d * b[1]
        as_ = kijk
    if (nieuw - punt).length > 1e-9:
        punt = nieuw
        wat.append("centred in the limb")
    return punt, as_, " and ".join(wat)
