# Tekens boven het hoofd in 3D (Daan, 14 nov 2026)

Model: `producten/steam-hol/modellen/tekens.py` (boos, uitroep, zweet, zzz, ster; zelfde volgorde als `godot/kunst/tekens.png`). Elk teken is een room wolkje met staartje naar het hoofd en het symbool er dik op, zodat het tegen de paarse aarde leest.

- `tekens-v1.png`: de vijf groot, op de kaartkleur.
- `tekens-in-strook120-ware-grootte.png` en `-3x.png`: de vijf op 24 px hoog (8 spelpixels, zelfde maat als het pixelteken) in de echte strook van run 43533954132, naast het oude pixelteken (blauwe druppel en bruin muzieknootje linksboven).

Eigen oordeel op ware grootte: alle vijf te noemen (ader, uitroepteken, druppel, z's, ster); het wolkje maakt ze los van de muur, wat de pixeltekens niet doen. Het muzieknootje van de bard zit niet in `tekens.png`; als dat ook een teken wordt, maak ik het erbij (6e: noot).
Waarom een wolkje: zonder achtergrond verdwijnt een rood of paars symbool van 24 px in de paarse aarde (zelfde les als de heksenhoed in ronde 6c).

## 14 nov 2026 ±08:55 UTC (Daan): laars, 7e teken
De uitgespuugde laars van Gloop in 3D, als frame `laars` achteraan in `modellen/tekens.py` (stand `6`), zoals Olaf vroeg (plek 0 tot 5 liggen vast in de toetsen). Zijaanzicht, neus naar rechts, korte schacht en lange neus (een duidelijke L), licht leer met een lichtere omgeslagen kraag, donkere zool en een donkere rug erachter zoals bij de noot. Maat zo gekozen dat het blad 8 x 8 spelpixels blijft en `eenheid_px` van de andere tekens gelijk blijft (lokaal nagemeten met `pijplijn/render.py tekens`: blad 224 x 32, eenheid 33,3203).
- `laars-los.png`: de laars groot.
- `tekens-met-laars.png`: alle zeven naast elkaar.
- `laars-voor-na-2x.png` en `laars-ware-grootte-voor-na.png`: pixellaars en 3D-laars op dezelfde plek in Olafs winkelbeeld week 160 (run 43570708482). De achtergrond direct achter de 3D-laars is met de hand opgeplakt.
Frisse kijkers: ronde 1 gaf 5 (las als flesje, L-vorm weg, slijm las als sjaal); daarna schacht korter, neus langer, gesp en slijm weg, leer lichter. Ronde 2 gaf 6 en las een laars. Groter kan niet zonder de cel van alle tekens groter te maken.
