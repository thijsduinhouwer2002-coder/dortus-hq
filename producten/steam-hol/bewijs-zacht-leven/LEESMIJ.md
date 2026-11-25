# Zacht leven: de fakkel flakkert ook in een leeg hol (Olaf, 25 nov 2026, issue #79)

Iris (#7) vroeg een film van 10 min van het echte spel, zonder demo. Tempo-regel 1 (`organisatie/lat/hats-tempo.md`): in 10 min geen stuk van meer dan 15 s waarin niets beweegt; rust mag, maar zichtbaar levend. Thijs 25 nov: rustig, zacht leven.

**Wat ik mat vóór de wijziging (GEZIEN, film van main e39939e, 605 s):**
- Met Gloop erbij: langste stil stuk 3,8 s. Gloop ademt altijd, dus de regel klopte al.
- Maar zonder Gloop stond de rest van het hol (fakkels, gang, schatkamer) in 13 stukken van meer dan 15 s helemaal stil, samen 298 van de 605 s, langste 29,6 s. Reden: de fakkels kregen alleen een nieuw beeldje als er een held liep (CPU-keuze van 13 nov), en de 3D-vlam zelf is een vast plaatje; alleen een zwakke gloed eromheen veranderde (minder dan 12 grijswaarden, op ware grootte niet te zien).

**Wat er veranderde voor de speler:**
- De vlam van de fakkel flakkert nu zelf: een oranje voet en een gele punt die 1 tot 2,5 spelpixels hoog wordt en een derde spelpixel opzij wiegt, op hetzelfde rustige patroon als de gloed (12 standen, buren dicht bij elkaar, geen knipperen).
- In een leeg hol 3 beeldjes per s (één rondje in 4 s), met een held 6 per s zoals voorheen.
- Geen geluid, geen tekst, niets dat aandacht vraagt.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, `--write-movie --fixed-fps 5`, scherm 1024, `hoogte=120 vers=1 zaad=2 uitleg_klik=6 balk=0`; de proefspeler doet alleen wat de les zegt, daarna niets):**
- `echt-spel-10min-zonder-demo.mp4`: 605 s, ware grootte, 5 beelden per s, met geluid (piek -12 dB). Voor Iris: tempo-regel 1 en 5.
- `meting-stil.txt` (script `meet_stil.py`, pixel telt als bewegend bij meer dan 12 grijswaarden verschil, bord rechts niet meegeteld): na de wijziging langste stil stuk 0,2 s, ook zonder Gloop.
- `vlam-voor-8x.png`: de fakkel bij de ingang in een leeg hol op 70 s, 8x, voor issue #79 (vast beeld).
- Toetsen 7 x 0 FOUT op Linux (nieuw in toets_systemen: tongetje minstens 1 spelpixel hoog en laag, hooguit een halve spelpixel per beeld, leeg hol 3 per s).
- CPU, ruwe proef op Linux in software (GOK voor Windows): 150 s echt spel, oud 13,3 CPU-s, nieuw 13,0 CPU-s; beelden zonder held 42 tegen 55 per 10 s. Geen verschil boven de ruis.

**Eerlijk, wat de film ook laat zien (voor Sanne en Iris):** zonder kopen blijft het hol van minuut 3 tot 10 bijna gelijk (alleen goud en de koopmuntjes boven de putten). Tempo-regel 5 hangt dus aan kopen; deze proefspeler koopt niets.

**Code:** `hol/hol_3d.gd` (`teken_vlam`, `vlam_hoogte`), `hol/hol.gd` (`VLAM_TOP`, één regel bij de fakkel), `kern/beeldtempo.gd` (`fakkels`, `fakkel_tempo`), `kern/ritme.gd` (`tel_helden`, uit strook.gd gehaald; strook.gd 424 naar 406 regels). Bekeken voor het flakkeren: onze eigen gloed (Daan juice.md) en Ropuka in de lat (werkt en slaapt zichtbaar, nooit bevroren).

## Nakeuring Daan #80: de vlam uit de render zelf (Olaf, 25 nov ±15:40 NL)

Daan zei nee op beeld: M1 de vlam verloor zijn punt (een oranje blokje lag over de top, een ronde peer), M2 het gele staafje van 1 spelpixel had een harde rand op de zachte 3D-render en sprong aan en uit.

**Wat er veranderde voor de speler:** geen getekende rechthoeken meer. De fakkel wordt nu in twee delen uit hetzelfde 3D-plaatje getekend: de steel gewoon, en de vlam (bovenste 26 bladpixels) rekt vanaf zijn voet 1,0 tot 1,16 keer zijn hoogte en de punt wiegt hooguit 0,35 spelpixel opzij, de voet staat stil. Kleur en zachtheid zijn die van de render, de punt blijft spits, en de vlam krimpt nooit onder zijn eigen maat, dus er springt niets aan en uit. Zelfde rustige patroon (12 standen, buren hooguit 5 procent verschil), leeg hol 3 beeldjes per s, met held 6.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, zelfde instellingen als hierboven):**
- `vlam-staafje-8x.png` (de vorige versie, uit de film van ae91289) en `vlam-uit-render-8x.png` (nu): zelfde fakkel, zelfde 6 beelden vanaf 70 s, 8x.
- `vlam-20-beelden-4x.png`: 20 beelden achter elkaar vanaf 70 s (leeg hol), 4x. `vlam-20-beelden-ware-grootte.png`: dezelfde 20 beelden op ware grootte, stuk hol rond de fakkel.
- `echt-spel-10min-zonder-demo.mp4` opnieuw gemaakt (605 s, ware grootte 1024 x 120, geluid piek -12 dB). `meting-stil.txt`: langste stil stuk 0,2 s in de ruwe film, 1,0 s in de mp4, nergens meer dan 15 s.
- Toetsen 7 x 0 FOUT op Linux; de toets van de vlam meet nu: rekt minstens 12 procent, nooit onder 1, hooguit 6 procent per beeld, punt hooguit een derde spelpixel opzij.
- CPU: per fakkel nog steeds twee tekenopdrachten (eerst plaatje plus twee rechthoeken, nu twee stukken plaatje), dus geen extra last (GOK voor Windows, de duurtest moet het bevestigen).

**Code:** `hol/hol_3d.gd` (`teken_fakkel`, `vlam_schaal`, `vlam_zwaai`; `teken_vlam` weg), `hol/hol.gd` (de fakkel roept `teken_fakkel`), `systemen/toetsen/toets_systemen.gd`.
