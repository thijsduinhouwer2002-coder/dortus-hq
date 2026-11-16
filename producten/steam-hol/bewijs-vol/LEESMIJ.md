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
