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

## Versie 2 na Daan #183 (Sanne, 26 nov ±16:45 NL)

Daan gaf 7,5 (nee). Wat er nu voor de speler anders is:
- **M1 stekelputten:** een put met een gekochte stap (of open na een klap) werd boven de lichtkaart getekend en stond als harde zalmroze rechthoek in de bruine gang. Nu tekent `hol.gd` hem pas vanaf de punten van de stekels (rij 6 van 16) en in de kleur van het licht op die plek, 20 procent lichter, zodat alleen de stekels oplichten. De koele achterwand van Mila (`hol_vast.gd`) loopt nu ook door boven de put; zonder die wand bleef de putkolom een lichtere rechthoek (GEZIEN: met de put weggelaten zag je hem nog, dus het zat in de wand). Trick Lid die schudt bij de koop krijgt ook het licht van de gang.
- **M2 plekken worden steen:** de soort per plek komt uit een hash (nooit gelijk aan de buur, geen vast ritme van drie), de plekken zijn 3,8 tot 6,2 tegels breed (gemeten in de toets 61 tot 99 spelpx), met een harde rand en een donkere staande voeg ertussen en per plek één liggende voeg op een eigen hoogte. Koele steen grijzer (geen paars).
- **Kan:** de vloerstrook waar de helden lopen is warm bruin in plaats van dof grijspaars.

**Beelden (GEZIEN, zelfde opzet als hierboven, voor = main f57708a, na = deze wijziging, 420 s, zaad 7):**
- `v2-voor-en-na-ware-grootte.png`, `v2-gang-voor-en-na-2x.png`, `v2-na-420s-2x.png`, `v2-na-hoogte160-60s.png` (de vier beelden die Daan vroeg)
- `v2-stekelput-1x-voor-en-na.png`: uitsnede op 1x rond twee stekelputten met Rusty Spikes (x 1100 tot 1500 van 2200).
De spelloop verschilt iets tussen voor en na (helden, koopmoment 229 s tegen 260 s); alleen de kleur is de wijziging.

**Toetsen:** 8 x 0 FOUT op Linux. `toets_licht.gd` toetst nu: geen buren met dezelfde steen, geen vast ritme, plekken verschillend breed, donkere voeg op de rand, liggende voegjes, warme vloer. Twee oude grenzen zijn verlaagd omdat een voeg nu met opzet donkerder is: "nooit zwart" 0,5 naar 0,4 en "steen nooit te donker" 0,45 naar 0,38 op een voeg (gewone steen houdt 0,45).
**Eerlijk:** tussen de stekels blijft iets van de oude putkleur te zien; CPU niet gemeten (de kaart wordt alleen opnieuw gemaakt als het hol verandert, per texel een paar rekenstappen meer; GOK: niet merkbaar).
