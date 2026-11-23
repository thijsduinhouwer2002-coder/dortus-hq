"""Cross-section of a closed mesh with an axis plane, as a grid (numpy, no bpy).

snijlijnen: the line segments where the triangles cross the plane, in 2D (u, v) = the two other axes.
raster: which grid points lie inside the cross-section (even-odd rule along +u).
klaring: per inside point the distance to the nearest point outside (the edge of the cut face).
eilanden: separate pieces of the cut face (4-connected), each gets its own pins and label."""
from collections import deque

import numpy as np

STUK = 4096  # rows of points per distance chunk


def assen(as_):
    """The two axes in the plane, in the order (u, v), so u x v points along +as_."""
    return (as_ + 1) % 3, (as_ + 2) % 3


def snijlijnen(punten, driehoeken, as_, pos):
    """Segments (K x 2 x 2) where the triangles cross the plane coordinate[as_] == pos."""
    v = np.asarray(punten, dtype=np.float64)
    f = np.asarray(driehoeken, dtype=np.int64).reshape(-1, 3)
    if len(f) == 0:
        return np.zeros((0, 2, 2))
    d = v[f, as_] - pos  # (M, 3)
    d = np.where(np.abs(d) < 1e-9, 1e-9, d)  # a point on the plane counts as just above it
    boven = d > 0
    n = boven.sum(axis=1)
    kruis = (n == 1) | (n == 2)
    f, d, boven = f[kruis], d[kruis], boven[kruis]
    if len(f) == 0:
        return np.zeros((0, 2, 2))
    # the odd vertex out: the one alone on its side
    alleen = np.where((boven.sum(axis=1) == 1)[:, None], boven, ~boven)
    k = np.argmax(alleen, axis=1)
    rij = np.arange(len(f))
    a = f[rij, k]
    b = f[rij, (k + 1) % 3]
    c = f[rij, (k + 2) % 3]
    da, db, dc = d[rij, k], d[rij, (k + 1) % 3], d[rij, (k + 2) % 3]
    u, w = assen(as_)
    pa, pb, pc = v[a][:, [u, w]], v[b][:, [u, w]], v[c][:, [u, w]]
    t1 = (da / (da - db))[:, None]
    t2 = (da / (da - dc))[:, None]
    p1 = pa + (pb - pa) * t1
    p2 = pa + (pc - pa) * t2
    return np.stack([p1, p2], axis=1)


def raster(segmenten, rect, h):
    """Grid over rect (umin, vmin, umax, vmax) with step h. Returns (us, vs, binnen[nv, nu])."""
    umin, vmin, umax, vmax = rect
    nu = max(1, int(np.floor((umax - umin) / h)))
    nv = max(1, int(np.floor((vmax - vmin) / h)))
    us = umin + (np.arange(nu) + 0.5) * (umax - umin) / nu
    vs = vmin + (np.arange(nv) + 0.5) * (vmax - vmin) / nv
    binnen = np.zeros((nv, nu), dtype=bool)
    if len(segmenten) == 0:
        return us, vs, binnen
    s = np.asarray(segmenten)
    u0, v0, u1, v1 = s[:, 0, 0], s[:, 0, 1], s[:, 1, 0], s[:, 1, 1]
    vlo, vhi = np.minimum(v0, v1), np.maximum(v0, v1)
    for j, vv in enumerate(vs):
        m = (vlo <= vv) & (vv < vhi)
        if not m.any():
            continue
        t = (vv - v0[m]) / (v1[m] - v0[m])
        uk = np.sort(u0[m] + (u1[m] - u0[m]) * t)
        rechts = len(uk) - np.searchsorted(uk, us, side="right")
        binnen[j] = (rechts % 2) == 1
    return us, vs, binnen


def klaring(us, vs, binnen):
    """Distance (mm) from each inside grid point to the nearest outside grid point, minus half a step.
    Outside the grid counts as outside. 0 for points outside."""
    nv, nu = binnen.shape
    hu = (us[1] - us[0]) if nu > 1 else 1.0
    hv = (vs[1] - vs[0]) if nv > 1 else 1.0
    pad = np.zeros((nv + 2, nu + 2), dtype=bool)
    pad[1:-1, 1:-1] = binnen
    buur = np.zeros_like(pad)
    buur[1:, :] |= pad[:-1, :]
    buur[:-1, :] |= pad[1:, :]
    buur[:, 1:] |= pad[:, :-1]
    buur[:, :-1] |= pad[:, 1:]
    rand = buur & ~pad  # outside points next to an inside point
    ri, rj = np.nonzero(rand)
    uit = np.zeros((nv, nu))
    bi, bj = np.nonzero(binnen)
    if len(bi) == 0 or len(ri) == 0:
        return uit
    ru = us[0] + (rj - 1) * hu
    rv = vs[0] + (ri - 1) * hv
    pu, pv = us[bj], vs[bi]
    beste = np.empty(len(bi))
    for s in range(0, len(bi), STUK):
        du = pu[s:s + STUK, None] - ru[None, :]
        dv = pv[s:s + STUK, None] - rv[None, :]
        beste[s:s + STUK] = np.sqrt((du * du + dv * dv).min(axis=1))
    uit[bi, bj] = np.maximum(beste - 0.5 * max(hu, hv), 0.0)
    return uit


def eilanden(binnen):
    """Label (nv, nu) int array: 0 outside, 1..n per separate piece of the cut face. Returns (labels, n)."""
    nv, nu = binnen.shape
    lab = np.zeros((nv, nu), dtype=np.int32)
    n = 0
    for i0, j0 in zip(*np.nonzero(binnen)):
        if lab[i0, j0]:
            continue
        n += 1
        lab[i0, j0] = n
        rij = deque([(i0, j0)])
        while rij:
            i, j = rij.popleft()
            for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= a < nv and 0 <= b < nu and binnen[a, b] and not lab[a, b]:
                    lab[a, b] = n
                    rij.append((a, b))
    return lab, n
