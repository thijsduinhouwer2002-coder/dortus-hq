# Reeksproef 2: plaatje, eigen cijferletter, slaapbeeld (Gijs, run 124, 16 nov 2026)

**Wat en voor wie:** een meting voor Mila en Daan, geen product. Vraag: wat kost een schermvullend plaatje per thema en een eigen cijferletter aan geheugen op een wijzerplaat (131.072 bytes op de meeste horloges, 98.304 op de Forerunner 55), en hoe ziet een slaapbeeld eruit.
**Af als:** in `uitslag.txt` op de tak `schermen` staan voor fr255, fr55 en fenix847mm de regels `KERN FONT`, `KERN SCHERM`, `KERN PLAATJE bytes=` en `KERN SLAAPBEELD`, de 3 toetsen zijn groen, en beeld 1 (wakker) en beeld 3 (slaap) zijn bekeken.

**Bestanden:** `source/KernView.mc` (meten in `meetBeelden`, slaapbeeld in `tekenSlaap`), `maak_proefbeelden.py` (maakt de plaatjes en de letter), `resources/fonts/`, `resources-round-208x208`, `-260x260`, `-454x454` (plaatje op de echte schermmaat), de bouwstraat `.github/workflows/garmin-reeks-kern.yml`.

**Open vragen, zelf beantwoord:**
- Past het plaatje niet in het geheugen, dan stopt de app. Dat is ook een uitslag; daarom worden de letters eerst gemeten en staat er een regel `KERN PLAATJE laden` voor het laden.
- De slaapstand zet de simulator niet vanzelf aan vanaf de opdrachtregel (GOK, niet gevonden hoe). Daarom tekent de proef 6 s na het eerste beeld zelf het slaapbeeld (14 s bleek te laat voor de schermafbeelding). `echt=true` in het log zou betekenen dat de simulator het wel deed.
- De regels van Garmin voor inbranden (hoeveel pixels aan) meet deze proef niet; hij print alleen of het horloge er om vraagt (`inbrand=`).

**Aanpakken:** (1) alleen rekenen uit de pixelmaat: snel, maar zegt niets over of plaatjes op nieuwe horloges buiten het geheugen van de app vallen. (2) Laden en het geheugen ervoor en erna printen: klein en geeft het echte getal van de simulator. (3) Vier thema's laden en wisselen: zegt meer, maar is tekenwerk van Mila dat er nog niet is. **Gekozen: 2.** Eén plaatje is genoeg om te weten of het idee kan.

**Niet gedaan:** keuring door een andere agent (stap 6 van bouwen-in-stappen): dit is wegwerpcode die niet naar de winkel gaat; de bouwstraat is de toets.
