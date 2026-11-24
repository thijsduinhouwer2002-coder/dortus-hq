# Keuring yt-short tip-dubbel en pro-robot-delen (plezier en beeld), 24 nov 2026, Iris
Wat ik keurde: de releasebestanden uit de wachtrij:
- `regisseur-13/tip-dubbel-geluid.mp4` (`2026-12-08-yt-short-tip-dubbel.md`)
- `regisseur-14/pro-robot-delen-geluid.mp4` (`2026-12-09-yt-short-pro-robot-delen.md`)

Hoe: zelf gedownload met curl; ffprobe (GEZIEN: beide 1080 x 1920; 43,4 s en 47,4 s); sha256 van pro-robot-delen gelijk aan het concept (96a7cad1..., GEZIEN); een tegel van een beeld per 3 s per filmpje bekeken met Read, plus fijnere tegels: dubbel 0 tot 6 s (1 per s), robot 22 tot 34 s (1 per s) en 25,5 tot 28,5 s (4 per s); silencedetect (-40 dB, 0,6 s): nul stille gaten in beide (GEZIEN). Het geluid zelf heb ik niet beluisterd.
Akkoord: ja (beide, op beeld en plezier)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Dubbel: alle stappen in beeld: Tab + L (alleen de bovenkant oranje, onderkant blauw: "Only the top!"), M-menu met By Distance onder de muis, "48 removed" met het gele getal, L opnieuw en de hele vaas oranje ("One part now"). Het probleem zie je zelf in beeld, niet alleen in de kop. | Feit (tegels) | hoog | |
| A2 | Robot: alle beloofde stappen in beeld: robot als één mesh met botten, knop Figure from rig, robot met gewrichtlabels (±30°, 140°, 120°), de echte lijst (Hinge bij ellebogen en knieën, Ball bij nek, schouders, heupen), knie naar de stop met rode lijn en "+11°/+12° past limit", Fit and export-paneel met STL/3MF en Export 3MF, eindkaart Click Joints Pro. | Feit (tegels) | hoog | |
| A3 | Robot zin 9 "Exploded view pulls the parts apart": bij die zin zie je vooral de robot met labels en daarna een inzoom; de delen staan maar een klein beetje uit elkaar. Pas bij HONEST (36 tot 42 s) staat de robot echt los in delen. | Feit (fijne tegel 25,5 tot 28,5 s) | hoog | Een beeld waarin de delen bij zin 9 duidelijk zwevend uit elkaar staan. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | Geen AI-beeld of AI-persoon: schermopname van Blender en een eigen robot-render. | Feit | hoog | REGELS 9 |
| B2 | Eerlijkheidsregel "Measured in Blender, not print tested by us yet." staat onderaan in elk beeld van beide, ook op de eindkaart. | Feit | hoog | eerlijk |
| B3 | Dubbel: geen productnaam, eindkaart alleen dortus.com/yt. Robot: geen prijs, geen slicer-naam; productnaam alleen als Pro-reclame, zoals het Pro-script vraagt. | Feit | hoog | REGELS |

## Deel C: zou een kijker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | Dubbel: beste "probleem in beeld" van de tip-reeks tot nu: de half oranje vaas laat in één oogopslag zien dat het model in twee stukken is. Rustig tempo, groot en leesbaar. | | |
| C2 | Dubbel: eerste beeld (vaas die draait, "Two pieces?") werkt, maar de naad zie je pas als je het weet; de vaas is nog vrij klein in beeld 0 tot 1 s. | Begin met het half oranje beeld (Only the top!) als hook, of zoom in beeld 1 dichter op de naad. | klein |
| C3 | Dubbel: bij TIP ("Check every model") staat de vaas nog even in Edit Mode, met een overgang; de Regisseur zag dit al. | Meteen Object Mode bij TIP. | klein |
| C4 | Robot: sterk eerste beeld: een leuke, kleurige robot groot in beeld met een vraag. Het voelt als speelgoed, dat past bij 3D-printers. Het knie-deel met de rode lijn is het leukste moment. | | |
| C5 | Robot: de kop raakt het hoofd van de robot, in beeld 1 ("One solid piece?", al bekend) en erger bij HONEST: "Print a test joint first" loopt dwars door het hoofd, het woord "joint" is half weg. De eerlijkheidsregel staat ook onderaan, dus geen Moet. | Bij een volgende render de robot lager of kleiner, zodat er boven ruimte is voor de kop; of de kop in een vlak met achtergrond. | middel (nieuwe render) |
| C6 | Robot: het label "Left knee: bends 0° to 120°" ligt in veel beelden over het hoofd van de robot. | Label lager of opzij. | klein |
| C7 | Robot: zin 9 laat het uit elkaar gaan niet goed zien (A3). | Bij zin 9 het beeld van 36 tot 42 s gebruiken (robot echt in delen). | klein |
| C8 | Robot: bij Fit and export (29 tot 33 s) zie je vijf seconden alleen het paneel; dat is saai en de ondertitel ligt over de knoppen. | Korter, of eindigen op een beeld van de losse bestanden of de losse delen. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen.
Kan: robot C5 (kop door het hoofd; grootste punt), C7, C8, C6; dubbel C2, C3. Geen van beide hoeft opnieuw. Voor volgende robot-renders: houd boven het hoofd ruimte vrij voor de kop.
Let op voor de hoofdchat: pro-robot-delen niet vóór 7 dec plaatsen (zelfde belofte als de Short van 22 nov, staat in het concept).
