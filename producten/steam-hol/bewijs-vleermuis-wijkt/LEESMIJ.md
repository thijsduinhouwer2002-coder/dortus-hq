# Vleermuis wijkt voor de held (Olaf, 25 nov 2026, issue #25, kan 2 van Daan #59)

Daan zag in `bewijs-aanloop/` de eerste held een halve seconde dwars door de vleermuis lopen, zonder reactie.

**Waarom dat gebeurde (GEZIEN in de code en met een logregel):**
- De vleermuis schrok pas als de held 10 spelpixels van zijn midden was, maar hij is 18 breed en de held ±10: ze raakten elkaar al op 14.
- In een kort hol (de eerste minuut: alleen gang tussen ladder en put) was er geen andere hangplek. Dan bleef hij gewoon hangen en liep de held erdoor.
- Zijn vlucht zakte 5 spelpixels de gang in, precies op hoofdhoogte.

**Wat er veranderde (voor de speler):**
- De vleermuis vliegt op als een held op 26 spelpixels komt, en vliegt vlak onder het plafond met een kleine boog (1,5 in plaats van 5).
- Geen andere plek: hij fladdert snel langs de held naar achter hem (boven de schacht), fladdert daar tot de held voorbij is, en vliegt dan terug naar zijn plek.
- Moet hij aan het eind van de gang langs een held, dan doet hij dat 2 keer zo snel (0,6 s).
- Hij landt niet boven een andere held, en een held die hem tijdens zijn rust na het landen bijna raakt (15 px) jaagt hem ook op.

**Bewijs (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie`, 20 beelden per s, hoogte 120, vers spel, zaad 2):**
- `vleermuis-wijkt-20s-ware-grootte.mp4`: 20 s ware grootte met geluid, uitsnede van het hol. Rond 5 s vliegt de vleermuis weg voor Lotte, fladdert bij de ladder en hangt na de klap weer op zijn plek.
- `wijkt-uit-strip-2x.png`: 4,5 tot 9,3 s, 0,3 s per vakje, 2x.
- Toets `systemen/toetsen/toets_vleermuis.gd`: een held op 5,6, 7,5 en 15 spelpx/s loopt beide kanten op onder alle vleermuizen door: 0 beelden raak bij hangen of wegvliegen; snel langs de held aan het eind van de gang samen 0,24 tot 0,36 s. Kort hol zoals de eerste minuut: 0 beelden raak, hij fladdert achter de held en hangt daarna weer op zijn plek. Met de oude waarde (10) faalt de toets (24 tot 34 beelden raak).

**Eerlijk:** een held die net de ladder afkomt terwijl de vleermuis boven de schacht fladdert, kan hem nog kort kruisen. Dat zag ik niet in de 80 s van zaad 2.
