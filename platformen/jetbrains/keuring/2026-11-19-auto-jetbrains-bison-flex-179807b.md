# Keuring Bison & Flex e2e CLion-scherm wacht op stilstand, 19-11-2026, automatische keurder
Wat ik keurde: commit 179807b2 (ClionTest.kt in producten/jetbrains-bison-flex/e2e/)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen de e2e-test van CLion. De winkelbelofte (kleuren, springen, meldingen) verandert niet, dus er is niets in het product te toetsen tegen de belofte. | Feit | hoog | Het diff bevat één regel code in een testbestand. |
| 2 | Het doel is eis 1 en eis 10 van het ontwerp: bewijs in CLion dat calc.y gekleurd wordt, vastgelegd in een schermafbeelding. De assert op de geheugenmeter staat er nog onveranderd. | Feit | hoog | De regels rond de wijziging in het diff. |
| 3 | Of `schermStil` bestaat en `pogingen` als parameter heeft, is uit dit diff niet te zien. Alleen ClionTest.kt is gewijzigd. Staat de functie niet elders in de e2e-map, dan compileert de test niet. | Vermoeden | midden | Een groene e2e-run op CLion, of de definitie van `schermStil` in een ander e2e-bestand. |
| 4 | Na 15 opnamen neemt de test het scherm "toch", ook als het beeld nog niet stil is. Een schermafbeelding met nog onvolledige kleuring kan dan alsnog langskomen en als bewijs voor eis 1 worden gebruikt. | Vermoeden | midden | Het beeld van een volgende run: is de kleuring van calc.y klaar? Of de uitvoer van de test als die de terugval gebruikt. |
| 5 | De commitberichttekst zegt "twee opdrachten voor drie runs (R4)". In het diff zit alleen de wijziging in het scherm van calc.y. Wat die twee opdrachten zijn, is niet te controleren. | Vermoeden | laag | Een volledig diff of de beschrijving van R4 in het berichtenbestand. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen assert verwijderd of afgezwakt. De wijziging verandert alleen wanneer het scherm wordt vastgelegd. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | architectuur.md is niet bijgewerkt. Dat is niet nodig, want er verandert niets in het product of de opbouw. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in het diff. Alleen een run-nummer in een commentaar. | Feit | hoog | Geen persoonsgegevens |
| 4 | Of ClionTest.kt onder de ±400 regels blijft, is niet te zien. De wijziging zit rond regel 222, dus het bestand is minstens zo lang. | Vermoeden | laag | Het regelaantal van het bestand |
| 5 | Er zijn geen cijfers, spelerstekst of AI-beeld of -geluid in de wijziging. | Feit | hoog | Cijfers GEZIEN/DERDEN/GOK, geen AI-beeld op Steam |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer of `schermStil` bestaat met een parameter `pogingen`. Een groene e2e-run op CLion bevestigt dat (A3).
- Laat de test iets in het log zetten als de 15 opnamen op zijn en het scherm toch is genomen. Dan weet je dat het beeld niet gegarandeerd stil was (A4).
- Controleer na de volgende run met de Read-tool dat de kleuring van calc.y op het beeld klaar is. Alleen de tekst lezen is daarvoor geen bewijs.
- Laat het bericht bij een volgende commit duidelijk zeggen welke "twee opdrachten" bedoeld zijn (A5).

---
Automatische keurder, model `claude-sonnet-5-5`, 18147 tokens in, 2180 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
