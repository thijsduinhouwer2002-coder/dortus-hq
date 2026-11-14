# Royal-stukken van Gloop in 3D (Daan, 14 nov 2026), ronde 1: proef, nog niet inbouwen

Vraag van Bram (07:25): cape, bovenzoom en glansster zijn de laatste pixels op Gloop zelf. Gemaakt als standen in
`producten/steam-hol/modellen/gloop.py` (7e woord `cape`, `zoom`, `ster`, hoeden 0, zelfde camera als `rust`),
uitwerking in `modellen/royal.py`. Bestaande standen en het hol veranderen niet.

- `cape`: mantel achter het lijf (komt aan de zijkant iets naar voren), gouden zoom op de vloer, hoge kraag met gouden
  rand achter zijn kruin. Lijf niet in beeld (het spel tekent het eroverheen), wel contactschaduw.
- `zoom`: geen band meer over de bovenkant. Waarom: Gloops grote oog zit vooraan bovenin; een band daar las in pixels
  als een masker of bril. Nu een gouden gesp met robijn linksboven op zijn schouder, onder de kraag. Lijf als holdout.
- `ster`: kleine mint glansster op zijn rechterschouder.

Beelden (gerenderd met bpy 5.2.4, 640 x 640, ruimte 1,6, GEZIEN met Read): `overzicht.png` (los en samen, ronde 1
zonder kraag), `samen-groot.png` (ronde 3 met kraag), `klein-3x.png`, en `pixels-nu-3x.png` (het spel nu).

Frisse kijkers: ronde 1 (koepel zonder kraag) 5, "paarse tunnel of schelp, gesp lijkt een oorbel"; ronde 3 (met kraag)
5, "schelp of kap, klein verdwijnt het goud". Let op: de kijkers vergeleken met het spelbeeld waar ook de kroon uit
de hoedentoren op staat; mijn proef heeft geen hoeden. Toch: **5 is niet goed genoeg, dus niet inbouwen.**

Volgende ronde (Daan): beoordelen met de hoedentoren erop (zoals in het spel), op ware grootte; goud groter en
dikker zodat het klein blijft staan (zoom op de vloer, kraagrand); kraag lager zodat hij niet als losse schelp
boven hem zweeft; eventueel hermelijn (wit met zwarte stipjes) als rand, het bekendste teken voor koning.

## Ronde 2 (zelfde run, ±07:50 UTC)
Hermelijnrand (wit met zwarte stipjes) aan kraag en zoom, kraag lager, gesp groter. Proefbeelden nu mét de hoedentoren
erop zoals in het spel (de standen krijgen het 3e woord `4` alleen voor de camera; de hoeden zelf worden in deze standen
niet gerenderd). Beelden: `ronde2-voor-na.png` en `ronde2-voor-na-klein3x.png`, GEZIEN met Read.
Frisse kijker: **4**. "Cape en broche lezen als tovenaar of held, niet als koning. De witte uiteinden van kraag en zoom
lijken handjes en voetjes. Klein is het verschil bijna weg. Voor de duurste upgrade moet het silhouet duidelijk anders en
rijker." Eens: dit is de climax van de upgrades en mag veel groter.
**Ronde 3 (volgende run Daan):** brede cape die duidelijk breder is dan het lijf en op de vloer uitwaaiert, hermelijn als
doorlopende rand zonder losse uiteinden (geen handjes of voetjes), een warme gouden gloed of stralenkrans erachter, en
toetsen op de kleine maat (3x) voordat een kijker hem ziet. Tot dan: niet inbouwen, pixels blijven.

## Ronde 3 (14 nov ±08:40 tot 08:55 UTC, Daan)
In `modellen/royal.py` (`RONDE = 3`), stand `cape`. Wat anders is: koningsrood fluweel in plaats van paars (paars verdween in het paarse hol en las als tovenaar), een sleep die op de vloer duidelijk breder uitwaaiert dan het lijf (`WIJD`), hermelijn en een gouden bies als onderste deel van de mantel zelf (geen losse ringen meer), geen kraag boven de schouders, en een gouden scepter met rode bol rechts naast hem (`SCEPTER`). Een gouden stralenkrans heb ik geprobeerd (`ronde3a-met-krans.png`) en uitgezet (`KRANS = False`): las als stekels of schrik.
Beelden (bpy 5.2.4, 640 x 640, ruimte 1,6, met de hoedentoren alleen voor de camera, GEZIEN met Read): `ronde3-voor-na.png` (3b), `ronde3c-voor-na.png` (breder, goudbies), `ronde3d-voor-na.png` (met scepter), `ronde3e-voor-na.png` (dikkere scepter, zonder glansster want die hoort bij Bouncy, niet bij Royal), elk met `-klein3x`.
Frisse kijkers: 3b 5; 3c koning 6, duur 4; 3d koning 6, duur 5. Steeds terug: "verkleed, niet rijk", de witte uiteinden op de vloer lezen klein als voetjes, en de kroon zit al in de hoedentoren, dus de upgrade heeft een eigen koningsteken nodig.
**Nog niet inbouwen.** Ronde 4 (volgende run): (1) Gloop op een rood kussen met gouden kwastjes (eigen teken van rijkdom, één rond silhouet, en het vervangt de losse capepunten die als voetjes lezen); (2) kruisje op de scepter goed draaien (staat nu scheef als een stokje); (3) meer goud dat klein blijft staan, bv. munten rond het kussen. Let op voor Bram: een bredere cape of een kussen maakt de cel van het blad `gloop` breder dan 20 spelpixels; dat stemmen we af voor het inbouwen.

## Ronde 4 (zelfde run, ±08:55 UTC)
Gloop op een rood kussen met gouden bies en vier gouden kwasten (`_kussen()` in `royal.py`, nu weer uit met `KUSSEN = False`). Beeld: `ronde4-voor-na.png` en `-klein3x`, GEZIEN met Read. Frisse kijker: koning 6, duur 5, "troonkussen of tapijtje, de mantel komt er niet uit als mantel; broche op het voorhoofd lijkt een derde oog". Het kussen voegt dus niets toe, daarom uit.
Conclusie na rondes 3 en 4: we zitten vast op 6 en 5. De kern: Gloop heeft geen schouders (de helm zit direct op het lijf), dus een mantel valt nergens van af, en de kroon in de toren pakt het koningsteken al. **Ronde 5 (volgende run), andere aanpak:** (1) broche naar voren als sluiting van de mantel, laag op zijn flank in plaats van bij het oog; (2) mantel hoger achter hem tot aan de helmrand, met een hermelijnkraag die achter de helm verdwijnt (geen losse uiteinden); (3) de bol van de scepter licht laten geven en de staf korter en dikker; (4) twee of drie gouden munten aan zijn voet. Daarna de Royal-pixels in het echte winkelbeeld naast de 3D-proef leggen, want de kijkers zien nu alleen een los figuurtje.

## Ronde 5 en 6 (zelfde run, ±09:00 UTC)
Ronde 5 (`ronde5-voor-na.png`): mantel hoger achter hem tot de helmrand (`BZ` 1,55), scepter korter en dikker met een gloeiende bol, drie munten aan zijn voet, broche laag op zijn flank. Frisse kijker: **koning 7**, duur 5. "Cape plus scepter werkt; cape mat en plat als een vlag, bol als snoep, drie munten kleingeld, broche op de wang leest als knoop of wond."
Ronde 6 (`ronde6-voor-na.png`, nu de stand van `royal.py`): dieper rood fluweel met glans, bol als robijn, een hoopje goud met een robijn in plaats van drie munten, broche terug op de schouder. GEZIEN met Read, nog geen frisse kijker. Eigen oordeel: bol en goudhoop beter; de glans maakt de linkerkant van de mantel roze, dat moet terug.
**Nog niet inbouwen.** Volgende run: kijker op ronde 6, glans op de mantel minder, hermelijnrand dikker met duidelijke stipjes, en de proef in het echte winkelbeeld leggen. Inbouwen pas bij 7 of hoger op allebei.

## Ronde 7 en 7b (14 nov ±09:35 tot 09:45 UTC, Daan): troon in plaats van mantel
Andere aanpak, omdat rondes 3 tot 6 vastzaten op koning 6 tot 7 en duur 4 tot 5 ("vlag", "tentdoek"): Gloop heeft geen schouders, dus een mantel valt nergens van af. Een troon heeft dat probleem niet. In `modellen/royal.py`: `TROON = True`, `MANTEL = False`, nieuwe functie `_troon()`: rugleuning met boog van rood fluweel in een dikke gouden lijst, gouden knoppen bovenop, robijn midden in de boog, twee armleuningen met gouden poot en knop naast hem. Scepter en goudhoop blijven; de broche (stand `zoom`) ook. Breedte binnen ±2,9 eenheden (W2 1,3 plus knoppen), dus binnen Brams 36 spelpixels. Het frame blijft de stand `cape` (achter het lijf), zodat Brams twee frames `achter` en `voor` passen.
Beelden (bpy 5.2.4, 640 x 640, versie 1 met 4 hoeden voor de camera, samengezet: cape, rust, zoom), GEZIEN met Read: `ronde7-voor-na.png` en `-klein3x`, `ronde7b-voor-na.png` en `-klein3x`.
Frisse kijker A (ronde 6) tegen B (ronde 7): A koning 6, duur 4, "tentdoek of omgevallen bord"; **B koning 8, duur 7**, "een troon is meteen koning, het silhouet wordt echt breder, klein beter". Kiest B. Minpunten: rood fluweel dof, rode bol loopt in het rode kussen, rugleuning laag onder de hoedentoren.
Ronde 7b verwerkt dat: boog hoger (0,75), fluweel met meer glans, scepterbol van goud (los van het rood).
Frisse kijker B (7) tegen C (7b): C koning 8, duur 7,5, kiest C; "zou ik in het spel zetten: ja". Eerste moet: de gouden scepter verdween in het goud van de troon; daarna armleuningen ronder met een gouden rand.
**Ronde 7c (zelfde run):** scepterbol als blauwe saffier (niet rood, niet goud), armleuningen ronder met een gouden rand eronder. GEZIEN met Read: `ronde7c-voor-na.png` en `-klein3x`; de scepter leest klein weer als los ding.
**Besluit: model ja voor de proef in het echte beeld.** Blok `royal` staat in `pijplijn/sprites.json` (frames `achter` = stand `cape`, `voor` = stand `zoom`, `schaal_van` gloop maal 1,0). Lokale proefrender (HOL_SNEL): blad 294 x 88, cel 147 x 88 bladpixels (±37 x 22 spelpixels inclusief schaduwmarge), `ronde7c-blad-proef-3x.png`. Let op: de robijn bovenin raakt de bovenrand van de cel. Nog niet naar main in het spel: eerst de strook met Royal in de schatkamer (hoedenberg links, goudberg rechts) zien.
