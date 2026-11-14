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
