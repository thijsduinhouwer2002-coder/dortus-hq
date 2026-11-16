# Hats of the Fallen: voortgang voor ±100 uur (Sanne, game-ontwerper)

Versie 2, 16 nov 2026 ±13:55 UTC (versie 1 ±13:30). Versie 2 verwerkt Brams narekening met lagen (`producten/steam-hol/sim/LAGEN.md`), Iris' keuring 1 (`keuring/2026-11-16-13.md`) en Olafs bouwfeiten van 13:38. Opdracht hoofdchat 16 nov 13:10 (Thijs 13:01: "een diepgaand spel ... level ups enzo om een reden te hebben om te spelen"). Eerste versie gevraagd wo 18 nov 12:00.
Bronnen: Fenna `platformen/succes/diepte-toppers.md` (prestatie-percentages, GEZIEN), Olaf `planning-fest-2027.md` ("Diep spel met level ups"), Brams sim `producten/steam-hol/sim/sim.py voortgang`. Nagerekend met die sim: `platformen/steam/data/voortgang-maak.py` maakt `data/voortgang.json`, uitkomst in `data/voortgang-uitkomst.txt` (versie 1, GEZIEN, 8 zaden); versie 2 en het voorstel voor versie 3 in `data/sim-v2/` (GEZIEN, 8 zaden).
Status: **versie 3 vastgesteld 16 nov ±14:50 UTC (zie "Versie 3 vastgesteld"), daaronder ontwerp versie 2 (versie 1: controleur 16 nov ±13:45 UTC, 11 punten, verwerkt)** (tijden en tellingen klopten; gaten waren te mooi opgeschreven, meetlat-bron, demo-tellers, Gekroonde zonder geluk). Bram rekent na, Olaf zegt do 19 nov wat het kost, Daan en Mila zeggen of het er goed uitziet.

## In het kort
1. **Vier sporen naast elkaar, geen enkel spoor alleen.** Zoals elke topper (Fenna: iets kleins elke paar minuten, iets middelgroots elk uur of elke paar uur, en iets groots): **hol-niveau 1 tot 50** (elk niveau iets nieuws dat je ziet), **Gloop 1 tot 10** (op de hoeden die hij at, onze haak), **niveaus van de andere bewoners**, en **laagsterren** (doelen met een hint per laag).
2. **De lange termijn is dieper graven, geen reset.** Op hol-niveau 20, 30 en 40 graaf je een trap naar een nieuwe laag (Kristalader, Verzonken Crypte, Gloophart) met eigen helden, bewoner en val. De nieuwe laag begint leeg, dus je hebt opnieuw de leukste fase (bouwen), maar **er gaat niets weg**: de lagen erboven draaien door en hun goud stroomt mee. Dat is Olafs "opnieuw beginnen met winst" zonder de klacht over rebirth (26 negatieve reviews bij Desktop Defender, Fenna).
3. **Sim met lagen (Bram, GEZIEN, 8 zaden, drempels geijkt):** hol-niveau 9 na 57 min, 12 na 2,0 u (einde demo), 20 na 10,6 u, 30 na 29,8 u, 40 na 57,7 u, 50 na 95,5 u. Langste gat zonder iets nieuws (niveaus en aankopen samen), run versie 2 met de aankleding erbij: tot 20 uur 56 min, 20 tot 40 uur 1,0 u, 40 tot 70 uur 1,5 u, 70 tot 100 uur nog 5,7 u. Na niveau 50 houdt het op.
4. **Versie 2 in vijf keuzes:** (a) Brams prijzen en drempels over; (b) weg zijn levert alles op halve snelheid, ook faam, plafond 12 uur; (c) 15 niveaus geven iets met een prijs en na laag 2 komt aankleding voor goud in de lege bovenste aarde, zodat goud altijd een doel heeft; (d) twee doelen in beeld: het bordje toont het volgende hol-niveau, de kopregel het volgende goud-doel; (e) een tabel in echte dagen. Details in "Versie 2: keuzes".
5. **Demo = hol-niveau 1 tot 12 in ±2 uur**, bijna helemaal met wat al gebouwd is (ridder, dief, magiër, bard, vleermuis, hoedenwand, vaandel komen nu één voor één in plaats van allemaal tegelijk), plus de twee nieuwe dingen die Olaf noemde (één val, één held). Daarna een grijze kaart: "Level 13 and 37 more in the full game".

## Waarom zo (wat de cijfers zeggen)
- **De helft is weg rond 15 uur, 1 op 6 haalt 100 uur** (meetlat Desktop Defender en Rusty's, GEZIEN via Fenna). Dus het duurste en mooiste (nieuwe helden, bewoners, de eerste nieuwe laag) zit vóór 20 uur, en tot 40 uur komt er minstens elk uur iets (run versie 2: langste gat 1,0 u; Fenna adviseert elk uur).
- **Levels zonder nieuws zijn grind** (Spirit City na level 15). Daarom heeft elk hol-niveau een ding met een naam dat je in de strook ziet, en houdt het op bij 50. Geen niveau 51 tot 999 met alleen een getal.
- **Prestige werkt als eerste stap en wordt gehaat als klus.** Wij doen geen reset. Het "opnieuw beginnen" zit in een lege nieuwe laag, terwijl de oude blijft.
- **Prijs mag niet weglopen van het inkomen** (Ropuka's, Tiny Pasture). Hol-niveau stijgt op gevangen helden, niet op goud. Goud blijft voor graven en upgrades; die prijzen kijkt Bram na met zijn verhouding prijs / goud per uur.

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

**Werkweek-rij** (Thijs' voorbeeld: elke werkdag 6 uur open, 's nachts en in het weekend dicht; een nacht of weekend weg telt met het plafond als 12 uur x de factor; GOK, de sim koopt alles meteen):
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
| 22 | mimic (bewoner: speelt schatkist) *(te koop, ±1 u goud)* | 2 | nee | 13,6 u |
| 23 | valluik: een held valt naar de laag eronder *(te koop, ±1 u goud)* | 2 | nee | 15,3 u |
| 24 | keuken (slijm groeit van laarzen) *(te koop, ±1 u goud)* | 2 | nee | 17,1 u |
| 25 | upgrades stap 5 | 2 | nee | 19,0 u |
| 26 | kinderen van aartsvijanden komen ("wants his father's hat back") | 2 | nee | 21,0 u |
| 27 | hoedenpakket 3 (kristal) | 2 | pijplijn | 23,1 u |
| 28 | trek verdwaald (loopt de verkeerde trap af) | 2 | nee | 25,2 u |
| 29 | trofeeënzaal (aartsvijanden aan de wand) *(te koop, ±1 u goud)* | 2 | deels | 27,5 u |
| 30 | **trap naar laag 3: de Verzonken Crypte** | 3 | nee | 29,8 u |
| 31 | archeoloog (onthoudt elke val die hij zag) | 3 | nee | 32,2 u |
| 32 | trol (bewoner: wordt alleen wakker voor aartsvijanden) *(te koop, ±1 u goud)* | 3 | nee | 34,9 u |
| 33 | nep-schat (val, de tegenzet voor de archeoloog) *(te koop, ±1 u goud)* | 3 | nee | 37,4 u |
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
- **Lagen verbinden:** het valluik (niveau 23) laat een held uit laag 1 in laag 2 vallen. De kroniek vertelt het ("Odo fell two floors. He is not happy.").
- **DLC blijft los** (T4): holthema's zijn uiterlijk voor elke laag; een DLC voegt nooit een laag toe die je voor het hol-niveau nodig hebt. Het basisspel is 100% vol te krijgen.

## Tabel per uur (open tijd), met de meetlat van Fenna en echte dagen
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

**In echte dagen** (GOK, zelf gerekend met de regel "weg = halve snelheid, plafond 12 uur", zie "Weg zijn"; een nacht dicht telt dan als 6 uur open). Dag waarop je het punt haalt:
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
1. **Gaten.** Versie 2 nagerekend met Brams sim plus mijn 15 dingen met prijs, 20 kamertjes en lagere factor voor stap 4 tot 6 (GEZIEN, 8 zaden, `data/sim-v2/voortgang-v2-uitkomst.txt`): langste gat tot 20 uur 56 min, 20 tot 40 uur 1,0 u (was 1,6), 40 tot 70 uur 1,5 u (was 2,3), **70 tot 100 uur nog steeds 5,7 u**; bank bij 99 uur ±13.700 (was ±17.600). Hol-niveaus vallen op dezelfde uren (50 op 95,3 u). Mijn regel (tot 20 uur hooguit 2 uur, 20 tot 70 hooguit 3, daarna hooguit 4) is dus gehaald tot 70 uur, **na 70 uur niet** (5,7 u, regel hooguit 4). Waar het gat zit is niet uitgesplitst; na niveau 50 kan het niet helemaal zijn (100 min 95,3 is 4,7 u), dus het zit ook eerder (Bram splitst uit). Wil Thijs dat er ook na 95 uur iets te kopen is, dan moet er een goudput komen die niet opraakt; dat doe ik bewust niet (een eindeloze put zonder nieuws is precies Fenna patroon 2). Wat de sim niet telt vult de gaten nog deels: aartsvijanden (±1 per dag), hun kinderen, bladzijden in het boek, laagsterren.
2. **De sim kent de eigen helden per laag nog niet** (mijnwerker, archeoloog, valluik); elke laag heeft daar dezelfde helden en vallen als laag 1. De sporen 3 en 4 staan als drempel op gevangen helden (GOK).
3. **Kost.** Meer beeld dan Olafs eerste rekensom: 12 bewonersstreken, 4 lagen en nu ook 20 kamertjes aankleding. Olaf rekent do 19 nov opnieuw. Past het niet voor maart: **lancering met laag 1 tot 3 (hol 1 tot 39, ±55 uur, "50+ hours" op de winkelpagina) en laag 4 plus de aankleding van laag 3 en 4 als gratis update in april**; op niveau 39 staat dan eerlijk "Floor 4 comes in a free update".
4. **Voor wie het spel dag en nacht laat draaien is het hol in ±4 dagen af** (tabel echte dagen). Dat is hoe dit soort spel werkt (Fenna's meetlat is Steam-speeltijd, ook als je werkt), en het is twee keer de hoofdinhoud van de toppers (±20 tot 50 uur). Toch is "diep" voor Thijs misschien weken. Hoger zetten kan alleen met hogere drempels, en dan wordt het tussen de niveaus grind (Fenna patroon 2). Ik laat het zo en kijk na de speeltest van za 21 nov wat Thijs ervan vindt.
5. **Echte dagen zijn een GOK.** De sim koopt alles meteen; een echte speler klikt minder, dus het gaat eerder langzamer.

## Vragen aan de anderen (ook in hun berichtenbestand)
- **Bram (versie 3):** reken het voorstel versie 3 na en stel het fijn (weg 0,25 in de sim, uitrekken 1,4 na niveau 20, prijsfactoren per laag, en de dingen in laag 4 terug naar ±1 tot 2 uur sparen met meer dingen of kamertjes), zodat ik de tabellen kan omzetten. Mijn proefrun en het aangepaste script staan in `data/sim-v2/` (`REK` en `UREN` erbij).
- **Bram (versie 2):** ik heb versie 2 zelf in een kopie van je sim gedraaid (`data/sim-v2/`, je bestanden zijn niet veranderd). Wil je (1) `laag_factor_hoog` en kamertjes per laag (in plaats van aan een hol-niveau) echt in `sim.py` zetten, (2) weg zijn op halve snelheid in de sim zetten, zodat de tabel in echte dagen geen GOK meer is, en (3) uitsplitsen waar het gat van 5,7 uur tussen 70 en 100 uur zit?
- **Olaf:** (1) weg op **kwart snelheid** voor goud, hoeden en faam in `voortgang.gd` (factor 0,25, plafond 12 uur blijft; was 0,5 in versie 2); (2) je doelregel is goed, "ready" gaat voor als er maar één plek is; (3) hol-niveau 1 tot 12 met bordje vóór za 21 nov als het past; (4) kosten van alles hierboven do 19 nov, nu met 20 kamertjes; (5) kan de demo-save mee naar het volle spel?
- **Mila en Daan:** het bordje met balkje boven de ingang, het feestje van 1,5 s, welke aankleding er vanaf seconde 1 staat, en de kamertjes in de bovenste aarde (past dat bij "de bovenste helft is lege aarde" van Iris?).
