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
I = np.clip(n@L, 0, 1)*0.75 + 0.22
base = np.array([0.93,0.55,0.20])  # oranje PLA-kleur
cols = np.clip(I[:,None]*base, 0, 1)
if elev<0:
    zc=tri[:,:,2].mean(1); rec=(zc>0.05)&(zc<1.5)
    cols[rec]=cols[rec]*0.35
fig = plt.figure(figsize=(16,9), dpi=100); fig.patch.set_facecolor('#2b2b2b')
ax = fig.add_subplot(111, projection='3d'); ax.set_facecolor('#2b2b2b')
pc = Poly3DCollection(tri, facecolors=cols, edgecolors=cols, linewidths=0.3, antialiased=False)
ax.add_collection3d(pc)
mn, mx = m.bounds; c = (mn+mx)/2; r = (mx-mn).max()/2*float(sys.argv[5]) if len(sys.argv)>5 else (mx-mn).max()/2
ax.set_xlim(c[0]-r, c[0]+r); ax.set_ylim(c[1]-r, c[1]+r); ax.set_zlim(c[2]-r, c[2]+r)
ax.set_box_aspect((1,1,1)); ax.view_init(elev=elev, azim=azim); ax.set_axis_off()
plt.subplots_adjust(0,0,1,1); ax.dist = 6
plt.savefig(out, facecolor=fig.get_facecolor()); print(out)
