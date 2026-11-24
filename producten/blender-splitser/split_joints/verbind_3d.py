"""Pins and labels on every cut face, with the 3D checks (BVH of the model, in mm).

For each pair of neighboring cells we take the cross-section of the model on their shared plane
(doorsnede.py), let verbinders.py pick pin spots and a label spot, and check each pin in 3D here:
deep enough on both sides, enough wall around the whole hole, and not touching a hole of another face."""
import math

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

from . import doorsnede, verbinders

EXTRA_DIEPTE_MM = 0.3  # each hole is half a pin plus this much, so the pin always goes all the way in


def segment_afstand(p1, q1, p2, q2):
    """Shortest distance between segments p1-q1 and p2-q2 (mathutils Vectors)."""
    d1, d2, r = q1 - p1, q2 - p2, p1 - p2
    a, e, f = d1.dot(d1), d2.dot(d2), d2.dot(r)
    if a < 1e-12 and e < 1e-12:
        return (p1 - p2).length
    if a < 1e-12:
        s, t = 0.0, min(max(f / e, 0.0), 1.0)
    else:
        c = d1.dot(r)
        if e < 1e-12:
            t, s = 0.0, min(max(-c / a, 0.0), 1.0)
        else:
            b = d1.dot(d2)
            noemer = a * e - b * b
            s = min(max((b * f - c * e) / noemer, 0.0), 1.0) if noemer > 1e-12 else 0.0
            t = (b * s + f) / e
            if t < 0.0:
                t, s = 0.0, min(max(-c / a, 0.0), 1.0)
            elif t > 1.0:
                t, s = 1.0, min(max((b - c) / a, 0.0), 1.0)
    return ((p1 + d1 * s) - (p2 + d2 * t)).length


def as_vec(as_):
    v = Vector((0.0, 0.0, 0.0))
    v[as_] = 1.0
    return v


class Plaatser:
    def __init__(self, punten, driehoeken, opties):
        # tolist instead of a tuple per point: 5 s less on 1M polygons (speed test 24 nov)
        self.bvh = BVHTree.FromPolygons(np.asarray(punten).tolist(), np.asarray(driehoeken).tolist())
        self.opties = opties
        self.gaten = {}  # cell ijk -> list of (start, end, r) in mm, for the distance between holes

    def binnen_wand(self, q, wand):
        co, normaal, _i, afstand = self.bvh.find_nearest(q)
        if co is None:
            return False
        return (q - co).dot(normaal) < 0 and afstand >= wand

    def toets(self, punt, as_, r_gat, diepte, cellen):
        n = as_vec(as_)
        wand = self.opties["wand"]
        for teken in (1.0, -1.0):
            hit = self.bvh.ray_cast(punt, n * teken)
            if hit[0] is None or hit[3] < diepte + wand:
                return False
        e1 = as_vec((as_ + 1) % 3)
        e2 = as_vec((as_ + 2) % 3)
        marge = wand + 0.03  # a little more than asked: the check per piece afterwards measures the same points
        for z in np.concatenate([np.linspace(0.0, diepte, 6), -np.linspace(0.0, diepte, 6)[1:]]):
            for k in range(16):
                hoek = 2 * math.pi * k / 16
                q = punt + n * float(z) + (e1 * math.cos(hoek) + e2 * math.sin(hoek)) * r_gat
                if not self.binnen_wand(q, marge):
                    return False
        for teken in (1.0, -1.0):  # the bottom of each hole
            if not self.binnen_wand(punt + n * (teken * diepte), marge):
                return False
        a, b = punt - n * diepte, punt + n * diepte
        for ijk in cellen:
            for (p2, q2, r2) in self.gaten.get(ijk, ()):
                if segment_afstand(a, b, p2, q2) < r_gat + r2 + wand:
                    return False
        return True

    def voeg_toe(self, punt, as_, r_gat, diepte, cellen):
        n = as_vec(as_)
        for ijk in cellen:
            self.gaten.setdefault(ijk, []).append((punt - n * diepte, punt + n * diepte, r_gat))


def plan_alles(punten, driehoeken, cellen, nummers, grenzen, opties, label_aan):
    """cellen: ijk -> (mn, mx) mm. nummers: ijk -> piece number (only cells with a piece).
    Returns (gaten per ijk, labels per ijk, pennen [(d, count)], meldingen)."""
    pl = Plaatser(punten, driehoeken, opties)
    gaten, labels, meldingen, pennen = {}, {}, [], {}
    diepte = opties["pen_lengte"] / 2.0 + EXTRA_DIEPTE_MM
    for as_ in range(3):
        ua, va = doorsnede.assen(as_)
        for t in range(1, len(grenzen[as_]) - 1):
            c = grenzen[as_][t]
            segs = doorsnede.snijlijnen(punten, driehoeken, as_, c)
            if len(segs) == 0:
                continue
            smin, smax = segs.reshape(-1, 2).min(axis=0), segs.reshape(-1, 2).max(axis=0)
            for ijk_p in sorted(nummers):
                if ijk_p[as_] != t - 1:
                    continue
                ijk_q = tuple(t if i == as_ else ijk_p[i] for i in range(3))
                if ijk_q not in nummers:
                    continue
                mn_p, mx_p = cellen[ijk_p]
                mn_q, mx_q = cellen[ijk_q]
                rect = (max(mn_p[ua], smin[0]), max(mn_p[va], smin[1]), min(mx_p[ua], smax[0]), min(mx_p[va], smax[1]))
                if rect[2] - rect[0] <= 0 or rect[3] - rect[1] <= 0:
                    continue
                h = min(2.0, max(0.3, max(rect[2] - rect[0], rect[3] - rect[1]) / 150.0))
                us, vs, binnen = doorsnede.raster(segs, rect, h)
                if not binnen.any():
                    continue
                # the cell edges inside the plane are cut faces too: keep the pins away from them
                kl = doorsnede.klaring(us, vs, binnen)
                lab, n_eil = doorsnede.eilanden(binnen)
                np_, nq = nummers[ijk_p], nummers[ijk_q]
                naam = f"Cut {np_}-{nq}"
                dik = min(c - mn_p[as_], mx_q[as_] - c)

                def punt3(u_, v_):
                    p = [0.0, 0.0, 0.0]
                    p[as_], p[ua], p[va] = c, u_, v_
                    return Vector(p)

                def toets(u_, v_, r_gat):
                    if dik < diepte + opties["wand"]:
                        return False
                    return pl.toets(punt3(u_, v_), as_, r_gat, diepte, (ijk_p, ijk_q))

                tekst_p, tekst_q = f"{np_}-{nq}", f"{nq}-{np_}"
                uitslag = verbinders.plan_vlak(us, vs, binnen, kl, lab, n_eil, opties, toets, tekst_p)
                for eil in uitslag:
                    for (u_, v_, d) in eil["pennen"]:
                        r_gat = d / 2.0 + opties["speling"]
                        p3 = punt3(u_, v_)
                        pl.voeg_toe(p3, as_, r_gat, diepte, (ijk_p, ijk_q))
                        gat = {"p": list(p3), "as": as_, "r_gat": r_gat, "diepte": diepte, "pen_d": d,
                               "snede": c}
                        gaten.setdefault(ijk_p, []).append(dict(gat, teken=1, buur=nq))
                        gaten.setdefault(ijk_q, []).append(dict(gat, teken=-1, buur=np_))
                        pennen[d] = pennen.get(d, 0) + 1
                    if eil["melding"]:
                        if dik < diepte + opties["wand"]:
                            meldingen.append(f"{naam}: piece only {dik:.1f} mm thick here, a pin needs "
                                             f"{diepte + opties['wand']:.1f} mm. Glue this joint")
                        else:
                            meldingen.append(f"{naam}: {eil['melding']}")
                    if label_aan and eil["label"]:
                        u_, v_, hh, d2 = eil["label"]
                        p3 = list(punt3(u_, v_))
                        richting = None
                        if d2 is not None:
                            r3 = [0.0, 0.0, 0.0]
                            r3[ua], r3[va] = d2
                            richting = r3
                        breed = verbinders.label_maat(tekst_p, hh)[0]
                        for ijk, tk, tt in ((ijk_p, 1, tekst_p), (ijk_q, -1, tekst_q)):
                            labels.setdefault(ijk, []).append({"tekst": tt, "p": p3, "as": as_, "teken": tk, "h": hh,
                                                               "richting": richting, "breed": breed})
                    elif label_aan and eil["oppervlak"] > 4.0:
                        meldingen.append(f"{naam}: no room for the number on a part of this face")
    return gaten, labels, sorted(pennen.items()), meldingen
