# Gang in steen in plaats van één zalmroze buis (Sanne, 26 nov ±13:30 NL, issue #19)

**Waarom:** Iris (keuring 499fd9f, mooi 7): "op 1x leest de gang na 20 min nog als één zalmroze buis van rand tot rand, met overal dezelfde lichtkleur"; zij vroeg "donkerder naar beneden, minder roze, plekken met een andere kleur steen". Gemini zei eerder "too basic" en "flat". Thijs gaat de nieuwste build spelen (#19 punt d), dus wat hij ziet moet zo goed mogelijk zijn.

**Wat er voor de speler veranderde** (alleen de lichtkaart, `systemen/licht.gd`, geen nieuwe kunst):
- **Minder roze:** de schaduwkleur van de gang was koel (blauw-paars) op zalm, dat gaf roze. Nu een aardse kleur: gemiddelde tint van de gang 9 naar 18 graden (van rozerood naar bruin), rood ten opzichte van groen 1,53 naar 1,43 (GEZIEN, gemeten op beeld 420 s, x 400 tot 1500).
- **Plekken steen:** om de 5 tegels een andere steen, koele grijze steen, gewoon en gele leem, zacht in elkaar over en nooit twee dezelfde naast elkaar. Vast per kolom, dus geen flikkeren.
- **Donkerder naar de vloer:** onderaan de gang 86 procent van de kleur erboven.
- Licht om fakkel en schat blijft gelijk: dicht bij een lichtbron gaat alles nog naar hetzelfde warme licht.

**Bewijs (GEZIEN, Godot 4.3 Linux onder xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=420`):**
- `voor-en-na-ware-grootte.png`: boven main 3fddb22, onder nieuw, laatste beeld op 420 s, 1920 x 120 ware grootte. De spelloop verschilt iets (helden, goud); dat gebeurde ook zonder wijziging (Daan #165), alleen de kleur is de wijziging.
- `gang-voor-en-na-2x.png`: hetzelfde stuk gang (x 300 tot 1260) op 2x.
- `na-420s-2x.png`: het hele nieuwe beeld in twee helften op 2x.
- `na-hoogte160-60s.png`: hoogte 160, zaad 3, 60 s: ook het korte hol van de eerste minuut klopt.

**Toetsen:** 8 x 0 FOUT op Linux. `toets_licht.gd` toetst nu ook: drie plekken naast elkaar elk een andere steen, plekken liggen vast, gang donkerder naar de vloer, nergens donkerder dan 0,45, minder rood dan de oude gangkleur.

**Eerlijk:** de stekelputten worden boven de lichtkaart getekend en blijven dus hun eigen zalmkleur; in de donkerdere gang vallen ze daardoor meer op. Dat kan goed zijn (je ziet je vallen), Daan en Iris kijken ernaar. CPU: de kaart wordt alleen opnieuw gemaakt als het hol verandert, met een paar rekenstappen meer per texel (GOK: niet merkbaar, niet gemeten).
