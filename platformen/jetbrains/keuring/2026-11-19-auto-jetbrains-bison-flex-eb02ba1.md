# Keuring meldknop, error handler en meldformulieren, 19-11-2026, automatische keurder
Wat ik keurde: commit eb02ba15 (bereik 281d0a3..eb02ba1), product jetbrains-bison-flex
Akkoord: ja

## Deel A: doet het wat beloofd is?
Getoetst tegen het ontwerpblok "Ontwerp meldregel en error handler (R5)" in `ontwerp.md`. Ik kan niets draaien, dus alles hieronder komt uit de tekst.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De actie `BisonFlex.ReportProblem` staat in `plugin.xml` onderaan `HelpMenu`, met tekst in Title Case. `Melden.url` zet versie, IDE en OS in de velden en in de `body`, en `urlHier()` leest ze uit de IDE. | Feit | Hoog | Meegestuurde code en `MeldenTest` |
| 2 | De error handler `JetBrainsMarketplaceErrorReportSubmitter` staat in `plugin.xml`, zoals het ontwerp zegt. | Feit | Hoog | Het diff-fragment van `plugin.xml` |
| 3 | De uitkomst "GEZIEN groen lokaal, 4 van 4" in `architectuur.md` is de eigen uitspraak van de bouwer. De bewijsstukken ontbreken: de unittests in de CI, de IDE-test en de Plugin Verifier, die de eis "blijven groen" vraagt. | Vermoeden | Midden | Groene CI-run op deze commit, `verifyPlugin` voor 2025.3, 2026.2 en CLion |
| 4 | Het ontwerp zegt dat de veld-ids het formulier vullen zodra het in de loketrepo staat. Ik vermoed dat GitHub velden van een issueformulier alleen invult met `template=`. Zonder `template=` gebruikt de link vermoedelijk alleen `body`, en kan GitHub bij meerdere sjablonen eerst de keuzepagina tonen. De eis ("opent een melding met versies ingevuld") wordt wel gehaald via `body`. | Vermoeden | Midden | Een echte klik op de link, vóór en na het zetten van `bug.yml` in de loketrepo |
| 5 | Het nieuwe menu-item en de foutdialoog zijn nieuw zichtbaar werk. Er is geen scherm van, en Daans `Akkoord: ja` (18 nov) geldt voor 2026.1.2 zonder dit. | Feit | Hoog | Een IDE-testscherm van Help met het item, en een oordeel van Daan vóór de release |
| 6 | `config.yml` zegt dat het contactadres op `dortus.com/bison-flex/` staat. Uit de tekst is niet te zien of dat klopt. | Vermoeden | Laag | `curl` op die pagina |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen nieuwe tests erbij (`MeldenTest`), geen bestaande test aangepast. `Melden.kt` is 77 regels en `MeldenTest` 64. | Feit | Hoog | Tests niet aangepast om te slagen; bestanden onder ±400 regels |
| 2 | `architectuur.md` is bijgewerkt voor `Melden`, de error handler, de loketmap en `MeldenTest`. Het blijft deels verouderd ("versie 0.2", "versie 2026.1.1" bij `plugin.xml`). Dat was al zo. | Feit | Hoog | architectuur.md bijgewerkt |
| 3 | Het hard ingebouwde loket-adres in `Melden.kt` en `MeldenTest.kt` bevat een persoonsnaam in de accountnaam. Dat gaat in het openbare pluginpakket mee. Ik schrijf het adres hier niet over. | Feit | Hoog | Geen persoonsgegevens |
| 4 | De URL bevat OS-naam, versie en architectuur, maar geen gebruikersnaam of pad. Er is geen telemetrie, de gebruiker opent de link zelf. | Feit | Hoog | Geen persoonsgegevens |
| 5 | `testUrlHierHeeftEchteGegevens` controleert dat `user.name` niet in de OS-tekst staat. Bij een korte gebruikersnaam, zoals "a", kan die test onterecht falen. | Vermoeden | Midden | Tests moeten betrouwbaar zijn |
| 6 | `bug.yml` vraagt om een stacktrace in een openbaar loket. Het ontwerp noemt zelf dat dit openbaar wordt, maar het formulier waarschuwt er alleen voor privécode, niet voor paden of gebruikersnaam in een stacktrace. | Feit | Midden | Geen persoonsgegevens |
| 7 | De ontwerpbeslissing (a), (b), (c) is met GOK gemarkeerd. De formulierchecks hebben GEZIEN en DERDEN. Er is geen AI-beeld of -geluid en geen spelerstekst. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Draai de CI, de IDE-test en de Plugin Verifier op deze commit en noteer het resultaat bij de commit (A3).
2. Test met een echte klik wat GitHub doet zonder `template=`, met en zonder formulier in de loketrepo. Zet het in `ontwerp.md` als GEZIEN of GOK, en maak anders de zin "dezelfde ids vullen de velden" zwakker (A4).
3. Vraag Daan vóór de release om het nieuwe Help-item en de foutdialoog te bekijken, met een scherm erbij (A5).
4. Beslis of een persoonlijke accountnaam in de openbare plugin gewenst is. Een bedrijfsaccount of orgrepo is netter (B3).
5. Maak de test op `user.name` robuuster, bijvoorbeeld alleen controleren als de naam minstens 4 tekens heeft of een pad bevat (B5).
6. Zet in `bug.yml` een waarschuwing dat een stacktrace openbaar komt en geen paden met persoonsnamen mag bevatten (B6). Controleer het contactadres op de pagina in `config.yml` (A6).

---
Automatische keurder, model `claude-sonnet-5-5`, 29735 tokens in, 5870 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
