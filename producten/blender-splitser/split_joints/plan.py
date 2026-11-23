"""Cut plan: where to cut so every piece fits on the bed, with as few pieces as possible.

Works on a point cloud in mm (numpy, no bpy), so the test can check it without Blender.
Cuts are planes along the world axes. A plan with nx, ny, nz slabs gives a grid of cells; a cell
fits if its size (clipped to the model's bounding box) fits the bed in some 90 degree orientation.
Among all grids that fit we take the one with the fewest cells that hold part of the model."""
import itertools
import math

import numpy as np

from .printers import past

MAX_PUNTEN = 200_000


def _punten(punten):
    p = np.asarray(punten, dtype=np.float64).reshape(-1, 3)
    if len(p) > MAX_PUNTEN:
        p = p[np.linspace(0, len(p) - 1, MAX_PUNTEN).astype(np.int64)]
    return p


def bezette_cellen(p, grenzen):
    """Number of grid cells that hold at least one point. grenzen: per axis the sorted cut positions."""
    idx = np.stack([np.searchsorted(np.asarray(g, dtype=np.float64), p[:, i]) for i, g in enumerate(grenzen)], axis=1)
    return len(np.unique(idx, axis=0))


def maak(punten, bed):
    """Plan for a point cloud (N x 3, mm) and a bed (x, y, z, mm, margin already taken off).

    Returns a dict with n (slabs per axis), snedes (list of (axis, position mm)), stukken (cells with
    part of the model), cel (largest cell size in mm) or None if the model has no points."""
    p = _punten(punten)
    if len(p) == 0:
        return None
    lo, hi = p.min(axis=0), p.max(axis=0)
    lengte = np.maximum(hi - lo, 1e-6)
    groot, klein = max(bed), min(bed)
    bereik = [range(max(1, math.ceil(lengte[i] / groot - 1e-9)), max(1, math.ceil(lengte[i] / klein - 1e-9)) + 1)
              for i in range(3)]
    beste = None
    for n in itertools.product(*bereik):
        cel = lengte / np.array(n, dtype=np.float64)
        if not past(cel, bed):
            continue
        grenzen = [[lo[i] + lengte[i] * k / n[i] for k in range(1, n[i])] for i in range(3)]
        stukken = bezette_cellen(p, grenzen)
        naad = sum((n[i] - 1) * lengte[(i + 1) % 3] * lengte[(i + 2) % 3] for i in range(3))
        sleutel = (stukken, naad, -n[2])  # fewest pieces, then the least cut area, then horizontal cuts
        if beste is None or sleutel < beste[0]:
            beste = (sleutel, n, grenzen, cel)
    if beste is None:
        return None
    (stukken, _naad, _z), n, grenzen, cel = beste
    snedes = [(i, float(pos)) for i in range(3) for pos in grenzen[i]]
    return {"n": tuple(int(v) for v in n), "snedes": snedes, "stukken": int(stukken),
            "cel": tuple(float(v) for v in cel), "lo": tuple(float(v) for v in lo), "hi": tuple(float(v) for v in hi)}


def cellen(lo, hi, snedes):
    """All grid cells for the given cuts: list of ((i, j, k), (min xyz), (max xyz)) in mm, clipped to lo..hi."""
    grenzen = []
    for a in range(3):
        g = sorted(pos for as_, pos in snedes if as_ == a and lo[a] < pos < hi[a])
        grenzen.append([lo[a]] + g + [hi[a]])
    uit = []
    for ijk in itertools.product(*[range(len(g) - 1) for g in grenzen]):
        mn = tuple(grenzen[a][ijk[a]] for a in range(3))
        mx = tuple(grenzen[a][ijk[a] + 1] for a in range(3))
        uit.append((ijk, mn, mx))
    return uit, grenzen

