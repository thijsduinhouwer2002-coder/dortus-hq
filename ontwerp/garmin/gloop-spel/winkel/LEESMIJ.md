# Gloop: Hat Tower, winkelbeelden (Mila)

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
