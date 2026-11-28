# Grond zacht en stappen op het kaartje (#333, Olaf 28 nov)

**Grond zacht (keuze Sanne in #333: "grond zacht").** De laag over het hele venster kostte ±30 procent CPU (`bewijs-palet-zacht/`). Nu zit dezelfde demping (verzadiging 0,78, schaduwen iets op, hoge lichten iets terug, vleug warm) alleen in het vaste beeld van het hol: gras, aarde, gangwand, kamers en de lichtkaart (`kern/palet.gd` `zet_grond`, als laatste vlak in de viewport van `hol/hol_vast.gd`). Dat beeld tekent alleen opnieuw als het hol verandert (graven, put, ingang), dus de demping kost per beeld niets. Helden, Gloop, goud, fakkel en het bord tekenen er los overheen en blijven vol. Het vaste beeld is doorzichtig met premultiplied kleur: het oplichten gaat maal de dekking, anders kleurt de lucht mee. `grond=vol` zet het uit.

CPU binnen één run (`wissel=grond` zet de demping om de 20 s aan en uit en tekent het vaste beeld opnieuw, `wissel=grondnep` doet hetzelfde maar laat hem aan; 200 px, 1920 x 1080, Linux software-tekenen, 6 min, zaad 5, de twee tegelijk gedraaid): wissel buurparen +2,2 procent (fout ±5,2), placebo +12,4 (±2,9), alle seconden. Dus niet meetbaar, ver onder de poort van 20 procent (GEZIEN, `platformen/steam/data/cpu-duur/grond/`, `ALLES=1 python3 cpu_stenen.py grond/wissel grond/nep`). Eerlijk: twee runs tegelijk geven veel ruis.

**Stappen op het kaartje (Daan #344 K1: lege plank rechts van de knop).** Rechts op de knoppenrij staan 9 ronde steentjes: gekocht in goud (stap 1 tot 6) of robijn (stap 7 tot 9, zoals op troon en luik), nog te kopen als uitgesneden gaatje in het hout. Zo zie je in één blik hoe ver je bent en dat er nog 8 komen. Past het niet naast de knoppen, dan staat het er niet (`kern/tekst_kaart.gd` `stappen`). De robijnkleur heb ik niet in een film gezien (in 80 s koop je stap 1), alleen in de code (GOK dat hij goed leest).

Beelden (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `vers=1 uitleg_klik=6 koper=1 koper_wacht=8 balk=0`):
- `grond-vol-boven-zacht-onder-200-links-1x.png` en `...-rechts-1x.png`: zaad 11 op 75 s, boven `grond=vol`, onder de nieuwe standaard.
- `kaartje-stappen-240-200-160-120-96-1x.png`: zaad 12, links 73,4 s (voor Buy, alles leeg), rechts 76 s (na Buy, 1 goud), op 240, 200, 160, 120 en 96 px (Daan #344 K3: 96 erbij).
- `kaartje-stappen-200-2x.png`: hetzelfde op 200, 2 keer vergroot.
- `minuut1-200-plaat-ware-maat.png` (75 s) en `minuut1-200-kaartje-ware-maat.png` (78 s): zaad 11 op het bureaublad van `ontwerp/steam/mila/speelscherm/maak_speelscherm.py`, voor de blinde test `hats-speelscherm-grond-zacht`.

Films op 96, 120, 160, 200 en 240 px: 0 SCRIPT ERROR, log zegt `HOL grond zacht`. Toetsen: 11 x 0 FOUT op Linux.
