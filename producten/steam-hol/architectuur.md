# Het Hol: architectuur (Olaf, 10 nov 2026)

Godot 4.3, map `godot/`. Eén scène (`main.tscn`) met de strook als wortel.

| Deel | Bestand | Wie | Wat |
|---|---|---|---|
| Strook | `kern/strook.gd` | Olaf | venster boven de taakbalk, hoogte (96, 120, 160), de toestand van het spel, de eerste tien minuten (BEGIN, BEGIN_DEMO; de keuze van de stap staat in `binnenkomst.gd`), `_process` |
| Muisvlak | `kern/muisvlak.gd` | Olaf | welk deel van het venster de muis vangt (hol, gras, bult boven Gloop, paneel bij hover); strook.gd houdt `_muis_vlak`, `muis_vlak_punten` en `gloop_bult` als doorgeefluik |
| Proef | `kern/proef.gd` | Olaf | startargumenten (hoogte, duur, log, demo, film, zaad, fps en alle `*_proef`), en de winkelmomenten `moment=hap/val/munt` met de logregel `HOL moment vast` |
| Ritme | `kern/ritme.gd` | Olaf | wanneer de volgende held komt (ook na het lied van een bard) en het graven in de demo-film |
| Kroniek-wachtrij | `kern/wachtrij.gd` | Olaf | welke regel wanneer in het tekstvak komt (gebeurtenis gaat voor, binnenkom-regel vervalt na 3 s) |
| Beeldtempo | `kern/beeldtempo.gd` | Olaf | 10 beelden per s, 20 tijdens een moment (val, hap, muntjes); `fps=<n>` houdt het vast. Helden lopen in hele pixels op een klok van 0,1 s (`systemen/held.gd` PAS) |
| Binnenkomst | `kern/binnenkomst.gd` | Olaf | een nieuwe held of terugkomer binnen laten: stap van het begin, soort en trek, binnenkomstregel; `naamgenoot_mag` (II of III, één keer per voornaam, hooguit één naamgenoot-regel per 5 min); kiest `naamgenoot_laars` alleen als de ouder in `laars_namen` staat, anders `naamgenoot` |
| Namen | `kern/namen.gd` | Olaf | vrije naam uit 24 namen in families (laagste telling eerst, niet uit de laatste 6 recente namen, na III alles tegelijk wissen), `titel` (Dame voor vrouwennamen), `ouder` (mom of dad voor de naamgenoot), bijnamen, de terugkomer-regel met bijnaam |
| Afloop | `kern/afloop.gd` | Olaf | wat er gebeurt als een held klaar is: vlucht met wrok, of val met goud, munten en hoed op de toren; `terugslag` (de vangst slaat terug op de binnenkomst, `binnen_soort`), `hap_soort` (eigen hapregel per heldensoort, terugkomers en demofilm gewoon `val_bewoner`); zet de volle naam in `s.laars_namen` als de valregel een laars noemt (laarsgrap, Iris 19 nov; niet bewaard bij herstart) |
| Opslag | `kern/opslag.gd` | Olaf | bewaren en laden (`user://hol.json`), voortgang terwijl je weg was (via `systemen/voortgang.gd`) |
| Klap | `kern/klap.gd` | Olaf | het kernmoment van de val (issue 5): witte klap-ster, "+9" in goud uit de aarde, "x3" bij een reeks vangsten op rij; reeksbonus in `afloop.gd` (`reeks_bonus`, vanaf de derde +1, hooguit +4), vlucht zet de reeks op 0; toets `systemen/toetsen/toets_klap.gd` |
| Tekstvak | `kern/tekst.gd` | Olaf | goud, laatste regel, paneel bij hover |
| Regels | `kern/regels.gd` | Olaf | voorraad korte regels per soort (aangevuld uit `systemen/kroniek_regels.gd`), schudzak, max 42 tekens; `vul` vult {naam}, {held}, {oud} en {ouder} (die laatste uit de naam via `namen.gd`) |
| Hol | `hol/hol.gd` | Olaf | raster, graven, put, schat, munten, tekenen |
| Systemen | `systemen/*.gd` | Bram | held, slijm (Gloop), kroniek, upgrades, voortgang; toetsen in `systemen/toetsen/` |
| Kunst | `kunst/` | Daan, Mila | plaatjes |

**Hoe de kern-delen samenhangen:** `wachtrij.gd`, `namen.gd`, `afloop.gd`, `opslag.gd`, `binnenkomst.gd`, `muisvlak.gd`, `proef.gd` en `ritme.gd` hebben alleen statische functies met de strook als eerste argument (`s`). De toestand (kroniek, terugkomers, wachtrij, goud via het hol) blijft in `strook.gd`; die roept ze aan via korte doorgeefluiken met de oude namen (`_toon`, `_held_naam`, `_held_klaar`, `bewaar`, `laad`), zodat de rest niet veranderde.

**Afspraak kern en systemen:** zie `platformen/steam/taken.md` (functies van `hol.gd` die Bram gebruikt).

**Test:** `.github/workflows/steam-hol.yml` (Windows-runner): toetsen van Bram, alle kernscripts laden zonder fout, schermen op 96/120/160, CPU, film van een minuut (`film/film.log` is het bewijs; gelijk log = gelijk gedrag).

## App-balk op Windows (Olaf 25 nov 2026, issue #24)
- `balk/hol_balk.c` wordt `godot/balk/hol-balk.exe` (46 KB, mingw, gebouwd met `-Wl,--no-insert-timestamp`; de workflow `steam-hol-balk.yml` bouwt hem opnieuw uit de bron en vergelijkt). Hij zit in de .pck (`export_presets.cfg`) en `kern/balk.gd` start hem naast de .exe of kopieert hem naar `user://`.
- Het programma houdt met een eigen onzichtbaar venster een strook vrij bij Windows (ABM_NEW, QUERYPOS, SETPOS), zet het spel daarin, haalt de taakbalkknop weg, verstopt het spel bij volledig scherm, en laat de muis door (WS_EX_LAYERED + WS_EX_TRANSPARENT) behalve op het vlak dat `kern/muisvlak.gd` stuurt. Pijp dicht of venster weg: ABM_REMOVE en stoppen, ook na hard afsluiten.
- Zonder het programma (geen Windows, `balk=0`) blijft het oude `window_set_mouse_passthrough`.
- Systeemvak: `kern/systeemvak.gd` (Pause, Sound, Height, Quit). Naamsvermelding: `godot/DERDEN.txt`.
