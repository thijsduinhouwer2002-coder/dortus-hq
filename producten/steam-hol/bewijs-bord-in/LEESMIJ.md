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

## Muis weg glijdt, en de naad loopt nooit door de tekst (Sanne 27 nov ±13:15, Daan #261 kan-punt 1)
**Wat de speler ziet:**
- Muis van het ingeklapte bord af: het bord springt niet meer in één beeld naar één rij, maar glijdt in 0,35 s terug, net als na een regel. Met de muis erop blijft het bord vol (`bord_doel`, setter op `hover` in `kern/tekst.gd`).
- Tijdens het in- en uitklappen werd het hout van het bord samengeperst, waardoor de donkere naad tussen twee planken dwars door het goud en het doel schoof (gezien in een film van 20 beelden per s, ±0,15 s lang). Nu wordt het hout van boven afgesneden in plaats van samengeperst (`bron_midden`): de naad schuift mee met de tekst en blijft eronder.
- Gevolg ingeklapt: de naad staat nu als een lijn onder goud en doel (was weggeperst). Zie `naad-60s-voor-en-na-2x.png`; keurder beslist of dat mag.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb):**
- `muis-weg-glijdt-2x.png`: alleen het bord (640 x 120, losse proef), ingeklapt, muis erop (vol, drie regels), dan muis weg na +0,04 tot +0,41 s: open 0,90, 0,74, 0,59, 0,44, 0,29, 0,00; de naad blijft in elk beeld onder de tekst.
- `naad-60s-voor-en-na-2x.png` en `na-muis-60s-ware-grootte.png`: echt spel, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`, 5 beelden per s, op 60,0 s, b519038 tegen nu (zelfde stand van het spel).
- Toetsen 11 x 0 FOUT op Linux (3 nieuwe in `toets_systemen.gd`: muis houdt het bord vol, muis weg glijdt, hout afgesneden).
