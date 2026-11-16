# Gloop: Hat Tower, winkelbeelden (Mila)

## v2, de vijf voor de upload (16 nov ±20:40 tot 21:00 UTC)
Uit run 43944787840 (commit 07b9999, 52 horloges, donkere grot op AMOLED). Elk scherm is een echte opname op 1x, uitgesneden uit het simulatorbeeld (Venu 3 op x 92, y 232, 454 px; FR255 op x 80, y 184, 260 px), bronnen in `bron/r122-*.png`. Script: `ontwerp/garmin/bron/gloop_winkel_v2.py`. 800x800, zelfde grot en letter (Lilita One) als het icoon.

1. `1-taller.png`: **"A tower of hats taller than your watch."** (venu3-21, GULP! x8, 12 hoeden). Zelfde zin als de eerste regel van Chris. De toren loopt buiten de kast door met hoeden uit de kit; in het spel loopt hij echt over de bovenrand. Frisse kijker: 9, sterkste, daarom vooraan.
2. `2-feed-him.png`: **"Feed him. Keep the hat."** (venu3-22, held ondersteboven in de mond, 12 hoeden).
3. `3-wait-for-it.png`: **"Wait for it... GULP!"** (venu3-25, held met "!" bij de open mond, 14 hoeden). Zegt hoe je speelt: op tijd drukken.
4. `4-one-button.png`: **"One button. That's the manual."** (venu3-01, startscherm met titel).
5. `5-older-watch.png`: **"Old watch? Gloop doesn't mind."** (fr255-16, GULP! x4, 8 hoeden), MIP precies 2x met scherpe pixels.

GEZIEN met Read: alle vijf op 800 en samen op 200 px (`strook-v2-200.png`). Frisse kijker (Agent) op de eerste versie: koppen lezen op 200 px, kleine onderregels niet (dat mag, ze zijn extra). Op zijn punten veranderd: het eindscherm "15 HATS" eruit (de zwarte balk verbergt de toren en het eindgezicht las als kapot gezicht), MIP-beeld zonder afgesneden held en zonder waas, en een kop met grap in plaats van uitleg.
Zwak (eerlijk): op beeld 4 staat `PRESS = GULP` over Gloops mond (Daans kan van 13:50, zit in het spel); gaat Gijs dat nog verplaatsen, dan neem ik beeld 4 opnieuw op. Het eindgezicht (oog dicht, tandje) leest op een stilstaand beeld als een "3": voor een volgende versie van het spel, geen voorwaarde voor upload.
Keuring op fouten en leesbaarheid: Daan.


## Concept 1 (16 nov ±07:00 UTC): nog niet indienen
`blad-concept-1.png` (op 800 en op 200 px). 800x800 zoals Ebb. Elk scherm is een echte simulatoropname op 1x (map `bron/`, uit tak `schermen`, map `garmin-gloop/claude-garmin-gloop-2026-11-16/`), in een getekende horlogekast zonder merk. Achtergrond is de donkere warme grot van het icoon, letters Lilita One zoals Het Hol.

1. `concept-1-feed-him.png`: **"Feed him. Keep the hat."** De grap van het spel in vier woorden: Gloop slokt de held op en houdt zijn hoed. Scherm: slok "GULP! x3" bij 7 hoeden (venu3-14). Wordt vervangen door een slok bij 10+ hoeden (wens Daan), zodra Gijs die in de bouwstraat vasthoudt.
2. `concept-2-taller.png`: **"A tower of hats taller than your watch."** De toren loopt in het spel over de rand van het scherm; hier gaat hij buiten de kast door met dezelfde hoeden uit de kit, steeds schever. Dat is de haak: je ziet in één tel wat je doet en dat het misgaat. Eerlijk: wat buiten het scherm staat, zie je in het spel niet; het is de belofte uit de openingsregel van Gijs, met alleen hoeden die in het spel zitten. Daan mag zeggen of dat te ver gaat.
3. (eindscherm "15 HATS / NEW BEST!") wacht op de moet van Daan (rand om "START = AGAIN").
4. (held valt met "!") volgt.
5. `concept-5-mip.png`: **"Same Gloop. Older watch."** FR255 (260 MIP) vergroot naar 454, je ziet de pixels; eerlijk over wat een MIP-koper krijgt.

GEZIEN met Read: alle drie op 800 en de strook op 200 px. Zwak (eerlijk): op 200 px is de slok in beeld 1 klein, en het oranje scherm steekt weinig af tegen de bruine grot. Beide worden beter als het spel op AMOLED de donkere grot krijgt (zie hieronder) en de slok bij een hoge toren komt.

## Voorstel aan Gijs: donkere grot op AMOLED
`voorstel-donkere-grot-amoled.png`: links het spel nu (effen oranje), midden en rechts dezelfde opname met alleen de achtergrondkleuren vervangen (script `bron/gloop_spel_donker_voorstel.py`): warm in het midden achter Gloop, bijna zwart aan de rand, lichtbaan erover. Waarom: het icoon is zo (zes blinde kijkers: donker wint tussen de toppers), Gloops mint en de gele teksten springen eruit, de rand loopt over in de zwarte kast van het horloge zodat het scherm groter lijkt, en zwarte pixels kosten op AMOLED minder stroom. MIP blijft effen zoals nu (64 kleuren).
Script: `bron/gloop_winkel_v1.py`.

## 16 nov ±08:00 UTC: beeld 1 met de slok bij 12 hoeden
- `concept-1-feed-him.png` nu uit `bron/venu3-22.png` (run 43822689413, Venu 3, 1x): "GULP! x8", 12 hoeden, toren loopt boven over de rand. GEZIEN met Read op 800 en 200 px: op 200 leest de toren nu als toren, niet meer als klein figuurtje. Zwak: het dunne systeemfont van de Venu ("GULP! x8", "12"); verbetert zodra Gijs het nep-vet bouwt. Opnieuw opnemen zodra de donkere grot erin zit (dan ook beelden 2 en 5).
