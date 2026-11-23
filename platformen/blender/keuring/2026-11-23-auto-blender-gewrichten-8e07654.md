# Keuring blender-gewrichten architectuur (volgende plek bij Figure from rig), 23-11-2026, automatische keurder
Wat ik keurde: commit 8e07654fc (alleen `producten/blender-gewrichten/architectuur.md`, één nieuwe regel)
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is alleen tekst in de architectuur. De goedgekeurde uitgaven (gratis 0.1.1, Pro 1.0.2) veranderen niet, want de beschreven functie hoort bij Pro 1.1. | Feit | hoog | De bestandslijst bevat alleen `architectuur.md`. |
| 2 | De regel beschrijft dat de knop na "too close", "no watertight parts" of (alleen scharnier) "too thin"/"tight" de volgende plek probeert en bij andere meldingen stopt. Of de code dat echt doet, kan ik niet zien. | Vermoeden | midden | De wijziging in `betaald/rig.py` en `e2e/toetsen_mens.py`, en een groene run met `CJ_HERKANS=1`. |
| 3 | De beweringen "CI 8 gewrichten, lokaal 9" en "ook met 1 of 2 threads" staan als GEZIEN. In de tekst is er geen log of run-id om dat na te gaan. | Vermoeden | midden | Een run-id of loguitvoer van beide metingen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `architectuur.md` is bijgewerkt voor deze functie en noemt de toets. | Feit | hoog | architectuur.md bijgewerkt |
| 2 | De commit bevat alleen de documentatie. De code en de toets waar de regel naar verwijst zitten niet in dit bereik. Ze moeten dus eerder zijn gekomen, of ze komen nog. | Vermoeden | midden | Doc en code horen bij elkaar te blijven |
| 3 | Er zijn geen tests aangepast en er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | hoog | Tests niet aangepast om te slagen, geen persoonsgegevens |
| 4 | De cijfers dragen het label GEZIEN met datum en Blenderversie. | Feit | hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 5 | De nieuwe regel is erg lang, en het bestand lijkt al ruim boven ±400 regels te zitten. Dat laatste kan ik niet tellen, want het bestand is afgekapt. | Vermoeden | laag | Een regeltelling van `architectuur.md` (bestanden onder ±400 regels) |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen, dus hier geen oordeel op plezier of beeld. | Iris en Daan keuren Pro 1.1 apart zodra er schermen zijn. | klein |
| 2 | Door het zoeken naar de volgende plek kan een rig per machine een ander aantal gewrichten krijgen (8 tegen 9). Een koper kan dat als willekeurig ervaren. | Laat het paneel kort melden welke plek is gebruikt. Zoek ook uit waarom "no watertight parts" per machine verschilt. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet bij de bewering over 8 en 9 gewrichten een run-id, zodat ze naspeurbaar is.
- Zoek de oorzaak van de wisselende snede ("no watertight parts") en laat het herkansen niet de enige oplossing zijn.
- Splits de lange regels in `architectuur.md` of het hele bestand in kleinere delen.
- Keur de bijbehorende code en toets (`rig.py`, `toetsen_mens.py`) zodra ze in een commit staan. Vandaag is alleen de tekst gekeurd, niet het gedrag.

---
Automatische keurder, model `claude-sonnet-5-5`, 20198 tokens in, 2502 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
