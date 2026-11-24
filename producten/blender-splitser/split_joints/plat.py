"""Lay parts flat (1.0.1): which face of a piece goes down on the print bed (numpy, no bpy).

A cut face is always truly flat, so it is the best side to print on: no supports under it and the most
contact with the bed. We group the faces of a piece by their plane (normal and distance from the origin)
and pick the plane with the largest total area. On a piece of a split model that is almost always a cut
face; on a piece with a big flat bottom of its own (a box) that bottom can win, which is just as good.
Pin holes and engraved numbers sit in the cut face, so the rest of that face still counts as one plane."""
import numpy as np

HOEK = 1e-3  # normals closer than this (about 0.06 degrees) count as the same direction
AFSTAND_MM = 0.02  # planes closer than this count as the same plane
BUITEN_MM = 0.05  # a face down must be the lowest point of the piece, within this


def grootste_vlak(normalen, punten, oppervlak):
    """normalen (n, 3) unit normals, punten (n, 3) one point per face in mm, oppervlak (n,) in mm2.
    Returns (normal (3,), area in mm2, distance d in mm with n . p = d) of the flat plane with the largest
    total area, or (None, 0.0, 0.0)."""
    nrm = np.asarray(normalen, dtype=np.float64).reshape(-1, 3)
    pts = np.asarray(punten, dtype=np.float64).reshape(-1, 3)
    opp = np.asarray(oppervlak, dtype=np.float64).reshape(-1)
    lengte = np.linalg.norm(nrm, axis=1)
    goed = (lengte > 1e-9) & (opp > 0.0)  # any length: a scaled piece gives normals shorter or longer than 1
    if not goed.any():
        return None, 0.0, 0.0
    nrm = nrm[goed] / lengte[goed, None]
    pts, opp = pts[goed], opp[goed]
    afstand = np.einsum("ij,ij->i", nrm, pts)
    sleutel = np.column_stack([np.round(nrm / HOEK), np.round(afstand / AFSTAND_MM)]).astype(np.int64)
    _, groep = np.unique(sleutel, axis=0, return_inverse=True)
    groep = groep.reshape(-1)
    som = np.bincount(groep, weights=opp)
    beste = int(np.argmax(som))
    lid = groep == beste
    n = (nrm[lid] * opp[lid, None]).sum(axis=0)
    d = float(np.average(afstand[lid], weights=opp[lid]))
    return n / np.linalg.norm(n), float(som[beste]), d


def draai_naar_beneden(n):
    """3 x 3 rotation matrix that turns unit vector n to (0, 0, -1) along the shortest way."""
    n = np.asarray(n, dtype=np.float64)
    n = n / np.linalg.norm(n)
    doel = np.array([0.0, 0.0, -1.0])
    c = float(np.dot(n, doel))
    if c > 1.0 - 1e-12:
        return np.eye(3)
    if c < -1.0 + 1e-12:  # facing straight up: half a turn around x
        return np.diag([1.0, -1.0, -1.0])
    v = np.cross(n, doel)
    k = np.array([[0.0, -v[2], v[1]], [v[2], 0.0, -v[0]], [-v[1], v[0], 0.0]])
    return np.eye(3) + k + k @ k / (1.0 + c)


def vlakken(normalen, punten, oppervlak, n_max=5):
    """Up to n_max flat planes, largest total area first: list of (normal (3,), area in mm2, d in mm)."""
    nrm = np.asarray(normalen, dtype=np.float64).reshape(-1, 3)
    pts = np.asarray(punten, dtype=np.float64).reshape(-1, 3)
    opp = np.asarray(oppervlak, dtype=np.float64).reshape(-1)
    uit = []
    over = np.ones(len(opp), dtype=bool)
    while len(uit) < n_max and over.any():
        n, a, d = grootste_vlak(nrm[over], pts[over], opp[over])
        if n is None:
            break
        uit.append((n, a, d))
        weg = (np.einsum("ij,j->i", nrm, n) > 1.0 - 4 * HOEK * HOEK) & over
        over &= ~weg
    return uit


def _draai_z(graden):
    a = np.radians(graden)
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


SNIJ_MM = 0.1  # a plane counts as a cut face if a pin hole or a number of that cut lies in it, within this


def is_snijvlak(n, d, snij):
    """True if plane n . p = d holds a pin hole or a number (snij: list of (point mm, axis)) of a cut."""
    for p, a in snij:
        if abs(float(np.dot(n, a))) > 0.999 and abs(float(np.dot(n, p)) - d) < SNIJ_MM:
            return True
    return False


def kies_stand(normalen, punten, oppervlak, hoeken, bed, snij=(), alleen_snijvlak=True):
    """Which way a piece lies on the bed. hoeken (m, 3) vertices in mm, bed (x, y, z) usable size in mm.
    Tries the largest flat planes in turn (each turned face down) and turns around z in steps of 5 degrees
    so the footprint fits the bed. A plane only counts if nothing of the piece sticks out past it.
    alleen_snijvlak (the add-on always): only cut faces (snij: points and axes of the pin holes and numbers,
    see is_snijvlak) may go down. A flat side of the model itself does not: on a thin curved shell (the low
    poly vase) a facet down leaves the curve hanging over, while its own way up prints without supports.
    Returns (rotation 3 x 3, area of the face down in mm2, rank of that plane from 0, True if it is a cut
    face) or (None, 0.0, -1, False) if no allowed plane down fits: then the piece keeps its own way up."""
    alle = np.asarray(hoeken, dtype=np.float64).reshape(-1, 3)  # all points: one sticking out never misses the bed
    bx, by, bz = (float(b) + 1e-6 for b in bed)
    snij = [(np.asarray(p, dtype=np.float64), np.asarray(a, dtype=np.float64) / np.linalg.norm(a)) for p, a in snij]
    kandidaten = vlakken(normalen, punten, oppervlak, n_max=12)
    kandidaten = [(n, a, d, is_snijvlak(n, d, snij)) for n, a, d in kandidaten]
    if alleen_snijvlak:
        kandidaten = [k for k in kandidaten if k[3]]
    kandidaten.sort(key=lambda k: not k[3])  # stable: cut faces first, by area within each group
    for rang, (n, a, d, snijvlak) in enumerate(kandidaten):
        if float(np.max(alle @ n)) > d + BUITEN_MM:  # part of the piece sticks out past this plane: not a bottom
            continue
        if float(np.ptp(alle @ n)) > bz:
            continue
        r = draai_naar_beneden(n)
        w = alle @ r.T
        beste = None
        for graden in range(0, 90, 5):
            rz = _draai_z(graden)
            xy = w[:, :2] @ rz[:2, :2].T
            dx, dy = np.ptp(xy[:, 0]), np.ptp(xy[:, 1])
            if (dx <= bx and dy <= by) or (dx <= by and dy <= bx):
                if beste is None or dx * dy < beste[0] - 1e-9:
                    beste = (dx * dy, rz)
        if beste is not None:
            return beste[1] @ r, a, rang, snijvlak
    return None, 0.0, -1, False
