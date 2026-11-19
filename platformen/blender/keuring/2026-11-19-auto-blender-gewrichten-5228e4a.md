# Keuring blender-gewrichten (Fit test strip, herkansing snede), 19-11-2026, automatische keurder
Wat ik keurde: commit 5228e4a60 (4d9de40..5228e4a): `betaald/testkaart.py`, `e2e/toetsen_testkaart.py`, `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Ik heb alleen de diff gezien, niet het ontwerp `platformen/blender-2/testkaart-ontwerp.md` en geen runlog.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De snede is nu een eigen functie `_snijd`. Die probeert hooguit vier kleine cursorschuiven en ruimt bij mislukken de halve delen op. De eerste schuif is gelijk aan de oude vaste waarde, dus het gedrag bij succes blijft gelijk. | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | De commit zegt dat "Fit test strip rood in 4.2" is opgelost. In de tekst staat geen groene run die dat bevestigt. Alleen de code-opmerking noemt run 44576138702, de run met de fout. | Vermoeden | Midden | Een groene run van de betaalde build op 4.2.23 en 5.2.3 met stap "Figuurpresets" na deze commit. |
| 3 | De oorzaak van de weigering in 4.2.23 is niet onderzocht. De herkansing met een andere schuif verbergt hem. Dat past bij een weigering die afhangt van samenvallende vlakken, maar dat is niet bewezen. | Vermoeden | Midden | Meerdere runs achter elkaar op 4.2.23 in meters, zonder dat de melding "Missing" voorkomt. |
| 4 | Het herstel van de koperinstellingen zet nu `kogel_mm` vóór `kogel_auto` terug. Dat klopt met de update die Auto uitzet. De test controleert dat Auto aan blijft. | Feit (uit de diff) | Hoog | n.v.t. |
| 5 | De test raakt het herkansingspad zelf niet. Er is geen figuur of afdwinging waarbij de eerste schuif faalt. | Feit | Hoog | Een test die de eerste schuif laat falen en dan een geslaagde set eist. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is strenger gemaakt (Auto-controle erbij), niet versoepeld. | Feit | Hoog | Tests niet aangepast om te slagen: ok |
| 2 | `architectuur.md` is bijgewerkt met de Fit test strip, de herkansing en het terugzetten van Auto. | Feit | Hoog | architectuur.md bijgewerkt: ok |
| 3 | De architectuurtekst zegt "nog een keer ... (vier keer)". De code heeft vier schuiven in totaal, dus drie herkansingen. De tekst is dubbelzinnig. | Feit | Hoog | Architectuur moet kloppen met de code (klein) |
| 4 | De Pro-functie staat niet in de gratis `CHANGELOG.md`. De gratis build blijft zonder betaalde woorden. | Feit | Hoog | Gratis zip zonder betaald: ok |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | Hoog | Geen persoonsgegevens: ok |
| 6 | `testkaart.py` lijkt ruim onder ±400 regels. De exacte regelaantallen staan niet in de diff. | Vermoeden | Midden | Regelaantal van het bestand |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik heb niets kunnen zien of spelen. Dit zijn vermoedens uit de tekst.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Het vak zegt nu alleen "Print this first". De uitleg "vijf spelingen van 0,10 tot 0,30 mm" staat alleen in de knoptip. Een nieuwe koper ziet dus niet wat de knop doet. | Een korte tweede regel onder de kop, bijvoorbeeld "5 clearances, 0.10 to 0.30 mm", als die in de smalle zijbalk past. | klein |
| 2 | Lukt één staaf niet, dan staat er een getal bij "Missing" in de melding. De koper krijgt dan een onvolledige set. | Bij "Missing" zeggen wat te doen, bijvoorbeeld "klik nog een keer". | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Bevestig met een groene betaalde run op 4.2.23 en 5.2.3 dat de rode strip weg is (A2). Zonder die run is dit een vermoeden.
- Voeg een test toe voor het herkansingspad (A5).
- Zoek de echte oorzaak van de weigering in 4.2.23 in meters (A3).
- Maak de architectuurtekst eenduidig: vier pogingen in totaal (B3).
- Zet een korte uitleg in het vak "Print this first" (C1) en een tip bij "Missing" (C2).

---
Automatische keurder, model `claude-sonnet-5-5`, 22952 tokens in, 3654 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
