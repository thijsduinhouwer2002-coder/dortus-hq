# Hats of the Fallen: voortgang voor ±100 uur (Sanne, game-ontwerper)

Versie 1, 16 nov 2026 ±13:30 UTC. Opdracht hoofdchat 16 nov 13:10 (Thijs 13:01: "een diepgaand spel ... level ups enzo om een reden te hebben om te spelen"). Eerste versie gevraagd wo 18 nov 12:00.
Bronnen: Fenna `platformen/succes/diepte-toppers.md` (prestatie-percentages, GEZIEN), Olaf `planning-fest-2027.md` ("Diep spel met level ups"), Brams sim `producten/steam-hol/sim/sim.py voortgang`. Nagerekend met die sim: `platformen/steam/data/voortgang-maak.py` maakt `data/voortgang.json`, uitkomst in `data/voortgang-uitkomst.txt` (GEZIEN, 8 zaden).
Status: **ontwerp, nog niet nagekeken.** Bram rekent na, Olaf zegt do 19 nov wat het kost, Daan en Mila zeggen of het er goed uitziet.

## In het kort
1. **Vier sporen naast elkaar, geen enkel spoor alleen.** Zoals elke topper (Fenna: klein elke paar minuten, middel elk uur, groot elke paar uur): **hol-niveau 1 tot 50** (elk niveau iets nieuws dat je ziet), **Gloop 1 tot 10** (op de hoeden die hij at, onze haak), **niveaus van de andere bewoners**, en **laagsterren** (doelen met een hint per laag).
2. **De lange termijn is dieper graven, geen reset.** Op hol-niveau 20, 30 en 40 graaf je een trap naar een nieuwe laag (Kristalader, Verzonken Crypte, Gloophart) met eigen helden, bewoner en val. De nieuwe laag begint leeg, dus je hebt opnieuw de leukste fase (bouwen), maar **er gaat niets weg**: de lagen erboven draaien door en hun goud stroomt mee. Dat is Olafs "opnieuw beginnen met winst" zonder de klacht over rebirth (26 negatieve reviews bij Desktop Defender, Fenna).
3. **Sim (GEZIEN, economie van nu plus de effecten van de niveaus):** hol-niveau 9 na 55 min, 12 na 1,9 u (einde demo), 20 na 10,4 u, 30 na 29,8 u, 40 na 57 u, 50 na 94,3 u. 14 ontgrendelingen in het eerste uur, langste gat tot 20 uur 1,7 u. Eerlijk: tussen 20 en 100 uur zijn er nog 13 gaten van 2 tot 3,2 uur (en 5,8 u op het eind); zie "Wat nog niet klopt".
4. **Demo = hol-niveau 1 tot 12 in ±2 uur**, bijna helemaal met wat al gebouwd is (ridder, dief, magiër, bard, vleermuis, hoedenwand, vaandel komen nu één voor één in plaats van allemaal tegelijk), plus de twee nieuwe dingen die Olaf noemde (één val, één held). Daarna een grijze kaart: "Level 13 and 37 more in the full game".

## Waarom zo (wat de cijfers zeggen)
- **De helft is weg rond 15 uur, 1 op 6 haalt 100 uur** (meetlat Desktop Defender en Rusty's, GEZIEN via Fenna). Dus het duurste en mooiste (nieuwe helden, bewoners, de eerste nieuwe laag) zit vóór 20 uur, en tot 40 uur komt er elk uur of twee iets.
- **Levels zonder nieuws zijn grind** (Spirit City na level 15). Daarom heeft elk hol-niveau een ding met een naam dat je in de strook ziet, en houdt het op bij 50. Geen niveau 51 tot 999 met alleen een getal.
- **Prestige werkt als eerste stap en wordt gehaat als klus.** Wij doen geen reset. Het "opnieuw beginnen" zit in een lege nieuwe laag, terwijl de oude blijft.
- **Prijs mag niet weglopen van het inkomen** (Ropuka's, Tiny Pasture). Hol-niveau stijgt op gevangen helden, niet op goud. Goud blijft voor graven en upgrades; die prijzen kijkt Bram na met zijn verhouding prijs / goud per uur.

## Spoor 1: hol-niveau (1 tot 50)
**Waarop:** faam = gevangen helden (1 per held), plus een klein beetje voor verhalen: +5 voor een nieuwe bladzijde in het Heldenboek, +25 voor een afgerekende aartsvijand (zit nog niet in de sim, maakt het hooguit iets sneller). Faam gaat nooit omlaag (T3). Helden die je in een oude laag vangt, tellen mee.
**Wat je ziet:** boven de ingang een klein bordje met het niveau en daaronder een balkje van 1 spelpixel hoog. Bij hover: "Level 5: the Thief. 12 more heroes." Het volgende doel staat dus altijd in beeld, zonder venster.
**Het feestje (klein, standaard zonder geluid):** het bordje wipt, een handvol muntjes springt uit de schat, het nieuwe ding verschijnt met een poef (zelfde soort als bij graven), en één regel in de kroniek ("Hole level 4: a bat moves in."). 1,5 seconde, binnen de strook, niets knippert buiten de strook. Uiterlijk: Mila, keuring Daan.

| Niv. | Wat er bijkomt | Laag | Nu al gebouwd? | Sim (mediaan) |
|---|---|---|---|---|
| 1 | gewone held, Gloop, stekelput, graven, de winkel | 1 | ja | 0 |
| 2 | Heldenboek open, met grijze vakjes ("2 of 11 heroes") | 1 | deels (boek: ontwerp in features.md) | 1 min |
| 3 | ridder komt | 1 | ja | 7 min |
| 4 | vleermuis komt wonen | 1 | ja | 11 min |
| 5 | dief komt | 1 | ja | 16 min |
| 6 | tweede put of tweede slijm te koop | 1 | deels | 25 min |
| 7 | **rolsteen** (nieuwe val, demo) | 1 | nee | 33 min |
| 8 | magiër komt | 1 | ja | 44 min |
| 9 | vaandel met de naam van je hol | 1 | ja | 55 min |
| 10 | **edelman** (nieuwe held, demo): hoge hoed, betaalt 2 goud extra, de zeldzaamste hoed van de demo | 1 | nee | 1,2 u |
| 11 | bard komt (het lied) | 1 | ja | 1,5 u |
| 12 | hoedenwand in de schatkamer | 1 | ja | 1,9 u |
| 13 | upgrades stap 4 (elke lijn gaat naar 6) | 1 | nee | 2,7 u |
| 14 | skelet (bewoner) | 1 | nee | 3,4 u |
| 15 | trek slaapkop (doet een dutje in je hol) | 1 | nee | 4,3 u |
| 16 | slaapkamer (bewoners sneller op) | 1 | nee | 5,3 u |
| 17 | lijmplaat (val, goed tegen de dief) | 1 | nee | 6,5 u |
| 18 | hoedenpakket 2 (helden dragen 8 nieuwe hoeden) | 1 | pijplijn | 7,6 u |
| 19 | trek opschepper | 1 | nee | 8,9 u |
| 20 | **trap naar laag 2: de Kristalader** | 2 | nee | 10,4 u |
| 21 | mijnwerker (held laag 2: graaft om je eerste val heen) | 2 | nee | 11,9 u |
| 22 | mimic (bewoner: speelt schatkist) | 2 | nee | 13,6 u |
| 23 | valluik: een held valt naar de laag eronder | 2 | nee | 15,3 u |
| 24 | keuken (slijm groeit van laarzen) | 2 | nee | 17,1 u |
| 25 | upgrades stap 5 | 2 | nee | 19,0 u |
| 26 | kinderen van aartsvijanden komen ("wants his father's hat back") | 2 | nee | 20,9 u |
| 27 | hoedenpakket 3 (kristal) | 2 | pijplijn | 23,0 u |
| 28 | trek verdwaald (loopt de verkeerde trap af) | 2 | nee | 25,2 u |
| 29 | trofeeënzaal (aartsvijanden aan de wand) | 2 | deels | 27,4 u |
| 30 | **trap naar laag 3: de Verzonken Crypte** | 3 | nee | 29,8 u |
| 31 | archeoloog (onthoudt elke val die hij zag) | 3 | nee | 32,2 u |
| 32 | trol (bewoner: wordt alleen wakker voor aartsvijanden) | 3 | nee | 34,8 u |
| 33 | nep-schat (val, de tegenzet voor de archeoloog) | 3 | nee | 37,2 u |
| 34 | upgrades stap 6 (laatste) | 3 | nee | 39,9 u |
| 35 | hoedenpakket 4 (crypte) | 3 | pijplijn | 42,7 u |
| 36 | heks (betovert Gloops hoeden een minuut tot kikkers, daarna weer hoeden) | 3 | nee | 45,5 u |
| 37 | trek verzamelaar (komt voor één bepaalde hoed op de berg) | 3 | nee | 48,2 u |
| 38 | kaarsenkamer (crypte) | 3 | nee | 51,2 u |
| 39 | skelet in harnas (verdiend uiterlijk, niet te koop) | 3 | nee | 54,2 u |
| 40 | **trap naar laag 4: het Gloophart** (waar slijm vandaan komt) | 4 | nee | 57,0 u |
| 41 | hoedenjager (wil een hoed van de berg terug, lukt nooit, krijgt een wrok) | 4 | nee | 60,2 u |
| 42 | Moeder Gloop (bewoner) | 4 | nee | 63,5 u |
| 43 | gloopbron (val: een gevangen held wordt even een slijmpje) | 4 | nee | 66,9 u |
| 44 | hoedenpakket 5 (legendarisch: hoeden van je oude aartsvijanden als goud) | 4 | pijplijn | 70,4 u |
| 45 | mimic van goud | 4 | nee | 74,0 u |
| 46 | vleermuisfamilie | 4 | deels | 77,7 u |
| 47 | trol met leesbril (leest de kroniek voor) | 4 | nee | 81,4 u |
| 48 | zeldzame held: de Gekroonde (komt alleen als je alle lagen hebt) | 4 | nee | 85,4 u |
| 49 | hoedentroon voor Gloop | 4 | nee | 89,6 u |
| 50 | Hol van de Hoedenkoning: gouden vaandel, titel, prestatie | 4 | nee | 94,3 u |

Samen: 11 heldensoorten (5 nu plus edelman, mijnwerker, archeoloog, heks, hoedenjager, en de Gekroonde als zeldzame), 6 vallen (stekelput, rolsteen, lijmplaat, valluik, nep-schat, gloopbron), 5 bewoners (Gloop, skelet, mimic, trol, Moeder Gloop), 4 lagen, ±40 hoeden in 5 pakketten. Dat is ongeveer de omvang die Olaf al rekende (±10 helden, ±6 vallen, ±40 hoeden, ±3 diepten).

## Spoor 2: Gloop (1 tot 10), op de hoeden die hij at
Dit is onze haak, dus Gloop krijgt het rijkste spoor. Hij stijgt op de hoeden op zijn toren (bron `hoeden_gloop`), en de drempels sluiten aan op de maten van de hoedenberg (`BERG_MAAT`).
| Niv. | Hoeden | Wat je ziet | Sim |
|---|---|---|---|
| 2 | 5 | wiebeltoren: de hoeden wiebelen als hij beweegt | 10 min |
| 3 | 25 | boer: spuugt soms een hoed op de berg | 43 min |
| 4 | 60 | kleverig: een held plakt even (iets meer vangen) | 1,6 u |
| 5 | 100 | Grote Gloop, toren van 5 hoeden | 2,5 u |
| 6 | 200 | hoedendans: jongleert met een hoed als het stil is | 4,5 u |
| 7 | 300 | Gloopje splitst af (kleine tweede slijm, wordt de oppas van een oude laag) | 6,4 u |
| 8 | 600 | hoedenworp: gooit een hoed van de berg naar een vluchter | 12,5 u |
| 9 | 1000 | Gloop the Hatted, kroon op de berg | 20,8 u |
| 10 | 3000 | Gloop de Hoedenkoning, gouden slijm | 61,7 u |
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
- **Openen:** op hol-niveau 20, 30 en 40 verschijnt in de schatkamer een luik. Graven kost goud (prijs: Bram, zo dat het met ±1 uur sparen lukt). Je kiest zelf wanneer; wachten kost niets.
- **De strook toont één laag tegelijk.** Een klein trapje links in de strook wisselt van laag (één klik, gratis, altijd terug).
- **De nieuwe laag begint leeg:** ingang, Gloop en een kale gang. Je graaft en richt opnieuw in. Dat is de winst van "opnieuw beginnen": de leukste uren komen terug, met nieuwe helden die alleen hier komen.
- **De oude laag draait door,** met Gloopje als oppas. Om zuinig te blijven rekent het spel een laag die je niet ziet niet held voor held door, maar geeft het goud, hoeden en faam per uur van het laatste uur dat je er keek (zelfde aanpak als het "weg geweest"-bericht, Bram `voortgang.gd`). Zo bouw je laag 2 met het inkomen van laag 1 erbij, ongeveer twee keer zo snel als laag 1 de eerste keer (GOK, Bram rekent het na).
- **Lagen verbinden:** het valluik (niveau 23) laat een held uit laag 1 in laag 2 vallen. De kroniek vertelt het ("Odo fell two floors. He is not happy.").
- **DLC blijft los** (T4): holthema's zijn uiterlijk voor elke laag; een DLC voegt nooit een laag toe die je voor het hol-niveau nodig hebt. Het basisspel is 100% vol te krijgen.

## Tabel per uur (open tijd), met de meetlat van Fenna
Percentage = hoeveel spelers dit punt halen bij Desktop Defender en Rusty's (GEZIEN bij 1, 5, 10, 20, 50 en 100 uur; 2, 40 en 70 uur zijn tussengerekend, GOK). Of Hats net zo afhaakt is een GOK.
| Uur | Spelers | Wat je dan hebt (sim) | Wat is nieuw rond dit uur | Het volgende doel dat je ziet |
|---|---|---|---|---|
| 1 | 83% | hol 9, Gloop 3, 4 heldensoorten, rolsteen, vleermuis, 2e bewoner, ±36 hoeden | vaandel met je holnaam, ridder, dief, magiër | "Level 10: the Noble" (±15 min) |
| 2 | ±78% | hol 12, Gloop 4, 6 van 11 heldensoorten | bard, hoedenwand, edelman | grijze kaart "Level 13: upgrades tier 4" en Grote Gloop (2,5 u); in de demo "and 37 more in the full game" |
| 5 | 66% | hol 15, Gloop 6, skelet | slaapkop, hoedendans | slaapkamer (5,3 u), eerste laagster, Gloopje (6,4 u) |
| 10 | 57% | hol 19 of 20, Gloop 7, 3 laagsterren | **trap naar de Kristalader** | mijnwerker en mimic, laag 2 inrichten |
| 20 | 46% | hol 25, Gloop 8 of 9, laag 2 ingericht | upgrades stap 5, Gloops kroon | kinderen van aartsvijanden (20,9 u) |
| 40 | ±35% | hol 34, laag 3 open, trol, 7 laagsterren | laatste upgradestap, nep-schat | heks (45,5 u), trap naar het Gloophart op niveau 40 |
| 70 | ±23% | hol 44, laag 4, Moeder Gloop, Gloop 10 | hoedenpakket 5 (je oude aartsvijanden in goud) | mimic van goud, de Gekroonde (85 u) |
| 100 | 17% | hol 50 (94 u), alle sporen af | Hol van de Hoedenkoning | geen nieuw niveau meer; wel aartsvijanden en hun kinderen, en de stempel bij 10.000 hoeden (±300 u) |

## De demo: de eerste 2 uur uitgewerkt
Doel (Fenna): 4 tot 6 kleine feestjes in het eerste half uur tot uur, en na 2 uur zien dat het diep is (Olaf: dichte plekken laten zien). De eerste tien minuten blijven zoals in `features.md` (eerste val ±5 s, vlucht en terugkomer, eerste hoed op Gloop, Hoard-Toucher); de niveaus komen ertussen.
| Tijd (sim) | Wat er gebeurt | Feestje? |
|---|---|---|
| 0 tot 10 min | script van `features.md`; hol-niveau 2 (1 min): Heldenboek met grijze vakjes; ridder (7 min); Gloop 2 (10 min); eerste aankoop | ja: 3 kleine |
| 11 min | vleermuis komt wonen (hol 4) | ja |
| 16 min | dief (hol 5); het boek laat zien "Weak to: Gloop" na zijn eerste vangst | ja |
| 25 min | tweede put of slijm te koop (hol 6): nu kies je waar | ja |
| 33 min | rolsteen (hol 7), goed tegen de ridder | ja |
| 43 min | Gloop 3: spuugt een hoed op de berg | klein |
| 44 min | magiër (hol 8) | ja |
| 55 min | vaandel met de naam van je hol (hol 9) | ja |
| 1,2 u | edelman (hol 10); zijn hoge hoed is het pronkstuk op de toren | ja |
| 1,5 u | bard en zijn lied (hol 11) | ja |
| 1,6 u | Gloop 4, kleverig | klein |
| 1,9 u | hoedenwand (hol 12); daarna staat de grijze kaart in het bordje | ja |
| 2,5 u | Grote Gloop (Gloop 5); in de demo kan Gloop wel door, het hol-niveau niet | |
**Wat de demo laat zien zonder het te tekenen:** in het Heldenboek de lege vakjes ("6 of 11 heroes", "12 of 40 hats", "1 of 4 floors"), in de winkel grijze stappen 4 tot 6 met "Level 13", in de schatkamer een dicht luik met "Level 20". Zo ziet een speler de omvang (Olaf). De demo houdt niet op: helden blijven komen, Gloop groeit door, alleen het hol-niveau stopt bij 12.
**Save mee naar het volle spel:** wie de demo speelde, begint in het volle spel op zijn eigen niveau. Vraag aan Olaf of dat kan met een demo als eigen app-ID (zelfde map voor de save?).
**Let op "armoedig":** dingen later laten komen mag het begin niet kaal maken (Thijs vond het eerste plaatje armoedig). Voorstel: de vaste aankleding van "een vol hol" (spinrag, stutten, wortels, Daans regels) staat er vanaf de eerste seconde; alleen wat leeft of een naam heeft (vleermuis, hoedenwand, vaandel) komt met een niveau. Daan en Mila beslissen.

## Prestaties (meetinstrument, kost bijna niets)
Zes prestaties voor open tijd (1, 5, 10, 20, 50, 100 uur), net als Desktop Defender, zodat we na de lancering zien waar spelers afhaken (advies Fenna). Daarbij: hol-niveau 10, 20, 30, 40, 50; elke laag geopend; Gloop 5 en 10; alle laagsterren. Geen prestatie voor iets dat via geluk loopt.

## Toets T1 tot T4
- **T1 tussendoor:** het volgende doel staat altijd in het bordje; elk bezoek zie je hoe ver het balkje is. Ja.
- **T2 grappig om te onderhouden:** de nieuwe dingen zijn figuren met een grap (heks met kikkers, trol met leesbril, hoedenjager die het nooit lukt). Ja.
- **T3 nooit straf, geen grindmuur, geen plicht:** faam gaat nooit omlaag, geen reset, oude lagen draaien door, geen timers. Bijna: zie de gaten na 20 uur hieronder.
- **T4 niets te koop:** alle 50 niveaus, lagen en verdiende uiterlijken zitten in het basisspel; DLC is alleen uiterlijk en eigen hoofdstukken.

## Wat nog niet klopt (eerlijk)
1. **Gaten na 20 uur.** De sim geeft 13 keer een gat van 2 tot 3,2 uur tussen 20 en 94 uur, en na niveau 50 houdt het op. Mijn regel uit `features.md` (nooit meer dan 2 uur zonder iets nieuws) haal ik dus alleen tot 20 uur. Voorstel: tot 20 uur hooguit 2 uur, van 20 tot 70 uur hooguit 3 uur, daarna mag het. Fenna's advies past daarbij ("na 40 uur goedkoper per uur, maar nooit leeg"), en wat de sim niet telt vult de gaten deels: aartsvijanden (±1 per dag), hun kinderen, nieuwe bladzijden in het boek.
2. **De sim kent de nieuwe inhoud niet.** Lagen, nieuwe helden en bewoners zitten nog niet in `speel()`; de sporen 3 en 4 zijn als drempel op gevangen helden gezet (GOK). Een nieuwe laag die leeg begint, haalt eerst minder helden binnen; dat kan de niveaus erna later maken. Bram, wil je de laag in de sim zetten?
3. **Kost.** Dit is meer beeld dan Olafs eerste rekensom: 12 bewonersstreken en 4 lagen. Olaf rekent do 19 nov opnieuw. Als het niet past voor maart: **mijn voorstel is lancering met laag 1 tot 3 (hol 1 tot 39, ±54 uur, "50+ hours" op de winkelpagina) en laag 4 als gratis update in april**; op niveau 39 staat dan eerlijk "Floor 4 comes in a free update".

## Vragen aan de anderen (ook in hun berichtenbestand)
- **Bram:** reken `data/voortgang.json` na met de prijs / goud per uur-verhouding (Fenna punt 5), en zet als het kan een tweede laag in de sim. Klopt "laag 2 bouwen gaat ±2 keer zo snel"?
- **Olaf:** kosten van de lijst hierboven voor do 19 nov; kan een laag die je niet ziet op een vast tempo doorlopen; kan de demo-save mee naar het volle spel?
- **Mila en Daan:** het bordje met balkje boven de ingang, het feestje van 1,5 s, en welke aankleding er vanaf seconde 1 staat.
