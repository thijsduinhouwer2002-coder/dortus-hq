"""Draw cut: the free cut plane from a line drawn on the screen. Pure numpy, tested in e2e/test_logica.py."""
import numpy as np


def vlak_uit_lijn(p1, p2, kijk, punten, marge=1.0):
    """Free cut plane from a line drawn on the screen (issue #208, lesson Bool Tool in the lat).
    p1, p2: the ends of the line in 3D, kijk: the view direction, punten: N x 3 points of the piece, all in the
    same space and unit; marge: extra room around the rectangle in that unit.
    The plane holds the line and the view direction. Local X runs along the line (half width a = half the line
    plus marge), local Y along the view (the whole depth of the piece plus marge), local Z is the arrow: it
    points to the side whose part of the piece lies most inside the rectangle, the part that comes off (an arm
    end lies fully inside, the body around it does not); if both lie fully inside, the side that reaches less
    far from the plane. Returns (R 3x3 with columns X Y Z, origin, a, b) or None
    when the line is too short or runs along the view."""
    p1, p2 = np.asarray(p1, dtype=float), np.asarray(p2, dtype=float)
    k = np.asarray(kijk, dtype=float)
    if np.linalg.norm(k) < 1e-12:
        return None
    k = k / np.linalg.norm(k)
    t = (p2 - p1) - k * float(np.dot(p2 - p1, k))
    lengte = float(np.linalg.norm(t))
    if lengte < 1e-9:
        return None
    e1 = t / lengte
    e2 = k
    n = np.cross(e1, e2)
    o = (p1 + p2) / 2.0
    pts = np.asarray(punten, dtype=float).reshape(-1, 3)
    lok = (pts - o) @ np.column_stack((e1, e2, n))
    y0, y1 = float(lok[:, 1].min()), float(lok[:, 1].max())
    o = o + e2 * (y0 + y1) / 2.0
    lok[:, 1] -= (y0 + y1) / 2.0
    a = lengte / 2.0 + marge
    b = (y1 - y0) / 2.0 + marge
    binnen = (np.abs(lok[:, 0]) <= a) & (np.abs(lok[:, 1]) <= b)

    def deel_binnen(kant):
        op = kant * lok[:, 2] > 0
        if not op.any():
            return (0.0, 0.0)
        return (round(float(binnen[op].mean()), 6), -float(np.abs(lok[op, 2]).max()))

    if deel_binnen(-1) > deel_binnen(1):
        e1, n = -e1, -n  # turn around Y: the arrow flips, the frame stays right-handed
    return np.column_stack((e1, e2, n)), o, a, b


def deel_eraf(punten, tri, R, o, a, b):
    """Which triangles of the piece come off with the free cut (keuring #212 M1: light them up before Cut piece).
    punten N x 3, tri M x 3 indices, (R, o, a, b) the frame of the cut in the same space and unit as punten.
    A triangle comes off when its middle lies on the arrow side (local Z > 0) and inside the rectangle, the same
    rule as the box the cut makes. Returns a bool array of length M."""
    pts = np.asarray(punten, dtype=float).reshape(-1, 3)
    tri = np.asarray(tri, dtype=np.int64).reshape(-1, 3)
    if len(tri) == 0:
        return np.zeros(0, dtype=bool)
    mid = pts[tri].mean(axis=1)
    lok = (mid - np.asarray(o, dtype=float)) @ np.asarray(R, dtype=float)
    return (lok[:, 2] > 0) & (np.abs(lok[:, 0]) <= a) & (np.abs(lok[:, 1]) <= b)


def omdraaien(R):
    """The frame turned half a turn around its local Y (Flip side): the arrow and X flip, Y stays, still
    right-handed. The rectangle stays where it is."""
    R = np.asarray(R, dtype=float)
    return np.column_stack((-R[:, 0], R[:, 1], -R[:, 2]))


def eraf_hoeken(punten, tri, R, o, a, b, mee=None):
    """Corners (K x 3 x 3) of the part that comes off, cut clean at the plane: triangles that cross the plane
    are clipped to the arrow side, so the light ends on the cut line and not in slivers past it.
    mee: optional N x 3 points that get the same clipping (the lifted points that are drawn); default punten."""
    pts = np.asarray(punten, dtype=float).reshape(-1, 3)
    mee = pts if mee is None else np.asarray(mee, dtype=float).reshape(-1, 3)
    tri = np.asarray(tri, dtype=np.int64).reshape(-1, 3)
    if len(tri) == 0:
        return np.zeros((0, 3, 3))
    R = np.asarray(R, dtype=float)
    lok = (pts - np.asarray(o, dtype=float)) @ R
    z = lok[tri][:, :, 2]
    mid = lok[tri].mean(axis=1)
    hoek = mee[tri]
    in_rect = (np.abs(mid[:, 0]) <= a) & (np.abs(mid[:, 1]) <= b)
    heel = in_rect & (z > 0).all(axis=1)
    uit = [hoek[heel]]
    half = in_rect & (z > 0).any(axis=1) & ~(z > 0).all(axis=1)
    stukjes = []
    for h, zz in zip(hoek[half], z[half]):
        poly = []
        for i in range(3):  # Sutherland-Hodgman against z >= 0
            j = (i + 1) % 3
            if zz[i] >= 0:
                poly.append(h[i])
            if (zz[i] >= 0) != (zz[j] >= 0):
                t = zz[i] / (zz[i] - zz[j])
                poly.append(h[i] + (h[j] - h[i]) * t)
        for k in range(1, len(poly) - 1):
            stukjes.append((poly[0], poly[k], poly[k + 1]))
    if stukjes:
        uit.append(np.array(stukjes))
    return np.concatenate(uit, axis=0) if uit else np.zeros((0, 3, 3))
