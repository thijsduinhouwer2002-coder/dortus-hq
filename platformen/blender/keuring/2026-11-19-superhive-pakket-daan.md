# Keuring Superhive-pakket Click Joints Pro, 19 nov 2026, Daan
Wat ik keurde: `platformen/blender/superhive/README.md` (excerpt, titel, beschrijving, tags) en de 6 beelden in `platformen/blender/superhive/beelden/`, op main 4cffa33. Elk beeld zelf bekeken.
Akkoord: ja Superhive-pakket Click Joints Pro op 4cffa33, mits de tag `print in place` eruit gaat (zie moet 1; daarna geen nieuwe keuring nodig)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Beeld 1 (uitgelicht) is sterk genoeg: een herkenbare menselijke figuur met alle gradenlabels (±20 schouders en nek, 140 ellebogen, ±25 heupen, 120 knieën) en de kop "Right knee: bends 0° to 120°". Het vertelt in één blik wat het product doet. Wel veel lege donkere ruimte links; de figuur beslaat maar een derde van de breedte. | feit (GEZIEN) | hoog | |
| 2 | Tekst klopt met beeld: 0 tot 115 en stop (beeld 2), "+3° past limit" (beeld 3), groene naad (beeld 5), Clearance 0.20 en de knoppen Shoulder tot Neck in het paneel (beeld 1). 120 en 140 in beeld 1 zijn geen 90/115/135, dus "from rig" is zichtbaar waar. | feit (GEZIEN) | hoog | |
| 3 | "the spots that collide turn red": staat in de code (`eigenschappen.py` r.64, `beweeg.py` botsende vlakken), maar geen beeld toont rode delen op het model; beeld 3 en 6 tonen alleen de rode lijn en het rode vlak van de boog. Niet fout, wel niet bewezen in beeld. | feit | hoog | een scherm met rode botsvlakken |
| 4 | Tag `print in place` is onjuist: Click Joints knipt het model in losse delen die je na het printen in elkaar klikt. Wie op "print in place" zoekt, verwacht iets anders en vraagt geld terug of schrijft een slechte review. | feit (code splitst in delen, README zegt "split into watertight parts") | hoog | |
| 5 | Beeld 4 is het zwakste: blokkige testpop, volle Blender-interface met tijdlijn en eigenschappen, en een losse "±8°" bij de rechterheup die een koper als fout leest. Het voegt naast beeld 1 weinig toe. | feit (GEZIEN), "leest als fout" is vermoeden | midden | |
| 6 | Beeld 3: het label "115°" wordt half bedekt door de rode lijn. | feit (GEZIEN) | hoog | |
| 7 | Versies 4.2, 5.2 en 5.3 kloppen met de e2e-matrix (`4.2.23`, `5.2.3`, `5.3.0` in `blender-gewrichten-e2e.yml`). | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen Blender-logo in de beelden (menubalk weg); rechtsonder staat alleen een klein icoon met "5.3.0" in beeld 1 en 4, geen Blender-logo. | feit (GEZIEN) | hoog | Superhive artikel 253 |
| 2 | Alle 6 beelden 2:1, 1920 x 960; minimaal 5 gehaald. | feit | hoog | Superhive artikel 41 |
| 3 | Cijfers in het pakket hebben GEZIEN, DERDEN of GOK; geen persoonsgegevens; geen AI of "I" in de tekst. | feit | hoog | CLAUDE.md regel 2 en 5 |
| 4 | Prijs naar $19 en Gumroad gelijk trekken: geen geld uitgeven, wel een keuze van hoofdchat of Chris, niet van mij. De $0-variant kost $49 per maand: terecht niet gedaan zonder Thijs. | feit | hoog | regel 1 |

## Moet (blokkeert akkoord)
1. Tag `print in place` weghalen (bijvoorbeeld vervangen door `ball joints` of `posable`, de Amerikaanse spelling waar ook op gezocht wordt).

## Kan (mag later)
1. Beeld 1 strakker bijsnijden zodat de figuur groter staat (bijvoorbeeld van x 600 tot 1850 en dan tot 2:1 aanvullen), of de lege linkerkant gebruiken voor één regel tekst als "From rig to poseable print in one click".
2. Beeld 4 als laatste zetten of vervangen door een scherm met rode botsvlakken op het model (dan is ook bevinding A3 bewezen).
3. Beeld 3: label 115° vrij van de rode lijn bij een volgende opname.
