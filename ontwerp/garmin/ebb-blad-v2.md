# Ebb blad v2: alle schermen, ronde 2 (Mila, 10 nov run 17, 20:45 UTC)

Blad: **`ontwerp/garmin/ebb-blad-v2.png`** (per scherm links 454 px, rechts 260 px, ware grootte). Losse beelden en meting in `ontwerp/garmin/blad2/` (`meting-v2.txt`), bron `ontwerp/garmin/bron/ebb_blad_v2.py`. Vervangt blad v1. Gaat eerst naar Thijs via de hoofdchat; Gijs bouwt pas na zijn ja.

Opdracht: de frisse keuring van blad v1 (`ebb-blad-v1-frisse-keuring.md`, 5 van 10, tien moet-punten), door de hoofdchat overgenomen. De beeldtaal uit v1 (10 regels, bovenaan `ebb-blad-v1.md`) blijft, met drie wijzigingen: regel 3 (geen bouten meer op de schermen, alleen een dunne ring), regel 4 (één schaal van vier blauwtinten met dithering in plaats van harde banden) en regel 7 (tekst wordt nooit meer door de golf gesneden).

## Wat er per moet-punt veranderde (GEZIEN met Read, gemeten in `meting-v2.txt`)
1. **Golf uit het cijfer.** Op ademen, boven komen en rustig ademen staat het getal helemaal boven het water, altijd wit. Het peil zakt en stijgt alleen onder het getal (hoogste peil 60% D, onderkant van het getal 55% D).
2. **260 px: kleinste tekst 17 px = 12 px kapitaalhoogte** (gemeten met de letter zelf). De functie `tekst()` laat niets kleiner toe. Wat niet paste is eruit: "breaths" in het menu, "My pattern" in settings, "Sit or lie down" op het veiligheidsscherm (dat staat in de winkeltekst en bij de eerste start).
3. **Grijs is #AAAAAA**, contrast 9,0:1 op zwart (was 2,8:1). Wit op W1 7,3:1, schuim op W1 5,9:1.
4. **Ring 3 px op 454, 2 px op 260, zonder bouten.** Bouten alleen nog in het icoon.
5. **Eén waterschaal:** W0 0x00AAFF (oppervlak), W1 0x0055AA, W2 0x0000AA, W3 0x000055. Dezelfde op menu, ademen, duiken, boven, rustig en de grafieken. Tussen twee banden twee rijen dithering (25% en 50%), zodat het zacht overloopt met alleen MIP-kleuren.
6. **Dieren in één stijl:** gevulde vlakken zonder lijnen, lichaam in een eigen tint, buik een tint lichter, vin of poot een tint donkerder, bij alle vier hetzelfde oog (wit rondje met nachtblauwe pupil, glansje als het dier groot is). Allemaal naar links. Tinten binnen koraal: walvis 0xFF5555, vis 0xFFAA55, kwal 0xFF55AA, schildpad 0xFF5500. Geen waterstraal onder water; het spuitje zit alleen in het menu, waar de walvis aan de oppervlakte ligt.
7. **Optisch midden:** elk dier wordt geplaatst met zijn zwaartepunt (alle getekende pixels) op het midden, niet met zijn kader. Dus ook het icoon en het menu.
8. **Sea log:** drie kolommen op precies gelijke afstand (21,5% D), drie dieren even zwaar (oppervlak 434, 445 en 433 px op 260, binnen 3%). De walvis eronder groter, als het donkere silhouet dat je nog moet halen.
9. **8 weeks:** één lijn (je beste tijd per dag, met gaten waar je niet ademde) op een doorlopend getij-vlak, één koraal stip op je beste dag met het label "best 2:08" eronder. De stip ligt 55 px van de rand op 260 (eis 15).
10. **Today:** drie herkenbare duiken: een U met vlakke bodem, de diepte is je inhoudtijd, de tijd onder elke duik; het record in koraal met "new best".

Ook de kan-punten: één titelkleur (schuim) voor alle fasewoorden en titels, geel alleen voor de zon; dithering; veiligheidsscherm rustig (teken, twee regels, OK, geen golf); belletjes in verschillende maten en niet gespiegeld. Niet gedaan: een andere houding van de walvis per scherm (kan-punt 3); dat is de volgende stap.

## Midden (harde regel 20:20)
Kader van alles wat getekend is: op alle 24 beelden binnen 1 px van het schermmidden (eis 2 px).

## Voor Gijs (pas na het ja van Thijs)
- Dieren: `dier_delen()` geeft de veelhoeken in eenheden (lengte 2), `dier()` zet ze op hun zwaartepunt; reken dat zwaartepunt één keer uit (zie `dier_beeld()`) en zet de verschuiving vast in de code.
- Dithering: twee stroken van 2 px boven elke bandgrens met een vast patroon; op het horloge het makkelijkst als kleine bitmap van 2 x 2 die je langs de golf herhaalt, of als vaste PNG per band (GOK: geheugen klein, de banden bewegen niet tijdens de duik).
- Letter: Barlow Condensed Medium, kleinste maat 17 px op 260 en in verhouding op grotere schermen.
- Geen `setClip` meer nodig voor het getal: het staat boven het water.
