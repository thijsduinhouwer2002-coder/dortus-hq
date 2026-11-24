# Keuring blender-gewrichten Pro 1.2.5 (afstandsregel en enkels), 24-11-2026, automatische keurder
Wat ik keurde: commit 75d82bc72 (f966831..75d82bc), bestanden `betaald/scharnier_vorm.py` en `e2e/toetsen_mens.py`
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De regel is nu `min(2*max(r, eigen), r+eigen+1 mm)`. Dat is nooit strenger dan 2 keer de grootste reik. De opdracht "nooit strenger dan voorheen" klopt dus als de oude regel precies 2*max(r, eigen) was. | Feit voor de formule, vermoeden voor "voorheen" | midden | De oude regel (commit voor de PROEF-regel) laten zien in dezelfde eenheden. |
| 2 | De bewering "tussen knie en enkel blijft ±20 mm scheen met de oorspronkelijke doorsnede over" staat alleen in een commentaar. Het is gemeten op één lichaam (MakeHuman 220 mm, 5.3.0). Een log of run ontbreekt. | Vermoeden | midden | Een groene run met `CJ_MEER=1`, op meer dan één rig (robot én MakeHuman) en in 4.2 en 5.2. |
| 3 | Het commentaar noemt MakeHuman eerst 150 mm en dan 220 mm hoog. De 35 mm tussen knie en enkel hoort bij 150 mm. De meting op 220 mm is dus een andere schaal. | Feit | hoog | Meting op dezelfde schaal als de afstand van 35 mm. |
| 4 | De test eist voor beide enkels minstens 45 graden buiging en dat de knie 120 graden houdt. Dat toetst precies wat Regisseur vroeg. | Feit | hoog | Een groene run met de test aan. |
| 5 | Het commitbericht noemt "versie 1.2.5", maar geen manifest of changelog staat in de gewijzigde bestanden. | Vermoeden | midden | `blender_manifest.toml` van de betaalde build en de changelog. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | `MEER` staat standaard uit (`CJ_MEER` moet "1" zijn). De wijziging past de workflow niet aan en toont geen run. Zonder `CJ_MEER=1` toetst geen enkele run de versoepelde afstandsregel, terwijl dat een veiligheidsregel is. | Vermoeden | midden | Een test moet de verandering echt dekken |
| 2 | De toets is niet aangepast om te slagen: er zijn alleen extra eisen bijgekomen. | Feit | hoog | Tests niet aangepast om te slagen |
| 3 | `architectuur.md` en `CHANGELOG.md` staan niet in de wijziging. Eis 6 (afstand tussen scharnieren) en de nieuwe regel zijn daar mogelijk beschreven. | Vermoeden | laag | architectuur.md bijgewerkt |
| 4 | De regel in `te_dicht` is nu ±130 tekens lang en het commentaar bij de functie verwijst naar "PROEF"/"1.2.5" in twee versies. Of het bestand onder ±400 regels blijft, valt uit de diff niet te halen. | Vermoeden | laag | Bestanden onder ±400 regels |
| 5 | Geen persoonsgegevens, sleutels of AI-beeld of -geluid gezien. | Feit | hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Enkels via More bones zijn voor wie een rig heeft een zichtbare winst. Er is niets te zien of te spelen in tekst, dus het gevoel kan ik niet beoordelen. | Daan of Iris keurt een beeld van knie plus enkel op MakeHuman en op de robot. | klein |
| 2 | Als de regel te los is, kan een scharnier dicht bij een ander een raar stopvlak geven. Dat merkt de speler pas bij het buigen. | Een beweegproefplaatje (hoek per gewricht) bij elke nieuwe afstandsregel. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Zorg dat de e2e echt met `CJ_MEER=1` draait (workflow of standaardwaarde) en laat een groene run zien in 4.2 en 5.2. Daarmee is bevestigd dat de versoepelde afstandsregel de knie en de enkels goed laat. Nu is de regel losser gemaakt zonder bewijs dat dit door een run wordt getoetst.

**Kan**
1. Toon de oude regel (2*max) of verwijs ernaar, zodat "nooit strenger dan voorheen" controleerbaar is.
2. Corrigeer het commentaar (150 mm tegenover 220 mm) en haal de "PROEF"-sporen weg.
3. Controleer of manifest en changelog naar 1.2.5 gaan, en werk `architectuur.md` bij met de nieuwe afstandsregel.
4. Meet de regel ook op een tweede rig, niet alleen op MakeHuman.

---
Automatische keurder, model `claude-sonnet-5-5`, 19529 tokens in, 3862 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
