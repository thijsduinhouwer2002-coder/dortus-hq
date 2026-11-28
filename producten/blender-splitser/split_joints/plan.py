"""Cut plan: where to cut so every piece fits on the bed, with as few pieces as possible.

Works on the mesh in mm (numpy, no bpy), so the test can check it without Blender.
Cuts are planes along the world axes. A plan with nx, ny, nz slabs gives a grid of cells; a cell
fits if its size (clipped to the model's bounding box) fits the bed in some 90 degree orientation.
Among all grids that fit we take the one with the fewest cells that hold part of the model.

A cell holds part of the model if the surface passes through it (points sampled on every triangle,
closer together than the smallest possible cell) or if its middle lies inside the model (a cell deep
inside a solid block has no surface). Counting only the vertices was wrong for models with big flat
faces: a box of 8 vertices gave 2 pieces instead of 3 (keuring 23 nov, A8).
MAX_CELLEN stops a plan that would make thousands of pieces (a model in mm in a scene in meters)."""
import itertools
import math

import numpy as np

from . import doorsnede
from .printers import past

MAX_PUNTEN = 400_000
MAX_CELLEN = 200


def _uitdunnen(p):
    if len(p) > MAX_PUNTEN:
        p = p[np.linspace(0, len(p) - 1, MAX_PUNTEN).astype(np.int64)]
    return p


def oppervlak_punten(punten, driehoeken, stap):
    """Points on the surface: every vertex, plus a barycentric grid on each triangle whose longest edge
    is longer than stap (mm), so no part of the surface is farther than stap from a point."""
    v = np.asarray(punten, dtype=np.float64).reshape(-1, 3)
    f = np.asarray(driehoeken, dtype=np.int64).reshape(-1, 3)
    if len(f) == 0:
        return v
    a, b, c = v[f[:, 0]], v[f[:, 1]], v[f[:, 2]]
    rand = np.max(np.stack([np.linalg.norm(b - a, axis=1), np.linalg.norm(c - b, axis=1),
                            np.linalg.norm(a - c, axis=1)]), axis=0)
    k = np.minimum(np.ceil(rand / stap).astype(np.int64), 400)
    lijst = [v]
    for kk in np.unique(k[k > 1]):
        kk = int(kk)
        sel = k == kk
        i, j = np.meshgrid(np.arange(kk + 1), np.arange(kk + 1))
        m = (i + j) <= kk
        wi, wj = i[m] / kk, j[m] / kk
        wk = 1.0 - wi - wj
        pa, pb, pc = a[sel], b[sel], c[sel]
        pts = pa[:, None, :] * wk[None, :, None] + pb[:, None, :] * wi[None, :, None] + pc[:, None, :] * wj[None, :, None]
        lijst.append(pts.reshape(-1, 3))
    return np.concatenate(lijst)


def binnen(punten, driehoeken, pts):
    """True per point (K x 3, mm) if it lies inside the closed mesh (cross-section in the plane z = point z)."""
    uit = np.zeros(len(pts), dtype=bool)
    for z in np.unique(pts[:, 2]):
        sel = np.nonzero(pts[:, 2] == z)[0]
        s = doorsnede.snijlijnen(punten, driehoeken, 2, float(z) + 1e-7)
        if len(s) == 0:
            continue
        u0, v0, u1, v1 = s[:, 0, 0], s[:, 0, 1], s[:, 1, 0], s[:, 1, 1]
        for i in sel:
            x, y = pts[i, 0], pts[i, 1]
            m = (np.minimum(v0, v1) <= y) & (y < np.maximum(v0, v1))
            if not m.any():
                continue
            t = (y - v0[m]) / (v1[m] - v0[m])
            uit[i] = int(np.count_nonzero(u0[m] + (u1[m] - u0[m]) * t > x)) % 2 == 1
    return uit


def bezette_cellen(p, grenzen, punten=None, driehoeken=None, lo=None, hi=None):
    """Number of grid cells with part of the model: a surface point inside, or (with the triangles) the
    middle of the cell inside the mesh. grenzen: per axis the sorted cut positions."""
    idx = np.stack([np.searchsorted(np.asarray(g, dtype=np.float64), p[:, i]) for i, g in enumerate(grenzen)], axis=1)
    bezet = {tuple(int(x) for x in r) for r in np.unique(idx, axis=0)}
    if driehoeken is not None and lo is not None:
        rand = [[lo[a]] + list(grenzen[a]) + [hi[a]] for a in range(3)]
        leeg = [ijk for ijk in itertools.product(*[range(len(r) - 1) for r in rand]) if ijk not in bezet]
        if leeg:
            mid = np.array([[(rand[a][ijk[a]] + rand[a][ijk[a] + 1]) / 2.0 for a in range(3)] for ijk in leeg])
            bezet |= {ijk for ijk, ja in zip(leeg, binnen(punten, driehoeken, mid)) if ja}
    return len(bezet)


def roosters(n_min, n_max):
    """Every (nx, ny, nz) between n_min and n_max with at most MAX_CELLEN cells, without walking past it."""
    for nx in range(n_min[0], n_max[0] + 1):
        if nx * n_min[1] * n_min[2] > MAX_CELLEN:
            break
        for ny in range(n_min[1], n_max[1] + 1):
            if nx * ny * n_min[2] > MAX_CELLEN:
                break
            for nz in range(n_min[2], n_max[2] + 1):
                if nx * ny * nz > MAX_CELLEN:
                    break
                yield (nx, ny, nz)


def te_veel_tekst(naam, maat, bed, minimaal):
    """(message, panel lines) when a model needs more than MAX_CELLEN pieces (kopersreis #385: the default
    cube of 2 m said only "No plan", without its size or a way out). maat and bed in mm (x, y, z)."""
    keer = max(maat) / max(bed)
    afm = " x ".join(f"{m:,.0f}" for m in maat)
    bedtekst = " x ".join(f"{b:,.0f}" for b in bed)
    melding = (f"{naam} is {afm} mm, about {keer:.0f} times as long as your bed ({bedtekst} mm): that needs at least "
               f"{minimaal:,} pieces (limit {MAX_CELLEN}). Scale it down (S) or pick a bigger printer")
    # short lines: the sidebar cut "Scale it down (S) or pick a bigger p..." off at its default width (GEZIEN)
    paneel = [f"Too big: {afm} mm", f"About {keer:.0f} times your bed", "Scale it down (S)", "or pick a bigger printer"]
    return melding, paneel


def maat_tekst(mm):
    """A size in mm as a maker reads it (kopersreis #386: "3.985e+05 mm" was unreadable).
    398500 -> "398,500 mm (about 400 m)", 120 -> "120 mm", 0.3985 -> "0.4 mm"."""
    if mm >= 1000.0:
        meter = float(f"{mm / 1000.0:.2g}")
        return f"{mm:,.0f} mm (about {meter:,.0f} m)" if meter >= 10 else f"{mm:,.0f} mm (about {meter:g} m)"
    if mm >= 10.0:
        return f"{mm:,.0f} mm"
    if mm <= 0:
        return "0 mm"
    decimalen = max(1, 1 - math.floor(math.log10(mm)))  # two digits that mean something, never e-05
    return f"{mm:.{decimalen}f}".rstrip("0").rstrip(".") + " mm"


_EENHEID = {0.001: "mm", 0.01: "cm", 1.0: "meter"}


def eenheid_tekst(naam, mm, nu, keuze):
    """Message when the unit of the scene is wrong (#386). mm: largest size now; nu: unit scale of the scene
    (1.0 = meters); keuze: unit scale that gives a printable size, or None. The button is named as in the panel."""
    if keuze is None:
        return f"{naam} is {maat_tekst(mm)}: no unit (mm, cm or m) makes that printable. Scale it yourself (S)"
    keer = nu / keuze
    hoe = f"{keer:,.0f} times too big" if keer > 1 else f"{1 / keer:,.0f} times too small"
    van, in_ = _EENHEID.get(keuze), _EENHEID.get(nu)
    waarom = f": a {van} model in a {in_} scene" if van and in_ else ""
    return (f"{naam} is {maat_tekst(mm)}, it looks {hoe}{waarom}. "
            "Open More settings and press Convert to mm, then Split to fit again")


def maak(punten, bed, driehoeken=None):
    """Plan for a mesh (points N x 3 and triangles M x 3, mm) and a bed (x, y, z, mm, margin taken off).

    Returns a dict with n (slabs per axis), snedes (list of (axis, position mm)), stukken (cells with
    part of the model) and cel (largest cell size in mm); or a dict with "fout": "te_veel" and
    "minimaal" (more than MAX_CELLEN pieces needed); or None if the model has no points.
    Without triangles only the points count (only for a point cloud)."""
    v = np.asarray(punten, dtype=np.float64).reshape(-1, 3)
    if len(v) == 0:
        return None
    lo, hi = v.min(axis=0), v.max(axis=0)
    lengte = np.maximum(hi - lo, 1e-6)
    groot, klein = max(bed), min(bed)
    n_min = [max(1, math.ceil(lengte[i] / groot - 1e-9)) for i in range(3)]
    n_max = [max(1, math.ceil(lengte[i] / klein - 1e-9)) for i in range(3)]
    minimaal = n_min[0] * n_min[1] * n_min[2]
    fout = {"fout": "te_veel", "minimaal": int(minimaal), "lo": tuple(lo), "hi": tuple(hi)}
    if minimaal > MAX_CELLEN:
        return fout
    p = _uitdunnen(oppervlak_punten(v, driehoeken, klein / 8.0) if driehoeken is not None else v)
    beste = None
    for n in roosters(n_min, n_max):
        cel = lengte / np.array(n, dtype=np.float64)
        if not past(cel, bed):
            continue
        grenzen = [[lo[i] + lengte[i] * k / n[i] for k in range(1, n[i])] for i in range(3)]
        stukken = bezette_cellen(p, grenzen, v, driehoeken, lo, hi)
        naad = sum((n[i] - 1) * lengte[(i + 1) % 3] * lengte[(i + 2) % 3] for i in range(3))
        sleutel = (stukken, naad, -n[2])  # fewest pieces, then the least cut area, then horizontal cuts
        if beste is None or sleutel < beste[0]:
            beste = (sleutel, n, grenzen, cel)
    if beste is None:
        return fout
    (stukken, _naad, _z), n, grenzen, cel = beste
    snedes = [(i, float(pos)) for i in range(3) for pos in grenzen[i]]
    return {"n": tuple(int(x) for x in n), "snedes": snedes, "stukken": int(stukken),
            "cel": tuple(float(x) for x in cel), "lo": tuple(float(x) for x in lo), "hi": tuple(float(x) for x in hi)}


def aantal_cellen(lo, hi, snedes):
    """Number of grid cells for these cuts, without making them (cheap: for the panel and the brake)."""
    n = 1
    for a in range(3):
        n *= 1 + sum(1 for as_, pos in snedes if as_ == a and lo[a] < pos < hi[a])
    return n


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
