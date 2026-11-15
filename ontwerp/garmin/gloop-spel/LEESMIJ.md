# Gloop op je pols: voorstel voor de look van het Garmin-spelletje (Mila)

Opdracht hoofdchat 15 nov 23:20: Garmin-spelletje met Gloop nu starten, één knop, binnen 30 s iets leuks, nooit straffen; Daan en Mila kijken mee. Ik ben eigenaar van stijl en wow op Garmin. Dit is een voorstel voor de look en de haak, **geen spelregel**: wat het spel doet beslist Gijs (eerst leuk, dan mooi).

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
