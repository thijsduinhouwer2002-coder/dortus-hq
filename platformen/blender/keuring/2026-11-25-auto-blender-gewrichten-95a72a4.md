# Keuring Pro 1.2.8 omhulsel H bij Exact, 25-11-2026, automatische keurder
Wat ik keurde: commits 08c4b03..95a72a4 (95a72a47c), bestanden `click_joints/betaald/omhulsel.py` en `architectuur.md`
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Met Exact (4.2) krijgt H nu hooguit ±30.000 vlakken (`MAX_VLAKKEN_EXACT`, voxel = wortel(oppervlak/30000), geen ondergrens m/2). Met Manifold blijft het gedrag gelijk. | Feit (uit de diff) | Hoog | n.v.t. |
| 2 | De beloofde geheugenwinst (15 GB naar ±2,5 GB) staat alleen als opmerking in de code, als "lokaal, GEZIEN". Er is geen run-id van een groene CI-run met de nieuwe grens. | Vermoeden | Midden | Een groene e2e-run in 4.2.23 met de Rigify-toets onder 6000 MB. |
| 3 | Een grovere H kan ertoe leiden dat de controle "lid binnen H, hooguit 2% erbuiten" faalt. Dan volgt "de oude weg", en die kan met Exact nog steeds veel geheugen vragen. Dat geval is niet beschreven of getoetst. | Vermoeden | Laag | Een toets of log waarin die terugval met Exact wordt doorlopen. |
| 4 | `from ..gewricht import solver_naam` staat vóór de if, dus hij draait bij elke aanroep van `voxel_h`, ook met Manifold. Of `solver_naam` in `gewricht.py` bestaat, kan ik niet zien. | Vermoeden | Laag | `grep solver_naam gewricht.py` en een groene run in 5.2.3 en 5.3.0. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Het commit en `architectuur.md` zeggen dat de Rigify-toets nu in een eigen e2e-stap draait na army_man en faalt boven 6000 MB. Er staat geen workflow- of toetsbestand in de wijziging. | Feit dat het niet in de diff staat; of het elders bestaat is vermoeden | Midden | Beschrijving moet kloppen met wat is ingeleverd |
| 2 | "Pro 1.2.8" staat in de commit, maar er is geen versieverhoging in het manifest of de changelog van de Pro-build in de wijziging. | Vermoeden (diff kan gefilterd zijn) | Laag | Versie en uitgave moeten kloppen |
| 3 | `architectuur.md` is bijgewerkt met de nieuwe grens, de reden en de meetwaarden (GEZIEN, lokaal). | Feit | Hoog | architectuur.md bijgewerkt: voldaan |
| 4 | Er zijn geen bestaande tests aangepast; er staan geen persoonsgegevens of sleutels in. De bestandslengte van `omhulsel.py` is uit de diff niet te zien. | Feit, behalve de lengte | Midden | Tests, privacy en ±400 regels |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Niets hiervan is te zien of te spelen. Voor een koper op 4.2 betekent het dat Figure from rig niet meer ±15 GB vraagt en dus niet vastloopt. De snelheid is gemeld als ±85 tot 122 s voor de toets. | Laat in de melding of het paneel zien dat het lang kan duren, en meet de tijd per gewricht op 4.2. | Klein |
| 2 | Een grovere H kan op 4.2 vaker een overgeslagen gewricht geven met de melding uit `redenen.py`. Dat is een vermoeden. | Toets het aantal geplaatste gewrichten op 4.2 voor en na de grens. | Midden |

## Deel C: is het goed genoeg?
Geen beeld, winkeltekst of spel in deze wijziging, dus geen blindtest of vergelijking met een concurrent mogelijk. De cijfers zijn niet te geven (n.v.t.) en tellen hier niet mee. Beeld en speelplezier keuren Daan en Iris.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Laat zien dat de e2e-stap met de geheugengrens van 6000 MB en de versie 1.2.8 echt zijn ingeleverd (workflow- of toetsbestand in de wijziging, of de commit waarin ze staan). Zo niet, haal de bewering uit `architectuur.md` of lever ze alsnog aan.
2. Voeg een run-id toe van een groene e2e in 4.2.23, 5.2.3 en 5.3.0 met de nieuwe grens. Het hele doel van de wijziging is dat CI niet meer 15 GB vraagt, en dat is nu alleen lokaal gezien.

**Kan**
- Toets of beschrijf wat er gebeurt als de controle "lid in H" faalt en de oude weg met Exact toch te veel geheugen vraagt.
- Controleer dat `solver_naam` bestaat en verplaats de import naar binnen de Exact-tak.
- Meet het aantal geplaatste gewrichten op 4.2 voor en na de grens van 30.000.

---
Automatische keurder, model `claude-sonnet-5-5`, 23787 tokens in, 4571 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
