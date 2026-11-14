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
