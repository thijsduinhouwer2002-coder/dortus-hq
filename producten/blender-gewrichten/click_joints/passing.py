"""Passingcontrole met een BVH-tree: wanddikte rond de kom en uitsteken uit het figuur."""
import math

from mathutils import Vector

GRENS_ROOD_MM = 0.8    # dunner dan dit: te dun om te printen
GRENS_ORANJE_MM = 1.5  # dunner dan dit: krap
# Heldere kleuren van Daan (lineair, zoals Blender ze opslaat): groen #3DDC84, oranje #FFB020,
# rood #FF4D4D. Naast de kleur staat in het paneel altijd een icoon (kleurenblind).
KLEUREN = {"groen": (0.047, 0.716, 0.231, 1.0), "oranje": (1.0, 0.434, 0.014, 1.0),
           "rood": (1.0, 0.074, 0.074, 1.0)}
ICONEN = {"groen": "CHECKMARK", "oranje": "ERROR", "rood": "CANCEL"}


def richtingen(n):
    """n richtingen gelijk verdeeld over een bol (Fibonacci)."""
    uit = []
    gouden = math.pi * (3 - math.sqrt(5))
    for i in range(n):
        z = 1 - 2 * (i + 0.5) / n
        r = math.sqrt(1 - z * z)
        uit.append(Vector((r * math.cos(i * gouden), r * math.sin(i * gouden), z)))
    return uit


def ring(n=24):
    return [Vector((math.cos(2 * math.pi * i / n), math.sin(2 * math.pi * i / n), 0)) for i in range(n)]


def binnen(bvh, p):
    loc, nor, _, _ = bvh.find_nearest(p)
    return loc is not None and (p - loc).dot(nor) < 0


def monsters(maat, soort):
    """Lijst (oorsprong, richting, nodige afstand, opening) in het gewrichtsframe.
    Een monster met opening houdt ook rekening met het snijvlak (de bodem van deel B)."""
    lijst = []
    if soort == "KOGEL":
        c = Vector((0, 0, maat["midden_z"]))
        for d in richtingen(400):
            lijst.append((c, d, maat["r"] + maat["s"], maat["open_r"]))
        for d in ring():
            lijst.append((Vector((0, 0, maat["schuif"] * 2)), d, maat["open_r"], None))
    else:
        top = maat["top_z"]
        for i in range(6):
            o = Vector((0, 0, top * i / 5))
            for d in ring():
                lijst.append((o, d, maat["r"] + maat["s"], None))
        lijst.append((Vector((0, 0, top)), Vector((0, 0, 1)), maat["s"], None))
    return lijst


def bodem(maat):
    """Dikte van de rand van deel B tussen snijvlak en kom, net naast de klikopening."""
    rk = maat["r"] + maat["s"]
    return maat["midden_z"] - math.sqrt(max(rk * rk - maat["open_r"] ** 2, 0.0)) - maat["schuif"]


def beoordeel(bvh, frame, maat, soort, eenheid_per_mm):
    """Geeft (kleur, kleinste wand in mm, uitleg)."""
    rot = frame.to_3x3()
    for o in ((0, 0, maat["schuif"] * 2), (0, 0, maat["midden_z"])):
        if not binnen(bvh, frame @ Vector(o)):
            return "rood", -1.0, "het gewricht steekt uit het figuur"
    kleinste = bodem(maat) if soort == "KOGEL" else math.inf
    for o, d, nodig, opening in monsters(maat, soort):
        afstand = math.inf
        if opening is not None and d.z < 0:
            uit = o + d * nodig
            if math.hypot(uit.x, uit.y) < opening:
                continue  # deze straal gaat door de klikopening
            afstand = (o.z - maat["schuif"]) / -d.z  # tot het snijvlak: de bodem van deel B
        hit = bvh.ray_cast(frame @ o, (rot @ d).normalized())
        if hit[0] is None:
            return "rood", -1.0, "het gewricht steekt uit het figuur"
        kleinste = min(kleinste, min(hit[3], afstand) - nodig)
    wand = kleinste / eenheid_per_mm
    if wand < GRENS_ROOD_MM:
        return "rood", wand, f"wand {wand:.2f} mm is te dun (minstens {GRENS_ROOD_MM} mm)"
    if wand < GRENS_ORANJE_MM:
        return "oranje", wand, f"wand {wand:.2f} mm is krap"
    return "groen", wand, f"wand {wand:.2f} mm"


def meet_speling(deel_kogel, bvh_kom, centrum, r, as_richting, tol):
    """Afstanden van punten op de kogel naar het dichtstbijzijnde vlak van het komdeel."""
    afst = []
    for v in deel_kogel.data.vertices:
        p = deel_kogel.matrix_world @ v.co
        rel = p - centrum
        if abs(rel.length - r) < tol and rel.dot(as_richting) > -0.4 * r:
            hit = bvh_kom.find_nearest(p)
            if hit[0] is not None:
                afst.append(hit[3])
    return afst
