# Keuring beeldvergelijking R4 (Bison & Flex e2e), 19-11-2026, automatische keurder
Wat ik keurde: commit 7f492ff2 (417f1b3..7f492ff), bestanden `architectuur.md` en `e2e/.../Gedeeld.kt` van jetbrains-bison-flex
Akkoord: ja

## Deel A: doet het wat beloofd is?
(Het ontwerp zegt niets over de beeldvergelijking. Ik toets tegen de belofte in de commitmelding en de architectuurtekst, en kijk of de plugin zelf verandert.)

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De plugin, de winkeltekst en het zichtbare gedrag veranderen niet. Alleen testhulpcode (`winkelproject()`) en documentatie zijn aangeraakt. De akkoord-ja van Daan (tot en met 281d0a3) blijft dus ongemoeid. | Feit | Hoog | Het diff bevat geen bestand onder `src/main`. |
| 2 | `winkelproject()` maakt nu een vaste map `<tmp>/<voorvoegsel>/calculator` in plaats van een willekeurige. Dat past bij de bedoeling: geen wisselende mapnaam in de projectboom en op de projectknop. | Feit | Hoog | Te zien in het diff. |
| 3 | Of het vals alarm echt weg is, kan ik niet zien. De commitmelding noemt ook maskers, LEEG-detectie, één bericht per run en het week-bericht, maar daarvan staat niets in het diff. | Vermoeden | Midden | Een e2e-run op main waarvan het beeldverschil onder 0,3 procent blijft, en het script `organisatie/controle/beelden.sh` met de maskers erin. |
| 4 | De map wordt eerst leeggemaakt en daarna aangemaakt. Gebruiken twee tests hetzelfde voorvoegsel, of staat de map nog open in een draaiende IDE, dan kunnen ze elkaar in de weg zitten. | Vermoeden | Laag | Een grep naar alle aanroepen van `winkelproject(` met hun voorvoegsels, en een groene e2e-run. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt en legt uit waarom de map vast is. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Er is geen test aangepast om te slagen. Alleen een hulpfunctie voor de e2e-opzet is veranderd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 3 | De tekst beschrijft maskers, GEMELD.md, de job `beeldbericht` en LEEG als bestaand gedrag. Die code staat niet in dit diff. Waarschijnlijk zit ze in bestanden buiten het productmap (workflow, `beelden.sh`) die niet zijn meegestuurd. Is dat niet zo, dan loopt de documentatie voor op de code. | Vermoeden | Midden | architectuur.md klopt met de code |
| 4 | De ruiscijfers (0,34 tot 1,56 procent) staan er zonder GEZIEN, DERDEN of GOK. De bron is wel genoemd (keuring R4, 19 nov). | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden in het diff. Bestandslengte van `architectuur.md` en `Gedeeld.kt` kan ik uit het diff niet halen. | Feit, lengte onbekend | Midden | Geen persoonsgegevens, bestanden onder ±400 regels |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Controleer dat `beelden.sh`, `week-test.yml` en het masker echt in deze commit of een eerdere zitten, zodat `architectuur.md` niet vooruitloopt op de code (B3, A3).
- Zet GEZIEN voor de ruiscijfers en noem de run waaruit ze komen (B4).
- Controleer dat geen twee e2e-tests hetzelfde voorvoegsel voor `winkelproject()` gebruiken (A4).
- Kijk bij de volgende main-run of het beeldverschil echt onder de 0,3 procent blijft (A3).

---
Automatische keurder, model `claude-sonnet-5-5`, 20378 tokens in, 2972 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
