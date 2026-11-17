"""Toets: een knie in een echte Meshy-figuur laat de voet niet achter (Chris, army_man, 16 nov 20:00).

Fout in 0.1.1 en 1.0.2: Exact UNION van omhulsel en lid (een_lid._samen) gaf soms alleen het omhulsel terug. Alles
van het lid buiten het omhulsel (de zool) bleef als los stuk in deel B. Nu telt die UNION alleen als hij het lid echt
bevat, anders Self Intersection, anders "los".
Eis per knie-hoogte (27, 25, 29 % van de hoogte, zoals maak_chris_figuur): óf geen delen (eerlijke weigering), óf
deel A en B elk één stuk en deel A reikt tot de vloer (de voet zit erin). Minstens één hoogte lukt (vanaf Blender 4.5; in 4.2 met alleen
de Exact-solver mag hij op alle hoogtes eerlijk weigeren, plan punt 3).
Gebruik: blender -b --factory-startup --python e2e/toetsen_meshy_voet.py -- <betaalde zip> <army_man.glb>
"""
import os
import sys

import bpy

HIER = os.path.dirname(os.path.abspath(__file__))
FOUT = []


def check(ok, t):
    print(f"[cj-voet] {'OK  ' if ok else 'FOUT'} {t}", flush=True)
    if not ok:
        FOUT.append(t)


src = open(os.path.join(HIER, "maak_chris_figuur.py"), encoding="utf-8").read()
c = {"__name__": "maak_chris_figuur", "__file__": os.path.join(HIER, "maak_chris_figuur.py")}
exec(compile(src, "maak_chris_figuur.py", "exec"), c)
args = sys.argv[sys.argv.index("--") + 1:]
c["g"]["installeer"](args[0])
gelukt = 0
for pct in (27, 25, 29):
    heel, naam, zij, voor = c["een_poging"](args[1], pct)
    delen = [o for o in c["zichtbaar"]() if o.get("cj_deel")]
    if not delen:
        check(True, f"knie {pct}%: geweigerd, geen delen")
        continue
    st = {o.get("cj_deel"): c["stukken"](o) for o in delen}
    check(st.get("A") == 1 and st.get("B") == 1, f"knie {pct}%: A en B elk één stuk ({st})")
    a = next(o for o in delen if o.get("cj_deel") == "A")
    laag = min((a.matrix_world @ v.co).z for v in a.data.vertices)
    check(laag < 1.0, f"knie {pct}%: deel A reikt tot de vloer (laagste {laag:.2f} mm)")
    check(voor.x < -0.5, f"knie {pct}%: tenen naar -x zoals op het beeld van Chris ({tuple(voor)})")
    gelukt += 1 if heel and laag < 1.0 else 0
if bpy.app.version >= (4, 5, 0):
    check(gelukt >= 1, f"minstens één knie heel gelukt ({gelukt})")
else:
    # Blender 4.2 heeft alleen de Exact-solver; daar weigert de knie op army_man op alle drie de hoogtes eerlijk
    # ("no watertight parts", CI run 43948028758). Bekend punt 3 van het plan; nooit een kapot deel is hier de eis.
    print(f"[cj-voet] INFO 4.2: {gelukt} knie(ën) heel gelukt, weigeren is hier toegestaan (plan punt 3)", flush=True)
print(f"[cj-voet] KLAAR {len(FOUT)} FOUT", flush=True)
