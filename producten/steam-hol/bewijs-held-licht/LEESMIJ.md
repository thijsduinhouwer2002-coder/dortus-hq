# Licht randje om een held op donkere steen (Olaf, 27 nov ±10:15 NL, issue #256)

**Waarom:** Iris (keuring 1b0e933, punt 2 voor een 9, ook al bij deea47d): een held met donker pak zakt weg in de blauwgrijze stenen in het midden. De donkere rand van #242 helpt daar niet: donker op donker. Thijs zei 24 nov zelf dat helden niet opvallen. Rusty's Retirement (lat `organisatie/lat/hats.md`): figuren staan altijd los van de achtergrond.

**Stand (27 nov ±12:45 NL): staat AAN** (uit met startargument `licht=0`). De +7 procent van de eerste meting was het verschil tussen losse runs; binnen één run kost het hooguit enkele tienden van een procent (zie "CPU binnen één run" onderaan).

**Wat de speler ziet als het aan staat** (`godot/systemen/held_licht.gd`, aangeroepen uit `held_rand.gd`):
- Buiten de donkere rand een warm licht randje van 1 spelpx (kleur als het fakkellicht), hard op hele pixels (nearest), dekking 0,5. Volgorde van buiten naar binnen: licht, donker, lijf.
- Alleen waar het nodig is: voor koel blauwgrijs vol, voor rode baksteen half, voor oker leem niets. In het fakkellicht en bij de schat gaat het uit (lichtkaart), daar staat de donkere rand al goed.
- Komt en gaat zacht over 0,4 s, dus het knipt niet als een held van de ene steen naar de andere loopt. Ook om de hoed. Niets nieuws dat beweegt, geen tekst.
- Uit voor vergelijken: `uit3d=licht`. Voor dit bewijs: `licht_wissel=1` zet het om het andere beeld aan en uit (zelfde held, 0,2 s uit elkaar).

**Beelden** (GEZIEN, Godot 4.3 Linux onder Xvfb, `--write-movie --fixed-fps 5`, `hoogte=120 vers=1 zaad=7 uitleg_klik=6 koper=1 koper_wacht=8 balk=0 duur=540 licht_wissel=1`; per paar is het ene beeld met en het volgende zonder randje):
- `paren-boven-met-onder-zonder-1x.png` en `-2x.png`: drie helden op blauwgrijze steen, telkens boven met, onder zonder.
- `links-met-rechts-zonder-4x.png`: drie keer dezelfde held van dichtbij. Onderste rij (tovenaar in het fakkellicht, uit de eerste film met de zachte versie): geen randje, zoals bedoeld.
- `blind-a-1x.png` (met) en `blind-b-1x.png` (zonder): wat blinde lezer 2 kreeg.

**Blinde lezers** (agents zonder code of uitleg, twee beelden op 1x, GEZIEN):
| | eerste versie (zacht, dekking 0,6, 4 + 4 tekenbeurten) | deze versie (hard, 0,5) |
|---|---|---|
| hoe snel zie je het hele lijf, met randje | 4 | 4 |
| zonder randje | 2 ("broek en benen gaan op in de donkere stenen") | 3 ("romp en benen gaan op in de donkere onderste rij") |
| best los van de wand | met | met |
| wat stoort | "dik en wazig, meer gloed dan een pixelrand, een beetje opgeplakt" | "leest een beetje als een gloed of sticker, niet lelijk wel merkbaar" |
Eerlijk: beide lezers vinden de held met randje beter te zien, en beide vinden hem iets opgeplakt. Lezer 2 stelt een dunnere of donkerdere rand voor.

**CPU** (GEZIEN, echt spel 120 s, `zaad=5`, onder Xvfb met software-OpenGL, CPU-tijd van Godot plus Xvfb, met tegen `uit3d=licht`):
- Eerste versie (4 + 4 tekenbeurten): met 17,90 / 18,20 / 18,35 / 18,43, zonder 15,72 / 16,21 / 17,90 / 15,99; +10,7 procent.
- Deze versie (1 + 1 tekenbeurt, ring per blad één keer gemaakt): met 17,97 / 17,60 / 18,38, zonder 16,51 / 16,23 / 17,65; +7,0 procent.
- Een paar in omgekeerde volgorde (zonder eerst) liep niet meer in deze run.
- **Boven de eis van 2 procent.** Minder tekenbeurten maakte het nauwelijks goedkoper, dus het zit niet in het tekenen. Nog te zoeken (volgende run): meten met een wissel binnen één run (les uit `platformen/steam/balans.md`: een los paar kan veel schelen), en per stuk uitzetten (meten van de plek, de meta op de held, het tekenen).

**Toetsen:** 11 x 0 FOUT op Linux. `toets_rand.gd` toetst nu ook: 2 spelpx naar buiten, vol voor blauwgrijs, niets voor leem, uit in vol licht, vol in de donkere gang, geen randje zonder hol.

## CPU binnen één run (Olaf, 27 nov ±12:40 NL)

Les uit `platformen/steam/balans.md`: tussen losse runs scheelt het hier ±10 procent, alleen een wissel binnen één run telt.
- Startargumenten: `wissel=licht licht_blok=3` zet het licht om de 3 s aan en uit (op de klok, oneven blokken uit); `wissel=nep` doet hetzelfde maar laat het aan (placebo). `licht_keer=<n>` doet alles n keer (meten en tekenen), om de kosten boven de ruis te tillen, zoals de 100 keer stenen bij #162.
- Linux, xvfb 1920 x 1080, software-OpenGL, `hoogte=120 vers=1 zaad=5 koper=1 balk=0 drukte=1` (altijd een held in beeld), 5 tot 7 min per run. Script `platformen/steam/data/cpu-duur/cpu_licht.py`, ruwe meting in `platformen/steam/data/cpu-duur/licht/`.

| run | aan | uit | verschil |
|---|---|---|---|
| 1 keer, echt | 18,43 | 18,62 | -1,1 procent |
| 1 keer, placebo | 20,23 | 18,67 | +8,4 procent |
| 20 keer, echt | 23,19 | 19,45 | +19,2 procent |
| 20 keer, placebo | 24,04 | 20,81 | +15,5 procent |
| 100 keer, echt | 32,80 | 18,20 | +80,2 procent |
| 100 keer, placebo | 31,08 | 32,55 | -4,5 procent |

(CPU-ticks per seconde van het Godot-proces, GEZIEN.) Eén keer valt weg in de ruis (de placebo alleen al geeft tot +8). 100 keer is duidelijk: +80 procent, dus **één keer ±0,8 procent**; 20 keer min placebo geeft ±0,2 procent per keer (GEZIEN, afgeleid). Beide onder de eis van +2. Mipmaps of minder tekenen hoeft dus niet; het licht staat aan.

Toetsen 11 x 0 FOUT op Linux (GEZIEN); de Windows-toetsrun draait na de push. Nog open: de opmerking van lezer 2 ("iets opgeplakt"); dat beslist Daan in zijn keuring.

## v2: hard masker en sikkel aan de lichtkant (Olaf, 27 nov ±15:00 NL, issue #276): NIET op main

**Waarom:** Iris 3240a1b (mooi punt 1 voor een 9): randje zacht en golvend, leest als sticker. Daan #266: K1 koeler en dekking ±0,35, K2 strak op het silhouet zonder bobbel bij tonhoed en elleboog.

**Gebouwd** (code op tak `olaf-276-licht-v2`, commit 75d7119; toetsen `toets_rand` 0 FOUT): één masker voor lijf en hoed samen (geen dubbele rand), hard silhouet (alfa 0 of vol), gegroeid met afwisselend 4 en 8 buren (overal even breed), alles met Image-bewerkingen van de motor en één keer per beeld. Drie versies geprobeerd (GEZIEN, Godot 4.3 Linux, zelfde startargumenten als hierboven, `licht_wissel=1`):
1. op het raster van spelpixels: grove trapjes, een vierkante waas om de held (niet verder getoond);
2. rondom, koel blauwgrijs, dekking 0,42 (Daan K1);
3. warm, alleen aan de kant van de dichtstbijzijnde lichtbron (sikkel), niets onder de voeten. Dit is de versie in `v2-*`.

**Beelden:** `v2-boven-oud-midden-nieuw-onder-zonder-1x.png`, `-2x.png`, `-4x.png`: drie keer dezelfde held op hetzelfde moment (de films zijn tot ±250 s gelijk), boven het randje van nu (main), midden versie 3, onder zonder randje. `v2-blind-P-nieuw-2x.png` en `v2-blind-Q-oud-2x.png`: wat blinde lezer 2 kreeg.

**Blinde lezers** (agents zonder code of uitleg, GEZIEN):
| | lijf los op 1x (1 tot 5) | hoort erbij op 2x (1 sticker, 5 hoort erbij) | kiest |
|---|---|---|---|
| lezer 1: versie 2 (koel rondom) tegen main | 3 tegen 3 | 2 tegen 4: koel "leest als een uitsnede met witte contour", warm "als licht dat op de rand valt" | main |
| lezer 2: versie 3 (warme sikkel) tegen main | 3 tegen 3,5 | 2,5 tegen 4: sikkel "donkere lijn met losse lichte stukjes, uitsnede" | main |

**Besluit (Olaf):** niet op main. Beide lezers vinden het randje van nu (warm, zacht, rondom) het meest "licht dat erbij hoort" en het mooist; hard en koel (wat Iris en Daan vroegen) leest voor een frisse blik juist meer als sticker. De speler houdt het randje van #256. Wat de lezers nog noemen: rond benen en voeten wat dik en egaal (lezer 2), en echt licht is aan de lichtkant sterker (lezer 1).

**CPU** (binnen één run, `wissel=licht licht_blok=3`, 360 s, versie 2; ruw in `platformen/steam/data/cpu-duur/licht-v2/`, GEZIEN): 1 keer +14,4, 20 keer +24,1, placebo 20 keer +5,9 procent (buurparen fout ±6). Liep tegelijk met een film en twee andere metingen, dus te veel ruis om er een getal uit te halen; niet nodig zolang het niet op main komt.
