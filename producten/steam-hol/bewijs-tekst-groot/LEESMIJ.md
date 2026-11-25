# Bord: één regel, groot, en weg na 6 s (Sanne, 25 nov 2026, issue #19, bouwblad D)

Thijs 24 nov: "de tekst is heel klein en te veel". Iris 25 nov (build e39939e): tekst 6, "bord naar 12 px".

**Wat de speler ziet (dicht bord, strook 120):**
- Goud, doel en de laatste regel in letters 18 (was 13); het doel 17 (was 12). Hoofdletter F van "First" is nu 13 px hoog op ware grootte, was 9 px (GEZIEN, gemeten in beeld 300 van beide films).
- De regel staat 5,4 s vol in beeld en gaat in 0,6 s zacht weg. Daarna staan alleen het goud en het doel op het bord. Het bord blijft even hoog, zodat het niet verspringt.
- Muntje mee groter naast het getal.
- Op 96: letters 15 (hoofdletter 10,5 px), op 160: 24 (16,8 px).
- Niet veranderd: met de muis op het bord de laatste drie regels in de oude maten (Daan ronde 3), het kaartje van een upgrade, de telling na terugkomst (blijft staan tot de eerste nieuwe held). Een regel die niet past wordt hooguit 3 px kleiner en anders op een woordgrens afgekort met "...".

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, scherm 1920 breed, `hoogte=120 vers=1 zaad=2 uitleg_klik=6 balk=0`, 10 beelden per s, zonder geluid):**
- `bord-voor-en-na-2x.png`: main 1a344e5 tegen nu op 29,9 s, de regel die wegzakt op 34,2 s, en het bord met alleen goud en doel op 38 s.
- `bord-96-2x.png`: hetzelfde op 96.
- `bord-160-2x.png`: hetzelfde op 160 (25 nov ±18:50, Daan #88): 29,9 s, 34,2 s en 38,0 s, uitsnede rechts 720 x 160 op 2x. "Next: Big Gloop, 13 gold to go" past naast het goud binnen de houten lijst, de regel ook. Log: "First hero for Gloop!" op 28,5 s, net als op 120.
- `bord-groot-60s-ware-grootte.mp4`: 60 s, de hele strook op ware grootte (1920 x 120). In de log: "First hero in the pit!" 10,0 s, "First hero for Gloop!" 28,5 s, "First hero got away." 43,7 s.
- Toetsen 7 x 0 FOUT op Linux (systemen met 7 nieuwe toetsen "bord D", namen, held, vleermuis, berg_wand, klap, aanloop).

**Code:** `godot/kern/tekst.gd` (`bord_maten`, `regel_zicht`, klok per regel in `zet` en `_process`), toetsen in `systemen/toetsen/toets_systemen.gd`.
