# Hoofdbeeld Click Joints Pro voor Superhive (Bram, 21 nov 2026)

Opdracht hoofdchat 21 nov 06:45 NL: nieuw uitgelicht beeld, €0, echte Blender-render, 1200 x 600, naam groot en één belofte, duidelijke kleur.

- `0-hoofdbeeld-pro.png`: 1200 x 600, het beeld voor Superhive.
- `0-hoofdbeeld-pro-600.png`: zelfde op 600 x 300, om de rijtjesweergave te keuren.
- `render-figuur.png`: de kale Cycles-render (doorzichtig), 900 x 1200.

## Hoe gemaakt (alles na te doen)
1. Figuur: de CI-toets `producten/blender-gewrichten/e2e/toetsen_mens.py` met Pro 1.1.0 (`PRO_VERSIE=1.1.0 bash e2e/maak_zip.sh betaald`) op MakeHuman base.obj (CC0), Blender 5.3.0. Uitslag lokaal: 9 gewrichten, 10 delen, alle delen gesloten en één stuk, "KLAAR 0 FOUT" (GEZIEN, 21 nov).
2. `render_hoofdbeeld.py`: draait de linkerknie 55° (bereik 120°) en de rechterelleboog 70° (bereik 140°) om hun eigen scharnieras uit de add-on, twee kleuren (romp licht, ledematen donker), Cycles 160 samples, schaduw op een vloer.
3. `maak_hoofdbeeld.py`: oranje vlak, "Click Joints" + blok "Pro", belofte "Turn your rig into a poseable 3D print", regel "Add-on for Blender". Letter Inter Display (OFL).

Niets nagetekend: de vorm van elk deel en de naden zijn wat Pro maakt. De houding is een echte draai binnen het gemeten bereik.

Belofte past bij de geldende titel op Superhive ("poseable 3D print figures from your rig"). Prijs blijft $12 (geldend besluit), staat niet in het beeld.
