# Keuring Click Joints Lite (zip en varianttekst Superhive), 23 nov 2026, Daan
Wat ik keurde: `platformen/blender/superhive/lite-variant.md` (commit b577dbe), zip `producten/blender-gewrichten/uitgave/click_joints-0.1.1.zip`
Akkoord: **ja voor de zip, nee voor de varianttekst** (twee moet-punten, kleine zinswijziging; vervangtekst staat onderaan)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Zip op main: sha256 d1643ba5...fe3d, 44.928 bytes. Live API extensions.blender.org geeft voor click_joints 0.1.1 dezelfde hash en grootte (zelf met curl, 23 nov ±09:30 UTC, GEZIEN). Zelfde zip als gratis: klopt. | feit | hoog | |
| 2 | Manifest: id click_joints, 0.1.1, Blender 4.2.0 en nieuwer, export STL of 3MF (GEZIEN na uitpakken). | feit | hoog | |
| 3 | "ball joints with a fit colour": klopt (`kleur.py`, ring groen/geel/rood rond de snede). | feit | hoog | |
| 4 | "the bend range in degrees": klopt (`gradenboog.py`, getal gelijk aan paneel). | feit | hoog | |
| 5 | "split into parts": klopt (CHANGELOG 0.1.0: mesh wordt in twee waterdichte delen gesneden). | feit | hoog | |
| 6 | "export to STL or 3MF": klopt (`exporteer.py`, één bestand per deel, mm). | feit | hoog | |
| 7 | **"click hinges"**: op 19 nov is in de Pro-tekst "click hinge" bewust "hinge" geworden: geen klik beloven zonder print (README superhive, regel 56). Hier komt "click" terug. | feit | hoog | |
| 8 | **"red where the parts hit"** als iets wat Pro toevoegt: de gratis versie doet dit al bij kogels (CHANGELOG 0.1.0: "turns red where the parts would collide"). Pro voegt rood voorbij de stop van het scharnier toe. Nu leest het alsof Lite dat mist. | feit | hoog | |
| 9 | "stop at 115°": de knop biedt 90°, 115° of 135° (`betaald/scharnier.py`, gezien in where-to-find-it.md voor 1.1.0). Of 1.0.x die keuze al had weet ik niet. "Stop at 115°" leest als vast. Veiliger zonder getal. | vermoeden | midden | code van Pro 1.0.x op de Superhive-zip |
| 10 | "pose slider": de schuif heet in het paneel "Bend" (where-to-find-it.md). "bend slider" sluit beter aan bij wat de koper ziet. | feit (voor 1.1.0) | midden | |
| 11 | Geen upgradekorting beloofd: klopt. | feit | hoog | |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Cijfers in het bestand hebben GEZIEN; geen persoonsgegevens. | feit | hoog | eerlijk, openbaar |
| 2 | Variantnaam "Lite (same code as the free version)" is eerlijk: niemand betaalt zonder te weten dat het gratis kan. Goed. | feit | hoog | eerlijk |
| 3 | GPL staat verkoop toe. Of Superhive een variant toestaat die elders gratis is, heb ik niet nagekeken. | vermoeden | laag | regels Superhive (hoofdchat leest die bij het aanzetten) |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Wie Lite kiest, ziet in één zin wat Pro meer doet: goed, dat duwt naar Personal. | eventueel "Most people pick Personal." is te veel beloofd, dus niet doen | |
| 2 | Lite onderaan de varianten (stap 6) houdt Pro in beeld. Goed. | | |

## Moet (blokkeert akkoord)
1. "click hinges" wordt "hinges" (A7).
2. Rood als Pro-extra alleen voor het scharnier: "red where the parts hit past the stop" (A8).

## Kan
1. Geen vast getal: "with an end stop" in plaats van "that stop at 115°" (A9).
2. "pose slider" wordt "bend slider" (A10).

## Voorstel vervangzin (met moet en kan verwerkt)
```
Lite is the same code as the free Click Joints 0.1.1 on extensions.blender.org: ball joints with a fit colour and the bend range in degrees, split into parts, export to STL or 3MF. Buying Lite supports the work and gives you the zip here. Want more? Pro adds hinges for knees and elbows with an end stop, a bend slider, and red where the parts hit past the stop.
```
Neemt Bram deze zin letterlijk over, dan is de tekst akkoord zonder nieuwe keuring (alleen de woorden uit moet en kan zijn veranderd). Webpagina's lees je met `curl` in Bash, nooit met WebFetch.
