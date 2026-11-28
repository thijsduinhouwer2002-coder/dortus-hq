# Palet zacht: gemeten en niet standaard (#333, Olaf 28 nov)

Keuze Sanne in #333 (28 nov ±04:00): grond `zacht`, figuren B van Mila. Dit is het deel voor de grond.

**Uitkomst:** `zacht` stond kort standaard (commit 702d264) maar staat weer op `vol`. Binnen één run gemeten (`wissel=palet` zet de laag om de 20 s aan en uit, `wissel=nep` is de placebo; 200 px, 1920 x 1080, Linux software-tekenen, 6 min elk, zaad 5) kost de laag **±30 procent CPU**: palet buurparen +41,0 procent (fout ±10,6), placebo +11,3 (±4,5), dus ±30 (GEZIEN, ruwe meting `platformen/steam/data/cpu-duur/palet/`, script `cpu_stenen.py`, `ALLES=1`). De Windows-run 46107305080 gaf los 200 zacht 3,65 tegen 200 vol 2,86 CPU-s per 10 s (+28 procent, GEZIEN, losse runs). Dat is boven de poort van 20 procent in `platformen/steam/balans.md`, en de blinde test zag geen verschil tussen vol en zacht. Op een pc met grafische kaart kost zo'n laag waarschijnlijk veel minder (GOK), maar onze poort meet zo.

Daan #339 punt (1): de laag hangt nu met ankers over het hele venster (`set_anchors_and_offsets_preset(FULL_RECT)`), dus hij groeit mee als het venster na de start nog van maat verandert. Een andere hoogte kiezen herlaadt de scène al, dus daar ging het niet mis; nu kan het ook niet meer bij een late venstermaat.

Daan #344 K2: 1 px meer lucht tussen het muntje en het getal op de knop (`kern/tekst_kaart.gd`). Op 120 raakte de munt de 4 van 40.

Beelden (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=200 vers=1 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 zaad=11`, beeld op 75 s):
- `vol-boven-zacht-onder-200-links-1x.png` en `...-rechts-1x.png`: boven `palet=vol`, onder de nieuwe standaard. De laag dekt de volle breedte en hoogte.
- `kaartje-120-munt-lucht-2x.png`: het kaartje op 120 px, munt los van de 40.

Films van 80 s op 96, 120, 200 en 240 px: 0 SCRIPT ERROR, log zegt `HOL palet zacht` (GEZIEN). Toetsen: 11 x 0 FOUT op Linux.

CPU (Daan #339 M2): `steam-hol.yml` meet nu op 120, 200, 240 en 200 met `palet=vol` in dezelfde run; uitslag in `cpu.txt` op de tak schermen. Alleen ter info: losse metingen op een gedeelde runner schommelen (zie `platformen/steam/balans.md`).
