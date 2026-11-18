# Keuring obsidian-rollwright, 19-11-2026, automatische keurder
Wat ik keurde: commits 3424f23..281d0a3 (281d0a3b), alleen `producten/obsidian-rollwright/architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|-----------|-------------------|-----------|--------------------------------------|
| 1 | De wijziging raakt alleen `architectuur.md`. `src/`, `styles.css` en `manifest.json` zijn niet veranderd. Het akkoord van Daan voor 0.3.5 (op code van main 465cca4) blijft daardoor van kracht en de speler merkt niets. | Feit | Hoog | De bestandenlijst bij deze keuring bevat alleen dit ene bestand. |
| 2 | Het commitbericht noemt ook maskers voor kluisnaam en melding, een verslag naast de schermen en een oorzaak voor Chris. Daarvan staat alleen de beschrijving van de maskers in deze wijziging, geen code of verslag. | Vermoeden | Midden | De commits van de maskers (`beelden.sh`, `wdio.conf.mjs`, `week-test.yml`) en het bericht aan Chris in `berichten/`. Die zitten dan buiten wat ik kreeg of in een eerdere commit. |
| 3 | De alinea beschrijft de week-test en de beeldvergelijking met een vast zaad, een grens van 0,4 procent en een verschilbeeld bij overschrijding. Dit raakt de speler niet. | Feit | Hoog | Niet van toepassing: het is interne documentatie. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|-----------|-------------------|-----------|-------|
| 1 | `architectuur.md` is bijgewerkt voor de nieuwe week-test en beeldvergelijking. De regel "werk dit bij als je iets toevoegt" is gevolgd. | Feit | Hoog | architectuur.md bijgewerkt |
| 2 | Het getal "0,36 procent" staat met GEZIEN 19 nov en "twee runs van dezelfde commit". Er staat geen run-id bij. | Feit dat de label er staat, vermoeden dat het klopt | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | De wijziging bevat geen persoonsgegevens, sleutels of wachtwoorden. Er is geen test aangepast. Geen AI-beeld of -geluid en geen spelerstekst. | Feit | Hoog | Geen persoonsgegevens, tests niet aangepast |
| 4 | De regelgrens van ±400 regels geldt voor bestanden. `architectuur.md` is een document en de toevoeging is één lange alinea. Ik kon de totale lengte niet zien. | Vermoeden | Laag | Bestanden onder ±400 regels |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- Zet bij "0,36 procent" de twee run-id's, zodat de GEZIEN-label na te lopen is. De marge tot de grens van 0,4 is klein.
- Splits de lange alinea in een paar korte punten. De zin over "één keer met de oudste en één keer met de nieuwste installer" is lastig te lezen.
- Controleer dat de code van de maskers, het verslag en het bericht aan Chris echt in main staan (punt A2). Dat kon ik uit deze tekst niet zien.

---
Automatische keurder, model `claude-sonnet-5-5`, 19361 tokens in, 2226 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
