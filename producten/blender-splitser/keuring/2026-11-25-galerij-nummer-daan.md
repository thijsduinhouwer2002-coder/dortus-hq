# Keuring Daan: galerijbeeld Click Cuts "Numbered for assembly" (issue #40, 25 nov 2026)

Gekeurd: `ontwerp/cuts-galerij/beelden/nummer-2400x1200.jpg` en `nummer-1920x1080.jpg`, ook verkleind tot 600 px.
Naast: Cleave "Connectors that fit" (beste galerijbeeld uit de lat, met curl opgehaald en naast elkaar bekeken).

**Akkoord: ja**

## Deel A: klopt het met 1.0.0 (GEZIEN in de code)
| Bewering | Klopt? | Waar |
|---|---|---|
| pengaten op de snijvlakken | ja | `verbind_3d.py` plan_alles |
| gegraveerd nummer 7-11 (stuk-buur) | ja, per eiland; daarom staat 7-11 ook op het snijvlak van het been | `verbind_3d.py` r. 156-166, `nummer.json` |
| 5 mm pennen | ja, standaard `pen_mm` 5.0 | `eigenschappen.py` |
| 0.2 mm clearance | ja voor dit beeld (`speling_mm` 0.2 in `nummer.json`) | |
| gouden pennen | de add-on maakt zelf een object "Pins" (goud bij kleuren per stuk); in beeld alleen in de gaten gezet | `splitsen.py` r. 387 |

## Deel C: is het goed genoeg?
| Vraag | Cijfer | Waarom |
|---|---|---|
| Top, op niveau van de beste? | 8 | Rustig, groot nummer 7-11 leest nog op 600 px. Cleave is duidelijker (9 verbinders op kubussen), maar wij tonen iets wat niemand heeft op een echt model. Blinde test plek 2,0 en 2,0 (GEZIEN). |
| Zou ik kopen op basis hiervan? | 8 | Het nummer lost een echte ergernis op (welk stuk hoort waar). |
| Zou Thijs trots zijn? | 8 | Ja, schoon en eerlijk (render, geen printclaim). |

## Kan (volgende versie, niet blokkerend)
1. Stuk 11 zwevend boven de pennen, met zijn eigen 11-7: dan zie je "past op elkaar" in plaats van het te lezen. Beide rechters vroegen erom.
2. Het gebogen been links leest op 600 px als een losse buis; iets meer van de borst of een andere hoek maakt het paard herkenbaarder.
3. "part 7 meets part 11" staat twee keer (onderschrift en wijzer); de wijzer kan alleen "5 mm pins, 0.2 mm clearance" dragen.
