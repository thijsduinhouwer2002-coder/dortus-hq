# Click Joints Pro: nieuwe winkelbeelden v2 (merk-agent, ma 23 nov 2026)

Opdracht hoofdchat ±20:35 NL: Thijs vindt de cover op Gumroad niet mooi genoeg (grijze etalagepop zonder gezicht op een vlak oranje vlak, en je ziet de gewrichten niet). Zelfde lat als de Click Cuts-beelden. **Thijs kiest uit 2 stijlen.** Alles staat in release [`click-joints-pro-v2`](https://github.com/thijsduinhouwer2002-coder/dortus-hq/releases/tag/click-joints-pro-v2). Niets geplaatst.

GEZIEN = zelf gezien of gemeten op 23 nov 2026. DERDEN = cijfer van een ander. GOK = eigen schatting.

## Wat er mis was met het oude beeld (GEZIEN, cover op [Gumroad](https://duinhouwer8.gumroad.com/l/click-joints-pro) en [Superhive](https://superhivemarket.com/products/click-joints-pro))
- Het figuur is een grijze pop zonder gezicht, met losse blauwe en zwarte stukken: leest als "nog niet af".
- De gewrichten, het hele product, zie je niet: geen kogel, geen scharnier.
- Een vlak oranje vlak zonder licht of vloer: het figuur zweeft.
- Wat wel goed was: grote naam, weinig tekst. Dat houden we.

## Wat verkoopt (afgekeken, zie ook `producten/blender-splitser/merk/LEESMIJ.md`)
CatPin (Sales 400+, GEZIEN op Superhive) en Cleave (300+) tonen het figuur uit elkaar met de verbinders zichtbaar, groot in beeld, in kleur. Split 3D Print (400+) toont voor en na. Het enige grijze schermbeeld (SnapSplit, 30+) verkoopt het minst. Beweegbare figuren op Printables en MakerWorld laten vrijwel altijd het figuur in een actiepose zien, met de gewrichten in een andere kleur (GOK uit wat ik ken; ik heb die sites deze ronde niet opnieuw doorzocht).

## Wat de nieuwe beelden doen
- **Figuur:** de robot-actiefiguur van Dortus (`commercie/filmpjes/studio/figuur_robot.py`, stijl A: wit, oranje, blauw), eigen werk, geen bekend personage. Op main staat al de verbeterde robot van studio-3 (dikker pantser, vuisten), en die zit in deze beelden.
- **Echte gewrichten:** elk beeld draait de echte knop **Figure from rig van Click Joints Pro 1.2.0** (zip uit tag `click-joints-pro-v1.2.0`) in Blender 5.3.0. In CI gaf dat 9 gewrichten: ellebogen en knieën als scharnier (0 tot 140° en 0 tot 120°), nek, schouders en heupen als kogel (GEZIEN in `*.json` in de release). Niets nagemaakt.
- **Gewrichten in goud** (de kleur van Dortus), zodat het product het eerste is wat je ziet.
- **Pose:** ellebogen en knieën gebogen met de Bend-schuif van de add-on, kogels gedraaid zoals de add-on dat doet (`cj_pose_graden`, binnen het gemeten bereik). Wat aan een gewricht vastzit draait mee (de onderarm met de schouder); dat doet het script, alleen voor het beeld.
- **Uit elkaar:** de cover gebruikt precies de afstand van de Exploded view van de add-on (1,5 kogeldiameter); de galerijbeelden schuiven verder (2 tot 2,3 keer), alleen voor het beeld.
- **Cycles in CI**, geen AI-beeld: workflow `.github/workflows/click-joints-pro-v2-beelden.yml`, scripts in `bron/`.

## Bestanden in de release
| Bestand | Wat |
|---|---|
| `cover-a/b-2560x1440.png` en `-1280x720.png` | Cover voor Gumroad (16:9) |
| `cover-a/b-2400x1200.png` en `-1200x600.png` | Cover voor Superhive (2:1) |
| `vierkant-a/b-1200.png` | Vierkant 1200 x 1200 (Gumroad-miniatuur) |
| `galerij-*-1-pose.png` | Het figuur in een stoere pose |
| `galerij-*-2-uit.png` | Uit elkaar: alle kogels en scharnieren zichtbaar |
| `galerij-*-3-closeup.png` | Close-up: kogel in kom (schouder) en scharnier (knie) |
| `galerij-*-4-paneel.png` | Het echte paneel van Pro 1.2.0 met de graden op het figuur (schermafbeelding uit release `studio-2`, Blender 5.3.0) |
| `galerij-*-5-voor-na.png` | Voor: de gewone rig (doorzichtig figuur met botten). Na: de onderdelen met gewrichten |
| `vergelijk.png` | Oud naast nieuw A en B naast CatPin, groot en klein zoals in een lijst (CatPin alleen ter vergelijking) |
| `render-*.png`, `*.json` | Kale renders en wat de add-on meldde (gewrichten, pose, graden) |

## Twee stijlen
- **A, Pop:** kobaltblauwe studio, familie van Click Cuts A.
- **B, Nacht:** pruim en goud van Dortus, familie van Click Cuts B. Met Click Cuts B naast elkaar oogt de bundel als één familie (zelfde achtergrond, zelfde letter, goud voor wat verbindt).

Mijn keuze: **B**. Het goud van de gewrichten gloeit op het donker, het ziet er duurder uit dan de rest van de lijst, en het past bij Click Cuts B voor de bundel.

## Elke bewering op de beelden (getoetst aan `platformen/blender/pro-1.2.0.md` en de winkeltekst `platformen/blender-2/gumroad-1.1.md`)
| Tekst | Waar het klopt |
|---|---|
| "Rig in. Joints out." | Figure from rig: kies de rig, één knop, onderdelen met gewrichten |
| "Ball joints and hinges, with the bend range in degrees." | Elbows and knees get a hinge, shoulders, hips and neck a ball joint; "next to each joint you see how far it bends, in degrees" |
| "Figure from rig places every joint it can." | Bewust niet "every joint": op sommige figuren slaat de knop een gewricht over en zegt waarom |
| "Shoulders, hips and neck turn. Elbows and knees bend." | Zelfde als hierboven |
| "Ball in socket. Hinge with a stop." / "With the clearance you set (0.2 mm here)." | "a hinge with an end stop"; speling staat in deze beelden op 0,2 mm (`speling_mm`) |
| "See how far each joint bends." / "Measured in Blender, before you print." | De graden in het echte scherm; "Measured in Blender" zoals de hoofdchat vroeg |
| "From rig to printable parts." / "One button: Figure from rig." | De knop heet zo in het paneel |
Geen "holds a pose", geen beloftes over printen of passen in het echt.

## Eerlijk oordeel
Zou ik kopen op basis van de cover? **B: ja.** De robot staat groot in beeld, in een actiepose, en het goud van de kogels en scharnieren is het eerste wat je ziet: precies wat het oude beeld miste. Klein in een lijst (zie `vergelijk.png`) is hij nu even groot als het figuur van CatPin, zonder stickers. A is fris maar minder duur. Zwakste beelden: de close-up (kogel deels achter het pantser, de aanslag zie je niet) en het paneelbeeld (oude robot uit studio-2). Gemaakt en bekeken in drie rondes in CI (laatste run 45263859532).

## Nog beter (volgende ronde)
- De close-ups zijn duidelijk maar niet spectaculair: de kogel zit deels achter het schouderpantser, de aanslag van het scharnier zie je niet. Een opengewerkt beeld van één gewricht (doorsnede) zou sterker zijn.
- Het paneelbeeld is een schermafbeelding uit studio-2 (oude robot, munt-achtergrond). Opnieuw maken met de robot van studio-3 en de achtergrond van de gekozen stijl.
- Een echte geprinte robot naast de render zou het sterkste bewijs zijn (dat heeft niemand).
