# Hoofdbeeld Click Joints Pro voor Superhive en Gumroad (Bram, 21 nov 2026)

Opdracht hoofdchat 21 nov 06:45 NL: nieuw uitgelicht beeld, €0, echte Blender-render, 1200 x 600, naam groot en één belofte, duidelijke kleur.

Versie 2 (opdracht hoofdchat 08:50 NL, Daan kan 1 en 2): figuur groter, elk deel een andere kleur dan zijn buur, voeten van de onderrand, en twee Gumroad-maten erbij.

- `0-hoofdbeeld-pro.png`: 1200 x 600, Superhive (uitgelicht beeld).
- `0-hoofdbeeld-pro-1005.png`: 1005 x 565, Gumroad omslag op de productpagina.
- `0-hoofdbeeld-pro-vierkant.png`: 600 x 600, Gumroad zoeken, Discover en profiel.
- `0-hoofdbeeld-pro-600.png`: de 1200 x 600 op 600 x 300, om de rijtjesweergave te keuren.
- `render-figuur.png`: de kale Cycles-render (doorzichtig), 900 x 1200.

Wat er anders is dan versie 1 (GEZIEN, eigen meting met `maak_hoofdbeeld.py`):
- Figuur 555 px hoog in plaats van ±520 (de vage waas van de schaduwvanger telde eerst mee bij het bijsnijden). Breedte 26% van 1200, 29% van 1005, 51% van 600. De ±45% van Daan haal je bij een staande figuur op 2:1 alleen door hem af te snijden; ik koos de hele figuur met armen en been wijder uit elkaar.
- Drie kleuren als drie rollen filament: romp en hoofd licht, bovenarmen en dijen antraciet, onderarmen en onderbenen blauw. Elk deel verschilt van zijn buur, dus alle 10 delen zijn te tellen.
- Houding: beide ellebogen (80° en 40°), linkerknie 60°, beide schouders 18°, linkerheup 20°, nek 10°. Alles binnen wat Pro meldt (scharnier 140/120, kogel 20/25); het script stopt als een draai buiten het bereik valt.
- Voeten 17 tot 22 px boven de onderrand.

## Hoe gemaakt (alles na te doen)
1. Figuur: de CI-toets `producten/blender-gewrichten/e2e/toetsen_mens.py` met Pro 1.1.0 (`PRO_VERSIE=1.1.0 bash e2e/maak_zip.sh betaald`) op MakeHuman base.obj (CC0), Blender 5.3.0. Uitslag lokaal: 9 gewrichten, 10 delen, alle delen gesloten en één stuk, "KLAAR 0 FOUT" (GEZIEN, 21 nov).
2. `render_hoofdbeeld.py` (op het .blend dat `e2e/proef_mens.py` bewaart, met `CJ_HOOGTE=220`): draait scharnieren om hun eigen as en kogels om hun centrum uit de add-on, drie kleuren, Cycles 160 samples, AgX Punchy, schaduw op een vloer. Camera `HB_CAM=-450,-750`.
3. `maak_hoofdbeeld.py`: oranje vlak, "Click Joints" + blok "Pro", belofte "Turn your rig into a poseable 3D print", regel "Add-on for Blender" (niet in het vierkant, daar is geen plek). Maakt alle maten. Letter Inter Display (OFL).

Niets nagetekend: de vorm van elk deel en de naden zijn wat Pro maakt. De houding is een echte draai binnen het gemeten bereik.

Belofte past bij de geldende titel op Superhive ("poseable 3D print figures from your rig"). Prijs blijft $12 (geldend besluit), staat niet in het beeld.
