# Welkom en Gloop-teken altijd in beeld bij een oude save (Sanne, 28 nov, #406)

Iris #399 (865530f, leuk 7): (1) het welkom "Heroes want your gold. Trap them first!" stond nooit in beeld; (2) "Click Gloop to grow him." ging na 6 s weg als Gloop plat ging en kwam nooit terug.

Oorzaak (1): het welkom stond midden boven het hele venster. Bij een oude save staat het hol rechts (x ±1085 tot 1440 op 1920), dus het plaatje hing boven leeg gras, ver van waar je kijkt.

Wat veranderde (`kern/eerste_minuut.gd`, `kern/kaartje.gd`, `kern/opslag.gd`, `kern/strook.gd`):
- Het welkom staat midden boven het hol zelf (ingang tot schat) en nooit over het bord. Bij een oude save 6 s (was 4): de eerste 1 tot 2 s tekent het venster soms nog niet (Iris' film).
- De Gloop-les telt pas als gehad als de speler één keer het kaartje van Gloop opent (save `gloop_klik`). Tot dan komt de regel terug zodra de ring weer aangaat (na plat), en staat de ring aan zonder klik, dan na 45 s opnieuw (20 s aan). Wie Gloop al kocht, krijgt hem niet. De oude sleutel `gloop_les` telt niet meer: Thijs krijgt hem dus opnieuw.

Bewijs (GEZIEN, Linux Xvfb, Godot 4.3, 1920 x 1080, hoogte 96, oude save: 1059 goud, `uitleg=4`, zonder `uitleg_v`, 519 s weg, 0 SCRIPT ERROR):
- `welkom-0-tot-6s-per-s-1920x96.png` (hele venster) en `welkom-0-tot-6s-hol-2x.png` (alleen het hol, 2x): elke seconde van 0,5 tot 6,5 s. Het welkom staat 0,5 tot 5,5 s boven het hol naast het verslag op het bord; op 6,1 s "Click the dirt to dig." (`welkom-film.log`).
- `gloopteken-komt-terug.log` (200 s, speler volgt de les na 25 s maar klikt nooit op Gloop): Gloop-les aan op 56,1 s, weg 76,1 (tijd), terug 121,2, weg 141,3, terug 186,3. Met een klik (`uitleg_klik=3`): kaartje open op 15,2 s, "gloop gehad", daarna nooit meer.
- Toetsen: alle 11 bestanden 0 FOUT, 4 nieuwe in `toets_systemen.gd` (terugkomen na rust, nooit na klik, niet zonder ring of tijdens de les, welkom 6 s bij oude save).
