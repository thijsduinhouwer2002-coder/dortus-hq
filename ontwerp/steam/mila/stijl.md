# Het Hol: eigen gezicht (Mila)

Begonnen 9 nov 2026. Dit is de stijl die Het Hol herkenbaar van ons maakt. Daans basis (pixel art, cellen 16 x 16, schaal 3, strook 120 px, nooit schalen buiten hele getallen) blijft staan: die is goed. Wat ontbrak was een eigen gezicht. Daan zei het zelf: "nette pixelart zoals de hele hoek", te veel bruin.

## 1. Kleur: pruimkleurige aarde, munt en goud
- **De aarde en de holwand zijn pruim (paars-aubergine), niet bruin.** Bruin is de kleur van elk graafspel; pruim zie je in de hoek nergens (Rusty's Retirement is zonnig groen en bruin, Ropuka blauw water, Tiny Pasture lichtgroen). Na één keer zien herken je "die paarse strook".
- Pruim is de tegenkleur van goud en van de muntgroene Gloop. Daardoor springen de schat, de helden en Gloop eruit zonder dat ze groter hoeven. GEZIEN in `palet-voor-na-build.png` (echte build 4dcbda4, kleuren omgezet): boven bruin, midden pruim, onder een blauwe proef die ik afwees (koud, en blauw is de kleur van Ropuka).
- **Warm licht op koel donker.** De fakkels en de schat geven een oranje gloed op de pruim. Daar zit de sfeer: een knus hol, geen modderbak.
- Hout, steen, gras en de helden houden hun kleur. Gras boven, pruim eronder: de grens tussen buiten en het hol is in één oogopslag te zien, ook op 96 px.
- Bron: `kunst-bron/maak_kunst.py` (sleutels 1 tot 5 en w W v V) en `maak_aarde.py` (A a d D). Alles in `godot/kunst/` is opnieuw getekend uit die bron.

## 2. De haak: Gloop draagt de hoeden van wie hij opat
- Elke held die Gloop opeet, verliest zijn hoed. **Die hoed komt op het hoofd van Gloop**, op de stapel. Na een paar dagen heeft Gloop een wiebelende toren van helmen, puntmutsen en kappen op. Zie `gloop-hoedentoren-6x.png` (0 tot 4 hoeden).
- Waarom dit de haak is: (1) je ziet in één plaatje wat Gloop gedaan heeft, zonder te lezen; (2) het is grappig en het is een verhaal ("mijn Gloop heeft er zeven op"); (3) het groeit vanzelf terwijl je weg bent, zonder straf en zonder grind; (4) het past bij de wrok: een held die terugkomt, ziet zijn eigen hoed op Gloop staan (boos teken); (5) later skins: elke hoed-skin komt ook op de toren.
- Maat: Gloop staat in de schatkamer (2 rijen hoog = 32 spelpixels). Gloop is 10 px hoog, een hoed 3 tot 6 px. **Hooguit 4 hoeden op zijn hoofd**, elke hoed 1 px in de vorige gezakt, scheef om en om (x 0, +1, -1, +1), zodat het wiebelt. Hoed nummer 5 en verder: op een stapeltje naast Gloop op de vloer (de "hoedenberg"), hooguit 3 zichtbaar.
- **Eerlijk:** dit plaatje mag pas in winkelplaatjes als het in het spel zit. Bouwtaak voor Bram staat in `platformen/steam/taken.md`.

## 3. Gloop heeft één oog (gedaan 9 nov)
- Gloop is nu een **eenogige slijm met een scheve grijns en één tand**. Een gewone slijm met twee oogjes en blosjes heeft elk spel; één groot oog zie je op ware grootte (16 px, schaal 3) meteen en vergeet je niet. GEZIEN in `kunst-bron/voorbeeld-strook.png`.
- Het oog kijkt naar rechts. Kijkt Gloop naar links (held komt van links): het hele frame spiegelen, dat mag (hele pixels). Knipperen, slapen, blij, bol, kauwen, hap, spugen, plat en opstaan zijn allemaal mee getekend, zelfde bladen en indeling (`slijm.png`, `slijm_leven.png`), dus de code hoeft niet te veranderen. De bovenkant blijft y 6, dus de hoedentoren past.
- Ontwerpen die ik afwees (`gezichten`, alleen in mijn kladmap): twee ogen met grijns (te gewoon), scheel (leest als fout), loens (te druk op 10 px).

## 4. Wat ik nog ga doen (volgorde)
1. De echte build met pruim bekijken (Actions draait vanzelf op main) en de gloed bijstellen als die vlekt.
2. (gedaan, zie 3) Gloop met één oog.
3. Het meldingenvlak is nu een groot zwart blok over een derde van de strook. Kleiner en in de stijl van het hol (een houten bordje of perkament dat even uit de grond komt).
4. Helden 13 tot 14 px en meer contrast (Daans punt 4).
5. Winkelplaatje 1: de paarse strook op een rustig bureaublad, Gloop met toren groot ingezoomd ernaast. Pas als de toren gebouwd is.

## 5. Eerlijk naast Rusty's Retirement (9 nov, build 09a7ab4)
`vergelijk-rusty-pruim.png`: boven het eerste winkelplaatje van Rusty's Retirement op ware grootte, onder onze echte build met pruim.
- GEZIEN: de strook van Rusty is in dat winkelplaatje ±330 px hoog op 1080 (31% van het scherm). Die van ons is 120 px (11%). Rusty laat dus in zijn winkelplaatje een veel grotere strook zien dan Thijs wil.
- Wij winnen het niet op dichtheid: Rusty heeft vijf keer zoveel dingen per vierkante centimeter en tien kleuren meer. Dat hoeft ook niet, want Thijs wil klein en rustig. **Wij moeten winnen op karakter**: de paarse strook die je herkent, Gloop met één oog en een hoedentoren, helden met een wrok. Per scène minder dingen, maar elk ding grappig.
- Gevolg voor de winkelplaatjes: de strook op 160 px (de hoogste stand, eerlijk) plus een ingezoomd stukje ernaast (Gloop met toren, een held met pleister), duidelijk als vergroting.
- Wat nu nog het meest schaadt (build 09a7ab4): (1) het meldingenvlak, een zwart blok van een derde van de breedte; (2) geen gloed rond fakkels en schat, terwijl warm licht op pruim juist de sfeer maakt; (3) lege gangen. Punten 1 en 2 staan bij Olaf.

## 6. Hoeden, tekens en kleine dingen (9 nov, run 2)
- **10 hoedsoorten** (`held_hoeden.png`, index 0 tot 9): helm, puntmuts, kap, pet, kroon, koksmuts, emmer, hoge hoed, pan, veermuts. Elk een eigen silhouet en een eigen kleur, zodat je op de toren een stapel ziet en geen vlek. De grap zit in de pan, de emmer en de koksmuts. Zie `hoeden-3x.png` (ware grootte) en `hoeden-6x.png`; maker `bron/voorbeeld_hoeden.py`.
- **Boos teken** = onweerswolkje met rode bliksem. Vuist en stoomwolkje afgewezen (gezicht en bot op 8 px).
- **Paneel** in pruim met gouden spijkertjes, geen bruin hout meer. GEZIEN in build 1bbdbc6: hoort nu bij het hol.
- **Spinrag** = plat hangend web, 8 rijen bovenaan de gang, met een spinnetje eronder. In build 1bbdbc6 (`build-1bbdbc6-gloop.png`) stond het oude web nog als gewei op Gloops kop: de gang is maar één cel hoog, dus elk web van 14 rijen botst met wie eronder staat. Daarom plat, en een kolom opzij (Olaf).

## Lat (elke keer)
Stopt iemand met scrollen? Herkenbaar van ons? Grap of haak? Werkt het klein? Eerlijk?
