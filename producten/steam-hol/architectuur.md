# Het Hol: architectuur (Olaf, 10 nov 2026)

Godot 4.3, map `godot/`. Eén scène (`main.tscn`) met de strook als wortel.

| Deel | Bestand | Wie | Wat |
|---|---|---|---|
| Strook | `kern/strook.gd` | Olaf | venster boven de taakbalk, hoogte (96, 120, 160), muis door lucht en gras, helden laten komen, de eerste tien minuten (BEGIN, BEGIN_DEMO), de demo, `_process` |
| Kroniek-wachtrij | `kern/wachtrij.gd` | Olaf | welke regel wanneer in het tekstvak komt (gebeurtenis gaat voor, binnenkom-regel vervalt na 3 s) |
| Namen | `kern/namen.gd` | Olaf | vrije naam (geen twee tegelijk, Kees II), bijnamen, de terugkomer-regel met bijnaam |
| Afloop | `kern/afloop.gd` | Olaf | wat er gebeurt als een held klaar is: vlucht met wrok, of val met goud, munten en hoed op de toren |
| Opslag | `kern/opslag.gd` | Olaf | bewaren en laden (`user://hol.json`), voortgang terwijl je weg was (via `systemen/voortgang.gd`) |
| Tekstvak | `kern/tekst.gd` | Olaf | goud, laatste regel, paneel bij hover |
| Regels | `kern/regels.gd` | Olaf | voorraad korte regels per soort, schudzak, max 42 tekens |
| Hol | `hol/hol.gd` | Olaf | raster, graven, put, schat, munten, tekenen |
| Systemen | `systemen/*.gd` | Bram | held, slijm (Gloop), kroniek, upgrades, voortgang; toetsen in `systemen/toetsen/` |
| Kunst | `kunst/` | Daan, Mila | plaatjes |

**Hoe de kern-delen samenhangen:** `wachtrij.gd`, `namen.gd`, `afloop.gd` en `opslag.gd` hebben alleen statische functies met de strook als eerste argument (`s`). De toestand (kroniek, terugkomers, wachtrij, goud via het hol) blijft in `strook.gd`; die roept ze aan via korte doorgeefluiken met de oude namen (`_toon`, `_held_naam`, `_held_klaar`, `bewaar`, `laad`), zodat de rest niet veranderde.

**Afspraak kern en systemen:** zie `platformen/steam/taken.md` (functies van `hol.gd` die Bram gebruikt).

**Test:** `.github/workflows/steam-hol.yml` (Windows-runner): toetsen van Bram, alle kernscripts laden zonder fout, schermen op 96/120/160, CPU, film van een minuut (`film/film.log` is het bewijs; gelijk log = gelijk gedrag).
