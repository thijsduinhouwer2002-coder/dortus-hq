# Gloop-spel voor Garmin: onderdelen

- `source/Spel.mc`: module `Regel` (vaste getallen) en klasse `Spel` (de regels: toestand, vallen, drukken, klok, beste score). Kent het scherm niet, dus volledig te toetsen.
- `source/SpelView.mc`: tekent het spel met de plaatjes van Mila in opstelling (c): Gloop in het midden met de toren op zijn kop, de held schuin van linksboven. Plaatst alles naar verhouding van het scherm, laat de klok elke 50 ms tikken, bewaart de beste score (`Application.Storage`, sleutel `beste`). Bevat ook de zelfspeler voor de bouwstraat.
- `source/Letters.mc`: alle letters op het scherm (stripletter met zwarte rand van 2 px en nep-vet op AMOLED, de regel onderaan, de knophint, de kreet bij een slok, het eindscherm). `knop()` geeft het woord voor de knop: START, of PRESS op de Venu 3, Venu 3S en Venu Sq 2; `monkey.jungle` kiest per horloge met `(:metstart)` en `(:zonderstart)`. In run 110 afgesplitst van `SpelView.mc`, dat boven de 400 regels zat (nu 318).
- `source/SpelDelegate.mc`: de ene knop (START of tik) roept `Spel.druk()` aan.
- `source/GloopApp.mc`: start, leest de beste score.
- `source/Bouw.mc`: bouwvlag `AUTO` (alleen de bouwstraat zet hem op true).
- `source/SpelTest.mc`: de toetsen (Run No Evil).
- `source/Maten.mc`: maten en ankers van de plaatjes per schermbreedte. Gemaakt door `maak_kit.py`, niet met de hand aanpassen.
- `res-208/` tot `res-454/` (acht mappen): de plaatjes per schermbreedte. 208, 240, 260 en 280 zijn MIP (64 kleuren, dithering uit); 320, 390, 416 en 454 zijn AMOLED en hebben ook `grot_donker.png`, de donkere grot van Mila als plaatje van het hele scherm. `res-208/` heeft `grot_8kleur.png` (zwart, rood, geel) voor de Forerunner 55; die laadt hem met dezelfde functie `laadGrot()` als AMOLED. Gemaakt door `maak_kit.py` uit `ontwerp/garmin/gloop-spel/kit/` op main. `monkey.jungle` koppelt elk horloge aan zijn map en sluit met `excludeAnnotations` één van de twee functies `laadGrot()` uit: `(:amoled)` laadt het plaatje, `(:mip)` geeft niets terug en dan tekent het spel de effen grot.
- `maak_kit.py`: zet de kit van Mila om naar de acht mappen en `Maten.mc`. Opnieuw draaien als de kit verandert.
