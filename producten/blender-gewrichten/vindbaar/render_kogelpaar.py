# Render van het kogelpaar voor Printables (Bram, 27 nov, #257). Kopie van commercie/verspreiden/beeld/render_stl.py
# met achterkanten weggelaten (anders zwarte streepjes) en dpi 150. Eerst het paar samenvoegen (B omgedraaid, 30 mm ernaast):
#   python3 -c "import trimesh,numpy as np; a=trimesh.load('commercie/blender-click-joints/testprint/kogel-deel-A.stl'); b=trimesh.load('commercie/blender-click-joints/testprint/kogel-deel-B.stl'); b.apply_transform(trimesh.transformations.rotation_matrix(np.pi,[1,0,0])); [m.apply_translation([-m.centroid[0],-m.centroid[1],-m.bounds[0][2]]) for m in (a,b)]; b.apply_translation([30,0,0]); trimesh.util.concatenate([a,b]).export('/tmp/kogelpaar.stl')"
#   python3 producten/blender-gewrichten/vindbaar/render_kogelpaar.py /tmp/kogelpaar.stl uit.png 38 -100 0.62
import sys, numpy as np, trimesh, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
stl, out, elev, azim = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
m = trimesh.load(stl)
tri = m.vertices[m.faces]; n = m.face_normals
# light from camera direction-ish
e, a = np.radians(elev), np.radians(azim)
cam = np.array([np.cos(e)*np.cos(a), np.cos(e)*np.sin(a), np.sin(e)])
L = cam*float(sys.argv[6] if len(sys.argv)>6 else 0.7) + np.array([0.5,-0.4,0.6 if elev>0 else -0.3]); L /= np.linalg.norm(L)
keep = (n@cam) > 0.0
tri, n = tri[keep], n[keep]
I = np.clip(n@L, 0, 1)*0.75 + 0.22
base = np.array([0.93,0.55,0.20])  # oranje PLA-kleur
cols = np.clip(I[:,None]*base, 0, 1)
if elev<0:
    zc=tri[:,:,2].mean(1); rec=(zc>0.05)&(zc<1.5)
    cols[rec]=cols[rec]*0.35
fig = plt.figure(figsize=(16,9), dpi=150); fig.patch.set_facecolor('#2b2b2b')
ax = fig.add_subplot(111, projection='3d'); ax.set_facecolor('#2b2b2b')
pc = Poly3DCollection(tri, facecolors=cols, edgecolors=cols, linewidths=0.3, antialiased=False)
ax.add_collection3d(pc)
mn, mx = m.bounds; c = (mn+mx)/2; r = (mx-mn).max()/2*float(sys.argv[5]) if len(sys.argv)>5 else (mx-mn).max()/2
ax.set_xlim(c[0]-r, c[0]+r); ax.set_ylim(c[1]-r, c[1]+r); ax.set_zlim(c[2]-r, c[2]+r)
ax.set_box_aspect((1,1,1)); ax.view_init(elev=elev, azim=azim); ax.set_axis_off()
plt.subplots_adjust(0,0,1,1); ax.dist = 6
plt.savefig(out, facecolor=fig.get_facecolor()); print(out)
