# Het Hol: architectuur (Olaf, 10 nov 2026)

Godot 4.3, map `godot/`. Eén scène (`main.tscn`) met de strook als wortel.

| Deel | Bestand | Wie | Wat |
|---|---|---|---|
| Strook | `kern/strook.gd` | Olaf | venster boven de taakbalk, hoogte (96, 120, 160), de toestand van het spel, de eerste tien minuten (BEGIN, BEGIN_DEMO; de keuze van de stap staat in `binnenkomst.gd`), `_process` |
| Muisvlak | `kern/muisvlak.gd` | Olaf | welk deel van het venster de muis vangt (hol, gras, bult boven Gloop, paneel bij hover); strook.gd houdt `_muis_vlak`, `muis_vlak_punten` en `gloop_bult` als doorgeefluik |
| Proef | `kern/proef.gd` | Olaf | startargumenten (hoogte, duur, log, demo, film, zaad, fps en alle `*_proef`), en de winkelmomenten `moment=hap/val/munt` met de logregel `HOL moment vast` |
| Hol-lagen | `kern/hol_lagen.gd` | Olaf | maakt de lagen in het hol in tekenvolgorde: klein leven, licht, vleermuis, bordje, Wezens (helden en Gloop bovenop) |
| Licht | `systemen/licht.gd`, `systemen/licht_gloed.gd` | Olaf | lichtkaart (vermenigvuldigen, halve spelpixels, alleen opnieuw als het hol verandert) en warme gloed (optellen, flakkert 90 tot 100%) om fakkel, schatkamer en schacht; `uit3d=licht` zet licht en leven uit (#97) |
| Gangwand | `hol/achterwand.gd`, `hol/metsel.gd` | Olaf | achterwand van gegraven cellen (uit `hol_vast.gd`) en scherp metselwerk op de gangwand: voeg 1 spelpx, drie soorten steen in tint, vóór het decor, in het vaste beeld (#210) |
| Leven | `systemen/leven.gd`, `systemen/leven_beest.gd` | Olaf | om de 5 tot 15 s één klein ding: stofje, goudstof, vleermuis wiegt, worm, mot (bladen Mila, #190); één tegelijk per hol; logregel `HOL leven`; `leven_proef=worm|mot` om te filmen, `wissel=leven|nep` om de CPU binnen één run te meten; toets `toets_licht.gd` (#97) |
| Ritme | `kern/ritme.gd` | Olaf | wanneer de volgende held komt (ook na het lied van een bard) en het graven in de demo-film |
| Kroniek-wachtrij | `kern/wachtrij.gd` | Olaf | welke regel wanneer in het tekstvak komt (gebeurtenis gaat voor, binnenkom-regel vervalt na 3 s) |
| Beeldtempo | `kern/beeldtempo.gd` | Olaf | 10 beelden per s, 20 tijdens een moment (val, hap, muntjes); `fps=<n>` houdt het vast. Helden lopen in hele pixels op een klok van 0,1 s (`systemen/held.gd` PAS) |
| Binnenkomst | `kern/binnenkomst.gd` | Olaf | een nieuwe held of terugkomer binnen laten: stap van het begin, soort en trek, binnenkomstregel; `naamgenoot_mag` (II of III, één keer per voornaam, hooguit één naamgenoot-regel per 5 min); kiest `naamgenoot_laars` alleen als de ouder in `laars_namen` staat, anders `naamgenoot` |
| Namen | `kern/namen.gd` | Olaf | vrije naam uit 24 namen in families (laagste telling eerst, niet uit de laatste 6 recente namen, na III alles tegelijk wissen), `titel` (Dame voor vrouwennamen), `ouder` (mom of dad voor de naamgenoot), bijnamen, de terugkomer-regel met bijnaam |
| Afloop | `kern/afloop.gd` | Olaf | wat er gebeurt als een held klaar is: vlucht met wrok, of val met goud, munten en hoed op de toren; `terugslag` (de vangst slaat terug op de binnenkomst, `binnen_soort`), `hap_soort` (eigen hapregel per heldensoort, terugkomers en demofilm gewoon `val_bewoner`); zet de volle naam in `s.laars_namen` als de valregel een laars noemt (laarsgrap, Iris 19 nov; niet bewaard bij herstart) |
| Opslag | `kern/opslag.gd` | Olaf | bewaren en laden (`user://hol.json`), voortgang terwijl je weg was (via `systemen/voortgang.gd`) |
| Veilig bestand | `kern/veilig_bestand.gd` | Olaf | save nooit stilletjes weg: schrijven via `.tmp`, vorige goede als `hol.vorige.json`, kapotte als `hol.kapot.json`, oude versie als `hol.v<n>.json` (#194, toets `toets_opslag.gd`) |
| Klap | `kern/klap.gd` | Olaf | het kernmoment van de val (issue 5): witte klap-ster, "+9" in goud uit de aarde, "x3" bij een reeks vangsten op rij; reeksbonus in `afloop.gd` (`reeks_bonus`, vanaf de derde +1, hooguit +4), vlucht zet de reeks op 0; toets `systemen/toetsen/toets_klap.gd` |
| Geluid | `kern/geluid.gd` | Sanne | speelt Mila's wav's af: plof of hap bij een vangst en 0,18 s later de munt, koop, lied; -6 dB, hooguit één munt per 0,12 s; Sound in het systeemvak dempt bus 0; toets in `toets_klap.gd` |
| Tekstvak | `kern/tekst.gd` | Olaf | goud, laatste regel, paneel bij hover |
| Regels | `kern/regels.gd` | Olaf | voorraad korte regels per soort (aangevuld uit `systemen/kroniek_regels.gd`), schudzak, max 42 tekens; `vul` vult {naam}, {held}, {oud} en {ouder} (die laatste uit de naam via `namen.gd`) |
| Hol | `hol/hol.gd` | Olaf | raster, graven, put, schat, munten, tekenen |
| Stap-tekens | `systemen/stap_teken.gd` | Olaf | stap 4 tot 6 zichtbaar (#162): per stap boven 3 één gouden steen, voor Gloop (`slijm.gd`) en op elke put (`hol.gd`); stilstaand, één keer per aantal en schaal gebakken tot een klein plaatje, eigen laag `systemen/stap_stenen.gd` (meten: `wissel=stenen`, `wissel=nep`, `stenen_keer=<n>`); toets in `toets_systemen.gd` |
| Systemen | `systemen/*.gd` | Bram | held, slijm (Gloop), kroniek, upgrades, voortgang; toetsen in `systemen/toetsen/` |
| Kunst | `kunst/` | Daan, Mila | plaatjes |

**Hoe de kern-delen samenhangen:** `wachtrij.gd`, `namen.gd`, `afloop.gd`, `opslag.gd`, `binnenkomst.gd`, `muisvlak.gd`, `proef.gd` en `ritme.gd` hebben alleen statische functies met de strook als eerste argument (`s`). De toestand (kroniek, terugkomers, wachtrij, goud via het hol) blijft in `strook.gd`; die roept ze aan via korte doorgeefluiken met de oude namen (`_toon`, `_held_naam`, `_held_klaar`, `bewaar`, `laad`), zodat de rest niet veranderde.

**Afspraak kern en systemen:** zie `platformen/steam/taken.md` (functies van `hol.gd` die Bram gebruikt).

**Test:** `.github/workflows/steam-hol.yml` (Windows-runner): toetsen van Bram, alle kernscripts laden zonder fout, schermen op 96/120/160, CPU, film van een minuut (`film/film.log` is het bewijs; gelijk log = gelijk gedrag).

## App-balk op Windows (Olaf 25 nov 2026, issue #24)
- `balk/hol_balk.c` wordt `godot/balk/hol-balk.exe` (46 KB, mingw, gebouwd met `-Wl,--no-insert-timestamp`; de workflow `steam-hol-balk.yml` bouwt hem opnieuw op ubuntu-24.04 met vaste mingw-pakketten en is rood als de sha256 anders is; opnieuw bouwen: `x86_64-w64-mingw32-gcc-win32 -O2 -s -Wall -mwindows -Wl,--no-insert-timestamp balk/hol_balk.c -o godot/balk/hol-balk.exe -lshell32 -luser32` op Ubuntu 24.04 met die pakketten). Hij meldt de app-balk opnieuw aan na een herstart van verkenner, draait maar één keer tegelijk, en het spel start hem opnieuw als hij crasht (`balk.gd` bewaak, hooguit 5 keer). Rechtsklik op het hol opent hetzelfde menu als het systeemvak (Windows-menu via NativeMenu, `kern/systeemvak.gd`). Hij zit in de .pck (`export_presets.cfg`) en `kern/balk.gd` start hem naast de .exe of kopieert hem naar `user://`.
- Het programma houdt met een eigen onzichtbaar venster een strook vrij bij Windows (ABM_NEW, QUERYPOS, SETPOS), zet het spel daarin, haalt de taakbalkknop weg, verstopt het spel bij volledig scherm, en laat de muis door (WS_EX_LAYERED + WS_EX_TRANSPARENT) behalve op het vlak dat `kern/muisvlak.gd` stuurt. Pijp dicht of venster weg: ABM_REMOVE en stoppen, ook na hard afsluiten.
- Zonder het programma (geen Windows, `balk=0`) blijft het oude `window_set_mouse_passthrough`.
- Systeemvak: `kern/systeemvak.gd` (Pause, Sound, Height, Quit). Naamsvermelding: `godot/DERDEN.txt`.
