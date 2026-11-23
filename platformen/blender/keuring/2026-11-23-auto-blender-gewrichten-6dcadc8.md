# Keuring Figure from rig, extra kogelplek (blender-gewrichten), 23-11-2026, automatische keurder
Wat ik keurde: commits 6748111..6dcadc8 (6dcadc823 en 08d1637ab): `betaald/rig.py`, `architectuur.md`, `proeven/studio2-figuren-2026-11-23/uitslag.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `kogel_schuif` krijgt als laatste kandidaat dezelfde plek 0,3 mm verder het lid in. Hij komt dus alleen aan de beurt na een weigering, en een figuur waar het al lukte merkt niets. | Feit (diff) | hoog | Niet nodig. |
| 2 | De claim "robot CI 8 nu 9, lokaal 9" staat in de uitslag met runnummers (45206324187, 45208410893). De logs zitten niet in de wijziging. | Vermoeden | midden | Die twee runs in `organisatie/actions-logs/` openen en het aantal gewrichten per run nalezen. |
| 3 | De nieuwe regel gebruikt `t_vrij`, `u` en `lengte`. Alleen `t_vrij` staat niet in het zichtbare stuk van de diff. | Vermoeden | midden | Het groene CI-resultaat met 9 gewrichten laat zien dat dit niet crasht. Of de volledige `rig.py` lezen. |
| 4 | Dit is een omweg, geen oorzaak. De snede valt per processor anders uit en blijft een kapotte snede opleveren die de controles op gesloten delen doorstaat. De uitslag zegt dat zelf ook ("kopers met AMD of Intel krijgen vaker hetzelfde"). | Feit (uitslag.md) | hoog | Een controle direct na de snede op overlap in rust (0°) zou de oorzaak vangen. |
| 5 | Er is geen toets voor de nieuwe kandidaat. `CJ_HERKANS=1` dekt alleen de linkerschouder. | Feit (diff) | midden | Een toets die de eerste plek van de linkerheup kapot forceert en 9 gewrichten eist. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Er is ook geen test aangeraakt. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | `architectuur.md` is bijgewerkt met `kogel_schuif`, reden en runnummers. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | Of `rig.py` en `architectuur.md` onder ±400 regels blijven kan ik uit de diff niet halen. De architectuurregels zijn erg lang. | Vermoeden | laag | Bestanden onder ±400 regels (`wc -l` zou het bevestigen) |
| 4 | De cijfers in de uitslag staan als GEZIEN of GOK (processortype, "GOK: andere processor"). De kop "CI-meting loopt" is achterhaald door het stuk eronder. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | Ik zie geen persoonsgegevens, sleutels of wachtwoorden in de drie bestanden. | Feit | hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Een koper met een andere processor kreeg een heup minder, zonder te weten waarom. Dat is nu voor de robot opgelost, als de runs kloppen. | Niets nodig. | klein |
| 2 | De 0,3 mm verschuiving merkt een speler niet. Dat kan ik niet zien, het is een vermoeden. | Na afloop in het paneel tonen dat de plek is aangepast. | klein |
| 3 | De andere studio-figuren (Mike, Stan, George, Cyberpunk) zijn niet lokaal nagedaan. Mike's linkerelleboog lukt wel en de rechter niet, en dat is niet nagekeken. | Dezelfde proef op Mike draaien. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen.

Kan:
- Een toets voor de nieuwe laatste kandidaat (A5).
- Direct na elke snede een overlapcontrole in rust, zodat de oorzaak wordt gevangen en niet één omweg per figuur (A4).
- Regelaantal van `rig.py` en `architectuur.md` nakijken, en afsplitsen als ze boven ±400 komen (B3).
- Mike's linkerelleboog tegenover de rechter nakijken en de koptekst "CI-meting loopt" in de uitslag bijwerken (C3, B4).

---
Automatische keurder, model `claude-sonnet-5-5`, 22683 tokens in, 2933 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
