# Keuring Report a problem (obsidian-rollwright, R5), 19-11-2026, automatische keurder
Wat ik keurde: commit eb02ba15 (281d0a3..eb02ba1), bestanden onder producten/obsidian-rollwright/
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het commando "Report a problem" is geregistreerd in `main.ts` en opent met `activeWindow.open` een link naar `thijsduinhouwer2002-coder/rollwright/issues/new`. | Feit | Hoog | Staat in de diff. |
| 2 | De link bevat `version`, `obsidian`, `os` en een `body` met dezelfde drie regels. De test controleert dat, ook dat `template=` ontbreekt en dat de link onder 2000 tekens blijft. | Feit | Hoog | Staat in `report-problem.test.ts`. |
| 3 | De ontwerpkeuze (c) klopt met de code. Zonder formulier in de loketrepo vult de `body` alles in. GitHub negeert dan de losse velden. | Vermoeden | Midden | Een klik op de link in de echte Obsidian en het geopende GitHub-scherm. |
| 4 | De opdracht eist ook dat vitest, lint, scanner-lint en e2e groen zijn. Dat zie ik niet in de tekst. | Vermoeden | Laag | Groene runs voor eb02ba15 (vitest, lint, scanner-lint, e2e). |
| 5 | De commitkop noemt ook meldknoppen in Bison & Flex en Click Joints, een error handler, meldformulieren en een loket-workflow. In deze diff staat daar niets van. De opdracht voor Rollwright vraagt er ook niet om. | Feit | Hoog | De diffs van de andere producten en van `.github/` bekijken. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `plugin.test.ts` is aangepast: de lijst met commando's heeft er één bij. Dat past bij de nieuwe functie en verzwakt geen test. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `architectuur.md` beschrijft `report-problem.ts` en de nieuwe `Platform` in de stub. `CHANGELOG.md` en `ontwerp.md` zijn ook bijgewerkt. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Er gaat alleen besturingssysteem, desktop of mobiel en de versies mee. Geen gebruikersnaam of pad, en er wordt niets vanzelf verstuurd. In de diff staan geen sleutels of wachtwoorden. | Feit | Hoog | Geen persoonsgegevens |
| 4 | Het nieuwe bestand is 57 regels. `main.ts` kreeg 6 regels erbij, maar zijn totaal zie ik niet. Op 8 nov was het 412 en is het toen gesplitst. | Vermoeden | Midden | Bestanden onder ±400 regels. `wc -l src/main.ts` bevestigt het. |
| 5 | Er is geen cijfer, spelerstekst van Hats of AI-beeld of -geluid in deze wijziging. | Feit | Hoog | Cijfers en Steam-regels |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer `main.ts` op ±400 regels en bevestig dat de groene runs bij eb02ba15 horen (A4, B4).
- In `tests/obsidian-stub.ts` is `apiVersion` een object, in echt Obsidian een tekst. `reportUrlHere` geeft in de test dus "[object Object]" als Obsidian-versie. De test kijkt daar niet naar. Maak de stub een tekst of test het veld `obsidian`.
- De opdracht zelf (de `callback` met `activeWindow.open`) wordt niet getest. Een kleine test met een nep-`activeWindow` volstaat.
- Het formulier in de loketrepo moet de veld-ids `version`, `obsidian` en `os` krijgen, anders vult alleen de `body`. Test na het aanmaken één keer met een echte klik.
- Het akkoord van Daan bovenaan `ontwerp.md` gaat over 0.3.5 en blijft zo. Deze functie staat onder "Unreleased". Laat Daan haar bekijken als de instellingen later een knop krijgen.

---
Automatische keurder, model `claude-sonnet-5-5`, 24876 tokens in, 3138 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
