# Aanloop naar de val en eerste klap (Olaf, 25 nov 2026, issue #25)

Op de keuring van Iris (build 46cdec1, lopen 7): twee helden draalden 20 s bij de val en de eerste klap kwam pas op 37 s.

**Wat er veranderde (voor de speler):**
- Een held die een val of Gloop nadert, kijkt binnen 64 spelpixels niet meer rond, en rent de laatste 24 spelpixels (zelfde loopbeelden, 3,5 keer zo snel, hooguit 42 beelden per s: de voeten blijven staan). Hij valt of springt binnen 2 s.
- Een held met een wrok kijkt nooit rond: hij weet waar hij heen wil. Na de val begint hij niet meteen weer stil te staan.
- De eerste held van een vers spel komt na 2 s (was 4) en loopt 2 keer zo snel recht op de eerste val af: eerste klap op 7,2 s (was 16,6 s in dezelfde meting; 37 s in de Windows-film van Iris).
- Het tekstwolkje wordt tijdens de witte flits niet meer een witte vlek (kan 1 van Daan, #53): het "!" komt na de flits.

**Bewijs (GEZIEN, Godot 4.3 Linux, scherm 1024 breed, hoogte 120, vers spel, zaad 2, 20 beelden per s):**
- `eerste-klap-20s-ware-grootte.mp4`: 20 s op ware grootte met geluid; klap op 7,2 s.
- `aanloop-80s-met-geluid.mp4`: 80 s met geluid (plof, munt). Beloningen op 7,2, 25,8 en 64,8 s.
- `aanloop-sprong-strip.png`: Femke loopt naar de put, rent het laatste stuk en springt er met "!" overheen (0,3 s per vakje).
- `eerste-val-flits-strip-2x.png`: eerste val, witte flits zonder wit wolkje, dan "!", ster en +6.
- Toets `systemen/toetsen/toets_aanloop.gd`: 59 helden van alle soorten bij een put; langste tijd van 24 px tot de keuze: gewoon 1,25 s, ridder 1,8, magier 1,8, bard 1,4, dief 0,95. Niemand kijkt rond binnen 64 px, niemand loopt over de put zonder vallen of springen.
- Eerste klap in 3 vaste spellen (zaad 1, 2, 3): 7,2 s alle drie.

Nog open (niet in dit issue): tussen 65 en 135 s komt er in deze meting geen beloning (ritme van helden, punt 1 van Iris).
