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

## Versie 3: metselwerk (Olaf, 26 nov ±19:45 NL, issue #210)

**Waarom:** Iris (keuring bb298d3 punt 3): op 1x weinig verschil tussen de vlakken steen. Gemeten: de drie soorten lagen in helderheid binnen 0,035 van elkaar (gewoon 0,59, koel 0,56, leem 0,55; GEZIEN in `licht.gd`). Een eerste poging met alleen meer verschil per plek en een lichte bovenrand gaf een blinde lezer "aarde" met "zachte banden", geen steen (GEZIEN).

**Wat er voor de speler veranderde** (alleen de lichtkaart `systemen/licht.gd`, geen nieuwe kunst):
- **Blokken steen:** de wand van de gang is nu metselwerk: rijen van 8 spelpx, blokken van één tegel breed, elke rij een half blok verschoven, een donkere voeg boven en links van elk blok en een lichte rand eronder en ernaast. De soort hoort bij het hele blok, dus de rand van een plek loopt langs de voegen. Elk blok is net iets anders (plus of min 6 procent).
- **Meer verschil tussen de soorten:** koel 0,54, gewoon 0,66, leem 0,75 helder (was 0,56, 0,59, 0,55). In het beeld op 420 s: gewoon tegen koel 11 tot 22 grijswaarden verschil (was 5; GEZIEN, gemiddeld per plek, y 28 tot 112).
- **Niet roziger:** gemiddelde tint van de gang (x 400 tot 1500) 14,5 naar 15,4 graden (GEZIEN, zelfde meetvlak voor en na; hoger is minder roze). Leem houdt r/g 1,04.
- Vloerstrook blijft glad en warm, licht om fakkel en schat gelijk.

**Blinde lezer** (agent zonder code of uitleg, alleen `v3-blind-beeld-1x.png`): "achterwand van baksteen. Eerste woord: baksteen. Donkere, bruinpaarse metselsteentjes in rijen." Hij telt "ongeveer 2 soorten": een lichtere warmere band en een donkerder paarsbruine (GEZIEN). **Eerlijk:** de 2 soorten die hij telt beschrijft hij als licht en donker "door lichtval", niet als ander materiaal, en hij noemt de wand "vrij eentonig". De leemplekken vallen in dit zaad in het licht van fakkel en kamers, dus geel zie je hier weinig. Bij de vorige versie (zelfde vraag, nieuwe lezer) was het eerste woord "aarde".

**Beelden (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=420`, voor = main 8180855, na = deze wijziging):**
- `v3-voor-en-na-ware-grootte.png`: 2200 x 120, boven voor, onder na, beeld op 420 s.
- `v3-gang-voor-en-na-2x.png`: gang x 300 tot 1260 op 2x.
- `v3-blind-beeld-1x.png`: het beeld dat de blinde lezer kreeg (twee helften op 1x).
- `v3-na-hoogte160-60s.png`: hoogte 160, zaad 3, 60 s, het korte hol van de eerste minuut.

**CPU:** het beeld per frame is gelijk (dezelfde lichtkaart als textuur in het vaste beeld). De kaart zelf maken kost nu minder: 34 ms tegen 45 ms voor een hele kaart van 46 tegels breed (GEZIEN, twee keer gemeten in één run, Godot headless). In 420 s werd 46 keer gegraven, dus de kaart wordt hooguit ±50 keer opnieuw gemaakt. CPU dus niet hoger (GEZIEN voor de kaart; het geheel binnen +1 procent).

**Toetsen:** 9 x 0 FOUT op Linux (de 9 uit de Windows-toetsrun). `toets_licht.gd` toetst nu: staande voeg tussen blokken, liggende voeg boven elk blok, lichte rand eronder, rijen verschoven, alle drie soorten komen voor, leem minstens 0,15 lichter dan koel, gang gemiddeld donkerder naar de vloer. In koele steen is de voeg minder diep (0,86 in plaats van 0,80), zodat "nooit zwart" (0,4) blijft gelden.

## Versie 4: scherp metselwerk in de wandkunst (Olaf, 26 nov ±21:50 NL, issue #210 na Daan #214)

**Waarom:** Daan #214 nee 7: M1 voegen wazig (de lichtkaart heeft 1 texel per 2 x 2 spelpixels en wordt lineair uitgerekt), M2 soorten alleen verschillend in helderheid, M3 voegen liepen over stut, houweel en ton.

**Wat er voor de speler veranderde:**
- **M1:** het metselwerk staat nu in het vaste beeld van het hol zelf (`hol/metsel.gd`, aangeroepen uit `hol/achterwand.gd`), op hele spelpixels met nearest: een voeg is 1 spelpx breed en hard. De lichtkaart legt er alleen nog licht en donker op (`systemen/licht.gd`, geen voegen of plekken meer).
- **M2:** elke soort heeft een eigen tint over de wand: koel blauwgrijs, gewoon zoals de wand, leem oker. Bij de rand van een plek nemen sommige blokken de soort van de buur, zodat de soorten in elkaar grijpen in plaats van te verspringen.
- **M3:** alleen op de gangwand, getekend ná de koele wand en vóór stenen in de wand, stutten, spinrag, vloerdingen, putten en figuren. De kamers boven de gang (waar stut, houweel en ton in de tegel zitten) krijgen geen voegen meer.
- Na de eerste blinde lezer ("plat tegelpatroon, goedkoop behang"): blokken 10 tot 22 spelpx breed (vast per blok), lichte bovenkant, donkere onderkant en zijkant, op ±1 op 3 blokken een afgebrokkelde hoek.

**Blinde lezers** (agents zonder code of uitleg, alleen het beeld op 1x, GEZIEN):
- Lezer 1 (versie zonder breedteverschil): eerste woord "steen", "muur van rechthoekige stenen"; telt 3 soorten (aarde, blauwgrijze blokken, oker blokken); grijs en oker "deels alleen andere kleur of belichting". Noemt de muur "herhaald plat tegelpatroon".
- Lezer 2 (`v4-blind-beeld-1x.png` op de versie met verschillende breedtes, nog zonder in elkaar grijpen): eerste woord "aarde" (hij bedoelt de kamers boven de gang), dan "in de onderste helft loopt een muur van stenen blokken"; telt 3 materialen, waarvan "grijs en zandkleurig lijken me ook twee soorten steen". Geen voegen over voorwerpen gezien. Kritiek: harde rechte overgang van aarde naar steen, en de kleur verspringt zonder reden (daarop kwam het in elkaar grijpen; dat is niet meer blind getoetst).

**Beelden** (Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=420`, voor = main cac2cc7, na = deze wijziging):
- `v4-voor-en-na-ware-grootte.png` (2400 x 120 elk, boven voor), `v4-gang-voor-en-na-2x.png` (x 300 tot 1260), `v4-blind-beeld-1x.png`, `v4-na-hoogte160-60s.png` (zaad 3, eerste minuut).

**CPU:** echt spel 120 s, om en om 3 keer: voor 16,66 / 16,04 / 15,81, na 16,05 / 16,01 / 16,59 CPU-s, gemiddeld 16,17 tegen 16,22, dus +0,3 procent, binnen de ruis (GEZIEN). Het metselwerk kost alleen iets als het vaste beeld opnieuw getekend wordt; de lichtkaart rekent minder per texel.

**Toetsen:** 9 x 0 FOUT op Linux. `toets_licht.gd` toetst nu `metsel.gd`: geen buren met dezelfde steen, geen vast ritme, alle drie soorten, koel blauwer en leem okerder in tint, voeg donker en dekkend, twee rijen met een voeg van 1 spelpx, blokken verschillend breed, diep in een plek altijd de soort van die plek, bij de rand in elkaar grijpen, lichtkaart zonder voegen.
**Opgeruimd:** de achterwand (130 regels) uit `hol/hol_vast.gd` naar `hol/achterwand.gd`; `hol_vast.gd` 835 naar 720 regels (nog boven 400).
