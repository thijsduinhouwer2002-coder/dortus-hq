# Studio voor de Blender-filmpjes van Click Joints Pro

Gemaakt 23 nov 2026 (opdracht hoofdchat ±11:45 NL, na "onze filmpjes zijn saai, de omgeving in Blender moet ook beter").
Vanaf nu wordt elk Blender-filmpje (Short, TikTok, lange video) in deze studio opgenomen, met dit figuur.
Bewijs: workflow `.github/workflows/studio.yml`, release `studio-1`.

## Wat erin zit
| Bestand | Wat |
|---|---|
| `figuur_laden.py` | `laad_mens_kleding(obj)`: het figuur (MakeHuman, CC0) aangekleed als speelgoedfiguur, met rig. `laad(glb)`: elk ander figuur met eigen rig (glb of blend) als één mesh voor Figure from rig. |
| `studio.py` | `bouw()`: gebogen achterwand in muntgroen, wit podium met gele rand, 3 vlakke lampen plus een zon zonder schaduw, EEVEE. `plastic(delen)`: geprint plastic. `camera()`, `richt()`: staand 9:16 of liggend 16:9. `render()`: door de camera. `rustig_scherm()`: opnamescherm. |
| `bewijs.py` | Het hele verloop als voorbeeld: figuur, studio, 3 schermafbeeldingen, Figure from rig, 3 renders. |
| `proef_figuur.py` | Proef per kandidaat-figuur: hoeveel gewrichten maakt Figure from rig? |
| `modellen/makehuman-base.obj` | Het model, ongewijzigd van MakeHuman, met `makehuman-base-LICENTIE.md` (CC0 1.0). |

## Het figuur
MakeHuman `base.obj` (CC0 1.0, bron en licentietekst in `modellen/`), door ons aangekleed in `laad_mens_kleding`:
borst plat en romp glad (zoals de e2e-figuur), dan per stuk kleding het oppervlak een fractie naar buiten zodat zomen in
de vorm zitten: shirt met korte mouwen (0,45 mm), broek (0,45 mm), riem (0,9 mm), schoenen (bolle schil om de voet, platte zool, geen tenen),
haar (2,2 mm). Ogen, wenkbrauwen en mond zijn kleur. Daarna Make watertight van de add-on en de rig uit
`producten/blender-gewrichten/e2e/proef_mens.py` (linkerknie 120 en linkerelleboog 140 in Limit Rotation).
Geen AI-model, geen merk of bekend personage.

Waar het niet mag: op de schouders en mouwen en aan de binnenkant van de dijen geen extra dikte. Daar komen de kogels
van schouder en heup; met dikte erbij werden ze geblokkeerd (proef: 6 of 7 gewrichten in plaats van 9).

Kleurstellingen (sRGB): **a** oranje shirt FF6B3D, blauwe broek 2F6BFF, gele schoenen FFD23F, bruin haar 4A2C1D.
**b** paars shirt 7B5CFF, donkere broek 2B2D42, roze schoenen en riem FF4F79, blond haar F4B942
(`STIJLEN` in `bewijs.py`, `stijl=` in `laad_mens_kleding`).

## Kandidaten (Figure from rig, Pro 1.2.0, Blender 5.3.0)
KANDIDATEN_TABEL

## Zo laad je de studio in een opname-workflow
In de workflow (zie `studio.yml`): Blender 5.3.0, de Pro-zip 1.2.0 (`PRO_COMMIT` f8dfbd3, `PRO_VERSIE=1.2.0 bash
e2e/maak_zip.sh betaald`) en `xvfb-run` met `--gpu-backend opengl`. In het opnamescript:
```python
import sys; sys.path.insert(0, "commercie/filmpjes/studio")
import figuur_laden as FL, studio as S
arm, ob, punten = FL.laad_mens_kleding("commercie/filmpjes/studio/modellen/makehuman-base.obj", 220.0)  # stijl={...} mag
arm.hide_set(True)
S.bouw(220.0)                  # studio rond het figuur (voeten op z=0, podium eronder)
S.rustig_scherm(ui=1.35)       # alleen 3D-weergave en paneel, groter lettertype, studiolicht in beeld
# ... echte klikken: figuur kiezen, Figure from rig, schuiven (zoals youtube-shorts-4/opname.py) ...
delen = [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_figuur") == ob.name and o.visible_get()]
S.plastic(delen)               # alleen voor de renders: plastic en de passingkleuren van de add-on weg
cam = S.camera(); S.richt(cam, delen, "staand", draai=-32, kantel=7, vul=0.74, midden_y=0.56)
S.render("/tmp/uit/eind.png")  # door de 3D-weergave, dus met de buiging van de add-on
```
- In `youtube-shorts-4/opname.py` vervang je `figuur()` door `FL.laad_mens_kleding` en `zet_render_scene()` door
  `S.bouw` plus `S.plastic` en `S.camera`. Het scherm: `S.rustig_scherm` in plaats van `kijk_breed` (de zijbalk breed
  slepen en de echte muis blijven werken zoals ze waren).
- Poseren alleen via de add-on: scharnieren met `wm.cj_scharnier_pose` op deel B (knie 0 tot 120, elleboog 0 tot 140).
  De kogels (schouder, heup, nek) zijn ±20 tot ±25° en draaien in de add-on allemaal tegelijk; laat ze in de renders op 0.
- Zijbalk scrollen gaat met het muiswiel (xdotool klik 5 omlaag, 4 omhoog, boven het paneel); klikken op de kop van
  het paneel om in te klappen werkte in de proef niet betrouwbaar.
- Renders gaan door de 3D-weergave (`bpy.ops.render.opengl`, Material Preview met de lampen van de scene). EEVEE in
  software-OpenGL is traag en zwaar: reken op ±1 minuut en 4 tot 6 GB geheugen per render. `CJ_TEST=1` geeft 40% en
  weinig samples om snel te kijken.

## Licht en kleur (in `studio.py`, bovenaan)
Achterwand: verloop van E4F6EF (vloer) naar 86D9C2 (wand), loopt rond over zonder naad. Podium FFFFFF met rand FFD23F.
Lampen (scene in mm, kracht op het oog gezet): sleutel links voor (schijf 1,1 keer de figuurhoogte), vul rechts,
rand achter, plus een zon zonder schaduw voor de wand. AgX, look Punchy. Plastic: ruwheid 0,36,
laklaag 0,25, laaglijnen 0,4 mm als licht reliëf.

## Wat nog niet mooi is
ZWAKTES
