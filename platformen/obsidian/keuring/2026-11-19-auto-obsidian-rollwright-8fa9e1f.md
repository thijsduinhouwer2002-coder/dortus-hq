# Keuring Rollwright R5 kan-punten (report-problem), 19-11-2026, automatische keurder
Wat ik keurde: commits 10a21ea..8fa9e1f6 (`src/ui/report-problem.ts`, `tests/obsidian-stub.ts`, `tests/report-problem.test.ts`)
Akkoord: ja

## Deel A: doet het wat beloofd is?
Opdracht: de commitboodschap (kan-punten van de vorige keuring) en de Unreleased-regel in CHANGELOG over "Report a problem".

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `reportUrlHere` zet `apiVersion` nu met `String(...)` om. In Obsidian is `apiVersion` al een tekst, dus voor gebruikers verandert er niets. | Feit | Hoog | Staat zo in de diff. |
| 2 | De stub geeft `apiVersion` nu een `toString()`, en de test controleert dat `obsidian` "1.7.2" is en `version` "0.3.6". Daarmee wordt de Obsidian-versie in de link echt getest. | Feit | Hoog | Staat zo in de diff. |
| 3 | De boodschap noemt "privacyzin in de formulieren". Daar zit niets van in de gewijzigde bestanden. | Feit (niet meegestuurd) | Hoog | Een issue-template of formulier in een ander commit of pad. Dat is hier niet te zien. |
| 4 | De boodschap noemt "test gebruikersnaam robuuster". De diff laat geen test op een gebruikersnaam zien. | Vermoeden | Midden | Een controle in `report-problem.test.ts` dat de link geen gebruikersnaam bevat, buiten de getoonde regels. |
| 5 | Of de tests slagen is niet te zien, er is geen testlog meegestuurd. De logica is klein en lijkt te kloppen. | Vermoeden | Midden | Een groene testrun of CI-log op 8fa9e1f6. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is strenger gemaakt (twee controles erbij), niet versoepeld. De stubwijziging maakt de code niet makkelijker te laten slagen. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Er is geen nieuw bestand en geen taakverschuiving. `architectuur.md` beschrijft `report-problem.ts` en de stub al, dus bijwerken is niet nodig. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | De wijziging is een paar regels. Of de bestanden onder de 400 regels blijven is niet te zien. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Alleen "1.7.2", "0.3.6" en "Linux (desktop)" als testwaarden. | Feit | Hoog | Geen persoonsgegevens |
| 5 | Er zijn geen cijfers, spelerstekst of AI-beeld en -geluid in de wijziging. | Feit | Hoog | Cijfers, Hats, Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Maak de commitboodschap eerlijk: de privacyzin in de formulieren en de gebruikersnaamtest staan niet in deze commit. Laat zien in welke commit ze zitten, of voeg ze toe.
- Voeg een test toe die bevestigt dat de link geen gebruikersnaam of pad bevat (Deel A 4).
- Bij de volgende release (0.3.6) hoort het nieuwe commando een ontwerp-akkoord van Daan in `ontwerp.md`. Het zichtbare deel van `ontwerp.md` noemt het niet, maar de tekst is afgekapt.

---
Automatische keurder, model `claude-sonnet-5-5`, 19150 tokens in, 2696 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
