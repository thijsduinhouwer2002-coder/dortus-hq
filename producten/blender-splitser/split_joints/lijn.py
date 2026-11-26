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
