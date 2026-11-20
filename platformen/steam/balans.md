# Het Hol: startgetallen voor de balans (Sanne)

Stand 9 nov 2026, ±19:10 UTC. Voorstel voor de **eerste speelbare versie**, zodat Olaf en Bram niet met losse gokgetallen bouwen. Bram's `sim/` is de echte toets; dit is een ruwe proef om te starten (`platformen/steam/data/balans-proef.py`, vast zaad, speler koopt steeds het goedkoopste). Alle getallen GOK tot Bram's sim en een speelronde ze bevestigen.



## Stand 17 nov ±10:00 UTC: drempels 49 / 60 / 72 gemeten, keurregel groen (Sanne, GEZIEN in `hol.log` van run 44048277638)
Run 44048277638 (demo-inhoudtak 31e2c98, nieuwe drempels, `steamdemo=1 koper=2 zaad=1794860558`, 75 min, editor; `schermen` → `steam-hol-duur/claude-steam-hol-demo-inhoud-steamdemo-1-koper-2-zaad-1794860558-1920x1080/`): hol 9 / 10 / 11 / 12 op 1753 / 2255 / 2707 / **3198 s (53,3 min)**. Gaten 8,4 / 7,5 / 8,2 min, het grootste gat in de hele run is 7,7 min (8 naar 9). **Mijn regel vooraf (hol 12 binnen 70 min, geen gat boven 14 min): groen.** Hol 12 komt 5 min eerder dan mijn schatting van 58; dat is goed, niet te snel: eerste uur 12 namen, gemiddeld één per 4,4 min.
**Wat dit opent:** tussen hol 12 (53 min) en het demo-einde (winkel vol, ±110 min voor koper=2) komt geen nieuwe naam meer. Nageteld in dezelfde `hol.log` (kroniek per 10 min): 51 / 48 / 50 / 39 / 41 / 43 / **43** regels, dus na hol 12 loopt de kroniek even druk door als ervoor, met terugkomers en wrok ("Tibbe III came back once too often.", "Gerda III is back for the Spike Pit.") en het winkeldoel in beeld. Geen leeg uur, wel een uur zonder grote mijlpaal. **Besluit: niets aan veranderen voor de speeltest.** De speeltest duurt 15 tot 30 min en zegt hier dus niets over; ik kijk het na in de eerste lange speelsessie van Thijs of de eerste duurtest van 120 min (vraag aan Olaf als hij er ruimte voor heeft, geen haast). Mijn regel dan: in elk blok van 10 min na hol 12 minstens één terugkomer of wrokregel en minstens 30 kroniekregels.
**Erbij uit dezelfde run, voor de teksten:** `Gloop says thanks for the snack. +6` 7 keer (meest herhaald), `val_bewoner` samen 16 keer; 6 keer `Sir` voor een vrouwennaam. Beide opgelost in het ontwerp van 10:00 (`features.md`: hap per soort, Dame).

## Stand 17 nov ±08:58 UTC: drempels 49 / 60 / 72 nagemeten op twee echte runs, blijven staan (Sanne, na Iris keuring 20 punt 3)
**Hoe:** geen model meer. Elke vangst geeft in `hol.log` een kroniekregel die eindigt op ` +<goud>`; tijd van die regel min zijn wachttijd is het moment van vangst k, dus faam k. Telling klopt precies met alle `HOL hol-niveau`-regels in beide logs (GEZIEN). Script `data/hol-tempo/faam_uit_log.py`, uitkomst `data/hol-tempo/uitkomst-gemeten.txt`. Zo lees je bij een run met de oude drempels af wanneer de nieuwe gehaald waren (dezelfde helden, dezelfde vangsten).

| run | hol 9 | hol 10 (49) | hol 11 (60) | hol 12 (72) | grootste gat |
|---|---|---|---|---|---|
| main editor 44030107525, 60 min | 32,0 | 46,1 | 55,8 | niet binnen 60 (67 vangsten op 60,2); GOK ±64 bij 1,2 per min | **14,1** (naar hol 10) |
| demo-inhoud 44040279373, 75 min, koper=2 | 37,7 | 44,3 | 50,4 | **58,5** | 10,1 (naar hol 7) |

Ter vergelijking met de oude drempels 53 / 69 / 88 in dezelfde 75-min run: hol 10 op 46,0, hol 11 op 56,2, hol 12 op 67,8, grootste gat 11,6 min.

**Wat Iris zei klopt:** mijn model van 07:55 zei voor main hol 10 op 41,6 met de nieuwe drempel; gemeten is het 46,1 (4,5 min later), want main heeft een trage stuk van 30 tot 40 min (7 vangsten tegen 11 tot 12 elders). Dat telt het model niet.

**Besluit: 49 / 60 / 72 blijven.** Hol 12 binnen 70 min haalt de 75-min run ruim (58,5) en main naar schatting ook (±64, GOK). De regel "geen gat boven 14 min" haalt main net niet (14,1), door dat ene trage blok; de andere run zit op 10,1. Eén meetpunt van 0,1 min over de grens is geen reden om de toetsen van Olaf weer om te gooien. **Regel vooraf voor duurtest 44048277638** (nieuwe drempels, klaar ±09:55): hol 12 binnen 70 min en geen gat boven 14 min. Gat toch boven 14: hol 10 naar **47** (main dan 12,9 min naar hol 10 en 10,9 naar hol 11; 75-min run 5,3 en 7,4). Hol 12 later dan 70: dan 72 naar 68.

**Demo-einde in deze run (vraag van 05:58 aan Olaf, nu zelf gelezen):** geen `HOL demo voorbij` binnen 75 min. Hol 12 kwam (67,8 met oude drempels), maar de winkel stond op slijm 2 en stekelput 2 met 329 goud, en stap 3 kost 353 per soort. Goud kwam laat binnen met ±11 per minuut, dus GOK: slijm 3 op ±78 min, stekelput 3 en het demo-einde op **±110 min** voor koper=2 (koopt, graaft niet). Met de nieuwe drempels zit daar ±50 min tussen hol 12 en het einde met alleen twee aankopen; de laatste ±32 min komt er niets nieuws. Dat is de traagste speler (graaft niet); wie graaft krijgt tot +3 per vangst (graafbonus), GOK einde rond 90 tot 95 min. **Nog niet aan de prijzen draaien**, eerst meten: na de speeltest één duurtest van 120 min met `koper=1` (graaft en koopt) en `steamdemo=1` op de nieuwe drempels. Regel vooraf: `HOL demo voorbij` binnen 100 min en geen stuk van meer dan 25 min zonder nieuw niveau of aankoop. Haalt hij dat niet, dan gaat stap 3 van 353 naar 280 (factor 2,8 naar 2,5 voor de laatste stap), voor iedereen: het volle spel krijgt meer winkeldingen, dus een goedkopere derde stap haalt daar niets weg.

## Stand 17 nov ±07:55 UTC: hol 10 tot 12 sneller, nieuwe drempels 49 / 60 / 72 (Sanne, na Iris keuring 19 punt 2)
**Vraag (Iris):** in de duurtest van main (44030107525, editor) komt hol 10 pas op 49 min, met 17,5 min zonder niveau ervoor, en hol 11 en 12 niet binnen het uur. Brams .exe-run (44018723753, zelfde zaad) had hol 10 op 39 min. Waar zit het verschil, en moeten de drempels omlaag?

**Wat ik zag (GEZIEN, `hol.log` op `schermen` → `steam-hol-duur/main-zaad-1794860558-1920x1080/`, script `data/hol-tempo/tempo.py`):**
- Faam is het aantal gevangen helden (`kern/afloop.gd`: +1 per val). Het tempo is dus vangsten per minuut.
- Helden komen in main heel gelijk binnen: 19 tot 23 per 10 min, het hele uur. Maar in minuut 30 tot 40 vluchtten er 13 en vielen er maar ±7 (andere blokken: 6 tot 9 vluchters, ±12 vangsten). Dat blok is precies het gat tussen hol 9 en 10.
- Beide runs lopen gelijk tot hol 4 (296 tegen 307 s) en gaan daarna uit elkaar. Zelfde zaad geeft na een paar minuten niet meer dezelfde helden, omdat editor en .exe andere beeldtijden hebben en het toeval dan anders valt. **Het verschil is dus vooral toeval** (GOK: geen bewijs voor een codeverschil; daarvoor zou ik twee runs op dezelfde code nodig hebben, en die zijn het niet waard).
- Belangrijker: **ook Brams snelle run haalt hol 12 niet rond 57 tot 63 min.** Met zijn eigen tempo vanaf hol 6 (1,28 vangst per min) komt hol 12 op ±68 min; met het tempo van main (1,03) op ±79 min. De oude schatting kwam uit het tempo van alleen het laatste stuk.

**Besluit (Sanne, balans is mijn keus): drempels voor hol 10, 11 en 12 worden 49, 60 en 72** (waren 53, 69 en 88). Hol 2 tot 9 blijven (3/5/7/12/17/25/31/39).

| | hol 10 | hol 11 | hol 12 | grootste stap |
|---|---|---|---|---|
| oud, tempo main 1,03 | 45,5 (echt 49,4) | 60,9 | 79,3 | 19 vangsten, ±18 min |
| oud, tempo exe 1,28 | 40,4 (echt 39,1) | 52,9 | 67,7 | 19 vangsten, ±15 min |
| **nieuw, tempo main** | **41,6** | **52,2** | **63,8** | **12 vangsten, ±12 min** |
| **nieuw, tempo exe** | **37,3** | **45,9** | **55,2** | **12 vangsten, ±9 min** |

**Waarom:** de stappen groeiden van 8 (hol 8 naar 9) ineens naar 14, 16 en 19. Dat is de grindmuur die we niet willen, precies waar de demo moet eindigen. Nu 10, 11, 12: elke stap iets groter, maar nooit meer dan ±12 min wachten voor wie alleen kijkt. Hol 12 komt dan rond een uur (55 tot 64 min), wie koopt is eerder. Het demo-einde hangt ook aan de volle winkel, dus de demo wordt hier niet korter van; alleen het bordje stopt niet meer op hol 10.

**Waarom niet lager:** wie hol 12 al op 45 min heeft, kijkt de rest van het uur naar een vol bordje terwijl de winkel nog niet op is. Op 16 nov 19:55 (punt 5) hield ik de drempels omdat hogere drempels de gaten groter maakten; dit gaat de andere kant op, dus dat bezwaar geldt niet.

**Wat het kost:** één regel in `hol_niveau.gd` (`DREMPEL`). De toetsen in `toets_systemen.gd` blijven groen (88 is nog steeds hol 12, `weg_regel(3, 88)` blijft "Grew 10 levels"); `inhoud_proef=1` zet faam 88 en blijft dus ook goed. Voorstel extra toets: `HN.niveau(72) == 12 and HN.niveau(71) == 11`. Het weg-tempo (hooguit 2 niveaus per nacht) blijft.

**Wanneer:** Olaf beslist. Mijn voorkeur: na de speeltest van za 21 nov, samen met de demo-inhoudtak, zodat de speeltest en de lopende 75-min run (44040279373) op hetzelfde meten. Thijs komt zaterdag met half uur plus een nacht op hol 7 tot 9, dus hij merkt het verschil nog niet.

**Regel vooraf voor de eerste 60-min duurtest daarna (gewoon spel, editor):** groen als hol 12 binnen 70 min komt en geen gat tussen twee niveaus langer is dan 14 min. Haalt hij dat niet, dan kijk ik naar het vangtempo (vluchters), niet weer naar de drempels.

## Stand 17 nov ±03:50 UTC: regel vooraf voor poort (b), voor de uitslag van main als .exe (Sanne, na Bram 03:40)
**Wat er ligt (Bram, GEZIEN in `data/cpu-duur/LEESMIJ.md`):** de speeltestbuild als .exe (44008361789, 959aef4, alleen) gaf **1,334**, 18,6 ms per beeld. Stil spel in die .exe 0,47 en `cpu bij helden=0` 0,73, gelijk aan main: mijn vraag over stil spel is dicht (Iris keuring 15: het editorverschil was een uitlijningsfout). Alle runs sinds ±02:00 zitten op 18,4 tot 19,0 ms, voor middernacht gaf dezelfde soort .exe 12,1. Main c38f267 als .exe op hetzelfde zaad loopt (klaar ±03:57).

**Mijn regel, vastgelegd voor ik de uitslag zie, zodat het geen dobbelen wordt:**
1. **Main als .exe per beeld binnen 20% van de tak (dus hooguit ±22,3 ms en minstens ±15,5 ms; CPU ruwweg 1,1 of hoger):** het ligt aan de runner. Poort (b) wordt dan: **.exe van de tak tegen .exe van main, in een paar, hooguit 20% per beeld duurder.** De vaste 1,0 geldt dan alleen op Thijs' eigen pc, via het Taakbeheer-getal dat hij bij de speeltest van za 21 nov opgeeft (nieuw in `speeltest-21-nov.md` punt 3; let op: de build schrijft zelf geen CPU in een log, de regel "CPU staat in de speeltestlog" van 16 nov klopte niet) (regel 3 hierboven blijft: 0,8 op zijn pc voor de demo). De speeltestbuild op main is dan goed zoals hij is.
2. **Main als .exe meer dan 20% per beeld goedkoper (onder ±15,5 ms, CPU rond 0,85):** de tak is echt duurder. De speeltestbuild blijft voorlopig op main (de spelregels wegen zwaarder voor de speeltest, zie 01:25), Bram zoekt met een `wissel=` binnen één .exe-run welke commit het is. Is het do 19 nov 12:00 UTC niet gevonden, dan beslist Olaf of de duurste commit eruit gaat voor de speeltest.
3. Ertussenin bestaat niet: 20% is de grens, net als bij (a). Valt het binnen 2 punten van de grens, één nieuw .exe-paar, het gemiddelde telt.

**Uitslag (±04:02 UTC, GEZIEN: `uitslag.txt`, `hol.log`, `cpu-per-10s.txt` van beide .exe-runs op `schermen`, zelf gedraaid met `cpu_per_beeld.py` en `cpu_stil.py`):**

| .exe, zaad 1794860558, alleen | CPU | beelden per 10 s | ms per beeld | stil | geen held, vast nieuw | held in beeld |
|---|---|---|---|---|---|---|
| tak 959aef4 (44008361789) | 1,334 | 71 | 18,6 | 0,47 / 16,3 ms | 1,35 / 13,1 ms | 1,68 / **20,1 ms** |
| main c38f267 (44011218826) | 1,023 | 71 | 14,5 | 0,97 / 25,8 ms | 1,49 / 16,8 ms | 0,95 / **11,6 ms** |

Tak tegen main: **+28% per beeld**, 8 punten boven de grens, dus **regel 2 geldt**, zoals vooraf vastgelegd. Ik reken Brams gemiddelde met het editor-paar (+16%) niet mee: dat zou een regel achteraf zijn, en een editor-paar en een .exe-paar meten iets anders.

Wat dat betekent, eerlijk:
- De speeltestbuild blijft op main. De spelregels wegen zwaarder voor de speeltest dan een kwart meer werk per beeld (zie 01:25), en het absolute getal zegt op deze runners niets meer: **main zelf als .exe gaf 1,023**, boven de 1,0, terwijl dezelfde soort run voor middernacht 0,71 tot 0,86 gaf.
- ~~Het verschil zit alleen met een held in beeld; zonder held is de tak juist goedkoper.~~ **Rechtgezet 17 nov 04:50 na keuring 16 (Iris):** dat was dezelfde uitlijningsfout als in keuring 15 (tak en main met een andere L). Met gelijke L is de tak zonder held gelijk of duurder en met held +24 tot +39%. Ik weet dus niet waar het zit, en noem geen kanshebbers. Het tegenbewijs blijft: het editor-paar van dezelfde twee commits gaf +3%. Niet nog een paar draaien, maar meten waar ruis niet bij kan.
- **Opdracht Bram:** een `wissel=` binnen één .exe-run (zoals bij de deco) die de spelregel-commits per blok aan en uit zet, of als dat niet kan het kaartje en de regels apart. Binnen één run vallen de runners weg. Uitkomst in `data/cpu-duur/LEESMIJ.md`.
- **Do 19 nov 12:00 UTC** niets gevonden of onder de 20% binnen één run: dan was het ruis en is de tak vrij. Wel gevonden en meer dan 20%: Olaf beslist of die commit eruit gaat voor de speeltest (zijn bouw, zijn keus).
- **Poort (b) voortaan:** .exe tak tegen .exe main in een paar, hooguit 20% per beeld, en bij twijfel een `wissel=` binnen één run. De vaste 1,0 (en 0,8 voor de demo) geldt op Thijs' pc via het Taakbeheer-getal.
- **Uitslag en gesloten (Sanne, 17 nov 05:55 UTC):** Brams `wissel=regels` binnen één .exe-run (44018723753, 40 min, groen, tabel in `data/cpu-duur/LEESMIJ.md` r.153) geeft bij elke L **alles uit duurder** dan alles aan (+6 tot +15%), niet meer dan 16% goedkoper. Dat is punt 3 van Brams regel vooraf, gelijk aan punt 2: de +28% van het .exe-paar zit niet in de spelregels. Nagekeken in de tabel, niet alleen in zijn bericht. **De vraag is dicht, vóór de grens van do 19 nov:** het was de runner. Geen runs meer hiervoor. Les die blijft: een los .exe-paar op deze runners kan ±25% schelen; voor CPU telt alleen een `wissel=` binnen één run, en het echte oordeel is het Taakbeheer-getal op Thijs' pc (`speeltest-21-nov.md` punt 3).

## Stand 17 nov ±03:15 UTC: het paar is binnen, regels-tak naar main, nieuwe CPU-poort (Sanne, na keuring 14 punt 1 en Olafs regel vooraf)
**Het paar (GEZIEN, zelf gedraaid met `cpu_per_beeld.py` op `uitslag.txt` en `hol.log` van tak `schermen`, zaad 1794860558, 20 min, 1920x1080, editor, elk alleen en direct na elkaar):**

| run | wat | CPU gem. | ms per beeld | CPU zonder held in beeld | met held |
|---|---|---|---|---|---|
| 44001895099 | `claude/steam-hol-regels` 959aef4 | 1,325 | 19,0 | 1,40 | 1,27 |
| 44005445378 | main c38f267 | **1,276** | 18,4 | 0,73 | 1,66 |

Tak tegen main in het paar: **+4% CPU, +3% per beeld**, ver onder de 20%. Main zelf zat deze keer ook boven 1,0. Eerder op hetzelfde zaad gaf main 0,844 en de tak 1,013. Dezelfde code geeft dus tussen runs 0,84 tot 1,28: één losse editor-run tegen een vaste 1,0 is een muntworp. Iris had gelijk.

**Besluit (Sanne):**
1. **`claude/steam-hol-regels` (959aef4) gaat naar main**, als de toetsrun groen is. Volgens Olafs eigen regel vooraf (minder dan 20% per beeld in het paar = runner). Speeltest za 21 nov krijgt de spelregels.
2. **Nieuwe CPU-poort, vervangt regel 1 tot 3 van 16 nov 23:55 en de aanvulling van 01:25.** Een tak mag langs de poort als (a) **in een paar** (tak en main op hetzelfde zaad, elk alleen, direct na elkaar) de tak per beeld hooguit 20% duurder is dan main, en (b) **de .exe van de tak** (wat Thijs draait) gemiddeld onder 1,0 blijft. Valt (a) net boven 20%: één nieuw paar, het gemiddelde van de twee paren telt. De editor-run alleen tegen een vaste 1,0 beslist niets meer; Olaf mag de rode grens in de editor-duurtest een waarschuwing maken (zijn workflow, zijn keus).
3. Regel 4 en 5 van 16 nov blijven: 0,8 op Thijs' eigen pc voor de demo, en de volgorde van inleveren.
4. **Deco** (87ffe43, 793a6e5, 2380714, ee19bd6) mag na de regels naar main zonder nieuwe poort: Brams `wissel=deco` binnen één run is precies zo'n paar (0 tot 1 ms per beeld). Wel één toetsrun, voor fouten, niet voor CPU.

**Eén ding dat ik niet wegpraat (aan Bram, na de speeltest, niet blokkerend):** zonder held in beeld zit de tak twee runs op rij hoger dan main (1,40 tegen 0,94 in Olafs vergelijking, 1,40 tegen 0,73 nu), met minder beelden (47 tegen 54 per 10 s). Met held is het andersom. In totaal valt het weg, maar een bureau-app staat vooral stil. Kijk in de .exe-run na de merge of `cpu bij helden=0` hoger is dan op main voor de merge; zo ja, zoek wat er draait als er niemand is (plat-toestand van Gloop, kaartje, wachtrij).

## Stand 17 nov ±01:25 UTC: aanvulling op de CPU-regel (Sanne, na Brams losse duurtest en keuring 12)
**Uitslag (GEZIEN door Bram en Iris):** de tak alleen gedraaid, run 43985774466 (c1fa66a): **1,321**, 18,4 ms per beeld tegen main 11,9 op hetzelfde zaad, evenveel beelden. Muisvlak en doorzicht zijn het niet (Brams wissel-proeven onder de meetlat). Regel 3 greep: de tak gaat zo niet naar main.
**Aanvulling (Sanne):** voor de speeltest van za 21 nov gaan **de spelregels voor de deco**. Weg 0,12, de korte regels, de naamgenoot-regel en de graafbonus lossen de problemen van keuring 9 tot 11 op; de losse dingen in gang en kamers maken het mooier, maar zonder de spelregels test Thijs een build waarin één nacht de hele winkel geeft. Dus: een build met **alleen de spelregel-commits** mag naar main als zijn losse duurtest (alleen gedraaid) onder 1,0 blijft. De deco komt pas terug na een meting binnen één run (`wissel=deco`) die niet meer dan 20% duurder per beeld laat zien. Olaf kiest wat het eerst klaar is en hoe hij de commits scheidt.

## Stand 16 nov ±23:55 UTC: CPU-grens voor de tak en de speeltest (Sanne, na keuring Iris 23:00 punt 1)
**Wat er ligt (GEZIEN in keuring 11 en Brams `data/cpu-duur/LEESMIJ.md`):** gewoon spel, zelfde zaad 1794860558: main 0,844, controle 0,948, tak 1,281 (liep naast drie andere runs), proef 1,357. Bram draaide dezelfde .exe drie keer: 0,71 tot 0,86. CPU tussen runs zegt op deze runners dus vooral iets over de machine, niet over het spel. De 0,8 was mijn wens; hij hoort bij de demo, niet bij de speeltest.

**Besluit (Sanne, het getal is van mij):**
1. **De grens van 1,0 in de workflow blijft staan.** Niet oprekken.
2. **Een rode run die naast andere duurtests liep telt niet als oordeel over het spel.** De tak `claude/steam-hol-regels-weg` mag naar main als één herhaling van de gewone duurtest **alleen** (geen andere duurtest tegelijk) onder 1,0 blijft, of als Brams proef binnen één run (`wissel`) laat zien dat de tak per getekend beeld niet meer dan 20% duurder is dan main. Eén van de twee is genoeg; Olaf kiest wat het eerst klaar is.
3. **Blijft de tak ook alleen boven 1,0:** niet naar main voor de speeltest, eerst uitzoeken wat duurder werd (deco in gang en kamers is het enige nieuwe dat de hele tijd in beeld staat).
4. **0,8 is de eis voor de demo van 18 dec, gemeten op Thijs' eigen pc** (CPU staat in de speeltestlog). Daar beslist het echte getal, niet de runner.
5. **Is het te zwaar op Thijs' pc, dan leveren we in deze volgorde in:** eerst de momenten op 20 beelden per s terug naar 10, dan deeltjes en licht (juice) kleiner, pas als laatste het ritme. Held in beeld onder 45% kost meer plezier dan een paar beelden per seconde, want op 120 px ziet bijna niemand het verschil tussen 10 en 20.

Waarom zo: Iris heeft gelijk dat "rood maar toch naar main" niet kan. Maar de grens verzetten op ruis is net zo fout. Een losse herhaling kost één run en geen bouw.

## Stand 16 nov ±22:50 UTC: graaftoets gelezen, graafbonus blijft ook als je weg bent (Sanne, na Olaf 22:40)
**Uitslag (GEZIEN door Olaf, tak `schermen`, `steam-hol-duur/claude-steam-hol-regels-weg-koper-{1,2}-zaad-1794857447-1920x1080/`, 20 min, zelfde zaad):** graver verdient **234**, alleen kopen **117**, dus +100%. Mijn eis was minstens +15%: ruim gehaald. Per val +45% (±9,4 tegen ±6,5): dat is precies de graafbonus op zijn hoogst (+3 op 6, plus wat terugkomers), dus zo bedoeld. De rest komt van meer vangsten (61% tegen 41%); de helden lopen niet gelijk, dus dat deel is geluk en tel ik niet als effect van graven. Iris (keuring 10) zag ook valregels van +9 tot +15 en geen zin vaker dan 3 keer.

**Wat ik om 22:00 te mooi schreef:** "de volgende ochtend is er nog wat te kopen" klopt alleen voor wie weinig graaft. Nagerekend voor een graver (GEZIEN, `data/sim-weg-nacht/avond.py`, `avond-uitkomst.txt`, 200 zaden): 30 min spelen (koopt put 1+2 en slijm 1+2, houdt ±29 over), dan 8 uur weg op 0,12 met kans 0,79. Met graafbonus in de ochtend **963** (864 tot 1071), de laatste twee kosten 706, dus de winkel is altijd leeg. Zonder graafbonus bij weg 690, 28% van de zaden leeg.

**Besluit (Sanne): niets veranderen, graafbonus blijft ook bij weg.** Waarom:
1. Het verhaal klopt: een groter hol trekt rijkere helden, ook 's nachts. De bonus alleen bij kijken geven voelt als een straf voor weggaan, en dat is onze vaste regel niet.
2. De speeltestbuild is de demo: 6 dingen in de winkel en hol 12 als eind, samen ±1,5 tot 2 uur. Een graver die een half uur speelt plus een nacht (±een uur spelen) heeft dan ±1,5 uur gehad; dat de winkel dan op is, is de demo die ophoudt, niet een fout in de nacht. Wat de tweede dag wel houdt: hol-niveaus (na 30 min ±hol 7 of 8, de nacht geeft hooguit 2, dus 2 tot 3 niveaus te halen in het spelen) en Gloop.
3. Een kleinere bonus bij weg haalt het niet echt (zonder bonus nog 28% leeg) en kost een regel bouw plus een nieuwe toets, twee dagen voor de tak naar main moet.

**Wel bekend en eerlijk opschrijven voor de speeltest (Olaf, `speeltest-21-nov.md`):** wie veel graaft heeft zondag goud zonder iets om te kopen. Dat is versie 3 (lagen en kamertjes, Brams prijzen), niet de demo. Vraag Thijs daar niet over, kijk alleen of het hem opvalt.

**Ook bekend, voor versie 3:** de graafbonus zit na 24 gegraven cellen op zijn hoogst (+3); de graver in de toets haalde dat in ±10 min. Daarna levert graven in de demo alleen nog ruimte en beeld op. Voor 2 uur demo is dat goed. In versie 3 moet graven per laag weer iets opleveren (Brams lagen geven graven per laag een eigen prijs; de bonus per laag hoort daarbij).

**Olafs vraag over 1632:** klopt wat hij dacht. "Goud 1e nacht 1632" in `data/sim-v3-weg/uitkomst.txt` is de nacht na werkdag 1 van versie 3 (6 open uur spelen, meer vallen en upgrades), niet mijn toets vanaf de beginopstelling. Mijn toets is Olafs Windows `weg-1.log`: vers hol, 8 uur, **+511**, faam 5 van 66, hol 3. Gehaald (onder 1048, hooguit hol 3). Mijn verwachting "650 tot 910" ging uit van +3 graafbonus, maar een vers hol heeft 0 gegraven, dus 559 (hoogste 643) was de juiste verwachting; 511 valt daarin.

**Brams x 1,4 in plaats van x 1,7:** gezien, goed zo. Hol 50 op 119,5 open uur, de gaten zijn niet slechter. Dat was de afspraak (buiten 100 tot 130 dan zelf zetten).

## Stand 16 nov ±22:00 UTC: een nacht weg na het nieuwe ritme, en de kroniek minder herhalen (Sanne, na Iris keuring 9)
**Vraag 1, weg:** Iris (keuring 9, `schermen/steam-hol/main/weg-1.log`, run 43953061155) zag 8 uur weg vanaf 20 goud: **+1098 goud en faam 143**, dus de hele winkel (1048) en hol 2 tot 12 in één keer. Klopt: mijn regel van 14:05 was "een nacht is minder dan de winkel" en die heb ik om 19:55 niet opnieuw nagerekend toen `HELD_ELKE_S` naar 30 ging. Mijn fout.

**Nagerekend (GEZIEN, `data/sim-weg-nacht/weg.py`, `uitkomst.txt`, zelfde rekenwijze als `voortgang.gd`, begin: 1 put en Gloop, kans 0,64; 200 zaden):**

| Snelheid weg | helden in 8 u | gevallen (= faam) | goud zonder graafbonus | met graafbonus +3 | +3 en kans 0,85 | hol vanaf 0 |
|---|---|---|---|---|---|---|
| 0,25 (nu) | 240 | 155 | 1170 | 1635 | 2076 | 12 |
| 0,17 (Iris' GOK) | 163 | 105 | 793 | 1108 | 1414 | 12 |
| 0,15 | 144 | 93 | 702 | 981 | 1251 | 12 |
| **0,12 (KEUS)** | **115** | **74** | **559** (hoogste 643) | **781** (hoogste 907) | 997 | 11 |
| 0,10 | 96 | 62 | 468 | 654 | 834 | 10 |

**Besluit (Sanne):**
1. **`SNELHEID` 0,25 naar 0,12** in `voortgang.gd`. Een nacht is dan ongeveer **een uur spelen** (in het spel ±10 goud per minuut), ongeveer de helft van de winkel, en ook met de volle graafbonus blijft het onder de winkel (hoogste van 200 zaden 907). De 0,17 van Iris haalt de grens niet meer zodra de graafbonus meetelt (1108). Het plafond van 12 uur blijft. Hoeden en de kans op de aartsvijand gaan vanzelf mee (±42 hoeden per nacht in plaats van ±80; nog steeds een berg).
2. **Faam als je weg bent: hooguit 2 hol-niveaus per keer weg.** Zonder plafond geeft ook 0,12 vanaf 0 meteen hol 11. Het bordje is de reden om te kijken; als één nacht het afmaakt, is de tweede speeldag leeg (keuring 1). Regel: faam uit de weg-stap telt tot net de drempel van huidig niveau + 2, de rest van die nacht telt niet als faam. Goud, hoeden en de kroniek van de nacht veranderen niet. Waarom eerlijk: er gaat niets weg wat je had, net als het plafond van 12 uur; faam is wat er rondverteld wordt, en 's nachts kijkt niemand. Tekst: geen nieuwe zin (op Olafs tak zijn de regels "Grew N levels" al weg; de optocht en de rij tonen dan hooguit 2 niveaus). Bouw: één regel in `kern/opslag.gd` bij `AFLOOP.faam_erbij(s, weg.faam)` (regel 133): weg-faam afkappen op de drempel van niveau(faam_voor) + 2 min faam_voor.
3. **Toets voor Olaf (stap 'Weg geweest'):** 8 uur weg vanaf 0, beginopstelling, graafbonus +3: goud **onder 1048** (verwacht 650 tot 910) en hol-niveau hooguit 3. En 8 uur weg vanaf hol 6: hooguit hol 8. De oude grens van 1572 vervalt.

**Wat het betekent voor de speeltest van za 21 nov:** Thijs speelt een half uur 's avonds (GOK hol 7 tot 8, koop 2 of 3), laat het 's nachts staan, en ziet 's ochtends ±560 tot 780 goud en 2 niveaus erbij. Er is dan nog wat te kopen en nog 2 tot 3 niveaus te halen in het spelen, precies de tweede dag die keuring 1 miste.

**Vraag 2, kroniek:** in 20 min 16 tot 18 naamgenoot-regels uit drie zinnen (Iris, `hol.log` .exe-run 43953082236). Met helden om de ±30 s en 12 namen is na minuut 5 bijna iedereen een naamgenoot. Thijs schrijft de tekst zelf, dus de oplossing is minder regels, geen nieuwe zinnen.

**Besluit (Sanne):** de naamgenoot-regel (`naamgenoot` en `naamgenoot_hoed`) komt **één keer per voornaam per speelbeurt** (dus "Kees II" wel, "Kees III" daarna niet; na terugkomst van weg begint de telling opnieuw, zoals Daans plat-regel). Een latere naamgenoot krijgt de gewone binnenkomstregel van zijn soort, en heeft hij een wrok, dan de terug-regel die de wrok noemt (dat is nieuw nieuws). Verwacht: hooguit ±8 naamgenoot-regels in de eerste 20 min, daarna bijna geen. Samen met Daans plat-regel (twee keer) gaat het aandeel herhaalde zinnen in 20 min van ruim een kwart naar GOK onder 10%. Toets: de teller in `uitslag.txt` (Olaf bouwde hem): geen enkele zin vaker dan 4 keer in 20 min.

**Klein, gezien en gelaten:** veel valregels noemen de val niet ("Kees will not be leaving. +6"). Klopt, maar wie keek zag het, en het oplossen kost nieuwe zinnen. Niet nu.

## Stand 16 nov ±21:00 UTC: graven moet iets opleveren (Sanne, na Bram 20:35 en Olaf 20:50)
**Vraag:** Brams meting (30 zaden, `data/graaf-vangst/LEESMIJ.md`): een graver vangt evenveel als wie niets doet (14,1 tegen 13,9 per 20 min). Mijn eis "wie graaft vangt minstens evenveel" haalt het, maar graven doet dan niets voor het hol. In `features.md` beloofden we "graven: het hol groter, meer goud per val later". In de speeltestbuild klopt dat niet: in het spel is het goud per val 6 plus 3 per eerder bezoek, los van de gang (`afloop.gd`). Thijs graaft in de speeltest het meest van alles; als dat niets doet merkt hij het.

**Wat de nieuwe duurtests zeggen (GEZIEN, `schermen` → `steam-hol-duur/`, nieuw ritme):** de winkel van de speeltestbuild is per soort 45 / 126 / 353 (slijm en put elk, samen 1048). koper=1 (graaft 41 keer) kocht op 2,4 / 9,0 / 19,6 min; koper=2 (graaft niet) op 2,9 / 9,1 min en daarna niets meer in 20 min. Het gat zit dus tussen de tweede en de derde koop (±10 min sparen voor 126). Goud per minuut ±10.

**Twee knoppen vergeleken:**
- (a) Brams idee, een kamer geeft de dichtstbijzijnde val een kleine kans erbij. Nadeel: meer vangsten is ook sneller faam, en het bordje loopt al snel (hol 12 rond 58 min). En je ziet het niet: een kans is onzichtbaar.
- (b) **Groter hol, rijkere helden: meer goud per val per gegraven stuk.** Je ziet het in elke valregel (+7, +8, +9) en in de munten. Het raakt de faam niet, en het helpt precies op het gat tussen koop 2 en 3. Het is ook wat de sim al rekent (`voortgang.gd` en `sim/`: goud x (1 + gangen / 40)).

**Besluit (Sanne):** (b), klein gehouden.
1. **Goud per val = 6 + 3 per eerder bezoek + graafbonus.** Graafbonus = **+1 per 8 gegraven cellen, hooguit +3** (bij 24 cellen). De begingang telt niet; alleen wat de speler zelf groef.
2. **Weg rekent mee:** `voortgang.gd` gebruikt dezelfde graafbonus (nu vast `gangen 6` = 7 per val, wordt 7 + graafbonus), zodat weg een kwart van spelen blijft.
3. **Undo/weghalen** van een gang is er niet; graven blijft gratis. Dus de bonus kan niet omhoog en omlaag gesjoemeld worden.
4. Tekst: geen nieuwe zin. De valregel toont het hogere getal al vanzelf (+7, +8, +9), en volgens het besluit van Thijs van 16 nov 21:05 is alle speltekst concept tot hij hem schrijft en liever beeld dan zin. (Mijn eerdere hoverzin "Bigger hole, richer heroes." trek ik in.)

**Nagerekend (GEZIEN, ±20:55 UTC, Brams sim, speeltestbuild met het nieuwe ritme, 40 zaden, graver 41 cellen per 20 min; `data/sim-graafbonus/graafbonus.py`, `uitkomst.txt`), koop 1 tot 6 in min, mediaan (ergste):**

| Variant | koop 2 | koop 3 | koop 4 | koop 5 | winkel leeg |
|---|---|---|---|---|---|
| niet graven / graver zonder bonus (gelijk, zoals Bram mat) | 8,2 | 22,0 (27,0) | 34,5 | 62,8 | 89,8 (98,1) |
| **graver +1 per 8, hooguit +3 (KEUS)** | 7,4 | **17,5** (21,4) | 26,4 | 47,3 | **66,1** (74,3) |
| graver +1 per 8, hooguit +2 | 7,4 | 18,2 | 28,1 | 50,7 | 71,9 |
| graver +1 per 4, hooguit +6 | 6,5 | 14,8 | 21,5 | 38,4 | 53,3 |

**Waarom +3 en niet groter:** de derde koop komt voor een graver 4,5 min eerder, het gat waar het om ging (koop 2 naar 3) gaat van ±14 naar ±10 min. Met +6 is de winkel al na 53 min op. Eerlijk: ook met +3 is de winkel voor iemand die zo veel graaft na ±66 min op in plaats van ±90 (mijn GOK van 75 was te zonnig). Dat lege tweede uur bestond al; de echte oplossing blijft de v3-economie na de speeltest. +2 scheelt maar 6 min en voelt kleiner, dus +3. Wie niets doet verandert niet.

**Wat het kost:** een paar regels in `afloop.gd` en `voortgang.gd` plus een teller van zelf gegraven cellen in de save. Geen nieuw beeld. Past in de speeltestbuild van vr 20 nov; lukt het niet meer voor do 19 nov, dan gaat het naar de v3-economie en blijft graven in de speeltest zoals het nu is (vangt evenveel, kost niets).

**Toets:** duurtest koper=1 en koper=2 met hetzelfde zaad. Geslaagd als de graver op 20 min minstens 15% meer goud heeft verdiend dan koper=2 en de derde koop eerder valt, en het gewone spel (niemand klikt) hetzelfde goud geeft als nu.

**Aanvulling ±22:05 UTC: eerste helft van de toets is binnen (GEZIEN).** `schermen` → `steam-hol-duur/claude-steam-hol-regels-weg-koper-1-zaad-1794857447-1920x1080/` (run 43959515338, commit 2ed8709, 20 min, graaft 41 cellen): graafbonus 1 na 8 cellen, 2 na 16, 3 na 24 (`HOL gegraven kolom ... (zelf 24, graafbonus 3)`), dus precies de regel. Valregels daarna **+9** (en +12 voor een terugkomer) in plaats van +6. 25 vangsten, **234 goud uit valregels** in 20 min. **Kopen op 208 / 528 / 1048 s: de derde koop op 17,5 min**, precies de mediaan van mijn sim (17,5) en 2 min eerder dan de koper-run van keuring 9 (1174 s, a90df14). Hol 7 op 1193 s. Ter vergelijking dezelfde koper met hetzelfde zaad op het oude main (run 43948608381, bd26b2c, zonder bonus en zonder haperfix): 18 vangsten, 114 goud, maar 2 kopen, hol 6; die vergelijking is niet eerlijk (haperfout), dus de echte maat blijft koper=2 (run 43959522480, nog niet op `schermen`). CPU van deze run 1,11 (de graver had eerder 0,59 en 0,81): schommeling of iets in de tak, Olaf of Bram kijkt mee met het muisvlak. Voorlopig oordeel: **de graafbonus doet wat hij moet doen**; definitief als koper=2 er is.

## Stand 16 nov ±19:55 UTC: ritme in het gewone spel (Sanne, na Iris keuring 7)
**Vraag:** Iris mat in de duurtest van 20 min (run 43931188663) dat er **62% van de tijd geen held in beeld** is, gaten mediaan 30 s, nooit twee helden tegelijk, en 13% van de tijd geen held terwijl Gloop plat ligt. Zij gaf drie knoppen: (a) helden sneller na elkaar, (b) Gloop korter plat, (c) soms twee helden kort na elkaar. Ik kies met Brams sim, speeltestbuild (graven gratis, upgrades 45/126/353, drempels 3/5/7/12/17), 40 zaden, held ±15 s in beeld. Script: `platformen/steam/data/sim-ritme/ritme.py`.

**Uitkomst (GEZIEN, mediaan over 40 zaden, eerste 20 min):**

| Variant | held in beeld | gat zonder held | geen held + Gloop plat | helden in paar | ergste gat koop/hol min 1-20 | min 1-60 | hol 6 | hol 12 |
|---|---|---|---|---|---|---|---|---|
| nu (35-45 begin, 40-60 later, plat 60) | 33% | 33 s | 20% | 4% | 10,7 | 14,1 | 21 min | 98 min |
| (b) alleen plat 30 | 33% | 32 s | 12% | 4% | 8,4 | 17,5 | 18 | 94 |
| (a) 25-35 altijd | 51% | 15 s | 23% | 2% | 8,1 | 14,0 | 14 | 61 |
| (a) 25-35 + plat 30 | 51% | 15 s | 15% | 2% | 7,4 | 13,5 | 12 | 59 |
| **(a+b+c) 28-38, 15% kans paar (6-10 s), plat 30** | **49%** | **18 s** | **17%** | **16%** | **7,6** | **13,5** | **13** | **58** |
| (a) 25-35 alleen tot min 20, daarna 40-60, plat 30 | 51% | 15 s | 15% | 2% | 7,4 | 22,5 | 12 | 84 |

De sim geeft voor nu 33% in beeld; de echte build mat 38%. De sim zit dus iets aan de lage kant, de verschillen tussen varianten tellen.

**Besluit (Sanne, het ritme is mijn keus):**
1. **Tijd tussen helden 28 tot 38 s** (was 35 tot 45 in het begin en 40 tot 60 daarna), ook na de vaste stappen van BEGIN. De eerste stappen (5-7 s en 18-22 s) en het lied van de bard (8-20 s) blijven.
2. **15% kans dat de volgende held al na 6 tot 10 s komt** (niet tijdens BEGIN, niet als het lied loopt). Dan lopen er twee kort na elkaar: de een ziet de ander in de put vallen, of ze staan samen voor Gloop. Ongeveer elke 3 min een paar. Gemiddeld komt er zo een held per ±30 s.
3. **Gloop 30 s plat** (was 60). Bouncy Gloop houdt zijn factor 2/3, dus 20 s.
4. **Weg-tempo mee: `HELD_ELKE_S` 47,5 naar 30** in `voortgang.gd`, zodat weg nog steeds precies een kwart van spelen is (mijn regel van 14:05). Een nacht levert dus ±1,6 keer zoveel als nu; dat is geen extra, het is hetzelfde kwart van een sneller spel.
5. **Drempels en prijzen blijven** (3/5/7/12/17/25/31/39/53/69/88, 45/126/353). Hogere drempels voor hol 8 tot 12 geprobeerd: dan wordt het ergste gat in uur 1 slechter (15,3 tegen 13,5 min), dus niet.

**Waarom:** (a) is de enige knop die het lege deel echt kleiner maakt (33 naar 49%); (b) alleen helpt niet voor beeld, wel voor de stilte met een platte Gloop, want meer helden betekent ook vaker plat; (c) kost bijna niets en geeft het moment dat Iris mist (twee helden die elkaar iets aandoen). Meer helden is ook meer goud: de kopen vallen op 2, 8, 22, 35, 63 en 90 min in plaats van 3, 12, 37, 57, 106 en 151 (mediaan), en het gat tussen minuut 5 en 20 waar ik om 18:55 geen oplossing voor had wordt ook kleiner (ergste 10,7 naar 7,6 min). Eén knop, twee problemen.

**Wat het kost (eerlijk):**
- Hol 12 (Gloop's Empire) komt rond **58 min** in plaats van 98. In een demo van ±2 uur komt er daarna niets nieuws meer op het bordje. Voor de speeltest van za 21 nov maakt dat niet uit (Thijs speelt het begin en een nacht); voor de demo van 18 dec rekenen we het opnieuw met de v3-economie, daar komen kamertjes en laag 2 bij.
- De winkel van de speeltestbuild is op na ±90 min in plaats van ±150.
- CPU: helden die lopen zijn de dure stukken (Olaf 13 nov: de metingen boven 1 zijn de stukken met helden). GOK: gemiddeld van ±0,55 naar ±0,7 CPU-s per 10 s, nog onder de grens van 1. Olaf meet het met de duurtest.
- "Gloop is flat. Back soon." komt vaker voor (Iris: nu al 5 keer in 20 min). Vraag aan Daan: na de tweede keer een andere regel of geen regel.

**Toets:** Olaf draait na de bouw dezelfde duurtest (20 min, 1920x1080, gewoon spel) en `ritme_meting.py`. Geslaagd als held in beeld **minstens 45%**, langste stuk zonder held en zonder regel **onder 40 s**, gemiddelde CPU **onder 0,8**. Haalt het de CPU niet, dan 32 tot 42 s in plaats van 28 tot 38 (sim: ±44% in beeld).

**Aanvulling ±20:10 UTC: de koper-duurtest is binnen en verandert het beeld (GEZIEN).** Run 43939923957 (commit 8fdb410, `koper=1`, 20 min, 1920x1080, `schermen` → `steam-hol-duur/main-koper-1-1920x1080/`), `ritme_meting.py` door mij gedraaid: **92%** van de tijd een held in beeld, langste stuk zonder held 21 s. Maar: de koper graaft ook (41 keer in 20 min, zoals de demo-film) en dan gaat het vangen mis. 28 helden binnen, 16 renden weg; hol 3 op **689 s** (gewoon spel 366), hol 4 op **1103 s** (531), eerste koop pas op **433 s** (259) en **maar één koop in 20 min**. CPU gemiddeld **1,233** (boven de grens van 1), `hol_vast` loopt op bij elke graaf. GOK over de oorzaak: in een lange gang met kamers lopen helden langer, lopen ze vaker langs de vallen naar de schat en rennen ze weg, dus minder vangsten en minder goud.
Wat dit betekent:
1. Leegte is een probleem van de speler die **niets** doet; wie graaft heeft juist bijna altijd een held in beeld. Mijn ritmekeus blijft voor het gewone spel, met één extra regel: **buiten een paar nooit meer dan 2 helden tegelijk in de gang** (nu 3), zodat een graver niet nog meer CPU en drukte krijgt.
2. **Graven straft nu.** Graven is gratis en voelt als vooruitgang, maar het halveert de vangsten. Dat is het omgekeerde van wat het moet zijn, en Thijs graaft za 21 nov zeker. Dit gaat voor op het ritme. Naar Olaf en Bram: waarom vluchten helden in een lange gang (16 van 28)? Mijn eis voor de speeltest: een speler die graaft vangt **minstens evenveel** als een speler die niets doet. De koper graaft wel extreem (elke ±9 s); een tweede koper-run die alleen koopt en niet graaft scheidt de twee oorzaken.

## Stand 16 nov 18:55 UTC: het gat tussen minuut 5 en 20 in de speeltestbuild (Sanne, na Bram 18:50)
**Vraag:** Bram zegt dat het gat in minuut 5 tot 20 (ergste 10,7 min zonder koop of nieuw hol-niveau) niet met drempels op te lossen is. Lukt het met prijzen, of met drempels voor hol 5 tot 7? Gerekend met Brams sim, zelfde opzet als `sim/samenval.py` deel 3 (graven gratis, 40 zaden). Scripts en aanpak: `platformen/steam/data/sim-prijzen/` (`prijsladder.py`, `zoek.py`, `drempels.py`, `lang.py`).

**Uitkomst (GEZIEN):**
1. **Prijzen helpen bijna niet.** Het gat komt van het inkomen (±6 tot 7 goud per minuut in het begin), niet van de ladder. 45/90/180, 45/75/200, 45 x 1,8 en de rest: ergste gat blijft 10,7 min. Beste van 105 ladders (35/50/x of 40/x/x): 9,3 min, maar dan is de winkel na ±90 min op in plaats van ±150. Niet doen.
2. **Hol 5 en 6 eerder (3/5/7/9/14) maakt minuut 1 tot 20 beter** (ergste 8,2, mediaan 5,5, bijna nooit samen met een koop), **maar schuift het gat naar later**: over minuut 1 tot 40 wordt het ergste gat 15,7 tot 20,5 min (nu 13,4), over 1 tot 60 18,2 tot 20,5 (nu 14,1).

| Reeks hol 2 tot 7 | min 1 tot 20 ergste / mediaan | min 1 tot 40 | min 1 tot 60 |
|---|---|---|---|
| **nu 3/5/7/12/17/25** | 10,7 / 6,1 | 13,4 / 9,1 | 14,1 / 11,2 |
| 3/5/7/9/14/25 | 8,2 / 5,5 | 20,5 / 13,1 | 20,5 / 13,3 |
| 3/5/7/9/14/21 | 8,2 / 5,5 | 15,7 / 10,8 | 18,2 / 12,0 |

**Besluit: 3/5/7/12/17 blijft (Olafs keus), prijzen blijven 45/126/353 voor de speeltest.** Waarom: de build heeft in het eerste uur gewoon te weinig dingen om te krijgen; met getallen schuif je het gat alleen heen en weer, en het eerste uur als geheel is nu het best. Wat het echt oplost is de v3-economie (kamertjes en dingen met een prijs van ±1 uur goud, daar is het ergste gat 8,4 min), en dat komt na de speeltest.

**Wat dit gat niet meet:** de vrije momenten die geen koop zijn (eerste wrok rond 63 tot 75 s, het lied van de bard, een nieuwe bladzijde in het heldenboek, hoeden op de toren). Of minuut 5 tot 20 saai voelt, zegt dus niet deze tabel maar (a) Olafs `e2e/ritme_meting.py` op de Windows-duurtest (langste stuk zonder held en zonder kroniekregel) en (b) Thijs zelf bij vraag 1 van de speeltest ("wanneer verveelde je je"). Zegt hij "rond minuut 10", dan is dit de oorzaak en is de eerste fix na de speeltest een ding van ±60 goud dat je rond minuut 8 tot 12 kunt kopen (het eerste kamertje uit v3), geen nieuwe drempels.

## Stand 10 nov 03:05 UTC: heldensoorten, elke soort een eigen zwakte (Sanne, antwoord op Bram 02:30)
**Probleem met de eerste getallen (Bram, GOK):** drie van de vier soorten zijn zwakker tegen Gloop en sterker tegen de put, de ridder is overal gewoon. Dan is het antwoord op elke soort "meer Gloop", en voegen de soorten geen keuze toe (gat 1 uit `toppers.md`). Gemeten met Brams sim (`data/soorten-keuze.py`, 8 zaden, 10 uur, GEZIEN): de put vangt bij elke soort minder dan bij een gewone held, ook bij de ridder (25% put tegen 39% slijm).

**Besluit:** de ridder wordt de held van de put: **ridder slijm 0,7, put 1,4** (zwaar harnas: hij past niet in Gloops mond, maar zakt wel door elke vloer), **bard 1,1 en 1,1** (zwak overal, iets minder dan 1,15 zodat hij nog weleens ontsnapt en zingt). Dief (slijm 1,15, put 0,5), magiër (1,25, 0,3), taai, snelheid en de wegingen (55, 15, 15, 10, 5) blijven zoals Bram ze zette.

**Uitkomst (GEZIEN, zelfde sim):**
| Soort | Bram: slijm / put / vlucht | Besluit: slijm / put / vlucht |
|---|---|---|
| gewoon | 41 / 23 / 36% | 42 / 23 / 35% |
| ridder | 39 / 25 / 36% | **32 / 36 / 32%** |
| dief | 48 / 14 / 39% | 49 / 12 / 39% |
| magiër | 52 / 9 / 39% | 53 / 10 / 37% |
| bard | 51 / 22 / 26% | 48 / 24 / 28% |
| alles | vluchten 36,2% | vluchten 35,1% (doel ±1 op 3 gehaald) |

**Waarom zo:** nu loont het om de put te upgraden als er veel ridders komen, en Gloop als het dieven en magiërs zijn. Dat is een keuze die je in een bezoek kunt maken en die je terugziet in de kroniek. Het Heldenboek kan per soort "Weak to: Spike Pit" laten zien zodra je hem een keer zo ving (versie 1). Met meer vallen in versie 1 (rolsteen, lijmplaat) krijgen dief en magiër elk hun eigen zwakte; dan stel ik dit opnieuw bij.

**Voor Bram:** `heldensoort.gd` DATA en `sim.py` SOORT_DATA naar deze getallen, en de uitleg van de ridder wordt "Heavy armor. Too big for Gloop. Pits love him." (eerlijk: zegt wat de getallen doen). Reken `python3 sim.py soorten` na. **Rekenscript gerepareerd:** `data/ritme-bezoeker.py` zet nu `UPG_BASIS` en `GRAAF_DREMPEL` in plaats van tekst te vervangen (moet-punt controleur 01:50); de tabel hieronder blijft kloppen (GEZIEN, opnieuw gedraaid: 16/21/49, 25/26/28 en 40/41/42 min, alles na 7,0 tot 7,8 u). Alleen "upgrade 45 zonder toeslag" wordt 5,6 tot 6,8 u (stond er al zo).

## Stand 10 nov 01:50 UTC: ritme van de eerste upgrade (Sanne, antwoord op Bram 01:40)
**Besluit:** (1) **upgrade stap 1 kost 45** (stappen 45, 126, 353; `45 x 2,8^n`), (2) **graven kost 5 + 1,2 x gangen, plus 3 per gang boven de 12** (heb je 13 gangen, dan kost de volgende 24 in plaats van 21; bij 20 gangen 53 in plaats van 29; de laatste, bij 39 gangen, 133 in plaats van 52; afgerond op hele munten), (3) **het muntje boven Gloop of de put blijft staan zolang je die upgrade kunt betalen, ook als graven goedkoper is.** Graven blijft een klik op aarde (geen regel op het kaartje). De demo houdt zijn 66 goud aan het begin: dan kan hij Big Gloop rond 20 s kopen en houdt hij 21 over voor de rest van de minuut.

**Waarom:** Brams sim koopt na elke held meteen het goedkoopste. Een echte speler kijkt eens per zoveel minuten (T1) en ziet dan het muntje. Ik rekende dat na met Brams sim en mijn eigen bezoekersmodel (`data/ritme-bezoeker.py`: zelfde regels, alleen het kopen anders: eerste 10 min ongeveer elke minuut kijken, daarna elke 5, 15 of 30 min, steeds bij de eerste held na dat moment; kan een upgrade, dan eerst die). Uitkomsten GEZIEN in die sim met 20 zaden; hoe spelers echt kijken is een GOK. Eerste upgrade (min/mediaan/max):
| Speler | upgrade 60, graven zonder toeslag | upgrade 45 + toeslag graven |
|---|---|---|
| koopt steeds het goedkoopste (Brams sim) | 136 / 154 / 170 min | 50 / 61 / 72 min (`data/ritme-varianten.py`) |
| kijkt elke 5 min, muntje eerst | 28 / 48 / 87 min | 16 / 21 / 49 min |
| kijkt elke 15 min, muntje eerst | 25 / 26 / 43 min | 25 / 26 / 28 min |
| kijkt elke 30 min, muntje eerst | 40 / 41 / 42 min | 40 / 41 / 42 min |

Het muntje doet het meeste werk: wie maar af en toe kijkt, heeft het goud al bij elkaar en koopt de upgrade bij het eerste bezoek. De 45 helpt wie vaak kijkt en dus steeds graaft. De toeslag op graven heeft een andere reden: bij Brams speler staat het hol nu na 1 uur op 20 tot 24 gangen en is alles na 5,9 tot 6,6 uur gekocht; met het besluit 18 tot 19 gangen na 1 uur (bezoekers 11 tot 18) en alles na 7,0 tot 7,8 uur (doel was ±7). Het hol groeit dan over dagen, niet in een middag (T2: elke week groter). Upgrade 45 zonder toeslag zou alles al na 5,6 tot 6,8 uur laten zijn.

**Wat het verandert en wat niet:**
- Vluchten blijft 33 tot 39% (was 31 tot 38%; alleen gemeten bij Brams speler, `ritme-varianten.py`).
- Aankopen in uur 1: bezoekers 8 tot 14 (was met 60 en het muntje 6 tot 17). Wie vaak kijkt koopt iets minder, want graven wordt duurder; wie elke 30 min kijkt iets meer.
- **Het langste gat zonder aankoop in uur 1 wordt groter:** bij Brams speler 6,7 tot 16,5 min (was 5,5 tot 13,4). Dat accepteer ik: in dat gat spaar je naar iets dat je ziet (Big Gloop), en het muntje laat zien wanneer het kan. Bram: reken je doel "langste wacht" na met de nieuwe getallen; komt het boven 20 min, dan zakt de toeslag naar 2.
- Graven kost in het spel nog geen goud (Olaf 01:50: komt voor het Fest); dit is het getal waarmee dat gebouwd wordt. Bram: `BASIS` in `upgrades.gd` naar 45 en beide in `sim.py`.

## Stand 9 nov 19:50 UTC: Bram's sim gaat voor (Sanne akkoord)
Bram's simulatie (`producten/steam-hol/sim/UITKOMST.md`) liet zien dat mijn startgetallen 68 tot 74% vluchten gaven, omdat een held in het spel omdraait na een klap. Zijn nieuwe getallen gelden, ik ben het met elk punt eens: **slijm 45%, put 35%, schijterig draait de helft van de keren om, faam x 0,97 per niveau met bodem 0,75, volgende held is een terugkomer 25%, een gevluchte held komt 60% ooit terug (aartsvijanden altijd), een aartsvijand die aan de beurt is komt 15%.** Uitkomst: 36 tot 41% vluchten, aartsvijand ongeveer één keer per dag, langste wacht 7 tot 11 min in het eerste uur, alles gekocht na 6,4 tot 7,1 uur. Kosten en goud hieronder blijven.

Drie dingen die ik er nog bij zie:
1. **Goud per val:** de tabel zegt 6 bij de start, `strook.gd` regel 180 geeft `3 + 2 x bezoeken` (film: +3 per val). Het idee van Olaf is goed: een terugkomer is meer waard, dus een held met een wrok is een beloning en geen last. Voorstel: **6 x faam-factor + 3 per eerder bezoek** (een aartsvijand na drie vluchten is dan 15 waard). De sim rekent met 6; met 3 duurt de eerste aankoop twee keer zo lang. Bram, wil je de 3 per bezoek in de sim zetten? Olaf beslist.
2. **De helden die "met pensioen" gaan** (40% van wie vlucht komt nooit terug) zijn een kans voor een kroniekregel bij openen ("Pim the Once-Fled retired. Opened a bakery."), geen straf. Staat in `kroniek-regels.md` als ik er tijd voor heb.
3. **Hoard-Toucher 3 tot 6%** is weinig voor een van onze beste grappen. Goed zo voor de balans, maar in de film van een minuut moet hij één keer te zien zijn (demo mag dat sturen, zoals `moet_vallen`).

## Getallen (startvoorstel 19:10; kansen en faam vervangen door de stand hierboven)
| Wat | Waarde |
|---|---|
| Held komt binnen | elke ±50 s (past bij `strook.gd` 25 tot 70 s en `voortgang.gd` 47,5 s) |
| Kans dat een held valt per verdediging op zijn pad | slijm 30%, stekelput 22%, +7 procentpunt per upgrade |
| Helden worden sterker met faam | elke 60 helden één faamniveau: kans per verdediging × 0,9, goud per val +10% |
| Goud per gevallen held | 6 × (1 + 0,1 × faam) × (1 + gangen / 40) |
| Graven, één cel | 5 + 1,2 × aantal gangcellen (start met 6 cellen, dus de eerste kost 12; max 40 cellen); vanaf 10 nov plus 3 per gang boven de 12 (zie boven) |
| Extra slijm of put | je begint met één van elk; extra kost 104, 270, 703 (40 × 2,6^aantal; max 4 van elk; de tweede pas bij 8 gangcellen, de derde bij 16, de vierde bij 24) |
| Upgrade per bewoner of val | 60, 168, 470 (× 2,8; drie per soort); vanaf 10 nov 45, 126, 353 (zie boven) |
| Weghalen of dichtgooien | volle prijs terug |
| **De eerste held van een nieuw spel** | valt altijd (een schijterige held die in de put struikelt), zodat je in de eerste minuut goud ziet (toets 1 in `spelgevoel.md`) |

## Wat de proef laat zien (GEZIEN, één zaad; drie andere zaden in haakjes)
- Eerste aankoop na 100 s (150 tot 200 s).
- Eerste uur: 13 aankopen, nooit langer dan 7 minuten wachten. Dat is "bij elk bezoek iets te kopen" (T1).
- Tot 3 uur: 32 aankopen, langste wachttijd 13 min; tot 6 uur: 44, langste 25 min. Geen muur: de wachttijd groeit langzaam.
- Alles van de eerste versie gekocht na ±7 uur open tijd (6,9 tot 7,9). Voor een prototype genoeg; versie 1 moet hier ±40 uur van maken (`features.md`).
- Vluchten: 36% (38 tot 43%). Doel was ongeveer 1 op 3, dus er blijven genoeg helden met een wrok over voor verhalen.

## Wat dit niet meet
De wrok (een held met wrok loopt naar zijn vijand en is daar misschien sterker of zwakker), aartsvijanden, de Hoard-Toucher, en het plafond van 12 uur terwijl je weg bent. Dat hoort in Bram's sim. Ook niet: of het **voelt** goed. Dat toets ik op de volgende GIF en, als die er is, op een echte speelronde.

## Besluit 20 nov 2026 (Sanne): stilte in de eerste 3,5 minuut
Vraag van Iris (bericht 13:50 UTC): geldt de grens 20 s of 32 s voor de langste stilte in de eerste 3,5 min? Op de tak `claude/steam-hol-niveau-gat` halen 3 van 5 zaden de 20 s niet (27,7 / 21,3 / 20,3 s, GEZIEN door Iris en Olaf in `data/vers-20nov-niveau/`), steeds een leeg hol nadat een held weg is.
**Besluit: 20 s blijft de lat, alleen voor de eerste 3,5 min.** Regel voor Olaf: is het hol in de eerste 210 s speeltijd van een nieuw spel leeg nadat een held weg is (gevlucht of opgegeten), dan komt de volgende held binnen ±8 s; daarna geldt gewoon `HELD_S` 28 tot 38 s. Geen nieuwe woorden, niet na weg zijn, niet in de demo-minuut (die heeft zijn eigen script). Keurregel: langste stilte (geen held in beeld en geen regel) in de eerste 210 s onder 20 s in 5 van 5 zaden.
**Waarom:** de eerste minuten beslissen of iemand de demo openhoudt of het spel terugvraagt (geld), en 28 s een leeg hol direct na de start leest als "kapot", niet als rust. Na 3,5 min mag het rustig worden; dat is het spel.
**Voorwaarde:** pas bouwen na de speeltest van za 21 nov. Zegt Thijs dat het begin te druk is of te snel gaat, dan vervalt dit en geldt 32 s (keuring 24).
