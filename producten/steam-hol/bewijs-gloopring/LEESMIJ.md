# Gloop laat zelf zien dat hij klaar is (Mila, 25 nov 2026, issue #62)

Iris (keuring 46cdec1): tekst 6, aandacht 6. Thijs wil rustig. Daarom staat "Big Gloop ready: click Gloop" niet meer op het bord: Gloop krijgt een ring van licht om zijn voet zodra je zijn volgende stap kunt kopen.

**Wat de speler ziet:**
- Genoeg goud voor Gloops volgende stap: een ring van licht ligt op de vloer om hem heen, licht mint met een wit hart en vier lichtpareltjes. De achterkant zit achter zijn lijf, de voorkant ervoor, dus hij staat ín de ring.
- De ring komt in 0,6 s zacht op en ademt daarna rustig in 2,8 s (licht 0,62 tot 1, maat 0,97 tot 1,03). Geen knipperen, geen geluid, geen schermschudden.
- Op het bord staat dan geen regel meer (alleen het goud en de kroniek). Het muntje boven Gloop is weg: de ring vervangt het. Het muntje boven een put blijft.
- Ligt Gloop plat, dan wacht de ring tot hij weer staat (plat las de ring als een schoteltje).
- Kleur: mint op de roodbruine aarde is het grootste kleurverschil in het hol; een gouden ring viel weg tegen de schat ernaast.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, scherm 1024 breed, strook 120, `vers=1 zaad=2 uitleg_klik=6`, 20 beelden per s):**
- `gloopring-45s-ware-grootte.mp4`: 155 tot 200 s speeltijd op ware grootte. Op 164,7 s heeft de speler 47 goud (Big Gloop kost 45): ring aan (log: `HOL gloop ring aan na 164.7 s (goud 47)`).
- `gloopring-strip-ware-grootte.png` en `gloopring-strip-2x.png`: 41 goud met "Next: Big Gloop, 4 gold to go" en geen ring; daarna de ring die opkomt, zwak en sterk ademend, bord zonder regel.
- Toetsen 7 x 0 FOUT op Linux (systemen, namen, held, vleermuis, berg_wand, klap, aanloop), met 4 nieuwe toetsen voor de ring.

**Kunst:** `modellen/gloopring.py` (Blender, geen AI, geen gekocht pakket) maakt `godot/kunst/gloopring.png`, 288 x 96 (cel 36 x 12 spelpixels, 8 bladpixels per spelpixel: scherp tot strook 160 zonder opschalen).
Draai: `~/bpyenv/bin/python modellen/gloopring.py godot/kunst/gloopring.png 8 96` (±5 s).

**Code:** `godot/systemen/gloop_ring.gd` (nieuw), `systemen/slijm.gd` (`zet_klaar`, `ring_aan`), `kern/kaartje.gd` (`tik` zet de ring, `doel_regel` geeft leeg als Gloop klaar is). Zuinig: de ring tekent één keer; het ademen is alleen doorzichtigheid en maat, 10 keer per seconde, en alleen als de ring aan is.

## Munt op de ring (Mila, 25 nov ±13:00, na de keuring van Iris op e39939e)
Iris: "je ziet dat Gloop iets bijzonders heeft, niet dat je hem kunt kopen. Half ja." Daarom staat er nu een gouden munt rechtop links vooraan op de ring. In het hol betekent een munt al "dit kun je kopen" (het muntje boven een put); de ring zegt nu hetzelfde, zonder tekst.
- Munt ±10 schermpixels op strook 120, even groot als de muntjes boven de putten (GEZIEN). Naast zijn mond, nooit ervoor; ver van de goudschat rechts zodat hij daar niet in wegvalt. Hij ademt mee met de ring, verder stil.
- Eigen blad `godot/kunst/gloopmunt.png` (64 x 64, 8 bladpixels per spelpixel) uit hetzelfde `modellen/gloopring.py`, zodat hij groter mag zijn dan de onderste helft van de ring en toch helemaal vóór Gloop staat.
- `gloopring-munt-30s-ware-grootte.mp4`: 155 tot 185 s, met geluid. Ring en munt aan op 164,1 s bij 47 goud (log `HOL gloop ring aan na 164.1 s (goud 47)`).
- `gloopring-munt-strip-ware-grootte.png` en `-2x.png`: 41 goud zonder ring, de klap die het goud brengt, ring en munt die opkomen, Gloop die knipoogt in de ring.
- Toetsen 7 x 0 FOUT op Linux, 3 nieuwe voor de munt (staat erin, naast de mond, vooraan op de ring).

## Gloop-les en witter hart vooraan (Mila, 25 nov ±15:05, keuring Daan #68)
Daan: "Juist op het moment dat de speler iets moet doen, verliest hij de enige uitleg. Een ring leest als geselecteerd of sokkel, niet vanzelf als klik mij."
- **Eén keer een les:** de eerste keer dat de ring aangaat staat dezelfde plaat met pijl als in de eerste minuut, met "Click Gloop to grow him." (concept tot Thijs hem schrijft). De pijl wijst van de lucht door de grond op Gloops kruin. Geen gouden vak: de ring is het vak. Weg zodra je op Gloop klikt (het kaartje gaat open), als de ring uitgaat, of na 20 s. Daarna nooit meer, ook niet na een herstart (save `gloop_les`). Niet tijdens de eerste minuut: komt de ring dan al, dan volgt de les als die klaar is.
- **Witter hart vooraan (kan):** een iets dikkere witte boog over de voorste helft van de ring (`modellen/gloopring.py`, `voorboog`), zodat de voorkant niet opgaat in Gloops eigen mint.
- **Bewijs (GEZIEN, Godot 4.3 Linux onder Xvfb, scherm 1024, `--write-movie --fixed-fps 20`, `vers=1 zaad=2 uitleg_klik=6 balk=0`):** op alle drie de hoogtes logt het spel `HOL uitleg gloop aan` op het moment dat de ring aangaat (120 en 96: 137,5 s bij 47 goud; 160: 131,7 s) en `HOL uitleg gloop weg ... na 6,0 s (klik)` als de proefspeler op Gloop klikt.
  - `gloop-les-strip-96-*.png`, `-120-*.png`, `-160-*.png` (ware grootte en 2x): voor de ring, les in beeld, les met ring, na de klik het kaartje met Buy 45 en geen les meer. Op 96 blijft de voorkant van de ring onder zijn voet zichtbaar.
  - `gloop-les-20s-ware-grootte.mp4`: 128 tot 148 s op strook 120.
- Toetsen 7 x 0 FOUT op Linux, 6 nieuwe voor de les (eerste keer ja, tweede keer nooit, niet tijdens de eerste minuut, blijft tot 20 s, weg na klik of ring uit, regel kort).
- Op 160 ligt de plaat 20 s lang over het bordje met de pijl naar de ingang; daarna is het weer vrij.
