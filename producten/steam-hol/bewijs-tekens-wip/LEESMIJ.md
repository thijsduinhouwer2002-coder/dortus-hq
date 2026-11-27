# Tekens boven een held poppen op en gaan zacht weg (Olaf, 27 nov 2026, issue #85)

Thijs zei op 24 nov dat de helden niet opvallen. Een teken (boos, zweet, "!", zzz, ster, sprongteken) knipte in één beeld aan en uit en stond daarna stil. Les uit Godot Open RPG (GDQuest, MIT, `ui_popup.gd`): groeien, af en toe een wip met een pauze ertussen, korter weg dan komen.

**Wat de speler nu ziet (keuzes Sanne):**
- Een teken komt in 0,2 s: het 3D-teken groeit uit het hoofd van klein (een kwart) naar vol met een zachte rem en wordt in die tijd van doorzichtig vol. Een pixelteken (oog van de magier, strepen van de dief, tekens.png zonder 3D-blad) schaalt nooit: dat wipt 2 hele spelpixels omhoog en zakt terug.
- Zolang het teken staat: elke 2,5 s één wip van 1 spelpixel (rustig, naast je werk).
- Weg in 0,15 s: krimpt en vervaagt, vanaf waar het was (ook midden in het komen). Wisselt het teken ("!" wordt zweet), dan gaat het oude zacht weg terwijl het nieuwe opkomt.
- Het sprongteken (sprong 0,6 s) krijgt alleen de komwip. De poef bij de val is zijn eigen beeldje en blijft zoals hij was.
- Geen nieuwe tekens, geen tekst, geen geluid.

**Bewijs (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie`, 20 beelden per s, demo-film `hoogte=120 demo=1 vers=1 film=1`):**
- `tekens-wip-26s-ware-maat.mp4`: 26 s ware maat met geluid (speltijd 14 tot 40 s, uitsnede van het hol). Rond 1,2 s springt een held over de put met een "!", landt en vlucht met zweet; rond 19,9 s ziet een held de schat ("!") en vlucht met zweet als Gloop hem slaat.
- Beeld per beeld op 4x (elk vakje is 1/20 s):
  - `1-sprong-uitroep-komt-4x.png`: sprongteken. Beeld 304 een stipje, 305 half en doorzichtig, 306 vol.
  - `2-sprong-uitroep-weg-zweet-komt-4x.png`: na de landing gaat de "!" in beeld 317 half doorzichtig en kleiner weg terwijl de zweetdruppel opkomt; 318 alleen zweet.
  - `3-schat-uitroep-komt-4x.png`: "!" bij de schat. Beeld 678 klein en grijs, 679 bijna vol, 680 vol.
  - `4-schat-uitroep-weg-zweet-komt-4x.png`: "!" bij de schat gaat weg en zweet bij vluchten komt op (beeld 769 tot 771).
- Toets `systemen/toetsen/toets_tekens.gd` (14 keer OK, 0 FOUT): eerste beeld klein en doorzichtig; groeit in 0,2 s tot vol zonder terug te krimpen; pixelteken alleen 0, 1 of 2 spelpixels hoog; pauze-wip op 2,46, 4,96, 7,46 en 9,96 s; geen pauze-wip bij een sprong; weg in 0,15 s; weg midden in het komen krimpt vanaf waar het was; vier echte helden (vallen, vluchten, dief, magier) met 20 beelden per s door een hol met een put: "!", zweet, strepen en oog komen en gaan, 12 wissels, 0 keer een teken dat van bijna vol ineens weg is of uit het niets bijna vol staat.
- Alle andere toetsen 0 FOUT (held 310, systemen 427, namen 50, vleermuis 56, berg-wand 13, klap 30, aanloop 7, licht 48, opslag 23).

## CPU (eis Sanne: hooguit +1 procent, om en om gemeten)
1. **Om en om binnen één run (GEZIEN):** `wissel=tekens` zet de wip om de 20 s aan en uit (uit = knippen zoals vroeger), `wissel=nep` schrijft dezelfde regels maar laat hem aan (placebo). Linux xvfb, `vers=1 zaad=5 koper=1`, 12 min, twee runs tegelijk op 2 kernen, alle seconden (met een koper is er bijna altijd een held). Script `platformen/steam/data/cpu-duur/cpu_stenen.py` (leest nu ook `wissel tekens`), ruwe meting en startscript in `platformen/steam/data/cpu-duur/tekens/`.

| run | aan | uit | verschil | buurparen |
|---|---|---|---|---|
| echt (wip aan of uit) | 1,404 | 1,352 CPU-s per 10 s | +3,9 % | +4,1 ± 3,8 |
| placebo (altijd aan) | 1,445 | 1,297 | +11,4 % | +11,5 ± 3,2 |

De aan-blokken zijn in deze runs vanzelf duurder (placebo +11). Echt min placebo: **-7,5 procent, met een ruis van ±5**: niet te onderscheiden van nul; een stijging is niet te zien. Deze meting alleen kan +1 niet hard bewijzen.
2. **Wat het werk zelf kost (GEZIEN, 200.000 aanroepen headless):** `held_wip.stand` kost 1,5 microseconde per held per beeld. Het spel tekent 100 tot 140 beelden per 10 s met 1 tot 2 helden (`HOL meting` in de run), dus hooguit ±420 aanroepen per 10 s = 0,0006 CPU-s per 10 s, tegen 1,35 CPU-s per 10 s voor het hele spel: **±0,05 procent**. Tekenen kost niets extra behalve 0,15 s lang een tweede teken als het oude weggaat terwijl het nieuwe komt; het 3D-teken schalen is dezelfde tekenbeurt.

**Mijn oordeel:** ruim binnen +1 procent (punt 2, GEZIEN); de om-en-om-meting ziet geen stijging (punt 1).

## Nakeuring Daan #237: het nootje knipt niet meer (Olaf, 27 nov ±04:30 NL)
Daan zag in strip 1 een muzieknootje dat in beeld 303 nog vol was en in 304 ineens weg. Oorzaak (GEZIEN in een logregel per beeld): de nootjes hangen aan de kruin van het hoofd; bij het sprongbeeld ligt die kruin 2 spelpx hoger, het nootje kwam dan 3 spelpx boven de grens onder het gras en werd daar in één beeld op 0 gezet. Wat de speler nu ziet:
- De hoogte van de nootjes glijdt zacht mee (hooguit 20 spelpx per s) in plaats van te springen, dus aan die rand vervaagt een nootje geleidelijk. Ze doen de hop van de sprong ook niet meer mee: ze zweven los in de lucht.
- Elk nieuw nootje komt in 0,2 s op van doorzichtig naar vol (eerst stond het er meteen vol).
- Het nootje van een held die door het lied komt gaat in 0,15 s weg: aan het eind van zijn 2 s, of eerder als er een teken boven die held opkomt. Valt een held, dan vervagen zijn nootjes in 0,15 s (eerst meteen weg).
- Bewijs, zelfde demo-film als hierboven, beeld per beeld op 4x (GEZIEN): `5-nootje-voor-knipt-4x.png` (beeld 303 vol, 304 weg) en `6-nootje-na-vervaagt-4x.png` (303 vol, 304 half doorzichtig, 305 weg).
- Toetsen: `toets_tekens.gd` 18 OK, 0 FOUT (nieuw: lied-nootje komt en gaat met hooguit 0,4 dekking per beeld, gaat weg als een teken het overneemt, nieuw bard-nootje begint bijna doorzichtig, glijden 1 spelpx per beeld). Alle 10 toetsen 0 FOUT op Linux (GEZIEN).
- CPU: per held per beeld een paar rekenstappen en twee getallen in `h.wip`, geen extra tekenbeurt (GOK: niet te meten naast de ±0,05 procent van de tekens zelf).
