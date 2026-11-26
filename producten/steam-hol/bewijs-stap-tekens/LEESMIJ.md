# Stap 4 tot 6 zie je aan gouden stenen (#162, Olaf 26 nov 2026)

Gat (Iris, keuring 499fd9f punt 1): een koop op stap 4 tot 6 veranderde niets aan Gloop of de put; Royal Gloop en bijna Gloop Prime waren niet uit elkaar te houden.

**Wat er nu is:** per gekochte stap boven 3 één gouden steen op de vloer, voor Gloop en op het luik van elke put. Stap 4 één steen, stap 5 twee, stap 6 drie. Tellen kan iedereen, dus de volgorde lees je zonder uitleg. De stenen blijven staan (ook na herstart en Undo haalt er één weg).

- Vorm en kleur: ruit van 4 bij 4 spelpixels (12 x 12 schermpixels op 120), dezelfde goudkleuren als het muntje met een donkere rand en een glimvlak. Een ruit, geen rondje: een rond muntje boven Gloop of de put betekent "dit kun je kopen".
- Geen nieuw getekend werk en geen AI: alleen vormen in code, in de kleuren die er al zijn. Getallen en tempo van #145 blijven gelijk.
- Code: `godot/systemen/stap_teken.gd` (vorm, aantal per stap), `godot/systemen/stap_stenen.gd` (eigen laag die alleen tekent als het aantal of de plek verandert), een paar regels in `hol/hol.gd` en `systemen/slijm.gd`. Toets in `toets_systemen.gd` (3 nieuwe regels).

## Beelden (GEZIEN, Godot 4.3 Linux onder xvfb, 1920 x 120, 1x)

Uit een echte koper-run van 1000 s (zaad 3, hol met gang en twee putten), daarna dezelfde save met `slijm_proef=<n> put_proef=<n>` (nu tot 6).

- `stap3-tot-6-1x.png`: vier volle stroken onder elkaar, stap 3, 4, 5, 6.
- `stap3-tot-6-uitsnede-1x.png`: hetzelfde, alleen de twee putten en Gloop.
- `blind-volgorde-abcd.png`: de vier stroken door elkaar (A = 5, B = 3, C = 6, D = 4). Een aparte agent die niets van dit werk wist, kreeg alleen dit beeld en de vraag "zet van minst naar meest verbeterd": hij gaf **B, D, A, C, goed**, en zei dat hij het aan de ruitjes onder de vallen en de troon zag (0, 1, 2, 3); hij las ook de regel op het bord. Eén blinde lezer, dus GEZIEN maar klein.

## CPU (GEZIEN, `meet.sh` naar `platformen/steam/data/cpu-duur/meet_linux.sh`: 1920 x 1080, zaad 4242, `slijm_proef=6 put_proef=6`, 130 s gemeten na 12 s, CPU-s per 10 s)

- Tegen main (oud = main, daar knipt de proef af op stap 3, dus zonder stenen en zonder de extra muntjes van stap 4 tot 6): oud 1,371 / 1,439 / 1,688 / 1,493 / 1,532, nieuw 1,661 / 1,611 / 1,697 / 1,605 / 1,638; +9 procent. Niet eerlijk: stap 6 geeft per vangst 3 muntjes meer in de lucht (#154), dat zit er ook in.
- Eerlijk, zelfde code, stenen aan of uit (eerste versie, stenen in het beeld van Gloop en het hol): uit 1,558 / 1,604 / 1,425 / 1,412, aan 1,573 / 1,609 / 1,559 / 1,510; +4,2 procent (per paar +1,0, +0,3, +9,4, +7,0).
- Tweede versie, stenen in een eigen laag die alleen tekent als er iets verandert (volgorde uit, aan, aan, uit): uit 1,395 / 1,381, aan 1,455 / 1,485; +5,9 procent.
- **Dus niet binnen de +1 procent van #162.** Wel binnen de CPU-poort van `platformen/steam/balans.md` (hooguit 20 procent per beeld tegen main). Let op: deze machine tekent in software (geen grafische kaart), dus ook het tekenen op het scherm telt hier als CPU; de spreiding tussen runs (1,38 tot 1,70) is groter dan het verschil. Volgende stap: de Windows-duurtest, en de stenen één keer naar een klein plaatje tekenen in plaats van ruiten met gladde randen.
