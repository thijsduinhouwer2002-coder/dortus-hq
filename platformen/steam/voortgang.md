# Hats of the Fallen: voortgang voor ±100 uur (Sanne, game-ontwerper)

Versie 2, 16 nov 2026 ±13:55 UTC (versie 1 ±13:30). Versie 2 verwerkt Brams narekening met lagen (`producten/steam-hol/sim/LAGEN.md`), Iris' keuring 1 (`keuring/2026-11-16-13.md`) en Olafs bouwfeiten van 13:38. Opdracht hoofdchat 16 nov 13:10 (Thijs 13:01: "een diepgaand spel ... level ups enzo om een reden te hebben om te spelen"). Eerste versie gevraagd wo 18 nov 12:00.
Bronnen: Fenna `platformen/succes/diepte-toppers.md` (prestatie-percentages, GEZIEN), Olaf `planning-fest-2027.md` ("Diep spel met level ups"), Brams sim `producten/steam-hol/sim/sim.py voortgang`. Nagerekend met die sim: `platformen/steam/data/voortgang-maak.py` maakt `data/voortgang.json`, uitkomst in `data/voortgang-uitkomst.txt` (GEZIEN, 8 zaden).
Status: **ontwerp versie 2 (versie 1: controleur 16 nov ±13:45 UTC, 11 punten, verwerkt)** (tijden en tellingen klopten; gaten waren te mooi opgeschreven, meetlat-bron, demo-tellers, Gekroonde zonder geluk). Bram rekent na, Olaf zegt do 19 nov wat het kost, Daan en Mila zeggen of het er goed uitziet.

## In het kort
1. **Vier sporen naast elkaar, geen enkel spoor alleen.** Zoals elke topper (Fenna: iets kleins elke paar minuten, iets middelgroots elk uur of elke paar uur, en iets groots): **hol-niveau 1 tot 50** (elk niveau iets nieuws dat je ziet), **Gloop 1 tot 10** (op de hoeden die hij at, onze haak), **niveaus van de andere bewoners**, en **laagsterren** (doelen met een hint per laag).
2. **De lange termijn is dieper graven, geen reset.** Op hol-niveau 20, 30 en 40 graaf je een trap naar een nieuwe laag (Kristalader, Verzonken Crypte, Gloophart) met eigen helden, bewoner en val. De nieuwe laag begint leeg, dus je hebt opnieuw de leukste fase (bouwen), maar **er gaat niets weg**: de lagen erboven draaien door en hun goud stroomt mee. Dat is Olafs "opnieuw beginnen met winst" zonder de klacht over rebirth (26 negatieve reviews bij Desktop Defender, Fenna).
3. **Sim met lagen (Bram, GEZIEN, 8 zaden, drempels geijkt):** hol-niveau 9 na 57 min, 12 na 2,0 u (einde demo), 20 na 10,6 u, 30 na 29,8 u, 40 na 57,7 u, 50 na 95,5 u. Langste gat zonder iets nieuws (niveaus en aankopen samen): tot 20 uur 1,0 u, 20 tot 40 uur 1,6 u, 40 tot 70 uur 2,3 u, 70 tot 100 uur nog 5,7 u (daar komt in versie 2 de aankleding bij, zie "Goud"). Na niveau 50 houdt het op.
4. **Versie 2 in vijf keuzes:** (a) Brams prijzen en drempels over; (b) weg zijn levert alles op halve snelheid, ook faam, plafond 12 uur; (c) 15 niveaus geven iets met een prijs en na laag 2 komt aankleding voor goud in de lege bovenste aarde, zodat goud altijd een doel heeft; (d) twee doelen in beeld: het bordje toont het volgende hol-niveau, de kopregel het volgende goud-doel; (e) een tabel in echte dagen. Details in "Versie 2: keuzes".
5. **Demo = hol-niveau 1 tot 12 in ±2 uur**, bijna helemaal met wat al gebouwd is (ridder, dief, magiër, bard, vleermuis, hoedenwand, vaandel komen nu één voor één in plaats van allemaal tegelijk), plus de twee nieuwe dingen die Olaf noemde (één val, één held). Daarna een grijze kaart: "Level 13 and 37 more in the full game".

## Waarom zo (wat de cijfers zeggen)
- **De helft is weg rond 15 uur, 1 op 6 haalt 100 uur** (meetlat Desktop Defender en Rusty's, GEZIEN via Fenna). Dus het duurste en mooiste (nieuwe helden, bewoners, de eerste nieuwe laag) zit vóór 20 uur, en tot 40 uur komt er ongeveer elke anderhalf uur iets (Fenna adviseert elk uur; dat halen we nog niet, zie "Wat nog niet klopt").
- **Levels zonder nieuws zijn grind** (Spirit City na level 15). Daarom heeft elk hol-niveau een ding met een naam dat je in de strook ziet, en houdt het op bij 50. Geen niveau 51 tot 999 met alleen een getal.
- **Prestige werkt als eerste stap en wordt gehaat als klus.** Wij doen geen reset. Het "opnieuw beginnen" zit in een lege nieuwe laag, terwijl de oude blijft.
- **Prijs mag niet weglopen van het inkomen** (Ropuka's, Tiny Pasture). Hol-niveau stijgt op gevangen helden, niet op goud. Goud blijft voor graven en upgrades; die prijzen kijkt Bram na met zijn verhouding prijs / goud per uur.

## Versie 2: keuzes (16 nov ±13:55 UTC)

### a. Brams prijzen en drempels: over, met één aanpassing
- **Upgrades stap 4, 5, 6: 600 / 1000 / 1600** (was 988 / 2766 / 7745; liep weg van het inkomen, Fenna patroon 1).
- **Graven en upgrade stap 1 tot 3 kosten per laag x 1 / 1,2 / 2,2 / 3,2** (Bram). **Stap 4 tot 6 per laag x 1 / 1,2 / 1,5 / 1,8** (mijn aanpassing): met Brams factor kost stap 6 in laag 4 ±4 uur sparen; zo wordt dat ±2,3 uur (GOK uit Brams goud per uur: laag 3 stap 6 = 2400 / 1000 per uur = 2,4 u, laag 4 stap 6 = 2880 / 1260 = 2,3 u). Laatste stap van een laag mag iets meer kosten, maar niet vier uur. **Nagerekend (GEZIEN, 8 zaden, `data/sim-v2/`):** stap 6 in laag 4 = 2880 goud bij 1237 per uur = 2,3 u sparen; stap 4 en 5 in laag 3 en 4 tussen 0,9 en 1,5 u.
- **Drempels hol-niveau na 20 hoger** (geijkt: 30 op ±2.900, 40 op ±8.300, 50 op ±18.600 gevangen helden). Alle helden blijven tellen, ook die van oude lagen; het bordje toont gewoon een groter getal. Eerlijk en simpel.
- **Gloops toren telt alleen de hoeden die hij zelf at.** Gloopje (de oppas van een oude laag) legt zijn hoeden op de berg. Gloop 10 komt dan op ±65 u in plaats van ±31 u.
- **Luik 500 / 750 / 1000 goud** (= ±1 uur goud van dat moment).

### b. Weg zijn: alles op halve snelheid, ook faam (antwoord op Iris punt 2 en Olaf punt 2)
Regel, voor de speler in één zin: **"While you're away, your hole works at half speed."** Als het spel dicht is, levert de tijd weg goud, hoeden en faam op de helft van het tempo van je laatste uur, met het plafond van 12 uur dat er al is. Een laag die je niet ziet maar die wel open staat, geeft de helft van zijn goud en al zijn faam (Gloopje vangt alles, maar steekt de helft van het goud in zijn eigen zak; dat is de grap in de kroniek).
Waarom zo:
- **Wel faam:** 391 gevangen helden zonder faam voelt als diefstal ("waarom telden die niet?"). Iris heeft gelijk dat het een keuze moet zijn.
- **De helft, niet alles:** met alles telt elke nacht als 12 uur spelen, en dan is het hol voor wie elke avond afsluit op dag 7 af in plaats van dag 12 (GOK, avondspeler met 3 uur open per dag). Met de helft blijft de tabel in open tijd dicht bij de waarheid voor iedereen.
- **Geen straf (T3):** weg zijn levert altijd winst op en je mist niets. Het is alleen minder dan kijken, en dat is eerlijk: als je kijkt, koop je ook.
- **Een plafond voor faam** zit er vanzelf in (Olaf: zelfde 12 uur).
- **Bouw (Olaf, klein):** factor 0,5 op goud, hoeden en faam in `systemen/voortgang.gd`; het "weg geweest"-bericht zegt het gewoon: "While you were away: 303 came, 196 fell. +1476 gold, +196 fame (your hole works at half speed)."

### c. Goud heeft altijd een doel (antwoord op Iris punt 1 en Brams open punt)
Iris rekende goed: in de build van nu is de hele winkel 1048 goud en een nacht weg geeft 2952. Dat lossen drie dingen samen op:
1. **Halve snelheid weg** (b): een nacht wordt ±1.500 goud in de build van nu.
2. **Veel meer om voor te sparen, en het groeit mee:** in versie 1 kost laag 1 alleen al samen ±4.300 goud (graven gang 6 tot 39 ±2.260 met Brams prijzen per gang 16 / 49 / 108, upgrades stap 1 tot 3 1.048, twee nieuwe dingen ±900), en daarna gaan stap 4 tot 6 (2 x 3.200) pas open op hol-niveau 13, 25 en 34. Een nacht weg na de eerste avond (hol ±12, ±335 goud per uur, dus ±2.000 goud) koopt een deel van wat open staat, niet alles, en het volgende doel komt van faam, niet van goud. Elke nieuwe laag kost meer (factor per laag), maar nooit meer dan ±1 tot 2,5 uur sparen.
3. **15 niveaus geven iets met een prijs van ±1 uur goud** (Brams GOK, ik neem hem over): hol-niveau 6, 7, 14, 16, 17, 22, 23, 24, 29, 32, 33, 38, 42, 43 en 45 (een kamer, val of bewoner; gemarkeerd "te koop" in de tabel hieronder). Het niveau maakt het ding zichtbaar met een grijze kaart en een prijs; kopen doe je zelf wanneer je wilt.
4. **Nieuw: aankleding voor goud in de bovenste aarde** (nagerekend in `data/sim-v2/`: met dit en punt 3 gaat de bank bij 99 uur van ±17.600 naar ±13.700 en het langste gat tussen 40 en 70 uur van 2,3 naar 1,5 uur) (antwoord op Brams gat na 70 uur, en ook op Iris' "de bovenste helft is lege aarde"). Vanaf laag 2 kun je per laag **5 holkamertjes** uitgraven in de aarde boven de gang en inrichten: bijvoorbeeld in laag 1 een hoedenkast, een schilderij van je eerste aartsvijand, een fontein met slijm; in de Crypte een orgel; in het Gloophart een slijmbad. **20 stuks**, alleen uiterlijk plus een klein grapje (de fontein spuit soms een hoed), prijs ±1 tot 1,5 uur goud van dat moment, de 5 van laag 4 tussen ±70 en ±100 uur. Zo vult de strook zich met wat jij kocht, zoals bij Rusty's, en is er tot het einde iets om voor te sparen. Verdiend met goud, nooit te koop voor geld (T4); de DLC-holthema's blijven los (die veranderen het hele hol).
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
| 41 | hoedenjager (wil een hoed van de berg terug, lukt nooit, krijgt een wrok) | 4 | nee | 60,9 u |
| 42 | Moeder Gloop (bewoner) *(te koop, ±1 u goud)* | 4 | nee | 64,2 u |
| 43 | gloopbron (val: een gevangen held wordt even een slijmpje) *(te koop, ±1 u goud)* | 4 | nee | 67,7 u |
| 44 | hoedenpakket 5 (legendarisch: hoeden van je oude aartsvijanden als goud) | 4 | pijplijn | 71,2 u |
| 45 | mimic van goud *(te koop, ±1 u goud)* | 4 | nee | 74,9 u |
| 46 | vleermuisfamilie | 4 | deels | 78,6 u |
| 47 | trol met leesbril (leest de kroniek voor) | 4 | nee | 82,3 u |
| 48 | zeldzame held: de Gekroonde (komt zeker binnen ±1 uur na dit niveau en daarna af en toe; geen kans-spul) | 4 | nee | 86,5 u |
| 49 | hoedentroon voor Gloop | 4 | nee | 90,7 u |
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
| 8 | 600 | hoedenworp: gooit een hoed van de berg naar een vluchter | 16,9 u |
| 9 | 1000 | Gloop the Hatted, kroon op de berg | 24,9 u |
| 10 | 3000 | Gloop de Hoedenkoning, gouden slijm | 64,6 u |
Verlies je een gevecht, dan blijft alles staan (plat, "Back in a minute", T3). Gloop verhuist mee naar elke nieuwe laag, met zijn toren en berg; Gloopje past op de laag die je verlaat.

## Spoor 3: de andere bewoners (elk 3 niveaus)
Ze stijgen op hun eigen teller (skelet: helden die hij bang maakte; mimic: helden die hem probeerden te openen; trol: aartsvijanden; Moeder Gloop: slijmpjes die ze opvoedde). Elk niveau een nieuwe streek, klein getekend (een animatie, geen nieuw figuur).
| Bewoner | Niv. 2 | Niv. 3 | Niv. 4 | Sim (GOK, zie onder) |
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
- **De oude laag draait door,** met Gloopje als oppas. Om zuinig te blijven rekent het spel een laag die je niet ziet niet held voor held door, maar geeft het de faam van het laatste uur dat je er keek en **de helft van het goud** (zelfde aanpak als het "weg geweest"-bericht, `voortgang.gd`). Gloopjes hoeden gaan naar de berg, niet naar Gloops toren. Bouwtijd per laag (Bram, GEZIEN): laag 1 8,2 u, laag 2 6,1 u, laag 3 6,9 u, laag 4 7,0 u. Zo is elke laag weer ±6 tot 7 uur bouwen, in plaats van steeds korter (met al het goud werd laag 4 één uur).
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
| 20 | 46% | hol 25, Gloop 8, laag 2 af (18,2 u) | upgrades stap 5, eerste aankleding te koop | kinderen van aartsvijanden (21 u), Gloops kroon (24,9 u) |
| 40 | ±30 tot 35% | hol 33 (34 op 40,1 u), laag 3 af (36,6 u), trol, 7 laagsterren | nep-schat, laatste upgradestap | heks (45,9 u), trap naar het Gloophart op niveau 40 (57,7 u) |
| 70 | ±24% | hol 43, laag 4 af (64,3 u), Moeder Gloop, Gloop 10 (64,6 u) | hoedenpakket 5 (71 u) | mimic van goud (75 u), aankleding van het Gloophart, de Gekroonde (86,5 u) |
| 100 | 17% | hol 50 (95,5 u), alle sporen af | Hol van de Hoedenkoning | geen nieuw niveau meer; wel aartsvijanden en hun kinderen, en de stempel bij 10.000 hoeden (GOK ±200 u) |

**In echte dagen** (GOK, zelf gerekend met de regel "weg = halve snelheid, plafond 12 uur", zie "Weg zijn"; een nacht dicht telt dan als 6 uur open). Dag waarop je het punt haalt:
| Punt (open uren) | Kantoor: spel 8 u per dag open | Avond: 3 u per dag open | Even kijken: 30 min per dag open | Spel en pc altijd aan |
|---|---|---|---|---|
| hol 9 (1 u) | dag 1 | dag 1 | dag 2 | dag 1 |
| hol 15 (5 u) | dag 1 | dag 2 | dag 2 | dag 1 |
| trap naar laag 2 (10,6 u) | dag 2 | dag 2 | dag 3 | dag 1 |
| hol 25 (19 u) | dag 2 | dag 3 | dag 4 | dag 1 |
| trap naar laag 3 (29,8 u) | dag 3 | dag 4 | dag 5 | dag 2 |
| trap naar laag 4 (57,7 u) | dag 5 | dag 7 | dag 10 | dag 3 |
| hol 50 (95,5 u) | dag 8 | dag 12 | dag 16 | dag 4 |
Kanttekening: de sim koopt alles meteen. Wie het spel open laat zonder te klikken koopt niets, dus vangt niet meer en gaat langzamer; en een nacht dicht is waarschijnlijk iets minder waard dan 6 uur open, omdat er dan niets gekocht wordt. De echte dagen liggen dus eerder later dan deze tabel. Eerlijk: voor iemand die het spel dag en nacht laat draaien en vaak klikt, is het hol in ±4 dagen af. Zie "Wat nog niet klopt" punt 4.

## De demo: de eerste 2 uur uitgewerkt
Doel (Fenna): 4 tot 6 kleine feestjes in het eerste half uur tot uur, en na 2 uur zien dat het diep is (Olaf: dichte plekken laten zien). De eerste tien minuten blijven zoals in `features.md` (eerste val ±5 s, vlucht en terugkomer, eerste hoed op Gloop, Hoard-Toucher); de niveaus komen ertussen.
| Tijd (sim) | Wat er gebeurt | Feestje? |
|---|---|---|
| 0 tot 10 min | script van `features.md`; hol-niveau 2 (1 min): Heldenboek met grijze vakjes; ridder (7 min); Gloop 2 (10 min); eerste aankoop | ja: 3 kleine |
| 11 min | vleermuis komt wonen (hol 4) | ja |
| 16 min | dief (hol 5); het boek laat zien "Weak to: Gloop" na zijn eerste vangst | ja |
| 25 min | tweede put of slijm te koop (hol 6): nu kies je waar | ja |
| 33 min | rolsteen (hol 7), goed tegen de ridder | ja |
| 44 min | magiër (hol 8) | ja |
| 55 min | vaandel met de naam van je hol (hol 9) | ja |
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
- **T3 nooit straf, geen grindmuur, geen plicht:** faam gaat nooit omlaag, geen reset, oude lagen draaien door, geen timers. Bijna: zie de gaten na 20 uur hieronder.
- **T4 niets te koop:** alle 50 niveaus, lagen en verdiende uiterlijken zitten in het basisspel; DLC is alleen uiterlijk en eigen hoofdstukken.

## Wat nog niet klopt (eerlijk)
1. **Gaten.** Versie 2 nagerekend met Brams sim plus mijn 15 dingen met prijs, 20 kamertjes en lagere factor voor stap 4 tot 6 (GEZIEN, 8 zaden, `data/sim-v2/voortgang-v2-uitkomst.txt`): langste gat tot 20 uur 56 min, 20 tot 40 uur 1,0 u (was 1,6), 40 tot 70 uur 1,5 u (was 2,3), **70 tot 100 uur nog steeds 5,7 u**; bank bij 99 uur ±13.700 (was ±17.600). Hol-niveaus vallen op dezelfde uren (50 op 95,3 u). Mijn regel (tot 20 uur hooguit 2 uur, 20 tot 70 hooguit 3, daarna hooguit 4) is dus gehaald tot 70 uur. Het gat van 5,7 uur zit waarschijnlijk na niveau 50 (95 u) tot het einde van de sim op 100 u (GOK, niet uitgesplitst): het hol is dan af. Wil Thijs dat er ook na 95 uur iets te kopen is, dan moet er een goudput komen die niet opraakt; dat doe ik bewust niet (een eindeloze put zonder nieuws is precies Fenna patroon 2). Wat de sim niet telt vult de gaten nog deels: aartsvijanden (±1 per dag), hun kinderen, bladzijden in het boek, laagsterren. Wat de sim niet telt vult de gaten deels: aartsvijanden (±1 per dag), hun kinderen, bladzijden in het boek, laagsterren.
2. **De sim kent de eigen helden per laag nog niet** (mijnwerker, archeoloog, valluik); elke laag heeft daar dezelfde helden en vallen als laag 1. De sporen 3 en 4 staan als drempel op gevangen helden (GOK).
3. **Kost.** Meer beeld dan Olafs eerste rekensom: 12 bewonersstreken, 4 lagen en nu ook 20 kamertjes aankleding. Olaf rekent do 19 nov opnieuw. Past het niet voor maart: **lancering met laag 1 tot 3 (hol 1 tot 39, ±55 uur, "50+ hours" op de winkelpagina) en laag 4 plus de aankleding van laag 3 en 4 als gratis update in april**; op niveau 39 staat dan eerlijk "Floor 4 comes in a free update".
4. **Voor wie het spel dag en nacht laat draaien is het hol in ±4 dagen af** (tabel echte dagen). Dat is hoe dit soort spel werkt (Fenna's meetlat is Steam-speeltijd, ook als je werkt), en het is twee keer de hoofdinhoud van de toppers (±20 tot 50 uur). Toch is "diep" voor Thijs misschien weken. Hoger zetten kan alleen met hogere drempels, en dan wordt het tussen de niveaus grind (Fenna patroon 2). Ik laat het zo en kijk na de speeltest van za 21 nov wat Thijs ervan vindt.
5. **Echte dagen zijn een GOK.** De sim koopt alles meteen; een echte speler klikt minder, dus het gaat eerder langzamer.

## Vragen aan de anderen (ook in hun berichtenbestand)
- **Bram:** ik heb versie 2 zelf in een kopie van je sim gedraaid (`data/sim-v2/`, je bestanden zijn niet veranderd). Wil je (1) `laag_factor_hoog` en kamertjes per laag (in plaats van aan een hol-niveau) echt in `sim.py` zetten, (2) weg zijn op halve snelheid in de sim zetten, zodat de tabel in echte dagen geen GOK meer is, en (3) uitsplitsen waar het gat van 5,7 uur tussen 70 en 100 uur zit?
- **Olaf:** (1) halve snelheid weg voor goud, hoeden en faam in `voortgang.gd` (factor 0,5, plafond 12 uur blijft); (2) je doelregel is goed, "ready" gaat voor als er maar één plek is; (3) hol-niveau 1 tot 12 met bordje vóór za 21 nov als het past; (4) kosten van alles hierboven do 19 nov, nu met 20 kamertjes; (5) kan de demo-save mee naar het volle spel?
- **Mila en Daan:** het bordje met balkje boven de ingang, het feestje van 1,5 s, welke aankleding er vanaf seconde 1 staat, en de kamertjes in de bovenste aarde (past dat bij "de bovenste helft is lege aarde" van Iris?).
