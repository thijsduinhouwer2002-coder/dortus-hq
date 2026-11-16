# Gloop op je pols: voorstel voor de look van het Garmin-spelletje (Mila)

## Slok v2 in de kit (16 nov ±04:50 UTC, moet Daan 04:40)
In het spel (run 43803456010, fr255-08, GEZIEN met Read) was de slok een kluwen: held, hoeden en helm over Gloops gezicht, oog weg. Nieuw in de kit (`kit/<maat>/gloop-slok.png`):
- **Gloop op dezelfde maat als `gloop-hap`, één grote donkere mond** (1,35 x zo breed als de hap-O, onderkant gelijk), de held met **alleen benen, laarzen, riem en buik** schuin naar linksboven (42 graden), de buik zakt weg in de keel (onderste deel van de mond weer donker met de tong erop). Geen armen meer (de hand bij het oog las als zwaaien).
- **Oog vrij.** Op MIP is de held effen (geen Bayer), iets lichter blauw met zwarte omtrek; Gloop houdt zijn Bayer.
- **Plek:** de slokplaat is even groot als `gloop-hap` en staat op dezelfde plek (anker `slok_gloop_pos` = [0, 0] in `kit.json`; voet gelijk aan de hap). De toren blijft dus gewoon op `toren_voet` van rust.
- Blinde kijkers (steeds een nieuwe, A/B gewisseld): ronde 1 nieuw 4/3/2 (held lag vóór de mond, "gevallen, niet ingeslikt"), daarna grotere mond en keel; ronde 2 nieuw 6/6/7 tegen oud 7/7/4; ronde 3 (held groter, schuiner) **nieuw 7/7/7 tegen oud 5/4/3**, kiest nieuw ("romp en benen verdwijnen schuin in een wijd open mond, ook op 260").
- **Open (moet van kijker 3):** op ware grootte zie je "iets blauws in een mond", nog niet meteen "een ridder". In het spel vliegt op hetzelfde moment de helm naar de toren (`helm-vlieg`), dat vertelt het. Kan later: pluim of zwaard uit de mond laten steken.
- Script: `ontwerp/garmin/bron/gloop_spel_kit.py bron-renders kit` (instellingen `SLOK_*` bovenaan).

## Spritekit en keuze (c) (16 nov ±03:45 UTC)
Gijs vroeg (run 105): toren op de kop of ernaast. Daan koos (c), ik ook: **toren op de kop, de held komt schuin van linksboven.** Waarom: de haak is dat Gloop de hoeden draagt; met een schuine schacht blijft de valbaan vrij van de toren, en de toren is de rechte lijn in het midden.
- **Kit voor de bouw:** `kit/<breedte>/` (320, 390, 416, 454 AMOLED) en `kit/260-mip/`, `kit/280-mip/` (al in de 64 kleuren, harde rand, zwarte omtrek van 1 px). Per map: `gloop-rust`, `gloop-hap`, `gloop-blij` (dikke oogboog), `gloop-slok` (held zijwaarts in de mond, oog vrij), `held-val` (schuin, hoofd naar rechtsonder), `hoed-00` tot `hoed-09` (alle tien), `helm-vlieg`. Maten en ankers in `kit/kit.json`: toren begint op `toren_voet` (px in de Gloopsprite), elke hoed 0,56 x zijn eigen hoogte hoger, Gloops voet op 0,90 van het scherm.
- **Proefbeelden alleen uit de kit:** `kit/proef-c-454-val/slok.png`, `kit/proef-c-260-val/slok.png`, blad `kit/blad-kit-c.png`. Schacht op MIP effen 255,170,85 van (0,04;0,04) naar (0,38;0,74) van het scherm, 0,20 breed.
- **MIP-regels:** Gloop met Bayer (het slijm blijft glanzend), hoeden en held zonder Bayer, effen. Waarom: blinde kijker 1 las de toren met Bayer als "onleesbare prut" (werkt klein 5); na effen hoeden, omtrek, hoed 0,17 breed en het oog vrij bij de slok blind A/B: oud 6/6/5, **nieuw 7/7/7**, kiest nieuw ("hij slikt je in en houdt je hoed").
- **Teller met de kroon** in plaats van het helmpje (te klein om te lezen). Kan van de kijker: hij vond kroon in de teller en helm bij +1 verwarrend; kies in het spel één teken.
- **Niet overgenomen:** de kijker wilde GULP weg bij het valbeeld, omdat het als klank leest. Op het horloge staat de boog naast de echte START-knop; daar is het een knophint. Gijs: kijk in de simulator of het naast de knop zo leest.
- Script: `ontwerp/garmin/bron/gloop_spel_kit.py bron-renders kit` (2 s).

Opdracht hoofdchat 15 nov 23:20: Garmin-spelletje met Gloop nu starten, één knop, binnen 30 s iets leuks, nooit straffen; Daan en Mila kijken mee. Ik ben eigenaar van stijl en wow op Garmin. Dit is een voorstel voor de look en de haak, **geen spelregel**: wat het spel doet beslist Gijs (eerst leuk, dan mooi).

## v3 (16 nov ±02:45 UTC, na Daans keuring van v2)
- **Nieuw beeld 2: de slok.** De held duikt ondersteboven in Gloops mond, benen en blauwe buik steken eruit (donkere rand eromheen), de helm schiet naar de toren. Gloop is in dit beeld groter (0,42 van de breedte): hij zwelt op bij het slikken. Bestanden `v3-amoled-454-slok.png`, `v3-mip-260-slok.png`.
- **Beeld 1 en 3: toren hoger op de kruin** (0,13 in plaats van 0,30), zodat de eerste hoed niet meer over het oog zakt; in beeld 3 is de blije oogboog dikker overgetrokken. `v3-*-beeld1/3.png`, blad `blad-gloop-spel-v3.png`.
- Script `ontwerp/garmin/bron/gloop_spel_v3.py <rendermap> <uitmap>` (gebruikt v2).
- Blinde kijker (A/B willekeurig): oud beeld 2 5/4/7 (scrollen, grap, klein), **slok 8/8/6**, kiest de slok als eerste winkelplaatje ("hij eet ridders en houdt hun hoed"). Moet van de kijker: held klein een blauwe vlek in het groen; gedaan met een donkere rand, op 1x GEZIEN. Beeld 3 oud tegen nieuw: geen verschil gezien, 7/6/7 allebei; kan: toren schever, Gloop zenuwachtig omhoog laten kijken.
- **Eerlijk:** de slok zit nog niet in het spel. Wil Gijs hem gebruiken als winkelplaatje, dan moet er in het spel een slokframe komen (held ondersteboven half in de mond, ±0,3 s). Zonder dat frame blijft beeld 2 van v2 het winkelplaatje.

## Het idee in drie beelden ("Hat Tower")
1. Een held valt door de schacht in het hol, met "!". Boog bij de START-knop: "GULP".
2. Druk: **GULP!** Gloop slokt de held op, zijn hoed schiet omhoog en landt op de toren, "+1".
3. De toren wordt hoger dan je horloge en loopt over de rand: kaartje "23 NEW BEST!". Geen game over: missen = de held loopt weg, geen hoed (nooit straffen).

De haak: **GULP** (Gloop/gulp) en een hoedentoren die letterlijk niet meer op je horloge past. Zelfde grap als de titel Hats of the Fallen, dus het spel is reclame voor Het Hol en andersom.

## Bestanden
- `v2-amoled-454-beeld1..3.png` (fenix 8, venu: 454x454), `v2-mip-260-beeld1..3.png` (FR255: 260x260, alleen de 64 MIP-kleuren), `blad-gloop-spel-v2.png` (boven AMOLED, midden MIP vergroot, onder MIP op 1x).
- v1 (`amoled-454-*`, `mip-260-*`, `blad-gloop-spel-v1.png`) bewaard ter vergelijking.
- Script: `ontwerp/garmin/bron/gloop_spel_v2.py <rendermap> <uitmap>`; renders in `bron-renders/` komen uit de echte modellen `producten/steam-hol/modellen/gloop.py` (versie 1, standen rust/hap/blij), `held.py` (ridder schrik) en `hoeden.py` (alle 10); de helm komt uit het spelblad `godot/kunst/3d/hoeden.png` (zilver, de losse render zonder omgeving maakt hem zwart).

## Besluiten
- **MIP: achtergrond alleen in de 64 paletkleuren, effen vlakken** (grot 170,85,0; schacht 255,170,85; vloer 85,0,0; munt 255,170,0). Figuren met een vaste 4x4-Bayer. Waarom: v1 met verloop plus dithering gaf modder met een rode rand (kijker: werkt klein 3 tot 4); effen gaf 7.
- **Lichte warme grot op AMOLED ook.** Waarom: de toppers (Stack, Crossy Road 3D, Floppy Bird, Step Farmer, door de kijker uit de winkel gehaald) zijn allemaal fel en licht; donkerbruin viel weg.
- **GULP in plaats van HAP, alles Engels.** Waarom: één taal, en Gloop/gulp is een woordgrap.
- **Beeld 3 is een feest, geen verlies.** Waarom: kijker v1 las "too tall!" als game over; nooit straffen.
- **Geen pijl omhoog, geen beentjes uit de mond.** Pijl leest als de UP-knop (kijker v2). Beentjes geprobeerd: in de valrender liggen de benen niet bovenaan, het werd een vlek op de mond.
- Kijkers: v1 AMOLED 8/9/7/7, MIP 5/7/7/4. Blind A/B: v1 5/7/6/3, **v2 7/8/8/7**, kiest v2 beeld 3 als winkelplaatje. Daarna de moets van v2 gedaan (pijl weg, kaartje één regel NEW BEST!, GULP-label groter).

## Voor de bouw (Gijs), alleen als het spel zo wordt
- Sprites op de echte maat: Gloop ±0,34 van de schermbreedte, held ±0,15, hoed ±0,15. Op 260 is Gloop ±88 px breed, een hoed ±40 px. Het spelblad van Het Hol (`gloop.png` 132x80 per cel, `hoeden.png` 63x46, `held0.png` 109x70) is al ongeveer op die maat: eerst die proberen.
- Boog "GULP" bij de START-knop van elk toestel (rechtsboven op de meeste; per toestel nakijken).
- Open: een slokbeeld met de held half in de mond (de kijkers willen de grap zien), en 1x-check op een echt MIP-scherm in de simulator.
