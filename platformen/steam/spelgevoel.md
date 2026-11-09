# Het Hol: spelgevoel en toetsen van het prototype (Sanne)

Hier toets ik elke GIF en elke schermafbeelding van het prototype: is het leuk, is het duidelijk, is het grappig. Nieuwste bovenaan. Wat er in het spel hoort staat in `features.md`.

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
