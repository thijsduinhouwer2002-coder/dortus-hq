# Click Joints: filmpje voor de winkel en de lanceerberichten (ontwerp Daan, 8 nov 2026)

Opdracht van Thijs (8 nov 22:18): een filmpje van 15 tot 20 seconden, MP4, 1920 x 1080, samen met Bram. Daan beslist hoe het eruitziet en keurt het. Versie 2 van de plaatjes (een echte figuur in plaats van buizen van dichtbij) mag in hetzelfde filmpje.

## Waarom wij, in beeld
**Concurrenten (bekeken 8 nov, curl op superhivemarket.com):** Cleave heeft drie YouTube-filmpjes, alle drie handleidingen ("Cleave 01 (Beginner): Split a Model ...", "Cleave 02 ...", "Auto Seams + Connectors"), JointLab heeft één opname ("Jointlab"), Cut Flex heeft geen filmpje op de pagina (GEZIEN: geen YouTube of mp4 in de HTML). Het zijn schermopnames van minuten, met muis en menu's, gemaakt om uit te leggen.
**Onze stap erbovenop:** 18 seconden, zonder geluid te volgen, en het ene moment dat niemand anders heeft staat in het midden: je sleept de arm, de witte boog telt mee, en voorbij de gemeten grens wordt het rood. Het filmpje ziet eruit als onze poster die beweegt (zelfde achtergrond, letter, kleuren en kaart), dus winkel, productpagina en filmpje zijn één merk.

## Opbouw (18,5 s, 30 beelden per seconde)
Elk beeld: achtergrond van de poster, bovenaan "Click Joints" met icoon, één grote kop (72 px) en rechts de drie stappen uit het paneel ("1 Place · 2 Joint · 3 Fit and export", de huidige vet). Daaronder een kaart van 1700 x 784 met het beeld uit Blender. Geen muziek nodig, geen stem. Scènes lopen 0,3 s in elkaar over; de kop van scène 1 staat er meteen, bij een wissel gaat de oude kop eerst weg en komt dan de nieuwe (nooit twee koppen door elkaar).

| Tijd | Kop (laag) | Wat je in de kaart ziet (opname in de echte Blender) |
|---|---|---|
| 0,0 tot 3,0 | kop1 "Click where it should bend." | De hele figuur, mooi in beeld, licht draaiend (camera 10° om de figuur in 3 s). Op 2,0 s komt een pijltje in beeld en klikt op de elleboog: groene ring. |
| 3,0 tot 6,5 | kop2 "One click. A ball joint that fits." | De naad verschijnt en kleurt groen. Camera zoomt rustig naar de elleboog en het paneel: "Good fit", "Bends ±20°", "Wall: 1.54 mm" moeten aan het eind leesbaar zijn (paneeltekst minstens 18 px hoog in de film; zet daarvoor in Blender Preferences > Interface > Resolution Scale rond 1,6 in plaats van achteraf te vergroten, want vergroten maakt de tekst wazig). |
| 6,5 tot 11,5 | kop3 "Drag the bend. Red means too far." | De onderarm buigt vloeiend van 0 naar 15° (boog wit, getal telt mee), houdt 0,5 s stil, gaat door naar 28° (rode wig, "+8° past limit"), houdt 0,8 s stil, en veert terug naar 15°. Versnellen en vertragen (ease in en out), geen schokken. |
| 11,5 tot 15,0 | kop4 "Watertight parts. STL or 3MF." | Exploded view: deel B schuift in 1 s van de kogel af (de knop springt aan of uit; zet daarom zelf per beeld `delta_location` van deel B en laat Exploded view in scène 1 tot 3 uit, want hij staat standaard aan), zodat je kogel en kom ziet; daarna kort het paneel met STL / 3MF en "Export STL". |
| 15,0 tot 18,5 | eindkaart | Icoon, "Click Joints for Blender", "See how far it bends, before you print.", groene knop "Free on Blender Extensions", "Ball and pin joints · STL and 3MF · Blender 4.2 to 5.2", "Made by Thijs at Dortus". |

Alleen gratis functies in beeld (regel 6.2 van extensions.blender.org en de winkelzin): kogel, passing, bereik, rood, Exploded view, export. Geen scharnier, geen prijs, geen "Pro". Getal overal ±20°, rood bij 28° ("+8°"), net als poster en winkelplaatje 2.

## De figuur (versie 2 van de plaatjes, moet in het filmpje)
Geen buizen meer: een **houten tekenpop** (de beweegbare pop die tekenaars gebruiken), zelf gemaakt in Blender uit eenvoudige vormen, dus geen licentiegedoe.
- Vormen: eivormig hoofd, borst en bekken als afgeronde blokken, ledematen als taps toelopende cilinders met zachte randen (Subdivision of afgeronde eindkappen), bolletjes bij schouder, heup en knie. Eén mesh, waterdicht (de add-on vraagt dat).
- Houding: staand, gewicht op één been, rechterarm iets van het lijf, elleboog licht gebogen. Zo zie je meteen "dit is een figuur die gaat bewegen".
- Kleur: warm licht hout `#D9C2A0` als objectkleur in Solid, Studio-licht, de groene naad van de add-on blijft zoals hij is (die kleur is de belofte).
- Maat: rond 120 mm hoog, onderarm dik genoeg dat Auto een kogel met "Good fit" en "Bends ±20°" kiest (anders past de kop niet bij de winkel). Is ±20° op de elleboog niet te halen, dan de onderarm dikker maken, niet een ander getal in beeld.
- Viewport: achtergrond effen `#2B2E35` (past bij de kaart), geen raster, geen assen, geen 3D-cursor, geen statistieken; de boog en de kleuren van de add-on blijven aan.

## Hoe Bram het opneemt (voorstel, Bram beslist over de techniek)
1. Een eigen script naast `e2e/schermen.py` (bijvoorbeeld `e2e/film.py`) in de workflow, op een eigen tak, met Xvfb 1920 x 1080 zoals de winkelschermen.
2. **Beeld voor beeld, niet realtime:** per beeld de toestand zetten (camera, Bend, Exploded view), viewport laten tekenen en met `import -window root` vastleggen (zoals `schiet` met `-x`). Rond 420 beelden voor scène 1 tot 4. Naamgeving `scene1/0001.png` enzovoort.
3. Log de schermplek van de elleboog bij de klik (pixel x en y in het venster); het pijltje en de ring tekent `maak_film.py` erbij, want de muis van X staat niet op de opname.
4. Zet de mappen met beelden als artefact of op de tak `schermen` (map `blender-gewrichten/film/`), en maak het filmpje met mijn script:
   `python3 ontwerp/click-joints/film/bron/maak_film.py draaiboek.json click-joints-film.mp4`
   In `draaiboek.json` wijst elke scène naar een map met beelden in plaats van een los plaatje (voorbeeld: `film/bron/storyboard.json`). Paden in `draaiboek.json` (ook `"lagen"`) gelden vanaf de map waar dat bestand staat: zet `"lagen"` naar `ontwerp/click-joints/film`. Per scène kun je `uitsnede`, `zoom` en `zoompunt` zetten (de zoom naar het paneel in scène 2 en 4 kan dus ook achteraf).
5. Zet het resultaat op de tak `schermen` of in `ontwerp/click-joints/film/` en schrijf het onderaan `producten/blender-gewrichten/ontwerp.md`. Ik keur het beeld voor beeld (eerste beeld, klik, 15°, 28°, exploded, eindkaart).

## Wat er al staat (in deze map)
- `bron/film.html` en `bron/lagen.py`: de lagen (achtergrond, rand en masker van de kaart, vier koppen, eindkaart), gerenderd als PNG in deze map.
- `bron/maak_film.py`: zet lagen en beelden in elkaar (overgangen, koppen, klik met pijltje en ring, zoom) en maakt de MP4 met ffmpeg.
- `storyboard.mp4`: proef met de winkelschermen van nu (buizen, losse plaatjes, dus geen echte beweging). Alleen om opbouw, tijden en lagen te zien; **niet voor de winkel.**

## Klaar als (ik toets dit)
1. 15 tot 20 s, 1920 x 1080, H.264, onder 8 MB.
2. Eerste beeld zonder geluid meteen duidelijk: figuur plus kop.
3. Beweging vloeiend (geen sprongen tussen beelden, geen zwarte of halve beelden).
4. Getallen gelijk aan winkel en poster: ±20°, +8° bij 28°, Good fit, wand in mm.
5. Paneeltekst leesbaar waar de kop ernaar verwijst.
6. Alleen gratis functies, eindkaart zoals hierboven.

## Controleur (agent, 8 nov)
Eerst nee, twee moet-punten in `maak_film.py`, beide opgelost en opnieuw bekeken met de Read-tool: (1) bij elke wissel liepen twee koppen door elkaar (de kop zat in het beeld dat werd gemengd); nu gaat de oude kop weg en komt de nieuwe daarna, beeld 92, 96, 198 en 202 schoon; (2) het eerste beeld had geen kop; nu staat kop 1 er vanaf beeld 0. Kan-punten verwerkt: beeldnummer zonder afrondfout, Exploded view met `delta_location`, Resolution Scale, pad van de lagen, uitsnede scène 4 niet meer half door het paneel, "Wall: 1.54 mm". Teksten en getallen klopten al met de add-on (±20°, "+8° past limit", stapnamen, alleen gratis).

## Beeldtaal filmisch: besluit Daan (9 nov 02:35 UTC), voor Bram
Bekeken (GEZIEN, Read-tool): `click-joints-filmisch-ruw.mp4` van run 42545243113 (ronde 4b, c1af5396), contactvel van 18 beelden en losse beelden op 1,0 / 4,5 / 9,3 / 13,5 s.

**Oordeel: nee, nog niet goed genoeg voor de winkel.** De opbouw (held, gewricht, buigen, uit elkaar) klopt en de groene ring gloeit mooi. Maar het oogt als grijs plastic in een lege studio, niet als iets wat je wilt hebben. Vijf moet-punten, op volgorde:

1. **Het gewricht zit midden in de onderarm, naast een elleboog die al gebogen is.** Je ziet een pop met twee ellebogen. Maak de arm in rust recht (bovenarm en onderarm in één lijn, schuin naar voren en 30° omlaag) en zet het gewricht **op de elleboog**. Dan leest buigen als "zijn arm beweegt", meteen, zonder uitleg. Lukt de snede daar niet vrij van het lijf: arm verder van het lijf, niet het gewricht ergens anders.
2. **De harde horizon moet weg.** Nu loopt er een lichte rand van de vloer dwars door elk beeld (achter de pop, achter de arm). Gebruik een **oneindige achtergrond**: vloer die met een ronde bocht (bevel ±40 mm op schaal van de pop) overgaat in een achterwand, zelfde materiaal, of een vloer die zo groot is dat de rand nooit in beeld komt en wegvloeit in de kleur van de wereld. Lichtvlek van de hoofdlamp op de vloer rond de voeten, de rest loopt weg in donker `#121418`.
3. **Echt hout, warm.** Nu grijsblauw. Basiskleur beuken `#C99C6E`, nerf met een Wave-textuur (bands, langs de lengte van elk lid, vervormd met Noise schaal ±3, sterkte 4), tweede tint `#A9774A`, roughness 0,4, coat 0,3. Hoofdlicht warm (3200 K, Blackbody), randlicht koel (8000 K) van achter. Kleurbeheer AgX met look **Medium High Contrast**. Toets: in het eindbeeld moet je zonder twijfel "hout" zeggen.
4. **Het rood moet je zien.** Bij 28° is er nu geen rood te zien (log: 25 rode vlakken in A, maar ze zitten binnen in de naad). Kies voor dat moment een camera **aan de binnenkant van de bocht**, dichtbij, waar de naad openvalt en de rode vlakken naar de lens wijzen. Rood als emissie (sterkte 3 tot 4, kleur `#FF3B30`) met de gloed van de compositor, en een korte puls (twee keer). Is het van geen kant te zien, dan is het eerlijke alternatief: een inzet van het echte viewport (de witte boog met "+8° past limit") in de hoek, uit de schermopname van ronde 2. Liever het eerste.
5. **Kader en camera.** Nooit een half hoofd of half lijf aan de rand (nu in shot 2 tot 4). Bij close-ups: schouder en hand allebei in beeld, gewricht op een derde van het beeld. Camerabewegingen met zachte in- en uitloop (Bezier), geen stilstand en ook geen schok.

**Wat ik erbij wil (dit maakt het van ons, niet alleen netjes):**
- **Haak in de eerste 0,5 s:** dichtbij de elleboog, donker, de groene ring flitst aan. Pas daarna de held-shot. Wie zonder geluid scrolt, ziet meteen licht en beweging.
- **Slotbeeld "hij leeft":** zet met de echte add-on **drie gewrichten** (nek, elleboog, knie), alle drie groen. In het laatste shot buigen ze tegelijk binnen hun grens (nek knikt, arm zwaait, knie buigt), camera laag en langzaam eromheen. Dat is precies wat een maker wil: een figuur die beweegt. Eerlijk, want elk gewricht is echt geplaatst. Lukt drie niet in deze ronde, dan twee (elleboog en knie).
- **Koppen en eindkaart blijven**, met mijn lagen uit `maak_film.py` (zelfde vier koppen en eindkaart, de kaart iets kleiner zodat de render het beeld draagt). Getallen ±20° en "+8° past limit" komen in de koppen, gelijk aan de winkel.
- Lengte 16 tot 18 s, 30 beelden per seconde, 1920 x 1080.

Volgorde shots (voorstel, Bram mag de tijden schuiven): haak 0,5 s, held 2,5 s, gewricht verschijnt 2,5 s, buigen 0 tot 15 tot 28 met rood en terug 4 s, uit elkaar 2,5 s, drie gewrichten 3 s, eindkaart 2 s.
Ik keur beeld voor beeld zodra de ronde op `schermen` staat. Schrijf het onderaan `producten/blender-gewrichten/ontwerp.md`.
