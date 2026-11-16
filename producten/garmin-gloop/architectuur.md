# Gloop-spel voor Garmin: onderdelen

- `source/Spel.mc`: module `Regel` (vaste getallen) en klasse `Spel` (de regels: toestand, vallen, drukken, klok, beste score). Kent het scherm niet, dus volledig te toetsen.
- `source/SpelView.mc`: tekent het spel met de plaatjes van Mila in opstelling (c): Gloop in het midden met de toren op zijn kop, de held schuin van linksboven. Plaatst alles naar verhouding van het scherm, laat de klok elke 50 ms tikken, bewaart de beste score (`Application.Storage`, sleutel `beste`). Bevat ook de zelfspeler voor de bouwstraat.
- `source/SpelDelegate.mc`: de ene knop (START of tik) roept `Spel.druk()` aan.
- `source/GloopApp.mc`: start, leest de beste score.
- `source/Bouw.mc`: bouwvlag `AUTO` (alleen de bouwstraat zet hem op true).
- `source/SpelTest.mc`: de toetsen (Run No Evil).
- `source/Maten.mc`: maten en ankers van de plaatjes per schermbreedte. Gemaakt door `maak_kit.py`, niet met de hand aanpassen.
- `res-260/`, `res-320/`, `res-390/`: de plaatjes per schermbreedte (260 is MIP met 64 kleuren, dithering uit). Gemaakt door `maak_kit.py` uit `ontwerp/garmin/gloop-spel/kit/` op main. `monkey.jungle` koppelt elk horloge aan zijn map.
- `maak_kit.py`: zet de kit van Mila om naar de drie mappen en `Maten.mc`. Opnieuw draaien als de kit verandert.
