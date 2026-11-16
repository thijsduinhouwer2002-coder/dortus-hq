# Hats of the Fallen: voortgang voor ±100 uur (Sanne, game-ontwerper)

Versie 2, 16 nov 2026 ±13:55 UTC (versie 1 ±13:30). Versie 2 verwerkt Brams narekening met lagen (`producten/steam-hol/sim/LAGEN.md`), Iris' keuring 1 (`keuring/2026-11-16-13.md`) en Olafs bouwfeiten van 13:38. Opdracht hoofdchat 16 nov 13:10 (Thijs 13:01: "een diepgaand spel ... level ups enzo om een reden te hebben om te spelen"). Eerste versie gevraagd wo 18 nov 12:00.
Bronnen: Fenna `platformen/succes/diepte-toppers.md` (prestatie-percentages, GEZIEN), Olaf `planning-fest-2027.md` ("Diep spel met level ups"), Brams sim `producten/steam-hol/sim/sim.py voortgang`. Nagerekend met die sim: `platformen/steam/data/voortgang-maak.py` maakt `data/voortgang.json`, uitkomst in `data/voortgang-uitkomst.txt` (versie 1, GEZIEN, 8 zaden); versie 2 en het voorstel voor versie 3 in `data/sim-v2/` (GEZIEN, 8 zaden).
Status: **eigen helden per laag nagerekend en vast 16 nov ±18:00 UTC (nep-schat: terugkomende ontdekker loopt recht op de schat af; valluik alleen voor de mijnwerker; kroniekregel kwart snelheid weg, zie "Narekening eigen helden"); eigen helden per laag ontworpen 16 nov ±17:00 UTC; versie 3 definitief 16 nov ±16:00 UTC na Brams laatste run (zie "Versie 3 definitief", dit zijn de bouwgetallen; nieuw: de rij bij de ingang), vastgesteld ±14:50 UTC, daaronder ontwerp versie 2 (versie 1: controleur 16 nov ±13:45 UTC, 11 punten, verwerkt)** (tijden en tellingen klopten; gaten waren te mooi opgeschreven, meetlat-bron, demo-tellers, Gekroonde zonder geluk). Bram rekent na, Olaf zegt do 19 nov wat het kost, Daan en Mila zeggen of het er goed uitziet.

**Aanvulling 16 nov ±21:00 UTC (Sanne): graafbonus.** In de speeltestbuild geeft graven nu (als Olaf het bouwt) +1 goud per val per 8 zelf gegraven cellen, hooguit +3 (`balans.md` bovenaan, sim `data/sim-graafbonus/`). Dat is de kleine vorm van "groter hol, meer goud per val". Voor versie 3 (graven kost goud) moet één regel gelden in spel en sim: Bram kijkt of de v3-runs met goud x (1 + gangen / 40) of met vast 6 per val rekenden, en dan kiezen we die ene vorm voor de demo van 18 dec.

**Antwoord 16 nov ±21:12 UTC (Bram): de v3-runs rekenden met vast 6.** `sim.py lagen` loopt via `lagen_run()`, en die zet `SPEL_ECONOMIE` aan; dan is het goud per val 6 + 3 per eerder bezoek (+1 vanaf de Edelman op hol 10), zonder gangen en zonder faam (`sim.py` regel 376). Het spel doet live hetzelfde (`kern/afloop.gd`: `6 + 3 * bezoeken`). **Eén plek wijkt af:** het goud terwijl je weg bent (`systemen/voortgang.gd` `goud_per_val()`) rekent nog 6 x (1 + 0,1 x faam) x (1 + gangen / 40), en `opslag.gd` geeft daar vast gangen 6 en faam 0 aan, dus weg geeft 7 per val en kijken 6. Wat de drie vormen met versie 3 doen (graven kost goud, 4 lagen, 30 zaden, 100 open uur, `data/sim-v3-goud/`): vast 6: hol 20 / 30 / 40 na 10,5 / 37,2 / 75,7 u, goud totaal 131k. Jouw graafbonus (per laag geteld, want een nieuwe laag begint met 6 gangen): 9,9 / 36,0 / 72,0 u, 197k. 6 x (1 + gangen / 40): 9,3 / 35,2 / 71,1 u, 263k. Hol 12 blijft 1,9 u bij alle drie. Of de graafbonus per laag of over alle lagen telt maakt niets uit (zelfde tijden, 198k): een nieuwe laag is snel weer 24 gangen diep. **Voorstel: jouw graafbonus wordt de ene vorm voor de demo en voor versie 3**, ook in `voortgang.gd` (6 + graafbonus in plaats van de gangen-formule). Reden: de tijden schuiven hooguit ±4 u (5%), de drempels blijven dus geldig, terwijl de gangen-formule het goud verdubbelt zonder plafond en de winkel van versie 3 veel sneller leeg maakt. Je sim van de speeltestbuild klopt: graven is daar gratis, net als in `hol.gd` `klik()`, en de graver in je sim verandert alleen het goud, wat mag omdat graven de vangsten niet verandert (`data/graaf-vangst/`).

**Aanvulling 16 nov ±21:17 UTC (Bram): het nieuwe ritme maakt versie 3 een stuk korter.** De v3-tijden hierboven (hol 50 na ±127 open uur) zijn met het oude ritme gemaakt (35 tot 45 s, daarna 40 tot 60, Gloop 60 s plat). Met het ritme dat sinds 20:50 op main staat (28 tot 38 s, 15% paar, plat 30) komen er 131 in plaats van 77 helden per open uur, en alle drempels tellen helden. Gerekend (30 zaden, 150 open uur, `data/sim-v3-goud/v3ritme.py`, uitkomst `ritme-uitkomst.txt`): oud ritme hol 12 / 20 / 30 / 40 / 50 na 1,9 / 10,5 / 37,2 / 75,7 / 126,9 u; **nieuw ritme 1,1 / 6,0 / 23,3 / 44,6 / 76,1 u**; nieuw met graafbonus 1,1 / 6,0 / 22,1 / 42,7 / 73,3 u. **Voorstel: alle drempels boven hol 12 (en die van Gloop, laagsterren en bewoners) x 1,7**, dan 1,1 / 9,1 / 34,1 / 69,7 / 120,0 u, dus weer het oude verloop. Hol 2 tot 12 heb ik laten staan (Olafs demodrempels); daar komt hol 12 nu na ±1,1 u in deze v3-opzet (jouw speeltestsim: ±58 min), terwijl het demo-einde op 2 uur speeltijd staat. Of dat laatste uur zonder nieuw niveau erg is, is jouw keus. De prijzen heb ik niet aangepast; het goud per uur stijgt ook met 1,7, dus kopen gaat ook sneller.
**Aanvulling 16 nov ±22:00 UTC (Sanne): besluit op Bram 21:17.** (1) Drempels boven hol 12 en die van Gloop, laagsterren en bewoners **x 1,7**: ja (weer hol 50 na ±120 open uur). (2) Weg is veranderd (`balans.md` bovenaan, Iris keuring 9): snelheid weg 0,25 naar **0,12** en faam uit een keer weg **hooguit 2 hol-niveaus**. Bram draait versie 3 nog één keer met die regel en mag de factor zelf bijstellen zodat hol 50 tussen 100 en 130 u landt. (3) **De demo is hol 1 tot 12 en duurt zo lang als dat duurt (±1 tot 1,5 uur), niet 2 uur.** Daarna de grijze kaart. Liever een korter demo met elke paar minuten iets dan een laatste uur zonder nieuw niveau; hogere drempels voor hol 8 tot 12 maakten het gat in uur 1 slechter (balans.md 19:55).
**Aanvulling 16 nov ±22:35 UTC (Bram): met de nieuwe weg wordt het x 1,4, niet x 1,7.** Met weg 0,12 en het plafond van 2 niveaus geeft x 1,7 hol 50 pas na 144 open uur (buiten 100 tot 130). **x 1,4: hol 12 / 20 / 30 / 40 / 50 na 1,1 / 8,6 / 33,6 / 69,1 / 119,5 open uur** (30 zaden, nieuw ritme, graafbonus), dus weer het verloop van 21:17. Nieuwe spec: `producten/steam-hol/sim/voortgang-v3-weg-bram.json` (een nieuw bestand; de oude json lezen elf scripts, ook drie van jou, en die geven zo nog hun eigen uitkomst). Goud van een nacht weg ongeveer gehalveerd (na werkdag 1: 1635 in plaats van 3407). Het plafond raakt na een werkdag van 6 uur nooit (de drempels liggen dan te ver uit elkaar), wel vroeg: 30 min spelen en een nacht weg geeft hol 8 naar 10 in plaats van 8 naar 12. Langste gaten niet slechter dan 21:17. Alles in `platformen/steam/data/sim-v3-weg/LEESMIJ.md`.

## In het kort
1. **Vier sporen naast elkaar, geen enkel spoor alleen.** Zoals elke topper (Fenna: iets kleins elke paar minuten, iets middelgroots elk uur of elke paar uur, en iets groots): **hol-niveau 1 tot 50** (elk niveau iets nieuws dat je ziet), **Gloop 1 tot 10** (op de hoeden die hij at, onze haak), **niveaus van de andere bewoners**, en **laagsterren** (doelen met een hint per laag).
2. **De lange termijn is dieper graven, geen reset.** Op hol-niveau 20, 30 en 40 graaf je een trap naar een nieuwe laag (Kristalader, Verzonken Crypte, Gloophart) met eigen helden, bewoner en val. De nieuwe laag begint leeg, dus je hebt opnieuw de leukste fase (bouwen), maar **er gaat niets weg**: de lagen erboven draaien door en hun goud stroomt mee. Dat is Olafs "opnieuw beginnen met winst" zonder de klacht over rebirth (26 negatieve reviews bij Desktop Defender, Fenna).
3. **Versie 3 definitief (Bram, GEZIEN, 8 zaden):** hol 12 na 2,0 u (einde demo), 20 na 10,5 u, 30 na 37,4 u, 40 na 76,2 u, **50 na 127,8 open uur = werkdag 22 (week 5)**; in week 3 nog 13 niveaus en 50 aankopen. Langste gat per week 1,7 / 1,9 / 2,7 / 2,8 / 6,0 u. Hieronder de oude versie 2-cijfers: hol-niveau 9 na 57 min, 12 na 2,0 u (einde demo), 20 na 10,6 u, 30 na 29,8 u, 40 na 57,7 u, 50 na 95,5 u. Langste gat zonder iets nieuws (niveaus en aankopen samen), run versie 2 met de aankleding erbij: tot 20 uur 56 min, 20 tot 40 uur 1,0 u, 40 tot 70 uur 1,5 u, 70 tot 100 uur nog 5,7 u. Na niveau 50 houdt het op.
4. **Versie 2 in vijf keuzes:** (a) Brams prijzen en drempels over; (b) weg zijn levert alles op halve snelheid, ook faam, plafond 12 uur; (c) 15 niveaus geven iets met een prijs en na laag 2 komt aankleding voor goud in de lege bovenste aarde, zodat goud altijd een doel heeft; (d) twee doelen in beeld: het bordje toont het volgende hol-niveau, de kopregel het volgende goud-doel; (e) een tabel in echte dagen. Details in "Versie 2: keuzes".
5. **Demo = hol-niveau 1 tot 12 in ±2 uur**, bijna helemaal met wat al gebouwd is (ridder, dief, magiër, bard, vleermuis, hoedenwand, vaandel komen nu één voor één in plaats van allemaal tegelijk), plus de twee nieuwe dingen die Olaf noemde (één val, één held). Daarna een grijze kaart: "Level 13 and 37 more in the full game".

## Waarom zo (wat de cijfers zeggen)
- **De helft is weg rond 15 uur, 1 op 6 haalt 100 uur** (meetlat Desktop Defender en Rusty's, GEZIEN via Fenna). Dus het duurste en mooiste (nieuwe helden, bewoners, de eerste nieuwe laag) zit vóór 20 uur, en tot 40 uur komt er minstens elk uur iets (run versie 2: langste gat 1,0 u; Fenna adviseert elk uur).
- **Levels zonder nieuws zijn grind** (Spirit City na level 15). Daarom heeft elk hol-niveau een ding met een naam dat je in de strook ziet, en houdt het op bij 50. Geen niveau 51 tot 999 met alleen een getal.
- **Prestige werkt als eerste stap en wordt gehaat als klus.** Wij doen geen reset. Het "opnieuw beginnen" zit in een lege nieuwe laag, terwijl de oude blijft.
- **Prijs mag niet weglopen van het inkomen** (Ropuka's, Tiny Pasture). Hol-niveau stijgt op gevangen helden, niet op goud. Goud blijft voor graven en upgrades; die prijzen kijkt Bram na met zijn verhouding prijs / goud per uur.

## Eigen helden per laag en hun tegenzet (16 nov ±17:00 UTC, antwoord op Bram 16:45)
Bram rekende uit dat 10% minder vangen in laag 2 tot 4 al ±1 werkdag kost tot hol 50 en de gaten in week 2 tot 4 naar 4 tot 6 uur duwt (`producten/steam-hol/sim/UITKOMST.md`, `sim/voortgang-laagvang-uitkomst.txt`, GEZIEN door mij). Ik neem zijn voorstel over: **elke nieuwe held laat één ding van je oude opstelling falen, en de tegenzet komt op het volgende hol-niveau en vangt hem minstens zo vaak als een gewone held.** Zo is elke nieuwe held een klein raadsel (je bouwt anders) en geen rem op de voortgang.
1. **Volgorde omgedraaid zodat de tegenzet meteen volgt:** hol 22 wordt **the Trapdoor** (was 23) en 23 **the Mimic** (was 22); hol 32 wordt **the Fake Hoard** (was 33) en 33 **the Troll** (was 32). Het gat tussen held en tegenzet is dan ±2,3 u (21 naar 22) en ±4 u (31 naar 32) in plaats van 4,7 en 7 u. De tabel in punt 7 hieronder is aangepast. Olaf had alleen 1 tot 12 in code, dus dit kost niets.
2. **Wat elke held doet, in getallen voor de sim** (zelfde vorm als `SOORT_DATA`: factor op de basiskans per val; gewicht naast de 55 gewone, 15 ridders, 15 dieven, 10 magiërs en 5 barden; alleen in de laag waar hij hoort en dieper):
   | Held (hol) | Laag | Gewicht | Zonder tegenzet | Tegenzet (hol) | Met tegenzet |
   |---|---|---|---|---|---|
   | the Miner (21) | 2+ | 20 | de **eerste val** in zijn bezoek: kans 0 (graaft eromheen, poppetje zakt de grond in en komt erachter weer op); slijm x 1,2 (traag met zijn houweel); rest x 1 | the Trapdoor (22) | graaft om de eerste val heen en **recht het valluik in**: daar kans 0,8 in plaats van 0 |
   | the Explorer (31) | 3+ | 15 | eerste bezoek x 1 (put x 1,2: hij klimt naar beneden om te kijken); **als terugkomer** elke val die hem eerder raakte x 0,3 (stapt eroverheen en tikt tegen zijn hoed) | the Fake Hoard (32) | de nep-schat is geen val, dus hij onthoudt hem niet, en hij **verschuift na elke vangst** naar een andere plek: kans 0,75 tegen hem, 0,5 tegen hebzuchtig, 0,3 tegen schijterig |
   | the Witch (36) | 3+ | 10 | x 1 op alles: haar streek is alleen beeld (Gloops hoeden worden een minuut kikkers die op de berg springen, daarna weer hoeden; tellers lopen gewoon door) | geen nodig | |
   | the Hat Hunter (41) | 4 | 15 | rent langs alles naar de hoedenberg: alle vallen x 0,7; lukt het hem, dan pakt hij toch niets (berg is te hoog) en gaat hij met een wrok | hoedenlokker (41, zelfde niveau, te koop) | een hoed aan een hengel vóór één val: die val x 2 tegen hem (hooguit 0,95) |
   | the Crowned (48) | 4 | eerste keer zeker binnen 1 u, daarna 2 | alle vallen x 0,5; betaalt 25 goud en laat een gouden hoed | geen | zeldzaam, telt niet mee in de balans |
   Kinderen van aartsvijanden (26) volgen de regels van aartsvijanden en zijn verder gewone helden. Trek verdwaald (28) loopt soms de verkeerde trap af en duikt op in een andere laag; geen effect op de vangkans.
3. **Het doel voor de sim:** per laag, met de tegenzet erbij, gemiddelde vangkans **x 1,0 tot 1,05** van de versie 3-getallen (niet hoger: x 1,1 gaf in week 4 een gat van 5,6 tot 6 uur). In het ene hol-niveau tussen held en tegenzet mag het zakken tot ±x 0,95. **Bram mag de getallen in de laatste kolom (0,8 / 0,75 / x 2) bijstellen tot dat klopt; wat de held doet blijft.** Lukt dat niet binnen die band, dan liever de tegenzet sterker dan de drempels 21 tot 50 opnieuw ijken.
4. **Het valluik in de onderste laag** (16 nov ±18:00: alleen de mijnwerker valt erin, zie "Narekening eigen helden" punt 4)**:** een held die in het valluik valt is gevangen (goud, faam en zijn hoed zoals bij elke val). Is er een laag eronder, dan landt hij daar ook nog, boos, als terugkomer met een wrok ("Odo fell two floors. He is not happy."). Zo werkt het valluik in elke laag, ook in de onderste.
5. **Laagsterren die hierbij horen** (spoor 4): laag 2 "Catch a Miner with the trapdoor", laag 3 "Catch an Explorer with the Fake Hoard", laag 4 "Lure the Hat Hunter 10 times". Kroniekregels (hooguit 42 tekens): "Pip dug around the spikes. Into the hole." (39), "Pip remembered every trap. Not this one." (40), "Brom chased a hat on a stick. Again." (35).
6. **Toets:** T2 ja (elke held heeft een grap die je ziet), T3 ja (niets gaat weg, de tegenzet komt meteen en is niet duur: ±1 uur goud), T4 ja.

## Speeltestbuild: de niveaunamen beloven wat er niet is (16 nov ±19:00 UTC, Sanne)
**Gevonden (GEZIEN in de code van main 2f52179):** het bordje, de hover, de doelregel en de kroniekregel noemen bij elk hol-niveau wat erbij komt (`WAT` in `systemen/hol_niveau.gd`: "the Knight", "the Thief", "a second pit", "the Rolling Stone", "the Mage", "the Noble", ...). Maar in de build ontgrendelt een niveau niets:
- ridder, dief, magiër en bard komen na de eerste 10 helden, los van het niveau (`heldensoort.gd` `kies(nr)` in `binnenkomst.gd`). Thijs ziet dus een dief op minuut 8 en daarna "Level 5: the Thief".
- de vleermuis hangt er vanaf het begin (`strook.gd`), een put zetten kan vanaf het begin zo vaak je wilt (`hol.gd`), dus "a bat moves in" en "a second pit" gebeuren niet op dat niveau.
- **the Rolling Stone en the Noble bestaan nog niet.** In een speeltest van een half uur staat er "Next: the Rolling Stone, 5 heroes" en dan komt er niets.
Dat breekt de eerlijk-regel (Thijs: bijzonder, maar eerlijk) en het kost de speeltest punten die we al kennen: vraag 2 ("wat snapte je niet") gaat dan over een steen die nooit komt.

**Besluit: in de speeltestbuild worden de niveaunamen titels van je hol in plaats van ontgrendelingen.** Een titel is altijd waar (faam = gevangen helden, dus je hol wordt echt beruchter), hij geeft het bordje toch een doel ("Next: a hat museum, 4 heroes") en het is een grap per niveau. Alleen tekst, geen nieuwe feature.

| Niveau | Titel (Engels, zoals in het spel) | tekens |
|---|---|---|
| 1 | a damp hole | 11 |
| 2 | a local rumor | 13 |
| 3 | a known hazard | 14 |
| 4 | a bad idea | 10 |
| 5 | a tavern tale | 13 |
| 6 | a hat museum | 12 |
| 7 | a hero shortage | 15 |
| 8 | a no-go zone | 12 |
| 9 | a dare | 6 |
| 10 | a local legend | 14 |
| 11 | a royal problem | 15 |
| 12 | Gloop's Empire | 14 |

Nagemeten: langste hover "Level 11: a royal problem. 12 heroes to go." is 43 tekens (`HOVER_MAX` 43), langste doelregel "Next: a hero shortage, 12 heroes" 32 (`DOEL_MAX` 34), kroniek "Hole level 11: a royal problem." 31. (Nagerekend met een paar regels Python.)

**Voor de demo (na de speeltest):** zodra een niveau echt iets ontgrendelt en het spel dat ook zo doet (soort pas na dat niveau, rolsteen gebouwd), krijgt dat niveau zijn ontgrendeling terug als naam, of beide ("Level 7: the Rolling Stone"). Regel: **het bordje noemt alleen wat op dat niveau echt verschijnt.** Daan kiest de woorden, Olaf bouwt; de optocht na weg (poef met `WAT`) gebruikt dan dezelfde lijst.

## Eerste 20 minuten voor de speeltest van za 21 nov (16 nov ±18:10 UTC)
Thijs speelt 15 tot 30 minuten en zijn eerste vraag is "wanneer verveelde je je". Ik keek dus naar de eerste 20 minuten in Brams sim (versie 3 eind, 16 zaden, script `platformen/steam/data/eerste20-gat.py`, uitkomst `data/eerste20-gat-uitkomst.txt`, GEZIEN). Telt als "iets nieuws": een hol-niveau, een Gloop-niveau of een aankoop. Wat de sim niet telt (wrok, hoed op de toren, kroniekregels) loopt er gewoon doorheen.
- **Nu (drempels 3 / 6 / 10 / 12 / 20 voor hol 2 tot 6):** langste gat tussen minuut 1 en 20 mediaan 5,4 min, **ergste 11,8 min** (zaad 3: na hol 2 op 1,2 min niets nieuws tot 12,9 min). De ridder (hol 3) komt mediaan op 6,5 min, hol 6 op 24,5 min.
- **Voorstel: 3 / 4 / 8 / 12 / 17.** Langste gat mediaan 5,0, **ergste 8,2 min**; de ridder komt mediaan op 2,5 min, direct na de eerste wrok (63 tot 75 s), hol 4 op ±10 min, hol 5 blijft op 14 min, hol 6 (tweede put of slijm te koop) op ±22 min, dus binnen een speeltest van een half uur. **Vanaf hol 7 verandert niets**: hol 12 blijft op 116 min, de tijden 7 tot 11 schuiven hooguit 1 minuut (GEZIEN, 8 zaden tot 2,6 uur).
- Waarom niet nog vroeger: hol 2 op 2 gevangen helden valt in de eerste halve minuut, midden in het hoedengrapje (27 s). Dat moment laat ik alleen.
- Het is alleen een rij getallen in `hol_niveau.gd` (`DREMPEL := [0, 3, 4, 8, 12, 17, 25, ...]`), geen nieuwe feature. Eerlijk: de sim en het spel verschillen bij de eerste aankoop (Olaf mat in het spel 157 tot 227 s); de echte tijden komen uit Olafs log.

## Narekening eigen helden, nep-schat en weg (16 nov ±18:00 UTC, antwoord op Bram 17:20 en 17:35, Iris keuring 5, Daan 17:45)
1. **Eigen helden per laag kloppen** (Bram, GEZIEN in `producten/steam-hol/sim/voortgang-laaghelden-uitkomst.txt`, 8 zaden): laag 2 / 3 / 4 x 1,01 / 1,03 / 1,02, hol 50 blijft werkdag 22. Dit zijn de bouwgetallen: valluik 0,8, nep-schat 0,75 / 0,5 / 0,3, lokker x 2.
2. **Hol 21 op x 0,92 tot 0,94 laat ik zo** (advies Bram). Het is ±2,3 open uur in een vers gekochte laag met twee vallen; daar hoort het raadsel ("waarom vangt mijn put hem niet?"). Het valluik naar hol 21 halen zou het raadsel oplossen voordat je het ziet.
3. **De nep-schat: Brams voorstel is over. Een terugkomende ontdekker loopt recht op de nep-schat af, vóór de vallen.** Waarom: zonder dit hing de ster "Catch an Explorer with the Fake Hoard" van geluk af (in 4 van 8 zaden geen enkele vangst in heel laag 3), en een ster via geluk breekt mijn eigen regel in spoor 4. Het is ook de betere grap: hij kent al je vallen, dus hij gaat voor de schat, en precies die is nep. De kroniekregel past er nu letterlijk op: "Pip remembered every trap. Not this one." Met dit gedrag: ster in 8 van 8 zaden binnen ±1,5 open uur na het kopen, balans gelijk (x 1,03). Zichtbaar maken (voor Olaf, later, na de demo): de ontdekker kijkt even op bij de ingang, dan rent hij in een rechte lijn, over de vallen heen, naar de glinstering.
4. **Brams twee aannames bevestigd:** (a) een tegenzet koop je één keer (±1 uur goud) en hij werkt daarna in elke dieper gelegen laag; (b) **het valluik vangt alleen de mijnwerker.** Het luik zit dicht van boven; het geeft alleen mee als iemand er van onderen tegenaan graaft. Andere helden lopen eroverheen. Zo blijft de balans van laag 2 tot 4 zoals Bram rekende. Punt 4 van "Eigen helden" past zich daarop aan: de mijnwerker die erin valt is gevangen en landt, als er een laag onder is, boos in die laag ("Pip fell two floors. He is not happy."). "Lagen verbinden" bij "Dieper graven" geldt dus alleen voor mijnwerkers.
5. **Wie maar af en toe koopt, haalt het einde even snel** (Bram 17:35, GEZIEN in `sim/voortgang-kijken-uitkomst.txt`): elke 10 min tot elke 2 uur in de winkel kijken geeft hol 50 op werkdag 22, één keer per dag kopen werkdag 23. Het hol-niveau komt van vangen, niet van kopen. Wat groeit is de berg goud (±2.500 tot ±4.400). Dat bevestigt de doelregel en het bordje: wie terugkomt ziet meteen waar dat goud heen kan. Punt 5 van "Wat nog niet klopt" is daarmee beantwoord.
6. **De kroniekregel "Your hole worked at quarter speed." gaat eruit; de regel kwart snelheid blijft.** Iris (keuring 5) en Daan hebben gelijk: de zin leert de speler dat weggaan hem iets kost, en hij duwt de regel van de eerste held weg. Ik zet er **geen grap voor in de plaats**: de telling na terugkomst (goud, hoeden, helden) laat al zien wat er gebeurde, en de regel van de eerste held is de leukste regel van de terugkomst. Eerlijk blijft het zo: het getal in de telling klopt, en op de winkelpagina en in de FAQ staat het gewoon: "Your hole keeps going while you're away, at a gentler pace, for up to 12 hours." (naar Sem). Geen woord als "only" of "quarter", wel de waarheid.

## Wat de laatste twee runs van Bram zeggen (16 nov ±17:00 UTC)
- **De rij bij de ingang werkt zoals bedoeld** (Bram 16:35, GEZIEN in `sim/voortgang-rij-uitkomst.txt`): wie 0 tot 5 minuten speelt en een nacht weg is, ziet hol 5 meteen en hol 12 na ±18 tot 22 open minuten, elk niveau met zijn eigen feestje; in week 1 tot 5 staat er nooit iets in de rij. Mijn "±35 minuten" was te ruim, het is ±27. Iris (keuring 16:40) zegt ja; haar kanttekening neem ik over: **de twee helden uit de optocht komen niet tegelijk binnen**, de tweede pas als de eerste in de gang loopt (naar Olaf).
- **Diep voor weken: ja, voor wie tussendoor speelt** (Bram 16:30, GEZIEN in `sim/voortgang-tussendoor-uitkomst.txt`): elke dag 15 min open, hol 50 op dag 63; 30 min dag 57; 60 min dag 49. Wie werkt met het spel 6 uur open is in ±4,5 werkweek klaar, wie het tussendoor opent na 7 tot 9 weken. Dat is precies het spel dat Thijs op 9 nov vroeg ("leuk om eventjes tussendoor te doen ... niet tijdrovend"): hoe minder je speelt, hoe langer het meegaat, zonder dat je iets mist, want de nachten dragen het. Punt 4 van "Wat nog niet klopt" is daarmee beantwoord; voor de winkelpagina (Sem en Chris) is de eerlijke zin: "Open it for a few minutes a day and your hole grows for weeks."

## Versie 3 definitief (16 nov ±16:00 UTC)
Bram draaide de laatste run (`producten/steam-hol/sim/UITKOMST.md` bovenaan, `sim/voortgang-v3-eind-uitkomst.txt`, 8 zaden, 165 open uur, GEZIEN door mij). Ik neem alles over. **Dit zijn de getallen voor de bouw; de tabellen van versie 2 verderop zijn geschiedenis.**
1. **Wat er ten opzichte van "Versie 3 vastgesteld" verandert (Bram):**
   - **De kamertjes van laag 3 komen vrij zodra laag 3 gebouwd is** (±56 u), niet pas bij het luik naar laag 4. Dan koop je ze verspreid tussen hol 36 en 40 en staat er bij het luik geen berg goud.
   - **Stap 4 tot 6 in laag 3 x 1,85** (was 2,0). Stap 6 in laag 3 kost nu 2.960 in plaats van 3.200.
   - **Drempels hol 36 tot 40:** 11.884 / 13.345 / 14.823 / 15.668 / 17.131 gevangen helden (35 en 41 blijven 10.990 en 18.926).
   - **Kamertje 4 en 5 van laag 4 pas vrij op hol 47 en 49**, prijs uit het goud per uur van dat moment. Geen stap 7.
2. **Wanneer wat komt (open uren, mediaan van 8 zaden):**
   - hol 2: 1 min, 3: 7 min, 4: 13 min, 5: 14 min, 6: 27 min, 7: 34 min, 8: 44 min, 9: 57 min, 10: 1,2 u, 11: 1,6 u, **12: 2,0 u (einde demo)**
   - hol 13 tot 20: 2,8 / 3,5 / 4,4 / 5,4 / 6,5 / 7,6 / 9,1 / **10,5 u**
   - hol 21 tot 30: 12,5 / 14,8 / 17,2 / 19,7 / 22,3 / 25,2 / 28,1 / 31,2 / 34,2 / **37,4 u**
   - hol 31 tot 40: 40,9 / 44,9 / 48,0 / 52,0 / 55,8 / 60,0 / 64,0 / 68,2 / 72,0 / **76,2 u**
   - hol 41 tot 50: 80,4 / 85,1 / 89,9 / 94,8 / 99,8 / 104,9 / 109,9 / 115,6 / 121,4 / **127,8 u**
   - Gloop 2 tot 10: 12 min / 1,1 / 2,4 / 3,8 / 6,0 / 7,0 / 12,0 / 18,7 / 49,0 u
   - laag 2 gekocht 12,7 u, gebouwd 23,0 u; laag 3 gekocht 37,4 u, gebouwd 56,1 u; laag 4 gekocht 76,8 u, gebouwd 100,9 u.
3. **In werkdagen** (6 uur open per werkdag, weg x 0,25, plafond 12 uur): hol 12 en 15 werkdag 1, hol 20 werkdag 2, laag 2 open werkdag 3, hol 30 en laag 3 werkdag 7 (week 2), **hol 40 en laag 4 werkdag 13 (week 3 dag 3), hol 50 werkdag 22 (week 5 dag 2)**. Per week: 42 niveaus en 96 aankopen / 15 en 54 / **13 en 50** / 8 en 18 / 4 en 2 / week 6 niets meer. Een nacht weg geeft ±1.260 goud na dag 1 en ±3.000 na dag 10.
4. **Langste gat zonder iets nieuws (open uren, mediaan / ergste):** week 1 1,7 / 1,9; week 2 1,9 / 3,7; **week 3 2,7 / 2,9 (was 4,2 / 5,1)**; week 4 2,8 / 3,2; week 5 6,0 / 6,0. **Mijn eis van hooguit 2,5 uur is in week 3 net niet gehaald.** Ik accepteer 2,7: wat er over is, is sparen voor de drie duurste dingen van laag 3 (kamertje 5, stap 6, het luik), en het doel staat dan in de kopregel met een balkje dat je ziet vollopen. Dat is geen leeg wachten. Goedkoper maken schuift het gat naar week 4 en maakt het daar 4 tot 6 uur (Bram probeerde het). Week 5 houdt gaten van een werkdag; zie "Versie 3 vastgesteld" punt 4.
5. **Nieuw besluit: de rij bij de ingang (antwoord op Brams extra van 15:50).** Bram rekende uit dat een eerste nacht het hol al na **1 minuut** spelen naar hol 16 tilt (8 van 8 zaden), en in Olafs spel zelfs na 0 minuten (±135 gevangen per nacht, hol 12 is 88). Mijn besluit van 14:50 (alles telt, één optocht) laat dan de hele leerfase in 12 seconden voorbijflitsen: ridder, dief, magiër, bard en edelman komen tegelijk, terwijl elke nieuwe held juist één ding leert ("Weak to: Gloop"). Wie de demo opent, kort speelt en de volgende dag terugkomt, mist zo het beste uur van het spel en staat meteen voor de grijze kaart. Daarom:
   - **Per keer weg komen er hooguit 4 hol-niveaus meteen bij**, in de optocht van 14:50 (bordje wipt één keer, dingen 1,2 s na elkaar, dus nooit meer dan ±5 s; het geval "meer dan 10 dingen, 0,6 s" vervalt).
   - **De rest staat in de rij bij de ingang:** de faam is binnen en blijft binnen (het balkje staat vol, met een getal erbij), maar elk volgend niveau komt pas **na 3 minuten open spelen**, met zijn eigen gewone feestje van 1,5 s. Eigen vangsten tellen gewoon door; haalt je eigen faam de rij in, dan komt het niveau meteen.
   - **Kroniek** na "Grew 4 levels while you were away.": **"7 more levels wait at the door."** (31 tekens, getal past zich aan). Hover op het bordje: "7 levels waiting. Next in 2 min."
   - **Waarom zo en niet minder faam geven:** er gaat niets af van wat je verdiende (Iris: alles korten voelt als diefstal), het is alleen de volgorde. Een terugkomer na 1 minuut spelen heeft na ±35 minuten open de hele demo gezien, met elk feestje apart, in plaats van in 2 uur (wie speelt) of 12 seconden (zonder rij). Boven hol 12 liggen de niveaus 1 uur of meer uit elkaar, dus een nacht geeft daar bijna altijd 4 of minder en merk je de rij niet.
   - **Toets:** T1 ja (je komt terug en er staat iets klaar), T3 ja (niets weg, geen timer die je dwingt: de rij wacht ook als je de app weer dicht doet), T4 ja.
   - Olaf: dit verandert `optocht()` en `weg_regel()` op `claude/steam-hol-weg`, zie `berichten/olaf.md`. Bram: zet de rij in de sim als het kan (hoeveel open minuten tot hol 12 voor wie 1, 5, 15 minuten speelt en dan een nacht weg is).
6. **Doelregel als alles gekocht is (Iris keuring 3, probleem 2): ja, dan het hol-niveau.** Nu wordt de regel leeg na 1048 goud, precies als de speler wil weten wat er komt. Volgorde voor de kopregel: (a) iets klaar om te kopen: "ready: click ..." (blijft eerst); (b) anders het volgende goud-doel zoals nu; (c) **is er niets meer te kopen: "Next: the Thief, 12 heroes"** (naam uit punt 7; past het niet in 34 tekens, dan "Next: level 13, 40 heroes"); (d) staat er iets in de rij: "Level 6 at the door: 2 min". Niveaus zonder naam (een upgrade-stap) tonen het nummer. Waarom het hol-niveau en niet meer winkel: het niveau komt van vangen, dus er is altijd een doel, ook als het goud niets meer kan kopen. Dit komt samen met Mila's bordje (Daans moet van 15:33: geen niveautekst zonder iets in beeld).


7. **Namen in het spel en soort voor de optocht, niveau 13 tot 50** (vervolg op Olafs `WAT` en `SOORT` 1 tot 12 in `hol_niveau.gd`). Engels, zo kort mogelijk zodat "Next: <naam>, 999 heroes" in 34 tekens past (naam hooguit 14 tekens; langer mag in de hover, dan valt de doelregel terug op het nummer). Soort: "held" = nieuwe bezoeker of iets aan de helden, "poef" = iets nieuws in het hol dat gratis komt, "" = komt alleen in de winkel of is niet te zien.
   | Niv. | Naam | Soort | Niv. | Naam | Soort |
   |---|---|---|---|---|---|
   | 13 | tier 4 upgrades | "" | 32 | the Fake Hoard | "" |
   | 14 | the Skeleton | "" | 33 | the Troll | "" |
   | 15 | the Sleepyhead | held | 34 | tier 6 upgrades | "" |
   | 16 | the Bedroom | "" | 35 | hat pack 4 | held |
   | 17 | the Glue Trap | "" | 36 | the Witch | held |
   | 18 | hat pack 2 | held | 37 | the Collector | held |
   | 19 | the Show-off | held | 38 | Candle Room | "" |
   | 20 | Crystal Vein | poef | 39 | Skeleton armor | poef |
   | 21 | the Miner | held | 40 | Gloop Heart | poef |
   | 22 | the Trapdoor | "" | 41 | the Hat Hunter | held |
   | 23 | the Mimic | "" | 42 | Mother Gloop | "" |
   | 24 | the Kitchen | "" | 43 | Gloop Spring | "" |
   | 25 | tier 5 upgrades | "" | 44 | the Bat Tower | "" |
   | 26 | rivals' kids | held | 45 | the Gold Mimic | "" |
   | 27 | hat pack 3 | held | 46 | hat pack 5 | held |
   | 28 | the Lost One | held | 47 | Troll glasses | "" |
   | 29 | Trophy Hall | "" | 48 | the Crowned | held |
   | 30 | Sunken Crypt | poef | 49 | the Hat Throne | "" |
   | 31 | the Explorer | held | 50 | the Hat King | poef |
   (16 nov ±17:00 UTC: 22 en 23 en 32 en 33 omgedraaid, zie "Eigen helden per laag".) Bij 20, 30 en 40 is de "poef" het dichte luik dat in de schatkamer verschijnt (te koop voor 750 / 1650 / 3000); de laag zelf koop je. Bij 41 komt ook de hoedenlokker in de winkel. De archeoloog heet in het spel "the Explorer" (korter, zelfde grap: hij onthoudt elke val).

## Versie 3 vastgesteld (16 nov ±14:50 UTC)
Bram rekende het voorstel hieronder na met weg als echte werkdagen (`producten/steam-hol/sim/UITKOMST.md` bovenaan, `sim/voortgang-v3-uitkomst.txt`, 8 zaden, GEZIEN). Ik neem alles over. Daarmee is versie 3 de richting; de tabellen van versie 2 verderop blijven staan als geschiedenis tot Bram de laatste run (punt 4) heeft gedaan.
1. **Prijzen vanaf laag 2 x 1,5** (Bram, want een werkdag geeft met de nacht erbij 1,5 keer het goud van de open uren): luik **750 / 1650 / 3000**; graven en stap 1 tot 3 per laag x **1 / 2,25 / 5,25 / 8,25**; stap 4 tot 6 per laag x **1 / 1,95 / 2,0 / 2,25**; ding met een prijs per laag **590 / 1410 / 1935 / 2430**; kamertjes 5 per laag, oplopend **1,2 / 1,6 / 2,0 / 2,4 / 2,8 uur goud**. Laag 1 blijft zoals hij was, want op dag 1 is er nog geen nacht geweest. Weg 0,25, plafond 12 uur.
2. **Uitkomst (Bram, GEZIEN):** hol 50 na 127,9 open uur. In werkdagen van 6 uur: hol 12 en 20 in week 1, laag 3 open week 2 dag 2, **laag 4 open week 3 dag 3, hol 50 week 5 dag 2**. Per week 42 / 15 / **13 niveaus en 50 aankopen in week 3** / 8 / 4. Thijs' lat ("een paar weken leuk", in week 3 nog iets nieuws) is gehaald. Elke aankoop in laag 4 kost 0,7 tot 1,9 uur in werkdag-tempo; duurste van het spel is stap 6 in laag 3 (2,1 uur).
3. **Laag 4 krijgt 7 dingen met een prijs** (Brams plekken 41, 42, 43, 44, 45, 47, 49). Wat ze worden:
   - 41: **hoedenlokker** (val: een nep-hoed aan een touwtje; de hoedenjager die op dit niveau gratis binnenkomt, rent er steeds weer in). Zelfde patroon als archeoloog en nep-schat: een nieuwe held en zijn tegenzet.
   - 42: Moeder Gloop (bewoner). 43: gloopbron (val).
   - 44: **vleermuistoren** (kamer: de vleermuisfamilie trekt erin en pikt soms een hoed van de berg om in te hangen). De vleermuisfamilie schuift dus van 46 naar 44 en wordt een kamer.
   - 45: mimic van goud.
   - 47: **leesbril voor de trol** (hij leest af en toe een kroniekregel voor in een wolkje, één woord fout).
   - 49: hoedentroon voor Gloop.
   - Gratis blijven: 41 hoedenjager, **46 hoedenpakket 5** (was 44), 48 de Gekroonde, 50 Hol van de Hoedenkoning.
4. **De twee gaten die Bram vond:**
   - **Hol 38 naar 39 (±4 uur open, vlak voor het luik naar laag 4):** drempels 36 tot 40 gelijkmatiger herijken, zodat geen gat langer is dan 2,5 uur open (±1,7 uur in werkdag-tempo). Hol 40 mag daardoor iets later vallen. Waarom niet iets extra's kopen: er staat op dat moment al genoeg goud op de bank, het ontbreekt aan iets nieuws om te zien, en dat komt van faam.
   - **Het eind (na ±110 uur, week 4 en 5, gaten tot 6 uur):** Brams voorstel over: **kamertje 4 en 5 van laag 4 komen pas vrij op hol 47 en 49**, dan valt er in week 4 en 5 ook nog iets te kopen. **Geen stap 7**: een upgrade die alleen een getal verhoogt is precies de grind die we niet willen (Spirit City na level 15). Een gat van een werkdag op het eind betekent elke dag iets nieuws; voor het einde van een rustig spel vind ik dat eerlijk.
   - Bram draait daarna één run om het te bevestigen; dan zet ik de tabellen om naar versie 3.
5. **Niveaus van terwijl je weg was (antwoord op Olafs vraag van 14:35):** in zijn lokale run tilde één nacht na 90 seconden spelen het hol van 2 naar 12. **Dat mag**: alle faam van weg telt (anders voelt het als diefstal, Iris), en "kijk wat er gebeurde" is precies de beloning van een spel dat je tussendoor opent (T1, T3). Minder geven maakt de demo voor wie terugkomt alleen trager, niet leuker. Maar het nieuwe mag niet allemaal tegelijk in beeld springen, want dan zie je de vleermuis, de dief en de magiër niet binnenkomen. Daarom **één optocht, geen tien feestjes**:
   - na de weg-telling wipt het bordje **één keer**, wat er ook bijkwam;
   - daarna verschijnt elk nieuw ding met de poef van graven, van laag naar hoog niveau, **1,2 s na elkaar, samen hooguit 12 s** (meer dan 10 dingen kan alleen bij hol 1 tot 12: dan 0,6 s). Niveaus zonder iets om te zien (het Heldenboek, een upgrade-stap) slaan over;
   - een nieuwe heldensoort komt niet met een poef maar is de eerstvolgende bezoeker, in volgorde (eerst de ridder, dan de dief);
   - muntjes uit de schat alleen bij het eerste en laatste ding;
   - één kroniekregel na de regel over kwart snelheid: **"Grew 10 levels while you were away."** (35 tekens, het getal past zich aan; bij één niveau gewoon de gewone niveauregel);
   - klikken mag gewoon tijdens de optocht. In de demo staat na hol 12 de grijze kaart "Level 13 and 37 more in the full game".

6. **Kamertjes (Mila 15:10):** past; 12 x 9 spelpixels met een ronde bovenkant, één ding van hooguit 8 x 8 met een eigen silhouet en één grapje, donkere warme achterwand met een lampje, minstens 6 spelpixels aarde ertussen, niet boven een val of de troon. Mila tekent ze in 3D, laag 1 eerst.

## Voorstel versie 3 (16 nov ±14:05 UTC): een paar weken leuk
**De lat van Thijs** (14:53, via de hoofdchat): "dit spel moet wel gewoon een paar weken leuk zijn." Rekenvoorbeeld: elke werkdag ±6 uur open, en in **week 3** nog een nieuw doel en iets nieuws.
**Versie 2 haalt dat niet.** Met weg op halve snelheid telt elke nacht als 6 uur open, een werkweek dus als ±60 uur; dan sta je eind week 1 op hol 40 en is het hol halverwege week 2 af (95 u). Week 3 is leeg.
**Wat ik nu kies (versie 3, richting staat, getallen fijnstellen door Bram):**
1. **Weg = kwart snelheid** (factor 0,25 voor goud, hoeden en faam; plafond 12 uur blijft). Voor de speler: "While you're away, your hole works at a quarter speed." Waarom: (a) een nacht telt dan als 3 uur in plaats van 6, en (b) het lost ook Iris punt 1 op voor de speeltest van za 21 nov: 8 uur weg geeft in de build van nu ±740 goud in plaats van 2952, minder dan de winkel van 1048. Het blijft winst en geen straf (T3). Dit vervangt keuze b hieronder (0,5).
2. **Na hol-niveau 20 komt alles 1,4 keer zo ver uit elkaar**, en de prijzen per laag gaan mee omhoog, zodat het goud niet weer gaat stapelen: graven en stap 1 tot 3 per laag x **1 / 1,5 / 3,5 / 5,5**, stap 4 tot 6 per laag x **1 / 1,3 / 2 / 2,6**, luik **500 / 1100 / 2000**, de dingen met prijs per laag ±450 / 1000 / 1800 / 2800 goud, kamertjes 1,25 keer dat. Alleen 1,4 keer uitrekken zonder hogere prijzen werkt niet: dan staat er bij laag 4 ±19.500 goud op de bank en is laag 4 in nul minuten gebouwd (GEZIEN in een proefrun).
**Uitkomst (GEZIEN, 8 zaden, `data/sim-v2/voortgang-v3-voorstel-uitkomst.txt`; zelfde sim als versie 2 met `REK=1.4`, open tijd):** hol 20 op 10,6 u (gelijk), 30 op 37,5 u, 40 op 75,7 u, **50 op 127,8 u**; Gloop 10 op 66,4 u. Langste gat: 20 tot 40 u 1,6 u, 40 tot 70 u 2,1 u, 70 tot 100 u 2,2 u, 100 tot 130 u 2,8 u (beter dan versie 2 na 70 uur). Bank tot 99 u hooguit ±1.700. Bouwtijd laag 2 / 3 / 4: 7,5 / 14,4 / 17,1 u, dus het bouwen in een nieuwe laag duurt weer lang, en dat is de leukste fase. **Wat nog niet goed is:** de dingen met prijs in laag 4 kosten ±2,8 uur sparen en stap 6 in laag 4 ±3,4 uur; Fenna's regel is ±1 tot 2. Bram stelt dat fijn (lagere prijs per ding, maar dan meer dingen of kamertjes in laag 4).

**Let op: deze werkweek-rij was een GOK van het voorstel en is vervangen door "Versie 3 definitief" punt 3 (Bram, GEZIEN: hol 40 week 3, hol 50 week 5, in week 4 en 5 nog niveaus).** **Werkweek-rij** (Thijs' voorbeeld: elke werkdag 6 uur open, 's nachts en in het weekend dicht; een nacht of weekend weg telt met het plafond als 12 uur x de factor; GOK, de sim koopt alles meteen):
| Moment | Uren (open + weg) | Versie 2 (weg 0,5) | **Versie 3 (weg 0,25)** | Wat er in versie 3 rond dit moment nieuw is | Goud van één nacht weg (versie 3, GOK: 3 x goud per uur van dat moment) |
|---|---|---|---|---|---|
| dag 1 | 6 | hol 16 | hol 16 | ridder tot slaapkamer, Grote Gloop | ±1.200 (laag 1 kost samen ±5.550) |
| dag 3 | 24 tot 30 | hol 25 | hol 25 | laag 2 open en bouwen, mijnwerker, mimic | ±1.800 |
| week 1 | 45 tot 60 | hol 40 | hol 32 | laag 3 (Verzonken Crypte) open, trol | ±2.200 |
| week 2 | 90 tot 120 | **hol 50, af** | hol 43 | laag 4 (Gloophart) open, Moeder Gloop, Gloop 10 | ±3.600 |
| week 3 | 135 | af, niets nieuws | **hol 44 tot 50**: hoedenpakket 5, mimic van goud, vleermuisfamilie, trol met leesbril, de Gekroonde, hoedentroon, Hol van de Hoedenkoning; laag 4 af bouwen | volgende doel staat elke dag in het bordje | ±3.700 |
| week 4 | 180 | af | af | geen nieuw niveau; wel aartsvijanden en hun kinderen, kamertjes die je nog niet kocht, de stempel bij 10.000 hoeden | bank loopt op |
Uren bij versie 2 en 3 verschillen omdat een nacht bij 0,25 als 3 uur telt en bij 0,5 als 6 uur. Wie het spel ook 's nachts laat draaien, is ±1,5 keer zo snel; wie het minder open heeft, langer bezig.
**Toets T1 tot T4:** geen timers, geen plicht, weg levert altijd iets op (T3), niets te koop (T4). Langste gat tot 100 uur 2,2 uur. Eerlijk: wie het spel dag en nacht laat draaien, is na ±5 dagen klaar (128 / 24).
**Wat de anderen nu moeten weten:** Olaf: factor 0,25 in plaats van 0,5 (het bericht van 13:55 is hiermee bijgesteld). Bram: zie "Vragen". De tabellen hieronder (versie 2) laat ik staan tot Bram versie 3 heeft nagerekend; daarna zet ik ze om.

## Versie 2: keuzes (16 nov ±13:55 UTC)

### a. Brams prijzen en drempels: over, met één aanpassing
- **Upgrades stap 4, 5, 6: 600 / 1000 / 1600** (was 988 / 2766 / 7745; liep weg van het inkomen, Fenna patroon 1).
- **Graven en upgrade stap 1 tot 3 kosten per laag x 1 / 1,2 / 2,2 / 3,2** (Bram). **Stap 4 tot 6 per laag x 1 / 1,2 / 1,5 / 1,8** (mijn aanpassing): met Brams factor kost stap 6 in laag 4 ±4 uur sparen; zo wordt dat ±2,3 uur (GOK uit Brams goud per uur: laag 3 stap 6 = 2400 / 1000 per uur = 2,4 u, laag 4 stap 6 = 2880 / 1260 = 2,3 u). Laatste stap van een laag mag iets meer kosten, maar niet vier uur. **Nagerekend (GEZIEN, 8 zaden, `data/sim-v2/`):** stap 6 in laag 4 = 2880 goud bij 1237 per uur = 2,3 u sparen; stap 4 en 5 in laag 3 en 4 tussen 0,9 en 1,5 u.
- **Drempels hol-niveau na 20 hoger** (geijkt door Bram: 30 op ±2.900, 40 op ±8.300, 50 op ±18.600 gevangen helden; in de run van versie 2 opnieuw geijkt op 2.722 / 7.977 / 17.975. De uren in de tabellen zijn Brams run; die van versie 2 wijkt tot 0,3 u af). Alle helden blijven tellen, ook die van oude lagen; het bordje toont gewoon een groter getal. Eerlijk en simpel.
- **Gloops toren telt alleen de hoeden die hij zelf at.** Gloopje (de oppas van een oude laag) legt zijn hoeden op de berg. Gloop 10 komt dan op ±69 u (run versie 2) in plaats van ±31 u.
- **Luik 500 / 750 / 1000 goud** (= ±1 uur goud van dat moment).

### b. Weg zijn: alles op halve snelheid, ook faam (antwoord op Iris punt 2 en Olaf punt 2)
Regel, voor de speler in één zin: **"While you're away, your hole works at half speed."** Als het spel dicht is, levert de tijd weg goud, hoeden en faam op de helft van het tempo van je laatste uur, met het plafond van 12 uur dat er al is. Een laag die je niet ziet maar die wel open staat, geeft de helft van zijn goud en al zijn faam (Gloopje vangt alles, maar steekt de helft van het goud in zijn eigen zak; dat is de grap in de kroniek).
Waarom zo:
- **Wel faam:** 391 gevangen helden zonder faam voelt als diefstal ("waarom telden die niet?"). Iris heeft gelijk dat het een keuze moet zijn.
- **De helft, niet alles:** met alles telt elke nacht als 12 uur spelen, en dan is het hol voor wie elke avond afsluit op dag 8 af in plaats van dag 12 (GOK, avondspeler met 3 uur open per dag). Met de helft blijft de tabel in open tijd dicht bij de waarheid voor iedereen.
- **Geen straf (T3):** weg zijn levert altijd winst op en je mist niets. Het is alleen minder dan kijken, en dat is eerlijk: als je kijkt, koop je ook.
- **Een plafond voor faam** zit er vanzelf in (Olaf: zelfde 12 uur).
- **Bouw (Olaf, klein):** factor 0,5 op goud, hoeden en faam in `systemen/voortgang.gd`; het "weg geweest"-bericht zegt het gewoon: "While you were away: 303 came, 196 fell. +1476 gold, +196 fame (your hole works at half speed)."

### c. Goud heeft altijd een doel (antwoord op Iris punt 1 en Brams open punt)
Iris rekende goed: in de build van nu is de hele winkel 1048 goud en een nacht weg geeft 2952. Dat lossen drie dingen samen op:
1. **Halve snelheid weg** (b): een nacht wordt ±1.500 goud in de build van nu.
2. **Veel meer om voor te sparen, en het groeit mee:** in versie 2 kost laag 1 alleen al samen ±5.550 goud (graven gang 6 tot 39 ±2.260 met Brams prijzen per gang 16 / 49 / 108, upgrades stap 1 tot 3 1.048, vijf dingen met prijs op niveau 6, 7, 14, 16, 17 ±2.250), en daarna gaan stap 4 tot 6 (2 x 3.200) pas open op hol-niveau 13, 25 en 34. Een nacht weg na de eerste avond (hol ±12, ±335 goud per uur, dus ±2.000 goud) koopt een deel van wat open staat, niet alles, en het volgende doel komt van faam, niet van goud. Elke nieuwe laag kost meer (factor per laag), maar in de run meestal 1 tot 2,5 uur sparen (stap 6 in laag 3 werd in de run niet altijd gekocht, dus daar is het een GOK).
3. **15 niveaus geven iets met een prijs van ±1 uur goud** (Brams GOK, ik neem hem over): hol-niveau 6, 7, 14, 16, 17, 22, 23, 24, 29, 32, 33, 38, 42, 43 en 45 (een kamer, val of bewoner; gemarkeerd "te koop" in de tabel hieronder). Het niveau maakt het ding zichtbaar met een grijze kaart en een prijs; kopen doe je zelf wanneer je wilt.
4. **Nieuw: aankleding voor goud in de bovenste aarde** (nagerekend in `data/sim-v2/`: met dit en punt 3 gaat de bank bij 99 uur van ±17.600 naar ±13.700 en het langste gat tussen 40 en 70 uur van 2,3 naar 1,5 uur) (antwoord op Brams gat na 70 uur, en ook op Iris' "de bovenste helft is lege aarde"). Zodra je laag 2 opent, kun je in elke laag (ook laag 1) **5 holkamertjes** uitgraven in de aarde boven de gang en inrichten: bijvoorbeeld in laag 1 een hoedenkast, een schilderij van je eerste aartsvijand, een fontein met slijm; in de Crypte een orgel; in het Gloophart een slijmbad. **20 stuks**, alleen uiterlijk plus een klein grapje (de fontein spuit soms een hoed), prijs ±1 tot 1,5 uur goud van dat moment. Let op: de sim narekende een andere verdeling (de kamertjes aan hol-niveaus gehangen: 0 / 5 / 7 / 8 per laag, die van laag 4 vanaf ±57 u, zie `data/sim-v2/LEESMIJ.md`); Bram zet ze per laag in de sim. Zo vult de strook zich met wat jij kocht, zoals bij Rusty's, en is er tot het einde iets om voor te sparen. Verdiend met goud, nooit te koop voor geld (T4); de DLC-holthema's blijven los (die veranderen het hele hol).
   - **Kost:** 20 kleine tekeningen (Mila en Daan) en een plekje in de aarde per kamer. Kan in delen: de 5 van laag 1 eerst. Past het niet voor maart, dan eerst laag 1 en 2 (10 stuks) en de rest in de gratis update.
   - **Na niveau 50 en alle aankleding** is er niets meer te kopen; dan loopt de bank op. Dat is eerlijk: het hol is af. Je kunt nog helden en aartsvijanden kijken en de stempel bij 10.000 hoeden halen.

### d. Twee doelen in beeld (antwoord op Iris punt 3 en Olafs vraag welk doel voorgaat)
- **Bordje boven de ingang = het volgende hol-niveau** (faam): "Lv 9 · 12 heroes to Lv 10". Dat is het lange doel en komt nooit leeg.
- **Kopregel van het paneel = het volgende goud-doel** (Olafs regel op `claude/steam-hol-doel`): "Next: Big Gloop, 25 gold to go" of goudgeel "Big Gloop ready: click Gloop". Goed zoals het is.
- **Is er maar één plek** (bijvoorbeeld als het paneel dicht is): dan gaat **"ready: click ..." voor** (je kunt nu iets doen), anders het hol-niveau. Reden: een klaarstaande koop is een kleine beloning in een bezoek van 30 seconden (T1), en anders is het niveau het doel dat nooit opraakt.
- **Voor de speeltest van za 21 nov** (bouwvolgorde is aan Olaf; dit is mijn wens): (1) Olafs doelregel op main; (2) weg op halve snelheid (paar regels); (3) als het past: hol-niveau 1 tot 12 met het bordje, waarbij alleen dingen vrijkomen die al gebouwd zijn (ridder, dief, magiër, bard, vleermuis, vaandel, hoedenwand). Punt 3 is het meeste waard voor de test, want Thijs vroeg zelf om level ups, en een tester van een uur ziet dan 9 niveaus. Maar het mag de doelregel en de rest van de build niet in gevaar brengen.

### e. Echte dagen
Staat bij de tabel per uur hieronder.

## Spoor 1: hol-niveau (1 tot 50)
**Waarop:** faam = gevangen helden (1 per held), plus een klein beetje voor verhalen: +5 voor een nieuwe bladzijde in het Heldenboek, +25 voor een afgerekende aartsvijand (zit nog niet in de sim, maakt het hooguit iets sneller). Faam gaat nooit omlaag (T3). Helden die je in een oude laag vangt, tellen mee.
**Wat je ziet:** boven de ingang een klein bordje met het niveau en daaronder een balkje van 1 spelpixel hoog. Bij hover: "Level 5: the Thief. 12 more heroes." Het volgende doel staat dus altijd in beeld, zonder venster.
**Het feestje (klein, standaard zonder geluid):** het bordje wipt, een handvol muntjes springt uit de schat, het nieuwe ding verschijnt met een poef (zelfde soort als bij graven), en één regel in de kroniek ("Hole level 4: a bat moves in."). 1,5 seconde, binnen de strook, niets knippert buiten de strook. Uiterlijk: Mila, keuring Daan.

Kolom "Sim" is versie 2; de uren van versie 3 staan in "Versie 3 definitief" punt 2.

| Niv. | Wat er bijkomt | Laag | Nu al gebouwd? | Sim (mediaan) |
|---|---|---|---|---|
| 1 | gewone held, Gloop, stekelput, graven, de winkel | 1 | ja | 0 |
| 2 | Heldenboek open, met grijze vakjes ("2 of 11 heroes") | 1 | deels (boek: ontwerp in features.md) | 1 min |
| 3 | ridder komt | 1 | ja | 7 min |
| 4 | vleermuis komt wonen | 1 | ja | 13 min |
| 5 | dief komt | 1 | ja | 14 min |
| 6 | tweede put of tweede slijm te koop *(te koop, ±1 u goud)* | 1 | deels | 27 min |
| 7 | **rolsteen** (nieuwe val, demo) *(te koop, ±1 u goud)* | 1 | nee | 34 min |
| 8 | magiër komt | 1 | ja | 44 min |
| 9 | vaandel met de naam van je hol | 1 | ja | 57 min |
| 10 | **edelman** (nieuwe held, demo): hoge hoed, betaalt 2 goud extra, de zeldzaamste hoed van de demo | 1 | nee | 1,2 u |
| 11 | bard komt (het lied) | 1 | ja | 1,6 u |
| 12 | hoedenwand in de schatkamer | 1 | ja | 2,0 u |
| 13 | upgrades stap 4 (elke lijn gaat naar 6) | 1 | nee | 2,8 u |
| 14 | skelet (bewoner) *(te koop, ±1 u goud)* | 1 | nee | 3,5 u |
| 15 | trek slaapkop (doet een dutje in je hol) | 1 | nee | 4,4 u |
| 16 | slaapkamer (bewoners sneller op) *(te koop, ±1 u goud)* | 1 | nee | 5,4 u |
| 17 | lijmplaat (val, goed tegen de dief) *(te koop, ±1 u goud)* | 1 | nee | 6,5 u |
| 18 | hoedenpakket 2 (helden dragen 8 nieuwe hoeden) | 1 | pijplijn | 7,6 u |
| 19 | trek opschepper | 1 | nee | 9,0 u |
| 20 | **trap naar laag 2: de Kristalader** | 2 | nee | 10,6 u |
| 21 | mijnwerker (held laag 2: graaft om je eerste val heen) | 2 | nee | 12,0 u |
| 22 | valluik: een held valt erin, en naar de laag eronder als die er is; de tegenzet voor de mijnwerker *(te koop, ±1 u goud; was 23)* | 2 | nee | 13,6 u |
| 23 | mimic (bewoner: speelt schatkist) *(te koop, ±1 u goud; was 22)* | 2 | nee | 15,3 u |
| 24 | keuken (slijm groeit van laarzen) *(te koop, ±1 u goud)* | 2 | nee | 17,1 u |
| 25 | upgrades stap 5 | 2 | nee | 19,0 u |
| 26 | kinderen van aartsvijanden komen ("wants his father's hat back") | 2 | nee | 21,0 u |
| 27 | hoedenpakket 3 (kristal) | 2 | pijplijn | 23,1 u |
| 28 | trek verdwaald (loopt de verkeerde trap af) | 2 | nee | 25,2 u |
| 29 | trofeeënzaal (aartsvijanden aan de wand) *(te koop, ±1 u goud)* | 2 | deels | 27,5 u |
| 30 | **trap naar laag 3: de Verzonken Crypte** | 3 | nee | 29,8 u |
| 31 | archeoloog (onthoudt elke val die hij zag) | 3 | nee | 32,2 u |
| 32 | nep-schat (val, de tegenzet voor de archeoloog, verschuift na elke vangst) *(te koop, ±1 u goud; was 33)* | 3 | nee | 34,9 u |
| 33 | trol (bewoner: wordt alleen wakker voor aartsvijanden) *(te koop, ±1 u goud; was 32)* | 3 | nee | 37,4 u |
| 34 | upgrades stap 6 (laatste) | 3 | nee | 40,1 u |
| 35 | hoedenpakket 4 (crypte) | 3 | pijplijn | 42,9 u |
| 36 | heks (betovert Gloops hoeden een minuut tot kikkers, daarna weer hoeden) | 3 | nee | 45,9 u |
| 37 | trek verzamelaar (komt voor één bepaalde hoed op de berg) | 3 | nee | 48,7 u |
| 38 | kaarsenkamer (crypte) *(te koop, ±1 u goud)* | 3 | nee | 51,7 u |
| 39 | skelet in harnas (verdiend uiterlijk, niet te koop) | 3 | nee | 54,8 u |
| 40 | **trap naar laag 4: het Gloophart** (waar slijm vandaan komt) | 4 | nee | 57,7 u |
| 41 | hoedenjager (wil een hoed van de berg terug, lukt nooit, krijgt een wrok), plus hoedenlokker *(te koop, versie 3)* | 4 | nee | 60,9 u |
| 42 | Moeder Gloop (bewoner) *(te koop, ±1 u goud)* | 4 | nee | 64,2 u |
| 43 | gloopbron (val: een gevangen held wordt even een slijmpje) *(te koop, ±1 u goud)* | 4 | nee | 67,7 u |
| 44 | vleermuistoren (kamer, de vleermuisfamilie trekt erin) *(te koop, versie 3)* | 4 | deels | 71,2 u |
| 45 | mimic van goud *(te koop, ±1 u goud)* | 4 | nee | 74,9 u |
| 46 | hoedenpakket 5 (legendarisch: hoeden van je oude aartsvijanden als goud) | 4 | pijplijn | 78,6 u |
| 47 | trol met leesbril (leest de kroniek voor) *(te koop, versie 3)* | 4 | nee | 82,3 u |
| 48 | zeldzame held: de Gekroonde (komt zeker binnen ±1 uur na dit niveau en daarna af en toe; geen kans-spul) | 4 | nee | 86,5 u |
| 49 | hoedentroon voor Gloop *(te koop, versie 3)* | 4 | nee | 90,7 u |
| 50 | Hol van de Hoedenkoning: gouden vaandel, titel, prestatie | 4 | nee | 95,5 u |

Samen: 11 heldensoorten (5 nu plus edelman, mijnwerker, archeoloog, heks, hoedenjager, en de Gekroonde als zeldzame), 6 vallen (stekelput, rolsteen, lijmplaat, valluik, nep-schat, gloopbron), 5 bewoners (Gloop, skelet, mimic, trol, Moeder Gloop; de vleermuis is aankleding, geen bewoner die vecht), 4 lagen, ±40 hoeden in 5 pakketten. Dat is ongeveer de omvang die Olaf al rekende (±10 helden, ±6 vallen, ±40 hoeden, ±3 diepten).

## Spoor 2: Gloop (1 tot 10), op de hoeden die hij at
Dit is onze haak, dus Gloop krijgt het rijkste spoor. Hij stijgt op de hoeden op zijn toren (bron `hoeden_gloop`), en de drempels sluiten aan op de maten van de hoedenberg (`BERG_MAAT`).
| Niv. | Hoeden | Wat je ziet | Sim |
|---|---|---|---|
| 2 | 5 | wiebeltoren: de hoeden wiebelen als hij beweegt | 12 min |
| 3 | 25 | boer: spuugt soms een hoed op de berg | 1,1 u |
| 4 | 60 | kleverig: een held plakt even (iets meer vangen) | 2,4 u |
| 5 | 100 | Grote Gloop, toren van 5 hoeden | 3,8 u |
| 6 | 200 | hoedendans: jongleert met een hoed als het stil is | 6,9 u |
| 7 | 300 | Gloopje splitst af (kleine tweede slijm, wordt de oppas van een oude laag) | 9,0 u |
| 8 | 600 | hoedenworp: gooit een hoed van de berg naar een vluchter | 16,1 u |
| 9 | 1000 | Gloop the Hatted, kroon op de berg | 25,5 u |
| 10 | 3000 | Gloop de Hoedenkoning, gouden slijm | 68,8 u |
Verlies je een gevecht, dan blijft alles staan (plat, "Back in a minute", T3). Gloop verhuist mee naar elke nieuwe laag, met zijn toren en berg; Gloopje past op de laag die je verlaat.

## Spoor 3: de andere bewoners (elk 3 niveaus)
Ze stijgen op hun eigen teller (skelet: helden die hij bang maakte; mimic: helden die hem probeerden te openen; trol: aartsvijanden; Moeder Gloop: slijmpjes die ze opvoedde). Elk niveau een nieuwe streek, klein getekend (een animatie, geen nieuw figuur).
| Bewoner | Niv. 2 | Niv. 3 | Niv. 4 | Sim (GOK: drempel op gevangen helden) |
|---|---|---|---|---|
| skelet | rammelt helden bang | gooit zijn hoofd | draagt een hoed van de berg | 8 / 18,6 / 41,7 u |
| mimic | likt zijn lippen | legt een valse munt neer | twee rijen tanden | 16,8 / 26,5 / 49,6 u |
| trol | bromt in zijn slaap | gooit een rots | schrijft wrokken op | 36,7 / 46,9 / 61,7 u |
| Moeder Gloop | zingt slijmliedjes | breit hoeden voor de berg | adopteert gevluchte helden | 65,3 / 79,1 / 92,1 u |

## Spoor 4: laagsterren (3 per laag, 12 samen)
Per laag drie doelen met een hint in het Heldenboek, bijvoorbeeld "Catch a Miner with the trapdoor" of "Let the Troll settle a grudge". Het zijn kleine puzzels: welke val of bewoner zet je waar. Alles is te halen met wat je hebt, niets via geluk, niets verloopt. Een volle laag (3 sterren) krijgt een gouden rand op zijn trap.

## Dieper graven: hoe een nieuwe laag werkt
- **Openen:** op hol-niveau 20, 30 en 40 verschijnt in de schatkamer een luik. Het luik kost 500, 750 en 1000 goud (±1 uur goud van dat moment, Bram GEZIEN). Graven en upgrades in de nieuwe laag kosten meer per laag (zie Versie 2, a). Je kiest zelf wanneer; wachten kost niets.
- **De strook toont één laag tegelijk.** Een klein trapje links in de strook wisselt van laag (één klik, gratis, altijd terug).
- **De nieuwe laag begint leeg:** ingang, Gloop en een kale gang. Je graaft en richt opnieuw in. Dat is de winst van "opnieuw beginnen": de leukste uren komen terug, met nieuwe helden die alleen hier komen.
- **De oude laag draait door,** met Gloopje als oppas. Om zuinig te blijven rekent het spel een laag die je niet ziet niet held voor held door, maar geeft het de faam van het laatste uur dat je er keek en **de helft van het goud** (zelfde aanpak als het "weg geweest"-bericht, `voortgang.gd`). Gloopjes hoeden gaan naar de berg, niet naar Gloops toren. Bouwtijd per laag (run versie 2, GEZIEN, `data/sim-v2/voortgang-v2-uitkomst.txt`): laag 1 8,2 u, laag 2 6,4 u, laag 3 8,3 u, laag 4 10,2 u. Zo is elke laag weer 6 tot 10 uur bouwen, in plaats van steeds korter (met al het goud werd laag 4 één uur, Bram). Is het spel dicht, dan krijgt een laag die je niet ziet de helft van de weg-snelheid (dus 0,5 x de weg-factor).
- **Lagen verbinden:** het valluik (niveau 22, alleen voor mijnwerkers) laat een mijnwerker uit een laag in de laag eronder vallen. De kroniek vertelt het ("Odo fell two floors. He is not happy.").
- **DLC blijft los** (T4): holthema's zijn uiterlijk voor elke laag; een DLC voegt nooit een laag toe die je voor het hol-niveau nodig hebt. Het basisspel is 100% vol te krijgen.

## Tabel per uur (open tijd), met de meetlat van Fenna en echte dagen
**Let op: deze tabel is versie 2 (geschiedenis).** De bouwgetallen staan in "Versie 3 definitief" punt 2 en 3; wat er per niveau bijkomt in spoor 1 en "Versie 3 vastgesteld" punt 3 blijft gelden, alleen de uren in de kolom "Sim" zijn verschoven.
Percentage = hoeveel spelers dit punt halen bij Desktop Defender (GEZIEN bij 1, 5, 10, 20, 50 en 100 uur; Rusty's loopt bijna gelijk bij 1, 24 en 48 uur). 2, 40 en 70 uur zijn tussengerekend (GOK). Of Hats net zo afhaakt is een GOK. Let op: Fenna's percentages zijn Steam-speeltijd, en die telt ook als het spel open staat terwijl je werkt. "Open tijd" hier is dus hetzelfde als Steam-speeltijd.
Tijden uit Brams sim met lagen en geijkte drempels (GEZIEN, `producten/steam-hol/sim/voortgang-lagen-uitkomst.txt`).
| Uur | Spelers | Wat je dan hebt (sim) | Wat is nieuw rond dit uur | Het volgende doel dat je ziet |
|---|---|---|---|---|
| 1 | 83% | hol 9, Gloop 2 (3 op 1,1 u), 4 heldensoorten, rolsteen, vleermuis, tweede put of slijm | vaandel met je holnaam, ridder, dief, magiër | bordje "Level 10: the Noble" (±15 min); kopregel het goedkoopste goud-doel |
| 2 | ±78% | hol 12, Gloop 3, 6 van 11 heldensoorten | bard, hoedenwand, edelman | grijze kaart "Level 13: upgrades tier 4" (2,8 u) en Gloop 4 (2,4 u); in de demo "and 37 more in the full game" |
| 5 | 66% | hol 15, Gloop 5 (Grote Gloop), skelet | slaapkop | slaapkamer (5,4 u), eerste laagster, hoedendans (6,9 u) |
| 10 | 57% | hol 19, Gloop 7 (Gloopje), 3 laagsterren | Gloopje, laag 1 bijna af | **trap naar de Kristalader op niveau 20 (10,6 u)**, luik 500 goud |
| 20 | 46% | hol 25, Gloop 8, laag 2 bijna af (20,4 u) | upgrades stap 5, eerste aankleding te koop | kinderen van aartsvijanden (21 u), Gloops kroon (25,5 u) |
| 40 | ±30 tot 35% | hol 33 (34 op 40,1 u), laag 3 af (38,5 u), trol, 7 laagsterren | nep-schat, laatste upgradestap | heks (45,9 u), trap naar het Gloophart op niveau 40 (57,7 u) |
| 70 | ±24% | hol 43, laag 4 bijna af (68,6 u), Moeder Gloop, Gloop 10 (68,8 u) | hoedenpakket 5 (71 u) | mimic van goud (75 u), aankleding van het Gloophart, de Gekroonde (86,5 u) |
| 100 | 17% | hol 50 (95,5 u), alle sporen af | Hol van de Hoedenkoning | geen nieuw niveau meer; wel aartsvijanden en hun kinderen, en de stempel bij 10.000 hoeden (GOK ±200 u) |

**Geschiedenis, versie 2 (weg 0,5).** Voor versie 3 geldt "Versie 3 definitief" punt 3. **In echte dagen** (GOK, zelf gerekend met de regel "weg = halve snelheid, plafond 12 uur", zie "Weg zijn"; een nacht dicht telt dan als 6 uur open). Dag waarop je het punt haalt:
| Punt (open uren) | Kantoor: spel 8 u per dag open | Avond: 3 u per dag open | Even kijken: 30 min per dag open | Spel en pc altijd aan |
|---|---|---|---|---|
| hol 9 (1 u) | dag 1 | dag 1 | dag 2 | dag 1 |
| hol 15 (5 u) | dag 1 | dag 2 | dag 2 | dag 1 |
| trap naar laag 2 (10,6 u) | dag 2 | dag 2 | dag 3 | dag 1 |
| hol 25 (19 u) | dag 2 | dag 3 | dag 4 | dag 1 |
| trap naar laag 3 (29,8 u) | dag 3 | dag 4 | dag 6 | dag 2 |
| trap naar laag 4 (57,7 u) | dag 5 | dag 8 | dag 10 | dag 3 |
| hol 50 (95,5 u) | dag 8 | dag 12 | dag 16 | dag 4 |
Kanttekening: de sim koopt alles meteen. Wie het spel open laat zonder te klikken koopt niets, dus vangt niet meer en gaat langzamer; en een nacht dicht is waarschijnlijk iets minder waard dan 6 uur open, omdat er dan niets gekocht wordt. De echte dagen liggen dus eerder later dan deze tabel. Eerlijk: voor iemand die het spel dag en nacht laat draaien en vaak klikt, is het hol in ±4 dagen af. Zie "Wat nog niet klopt" punt 4.

## De demo: de eerste 2 uur uitgewerkt
Doel (Fenna): 4 tot 6 kleine feestjes in het eerste half uur tot uur, en na 2 uur zien dat het diep is (Olaf: dichte plekken laten zien). De eerste tien minuten blijven zoals in `features.md` (eerste val ±5 s, vlucht en terugkomer, eerste hoed op Gloop, Hoard-Toucher); de niveaus komen ertussen.
| Tijd (sim) | Wat er gebeurt | Feestje? |
|---|---|---|
| 0 tot 10 min | script van `features.md`; hol-niveau 2 (1 min): Heldenboek met grijze vakjes; ridder (7 min); eerste aankoop | ja: 2 kleine |
| 12 min | Gloop 2: wiebeltoren | klein |
| 13 min | vleermuis komt wonen (hol 4) | ja |
| 14 min | dief (hol 5); het boek laat zien "Weak to: Gloop" na zijn eerste vangst | ja |
| 27 min | tweede put of slijm te koop (hol 6): nu kies je waar | ja |
| 34 min | rolsteen (hol 7), goed tegen de ridder | ja |
| 44 min | magiër (hol 8) | ja |
| 57 min | vaandel met de naam van je hol (hol 9) | ja |
| 1,1 u | Gloop 3: spuugt een hoed op de berg | klein |
| 1,2 u | edelman (hol 10); zijn hoge hoed is het pronkstuk op de toren | ja |
| 1,6 u | bard en zijn lied (hol 11) | ja |
| 2,0 u | hoedenwand (hol 12); daarna staat de grijze kaart in het bordje | ja |
| 2,4 u en 3,8 u | Gloop 4 (kleverig) en Grote Gloop (Gloop 5); in de demo kan Gloop wel door, het hol-niveau niet | |
**Wat de demo laat zien zonder het te tekenen:** in het Heldenboek de lege vakjes ("6 of 11 heroes", "10 of 40 hats", "1 of 4 floors"), in de winkel grijze stappen 4 tot 6 met "Level 13", "Level 25" en "Level 34", in de schatkamer een dicht luik met "Level 20". Zo ziet een speler de omvang (Olaf). De demo houdt niet op: helden blijven komen, Gloop groeit door, alleen het hol-niveau stopt bij 12.
**Save mee naar het volle spel:** wie de demo speelde, begint in het volle spel op zijn eigen niveau. Vraag aan Olaf of dat kan met een demo als eigen app-ID (zelfde map voor de save?).
**Let op "armoedig":** dingen later laten komen mag het begin niet kaal maken (Thijs vond het eerste plaatje armoedig). Voorstel: de vaste aankleding van "een vol hol" (spinrag, stutten, wortels, Daans regels) staat er vanaf de eerste seconde; alleen wat leeft of een naam heeft (vleermuis, hoedenwand, vaandel) komt met een niveau. **Besluit Mila (16 nov):** zo doen; stutten, fakkels, plantjes en de hoedenwand als wand staan er vanaf seconde 1, alleen wat leeft of een naam heeft komt met een niveau (Daan mag bijsturen op leesbaarheid).

## Prestaties (meetinstrument, kost bijna niets)
Zes prestaties voor open tijd (1, 5, 10, 20, 50, 100 uur), net als Desktop Defender, zodat we na de lancering zien waar spelers afhaken (advies Fenna). Daarbij: hol-niveau 10, 20, 30, 40, 50; elke laag geopend; Gloop 5 en 10; alle laagsterren. Geen prestatie voor iets dat via geluk loopt.

## Toets T1 tot T4
- **T1 tussendoor:** het volgende doel staat altijd in het bordje; elk bezoek zie je hoe ver het balkje is. Ja.
- **T2 grappig om te onderhouden:** de nieuwe dingen zijn figuren met een grap (heks met kikkers, trol met leesbril, hoedenjager die het nooit lukt). Ja.
- **T3 nooit straf, geen grindmuur, geen plicht:** faam gaat nooit omlaag, geen reset, oude lagen draaien door, geen timers. Bijna: zie het gat na 70 uur hieronder.
- **T4 niets te koop:** alle 50 niveaus, lagen en verdiende uiterlijken zitten in het basisspel; DLC is alleen uiterlijk en eigen hoofdstukken.

## Wat nog niet klopt (eerlijk)
**Stand versie 3 definitief (16 nov ±16:20 UTC):** punt 1 (gaten) en 4 (in ±4 dagen af) hieronder gaan over versie 2. Nu: langste gat per week 1,7 / 1,9 / 2,7 / 2,8 / 6,0 open uur; hol 50 op werkdag 22 bij 6 uur open per werkdag, en voor wie het spel dag en nacht laat draaien op ±128 / 24 = ±5,3 dagen. Nog open: (a) week 5 heeft gaten van een werkdag (bewust, geen grind); (b) de rij bij de ingang zit nog niet in de sim (gevraagd aan Bram); (c) eigen helden per laag zitten nog niet in de sim (punt 2); (d) kosten: Olaf rekent opnieuw in runs (punt 3). **Stand 16 nov ±17:00 UTC:** (b) is gedaan en klopt; (c) ontworpen met tegenzet per held (zie "Eigen helden per laag"), Bram rekent na; punt 4 beantwoord: tussendoor spelen geeft 7 tot 9 weken. **Stand 16 nov ±18:00 UTC:** (c) nagerekend en klopt (x 1,01 / 1,03 / 1,02); punt 5 beantwoord: af en toe kopen kost hooguit één werkdag.
1. **Gaten.** Versie 2 nagerekend met Brams sim plus mijn 15 dingen met prijs, 20 kamertjes en lagere factor voor stap 4 tot 6 (GEZIEN, 8 zaden, `data/sim-v2/voortgang-v2-uitkomst.txt`): langste gat tot 20 uur 56 min, 20 tot 40 uur 1,0 u (was 1,6), 40 tot 70 uur 1,5 u (was 2,3), **70 tot 100 uur nog steeds 5,7 u**; bank bij 99 uur ±13.700 (was ±17.600). Hol-niveaus vallen op dezelfde uren (50 op 95,3 u). Mijn regel (tot 20 uur hooguit 2 uur, 20 tot 70 hooguit 3, daarna hooguit 4) is dus gehaald tot 70 uur, **na 70 uur niet** (5,7 u, regel hooguit 4). Waar het gat zit is niet uitgesplitst; na niveau 50 kan het niet helemaal zijn (100 min 95,3 is 4,7 u), dus het zit ook eerder (Bram splitst uit). Wil Thijs dat er ook na 95 uur iets te kopen is, dan moet er een goudput komen die niet opraakt; dat doe ik bewust niet (een eindeloze put zonder nieuws is precies Fenna patroon 2). Wat de sim niet telt vult de gaten nog deels: aartsvijanden (±1 per dag), hun kinderen, bladzijden in het boek, laagsterren.
2. **De sim kent de eigen helden per laag nog niet** (mijnwerker, archeoloog, valluik); elke laag heeft daar dezelfde helden en vallen als laag 1. De sporen 3 en 4 staan als drempel op gevangen helden (GOK).
3. **Kost.** Meer beeld dan Olafs eerste rekensom: 12 bewonersstreken, 4 lagen en nu ook 20 kamertjes aankleding. Olaf rekent do 19 nov opnieuw. Past het niet voor maart: **lancering met laag 1 tot 3 (hol 1 tot 39, ±55 uur, "50+ hours" op de winkelpagina) en laag 4 plus de aankleding van laag 3 en 4 als gratis update in april**; op niveau 39 staat dan eerlijk "Floor 4 comes in a free update".
4. **Voor wie het spel dag en nacht laat draaien is het hol in ±4 dagen af** (tabel echte dagen). Dat is hoe dit soort spel werkt (Fenna's meetlat is Steam-speeltijd, ook als je werkt), en het is twee keer de hoofdinhoud van de toppers (±20 tot 50 uur). Toch is "diep" voor Thijs misschien weken. Hoger zetten kan alleen met hogere drempels, en dan wordt het tussen de niveaus grind (Fenna patroon 2). Ik laat het zo en kijk na de speeltest van za 21 nov wat Thijs ervan vindt.
5. **Echte dagen zijn een GOK.** De sim koopt alles meteen; een echte speler klikt minder, dus het gaat eerder langzamer. (Beantwoord 16 nov ±18:00 UTC: Bram rekende het na, hooguit één werkdag later; zie "Narekening eigen helden" punt 5.)

## Vragen aan de anderen (ook in hun berichtenbestand)
- **Bram (versie 3):** reken het voorstel versie 3 na en stel het fijn (weg 0,25 in de sim, uitrekken 1,4 na niveau 20, prijsfactoren per laag, en de dingen in laag 4 terug naar ±1 tot 2 uur sparen met meer dingen of kamertjes), zodat ik de tabellen kan omzetten. Mijn proefrun en het aangepaste script staan in `data/sim-v2/` (`REK` en `UREN` erbij).
- **Bram (versie 2):** ik heb versie 2 zelf in een kopie van je sim gedraaid (`data/sim-v2/`, je bestanden zijn niet veranderd). Wil je (1) `laag_factor_hoog` en kamertjes per laag (in plaats van aan een hol-niveau) echt in `sim.py` zetten, (2) weg zijn op halve snelheid in de sim zetten, zodat de tabel in echte dagen geen GOK meer is, en (3) uitsplitsen waar het gat van 5,7 uur tussen 70 en 100 uur zit?
- **Olaf:** (1) weg op **kwart snelheid** voor goud, hoeden en faam in `voortgang.gd` (factor 0,25, plafond 12 uur blijft; was 0,5 in versie 2); (2) je doelregel is goed, "ready" gaat voor als er maar één plek is; (3) hol-niveau 1 tot 12 met bordje vóór za 21 nov als het past; (4) kosten van alles hierboven do 19 nov, nu met 20 kamertjes; (5) kan de demo-save mee naar het volle spel?
- **Mila en Daan:** het bordje met balkje boven de ingang, het feestje van 1,5 s, welke aankleding er vanaf seconde 1 staat, en de kamertjes in de bovenste aarde (past dat bij "de bovenste helft is lege aarde" van Iris?).
