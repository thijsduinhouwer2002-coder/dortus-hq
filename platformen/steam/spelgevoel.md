# Het Hol: spelgevoel en toetsen van het prototype (Sanne)

Hier toets ik elke GIF en elke schermafbeelding van het prototype: is het leuk, is het duidelijk, is het grappig. Nieuwste bovenaan. Wat er in het spel hoort staat in `features.md`.

## Toets 2: hol met Daans kunst, 9 nov 2026 (run 42685438422, commit ce73494, main)
**Bekeken (GEZIEN):** `film.gif` op tak `schermen` (`steam-hol/main/`, 1024 x 120, 281 beelden), tien beelden op ware grootte onder elkaar, de val bij beeld 40 tot 56 en het einde (270 tot 280) twee keer vergroot, `film.log` en `cpu.txt` (1,03 CPU-s per 10 s op 120 px, 113 MB). Daans karakter-laag (kleuren per naam, littekens, tekens, paneel) zit er nog niet in; dat staat op Olafs lijst, dus daar oordeel ik nog niet over.

**Wat beter is dan toets 1 (punt 1, 4 en 6 van toets 1 zijn opgelost):**
- **Er komt goud binnen.** Na 10 s valt Kees in de stekelput, na een minuut staat er 12 goud. Vier van de zes helden vallen, twee vluchten. Dat is precies de eerste minuut die we wilden (T1).
- **De val leest goed.** De held loopt op de put, de pinnen schieten omhoog en hij is weg in twee beelden. Kort, duidelijk, een beetje gemeen. Goed.
- **Het ziet er voor het eerst uit als een spel:** gras met plantjes, fakkels, vaandel, de schatberg die glinstert, gangen in twee rijen. Het hol groeit tijdens de film (kolom 4, 13, 5, 6 gegraven).
- Geen afgekapte tekst meer. De wrok staat in de log (twee regels): "Ties the Once-Fled is back!" en "Grudge: the Spike Pit."

**Wat niet goed is (in volgorde van belang):**
1. **Gloop ligt de halve film plat** (vanaf ±28 s tot het einde; de GIF heeft eerst één beeld van 4 s, daarna beelden van 0,2 s). In de film komt er elke 6 tot 9 s een held (`strook.gd` regel 194, demo), maar Gloop blijft 60 s plat (`slijm.gd` PLAT_S). In het echte spel is 60 s plat ongeveer één held overslaan; in de film zijn het er vier tot vijf. Ook komt de regel "Gloop is flat. Back in a minute." nooit in de kroniek (`regel_plat()` wordt niet aangeroepen), dus je snapt niet waarom hij plat ligt. Daardoor doet de stekelput al het werk en is de film eentonig: vier keer dezelfde dood op dezelfde plek. **Eis:** in de demo alles even snel versnellen, ook plat zijn (60 s x 7,5/50 = ±9 s). Dat verandert niets aan de balans van Bram's sim, alleen aan wat de film laat zien.
2. **Je ziet het goud niet binnenkomen.** "+3 gold for your hoard" staat als losse regel en vervangt de regel van de val, dus je leest of de dood of het goud. Het fijnste moment van een idle-spel (iets binnen zien komen) zit nu alleen in een getal. **Eis:** drie muntjes springen van de put naar de schatberg (een halve seconde, alleen als er toch getekend wordt) en de regel wordt één regel: "Kees fell to the Spike Pit. +3" (zie `kroniek-regels.md`).
3. **De wrok is nog niet te zien op het poppetje.** Ties komt terug met een litteken van 1 bij 2 rode pixels (`held.gd` r.217), maar dat valt weg tegen zijn rode hemd. Er zweeft wel een klein rood kruisje, maar dat staat 3 spelpixels boven de hoed in de aarde en leest als "dicht" of "dood", niet als boos. Daan heeft `tekens.png` en `held_littekens.png` klaar; dat is Olafs volgende stap. **Eis:** teken direct boven het hoofd (1 of 2 spelpixels), en een litteken dat je bij terugkomst meteen ziet.
4. **Alle helden lijken op elkaar.** Vijf van de zes dragen dezelfde rode band en hetzelfde rode hemd; alleen de tovenaarshoed en één helm wijken af. Op 120 px is kleur het enige wat je in één blik ziet. Daans `held_lijf_kleuren.png` (vaste kleur per naam) lost dit op; graag tegelijk met punt 3.
5. **Een dode held komt terug met dezelfde naam.** Kees valt na 10 s, en na 40 s staat er "Kees the hero climbs in." Je denkt dat hij terug is, maar het is een nieuwe Kees zonder wrok. Dat is verwarrend, want terugkomen is juist ons eigen stuk. **Eis:** een naam van een gevallen held niet opnieuw gebruiken. Is een naam toch weer aan de beurt, dan als "Kees II" (geen wrok, wel een regel "Kees II climbs in. Kees fell here once."). Zo komt de grap uit "De kinderen van je aartsvijand" (`features.md`, versie 1) al klein in het prototype, zonder extra systeem.
6. **Niemand komt bij de schat.** De Hoard-Toucher van Bram is nog niet aangesloten (staat op Olafs lijst). In de film staan twee helden even naast de stapel en lopen weer weg. Dat blijft een gemiste grap tot hij erin zit.
7. **Het rechterderde deel van de strook is lege aarde.** Het hol stopt bij de schat op ±2/3 van de breedte, daarna steentjes tot het tekstvak. Wanneer je graaft, schuift de schat mee, maar in de film blijft het rechterstuk leeg. Kan de schat tegen het tekstvak aan staan, met het hol ervoor, zodat graven het hol naar links laat groeien? Dan is de strook altijd vol. Olaf beslist.

**Op de andere hoogtes (GEZIEN, `strook-96.png` en `strook-160.png` van dezelfde run):**
- **160 px (schaal 4): het tekstvak ligt over de schat.** Het hol is 256 spelpixels breed, dus de schatkamer komt precies onder het tekstvak; je ziet alleen het vaandel en de bovenkant van de stapel. Dit is het belangrijkste punt van deze toets: wie de strook groter zet om meer te zien, ziet zijn eigen schat niet meer. **Eis:** het hol eindigt altijd links van het tekstvak (of het tekstvak schuift weg tot hover).
- **96 px (schaal 2):** het hol neemt maar ±45% van de breedte, de rest is lege aarde tot het tekstvak. Hier geldt punt 7 nog sterker.

**Controleur (agent, 19:58):** feiten nagelopen tegen film, log en code; vier kleine onjuistheden verbeterd (halve film plat in plaats van twee derde, litteken is er wel maar valt weg, plat-regel ontbreekt, wrok in twee regels).

**Oordeel:** een grote stap. Het ziet eruit als een spel, er komt goud en de val is lekker kort. Wat nog mist om het aan Thijs te laten zien: de schat mag nooit onder het tekstvak liggen (160 px), Gloop moet meedoen (punt 1), het goud moet je zien vliegen (punt 2) en de wrok moet op het poppetje staan (punt 3 en 4). Punt 1 is één regel, punt 2 is klein, punt 3 en 4 zijn Daans kunst aansluiten. Doorgegeven aan Olaf en Bram.

## Toets 1: eerste kern, 9 nov 2026 (run 42676196548, commit dfd139e, tak `claude/steam-hol-kern`)
**Bekeken (GEZIEN):** `film.gif` (1024 x 120, 281 beelden, een minuut), zes beelden naast elkaar op ware grootte, `film.log`, `cpu.txt` op tak `schermen` (`steam-hol/claude-steam-hol-kern/`). Kunst is nog tijdelijk (Daans bladen zitten er nog niet in), dus over het uiterlijk oordeel ik niet; dat is Daan.

**Wat goed is:**
- Het draait, zuinig (1 CPU-seconde per 10 s op 120 px, GEZIEN in cpu.txt) en de strook is echt klein.
- De kern van ons eigen stuk werkt al in de log: "Kees escaped and is now Kees the Once-Fled. Grudge: Gloop the Slime." en "Kees the Once-Fled is back." Dat is de zin waar het spel om draait.
- Helden met namen die binnen druppelen, elk in een andere kleur: je ziet in één blik dat er iets gebeurt.

**Wat niet goed is (in volgorde van belang):**
1. **Na een minuut nog steeds "Hoard: 0 gold".** In de hele film valt niemand: alle helden vluchten (log: Kees, Mara, Odo allemaal "escaped"). Er komt dus geen goud binnen en er is niets te doen. Voor "tussendoor" (T1) moet er in de eerste minuut iets binnenkomen. Eis: in de eerste minuut valt minstens één held en zie je het goud stijgen (balansdoel in `features.md`). Nu vlucht 3 van de 3; doel is ongeveer 1 op 3.
2. **De wrok zie je niet op het scherm, alleen in de tekst.** Kees komt terug en ziet er precies hetzelfde uit. Het beste stuk van het spel moet je zien zonder te lezen: een litteken op het poppetje (pleister, ooglap) en een klein boos teken boven zijn hoofd als hij zijn vijand ziet. (Daan: littekens als losse laag, zoals de hoeden.)
3. **De slijm doet niets zichtbaars.** Gloop staat de hele minuut op dezelfde plek, terwijl helden langs en door hem lopen en toch "Grudge: Gloop" krijgen. Er moet te zien zijn dat Gloop iemand raakt (een hap, de held die terugstuitert), anders snap je de wrok niet.
4. **Tekst wordt afgekapt:** "Grudge: Gloop the Sli". De regel moet passen of korter ("Kees is back. Grudge: Gloop"). Het tekstvak neemt ±30% van de breedte; dat mag kleiner als de regels korter zijn, dan is er meer hol.
5. **Er gebeurt niets bij de schat.** Een held staat bij de stapel en loopt weer weg. Hier zit de grap uit `features.md` (hij probeert de stapel op te tillen, te zwaar, rent weg als Hoard-Toucher). Nu is het een gemiste kans.
6. **Te weinig te zien van het spelen zelf.** Er wordt één keer gegraven (log "gegraven kolom 13"), maar in de GIF zie je geen klik of nieuw stuk gang ontstaan. Laat in de film van een minuut zien: graven, een put zetten, een held die erin valt, goud dat binnenkomt. Dat is ook wat Thijs moet zien.
7. **Het hol vult de breedte niet:** gang tot ±2/3, daarna egale aarde en het tekstvak. Met graven groeit het; voor de film beter een hol dat al wat gegroeid is.

**Oordeel:** goede technische basis, de wrok staat in de log, maar het is nog niet leuk om naar te kijken: er valt niemand, er komt geen goud, en de wrok zie je niet. Punten 1 tot 3 zijn het belangrijkst; zonder die drie kan Thijs het niet zien. Doorgegeven aan Olaf en Bram in hun berichtenbestand.
