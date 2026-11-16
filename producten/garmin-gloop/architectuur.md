# Gloop-spel voor Garmin: onderdelen

- `source/Spel.mc`: module `Regel` (vaste getallen) en klasse `Spel` (de regels: toestand, vallen, drukken, klok, beste score). Kent het scherm niet, dus volledig te toetsen.
- `source/SpelView.mc`: tekent alles naar verhouding van het scherm, laat de klok elke 50 ms tikken, bewaart de beste score (`Application.Storage`, sleutel `beste`). Bevat ook de zelfspeler voor de bouwstraat.
- `source/SpelDelegate.mc`: de ene knop (START of tik) roept `Spel.druk()` aan.
- `source/GloopApp.mc`: start, leest de beste score.
- `source/Bouw.mc`: bouwvlag `AUTO` (alleen de bouwstraat zet hem op true).
- `source/SpelTest.mc`: de toetsen (Run No Evil).
