# Het hol vol (Olaf, 16 nov 2026, vraag Mila 09:00 punt 1, 2 en 3)

Lokaal gemaakt: Godot 4.3 linux onder xvfb, scherm 1920 x 1080, strook 160, de week-save van `steam-hol-winkel.yml`
(29 gangtegels, kamers op 4-5, 9-10, 15-16, 21-22, vier putten), `zaad=2`, beeld 50 op 5 fps (10 s).

- `main-boven-vol-onder-lokaal-160.png`: boven main, onder de tak `claude/steam-hol-vol`. Strook in twee helften onder elkaar.
- `vol-kamers-gang-2x.png`: uitsnede van de tak, 2 keer vergroot.
- `drukte-20s-lokaal-160.png`: met `drukte=1`, beeld 100 (20 s); de log zegt `helden=3` in die 10 s.

Wat het spel nu doet (alleen op de 3D-gang en vanaf 20 gangtegels, `hol/hol_vast.gd` `is_vol`):
1. Elke vrije gangtegel een vloerding (paddenstoel, lichtzwam, ton, krat, schedel, kristal), nooit twee dezelfde naast elkaar.
   Niet op de eerste tegel na de schacht, niet op of naast een val, niet bij de hoeden en Gloop (`schat_kol - 4` en verder).
2. Plafond los daarvan: stut, spinrag of vaandel op ±58% van de tegels, nooit twee naast elkaar, niet onder een kamer,
   niet bij de ingangsfakkel, boven een val geen stut.
3. In elke kamer van twee of meer kolommen twee dingen: rechts van de fakkel en links van het kistje, op 0,8 van de maat
   (kamers liggen achter de gang). Een losse kamer heeft zijn eigen paddenstoelen en krijgt niets.
4. Kleiner hol (onder 20 gangtegels) en de pixelgang: de uitdunning van 14 nov blijft precies zoals hij was.

## Hoedenwand (punt 4, zelfde tak, 16 nov ±09:50 UTC)
- `hoedenwand-lokaal-160.png` en `hoedenwand-2x.png`: zelfde save en beeld, nu met de hoeden in de wand.
- Blad van Bram (`ontwerp/steam/hoedenwand/blad/`) staat nu als `kunst/3d/hoedenwand.png`, stukken onder `hoedenwand` in `kunst/3d/sprites.json`.
- `hol/hol_vast.gd` `wand_plekken()`: dichte cellen in de bovenste rij boven gegraven gang, niet bij de schacht, niet bij
  de stapel en de schatkamer (`schat_kol - 4`), niet voorbij `max_kol`, vaste volgorde (hash), nooit twee naast elkaar.
  De oudste hoed van Gloop (`slijm.hoeden`) krijgt de eerste plek. Het vaste beeld tekent opnieuw als er een hoed bij komt.
- Alleen in 3D en alleen als het blad er is; zonder blad niets (er is geen pixelvorm).

## Daans regels voor een vol hol (16 nov ±10:30 UTC, `ontwerp/steam` stijlregels "Een vol hol")
- `regels-daan-voor-boven-na-onder-2x.png`: zelfde week-save, beeld 50; boven vóór, onder ná, linker 1100 schermpixels, 2x.
- (a) Spinrag en vaandel hangen hooguit 6 spelpixels onder het plafond (±een derde van de gang): spinrag op 0,75 en
  de onderkant eraf (daarmee valt ook de paarse spin weg, die leek op de vleermuis), vaandel kleiner tot het past.
  De stut blijft heel: hij staat op de vloer en is open in het midden, de held loopt erdoor (vraag aan Daan).
- (b) Nooit twee grote dingen (ton, krat, stut) naast elkaar of op dezelfde tegel: een stut wordt dan spinrag,
  een ton of krat een klein ding. Elke vrije tegel houdt een vloerding.
- (c) Eén tegel vrij voor de troon en de hoedenhoop (`schat_kol - 5`), geen stut op of naast een val.
- Hoedenwand zonder vast ritme: ±1 op 4 plekken leeg, soms een paar naast elkaar (op 3 of meer pixels andere hoogte),
  hoogte 14 tot 19, nooit drie op een rij.
