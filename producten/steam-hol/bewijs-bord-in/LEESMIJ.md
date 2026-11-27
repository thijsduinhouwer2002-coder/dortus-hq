# Bord klapt in als de regel weg is (Sanne, 27 nov 2026, issue #19, Iris 1b0e933 punt 1 voor mooi 9)

Iris 27 nov (build 1b0e933, #255): "nadat de regel na 6 s weggaat, is de onderste helft van het bord een lege plank. Het bord is daarmee het grootste lege vlak in beeld." Haar voorstel: kleiner bord als er geen regel is.

**Wat de speler ziet (dicht bord, strook 120):**
- Staat er een regel op het bord, dan is het bord zoals het was: goud en doel boven, de regel eronder.
- Is de regel weg (na 6 s), dan zakt het bord in 0,35 s zacht naar één rij: alleen goud en doel. Het bord is dan 48 in plaats van 70 px hoog (berekend uit de maten in de code), en erboven zie je weer hol: aarde, wortels, de helm van een held.
- Komt er een nieuwe regel, dan rijst het bord in 0,25 s weer op. Dat opkomen zegt: er is nieuws.
- Niet veranderd: muis op het bord (drie regels), het kaartje van een upgrade, de telling na terugkomst; die tonen altijd het volle bord.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`, 5 beelden per s, zelfde zaad als Iris):**
- `voor-en-na-60s-2x.png`: main 06fad37 tegen nu op 60,0 s, rechterhelft op 2x. Voor: lege plank onder "38  Next: Big Gloop, 2 gold to go". Na: één rij, en de helm van de held boven het bord is weer te zien.
- `voor-60s-ware-grootte.png` en `na-60s-ware-grootte.png`: de hele strook op ware grootte.
- `reeks-in-en-op-2x.png`: 44,0 s regel "First hero got away.", 49,6 s en 50,2 s ingeklapt, 60,0 s nog steeds rustig, 65,6 s nieuwe regel "Siem limps back to the Spike Pit." en het bord staat weer vol, 66,2 s idem.
- Toetsen 11 x 0 FOUT op Linux (3 nieuwe toetsen "bord in" in `toets_systemen.gd`).

**Code:** `godot/kern/tekst.gd` (`open`, `open_doel`, `open_stap`, `open_glad`, in `_process` en `_draw`).
