# Bovenste gang in dezelfde harde taal als de wand eronder (Olaf, 27 nov ±08:30 NL, issue #252)

**Waarom:** Iris (keuring 74f03c9, punt 1 voor een 9): de bovenste gang (lichte ronde buis met ton, houweel en rekjes) is de zachtste en leegste plek van de strook. Onder harde pixelstenen, boven zachte 3D zonder korrel: twee stijlen. Rusty's Retirement heeft één stijl (lat `organisatie/lat/hats.md`).

**Wat er voor de speler veranderde** (`godot/hol/kamerwand.gd`, aangeroepen uit `hol/achterwand.gd`, in het vaste beeld):
- **Harde bovenrand:** waar de aarde overgaat in de buis een donkere lijn van 1 spelpx (zo dekkend als de voeg in de gangwand), met hier en daar een hap omlaag en een smalle schaduw eronder, zodat de aarde over de buis hangt.
- **Ruwe aarde op hele spelpixels:** donkere en lichte spikkels van 1 spelpx in klonten (dichte en kale plekken), korte liggende laagjes van 3 tot 5 spelpx, steentjes van 2 x 1 of 2 x 2 met een lichte kop en een donkere voet, en hier en daar een barstje schuin omlaag.
- **Vloerrand:** een donkere lijn van 1 spelpx waar de wand de vloer raakt.
- **Nooit over decor:** alleen op pixels die `hol/kamerwand_masker.gd` als kale wand aanwijst, met 1 spelpx afstand tot stut, houweel, ton, fakkel en kistje in het kamerstuk. Het masker komt uit het hol-blad van Mila (`pijplijn/kamerwand_masker.py`: glad en zalmkleurig = wand; opnieuw draaien als het blad opnieuw gerenderd wordt). Wortels en rekjes in de kamer komen er daarna overheen. Niets beweegt, geen tekst.
- Alles vast per spelpixel (hash op de x in het hol): loopt door over de kolomranden, flikkert niet, en elke kolom heeft andere korrel (geen tegel).

**Beelden** (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=420`, laatste beeld op 420 s, voor = main e5c5684, na = deze wijziging):
- `voor-en-na-1x.png`: 2400 x 120 ware grootte, boven voor, onder na.
- `voor-en-na-2x-links.png`, `voor-en-na-2x-rechts.png`: elke helft op 2x, boven voor, onder na.
- `bovengang-voor-en-na-4x.png`: de lange kamer (x 850 tot 1450) op 4x.
- `blind-voor-1x.png`, `blind-na-1x.png`: de beelden die de blinde lezers kregen.
De spelloop verschilt iets tussen voor en na (goud 23 tegen 24, Gloop op een ander moment); dat gebeurde ook zonder wijziging (Daan #165). Alleen de wand van de bovenste gang is de wijziging.

**Blinde lezers** (agents zonder code of uitleg, alleen de twee beelden op 1x, GEZIEN):
- Lezer 1 (eerste versie, korrel gelijk verspreid): bij het oude beeld "boven zacht en vaag geschilderd, onder scherp en blokkerig: twee tekenstijlen", bij het nieuwe "ja, grotendeels: beide echt pixelwerk met harde randen, even scherp". Kritiek: korrel leest als ruis, geen klonten of lagen. Daarop kwamen klonten en laagjes.
- Lezer 2 (deze versie, nieuwe lezer): oud "nee, ze lijken uit twee verschillende spellen te komen", nieuw: eerste woord "steen of metselwerk", "grotendeels ja, het voelt als één spel". Kiest het nieuwe beeld als het beeld waar boven en onder het best bij elkaar horen.
- **Eerlijk, wat nog stoort (beide lezers):** de buis blijft valer en minder fel dan de gekleurde stenen eronder; het licht om de fakkel en de ronde einden van de buis lopen nog zacht uit; de aarde buiten de gangen (links van de ladder) is egaal en leeg. Dat is voor een volgende stap, niet in dit issue.

**CPU** (GEZIEN, echt spel 120 s onder Xvfb, zelfde args zonder film, om en om gemeten, gebruiker plus systeem in CPU-s):
- Eerste versie (korrel elke keer opnieuw uitgerekend): voor 17,93 / 17,43 / 17,60, na 17,98 / 17,84 / 19,04, gemiddeld +3,6 procent. Te veel, dus:
- Deze versie (per kolom één keer uitgerekend en bewaard): voor 18,19 / 18,92 / 18,91 / 18,42, na 19,36 / 18,70 / 18,44 / 18,54; gemiddeld 18,61 tegen 18,76, **+0,8 procent**, binnen de ruis (één losse run wijkt tot 4 procent af).
- Los gemeten in Godot headless: 150 kolommen uitrekenen 24 ms, daarna uit het geheugen 0,2 ms. Per beeld kost het niets: het vaste beeld is een SubViewport die alleen opnieuw tekent bij graven of een put.

**Toetsen:** 11 x 0 FOUT op Linux, geen SCRIPT ERROR. `toets_licht.gd` toetst nu ook: masker van de kale kamer is de hele buis, geen korrel op houweel en ton of op de fakkel, alle 6856 pixels van 5 stukken over 40 kolommen vallen op kale wand (0 buiten het masker), de bovenrand is donker en dekkend, de korrel ligt vast en de buurkolom heeft andere korrel.
