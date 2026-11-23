"""Where the pins and the label go on one cut face (numpy, no bpy).

Input is the grid from doorsnede.py. A pin may stand at a grid point whose clearance to the edge of the
face is at least hole radius + minimum wall. One island gets 1 to 4 pins depending on its area: one in
the middle for a small face, otherwise spread out (farthest point first) so the pieces cannot turn.
Each point is also checked in 3D by the caller (toets), which looks at the wall deeper in the model and
at the holes of other faces. The label goes where it has the most room, away from the holes."""
import math

import numpy as np

LABEL_HOOGTES = (8.0, 6.0, 5.0, 4.0, 3.0)  # text height in mm, largest that fits
LABEL_BREEDTE = 0.62  # width of one character in text heights (Blender's built-in font, digits and "-")
MAX_PENNEN = 4


def doel_aantal(oppervlak, d):
    """How many pins an island gets, from its area (mm2) and the pin diameter (mm)."""
    if oppervlak < 36.0 * d * d:
        return 1
    return int(min(MAX_PENNEN, max(2, round(oppervlak / (100.0 * d * d)) + 1)))


def label_maat(tekst, h):
    """(width, height) in mm of the label text at height h."""
    return LABEL_BREEDTE * h * max(1, len(tekst)), h


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
            d_min = min(maten)
            breed = 2.0 * float(k.max()) if len(k) else 0.0
            res["melding"] = (f"too small for a pin: the face is {breed:.1f} mm across, a {d_min:g} mm pin needs "
                              f"{d_min + 2 * (opties['speling'] + opties['wand']):.1f} mm. Glue this joint")
        res["label"] = kies_label(pu, pv, k, res["pennen"], opties, tekst)
        uit.append(res)
    return uit


def kies_label(pu, pv, k, pennen, opties, tekst):
    """(u, v, h) for the label: the point with the most room, away from the pin holes, or None."""
    if len(k) == 0:
        return None
    ruimte = k.copy()
    for (u, v, d) in pennen:
        r_gat = d / 2.0 + opties["speling"]
        ruimte = np.minimum(ruimte, np.hypot(pu - u, pv - v) - r_gat - 0.8)
    beste = int(np.argmax(ruimte))
    for h in LABEL_HOOGTES:
        w, hh = label_maat(tekst, h)
        if ruimte[beste] >= math.hypot(w / 2.0, hh / 2.0) + 0.5:
            return (float(pu[beste]), float(pv[beste]), h)
    return None
