"""Meet de cijfers van de Fit test strip in de eerste laag (keuring Daan A3).

Gebruik: python3 meet_strip.py [fit-test-strip.stl] [beeld/strip-cijfers-eerste-laag.png]
Doorsnede op 0,3 mm boven het bed. Groef = gat in de schijf. Smalste breedte: de grootste w waarbij de groef
na krimpen en weer groeien met w/2 nog 97% van zijn oppervlak houdt. Beeld: gespiegeld, zoals je de onderkant ziet.
"""
import sys

import numpy as np
import trimesh
from shapely.geometry import Polygon

pad = sys.argv[1] if len(sys.argv) > 1 else "fit-test-strip.stl"
png = sys.argv[2] if len(sys.argv) > 2 else "beeld/strip-cijfers-eerste-laag.png"
m = trimesh.load(pad)
delen = m.split(only_watertight=False)
print("delen", len(delen), "waterdicht", all(d.is_watertight for d in delen), "zmin", round(float(m.bounds[0][2]), 3),
      "maat mm", np.round(m.extents, 1))
pl, _ = m.section(plane_origin=[0, 0, 0.3], plane_normal=[0, 0, 1]).to_2D(to_2D=np.eye(4))
vlakken = pl.polygons_full
groeven = [Polygon(h) for P in vlakken for h in P.interiors]


def smal(g):
    lo, hi = 0.0, 3.0
    for _ in range(25):
        w = (lo + hi) / 2
        if g.buffer(-w / 2).buffer(w / 2).area >= 0.97 * g.area:
            lo = w
        else:
            hi = w
    return lo


ws = sorted(smal(g) for g in groeven)
print("groeven", len(groeven), "smalste mm", [round(w, 2) for w in ws[:6]], "onder 0,8 mm:", sum(w < 0.8 for w in ws))
for P in vlakken:
    if P.interiors:
        xs = [c[0] for h in P.interiors for c in h.coords]
        ys = [c[1] for h in P.interiors for c in h.coords]
        print(f"schijf {P.bounds[2]-P.bounds[0]:.1f} mm, cijfers {max(xs)-min(xs):.1f} breed x {max(ys)-min(ys):.1f} hoog")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(14, 6), dpi=110)
for P in vlakken:
    x, y = P.exterior.xy
    ax.fill([-v for v in x], y, color="#888")
    for h in P.interiors:
        x, y = zip(*h.coords)
        ax.fill([-v for v in x], y, color="white")
ax.set_aspect("equal")
ax.set_title("Eerste laag (0,3 mm), van onder gezien")
fig.savefig(png, bbox_inches="tight")
print("beeld", png)
