# Keuring herkansing Exact bij vaste kogel (proef A4), 23-11-2026, automatische keurder
Wat ik keurde: commit 0ea250f46 (kogel_exact.py, betaald/rig.py, e2e/toetsen_mens.py)
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Het doel is: zit een kogel na een Manifold-snede vast, dan dezelfde plek opnieuw met Exact snijden. Volgens het commitbericht en de docstring lukt dat op MakeHuman niet: Exact geeft daar op geen enkele plek gesloten delen (schouder 8 van 8, heup 11 van 11). | Feit (door de bouwer gemeld, lokaal Blender 5.3.0), niet door mij te controleren | Midden | Het log van de toets met `CJ_HERKANS=3` en de regels "no watertight parts". |
| 2 | De herkansing herstelt dus niets op de figuur waarvoor hij bedoeld is. De commit noemt zichzelf rood en "niet voor main". | Feit | Hoog | Een groene run van `toetsen_mens.py` met `CJ_HERKANS=3`. |
| 3 | De toets laat elke Manifold-snede op het doelgewricht met opzet "vast" lijken (`vast_nep3`). Het echte AMD-gedrag (delen die in rust overlappen) is dus niet getoetst. | Feit | Hoog | Een run op een AMD-runner zonder nep, met de gemeten beweegproef van 0° en daarna de herkansing. |
| 4 | De oorzaak "rekenfout per processor bij Manifold op AMD" is een aanname uit het spoor van Olaf. Bewezen is hij niet. | Vermoeden | Laag | Dezelfde snede op dezelfde figuur op AMD en Intel, met de volledige meshvergelijking. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `kogel_exact.py` zet `EXACT_ZELF = True`. Het ontwerp (afwijking Exact) zegt dat Self Intersection aan aantoonbaar open delen geeft en 26 tot 27 keer zo traag is, en dat het daarom uit staat. | Feit | Hoog | Ontwerp en code moeten kloppen. Als dit toch zo moet, moet het ontwerp met een reden worden aangepast. |
| 2 | `architectuur.md` is niet bijgewerkt voor de nieuwe module en de nieuwe stap in `figuur_uit_rig`. | Feit | Hoog | architectuur.md bijgewerkt. Voor een proef buiten main is dit een kan, voor main een moet. |
| 3 | `rig.py` is al groot (de wijziging zit rond regel 727) en wordt groter. De lengte kan ik uit de diff niet zien. | Vermoeden | Midden | Bestanden onder ±400 regels. `wc -l` op `betaald/rig.py` bevestigt of weerlegt dit. |
| 4 | De tests zijn niet verzwakt. Er is een nieuwe toets (`CJ_HERKANS=3`) bij gekomen die eerlijk rood blijft, en het terugzetten van de nepfuncties staat nu in `finally`. | Feit | Hoog | Tests niet aangepast om te slagen: in orde. |
| 5 | De cijfers (8 van 8, 11 van 11) staan met bron en omstandigheid in de docstring (lokaal, GEZIEN). Persoonsgegevens, sleutels of wachtwoorden zie ik niet. | Feit | Hoog | In orde. |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alleen uit tekst te schatten, niets gezien of gespeeld)
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een Exact-snede met Self Intersection aan kan voor de gebruiker minuten duren (op 261K driehoeken 87 s, zie het ontwerp). Daarna mislukt hij op MakeHuman toch en gaat de zoektocht door naar de volgende plek. Dat is wachten zonder resultaat. | Alleen herkansen als Exact aantoonbaar gesloten delen geeft, en anders meteen naar de volgende plek. Of een tijdgrens met een duidelijke melding. | Midden |
| 2 | Bij een mislukte herkansing ziet de gebruiker een algemene "geblokkeerd" en weet niet waarom. | Een korte melding in het paneel: "Cut stuck, tried another solver". | Klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. De herkansing werkt niet op de figuur waarvoor hij bedoeld is (zie A1 en A2) en de bouwer markeert hem zelf als rood. Zo niet naar main. Haal de aanroep in `rig.py` uit het pad naar main, of laat hem pas toe nadat een groene run laat zien dat hij werkt.
2. `EXACT_ZELF = True` gaat in tegen het vastgelegde besluit in het ontwerp (B1). Zet het terug op uit, of onderbouw met een meting waarom het toch moet en pas het ontwerp aan.

**Kan**
- Een toets zonder nep op een AMD-runner, zodat de oorzaak echt bewezen wordt (A3, A4).
- `architectuur.md` bijwerken en de lengte van `rig.py` nakijken (B2, B3).
- Een duidelijke melding bij een mislukte herkansing (C2).

---
Automatische keurder, model `claude-sonnet-5-5`, 20835 tokens in, 3681 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
