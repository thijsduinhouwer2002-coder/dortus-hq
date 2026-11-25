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
- `vlam-voor-8x.png` en `vlam-flakkert-8x.png`: de fakkel bij de ingang in een leeg hol op 70 s, 8x, voor en na.
- Toetsen 7 x 0 FOUT op Linux (nieuw in toets_systemen: tongetje minstens 1 spelpixel hoog en laag, hooguit een halve spelpixel per beeld, leeg hol 3 per s).
- CPU, ruwe proef op Linux in software (GOK voor Windows): 150 s echt spel, oud 13,3 CPU-s, nieuw 13,0 CPU-s; beelden zonder held 42 tegen 55 per 10 s. Geen verschil boven de ruis.

**Eerlijk, wat de film ook laat zien (voor Sanne en Iris):** zonder kopen blijft het hol van minuut 3 tot 10 bijna gelijk (alleen goud en de koopmuntjes boven de putten). Tempo-regel 5 hangt dus aan kopen; deze proefspeler koopt niets.

**Code:** `hol/hol_3d.gd` (`teken_vlam`, `vlam_hoogte`), `hol/hol.gd` (`VLAM_TOP`, één regel bij de fakkel), `kern/beeldtempo.gd` (`fakkels`, `fakkel_tempo`), `kern/ritme.gd` (`tel_helden`, uit strook.gd gehaald; strook.gd 424 naar 406 regels). Bekeken voor het flakkeren: onze eigen gloed (Daan juice.md) en Ropuka in de lat (werkt en slaapt zichtbaar, nooit bevroren).
