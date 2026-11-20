# Keuring gat na hol-niveau, 20 nov 2026, Daan
Wat ik keurde: tak `claude/steam-hol-niveau-gat`, commit 47b9fa3 (Olaf): `kern/afloop.gd`, `kern/regels.gd`, `toets_namen.gd`, logs `platformen/steam/data/vers-20nov-niveau/`
Akkoord: ja voor de code, met één moet over de volgorde (klein)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Bij een nieuw niveau terwijl je kijkt komt de regel meteen en de volgende held op +6,0 s (4242: niveau 74,5, held 80,6; 777: 66,2 en 72,2, 145,7 en 151,8) | feit (logs gelezen) | hoog | Windows-run op de tak |
| 2 | Na weg zijn en in de demo gebeurt niets extra: `live` alleen vanuit `held_klaar`, `opslag.gd` roept `faam_erbij` zonder `live`; demo via `s.get("demo")` (bestaat in `strook.gd` r. 43) | feit (code) | hoog | toetsen 4 en 5 in `toets_namen` |
| 3 | Een held die al eerder komt, blijft eerder (`minf`) | feit (code en toets) | hoog | |
| 4 | "Geen rng-trekking": `regels.kies` gebruikt de gedeelde `rng` van de strook, maar bij een lijst van één regel is het `randi_range(0, 0)`; in Godot 4 geeft dat het getal terug zonder te trekken | vermoeden | midden | zelfde zaad, logs vóór en na het eerste niveau naast elkaar. Komt er later een tweede `hol_niveau`-regel bij, dan trekt hij wel en schuift de rest van het zaad. Geen probleem, wel goed om te weten |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Spelerstekst staat als CONCEPT in `regels.gd`, past in 42 tekens met nummer 2 tot 12 (toets) | feit | hoog | spelerstekst Hats alleen CONCEPT |
| 2 | `architectuur.md` bijgewerkt, `afloop.gd` 182 regels | feit | hoog | bestanden onder ±400, architectuur |
| 3 | Geen bestaande toets aangepast, 6 nieuwe erbij; cijfers in het logboek met GEZIEN en zaden | feit | hoog | tests niet aanpassen, eerlijk |
| 4 | Op een tak, niet op main (bevroren tot na de speeltest) | feit | hoog | besluit speeltest |

## Deel C: zou een speler het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De volgorde leest verkeerd om. Nu: "Your hole has a reputation now. Level 2." en pas 2,6 s later "Joost came back. The Spike Pit won. +9". De speler ziet het gevolg vóór de oorzaak, en de beloning van de vangst (+9) komt na de feestregel. | Andersom: eerst de valregel (die al klaarstaat), dan de niveauregel als de valregel weg is. Held nog steeds uiterlijk 6 s na het niveau. De niveauregel staat dan ±3,4 s, net lang genoeg. | klein |
| 2 | Niveau 2 en 3 krijgen dezelfde zin met een ander getal; na een paar niveaus voorspelbaar | Thijs schrijft de echte tekst na de speeltest; vraag hem dan om 2 of 3 varianten (de schudzak kan dat al) | klein |
| 3 | Het bordje wipt op hetzelfde moment (`bordje wip niveau 2`): goed, regel en bordje vertellen samen één ding | niets | |

## Moet (blokkeert akkoord) / Kan (mag later)
- **Moet 1 (C1):** niveauregel ná de valregel van de held die het niveau gaf. Daarna alleen dat punt opnieuw (één log is genoeg).
- Kan 1 (A4): in het commentaar "geen rng-trekking" erbij zetten dat dit alleen klopt zolang `hol_niveau` één regel heeft.
- Kan 2 (C2): varianten van Thijs na de speeltest.
