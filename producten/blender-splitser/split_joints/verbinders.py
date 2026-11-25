"""Where the pins and the label go on one cut face (numpy, no bpy).

Input is the grid from doorsnede.py. A pin may stand at a grid point whose clearance to the edge of the
face is at least hole radius + minimum wall. One island gets 1 to 4 pins depending on its area: one in
the middle for a small face, otherwise spread out (farthest point first) so the pieces cannot turn.
Each point is also checked in 3D by the caller (toets), which looks at the wall deeper in the model and
at the holes of other faces. The label goes where it has the most room, away from the holes."""
import math

import numpy as np

LABEL_HOOGTES = (8.0, 6.0, 5.0, 4.0, 3.0, 2.5)  # text height in mm, largest that fits
MAX_PENNEN = 4
# Magnet sizes (diameter x thickness in mm) that are sold as standard neodymium discs. Key = what the panel shows.
MAGNETEN = (("5x2", 5.0, 2.0), ("6x2", 6.0, 2.0), ("6x3", 6.0, 3.0), ("8x3", 8.0, 3.0), ("10x3", 10.0, 3.0))
MAGNEET_LUCHT_MM = 0.1  # each magnet hole is this much deeper than the magnet, room for a drop of glue
MAGNEET_WAND_MM = 1.2  # never less wall than this around a magnet hole, whatever Min. wall says


def magneet_maat(sleutel):
    """(diameter, thickness) in mm of a magnet size key such as "6x2"."""
    for k, d, t in MAGNETEN:
        if k == sleutel:
            return d, t
    raise KeyError(sleutel)


def magneet_opties(sleutel, speling, wand):
    """Planner options for magnets: one fixed size (no smaller fallback), clearance on the diameter (half per
    side), hole as deep as the magnet plus a little, at least 1.2 mm wall."""
    d, t = magneet_maat(sleutel)
    return {"pen_d": d, "speling": speling / 2.0, "wand": max(wand, MAGNEET_WAND_MM), "auto": False, "min_d": d,
            "diepte": t + MAGNEET_LUCHT_MM, "soort": "magneet", "magneet": sleutel, "naam": f"{sleutel} mm magnet"}


def doel_aantal(oppervlak, d):
    """How many pins an island gets, from its area (mm2) and the pin diameter (mm)."""
    if oppervlak < 36.0 * d * d:
        return 1
    return int(min(MAX_PENNEN, max(2, round(oppervlak / (100.0 * d * d)) + 1)))


def label_maat(tekst, h):
    """(width, height) in mm of the label text at height h: pixel font of 3 x 5 cells, one empty column
    between characters (vormen.label_cellen)."""
    return (4 * max(1, len(tekst)) - 1) * h / 5.0, h


def kies_pennen(pu, pv, kl, nodig, n, toets):
    """Pick up to n points (indexes in pu/pv) with kl >= nodig. toets(i) is the 3D check."""
    kandidaat = np.nonzero(kl >= nodig)[0]
    if len(kandidaat) == 0:
        return []
    gekozen = []
    if n == 1:
        volgorde = kandidaat[np.argsort(-kl[kandidaat])]
        for i in volgorde[:400]:
            if toets(int(i)):
                return [int(i)]
        return []
    # spread out: start at the point farthest from the middle (most clearance), then farthest from the chosen.
    # Keep 3 mm more wall than the minimum where the face has room, so a hole does not show through the skin.
    ruim = max(nodig, min(nodig + 3.0, 0.5 * float(kl[kandidaat].max())))
    kandidaat = kandidaat[kl[kandidaat] >= ruim]
    vrij = np.ones(len(kandidaat), dtype=bool)
    midden = kandidaat[np.argmax(kl[kandidaat])]
    afstand = np.hypot(pu[kandidaat] - pu[midden], pv[kandidaat] - pv[midden])
    for _poging in range(400):
        if len(gekozen) >= n or not vrij.any():
            break
        if gekozen:
            g = gekozen[-1]
            nieuw = np.hypot(pu[kandidaat] - pu[g], pv[kandidaat] - pv[g])
            afstand = nieuw if len(gekozen) == 1 else np.minimum(afstand, nieuw)
        a = np.where(vrij, afstand, -1.0)
        best = int(np.argmax(a))
        if gekozen and a[best] < 2.0 * nodig:
            break  # no room for another pin without touching
        i = int(kandidaat[best])
        vrij[best] = False
        if toets(i):
            gekozen.append(i)
    return gekozen


def plan_vlak(us, vs, binnen, kl, labels, n_eil, opties, toets, tekst):
    """Plan pins and labels for every island of one cut face.

    opties: dict with pen_d (mm), speling, wand, auto (bool), min_d (mm).
    toets(u, v, r_gat) -> bool: the 3D check for a hole at (u, v).
    Returns a list per island: dict(oppervlak, pennen [(u, v, d)], label (u, v, h) or None, melding or None)."""
    gu, gv = np.meshgrid(us, vs)
    hu = (us[1] - us[0]) if len(us) > 1 else 1.0
    hv = (vs[1] - vs[0]) if len(vs) > 1 else 1.0
    uit = []
    for e in range(1, n_eil + 1):
        m = labels == e
        pu, pv, k = gu[m], gv[m], kl[m]
        opp = float(m.sum() * hu * hv)
        res = {"oppervlak": opp, "pennen": [], "label": None, "melding": None, "eiland": e}
        maten = [opties["pen_d"]]
        if opties.get("auto", True):
            d = opties["pen_d"] - 1.0
            while d >= opties.get("min_d", 3.0) - 1e-6:
                maten.append(round(d, 2))
                d -= 1.0
        for d in maten:
            r_gat = d / 2.0 + opties["speling"]
            nodig = r_gat + opties["wand"]
            n = doel_aantal(opp, d)
            gekozen = kies_pennen(pu, pv, k, nodig, n, lambda i: toets(float(pu[i]), float(pv[i]), r_gat))
            if gekozen:
                res["pennen"] = [(float(pu[i]), float(pv[i]), d) for i in gekozen]
                break
        if not res["pennen"]:
            res["melding"] = melding_geen_pen(k, min(maten), opties)
        res["label"] = kies_label(us, vs, np.where(m, kl, -np.inf), res["pennen"], opties, tekst)
        uit.append(res)
    return uit


def melding_geen_pen(k, d_min, opties):
    """Why no pin fits on this island, in words a buyer can check. k: clearance (mm to the edge) per grid point.
    Only name the width when the face really is too narrow; when it is wide enough, the 3D check refused every
    spot (the hole would come out of the surface behind the face, or touch another pin), so say that instead
    of numbers that read as a contradiction (7.6 mm across, needs 5.8 mm)."""
    breed = 2.0 * float(k.max()) if len(k) else 0.0
    nodig = d_min + 2 * (opties["speling"] + opties["wand"])
    if opties.get("soort") == "magneet":
        if breed < nodig:
            return (f"too small for a magnet: the face is {breed:.1f} mm across, a {opties['naam']} needs "
                    f"{nodig:.1f} mm with {opties['wand']:.1f} mm wall. Glue this joint or pick a smaller magnet")
        return ("no safe spot for a magnet: the wall around the hole would be under "
                f"{opties['wand']:.1f} mm or it would hit another hole. Glue this joint or pick a smaller magnet")
    if breed < nodig:
        return (f"too small for a pin: the face is {breed:.1f} mm across, a {d_min:g} mm pin needs "
                f"{nodig:.1f} mm. Glue this joint")
    return "no safe spot for a pin: a hole here would break out of the model or hit another pin. Glue this joint"


def kies_label(us, vs, kl2d, pennen, opties, tekst):
    """(u, v, h, richting) for the label, or None. kl2d: clearance on the grid, -inf outside this island.
    First straight (the text box fits in a circle), else along the face (a thin wall such as a vase or a
    hollow statue): the text follows the main direction of the face around the spot. richting is None for
    straight text, else (du, dv), the direction of the text line in the plane."""
    gu, gv = np.meshgrid(us, vs)
    ruimte = kl2d.copy()
    for (u, v, d) in pennen:
        r_gat = d / 2.0 + opties["speling"]
        ruimte = np.minimum(ruimte, np.hypot(gu - u, gv - v) - r_gat - 0.8)
    if not np.isfinite(ruimte).any():
        return None
    plat = np.where(np.isfinite(ruimte), ruimte, -1.0)
    i, j = np.unravel_index(int(np.argmax(plat)), plat.shape)
    for h in LABEL_HOOGTES:
        w, hh = label_maat(tekst, h)
        if plat[i, j] >= math.hypot(w / 2.0, hh / 2.0) + 0.5:
            return (float(us[j]), float(vs[i]), h, None)
    return langs_vlak(us, vs, plat, tekst)


def langs_vlak(us, vs, plat, tekst):
    """Label along a thin face: per spot the main direction of the roomy points around it (PCA), then the
    largest height whose text line keeps h/2 + 0.3 mm room along its whole length."""
    nv, nu = plat.shape
    hu = (us[1] - us[0]) if nu > 1 else 1.0
    hv = (vs[1] - vs[0]) if nv > 1 else 1.0
    volgorde = np.argsort(-plat, axis=None)[:300]
    beste = None
    for idx in volgorde:
        i, j = np.unravel_index(int(idx), plat.shape)
        if plat[i, j] <= 1.0:
            break
        straal = 15.0
        ri, rj = int(straal / hv) + 1, int(straal / hu) + 1
        blok = plat[max(0, i - ri):i + ri + 1, max(0, j - rj):j + rj + 1]
        bi, bj = np.nonzero(blok >= 0.6 * plat[i, j])
        if len(bi) < 3:
            continue
        pts = np.stack([us[bj + max(0, j - rj)], vs[bi + max(0, i - ri)]], axis=1)
        pts = pts - pts.mean(axis=0)
        _w, vecs = np.linalg.eigh(pts.T @ pts)
        d = vecs[:, -1]
        for h in LABEL_HOOGTES:
            if beste is not None and h <= beste[2]:
                break
            w, _hh = label_maat(tekst, h)
            t = np.linspace(-w / 2.0, w / 2.0, 13)
            qu, qv = us[j] + t * d[0], vs[i] + t * d[1]
            jj = np.rint((qu - us[0]) / hu).astype(int)
            ii = np.rint((qv - vs[0]) / hv).astype(int)
            if (jj < 0).any() or (jj >= nu).any() or (ii < 0).any() or (ii >= nv).any():
                continue
            if plat[ii, jj].min() >= h / 2.0 + 0.3:
                beste = (float(us[j]), float(vs[i]), h, (float(d[0]), float(d[1])))
                break
        if beste is not None and beste[2] >= LABEL_HOOGTES[0]:
            break
    return beste
