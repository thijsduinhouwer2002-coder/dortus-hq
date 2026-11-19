# Keuring Bison & Flex, beeldvergelijking R4, 19-11-2026, automatische keurder
Wat ik keurde: commit faf3effd (510aa24..faf3eff), bestanden `architectuur.md`, `e2e/.../Gedeeld.kt` en `e2e/.../Hernoemen.kt`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen e2e-testcode en documentatie. Plugin-code, winkeltekst en de belofte in `plugin.xml` blijven gelijk. | Feit | hoog | Een diff van `src/main` en `plugin.xml` over dezelfde reeks die leeg is. |
| 2 | Daans `Akkoord: ja` geldt tot en met 281d0a3. De meldknop en error handler uit `CHANGELOG.md` (Unreleased) zijn nog niet door hem gekeurd. Deze wijziging brengt die niet naar buiten. | Feit | hoog | Daans keuring van eb02ba1 vóór de volgende release. |
| 3 | `schermStil` wacht tot twee opnamen na elkaar gelijk zijn (300 ms ertussen, hooguit 4 of 10 keer), zodat de hernoem-plaatjes stabieler worden. De logica klopt zoals ze er staat. | Vermoeden | midden | Twee push-runs op dezelfde code zonder grote beeldverschillen op `*-hernoem-structuur` en `*-hernoem-conflict`. |
| 4 | `import -window <id> rgb:<pad>` krijgt hetzelfde venster-id als `scherm()`. Of dat id en die uitvoer werken op de CI-runner kan ik uit de tekst niet halen. | Vermoeden | midden | In het e2e-log de regel `DORTUS-E2E ...: beeld stil na N opnamen`. Staat daar steeds "niet stil" of een lege opname, dan werkt het niet. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen asserts of verwachtingen aangepast. De bestaande `assertTrue` en de verwachte hint-tekst blijven staan. Alleen het moment van de schermopname is veranderd. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | In `architectuur.md` zijn de runnummers en het label GEZIEN bij de twee overgebleven grote plaatjes weggehaald. De cijfers "0,34 tot 1,56 procent" en "0,3 procent" hebben nu geen label. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | De tekst noemt `beeldvergelijk.py`, maskers alleen op 2880x1800, vergelijking met verschuiving, `if: false` op de job `beeldbericht` en `l1` alleen kloktijden. Geen van die bestanden zit in deze wijziging. Misschien staan ze in een eerdere commit, maar uit de tekst kan ik dat niet bevestigen. | Vermoeden | midden | Architectuur.md klopt met de code |
| 4 | Het nieuwe KDoc van `schermStil` staat tussen het oude KDoc van `scherm()` en die functie in. Het oude commentaar ("alleen het actieve venster") hangt nu los en hoort niet meer bij `scherm()`. | Feit | hoog | Duidelijke code (klein) |
| 5 | Het commitbericht noemt een bericht aan de hoofdchat over de Pro-zip. Dat bestand zit niet in deze wijziging. Ik zie in de tekst geen persoonsgegevens, sleutels of wachtwoorden. | Feit | hoog | Geen persoonsgegevens |
| 6 | De regelaantallen van `architectuur.md`, `Gedeeld.kt` en `Hernoemen.kt` zijn uit de tekst niet te zien. De alinea over de beeldvergelijking in `architectuur.md` wordt wel steeds langer. | Vermoeden | laag | Bestanden onder ±400 regels (`wc -l`) |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet het KDoc van `scherm()` terug direct boven `scherm()` en laat het nieuwe KDoc boven `schermStil` staan.
- Zet bij de ruiscijfers in `architectuur.md` weer GEZIEN met het runnummer, of verwijs naar `BEELDVERSCHIL.md`.
- Controleer dat de genoemde `beeldvergelijk.py`, `beelden.sh` en `if: false` in de workflow echt zo bestaan, en dat die in een eerdere commit van deze reeks zitten.
- Controleer met `wc -l` de bestandsgrootte van `architectuur.md` en de e2e-bestanden.
- Laat het stilstaan-effect van `schermStil` bevestigen door het e2e-log van twee runs.

---
Automatische keurder, model `claude-sonnet-5-5`, 22537 tokens in, 4034 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
