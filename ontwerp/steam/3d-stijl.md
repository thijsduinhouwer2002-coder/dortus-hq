# Het Hol: de 3D-stijl (besluit Thijs 13 nov 13:35)

Thijs: "ja de hele app gewoon". **Alles in Het Hol wordt 3D, gemaakt met code in Blender (bpy) en gerenderd tot plaatjes**: figuren, helden, het hol, de spullen én de winkelbeelden. Geen pixelart meer, geen AI-beeld (dan hoeft er geen AI-melding op Steam). Het spel zelf blijft 2D in Godot: het toont de gerenderde plaatjes.

## Ankers (hier begint iedereen)
- `ontwerp/steam/proef-3d/gloop.py` en `groot2.png`: de eerste proef van de hoofdchat (20 minuten werk). Richting, geen eindbeeld.
- `ontwerp/steam/proef-3d/strook-3d-2x.png`: dezelfde Gloop op 44, 56 en 70 px in de echte strook. Op ware grootte leest hij goed; naast de pixelwereld vloekt hij. Daarom moet alles mee.
- Kleuren blijven die van `ontwerp/steam/mila/stijl.md`: pruim hol, muntgroene Gloop, goud, warm fakkellicht op koel donker. Het verhaal blijft: Gloop met één oog, scheve grijns met één tand, de hoedentoren.

## Regels
1. **Eén camera voor alles**: orthografisch, licht van boven (±15 graden), zodat alles in dezelfde wereld staat. Eén lichtopstelling (warme fakkel rechts, koel tegenlicht links, zacht van boven), in één gedeeld bestand.
2. **Vormen eenvoudig en rond**, zacht glanzend, "speelgoed". Grote ogen, duidelijke silhouetten. Op 40 tot 60 px moet je zien wat het is.
3. **Toets altijd op ware grootte in de echte strook** (120 px), naast Rusty's Retirement en Ropuka op dezelfde maat. Vergroot mag ernaast; ware grootte beslist.
4. **Herkennen toetst een frisse kijker** die alleen het plaatje krijgt. Letterlijk opschrijven wat hij zegt.
5. **Eerst één ding helemaal goed (Gloop), dan breed.** Thijs keurt op vaste momenten met hoogstens 3 versies per blad.
6. Renderen gaat met Blender als Python-pakket (`pip install bpy==5.2.4` in een venv; ±45 s per plaatje op de CPU) of in GitHub Actions. Elk model is een `.py`-bestand in `producten/steam-hol/modellen/`, zodat het herhaalbaar is.
7. Webpagina's lees je met `curl` in Bash, nooit met WebFetch.

## Wie doet wat
- **Daan:** Gloop in 3D (model, uitdrukkingen, hoedentoren, animaties). Daarna de helden.
- **Mila:** het hol in 3D (wand, vloer, gangen, schat, fakkels, val) en daarna de winkelafbeelding.
- **Bram:** de pijplijn: van `.py`-model naar beeldreeksen (frames) naar Godot, automatisch in Actions; zuinig blijven (CPU, geheugen).
- **Olaf:** het spel en de demolijst; hij zet de nieuwe beelden erin.
