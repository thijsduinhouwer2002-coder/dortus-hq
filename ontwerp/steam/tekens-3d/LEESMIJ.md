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

## 16 nov 2026 ±15:05 UTC (Mila): boos en zweet leesbaar op ware grootte (Iris keuring 2, probleem 3)
- **Boos:** eerst Daans eerste voorstel gedaan (bogen dikker 0,07 en dichter bij 0,16, ook 0,18/0,065 en 0,19/0,075 geprobeerd). Op ware grootte werd dat een rood bloemetje of donut, niet boos. Daarom Daans tweede voorstel: **een rood wolkje met twee dikke donkere gefronste wenkbrauwen** (binnenkant laag). Rood leest al als boos voordat je de vorm ziet, en het is het enige rode wolkje tussen de room wolkjes. `TEKEN_BOOS_VORM=ader` geeft de bogen terug (met de nieuwe maten).
- **Zweet:** druppel 1,3x groter en donkerder blauw (`3a86d8`, was `5aa8e8`), glans meegeschaald.
- Maten van het blad bleven gelijk (224 x 32, `eenheid_px` 33,3203), dus geen code nodig; held_beeld.gd pakt het nieuwe blad zo.
- `mila-boos-zweet-voor-na-120-ware-grootte.png` en `-4x.png`: oud boven, nieuw onder, op 24 px (8 spelpixels) op twee plekken van de echte strook (run met `strook-120.png` van tak `schermen`, commit 7ce6987). GEZIEN met Read op 4x en ware grootte: het boze wolkje springt eruit en leest als kwaad gezicht; de druppel blijft blauw tegen het room.
