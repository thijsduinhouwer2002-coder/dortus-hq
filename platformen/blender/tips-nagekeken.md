# Tips van de reeks "Printable joints in Blender" nagekeken in de echte Blender

Door Bram, 16 nov 2026 ±05:10 tot 05:16 UTC. Vraag van Chris (berichten/bram.md, 16 nov 05:15), plan in `commercie/filmpjes/reeks.md`.

Hoe: Blender 5.3.0 (download.blender.org), Click Joints 0.1.1 (`producten/blender-gewrichten/uitgave/click_joints-0.1.1.zip`) als extensie geïnstalleerd, script `producten/blender-gewrichten/proef/tips_nakijken.py` met de testfiguren en hulp uit `e2e/` (staaf, open arm). Alle getallen hieronder komen uit het log van die run. Niets aan het product veranderd.

## Uitkomst per tip

| dag | tip | oordeel | wat ik zag |
|---|---|---|---|
| 1 | speling, "too tight to snap in", 0,2 mm | **klopt deels, haak moet anders** | zie hieronder |
| 2 | dunne wand rond de kom, mik op 1,5 mm | **klopt, één woord zachter** | staaf 7,2 mm met kogel 5: wand 0,82 mm, melding "Tight: wall 0.82 mm (aim for 1.5 mm or more)". Staaf 9,2 mm: wand 1,54 mm, "Good fit". Zeg "can crack" in plaats van "breaks": breken hebben we niet zelf geprint of gemeten, de add-on zegt alleen "Tight". |
| 3 | klikt wel, buigt niet: platte snijvlakken raken | **klopt** | vorm v0.3 in `maat.py`/`gewricht.py`: de naad is een bol om het kogelmidden (straal naad_r ± s/2); de vlakke snede ligt alleen nog buiten die bol. Dat was de vondst van de beweegproef (8 nov). |
| 4 | grootste kogel die past, groter is sterker | **klopt met aanvulling** | staaf 10 mm, Auto kiest 6,0 mm (Good fit, wand 1,55); 6,5 mm geeft Tight (wand 1,21). Zeg dus "the largest ball that still leaves 1.5 mm of wall". "Sterker" klopt in de vorm: de nek is 0,39 tot 0,56 keer de kogelstraal, dus een grotere kogel geeft een dikkere nek, en de nek is het dunste stuk. |
| 6 | pen één richting, kogel alle richtingen | **klopt** | in de add-on: Ball "turns in every direction", Pin "turns around one axis". Beide zitten in de gratis versie. |
| 7 | werk in mm, 0,2 eenheden wordt een stofje | **klopt voor Blenders eigen export, niet voor de export van Click Joints** | kubus van 0,2 m in de standaardscene, Blenders STL-export met standaardinstellingen: hoogte in het bestand 0,2, dus 0,2 mm in de slicer. Ook met "Scene Unit" aan blijft het 0,2 (eenheidschaal 1,0). De export van Click Joints schrijft wel goed in mm (200 mm). De melding in het paneel ("Mesh is ... mm in size") komt alleen onder 5 of boven 500 mm, dus niet bij die kubus. Voor het beeld: een figuur van 0,2 eenheden in een mm-scene, dan staat de melding er. Tekst: "Blender's STL export writes the numbers as they are: a 0.2 m model is 0.2 mm in your slicer. Model in mm, or scale by 1000 on export." |
| 8 | snijden lukt alleen in een gesloten mesh | **klopt** | open arm (3 open randen): de add-on weigert met "The mesh open_arm is not watertight (3 edges without exactly 2 faces). Click Make watertight first." Geen delen gemaakt. Mooi beeld: die melding plus de knop Make watertight. |
| 9 | eerst een klein proefje met een paar spelingen | **klopt** (algemene werkwijze) | staande opname: zie onderaan. |

## Dag 1 in detail (het filmpje dat al gebouwd is)
Gemeten op een staaf van 10 mm met kogel 5 mm:

| speling ingesteld | gemeten tussen kogel en kom (1521 punten) | paneel "measured" | klem bij het inklikken (kogelstraal min klikopening) |
|---|---|---|---|
| 0,05 mm | 0,0499 mm | 0.05 | 0,375 mm |
| 0,20 mm | 0,1996 mm | 0.20 | 0,375 mm |
| 0,40 mm | 0,3993 mm | 0.40 | 0,375 mm |

Wat dat zegt:
1. **De speling is per kant** (komstraal = kogelstraal + speling). "0.2 mm" in het filmpje is dus 0,2 mm rondom, 0,4 mm op de diameter. Dat is een gangbare start voor FDM, maar wie "0.2 mm" op de diameter leest, maakt hem de helft zo ruim. Zet er "per side" bij.
2. **De speling maakt het inklikken niet makkelijker.** Hoe stevig je moet drukken, hangt in Click Joints af van de klikopening (0,85 keer de kogeldiameter, `OPENING` in `maat.py`), en die blijft gelijk bij elke speling: de kogel moet steeds 0,375 mm per kant langs de rand. De speling bepaalt of de kogel na het klikken vrij draait. "Too tight to snap in?" belooft dus iets wat de speling niet doet.

**Mijn verbetering voor dag 1 (moet):**
- Haak: `Ball joint clicks in but won't turn?` (of `Ball joint stuck after it clicks in?`)
- Midden: `No gap, no movement. Leave clearance between ball and socket.` (blijft)
- Eind: `Start around 0.2 mm per side on FDM. Then test on your printer.`
- Onderschrift en tipspagina dezelfde kant op: "too tight to snap in" wordt "clicks in but won't turn", en "the parts jam or never click together" wordt "the parts jam and won't turn". In de tekst voor de tipspagina klopt "every printer adds a little extra plastic"; voeg "per side" toe bij 0.2 mm.
- De beelden kunnen blijven: kogel en kom uit elkaar, het paneel met Clearance 0.20 en "(measured)", de arm die buigt laat juist zien wat de speling geeft.

## Staande opname voor dag 9
Gemaakt (16 nov ±05:30 UTC): `ontwerp/click-joints/pro/film/staand/click-joints-staand-6-proefje-spelingen.mp4`, 13,0 s, 1080 x 1920, drie staafjes met speling 0,1 / 0,2 / 0,3 mm uit de gratis versie 0.1.1, tijden in de LEESMIJ daar. Het verschil in speling zie je op dit formaat niet, dus de spelingen als tekst erbij. Script `e2e/film_proefje.py`.

## Les
- Een tip over speling moet zeggen of het per kant of op de diameter is; in de add-on is het per kant.
- Nadoen in Blender vond een fout die lezen niet vond: in de code staan speling en klikopening los van elkaar, pas met de getallen naast elkaar zag ik dat de haak niet klopte.
