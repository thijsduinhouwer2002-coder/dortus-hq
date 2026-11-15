# Munt met gladde rand (wens Mila 14 nov 23:50)

Olaf, 15 nov 2026, tak `claude/steam-hol-heldbeeld`.

- `proef-vier-manieren-4x.png`: losse proef in Godot 4.3 (Xvfb, opengl3), schaal 4, van links naar rechts:
  1. zoals main: `draw_circle`, trappetjes;
  2. voorstel Mila: `draw_arc(.., 0.3, true)` in spelpixels: glad maar 4 px wazig, want Godot rekent de zachte rand in plaatselijke eenheden en het hol staat op schaal 4;
  3. `draw_arc` met breedte -1: in 4.3 geen antialiasing voor dunne lijnen (waarschuwing in de log);
  4. gekozen: tekenen in schermpixels (transform gedeeld door de schaal) en om elke cirkel een antialiased boog van 1 schermpixel, een halve pixel naar binnen. Glad, scherp en even groot.
- `main-boven-tak-onder-6x-lokaal-160.png`: het echte spel op 160 px, zelfde save, koopmunt boven een put en paneelmunt, 6x vergroot. Boven main, onder de tak.
- `tak-strook-160-lokaal.png`: de hele strook van de tak op ware grootte.

Lokaal gemaakt op Linux, niet op de Windows-runner; de echte keuring is op de weekopname.
