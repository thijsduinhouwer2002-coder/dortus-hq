# Keuring Bison & Flex week-test (roestronde R4), 19-11-2026, automatische keurder
Wat ik keurde: commits 64cb28b..49cd861 (49cd8613) op `producten/jetbrains-bison-flex/`: `build.gradle.kts`, `ClionTest.kt`, `IdeTest.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
Opdracht: de wijziging raakt alleen build en e2e-tests, niet de plugin zelf. Ik toets daarom tegen eis 1 en 11 van `ontwerp.md` en tegen de commitbeschrijving.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|-----------|--------------------------------------|
| 1 | Er is geen plugincode, `plugin.xml` of winkeltekst gewijzigd. De belofte en de eisen 2 tot en met 10 blijven dus onaangetast. | Feit | Hoog | De bestandenlijst bevat alleen `build.gradle.kts` en twee e2e-bestanden. |
| 2 | Zonder `-PideBuild` en `-PclionBuild` blijft het gedrag gelijk: IDEA Community 2025.2.6.4 met de oude thema-ids, en CLion build 263.7307.35. Eis 1 (IDEA Community en CLion) blijft dus bewaakt. | Feit | Hoog | Te zien in de diff: de terugvalwaarden en de oude `draai(...)`-aanroepen staan er nog. |
| 3 | De Islands-thema-ids ("Islands Light", "Islands Dark") en `useEAP(...)` in de Starter-API kan ik niet controleren. Ze zouden in de week-test kunnen falen op een thema- of API-fout in plaats van op een echte regressie. | Vermoeden | Midden | Een groene of rode week-test-run met IU EAP 253 of hoger, met thema's die in het log of op de schermen echt wisselen. |
| 4 | Het commitbericht noemt Blender alpha, nieuwste Obsidian en "beeldvergelijking in drie e2e's". Voor dit product zie ik alleen build-parameters en versiekeuze, geen beeldvergelijking. | Feit | Hoog | De rest van de commit hoort waarschijnlijk bij andere producten. Beeldvergelijking hier is niet te zien. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | Er zijn geen tests aangepast om te slagen. Er zijn geen verwachtingen of asserts gewijzigd, alleen de keuze van de IDE-build. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | `CLION_BUILD` is van `const val` naar `val` gegaan en is alleen in `ClionTest` zelf te zien. Gebruikt een ander bestand het als constante, bijvoorbeeld in een annotatie, dan breekt de compilatie. | Vermoeden | Laag | Een groene build van de e2e-bronnen. |
| 3 | De verifier-uitbreiding stopt met een duidelijke fout bij een onbekende IDE-code. Hij valt dus niet stil terug op iets anders. | Feit | Hoog | Geen stille uitzonderingen |
| 4 | `architectuur.md` en `CHANGELOG.md` zijn niet bijgewerkt. Dat is hier te verdedigen: er is geen gedrag van de plugin veranderd. Een korte regel over de week-testparameters had in de architectuur kunnen staan. | Feit | Midden | architectuur.md bijgewerkt |
| 5 | Het Akkoord van Daan (18 nov, voor 2026.1.2) blijft geldig, want er is niets zichtbaars gewijzigd. Er staan geen persoonsgegevens of sleutels in de diff. | Feit | Hoog | Akkoord Daan, geen persoonsgegevens |
| 6 | De bestandsgrootte (±400 regels) van `IdeTest.kt` en `ClionTest.kt` kan ik uit deze diff niet zien. | Vermoeden | Laag | Regelaantal van beide bestanden. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in de eerste week-test-run dat de Islands-thema-ids en `useEAP` werken, en schrijf de uitkomst in het log.
- Zet één regel over `-PideBuild`, `-PclionBuild` en `-PverifierExtra` in `architectuur.md`, zodat de week-test vindbaar is.
- Laat het commitbericht per product alleen noemen wat er in dat product veranderd is. De beeldvergelijking is hier niet te zien.
- Controleer dat de bestanden onder ±400 regels blijven.

---
Automatische keurder, model `claude-sonnet-5-5`, 20535 tokens in, 2702 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
