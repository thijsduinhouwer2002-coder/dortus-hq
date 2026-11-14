"""Figuren voor het blad voor Thijs (Daan, 14 nov): zeven helden in een rij, doorzichtig.
Draai: python3.13 figuren.py <uit.png> <breedte> <hoogte>"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../producten/steam-hol/modellen"))
import bpy, held, gedeeld as g
g.leeg()
rij = [("held", 0), ("held", 1), ("held", 2), ("held", 3), ("held", 4), ("dief", 0), ("bard", 0)]
for i, (soort, k) in enumerate(rij):
    held.bouw(soort, "rust", ((i - 3) * 1.5, 0, 0), draai=20, kleur=k)
bpy.ops.mesh.primitive_plane_add(size=40); bpy.context.object.is_shadow_catcher = True
g.camera(hoogte_midden=1.25, schaal=11.0)
g.licht()
g.render(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), 32, doorzichtig=True)
