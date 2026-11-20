# Nakeuring gat na hol-niveau (volgorde), 20 nov 2026, Daan
Wat ik keurde: tak `claude/steam-hol-niveau-gat`, commit 857faa8 (Olaf), alleen moet 1 uit mijn keuring van 47b9fa3 (`2026-11-20-niveau-gat-47b9fa3-daan.md`)
Akkoord: ja, geen moets

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Volgorde klopt: log 4242 r. 40 tot 48 toont valregel 74,5 ("Joost came back. The Spike Pit won. +9"), dan "Level 2" op 77,1, held Bram op 80,6 | feit (log gelezen) | hoog | Windows-run op de tak |
| 2 | `faam_erbij` zegt zelf niets meer en geeft de niveaus terug; `niveau_na` staat in `held_klaar` direct na `s._kroniek(r + extra)`. Tussen die twee geen `return`, dus geen niveau dat wegvalt | feit (code) | hoog | |
| 3 | Na weg zijn (`opslag.gd` r. 138, zonder `live`) en in de demo blijft de lijst leeg, dus niets extra; toetsen 4 en 5 dekken dat | feit (code) | hoog | |
| 4 | Held blijft op uiterlijk +6 s na het niveau (niet na de niveauregel): niveauregel staat zo ±3,5 s. Goed genoeg | feit (log) | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Bestaande niveau-toetsen roepen nu `niveau_na(faam_erbij(...))` aan; de controles zelf (wat er moet gebeuren) zijn gelijk, er is één nieuwe toets voor de volgorde bij. Dat is aanpassen aan de nieuwe aanroep, geen toets losser maken | feit | hoog | tests niet afzwakken |
| 2 | Kan 1 (rng-commentaar) staat erin; `architectuur.md` bijgewerkt | feit | hoog | architectuur bij |
| 3 | Nog op de tak, main blijft bevroren tot na de speeltest | feit | hoog | besluit speeltest |

## Deel C: zou een speler het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Nu eerst de vangst met +9, dan het nieuwe niveau: oorzaak en gevolg in de goede volgorde, het bordje wipt mee | niets | |
| 2 | Kan 2 uit de vorige keuring blijft: varianten van de niveauzin van Thijs na de speeltest | | klein |

## Moet / Kan
- Geen moets. Na de speeltest mag dit naar main (Olaf, met groene Windows-run op de tak).
