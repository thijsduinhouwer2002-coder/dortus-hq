# Figure from rig op de figuren van studio-2 (Pro 1.2.0, Blender 5.3.0), 23 nov 2026, Olaf

Bron: release `studio-2` (run 45197874364, workflow `studio2.yml`), `kandidaten.txt`, `proef-*.log` en de beelden (GEZIEN).
Lokaal nagedaan: alleen de robot (zelfde Pro-commit f8dfbd3, zelfde Blender, zelfde script `proef_figuur.py`).

| Figuur | CI | Lokaal | Overgeslagen in CI | Oordeel |
|---|---|---|---|---|
| Robot (eigen, 220 mm) | 8 | **9** (ook met `-t 4` en `-t 8`) | Left hip "it would be blocked" | **Bug**: zelfde invoer, ander antwoord. Symmetrisch figuur, toch alleen links geweigerd. Rechterheup CI ±27°, lokaal ±30°. Zie onder |
| Stan (Quaternius mech, 240) | 4 | niet gedaan | knieën "too thin for a hinge", schouders "only a tiny ball", nek "too thin" | eerlijk; mech-ledematen zijn dun |
| Mike (mech, 240) | 4 | niet gedaan | linkerelleboog "parts overlap", rechterschouder "too close (37 mm)", heupen | linkerelleboog wel, rechter niet? niet nagekeken |
| George (mech, 240) | 0 | niet gedaan | ellebogen "joined on both sides", knieën overlap/los stuk, rest geen ruimte; figuur is 9 losse stukken | eerlijke weigering, losse stukken in de bron |
| Cyberpunk (240) | 2 | niet gedaan | knieën "Tight: cheek too stiff", schouders, heupen, nek | eerlijk; korte stripverhoudingen |

## De robot: waar het verschil zit (GEZIEN lokaal, CI-meting loopt)
- Zelfde voxel-uitkomst: CI en lokaal 240130 punten na Make watertight (GEZIEN in beide logs).
- Lokaal is de beweegproef van beide heupen ruim: kleine meter overal 30,4°, grote meter 27,8° in één richting
  (linkerheup), geen enkele botsing op 0° en geen punt binnen 0,001 mm van het andere deel (meetregels in de
  proef-zip, `../ci-verschil/diag-beweeg.patch`). Het is dus geen randgeval van de binnen-toets in `beweeg.py`.
- In CI meet de linkerheup op elke kandidaatplek minder dan 1° (`kogel_vast`), dus het verschil ontstaat eerder:
  in de vorm van de delen na de sneden (MANIFOLD). Threads zijn het niet (1, 2, 4, 8 lokaal gelijk). GOK: andere
  processor (lokaal Xeon met AVX-512) geeft net andere afronding in de snede.
- Meting in CI met dezelfde meetregels: tak `claude/olaf-diag-heup`, run 45206324187. De vingerafdruk per deel
  (`DIAGMESH`: aantal punten en som) laat zien bij welk gewricht CI en lokaal uit elkaar gaan. Lokaal:
  neck 130662/26491, schouders 121210/14829 en 111744/14847, heupen 91724/25170 en 71706/25172.
