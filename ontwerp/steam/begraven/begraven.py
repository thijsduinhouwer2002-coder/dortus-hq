"""Begraven dingen in de dichte aarde (Mila, 16 nov 2026, vraag Daan 20:50, voor de demo van 18 dec).
Vier stukken, elk in een vak van 64 x 64 bladpixels (= een cel van 16 x 16 spelpixels, 4 per spelpixel):
een oude hoed, een bot, een kistje, een wortel. Schuin, alsof ze zo in de grond zijn gezakt.
Het dempen (stof, aarde eroverheen) gebeurt daarna in leg_in_aarde.py, zodat het model gewoon blijft.
Gebruik: <venv>/bin/python begraven.py <uit.png>
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../producten/steam-hol/modellen'))
import bpy
import gedeeld as g

g.leeg()

def obj_uit(op, naam, m, **kw):
    op(**kw); o = bpy.context.active_object; o.name = naam; o.data.materials.append(m)
    bpy.ops.object.shade_smooth(); return o

def groep(naam, delen, loc, rot):
    leeg = bpy.data.objects.new(naam, None); bpy.context.scene.collection.objects.link(leeg)
    for d in delen: d.parent = leeg
    leeg.location = loc; leeg.rotation_euler = [math.radians(a) for a in rot]
    return leeg

M = bpy.ops.mesh
hoedm = g.mat('hoed', g.hex2('6b4fbf'), rough=0.8)         # paars, de hoed van een held die het niet haalde
bandm = g.mat('band', g.hex2('f2b632'), rough=0.4, metaal=0.3)
botm = g.mat('bot', g.hex2('efe6cc'), rough=0.6)
houtm = g.mat('hout', g.hex2('8a5a34'), rough=0.7)
goudm = g.mat('goud', g.hex2('f2b632'), rough=0.3, metaal=0.6)
wortm = g.mat('wortel', g.hex2('e8792a'), rough=0.6)
loofm = g.mat('loof', g.hex2('5fae4a'), rough=0.6)

# 1 hoed: punthoed met gouden band, half op zijn kant
kegel = obj_uit(M.primitive_cone_add, 'kegel', hoedm, radius1=0.2, radius2=0.02, depth=0.46, location=(0, 0, 0.26), vertices=32)
rand = obj_uit(M.primitive_cylinder_add, 'rand', hoedm, radius=0.32, depth=0.04, location=(0, 0, 0.03), vertices=40)
band = obj_uit(M.primitive_cylinder_add, 'band', bandm, radius=0.205, depth=0.06, location=(0, 0, 0.08), vertices=32)
groep('hoed', [kegel, rand, band], (-1.5, 0, -0.15), (0, 35, 0))

# 2 bot: staaf met twee knobbels aan elk eind, schuin
staaf = obj_uit(M.primitive_cylinder_add, 'staaf', botm, radius=0.06, depth=0.56, location=(0, 0, 0), vertices=20, rotation=(0, math.radians(90), 0))
kn = [obj_uit(M.primitive_uv_sphere_add, f'kn{i}', botm, radius=0.095, location=(sx * 0.3, 0, sz * 0.07)) for i, (sx, sz) in enumerate(((-1, 1), (-1, -1), (1, 1), (1, -1)))]
groep('bot', [staaf] + kn, (-0.5, 0, 0), (0, -25, 0))

# 3 kistje: kist met bolle deksel en gouden slot, iets gekanteld
kist = obj_uit(M.primitive_cube_add, 'kist', houtm, size=1, location=(0, 0, 0))
kist.scale = (0.44, 0.3, 0.26)
dek = obj_uit(M.primitive_cylinder_add, 'deksel', houtm, radius=0.15, depth=0.44, location=(0, 0, 0.13), vertices=24, rotation=(0, math.radians(90), 0))
dek.scale = (1, 1, 1); dek.scale[0] = 1
bnd = [obj_uit(M.primitive_cube_add, f'beslag{i}', goudm, size=1, location=(x, 0, 0.06)) for i, x in enumerate((-0.16, 0.16))]
for b in bnd: b.scale = (0.04, 0.32, 0.42)
slot = obj_uit(M.primitive_cube_add, 'slot', goudm, size=1, location=(0, -0.16, 0.08)); slot.scale = (0.08, 0.04, 0.1)
groep('kist', [kist, dek, slot] + bnd, (0.5, 0, -0.04), (0, 12, 0))

# 4 wortel: dikke oranje wortel met drie loofsprieten, met de punt naar beneden
wort = obj_uit(M.primitive_cone_add, 'wortel', wortm, radius1=0.12, radius2=0.015, depth=0.62, location=(0, 0, 0), vertices=24, rotation=(math.radians(180), 0, 0))
loof = [obj_uit(M.primitive_cone_add, f'loof{i}', loofm, radius1=0.035, radius2=0.0, depth=0.28, location=(math.sin(a) * 0.06, 0, 0.42), rotation=(0, a, 0), vertices=10) for i, a in enumerate((-0.45, 0, 0.45))]
groep("wortel", [wort] + loof, (1.5, 0, -0.08), (0, -30, 0))

g.camera(hoogte_midden=0.0, schaal=4.0)
g.licht()
g.render(sys.argv[-1], 256, 64, samples=48, doorzichtig=True)
